# -*- coding: utf-8 -*-
"""Enrich Telegram events and analyse leveraged paper-trade exit paths."""
from __future__ import annotations

import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from paper_trading_engine import current_prices

REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "paper_trading_state.json"
TRADE_LOG_PATH = REPORTS_DIR / "paper_trading_trade_log.csv"
PATH_LOG_PATH = REPORTS_DIR / "paper_trading_trade_path.csv"
EXIT_ANALYSIS_CSV_PATH = REPORTS_DIR / "paper_trading_exit_analysis.csv"
EXIT_ANALYSIS_REPORT_PATH = REPORTS_DIR / "paper_trading_exit_analysis.md"

PATH_FIELDS = [
    "timestamp", "trade_id", "portfolio", "asset", "side", "status",
    "mark_price", "unrealized_net_pnl_eur", "running_mfe_net_eur",
    "running_mae_net_eur", "stop_price", "target_price", "margin_eur", "leverage",
]

THRESHOLDS_EUR = (25.0, 50.0, 75.0, 100.0, 150.0, 200.0)


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
        return ((mark - level) / mark * 100.0 if side == "LONG"
                else (level - mark) / mark * 100.0)
    return ((level - mark) / mark * 100.0 if side == "LONG"
            else (mark - level) / mark * 100.0)


def _fmt_distance(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value < 0:
        return f"superato di {_fmt_pct(abs(value))}"
    return _fmt_pct(value)


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def _append_unique_path_rows(rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    PATH_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing_keys: set[tuple[str, str, str]] = set()
    if PATH_LOG_PATH.exists() and PATH_LOG_PATH.stat().st_size > 0:
        for row in _read_csv(PATH_LOG_PATH):
            existing_keys.add((
                str(row.get("timestamp", "")),
                str(row.get("trade_id", "")),
                str(row.get("status", "")),
            ))

    new_rows = [
        row for row in rows
        if (
            str(row.get("timestamp", "")),
            str(row.get("trade_id", "")),
            str(row.get("status", "")),
        ) not in existing_keys
    ]
    if not new_rows:
        return

    exists = PATH_LOG_PATH.exists() and PATH_LOG_PATH.stat().st_size > 0
    with PATH_LOG_PATH.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PATH_FIELDS, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        for row in new_rows:
            writer.writerow({field: row.get(field, "") for field in PATH_FIELDS})


def _estimated_unrealized_net(
    position: dict[str, Any],
    mark: float,
    eur_rate: float,
    fee_rate: float,
) -> float:
    entry = _safe_float(position.get("entry_price"))
    quantity = abs(_safe_float(position.get("quantity")))
    direction = 1.0 if str(position.get("side", "")).upper() == "LONG" else -1.0
    gross = (mark - entry) * quantity * direction / max(eur_rate, 1e-12)
    exit_notional = abs(mark * quantity / max(eur_rate, 1e-12))
    exit_fee = exit_notional * fee_rate
    return (
        gross
        - _safe_float(position.get("entry_fee_eur"))
        - exit_fee
        + _safe_float(position.get("funding_pnl_eur"))
    )


def _record_trade_paths(
    summary: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
) -> None:
    timestamp = str(
        summary.get("generated_utc")
        or datetime.now(timezone.utc).isoformat(timespec="seconds")
    )
    prices = current_prices(bundle)
    eur_rate = _safe_float(
        bundle.get("eur_usdt_rate", config.get("eur_usdt_fallback_rate", 1.0)),
        1.0,
    ) or 1.0
    fee_rate = (
        _safe_float(config.get("execution", {}).get("taker_fee_bps"), 0.0)
        / 10_000.0
    )
    rows: list[dict[str, Any]] = []

    if STATE_PATH.exists():
        try:
            state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            state = {}

        for portfolio_name, portfolio in state.get("portfolios", {}).items():
            for position in portfolio.get("open_positions", []):
                asset = str(position.get("asset", ""))
                mark = _safe_float(
                    prices.get(asset),
                    _safe_float(position.get("entry_price")),
                )
                pnl = _estimated_unrealized_net(position, mark, eur_rate, fee_rate)
                rows.append({
                    "timestamp": timestamp,
                    "trade_id": position.get("trade_id", ""),
                    "portfolio": portfolio_name,
                    "asset": asset,
                    "side": position.get("side", ""),
                    "status": "OPEN",
                    "mark_price": mark,
                    "unrealized_net_pnl_eur": pnl,
                    "running_mfe_net_eur": max(
                        _safe_float(position.get("mfe_net_eur"), pnl), pnl
                    ),
                    "running_mae_net_eur": min(
                        _safe_float(position.get("mae_net_eur"), pnl), pnl
                    ),
                    "stop_price": position.get("stop_price", ""),
                    "target_price": position.get("target_price", ""),
                    "margin_eur": position.get("margin_eur", ""),
                    "leverage": position.get("leverage", ""),
                })

    for trade in summary.get("closed", []):
        rows.append({
            "timestamp": str(trade.get("closed_at") or timestamp),
            "trade_id": trade.get("trade_id", ""),
            "portfolio": trade.get("portfolio", ""),
            "asset": trade.get("asset", ""),
            "side": trade.get("side", ""),
            "status": "CLOSED",
            "mark_price": trade.get("exit_price", ""),
            "unrealized_net_pnl_eur": trade.get("net_pnl_eur", ""),
            "running_mfe_net_eur": trade.get("mfe_net_eur", ""),
            "running_mae_net_eur": trade.get("mae_net_eur", ""),
            "stop_price": trade.get("final_stop_price", ""),
            "target_price": trade.get("target_price", ""),
            "margin_eur": trade.get("margin_eur", ""),
            "leverage": trade.get("leverage", ""),
        })

    _append_unique_path_rows(rows)


def _ordered_path(rows: list[dict[str, str]]) -> list[tuple[str, float]]:
    ordered = [
        (str(row.get("timestamp", "")),
         _safe_float(row.get("unrealized_net_pnl_eur")))
        for row in rows
    ]
    return sorted(ordered, key=lambda item: item[0])


def _first_threshold_outcome(
    path: list[tuple[str, float]],
    actual: float,
    take_profit: float | None = None,
    stop_loss: float | None = None,
) -> float:
    for _, pnl in path:
        if stop_loss is not None and pnl <= -abs(stop_loss):
            return -abs(stop_loss)
        if take_profit is not None and pnl >= take_profit:
            return take_profit
    return actual


def _protected_outcome(
    path: list[tuple[str, float]],
    actual: float,
    activation: float,
    floor: float,
) -> float:
    active = False
    for _, pnl in path:
        if not active and pnl >= activation:
            active = True
        elif active and pnl <= floor:
            return floor
    return actual


def _trailing_outcome(
    path: list[tuple[str, float]],
    actual: float,
    activation: float = 50.0,
    giveback_fraction: float = 0.20,
) -> float:
    active = False
    peak = 0.0
    for _, pnl in path:
        if not active and pnl >= activation:
            active = True
            peak = pnl
            continue
        if active:
            peak = max(peak, pnl)
            floor = max(0.0, peak * (1.0 - giveback_fraction))
            if pnl <= floor:
                return pnl
    return actual


def _write_exit_analysis() -> None:
    trade_rows = _read_csv(TRADE_LOG_PATH)
    path_rows = _read_csv(PATH_LOG_PATH)

    if not trade_rows:
        EXIT_ANALYSIS_REPORT_PATH.write_text(
            "# Analisi uscite paper trading a leva\n\n"
            "Nessun trade chiuso disponibile.\n",
            encoding="utf-8",
        )
        return

    paths_by_trade: dict[str, list[dict[str, str]]] = {}
    for row in path_rows:
        trade_id = str(row.get("trade_id", ""))
        if trade_id:
            paths_by_trade.setdefault(trade_id, []).append(row)

    detail_rows: list[dict[str, Any]] = []
    eligible = 0
    reached_50 = 0
    reached_50_closed_loss = 0
    actual_total = 0.0

    scenario_totals: dict[str, float] = {"actual": 0.0}
    scenario_totals.update(
        {f"tp_{int(value)}": 0.0 for value in THRESHOLDS_EUR}
    )
    scenario_totals.update({
        "sl_50": 0.0,
        "tp50_sl50": 0.0,
        "breakeven_after_50": 0.0,
        "lock20_after_50": 0.0,
        "lock30_after_50": 0.0,
        "partial50_after_50": 0.0,
        "trailing20_after_50": 0.0,
    })

    for trade in trade_rows:
        trade_id = str(trade.get("trade_id", ""))
        actual = _safe_float(trade.get("net_pnl_eur"))
        actual_total += actual
        scenario_totals["actual"] += actual

        path = _ordered_path(paths_by_trade.get(trade_id, []))
        mfe = _safe_float(trade.get("mfe_net_eur"))
        mae = _safe_float(trade.get("mae_net_eur"))
        hit50 = mfe >= 50.0 or any(pnl >= 50.0 for _, pnl in path)

        if hit50:
            reached_50 += 1
            if actual < 0:
                reached_50_closed_loss += 1

        if path:
            eligible += 1
            simulations: dict[str, float] = {
                f"tp_{int(value)}": _first_threshold_outcome(
                    path, actual, take_profit=value
                )
                for value in THRESHOLDS_EUR
            }
            simulations.update({
                "sl_50": _first_threshold_outcome(
                    path, actual, stop_loss=50.0
                ),
                "tp50_sl50": _first_threshold_outcome(
                    path, actual, take_profit=50.0, stop_loss=50.0
                ),
                "breakeven_after_50": _protected_outcome(
                    path, actual, 50.0, 0.0
                ),
                "lock20_after_50": _protected_outcome(
                    path, actual, 50.0, 20.0
                ),
                "lock30_after_50": _protected_outcome(
                    path, actual, 50.0, 30.0
                ),
                "partial50_after_50": (
                    25.0 + 0.5 * actual if hit50 else actual
                ),
                "trailing20_after_50": _trailing_outcome(path, actual),
            })
        else:
            simulations = {
                key: actual for key in scenario_totals if key != "actual"
            }

        for key, value in simulations.items():
            scenario_totals[key] += value

        detail_rows.append({
            "trade_id": trade_id,
            "portfolio": trade.get("portfolio", ""),
            "asset": trade.get("asset", ""),
            "side": trade.get("side", ""),
            "closed_at": trade.get("closed_at", ""),
            "actual_net_pnl_eur": actual,
            "mfe_net_eur": mfe,
            "mae_net_eur": mae,
            "reached_50_eur": hit50,
            "closed_loss_after_reaching_50": hit50 and actual < 0,
            **simulations,
        })

    if detail_rows:
        fields = list(detail_rows[0].keys())
        with EXIT_ANALYSIS_CSV_PATH.open(
            "w", encoding="utf-8", newline=""
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(detail_rows)

    labels = {
        "actual": "Strategia attuale",
        "tp_25": "Take profit fisso +€25",
        "tp_50": "Take profit fisso +€50",
        "tp_75": "Take profit fisso +€75",
        "tp_100": "Take profit fisso +€100",
        "tp_150": "Take profit fisso +€150",
        "tp_200": "Take profit fisso +€200",
        "sl_50": "Stop loss fisso -€50",
        "tp50_sl50": "TP +€50 / SL -€50",
        "breakeven_after_50": "Pareggio dopo +€50",
        "lock20_after_50": "Protegge +€20 dopo +€50",
        "lock30_after_50": "Protegge +€30 dopo +€50",
        "partial50_after_50": "Chiude 50% a +€50",
        "trailing20_after_50": "Trailing 20% dopo +€50",
    }

    ranked = sorted(
        scenario_totals.items(), key=lambda item: item[1], reverse=True
    )
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        "# Analisi uscite paper trading a leva",
        "",
        f"Generato: {now}",
        "",
        "> Analisi osservativa: non modifica ingressi, uscite o rischio "
        "del paper trading.",
        "",
        "## Verifica del target +€50",
        "",
        f"- Trade chiusi: **{len(trade_rows)}**",
        f"- Trade con percorso cronologico utilizzabile: **{eligible}**",
        f"- Trade che hanno raggiunto almeno +€50: **{reached_50}**",
        f"- Di questi, chiusi poi in perdita: "
        f"**{reached_50_closed_loss}**",
        "",
        "## Confronto simulazioni",
        "",
        "| Posizione | Regola di uscita | P&L simulato | "
        "Differenza dall'attuale |",
        "| ---: | --- | ---: | ---: |",
    ]

    for index, (key, total) in enumerate(ranked, start=1):
        delta = total - actual_total
        lines.append(
            f"| {index} | {labels.get(key, key)} | "
            f"{_fmt_eur(total, signed=True)} | "
            f"{_fmt_eur(delta, signed=True)} |"
        )

    lines.extend([
        "",
        "## Limiti metodologici",
        "",
        "Le simulazioni usano i campioni cronologici salvati a ogni ciclo. "
        "Non presumono l'ordine interno dei movimenti tra due campioni. "
        "Le decisioni operative restano invariate finché il campione "
        "non sarà sufficiente.",
        "",
    ])
    EXIT_ANALYSIS_REPORT_PATH.write_text(
        "\n".join(lines), encoding="utf-8"
    )


def enrich_opened_positions(
    summary: dict[str, Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
) -> None:
    prices = current_prices(bundle)
    eur_rate = _safe_float(
        bundle.get(
            "eur_usdt_rate",
            config.get("eur_usdt_fallback_rate", 1.0),
        ),
        1.0,
    ) or 1.0

    for position in summary.get("opened", []):
        asset = str(position.get("asset", ""))
        side = str(position.get("side", "")).upper()
        entry = _safe_float(position.get("entry_price"))
        mark = _safe_float(prices.get(asset, entry), entry)
        quantity = abs(_safe_float(position.get("quantity")))
        margin = _safe_float(position.get("margin_eur"))
        stop = _safe_float(position.get("stop_price"))
        target = _safe_float(position.get("target_price"))
        raw_usdt = (
            (mark - entry) * quantity
            if side == "LONG"
            else (entry - mark) * quantity
        )
        pnl_eur = raw_usdt / max(eur_rate, 1e-9)
        pnl_pct = pnl_eur / margin * 100.0 if margin > 0 else 0.0
        position["mark_price"] = mark
        position["unrealized_pnl_eur"] = pnl_eur
        position["unrealized_pnl_pct_margin"] = pnl_pct
        position["stop_distance_pct"] = _distance_pct(
            mark, stop, side, "stop"
        )
        position["target_distance_pct"] = _distance_pct(
            mark, target, side, "target"
        )

    try:
        _record_trade_paths(summary, bundle, config)
        _write_exit_analysis()
    except Exception as exc:
        print(f"Analisi cronologica uscite non aggiornata: {exc}")


def opening_status_lines(position: dict[str, Any]) -> list[str]:
    mark = _safe_float(
        position.get("mark_price"),
        _safe_float(position.get("entry_price")),
    )
    pnl = _safe_float(position.get("unrealized_pnl_eur"))
    pnl_pct = _safe_float(position.get("unrealized_pnl_pct_margin"))

    if pnl > 0:
        status = "✅ IN PROFITTO"
    elif pnl < 0:
        status = "❌ IN PERDITA"
    else:
        status = "➖ P&L INIZIALE"

    return [
        f"Mark {_fmt_price(mark)} · {status} "
        f"{_fmt_eur(pnl, signed=True)} "
        f"({_fmt_pct(pnl_pct, signed=True)} sul margine)",
        f"Distanza stop "
        f"{_fmt_distance(position.get('stop_distance_pct'))} · "
        f"distanza target "
        f"{_fmt_distance(position.get('target_distance_pct'))}",
    ]
