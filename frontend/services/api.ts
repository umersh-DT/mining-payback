const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://mining-payback.onrender.com';

export interface MinerRequestParams {
  electricity_cost: number;
  capex_budget?: number;
  additional_charges?: number;
  target_payback_months?: number;
}

export async function fetchMinerRecommendations(params: MinerRequestParams) {
  const payload = {
    electricity_cost: Number(params.electricity_cost || 0),
    capex_budget: params.capex_budget ? Number(params.capex_budget) : null,
    additional_charges: Number(params.additional_charges || 0),
    target_payback_months: params.target_payback_months ? Number(params.target_payback_months) : null,
  };

  const response = await fetch(`${API_BASE_URL}/api/v1/recommend-miners`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Tunnel-Skip-Anti-Phishing-Page': 'true',
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const errorDetail = await response.text().catch(() => '');
    throw new Error(`Backend Error (${response.status}): ${errorDetail || response.statusText}`);
  }

  return response.json();
}