'use client';

import React, { useState, useEffect } from 'react';
import { fetchMinerRecommendations } from '@/services/api';
import { Zap, DollarSign, AlertTriangle, ShieldCheck, TrendingUp, Award, Truck } from 'lucide-react';

export default function HomePage() {
  const [tariff, setTariff] = useState<number>(0.045);
  const [budget, setBudget] = useState<number>(10000);
  const [additionalCharges, setAdditionalCharges] = useState<number>(500);
  const [data, setData] = useState<any | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const handleFetch = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await fetchMinerRecommendations({
        electricity_cost: tariff,
        capex_budget: budget,
        additional_charges: additionalCharges,
      });
      setData(result);
    } catch (err: any) {
      setError(err.message || 'Failed to calculate payback.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    handleFetch();
  }, []);

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-12 font-sans">
      <div className="max-w-7xl mx-auto space-y-8">
        
        {/* Header */}
        <header className="border-b border-slate-800 pb-6">
          <div className="flex items-center space-x-3">
            <Zap className="h-8 w-8 text-amber-400" />
            <h1 className="text-3xl font-bold tracking-tight text-white">
              MinerPayback <span className="text-amber-400 text-sm font-normal">B2B Efficiency Engine</span>
            </h1>
          </div>
          <p className="mt-2 text-slate-400">
            Efficiency-First ($J/TH$) ASIC recommendation and CapEx recovery platform.
          </p>
        </header>

        {/* Input Parameters Form */}
        <section className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl grid grid-cols-1 md:grid-cols-4 gap-6 items-end">
          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Power Tariff ($/kWh)
            </label>
            <div className="relative">
              <Zap className="absolute left-3 top-3 h-5 w-5 text-slate-500" />
              <input
                type="number"
                step="0.005"
                value={tariff}
                onChange={(e) => setTariff(e.target.value === '' ? 0 : parseFloat(e.target.value))}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-10 pr-4 py-2.5 text-white focus:outline-none focus:ring-2 focus:ring-amber-400"
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Total CapEx Budget ($ USD)
            </label>
            <div className="relative">
              <DollarSign className="absolute left-3 top-3 h-5 w-5 text-slate-500" />
              <input
                type="number"
                step="1000"
                value={budget}
                onChange={(e) => setBudget(e.target.value === '' ? 0 : parseFloat(e.target.value))}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-10 pr-4 py-2.5 text-white focus:outline-none focus:ring-2 focus:ring-amber-400"
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Additional Charges ($ USD)
            </label>
            <div className="relative">
              <Truck className="absolute left-3 top-3 h-5 w-5 text-slate-500" />
              <input
                type="number"
                step="100"
                value={additionalCharges}
                onChange={(e) => setAdditionalCharges(e.target.value === '' ? 0 : parseFloat(e.target.value))}
                placeholder="Dynamic charges"
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-10 pr-4 py-2.5 text-white focus:outline-none focus:ring-2 focus:ring-amber-400"
              />
            </div>
          </div>

          <button
            onClick={handleFetch}
            disabled={loading}
            className="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-semibold py-2.5 px-6 rounded-lg transition duration-200 shadow-lg disabled:opacity-50"
          >
            {loading ? 'Calculating Math...' : 'Run Analysis'}
          </button>
        </section>

        {/* Error Alert */}
        {error && (
          <div className="bg-rose-950/50 border border-rose-800 text-rose-300 p-4 rounded-xl flex items-center space-x-3">
            <AlertTriangle className="h-6 w-6 text-rose-400" />
            <span>{error}</span>
          </div>
        )}

        {/* Executive Dashboard Badges */}
        {data && (
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl flex items-center justify-between shadow-md">
              <div>
                <p className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Max Allowable Cutoff</p>
                <p className="text-2xl font-bold text-amber-400 mt-1">
                  ≤ {data.max_allowable_efficiency_j_th} <span className="text-sm font-normal text-slate-300">J/TH</span>
                </p>
              </div>
              <ShieldCheck className="h-10 w-10 text-amber-400/20" />
            </div>

            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl flex items-center justify-between shadow-md">
              <div>
                <p className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Fastest Payback</p>
                <p className="text-xl font-bold text-white mt-1">
                  {data.top_payback_months} <span className="text-sm font-normal text-slate-300">mos</span>
                </p>
                <p className="text-xs text-amber-400 mt-0.5 truncate max-w-[140px]">{data.top_payback_model}</p>
              </div>
              <Award className="h-10 w-10 text-amber-400/20" />
            </div>

            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl flex items-center justify-between shadow-md">
              <div>
                <p className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Top Fleet Margin</p>
                <p className="text-2xl font-bold text-emerald-400 mt-1">
                  {data.top_operating_margin_pct}%
                </p>
              </div>
              <TrendingUp className="h-10 w-10 text-emerald-400/20" />
            </div>

            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl flex items-center justify-between shadow-md">
              <div>
                <p className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Spot Hash Price</p>
                <p className="text-2xl font-bold text-blue-400 mt-1">
                  ${data.hash_price_used} <span className="text-sm font-normal text-slate-300">/TH/day</span>
                </p>
              </div>
              <DollarSign className="h-10 w-10 text-blue-400/20" />
            </div>
          </div>
        )}

        {/* Table View */}
        {data && data.recommendations && (
          <section className="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden shadow-xl">
            <div className="p-6 border-b border-slate-800 flex justify-between items-center">
              <div>
                <h2 className="text-xl font-bold text-white">Ranked ASIC Recommendations</h2>
                <p className="text-sm text-slate-400 mt-1">
                  Daily revenue, daily power cost, and dynamic CapEx recovery analysis.
                </p>
              </div>
              <div className="bg-slate-950 border border-slate-800 px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-300">
                {data.total_viable_models} Models Found
              </div>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm text-slate-300">
                <thead className="bg-slate-950/60 text-slate-400 uppercase text-xs font-semibold tracking-wider">
                  <tr>
                    <th className="px-5 py-4">ASIC Model</th>
                    <th className="px-5 py-4">Unit Price</th>
                    <th className="px-5 py-4">Efficiency</th>
                    <th className="px-5 py-4">Daily Revenue</th>
                    <th className="px-5 py-4">Daily Power Cost</th>
                    <th className="px-5 py-4">Daily Net Profit</th>
                    <th className="px-5 py-4">Margin (%)</th>
                    <th className="px-5 py-4">Payback Period</th>
                    <th className="px-5 py-4">Units & Total CapEx</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800">
                  {data.recommendations.map((miner: any, index: number) => (
                    <tr key={index} className="hover:bg-slate-800/50 transition">
                      <td className="px-5 py-4 font-semibold text-white">
                        {miner.model}
                      </td>
                      <td className="px-5 py-4 font-mono text-slate-200">
                        ${miner.unit_price_usd?.toLocaleString()}
                      </td>
                      <td className="px-5 py-4 font-mono text-amber-400">
                        {miner.efficiency_j_th} J/TH
                      </td>
                      <td className="px-5 py-4 text-slate-200">
                        ${miner.daily_revenue_usd}/day
                      </td>
                      <td className="px-5 py-4 text-rose-300">
                        -${miner.daily_power_cost_usd}/day
                      </td>
                      <td className="px-5 py-4 font-semibold text-emerald-400">
                        +${miner.daily_profit_usd}/day
                      </td>
                      <td className="px-5 py-4 text-emerald-300 font-medium">
                        {miner.operating_margin_pct}%
                      </td>
                      <td className="px-5 py-4 font-bold text-white">
                        {miner.payback_months} mos
                      </td>
                      <td className="px-5 py-4 font-semibold text-slate-200">
                        {miner.units} units <span className="text-slate-400 font-normal">(${miner.total_capex_usd?.toLocaleString()} CapEx)</span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

      </div>
    </main>
  );
}