# -*- coding: utf-8 -*-
"""Reader for the structured scanner summary.

Import this module from global_confluence_report.py instead of parsing
reports/latest_report.md with regular expressions.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


REPORTS_DIR = Path("reports")
SUMMARY_CSV = REPORTS_DIR / "latest_scanner_summary.csv"
SUMMARY_JSON = REPORTS_DIR / "latest_scanner_summary.json"
MATCHES_CSV = REPORTS_DIR / "latest_scanner_matches.csv"

REQUIRED_FIELDS = {
    "asset",
    "direction_30d",
    "positive_cases_30d",
    "negative_cases_30d",
    "return_p50_pct",
    "return_p50_price",
    "current_price",
}


def safe_float(value: Any) -> float:
    try:
        value = float(value)
        return value if np.isfinite(value) else np.nan
    except (TypeError, ValueError):
        return np.nan


def normalize_asset(value: Any) -> str:
    return str(value).upper().replace("-USD", "").strip()


def _load_csv() -> pd.DataFrame:
    if not SUMMARY_CSV.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(SUMMARY_CSV, encoding="utf-8")
    except Exception:
        return pd.DataFrame()
    if "asset" in df.columns:
        df["asset"] = df["asset"].map(normalize_asset)
    return df


def _load_json() -> pd.DataFrame:
    if not SUMMARY_JSON.exists():
        return pd.DataFrame()
    try:
        payload = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    except Exception:
        return pd.DataFrame()

    assets = payload.get("assets", {})
    rows = []
    for asset, record in assets.items():
        row = dict(record)
        row["asset"] = normalize_asset(asset)
        rows.append(row)
    return pd.DataFrame(rows)


def _fallback_from_matches() -> pd.DataFrame:
    if not MATCHES_CSV.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(MATCHES_CSV, encoding="utf-8")
    except Exception:
        return pd.DataFrame()

    needed = {"target_asset", "return_30d"}
    if not needed.issubset(df.columns):
        return pd.DataFrame()

    df["target_asset"] = df["target_asset"].map(normalize_asset)
    df["return_30d"] = pd.to_numeric(df["return_30d"], errors="coerce")
    df = df.dropna(subset=["return_30d"])

    rows = []
    for asset, group in df.groupby("target_asset"):
        pos = float((group["return_30d"] > 0).mean() * 100)
        neg = 100.0 - pos
        if pos >= 60:
            direction = "SALITA"
        elif neg >= 60:
            direction = "DISCESA"
        else:
            direction = "INCERTO"
        rows.append({
            "asset": asset,
            "direction_30d": direction,
            "positive_cases_30d": pos,
            "negative_cases_30d": neg,
            "return_p50_pct": float(group["return_30d"].median()),
            "return_p50_price": np.nan,
            "current_price": np.nan,
            "match_count": int(len(group)),
            "source": "fallback latest_scanner_matches.csv",
        })
    return pd.DataFrame(rows)


def load_scanner_summary() -> pd.DataFrame:
    """Return one structured row per asset.

    Priority: CSV, JSON, then a limited fallback rebuilt from match rows.
    """
    for loader in (_load_csv, _load_json, _fallback_from_matches):
        df = loader()
        if not df.empty:
            return df.copy()
    return pd.DataFrame()


def scanner_signal(asset: str) -> dict[str, Any]:
    asset = normalize_asset(asset)
    df = load_scanner_summary()
    if df.empty or "asset" not in df.columns:
        return {
            "asset": asset,
            "available": False,
            "direction_30d": "n/a",
            "positive_cases_30d": np.nan,
            "negative_cases_30d": np.nan,
            "return_p50_pct": np.nan,
            "return_p50_price": np.nan,
            "current_price": np.nan,
        }

    row = df[df["asset"].map(normalize_asset) == asset]
    if row.empty:
        return {
            "asset": asset,
            "available": False,
            "direction_30d": "n/a",
            "positive_cases_30d": np.nan,
            "negative_cases_30d": np.nan,
            "return_p50_pct": np.nan,
            "return_p50_price": np.nan,
            "current_price": np.nan,
        }

    record = row.iloc[0].to_dict()
    record["asset"] = asset
    record["available"] = True
    return record


def validate_scanner_summary() -> list[str]:
    df = load_scanner_summary()
    if df.empty:
        return ["Scanner summary non disponibile."]

    missing = sorted(REQUIRED_FIELDS - set(df.columns))
    issues = []
    if missing:
        issues.append("Colonne mancanti: " + ", ".join(missing))

    for asset in ["BTC", "SOL", "DOGE"]:
        if asset not in set(df.get("asset", pd.Series(dtype=str)).map(normalize_asset)):
            issues.append(f"Riga {asset} mancante.")
    return issues


if __name__ == "__main__":
    print(load_scanner_summary().to_string(index=False))
