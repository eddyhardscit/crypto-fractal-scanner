# -*- coding: utf-8 -*-
"""Configuration loader for the automatic KuCoin paper-trading layer."""

from __future__ import annotations

import copy
import json
import os
from pathlib import Path
from typing import Any

DEFAULT_CONFIG_PATH = Path("paper_trading_config.json")


class ConfigError(RuntimeError):
    pass


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _deep_merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    config_path = Path(path or os.getenv("PAPER_TRADING_CONFIG", DEFAULT_CONFIG_PATH))
    if not config_path.exists():
        raise ConfigError(f"Configurazione paper trading non trovata: {config_path}")

    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ConfigError(f"Configurazione non leggibile: {exc}") from exc

    env_overrides: dict[str, Any] = {}
    if os.getenv("PAPER_INITIAL_CAPITAL_EUR"):
        env_overrides["initial_capital_eur"] = float(os.environ["PAPER_INITIAL_CAPITAL_EUR"])
    if os.getenv("PAPER_MONTHLY_TARGET_EUR"):
        env_overrides["monthly_target_eur"] = float(os.environ["PAPER_MONTHLY_TARGET_EUR"])
    if os.getenv("PAPER_COMPOUNDING_ENABLED"):
        env_overrides["compounding_enabled"] = os.environ["PAPER_COMPOUNDING_ENABLED"].strip().lower() in {
            "1", "true", "yes", "si", "sì"
        }
    if os.getenv("EUR_USDT_RATE"):
        env_overrides["eur_usdt_fallback_rate"] = float(os.environ["EUR_USDT_RATE"])

    config = _deep_merge(config, env_overrides)
    validate_config(config)
    config["_config_path"] = str(config_path)
    return config


def validate_config(config: dict[str, Any]) -> None:
    capital = float(config.get("initial_capital_eur", 0))
    target = float(config.get("monthly_target_eur", 0))
    if capital <= 0:
        raise ConfigError("initial_capital_eur deve essere maggiore di zero.")
    if target < 0:
        raise ConfigError("monthly_target_eur non può essere negativo.")
    if config.get("target_policy") != "MONITOR_ONLY_NEVER_CHASE":
        raise ConfigError("Il target deve restare MONITOR_ONLY_NEVER_CHASE.")

    risk = config.get("risk", {})
    for key in ("risk_per_trade", "max_total_open_risk", "max_daily_loss", "max_weekly_loss"):
        value = float(risk.get(key, 0))
        if not 0 < value < 1:
            raise ConfigError(f"Parametro rischio non valido: {key}={value}")
    if float(risk.get("absolute_max_leverage", 0)) > 5:
        raise ConfigError("La leva massima assoluta della fase paper non può superare 5x.")

    names: set[str] = set()
    main_count = 0
    for portfolio in config.get("portfolios", []):
        if not portfolio.get("enabled", True):
            continue
        name = str(portfolio.get("name", "")).strip()
        if not name or name in names:
            raise ConfigError(f"Nome portafoglio mancante o duplicato: {name!r}")
        names.add(name)
        main_count += int(bool(portfolio.get("is_main")))
        leverage = float(
            portfolio.get(
                "leverage",
                risk.get("default_leverage", 1),
            )
        )
        global_cap = float(
            risk.get("absolute_max_leverage", 5)
        )
        if leverage <= 0:
            raise ConfigError(
                f"Leva non valida per {name}: {leverage}"
            )
        if leverage > global_cap:
            allowed_test = bool(
                portfolio.get(
                    "paper_only_high_leverage_test"
                )
            )
            fixed_margin = float(
                portfolio.get("fixed_margin_eur", 0)
            )
            max_stop = float(
                portfolio.get(
                    "maximum_stop_pct",
                    1.0,
                )
            )
            if (
                not allowed_test
                or portfolio.get("is_main")
                or portfolio.get("strategy")
                != "rsi_extreme_reversal"
                or leverage > 15
                or not 0 < fixed_margin <= 50
                or max_stop > 0.05
            ):
                raise ConfigError(
                    "Leva oltre il limite globale consentita "
                    "solo ai test paper RSI estremi con margine fisso "
                    f"massimo €50: {name}={leverage}x"
                )
    if main_count != 1:
        raise ConfigError("Deve esistere esattamente un portafoglio principale abilitato.")


def public_config_snapshot(config: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in config.items() if not key.startswith("_")}
