"""
app/market.py
Live Bitcoin Market & On-Chain Hashprice Calculator.
Calculates Hashprice ($/TH/day) dynamically from Difficulty and BTC Price.
"""

import httpx
import logging

logger = logging.getLogger(__name__)

# Fallback hash price ($/TH/day) if all live endpoints fail
FALLBACK_HASH_PRICE_PER_TH = 0.052

# Optional: Add your CoinMarketCap key here if you prefer using CMC for BTC price
CMC_API_KEY = ""  # e.g., "your-api-key-here"


async def get_current_hash_price() -> float:
    """
    Returns current Bitcoin hash price in $/TH/day.
    Fetches live Difficulty and BTC Price to compute daily revenue per TH.
    """
    try:
        async with httpx.AsyncClient(timeout=6.0) as client:
            btc_price = await fetch_btc_price(client)
            difficulty = await fetch_btc_difficulty(client)

            if btc_price > 0 and difficulty > 0:
                # Standard On-Chain Hashprice Formula ($/TH/day)
                # Assuming ~3.25 BTC total block reward (3.125 subsidy + avg transaction fees)
                block_reward_btc = 3.25
                sec_per_day = 86400
                th_factor = 1e12
                two_pow_32 = 4294967296

                hash_price_per_th = (
                    (block_reward_btc * sec_per_day * th_factor) / (difficulty * two_pow_32)
                ) * btc_price

                calculated_hashprice = round(hash_price_per_th, 4)
                logger.info(f"[Market Engine] Live Hashprice computed: ${calculated_hashprice}/TH/day (BTC: ${btc_price}, Diff: {difficulty})")
                return calculated_hashprice

    except Exception as e:
        logger.warning(f"[Market Engine Warning] Failed to compute live hashprice: {e}")

    return FALLBACK_HASH_PRICE_PER_TH


async def fetch_btc_price(client: httpx.AsyncClient) -> float:
    """
    Fetches live BTC price in USD.
    Checks CoinMarketCap (if key provided), then Coinbase, then Mempool.space.
    """
    # Option A: CoinMarketCap (If API Key is set)
    if CMC_API_KEY:
        try:
            headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}
            url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC"
            resp = await client.get(url, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return float(data["data"]["BTC"]["quote"]["USD"]["price"])
        except Exception as e:
            logger.warning(f"CoinMarketCap API call failed: {e}")

    # Option B: Coinbase (Free, Fast, No API Key Required)
    try:
        resp = await client.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
        if resp.status_code == 200:
            return float(resp.json()["data"]["amount"])
    except Exception:
        pass

    # Option C: Mempool.space Backup
    try:
        resp = await client.get("https://mempool.space/api/v1/prices")
        if resp.status_code == 200:
            return float(resp.json().get("USD", 0))
    except Exception:
        pass

    return 0.0


async def fetch_btc_difficulty(client: httpx.AsyncClient) -> float:
    """
    Fetches live network difficulty from Blockchain.info.
    Returns exact difficulty number instantly without API keys.
    """
    try:
        resp = await client.get("https://blockchain.info/q/getdifficulty")
        if resp.status_code == 200:
            return float(resp.text.strip())
    except Exception:
        pass

    # Backup: Mempool.space Tip Block Header
    try:
        resp = await client.get("https://mempool.space/api/v1/difficulty-adjustment")
        if resp.status_code == 200:
            data = resp.json()
            # If current difficulty isn't direct, query tip block
            tip_height = await client.get("https://mempool.space/api/blocks/tip/height")
            if tip_height.status_code == 200:
                block_hash = await client.get(f"https://mempool.space/api/block-height/{tip_height.text.strip()}")
                if block_hash.status_code == 200:
                    header = await client.get(f"https://mempool.space/api/block/{block_hash.text.strip()}")
                    if header.status_code == 200:
                        return float(header.json().get("difficulty", 0))
    except Exception:
        pass

    return 0.0