"""Genereer de synthetische Fontasya-jaarset vanaf de commandline.

Voorbeelden:
    python generate_fontasya_jaarset.py --help
    python generate_fontasya_jaarset.py --customers 200 --no-zip
    python generate_fontasya_jaarset.py --force
"""

from __future__ import annotations

import argparse
import calendar
import gc
import hashlib
import json
import os
import random
import shutil
import stat
import sys
import time
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path

np = None
pd = None


@dataclass
class Config:
    seed: int = 20260917
    year: int = 2026
    n_customers: int = 30_000
    pv_share: float = 0.45
    own_electricity_share: float = 0.60
    wind_share_of_own: float = 0.65
    output_dir: str = "fontasya_representatieve_jaarset_30000_klanten"
    csv_compresslevel: int = 1


_quiet = False


def log(message: str) -> None:
    if not _quiet:
        print(f"{time.strftime('%H:%M:%S')}  {message}", flush=True)


def require_runtime_dependencies() -> None:
    global np, pd
    try:
        import numpy as numpy_mod
        import pandas as pandas_mod
    except ImportError as exc:
        print(
            "Dit script heeft numpy en pandas nodig in dezelfde Python als waarmee je het start.\n"
            f"  {sys.executable} -m pip install numpy pandas\n"
            f"Fout: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc
    np = numpy_mod
    pd = pandas_mod


def days_in_year(year: int) -> int:
    return 366 if calendar.isleap(year) else 365


def year_dates(year: int):
    return pd.date_range(f"{year}-01-01", f"{year}-12-31", freq="D")


def id_width(n: int, minimum: int = 5) -> int:
    return max(minimum, len(str(n)))


def ean13(seed: str) -> str:
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    digits = "".join(str(int(ch, 16) % 10) for ch in digest)
    base = ("871" + digits)[:12]
    weighted = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(base))
    return base + str((10 - weighted % 10) % 10)


def stable_coordinates(seed: str, lat: float = 51.48, lon: float = 5.66, spread: float = 0.45) -> tuple[float, float]:
    h = int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16], 16)
    rng = np.random.default_rng(h % (2**32))
    return round(lat + rng.uniform(-spread, spread), 6), round(lon + rng.uniform(-spread, spread), 6)


def write_gzip_csv(df, path: Path, compresslevel: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, compression={"method": "gzip", "compresslevel": compresslevel})


def create_dimensions(cfg: Config, rng) -> tuple:
    width = id_width(cfg.n_customers)
    customer_ids = np.array([f"CUST{i:0{width}d}" for i in range(1, cfg.n_customers + 1)])
    segments = np.array(["Single", "Couple", "Family", "Senior"])
    cities = np.array(["Helmond", "Eindhoven", "Deurne", "Venray", "Weert", "Roermond", "Tilburg", "Den Bosch"])
    household_segment = rng.choice(segments, cfg.n_customers, p=[0.22, 0.31, 0.32, 0.15])
    city = rng.choice(cities, cfg.n_customers)
    coordinates = np.array([stable_coordinates(cid) for cid in customer_ids])
    has_pv = rng.random(cfg.n_customers) < cfg.pv_share

    electricity_targets = np.select(
        [household_segment == "Single", household_segment == "Couple", household_segment == "Family", household_segment == "Senior"],
        [2100, 2750, 3750, 2450],
    ).astype(float) * rng.lognormal(0, 0.10, cfg.n_customers)
    gas_targets = np.select(
        [household_segment == "Single", household_segment == "Couple", household_segment == "Family", household_segment == "Senior"],
        [650, 1050, 1450, 1150],
    ).astype(float) * rng.lognormal(0, 0.12, cfg.n_customers)

    customers = pd.DataFrame(
        {
            "customer_id": customer_ids,
            "customer_token": [hashlib.sha256(cid.encode("utf-8")).hexdigest()[:18] for cid in customer_ids],
            "postcode4": rng.integers(1000, 10000, cfg.n_customers),
            "city": city,
            "region": "NL_ZUID",
            "household_segment": household_segment,
            "has_pv": has_pv,
            "ean_code": [ean13(cid) for cid in customer_ids],
            "latitude": coordinates[:, 0],
            "longitude": coordinates[:, 1],
            "annual_electricity_target_kwh": electricity_targets.round(2),
            "annual_gas_target_m3": gas_targets.round(2),
        }
    )

    contract_types = rng.choice(["FLEX", "FIXED_1Y", "FIXED_3Y", "FIXED_5Y"], cfg.n_customers, p=[0.28, 0.38, 0.22, 0.12])
    start_min = pd.Timestamp("2024-01-01").value // 10**9
    start_max = pd.Timestamp("2026-01-01").value // 10**9
    starts = pd.to_datetime(rng.integers(start_min, start_max, cfg.n_customers), unit="s").normalize()
    durations = np.select(
        [contract_types == "FLEX", contract_types == "FIXED_1Y", contract_types == "FIXED_3Y", contract_types == "FIXED_5Y"],
        [0, 1, 3, 5],
    )
    ends = [pd.NaT if years == 0 else start + pd.DateOffset(years=int(years)) for start, years in zip(starts, durations)]

    electricity_rates = np.select(
        [contract_types == "FLEX", contract_types == "FIXED_1Y", contract_types == "FIXED_3Y", contract_types == "FIXED_5Y"],
        [0.295, 0.283, 0.302, 0.319],
    ) + rng.normal(0, 0.006, cfg.n_customers)
    gas_rates = np.select(
        [contract_types == "FLEX", contract_types == "FIXED_1Y", contract_types == "FIXED_3Y", contract_types == "FIXED_5Y"],
        [1.34, 1.29, 1.37, 1.45],
    ) + rng.normal(0, 0.025, cfg.n_customers)

    contracts = pd.DataFrame(
        {
            "contract_id": [f"CON{i:0{width}d}" for i in range(1, cfg.n_customers + 1)],
            "customer_id": customer_ids,
            "contract_type": contract_types,
            "start_date": starts.date.astype(str),
            "end_date": [x.date().isoformat() if pd.notna(x) else "" for x in ends],
            "electricity_rate_eur_kwh": electricity_rates.round(4),
            "gas_rate_eur_m3": gas_rates.round(4),
            "monthly_service_fee_eur": (8.95 + rng.normal(0, 0.35, cfg.n_customers)).round(2),
            "status": "ACTIVE",
            "ean_code": customers["ean_code"],
            "latitude": customers["latitude"],
            "longitude": customers["longitude"],
        }
    )

    pv_customers = customers.loc[customers["has_pv"], ["customer_id", "ean_code", "latitude", "longitude"]].reset_index(drop=True)
    pv_width = id_width(len(pv_customers))
    pv_assets = pd.DataFrame(
        {
            "pv_id": [f"PV{i:0{pv_width}d}" for i in range(1, len(pv_customers) + 1)],
            "customer_id": pv_customers["customer_id"],
            "capacity_kwp": rng.gamma(4.5, 1.25, len(pv_customers)).clip(2.0, 18.0).round(1),
            "panel_count": rng.choice([8, 10, 12, 14, 16, 18, 20, 24, 28, 32], len(pv_customers)),
            "orientation": rng.choice(["South", "East West", "South East", "South West"], len(pv_customers), p=[0.42, 0.28, 0.15, 0.15]),
            "installation_year": rng.integers(2016, cfg.year + 1, len(pv_customers)),
            "ean_code": pv_customers["ean_code"],
            "latitude": pv_customers["latitude"],
            "longitude": pv_customers["longitude"],
        }
    )
    return customers, contracts, pv_assets


def create_market_and_assets(cfg: Config, rng) -> tuple:
    dates = year_dates(cfg.year)
    n = len(dates)
    t = np.arange(n)
    temperature = 10 + 8 * np.sin(2 * np.pi * (t - 110) / 365) + rng.normal(0, 2.3, n)
    irradiance = np.clip(280 + 260 * np.sin(2 * np.pi * (t - 80) / 365) + rng.normal(0, 85, n), 5, 850)
    wind_speed = np.clip(6.2 + 1.8 * np.sin(2 * np.pi * (t + 15) / 38) + rng.normal(0, 1.4, n), 1, 16)
    cloud_cover = np.clip(65 - irradiance / 12 + rng.normal(0, 10, n), 5, 100)

    weather = pd.DataFrame(
        {
            "weather_id": [f"WTH{i:04d}" for i in range(1, n + 1)],
            "date": dates.date.astype(str),
            "region": "NL_ZUID",
            "temperature_c": temperature.round(2),
            "wind_speed_ms": wind_speed.round(2),
            "solar_irradiance_wm2": irradiance.round(1),
            "cloud_cover_pct": cloud_cover.round(1),
            "wind_capacity_factor_forecast": np.clip((wind_speed - 2) / 12 + rng.normal(0, 0.04, n), 0, 0.92).round(3),
            "solar_capacity_factor_forecast": np.clip(irradiance / 950 + rng.normal(0, 0.03, n), 0, 0.85).round(3),
            "ean_code": ean13("NL_ZUID_WEATHER"),
            "latitude": 51.48,
            "longitude": 5.66,
        }
    )

    load = 235_000 + (temperature < 5) * 18_000 + 18_000 * np.sin(2 * np.pi * (t - 5) / 7) + rng.normal(0, 7_000, n)
    day_ahead = 70 + (load - 235_000) / 2200 + (1 - irradiance / 850) * 9 + (1 - wind_speed / 16) * 11 + rng.normal(0, 5, n)
    gas_spot = 48 + (10 - temperature) * 1.1 + rng.normal(0, 3, n)
    market = pd.DataFrame(
        {
            "market_id": [f"MKT{i:04d}" for i in range(1, n + 1)],
            "date": dates.date.astype(str),
            "bidding_zone": "NL",
            "day_ahead_eur_mwh": day_ahead.round(2),
            "intraday_eur_mwh": (day_ahead + rng.normal(0, 3, n)).round(2),
            "imbalance_eur_mwh": (day_ahead + rng.normal(0, 10, n)).round(2),
            "system_load_mwh": load.round(1),
            "gas_spot_eur_mwh": gas_spot.round(2),
            "gas_forward_1y_eur_mwh": (gas_spot + 3 + rng.normal(0, 1.2, n)).round(2),
            "ean_code": ean13("NL_MARKET"),
            "latitude": 52.132633,
            "longitude": 5.291266,
        }
    )

    network = pd.DataFrame(
        {
            "network_id": [f"NET{i:04d}" for i in range(1, n + 1)],
            "date": dates.date.astype(str),
            "region": "NL_ZUID",
            "distribution_eur_mwh": (41.5 + rng.normal(0, 0.5, n)).round(2),
            "transport_eur_mwh": (14.2 + rng.normal(0, 0.25, n)).round(2),
            "loss_factor": np.clip(0.021 + rng.normal(0, 0.002, n), 0.01, 0.04).round(4),
            "balancing_cost_eur_mwh": np.maximum(0, rng.normal(4.5, 2, n)).round(2),
            "congestion_index": np.clip((load - 205_000) / 90_000 + rng.normal(0, 0.05, n), 0, 1).round(3),
            "ean_code": ean13("NL_ZUID_GRID"),
            "latitude": 51.48,
            "longitude": 5.66,
        }
    )

    assets = pd.DataFrame(
        [
            ["GEN001", "Windpark Noord", "wind", "NL_NOORD", 14.0, 2018, 27.0, 8.0, 24.0, 1.10],
            ["GEN002", "Windpark Maas", "wind", "NL_ZUID", 12.0, 2020, 25.0, 5.0, 21.0, 0.90],
            ["GEN003", "Windpark Peel", "wind", "NL_ZUID", 10.0, 2022, 24.0, 4.5, 18.0, 0.80],
            ["GEN004", "Zonnepark Helios", "zon", "NL_ZUID", 17.0, 2021, 22.0, 3.2, 15.0, 0.60],
            ["GEN005", "Zonnepark Kempen", "zon", "NL_ZUID", 13.0, 2023, 20.0, 2.0, 11.0, 0.45],
        ],
        columns=["installation_id", "installation_name", "technology", "region", "capacity_mw", "commissioning_year", "depreciation_years", "grid_connection_cost_eur_mwh", "capex_million_eur", "annual_opex_million_eur"],
    )
    asset_coordinates = np.array([stable_coordinates(asset_id, 51.55, 5.65, 0.35) for asset_id in assets["installation_id"]])
    assets["ean_code"] = assets["installation_id"].map(ean13)
    assets["latitude"] = asset_coordinates[:, 0]
    assets["longitude"] = asset_coordinates[:, 1]

    production_rows = []
    for _, asset in assets.iterrows():
        factors = weather["wind_capacity_factor_forecast"].to_numpy() if asset["technology"] == "wind" else weather["solar_capacity_factor_forecast"].to_numpy()
        for i, dt in enumerate(dates):
            availability = float(np.clip(0.965 + rng.normal(0, 0.012), 0.85, 1.00))
            forecast = asset["capacity_mw"] * 24 * factors[i]
            actual = max(0, forecast * availability * (1 + rng.normal(0, 0.06)))
            production_rows.append([f"PRD{len(production_rows)+1:06d}", dt.date().isoformat(), asset["installation_id"], asset["technology"], forecast, actual, availability])
    production = pd.DataFrame(production_rows, columns=["production_id", "date", "installation_id", "technology", "forecast_mwh", "actual_mwh", "availability_pct"])
    return weather, market, network, assets, production


def create_customer_daily_partitions(cfg: Config, out: Path, customers, pv_assets, weather, market, rng):
    electricity_dir = out / "electricity_consumption_daily"
    gas_dir = out / "gas_consumption_daily"
    feedin_dir = out / "pv_feedin_daily"
    for directory in [electricity_dir, gas_dir, feedin_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    dates = year_dates(cfg.year)
    n_days = len(dates)
    t = np.arange(n_days)
    winter_weights = 1 + 0.48 * np.cos(2 * np.pi * (t - 15) / 365)
    winter_weights = winter_weights / winter_weights.sum()
    solar_weights = weather["solar_irradiance_wm2"].to_numpy()
    solar_weights = solar_weights / solar_weights.sum()
    temperatures = weather["temperature_c"].to_numpy()
    gas_weights_year = np.maximum(0.05, 12 - temperatures) ** 1.25
    gas_weights_year = gas_weights_year / gas_weights_year.sum()

    customer_ids = customers["customer_id"].to_numpy()
    customer_eans = customers["ean_code"].to_numpy()
    customer_lat = customers["latitude"].to_numpy()
    customer_lon = customers["longitude"].to_numpy()
    annual_electricity = customers["annual_electricity_target_kwh"].to_numpy()
    annual_gas = customers["annual_gas_target_m3"].to_numpy()

    pv_positions = np.flatnonzero(customers["has_pv"].to_numpy())
    pv_customer_ids = pv_assets["customer_id"].to_numpy()
    pv_capacity = pv_assets["capacity_kwp"].to_numpy()
    pv_eans = pv_assets["ean_code"].to_numpy()
    pv_lat = pv_assets["latitude"].to_numpy()
    pv_lon = pv_assets["longitude"].to_numpy()

    daily_aggregates = []
    for month in range(1, 13):
        date_positions = np.flatnonzero(dates.month == month)
        monthly_dates = dates[date_positions]
        days = len(date_positions)
        started = time.perf_counter()
        log(f"Maand {month:02d}/12: {days} dagen, {cfg.n_customers:,} klanten schrijven...")

        electricity_weight = winter_weights[date_positions]
        electricity_month_share = float(electricity_weight.sum())
        electricity_noise = rng.lognormal(0, 0.10, (cfg.n_customers, days))
        electricity_noise = electricity_noise / electricity_noise.sum(axis=1, keepdims=True) * electricity_month_share
        electricity_values = annual_electricity[:, None] * (0.72 * electricity_weight[None, :] + 0.28 * electricity_noise)

        gas_weight = gas_weights_year[date_positions]
        gas_month_share = float(gas_weight.sum())
        gas_noise = rng.lognormal(0, 0.13, (cfg.n_customers, days))
        gas_noise = gas_noise / gas_noise.sum(axis=1, keepdims=True) * gas_month_share
        gas_values = annual_gas[:, None] * (0.80 * gas_weight[None, :] + 0.20 * gas_noise)

        electricity = pd.DataFrame(
            {
                "customer_id": np.repeat(customer_ids, days),
                "date": np.tile(monthly_dates.date.astype(str), cfg.n_customers),
                "electricity_consumption_kwh": electricity_values.ravel().round(3),
                "ean_code": np.repeat(customer_eans, days),
                "latitude": np.repeat(customer_lat, days),
                "longitude": np.repeat(customer_lon, days),
            }
        )
        gas = pd.DataFrame(
            {
                "customer_id": np.repeat(customer_ids, days),
                "date": np.tile(monthly_dates.date.astype(str), cfg.n_customers),
                "gas_consumption_m3": gas_values.ravel().round(3),
                "ean_code": np.repeat(customer_eans, days),
                "latitude": np.repeat(customer_lat, days),
                "longitude": np.repeat(customer_lon, days),
            }
        )
        write_gzip_csv(electricity, electricity_dir / f"year={cfg.year}_month={month:02d}.csv.gz", cfg.csv_compresslevel)
        write_gzip_csv(gas, gas_dir / f"year={cfg.year}_month={month:02d}.csv.gz", cfg.csv_compresslevel)

        pv_weight = solar_weights[date_positions]
        pv_month_share = float(pv_weight.sum())
        n_pv = len(pv_customer_ids)
        if n_pv == 0:
            pv_generation = np.zeros((0, days))
        else:
            pv_noise = rng.lognormal(0, 0.08, (n_pv, days))
            pv_noise = pv_noise / pv_noise.sum(axis=1, keepdims=True) * pv_month_share
            pv_generation = (pv_capacity * 900)[:, None] * (0.86 * pv_weight[None, :] + 0.14 * pv_noise)
        self_consumption = np.minimum(pv_generation, electricity_values[pv_positions, :])
        exported = np.maximum(0, pv_generation - electricity_values[pv_positions, :])
        feedin_rates = np.maximum(0.025, market.loc[date_positions, "day_ahead_eur_mwh"].to_numpy() / 1000 - 0.015)

        feedin = pd.DataFrame(
            {
                "customer_id": np.repeat(pv_customer_ids, days),
                "date": np.tile(monthly_dates.date.astype(str), len(pv_customer_ids)),
                "pv_generation_kwh": pv_generation.ravel().round(3),
                "self_consumption_kwh": self_consumption.ravel().round(3),
                "exported_kwh": exported.ravel().round(3),
                "feedin_rate_eur_kwh": np.tile(feedin_rates, len(pv_customer_ids)).round(4),
                "ean_code": np.repeat(pv_eans, days),
                "latitude": np.repeat(pv_lat, days),
                "longitude": np.repeat(pv_lon, days),
            }
        )
        feedin["feedin_value_eur"] = (feedin["exported_kwh"] * feedin["feedin_rate_eur_kwh"]).round(4)
        write_gzip_csv(feedin, feedin_dir / f"year={cfg.year}_month={month:02d}.csv.gz", cfg.csv_compresslevel)

        daily_aggregates.append(
            pd.DataFrame(
                {
                    "date": monthly_dates.date.astype(str),
                    "electricity_consumption_kwh": electricity_values.sum(axis=0),
                    "gas_consumption_m3": gas_values.sum(axis=0),
                    "pv_generation_kwh": pv_generation.sum(axis=0),
                    "self_consumption_kwh": self_consumption.sum(axis=0),
                    "exported_kwh": exported.sum(axis=0),
                    "feedin_value_eur": (exported * feedin_rates[None, :]).sum(axis=0),
                }
            )
        )
        del electricity, gas, feedin, electricity_values, gas_values, pv_generation, self_consumption, exported
        gc.collect()
        log(f"Maand {month:02d}/12 klaar in {time.perf_counter() - started:.1f}s")
    return pd.concat(daily_aggregates, ignore_index=True)


def make_small_tables(cfg: Config, customers, contracts, pv_assets, market, production, assets, daily, rng) -> dict:
    annual_demand_mwh = customers["annual_electricity_target_kwh"].sum() / 1000
    target_own_mwh = annual_demand_mwh * cfg.own_electricity_share
    for technology, share in [("wind", cfg.wind_share_of_own), ("zon", 1 - cfg.wind_share_of_own)]:
        mask = production["technology"] == technology
        factor = target_own_mwh * share / production.loc[mask, "actual_mwh"].sum()
        production.loc[mask, "actual_mwh"] = (production.loc[mask, "actual_mwh"] * factor).round(3)
        production.loc[mask, "forecast_mwh"] = (production.loc[mask, "forecast_mwh"] * factor).round(3)
    production = production.merge(assets[["installation_id", "ean_code", "latitude", "longitude", "grid_connection_cost_eur_mwh"]], on="installation_id", how="left")
    production["variable_cost_eur_mwh"] = np.where(production["technology"] == "wind", 5.8, 4.2)
    production["total_cost_eur_mwh"] = (production["variable_cost_eur_mwh"] + production["grid_connection_cost_eur_mwh"] + np.where(production["technology"] == "wind", 27, 24)).round(2)

    production_daily = production.groupby(["date", "technology"], as_index=False)["actual_mwh"].sum().pivot(index="date", columns="technology", values="actual_mwh").reset_index().fillna(0)
    daily = daily.merge(production_daily, on="date").merge(market[["date", "day_ahead_eur_mwh", "gas_spot_eur_mwh"]], on="date")
    daily["demand_mwh"] = daily["electricity_consumption_kwh"] / 1000
    daily["own_mwh"] = daily["wind"] + daily["zon"]
    daily["pv_customer_mwh"] = daily["exported_kwh"] / 1000
    daily["market_purchase_mwh"] = np.maximum(0, daily["demand_mwh"] - daily["own_mwh"] - daily["pv_customer_mwh"])
    daily["gas_purchase_m3"] = daily["gas_consumption_m3"]

    trades = []
    for _, row in daily.iterrows():
        trades.extend(
            [
                [f"TRADE{len(trades)+1:05d}", row["date"], "ELECTRICITY", "OWN_WIND", row["wind"], 0.0, "INTERNAL_ASSET"],
                [f"TRADE{len(trades)+1:05d}", row["date"], "ELECTRICITY", "OWN_SOLAR", row["zon"], 0.0, "INTERNAL_ASSET"],
                [f"TRADE{len(trades)+1:05d}", row["date"], "ELECTRICITY", "CUSTOMER_PV_FEEDIN", row["pv_customer_mwh"], max(0.025, row["day_ahead_eur_mwh"] / 1000 - 0.015) * 1000, "HOUSEHOLD_PV_POOL"],
                [f"TRADE{len(trades)+1:05d}", row["date"], "ELECTRICITY", "MARKET_BALANCING", row["market_purchase_mwh"], row["day_ahead_eur_mwh"], "DAY_AHEAD_MARKET"],
                [f"TRADE{len(trades)+1:05d}", row["date"], "GAS", "EUROPEAN_GAS_MARKET", row["gas_purchase_m3"], row["gas_spot_eur_mwh"], "EU_GAS_HUB"],
            ]
        )
    procurement = pd.DataFrame(trades, columns=["trade_id", "date", "commodity", "source_type", "volume", "unit_price", "counterparty_token"])

    portfolio_rows = []
    for contract_type in ["FLEX", "FIXED_1Y", "FIXED_3Y", "FIXED_5Y"]:
        subset = contracts[contracts["contract_type"] == contract_type]
        customer_subset = customers[customers["customer_id"].isin(subset["customer_id"])]
        portfolio_rows.append(
            [
                f"PORT_{contract_type}",
                contract_type,
                len(subset),
                round(customer_subset["annual_electricity_target_kwh"].sum(), 2),
                round(customer_subset["annual_gas_target_m3"].sum(), 2),
                round(subset["electricity_rate_eur_kwh"].mean(), 4),
                round(subset["gas_rate_eur_m3"].mean(), 4),
                round(rng.uniform(0.02, 0.07), 4),
                ean13(f"PORT_{contract_type}"),
                51.48,
                5.66,
            ]
        )
    portfolio = pd.DataFrame(portfolio_rows, columns=["portfolio_id", "contract_type", "active_customers", "annual_electricity_kwh", "annual_gas_m3", "avg_electricity_rate_eur_kwh", "avg_gas_rate_eur_m3", "estimated_churn_risk", "ean_code", "latitude", "longitude"])

    pricing_rows = []
    for month in range(1, 13):
        subset = daily[pd.to_datetime(daily["date"]).dt.month == month]
        electricity_cost = subset["day_ahead_eur_mwh"].mean() / 1000
        gas_cost = subset["gas_spot_eur_mwh"].mean() / 10
        for contract_type, risk in [("FLEX", 0.010), ("FIXED_1Y", 0.017), ("FIXED_3Y", 0.032), ("FIXED_5Y", 0.050)]:
            pricing_rows.append([f"PRICE_{month:02d}_{contract_type}", f"RUN_{cfg.year}_{month:02d}", cfg.year, month, contract_type, round(electricity_cost + 0.055 + risk, 4), round(gas_cost + 0.18 + risk * 2, 4), round(0.055 + risk, 4), round(0.035 + risk, 4), "MODEL_V1.0", "APPROVED"])
    pricing = pd.DataFrame(pricing_rows, columns=["price_recommendation_id", "pricing_run_id", "year", "month", "contract_type", "recommended_electricity_eur_kwh", "recommended_gas_eur_m3", "risk_markup_eur_kwh", "target_margin_eur_kwh", "model_version", "approval_status"])
    return {"generation_production_daily": production, "energy_balance_daily": daily, "procurement_trades_daily": procurement, "portfolio": portfolio, "price_recommendation": pricing}


def write_documentation(out: Path, cfg: Config, pv_count: int) -> None:
    readme = f"""# Fontasya Electric — representatieve jaarset

## Inhoud
- {cfg.n_customers:,} synthetische huishoudens.
- Kalenderjaar {cfg.year} met dagelijkse facttabellen, per maand gepartitioneerd.
- {pv_count:,} PV-klanten ({pv_count / cfg.n_customers:.1%}); dit valt binnen de vereiste bandbreedte van 35% tot 55%.
- Eigen elektriciteitsproductie is jaarlijks gekalibreerd op {cfg.own_electricity_share:.0%} van de vraag.
- Eigen productie bestaat uit {cfg.wind_share_of_own:.0%} wind en {1-cfg.wind_share_of_own:.0%} zon.
- Gas wordt volledig ingekocht.

## Grote maandpartities
- `electricity_consumption_daily/`: {cfg.n_customers:,} klant-dagrecords per dag.
- `gas_consumption_daily/`: {cfg.n_customers:,} klant-dagrecords per dag.
- `pv_feedin_daily/`: alleen PV-klanten, met productie, zelfverbruik en teruglevering.

De grote tabellen zijn gecomprimeerde CSV-bestanden. Voor productiegebruik is Parquet aanbevolen, maar CSV.GZ werkt zonder extra Python-dependencies.

## Sleutels
- `customer_id` koppelt klanten, contracten, PV-assets, elektriciteitsverbruik, gasverbruik en PV-teruglevering.
- `installation_id` koppelt productielocaties en productiedata.
- `date` koppelt alle dagreeksen.
- EAN-codes en coördinaten zijn synthetisch en consistent binnen gekoppelde entiteiten.

## Privacy
De dataset is volledig synthetisch. In een werkelijke omgeving moeten PII, meterdata en pricingdata via toegangscontrole, pseudonimisering, logging en dataminimalisatie worden gescheiden.
"""
    (out / "README.md").write_text(readme, encoding="utf-8")
    er = """# Entiteit-relatieschets

```mermaid
erDiagram
  CUSTOMERS ||--|| CONTRACTS : heeft
  CUSTOMERS ||--o| PV_ASSETS : bezit
  CUSTOMERS ||--o{ ELECTRICITY_CONSUMPTION_DAILY : verbruikt
  CUSTOMERS ||--o{ GAS_CONSUMPTION_DAILY : verbruikt
  CUSTOMERS ||--o{ PV_FEEDIN_DAILY : levert_terug
  PV_ASSETS ||--o{ PV_FEEDIN_DAILY : produceert
  GENERATION_ASSETS ||--o{ GENERATION_PRODUCTION_DAILY : produceert
  WEATHER_FORECAST_DAILY ||--o{ GENERATION_PRODUCTION_DAILY : beinvloedt
  WEATHER_FORECAST_DAILY ||--o{ PV_FEEDIN_DAILY : beinvloedt
  MARKET_PRICE_DAILY ||--o{ PROCUREMENT_TRADES_DAILY : waardeert
  ENERGY_BALANCE_DAILY ||--o{ PROCUREMENT_TRADES_DAILY : balanceert
  CONTRACTS }o--|| PORTFOLIO : groepeert
  PRICE_RECOMMENDATION }o--|| PORTFOLIO : adviseert
```
"""
    (out / "entiteits_relatie_schets.md").write_text(er, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=Path(__file__).name,
        description="Genereer de synthetische Fontasya-jaarset (klanten, markt, verbruik en PV).",
        epilog=(
            "voorbeelden:\n"
            "  python generate_fontasya_jaarset.py --help\n"
            "  python generate_fontasya_jaarset.py --customers 200 --no-zip\n"
            "  python generate_fontasya_jaarset.py --year 2024 --force\n"
            "  python generate_fontasya_jaarset.py --dry-run\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-n", "--customers", type=int, default=Config.n_customers, metavar="N", help="Aantal synthetische huishoudens (standaard: %(default)s)")
    parser.add_argument("--year", type=int, default=Config.year, help="Kalenderjaar van de dagreeksen (standaard: %(default)s)")
    parser.add_argument("--seed", type=int, default=Config.seed, help="RNG-seed voor reproduceerbare output (standaard: %(default)s)")
    parser.add_argument("--pv-share", type=float, default=Config.pv_share, metavar="FRAC", help="Aandeel klanten met PV, 0-1 (standaard: %(default)s)")
    parser.add_argument("--own-electricity-share", type=float, default=Config.own_electricity_share, metavar="FRAC", help="Doel-aandeel eigen elektriciteitsproductie (standaard: %(default)s)")
    parser.add_argument("--wind-share-of-own", type=float, default=Config.wind_share_of_own, metavar="FRAC", help="Aandeel wind binnen eigen productie (standaard: %(default)s)")
    parser.add_argument("-o", "--output-dir", type=Path, default=None, help="Uitvoermap (standaard: fontasya_representatieve_jaarset_<N>_klanten)")
    parser.add_argument("--compresslevel", type=int, default=Config.csv_compresslevel, metavar="0-9", help="gzip-compressieniveau voor CSV (standaard: %(default)s)")
    parser.add_argument("-f", "--force", action="store_true", help="Overschrijf een bestaande uitvoermap")
    parser.add_argument("--no-zip", action="store_true", help="Sla het zip-archief over")
    parser.add_argument("--dry-run", action="store_true", help="Toon de configuratie en schrijf niets")
    parser.add_argument("-q", "--quiet", action="store_true", help="Alleen de eindstatus tonen")
    return parser


def config_from_args(args: argparse.Namespace) -> Config:
    n_customers = args.customers
    output_dir = args.output_dir
    if output_dir is None:
        output_dir = Path(f"fontasya_representatieve_jaarset_{n_customers}_klanten")
    return Config(
        seed=args.seed,
        year=args.year,
        n_customers=n_customers,
        pv_share=args.pv_share,
        own_electricity_share=args.own_electricity_share,
        wind_share_of_own=args.wind_share_of_own,
        output_dir=str(output_dir),
        csv_compresslevel=args.compresslevel,
    )


def validate_config(cfg: Config) -> None:
    errors: list[str] = []
    if cfg.n_customers < 1:
        errors.append("--customers moet minstens 1 zijn")
    if not 2000 <= cfg.year <= 2100:
        errors.append("--year moet tussen 2000 en 2100 liggen")
    if not 0 <= cfg.pv_share <= 1:
        errors.append("--pv-share moet tussen 0 en 1 liggen")
    if not 0 < cfg.own_electricity_share <= 1:
        errors.append("--own-electricity-share moet tussen 0 en 1 liggen (exclusief 0)")
    if not 0 <= cfg.wind_share_of_own <= 1:
        errors.append("--wind-share-of-own moet tussen 0 en 1 liggen")
    if not 0 <= cfg.csv_compresslevel <= 9:
        errors.append("--compresslevel moet tussen 0 en 9 liggen")
    if errors:
        print("Ongeldige opties:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        raise SystemExit(2)


def print_dry_run(cfg: Config, make_zip: bool) -> None:
    n_days = days_in_year(cfg.year)
    electricity_rows = cfg.n_customers * n_days
    expected_pv = int(round(cfg.n_customers * cfg.pv_share))
    print("Dry-run: er worden geen bestanden geschreven.")
    print(json.dumps(asdict(cfg), indent=2))
    print(f"Python: {sys.executable}")
    print(f"Dagen in {cfg.year}: {n_days}")
    print(f"Verwachte PV-klanten: circa {expected_pv:,}")
    print(f"Elektriciteitsrijen: {electricity_rows:,}")
    print(f"Gasrijen: {electricity_rows:,}")
    print(f"Zip-archief: {'nee' if not make_zip else 'ja'}")
    if cfg.n_customers >= 10_000:
        print("Let op: 10.000+ klanten is een zware run. Test eerst met --customers 200.")


def remove_tree(path: Path) -> None:
    def onexc(func, item, exc):
        if isinstance(exc, FileNotFoundError):
            return
        try:
            os.chmod(item, stat.S_IWRITE)
            func(item)
        except FileNotFoundError:
            return

    last_error: Exception | None = None
    for attempt in range(6):
        try:
            shutil.rmtree(path, onexc=onexc)
            return
        except FileNotFoundError:
            return
        except OSError as exc:
            last_error = exc
            time.sleep(0.35 * (attempt + 1))
    print(
        f"Kon bestaande uitvoermap niet verwijderen: {path.resolve()}\n"
        f"{last_error}\n"
        "Sluit open bestanden in die map (en eventuele OneDrive-sync) of kies --output-dir.",
        file=sys.stderr,
    )
    raise SystemExit(1)


def prepare_output_dir(out: Path, force: bool) -> None:
    if out.exists() and out.is_file():
        print(f"Uitvoerpad is een bestand, geen map: {out}", file=sys.stderr)
        raise SystemExit(1)
    if out.exists():
        if not force:
            print(
                f"Uitvoermap bestaat al: {out.resolve()}\n"
                "Gebruik --force om te overschrijven, of kies --output-dir.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        log(f"Bestaande map verwijderen: {out.resolve()}")
        remove_tree(out)
    out.mkdir(parents=True)


def write_zip_archive(out: Path) -> Path:
    archive = Path(f"{out}.zip")
    log(f"Zip-archief maken: {archive}")
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for file in out.rglob("*"):
            if file.is_file():
                zf.write(file, arcname=f"{out.name}/{file.relative_to(out)}")
    return archive


def generate(cfg: Config, make_zip: bool, force: bool) -> int:
    started = time.perf_counter()
    rng = np.random.default_rng(cfg.seed)
    random.seed(cfg.seed)
    out = Path(cfg.output_dir)
    prepare_output_dir(out, force)
    (out / "generation_config.json").write_text(json.dumps(asdict(cfg), indent=2), encoding="utf-8")

    log(f"Start: jaar={cfg.year}, klanten={cfg.n_customers:,}, seed={cfg.seed}")
    log(f"Uitvoermap: {out.resolve()}")
    if cfg.n_customers >= 10_000:
        log("Let op: dit kan meerdere minuten duren en veel schijfruimte vragen. Test met --customers 200.")

    log("Dimensies maken (klanten, contracten, PV)...")
    customers, contracts, pv_assets = create_dimensions(cfg, rng)
    log(f"Klanten: {len(customers):,}  |  PV: {len(pv_assets):,}")

    log("Markt, weer, net en productiemiddelen maken...")
    weather, market, network, assets, production = create_market_and_assets(cfg, rng)

    log("Dagelijkse klantpartities schrijven...")
    daily = create_customer_daily_partitions(cfg, out, customers, pv_assets, weather, market, rng)

    log("Afgeleide tabellen maken...")
    derived = make_small_tables(cfg, customers, contracts, pv_assets, market, production, assets, daily, rng)

    small = {
        "customers": customers,
        "contracts": contracts,
        "pv_assets": pv_assets,
        "weather_forecast_daily": weather,
        "market_price_daily": market,
        "network_system_daily": network,
        "generation_assets": assets,
        **derived,
    }
    quality_rows = []
    for name, df in small.items():
        quality_rows.append([f"DQ_{name}", name, len(df), float(rng.uniform(0.970, 0.999)), float(rng.uniform(0.965, 0.998)), float(rng.uniform(0.960, 0.999)), "CONFIDENTIAL", "OK"])
    quality = pd.DataFrame(quality_rows, columns=["quality_id", "dataset_name", "record_count", "completeness_score", "validity_score", "timeliness_score", "data_classification", "quality_status"])
    small["data_quality"] = quality

    log("Kleine tabellen schrijven...")
    for name, df in small.items():
        write_gzip_csv(df, out / f"{name}.csv.gz", cfg.csv_compresslevel)
        if name in {"customers", "contracts", "pv_assets", "generation_assets", "portfolio", "price_recommendation", "data_quality", "energy_balance_daily"}:
            df.head(1000).to_json(out / f"{name}_sample.json", orient="records", indent=2, date_format="iso")

    write_documentation(out, cfg, len(pv_assets))

    archive = None
    if make_zip:
        archive = write_zip_archive(out)
    else:
        log("Zip-archief overgeslagen (--no-zip)")

    balance = derived["energy_balance_daily"]
    own_total = balance["own_mwh"].sum()
    demand_total = balance["demand_mwh"].sum()
    wind_total = balance["wind"].sum()
    elapsed = time.perf_counter() - started
    print("Gereed")
    print(f"Map: {out.resolve()}")
    print(f"Archief: {archive.resolve() if archive is not None else '(overgeslagen)'}")
    print(f"Klanten: {len(customers):,}")
    print(f"PV-klanten: {len(pv_assets):,} ({len(pv_assets)/len(customers):.1%})")
    print(f"Elektriciteitsvraag: {demand_total:,.1f} MWh")
    print(f"Eigen productie: {own_total:,.1f} MWh ({own_total/demand_total:.1%})")
    print(f"Aandeel wind in eigen productie: {wind_total/own_total:.1%}")
    print(f"Duur: {elapsed:.1f}s")
    return 0


def main(argv: list[str] | None = None) -> int:
    global _quiet
    args = build_parser().parse_args(argv)
    _quiet = args.quiet
    cfg = config_from_args(args)
    validate_config(cfg)
    if args.dry_run:
        print_dry_run(cfg, make_zip=not args.no_zip)
        return 0
    require_runtime_dependencies()
    return generate(cfg, make_zip=not args.no_zip, force=args.force)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nAfgebroken.", file=sys.stderr)
        raise SystemExit(130)
