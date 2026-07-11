# -*- coding: utf-8 -*-
"""Run the full exchange collector on an allowed external/self-hosted machine.

This orchestrator restores the newest valid Release state, collects Binance,
Bybit and KuCoin, refuses to publish a geoblocked/incomplete run, then publishes
and audits the redundant state.

Required environment variables:
- GITHUB_REPOSITORY=OWNER/REPO
- GITHUB_TOKEN or GH_TOKEN with permission to read/write that repository's Releases

No exchange trading API keys are used. The host must be in a jurisdiction where
the public exchange APIs are permitted. This script does not configure proxies,
VPNs or geo-bypass mechanisms.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

HEALTH_PATH = Path("reports/exchange_market_data_health.json")
LOCK_PATH = Path(".exchange_external_collector.lock")


def run(*args: str, env: dict[str, str]) -> None:
    command = [sys.executable, *args]
    print("+", " ".join(command), flush=True)
    subprocess.run(command, check=True, env=env)


def read_health() -> dict:
    if not HEALTH_PATH.exists():
        raise RuntimeError(f"File health mancante dopo la raccolta: {HEALTH_PATH}")
    payload = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError("Health JSON non valido")
    return payload


def validate_external_health(health: dict) -> None:
    statuses = health.get("exchange_status", {}) if isinstance(health.get("exchange_status"), dict) else {}
    blocked = [name for name in ("binance", "bybit") if str(statuses.get(name, "")).upper() == "GEO_BLOCKED"]
    if blocked:
        raise RuntimeError(
            "Collector esterno ancora geobloccato per: " + ", ".join(blocked) + ". Stato non pubblicato."
        )
    minimum = int(os.getenv("EXTERNAL_MIN_AVAILABLE_PAIRS", "6"))
    available = int(health.get("available_exchange_asset_pairs") or 0)
    if available < minimum:
        raise RuntimeError(
            f"Copertura esterna insufficiente: {available}/9, minimo richiesto {minimum}. Stato non pubblicato."
        )


def main() -> None:
    repository = os.getenv("GITHUB_REPOSITORY", "").strip()
    token = os.getenv("GITHUB_TOKEN", "").strip() or os.getenv("GH_TOKEN", "").strip()
    if "/" not in repository:
        raise SystemExit("Imposta GITHUB_REPOSITORY=OWNER/REPO")
    if not token:
        raise SystemExit("Imposta GITHUB_TOKEN o GH_TOKEN con accesso al repository")
    if LOCK_PATH.exists():
        raise SystemExit(f"Collector già in esecuzione o lock non rimosso: {LOCK_PATH}")

    env = os.environ.copy()
    env.update(
        {
            "EXCHANGE_COLLECTOR_MODE": "external-allowed-host",
            "EXCHANGE_ENABLED_EXCHANGES": "binance,bybit,kucoin",
            "EXCHANGE_STORAGE_RELEASE_TAG": env.get("EXCHANGE_STORAGE_RELEASE_TAG", "exchange-data-v2-1"),
            "EXCHANGE_INTRADAY_RETENTION_DAYS": env.get("EXCHANGE_INTRADAY_RETENTION_DAYS", "180"),
            "EXCHANGE_LIQ_SAMPLE_SECONDS": env.get("EXCHANGE_LIQ_SAMPLE_SECONDS", "15"),
        }
    )

    LOCK_PATH.write_text(str(os.getpid()), encoding="utf-8")
    try:
        run("exchange_persistent_storage.py", "restore", env=env)
        run("exchange_market_data.py", env=env)
        health = read_health()
        validate_external_health(health)
        run("exchange_persistent_storage.py", "publish-state", env=env)
        run("exchange_persistent_storage.py", "audit", env=env)
        print(
            "Collector esterno completato: "
            f"{health.get('available_exchange_asset_pairs', 0)}/{health.get('total_exchange_asset_pairs', 9)} coppie disponibili."
        )
    finally:
        LOCK_PATH.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
