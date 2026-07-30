"""
app/main.py
FastAPI router with direct payload key extraction and cached hash price to prevent delays.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from app.engine import calculate_payback
from app.hardware import get_supported_miners
from app.market import get_current_hash_price
from app.models import MinerRequest, RecommendationResponse

app = FastAPI(
    title="MinerPayback Engine API",
    version="1.3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory cache for hash price to make analysis instant
HASH_PRICE_CACHE = {"price": 0.0334, "last_updated": 0}

async def get_cached_hash_price() -> float:
    now = time.time()
    # Fetch live price only once every 5 minutes (300 seconds)
    if now - HASH_PRICE_CACHE["last_updated"] > 300 or HASH_PRICE_CACHE["price"] == 0:
        try:
            live_price = await get_current_hash_price()
            if live_price > 0:
                HASH_PRICE_CACHE["price"] = live_price
                HASH_PRICE_CACHE["last_updated"] = now
        except Exception:
            pass  # Fall back to cached value if network call hangs
    return HASH_PRICE_CACHE["price"]


@app.get("/")
def read_root():
    return {"status": "ok", "message": "MinerPayback API is running"}


@app.get("/api/v1/market/hash-price")
async def fetch_hash_price():
    hash_price = await get_cached_hash_price()
    return {"hash_price": hash_price}


@app.post("/api/v1/recommend-miners", response_model=RecommendationResponse)
async def recommend_miners(payload: MinerRequest):
    miners = get_supported_miners()
    hash_price = await get_cached_hash_price()
    
    # Explicitly pull parameters from the Pydantic payload model
    elec_cost = payload.electricity_cost
    budget = payload.capex_budget
    extra_charges = payload.additional_charges
    target_payback = payload.target_payback_months

    engine_output = calculate_payback(
        miners=miners,
        electricity_cost=elec_cost,
        hash_price=hash_price,
        capex_budget=budget,
        additional_charges=extra_charges,
        target_payback_months=target_payback
    )
    
    return {
        "status": "success",
        "hash_price_used": hash_price,
        "max_allowable_efficiency_j_th": engine_output["max_allowable_efficiency_j_th"],
        "top_payback_model": engine_output["top_payback_model"],
        "top_payback_months": engine_output["top_payback_months"],
        "top_operating_margin_pct": engine_output["top_operating_margin_pct"],
        "total_viable_models": engine_output["total_viable_models"],
        "recommendations": engine_output["recommendations"]
    }