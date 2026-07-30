"""
app/hardware.py
Standardized ASIC hardware specs dataset extracted from market sources.
Filtered strictly for air-cooled models from approved B2B manufacturers.
"""

from typing import List, Dict, Any

SUPPORTED_MINERS: List[Dict[str, Any]] = [
    # --- BITDEER ---
    {
        "model": "Bitdeer SealMiner A4 Pro Air (336Th)",
        "hashrate_th": 336.0,
        "power_w": 3662.0,
        "price_usd": 3336.0
    },
    {
        "model": "Bitdeer SealMiner A3 Pro Air (290Th)",
        "hashrate_th": 290.0,
        "power_w": 3625.0,
        "price_usd": 4490.0
    },
    {
        "model": "Bitdeer SealMiner A3 Air (260Th)",
        "hashrate_th": 260.0,
        "power_w": 3640.0,
        "price_usd": 3999.0
    },
    {
        "model": "Bitdeer SealMiner A2 Pro Air (255Th)",
        "hashrate_th": 255.0,
        "power_w": 3790.0,
        "price_usd": 3379.0
    },
    {
        "model": "Bitdeer SealMiner A2 (226Th)",
        "hashrate_th": 226.0,
        "power_w": 3730.0,
        "price_usd": 3448.0
    },

    # --- BITMAIN ---
    {
        "model": "Bitmain Antminer S23 (318Th)",
        "hashrate_th": 318.0,
        "power_w": 3498.0,
        "price_usd": 4912.0
    },
    {
        "model": "Bitmain Antminer S21 XP (270Th)",
        "hashrate_th": 270.0,
        "power_w": 3645.0,
        "price_usd": 2883.0
    },
    {
        "model": "Bitmain Antminer S21 Pro (245Th)",
        "hashrate_th": 245.0,
        "power_w": 3510.0,
        "price_usd": 1519.0
    },
    {
        "model": "Bitmain Antminer S21 Pro (234Th)",
        "hashrate_th": 234.0,
        "power_w": 3510.0,
        "price_usd": 1849.0
    },
    {
        "model": "Bitmain Antminer S21+ (235Th)",
        "hashrate_th": 235.0,
        "power_w": 3877.0,
        "price_usd": 1526.0
    },
    {
        "model": "Bitmain Antminer S21+ (225Th)",
        "hashrate_th": 225.0,
        "power_w": 3712.0,
        "price_usd": 1499.0
    },
    {
        "model": "Bitmain Antminer S21+ (216Th)",
        "hashrate_th": 216.0,
        "power_w": 3564.0,
        "price_usd": 1399.0
    },
    {
        "model": "Bitmain Antminer S21 (200Th)",
        "hashrate_th": 200.0,
        "power_w": 3550.0,
        "price_usd": 735.0
    },
    {
        "model": "Bitmain Antminer T21 (190Th)",
        "hashrate_th": 190.0,
        "power_w": 3610.0,
        "price_usd": 539.0
    },
    {
        "model": "Bitmain Antminer S19j XP (151Th)",
        "hashrate_th": 151.0,
        "power_w": 3247.0,
        "price_usd": 123.0
    },
    {
        "model": "Bitmain Antminer S19 XP (140Th)",
        "hashrate_th": 140.0,
        "power_w": 3010.0,
        "price_usd": 109.0
    },
    {
        "model": "Bitmain Antminer S19k Pro (120Th)",
        "hashrate_th": 120.0,
        "power_w": 2760.0,
        "price_usd": 135.0
    },

    # --- MICROBT WHATSMINER ---
    {
        "model": "MicroBT WhatsMiner M79 (920Th)",
        "hashrate_th": 920.0,
        "power_w": 14500.0,
        "price_usd": 14487.0
    },
    {
        "model": "MicroBT WhatsMiner M73S (500Th)",
        "hashrate_th": 500.0,
        "power_w": 7200.0,
        "price_usd": 4977.0
    },
    {
        "model": "MicroBT WhatsMiner M78S (472Th)",
        "hashrate_th": 472.0,
        "power_w": 6550.0,
        "price_usd": 6963.0
    },
    {
        "model": "MicroBT WhatsMiner M6DS+ (540Th)",
        "hashrate_th": 540.0,
        "power_w": 9200.0,
        "price_usd": 4000.0
    },
    {
        "model": "MicroBT WhatsMiner M73 (470Th)",
        "hashrate_th": 470.0,
        "power_w": 7200.0,
        "price_usd": 4517.0
    },
    {
        "model": "MicroBT WhatsMiner M63S++ (464Th)",
        "hashrate_th": 464.0,
        "power_w": 7200.0,
        "price_usd": 10382.0
    },
    {
        "model": "MicroBT WhatsMiner M76S+ (390Th)",
        "hashrate_th": 390.0,
        "power_w": 5200.0,
        "price_usd": 4875.0
    },
    {
        "model": "MicroBT WhatsMiner M63S (390Th)",
        "hashrate_th": 390.0,
        "power_w": 7215.0,
        "price_usd": 4930.0
    },
    {
        "model": "MicroBT WhatsMiner M72S (264Th)",
        "hashrate_th": 264.0,
        "power_w": 4000.0,
        "price_usd": 3999.0
    },
    {
        "model": "MicroBT WhatsMiner M70S (226Th)",
        "hashrate_th": 226.0,
        "power_w": 3140.0,
        "price_usd": 2997.0
    },
    {
        "model": "MicroBT WhatsMiner M66S (298Th)",
        "hashrate_th": 298.0,
        "power_w": 5513.0,
        "price_usd": 4999.0
    },
    {
        "model": "MicroBT WhatsMiner M63 (334Th)",
        "hashrate_th": 334.0,
        "power_w": 6646.0,
        "price_usd": 5692.0
    },
    {
        "model": "MicroBT WhatsMiner M60S++ (226Th)",
        "hashrate_th": 226.0,
        "power_w": 3600.0,
        "price_usd": 2100.0
    },
    {
        "model": "MicroBT WhatsMiner M60S+ (212Th)",
        "hashrate_th": 212.0,
        "power_w": 3600.0,
        "price_usd": 1780.0
    },
    {
        "model": "MicroBT WhatsMiner M60S (186Th)",
        "hashrate_th": 186.0,
        "power_w": 3441.0,
        "price_usd": 2105.0
    },
    {
        "model": "MicroBT WhatsMiner M60 (172Th)",
        "hashrate_th": 172.0,
        "power_w": 3422.0,
        "price_usd": 760.0
    },
    {
        "model": "MicroBT WhatsMiner M56S (212Th)",
        "hashrate_th": 212.0,
        "power_w": 5550.0,
        "price_usd": 1699.0
    },
    {
        "model": "MicroBT Whatsminer M50S (128Th)",
        "hashrate_th": 128.0,
        "power_w": 3276.0,
        "price_usd": 800.0
    },

    # --- CANAAN AVALON ---
    {
        "model": "Canaan Avalon A16XP-300T (300Th)",
        "hashrate_th": 300.0,
        "power_w": 3850.0,
        "price_usd": 4194.0
    },
    {
        "model": "Canaan Avalon A16-282T (282Th)",
        "hashrate_th": 282.0,
        "power_w": 3900.0,
        "price_usd": 4199.0
    },
    {
        "model": "Canaan Avalon A15Pro-221T (221Th)",
        "hashrate_th": 221.0,
        "power_w": 3662.0,  # Extracted from standard specs for 221T series
        "price_usd": 1890.0
    },
    {
        "model": "Canaan Avalon A15Pro-218T (218Th)",
        "hashrate_th": 218.0,
        "power_w": 3662.0,
        "price_usd": 2499.0
    },
    {
        "model": "Canaan Avalon A15XP-206T (206Th)",
        "hashrate_th": 206.0,
        "power_w": 3667.0,
        "price_usd": 1100.0
    },
    {
        "model": "Canaan Avalon A15-194T (194Th)",
        "hashrate_th": 194.0,
        "power_w": 3647.0,
        "price_usd": 1099.0
    },
    {
        "model": "Canaan Avalon A1566 (185Th)",
        "hashrate_th": 185.0,
        "power_w": 3420.0,
        "price_usd": 1170.0
    },
    {
        "model": "Canaan Avalon Q (90Th)",
        "hashrate_th": 90.0,
        "power_w": 1674.0,
        "price_usd": 1298.0
    },
    {
        "model": "Canaan Avalon Mini 3 (37.5Th)",
        "hashrate_th": 37.5,
        "power_w": 800.0,
        "price_usd": 746.0
    }
]


def get_supported_miners() -> List[Dict[str, Any]]:
    """Returns the cleaned list of supported ASIC miners."""
    return SUPPORTED_MINERS