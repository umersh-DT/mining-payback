export interface RecommendedMiner {
  id: string;
  model: string;
  manufacturer: string;
  efficiency_j_th: number;
  hashrate_th: number;
  power_watts: number;
  unit_capex_usd: number;
  daily_profit_usd: number;
  payback_days: number | null;
  units_in_budget: number | null;
}

// Alias for easy importing
export type Miner = RecommendedMiner;

export interface RecommendationResponse {
  client_tariff_kwh: number;
  spot_hash_price_usd_th: number;
  target_margin_percent: number;
  max_allowable_efficiency_j_th: number;
  total_viable_models: number;
  recommended_miners: RecommendedMiner[];
}