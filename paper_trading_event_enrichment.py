# -*- coding: utf-8 -*-
"""Enrich and render newly opened paper positions for Telegram."""
from __future__ import annotations

import math
from typing import Any

from paper_trading_engine import current_prices


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except Exception:
        return default


def _fmt_eur(value: Any, signed: bool = False) -> str:
    number = _safe_float(value)
    if number < 0:
        prefix = "-"
    elif signed and number > 0:
        prefix = "+"
    else:
        prefix = ""
    rendered = f"{prefix}€{abs(number):,.2f}"
    return rendered.replace(",", "X").replace(".", ",").replace("X", ".")


def _fmt_pct(value: Any, signed: bool = False) -> str:
    number = _safe_float(value)
    prefix = "+" if signed and number > 0 else ""
    return f"{prefix}{number:.2f}%".replace(".", ",")


def _fmt_price(value: Any) -> str:
    number = _safe_float(value)
    if number >= 100:
        rendered = f"{number:,.2f}"
        return rendered.replace(",", "X").replace(".", ",").replace("X", ".")
    if number >= 1:
        return f"{number:.4f}".rstrip("0").rstrip(".").replace(".", ",")
    return f"{number:.8f}".rstrip("0").rstrip(".").replace(".", ",")


def _distance_pct(mark: float, level: float, side: str, kind: str) -> float | None:
    if mark <= 0 or level <= 0:
        return None
    side = side.upper()
    if kind == "stop":
        return ((mark - level) / mark * 100.0 if side == "LONG" else (level - mark) / mark * 100.0)
    return ((level - mark) / mark * 100.0 if side == "LONG" else (mark - level) / mark * 100.0)


def _fmt_distance(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value < 0:
        return f"superato di {_fmt_pct(abs(value))}"
    return _fmt_pct(value)


def enrich_opened_positions(summary: dict[str, Any], bundle: dict[str, Any], config: dict[str, Any]) -> None:
    prices = current_prices(bundle)
    eur_rate = _safe_float(bundle.get("eur_usdt_rate", config.get("eur_usdt_fallback_rate", 1.0)), 1.0) or 1.0
    for position in summary.get("opened", []):
        asset = str(position.get("asset", ""))
        side = str(position.get("side", "")).upper()
        entry = _safe_float(position.get("entry_price"))
        mark = _safe_float(prices.get(asset, entry), entry)
        quantity = abs(_safe_float(position.get("quantity")))
        margin = _safe_float(position.get("margin_eur"))
        stop = _safe_float(position.get("stop_price"))
        target = _safe_float(position.get("target_price"))
        raw_usdt = ((mark - entry) * quantity if side == "LONG" else (entry - mark) * quantity)
        pnl_eur = raw_usdt / max(eur_rate, 1e-9)
        pnl_pct = pnl_eur / margin * 100.0 if margin > 0 else 0.0
        position["mark_price"] = mark
        position["unrealized_pnl_eur"] = pnl_eur
        position["unrealized_pnl_pct_margin"] = pnl_pct
        position["stop_distance_pct"] = _distance_pct(mark, stop, side, "stop")
        position["target_distance_pct"] = _distance_pct(mark, target, side, "target")


def opening_status_lines(position: dict[str, Any]) -> list[str]:
    mark = _safe_float(position.get("mark_price"), _safe_float(position.get("entry_price")))
    pnl = _safe_float(position.get("unrealized_pnl_eur"))
    pnl_pct = _safe_float(position.get("unrealized_pnl_pct_margin"))
    if pnl > 0:
        status = "✅ IN PROFITTO"
    elif pnl < 0:
        status = "❌ IN PERDITA"
    else:
        status = "➖ P&L INIZIALE"
    return [
        f"Mark {_fmt_price(mark)} · {status} {_fmt_eur(pnl, signed=True)} ({_fmt_pct(pnl_pct, signed=True)} sul margine)",
        f"Distanza stop {_fmt_distance(position.get('stop_distance_pct'))} · distanza target {_fmt_distance(position.get('target_distance_pct'))}",
    ]
