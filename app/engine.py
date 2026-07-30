"""
app/engine.py
Core calculation engine for ASIC efficiency, payback periods, daily economics,
and dynamic client additional charges budget deduction.
"""

from typing import List, Dict, Any, Optional


class BreakevenEngine:
    """Handles breakeven math and power rate thresholds."""

    @staticmethod
    def calculate_max_allowable_efficiency(electricity_cost: float, hash_price: float) -> float:
        """Calculates maximum J/TH efficiency cutoff for non-negative operating margin."""
        if electricity_cost <= 0:
            return 999.0
            
        max_j_th = (hash_price * 1000.0) / (electricity_cost * 24.0)
        return round(max_j_th, 2)


class RecommendationEngine:
    """Ranks and evaluates ASIC models based on efficiency, revenue, power costs, and payback speed."""

    @staticmethod
    def evaluate_miner(
        miner: Dict[str, Any],
        electricity_cost: float,
        hash_price: float,
        capex_budget: Optional[float] = None,
        additional_charges: float = 0.0
    ) -> Optional[Dict[str, Any]]:
        """
        Evaluates miner economics. Subtracts dynamic additional_charges directly 
        from capex_budget to find available hardware capital.
        """
        
        model = miner.get("model", "Unknown")
        hashrate = float(miner.get("hashrate_th", 0))
        power_w = float(miner.get("power_w", 0))
        price_usd = float(miner.get("price_usd", 0))
        
        if hashrate <= 0 or power_w <= 0 or price_usd <= 0:
            return None

        # 1. Efficiency (J/TH)
        efficiency_j_th = power_w / hashrate

        # 2. Daily Unit Economics ($/day per single miner)
        unit_daily_revenue = hashrate * hash_price
        unit_daily_kwh = (power_w / 1000.0) * 24.0
        unit_daily_power_cost = unit_daily_kwh * electricity_cost
        unit_daily_profit = unit_daily_revenue - unit_daily_power_cost

        # 3. Dynamic Budget Deduction Math
        units_possible = 1
        if capex_budget and capex_budget > 0:
            # Net money remaining strictly for hardware purchase
            remaining_hardware_budget = capex_budget - additional_charges
            if remaining_hardware_budget <= 0:
                return None  # Additional charges consume or exceed entire budget
            
            # Floor division to get purchasable units
            units_possible = int(remaining_hardware_budget // price_usd)
            if units_possible < 1:
                return None  # Remaining hardware budget insufficient for even 1 miner

        # Hardware Subtotal & True Project Outlay
        total_hardware_capex = units_possible * price_usd
        total_project_capex = total_hardware_capex + additional_charges

        # Aggregate Fleet Daily Figures
        fleet_daily_revenue = unit_daily_revenue * units_possible
        fleet_daily_power_cost = unit_daily_power_cost * units_possible
        fleet_daily_profit = unit_daily_profit * units_possible

        # 4. Operating Margin (%)
        operating_margin_pct = (fleet_daily_profit / fleet_daily_revenue * 100.0) if fleet_daily_revenue > 0 else 0.0

        # 5. Payback Period (Months) using Total CapEx Outlay (Hardware Total + Additional Charges)
        if fleet_daily_profit <= 0:
            payback_months = 999.0
        else:
            payback_days = total_project_capex / fleet_daily_profit
            payback_months = round(payback_days / 30.4375, 2)

        return {
            "model": model,
            "hashrate_th": hashrate,
            "power_w": power_w,
            "efficiency_j_th": round(efficiency_j_th, 2),
            "unit_price_usd": price_usd,
            "units": units_possible,
            "hardware_capex_usd": round(total_hardware_capex, 2),
            "additional_charges_usd": round(additional_charges, 2),
            "total_capex_usd": round(total_project_capex, 2),
            "daily_revenue_usd": round(fleet_daily_revenue, 2),
            "daily_power_cost_usd": round(fleet_daily_power_cost, 2),
            "daily_profit_usd": round(fleet_daily_profit, 2),
            "operating_margin_pct": round(operating_margin_pct, 1),
            "payback_months": payback_months,
            "is_profitable": fleet_daily_profit > 0
        }


def calculate_payback(
    miners: List[Dict[str, Any]],
    electricity_cost: float,
    hash_price: float,
    capex_budget: Optional[float] = None,
    additional_charges: float = 0.0,
    target_payback_months: Optional[float] = None
) -> Dict[str, Any]:
    """Calculates fleet summary metrics and returns ranked recommendations."""
    results = []
    
    for miner in miners:
        evaluated = RecommendationEngine.evaluate_miner(
            miner=miner,
            electricity_cost=electricity_cost,
            hash_price=hash_price,
            capex_budget=capex_budget,
            additional_charges=additional_charges
        )
        
        if evaluated:
            if target_payback_months and evaluated["payback_months"] > target_payback_months:
                continue
            results.append(evaluated)

    # Sort results by fastest payback period
    results.sort(key=lambda x: x["payback_months"])
    
    max_allowable_j_th = BreakevenEngine.calculate_max_allowable_efficiency(electricity_cost, hash_price)
    
    top_model_name = results[0]["model"] if results else "None"
    top_payback_months = results[0]["payback_months"] if results else 0.0
    top_margin_pct = max([r["operating_margin_pct"] for r in results], default=0.0)
    profitable_count = sum(1 for r in results if r["is_profitable"])

    return {
        "max_allowable_efficiency_j_th": max_allowable_j_th,
        "top_payback_model": top_model_name,
        "top_payback_months": top_payback_months,
        "top_operating_margin_pct": top_margin_pct,
        "total_viable_models": profitable_count,
        "recommendations": results
    }