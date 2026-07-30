"""
app/models.py
Updated Pydantic schemas to ensure dynamic additional_charges parses cleanly.
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class MinerRequest(BaseModel):
    electricity_cost: float = Field(default=0.05, alias="electricity_cost")
    capex_budget: Optional[float] = Field(default=None, alias="capex_budget")
    additional_charges: float = Field(default=0.0, alias="additional_charges")
    target_payback_months: Optional[float] = Field(default=None, alias="target_payback_months")

    class Config:
        populate_by_name = True


class MinerRecommendation(BaseModel):
    model: str
    hashrate_th: float
    power_w: float
    efficiency_j_th: float
    unit_price_usd: float
    units: int
    hardware_capex_usd: float
    additional_charges_usd: float
    total_capex_usd: float
    daily_revenue_usd: float
    daily_power_cost_usd: float
    daily_profit_usd: float
    operating_margin_pct: float
    payback_months: float
    is_profitable: bool


class RecommendationResponse(BaseModel):
    status: str
    hash_price_used: float
    max_allowable_efficiency_j_th: float
    top_payback_model: str
    top_payback_months: float
    top_operating_margin_pct: float
    total_viable_models: int
    recommendations: List[MinerRecommendation]