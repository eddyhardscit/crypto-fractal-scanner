# -*- coding: utf-8 -*-
"""Research ledger that simulates every valid signal without portfolio caps."""
from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
from kucoin_public_data import bundle_frames

REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "research_all_signals_state.json"
TRADES_PATH = REPORTS_DIR / "research_all_signals_trades.csv"
REPORT_PATH = REPORTS_DIR / "research_all_signals_report.md"
LATEST_PATH = REPORTS_DIR / "research_all_signals_latest.json"
TRADE_FIELDS = [
    "research_id", "experiment_group_id", "profile", "portfolio_source",
    "strategy", "asset", "side", "timeframe_minutes", "opened_at",
    "closed_at", "entry_price", "exit_price", "stop_price", "target_price",
    "stop_pct", "target_pct", "holding_hours", "close_reason",
    "normalized_risk_eur", "normalized_notional_eur", "gross_pnl_eur",
    "costs_eur", "net_pnl_eur", "r_multiple", "score", "confidence",
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_time(value: Any) -> datetime:
    stamp = pd.Timestamp(value)
    if stamp.tzinfo is None:
        stamp = stamp.tz_localize("UTC")
    return stamp.to_pydatetime()


def profile_name(portfolio: str) -> str:
    raw = str(portfolio)
    if raw.startswith("SHADOW_RSI_LONG_"):
        return "RSI_EXTREME_LONG_15M"
    if raw.startswith("SHADOW_RSI_SHORT_"):
        return "RSI_EXTREME_SHORT_15M"
    return raw


def load_state() -> dict[str, Any]:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    current = now_utc().isoformat(timespec="seconds")
    return {
        "schema_version": 1,
        "created_utc": current,
        "updated_utc": current,
        "seen_research_ids": [],
        "open_positions": [],
        "skipped_overlap": 0,
    }


def save_state(state: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_utc"] = now_utc().isoformat(timespec="seconds")
    temp = STATE_PATH.with_suffix(".json.tmp")
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(STATE_PATH)


def append_trade(row: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    exists = TRADES_PATH.exists() and TRADES_PATH.stat().st_size > 0
    with TRADES_PATH.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRADE_FIELDS, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow({field: row.get(field, "") for field in TRADE_FIELDS})


def read_trades() -> list[dict[str, Any]]:
    if not TRADES_PATH.exists():
        return []
    with TRADES_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def canonical_signals(signals: list[Any]) -> list[Any]:
    chosen: dict[tuple[str, str, int, str, str], Any] = {}
    for signal in signals:
        key = (
            profile_name(signal.portfolio), str(signal.asset),
            int(signal.timeframe_minutes), str(signal.candle_time), str(signal.side),
        )
        current = chosen.get(key)
        if current is None or abs(float(signal.score)) > abs(float(current.score)):
            chosen[key] = signal
    return list(chosen.values())


def research_id(signal: Any) -> str:
    return "|".join([
        profile_name(signal.portfolio), str(signal.asset),
        str(signal.timeframe_minutes), str(signal.candle_time), str(signal.side),
    ])


def mark_prices(bundle: dict[str, Any]) -> dict[str, float]:
    output: dict[str, float] = {}
    for asset, payload in bundle.get("assets", {}).items():
        try:
            output[str(asset)] = float(payload.get("mark_price"))
        except Exception:
            pass
    return output


def close_trade(position: dict[str, Any], exit_price: float, reason: str, when: datetime) -> dict[str, Any]:
    entry = float(position["entry_price"])
    direction = 1.0 if position["side"] == "LONG" else -1.0
    risk_eur = float(position["normalized_risk_eur"])
    notional = float(position["normalized_notional_eur"])
    gross = direction * (float(exit_price) / entry - 1.0) * notional
    costs = notional * 0.0008 * 2.0
    net = gross - costs
    opened = parse_time(position["opened_at"])
    row = {
        **position,
        "closed_at": when.isoformat(timespec="seconds"),
        "exit_price": float(exit_price),
        "holding_hours": max(0.0, (when - opened).total_seconds() / 3600.0),
        "close_reason": reason,
        "gross_pnl_eur": gross,
        "costs_eur": costs,
        "net_pnl_eur": net,
        "r_multiple": net / risk_eur if risk_eur > 0 else 0.0,
    }
    append_trade(row)
    return row


def update_open_positions(state: dict[str, Any], bundle: dict[str, Any], current: datetime) -> list[dict[str, Any]]:
    frames = bundle_frames(bundle)
    prices = mark_prices(bundle)
    remaining, closed = [], []
    for position in state.get("open_positions", []):
        asset = str(position["asset"])
        timeframe = int(position["timeframe_minutes"])
        frame = frames.get(asset, {}).get(timeframe)
        stop, target = float(position["stop_price"]), float(position["target_price"])
        opened = parse_time(position["opened_at"])
        exit_price, reason, exit_time = None, "", current
        if frame is not None and not frame.empty:
            for stamp, candle in frame.sort_index().iterrows():
                candle_time = parse_time(stamp)
                if candle_time <= opened:
                    continue
                if position["side"] == "LONG":
                    stop_hit = float(candle["low"]) <= stop
                    target_hit = float(candle["high"]) >= target
                else:
                    stop_hit = float(candle["high"]) >= stop
                    target_hit = float(candle["low"]) <= target
                if stop_hit and target_hit:
                    exit_price, reason, exit_time = stop, "STOP_SAME_CANDLE_CONSERVATIVE", candle_time
                    break
                if stop_hit:
                    exit_price, reason, exit_time = stop, "STOP", candle_time
                    break
                if target_hit:
                    exit_price, reason, exit_time = target, "TARGET", candle_time
                    break
        if exit_price is None and (current - opened).total_seconds() / 3600.0 >= float(position.get("max_holding_hours", 168)):
            exit_price = float(prices.get(asset, position["entry_price"]))
            reason = "TIME_EXIT"
        if exit_price is None:
            remaining.append(position)
        else:
            closed.append(close_trade(position, float(exit_price), reason, exit_time))
    state["open_positions"] = remaining
    return closed


def open_new_signals(state: dict[str, Any], signals: list[Any], current: datetime) -> list[dict[str, Any]]:
    seen = set(state.get("seen_research_ids", []))
    active = {(str(x["profile"]), str(x["asset"]), str(x["side"])) for x in state.get("open_positions", [])}
    opened = []
    for signal in canonical_signals(signals):
        rid = research_id(signal)
        if rid in seen:
            continue
        seen.add(rid)
        profile = profile_name(signal.portfolio)
        overlap_key = (profile, str(signal.asset), str(signal.side))
        if overlap_key in active:
            state["skipped_overlap"] = int(state.get("skipped_overlap", 0)) + 1
            continue
        entry = float(signal.entry_reference_price)
        stop_pct = max(1e-6, float(signal.stop_pct))
        target_pct = max(1e-6, float(signal.target_pct))
        direction = 1.0 if str(signal.side) == "LONG" else -1.0
        risk_eur = 10.0
        position = {
            "research_id": rid,
            "experiment_group_id": str(signal.experiment_group_id),
            "profile": profile,
            "portfolio_source": str(signal.portfolio),
            "strategy": str(signal.strategy),
            "asset": str(signal.asset),
            "side": str(signal.side),
            "timeframe_minutes": int(signal.timeframe_minutes),
            "opened_at": current.isoformat(timespec="seconds"),
            "entry_price": entry,
            "stop_price": entry * (1.0 - direction * stop_pct),
            "target_price": entry * (1.0 + direction * target_pct),
            "stop_pct": stop_pct,
            "target_pct": target_pct,
            "max_holding_hours": int(signal.max_holding_hours),
            "normalized_risk_eur": risk_eur,
            "normalized_notional_eur": risk_eur / stop_pct,
            "score": float(signal.score),
            "confidence": str(signal.confidence),
        }
        state.setdefault("open_positions", []).append(position)
        active.add(overlap_key)
        opened.append(position)
    state["seen_research_ids"] = list(seen)[-100000:]
    return opened


def num(value: Any) -> float:
    try:
        x = float(value)
        return x if math.isfinite(x) else 0.0
    except Exception:
        return 0.0


def build_metrics(state: dict[str, Any], trades: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped = defaultdict(list)
    for trade in trades:
        grouped[str(trade.get("profile", "UNKNOWN"))].append(trade)
    open_counts = defaultdict(int)
    for row in state.get("open_positions", []):
        open_counts[str(row.get("profile", "UNKNOWN"))] += 1
    rows = []
    for profile in sorted(set(grouped) | set(open_counts)):
        items = grouped.get(profile, [])
        pnl = [num(x.get("net_pnl_eur")) for x in items]
        rvals = [num(x.get("r_multiple")) for x in items]
        wins = sum(x > 0 for x in pnl)
        gp = sum(x for x in pnl if x > 0)
        gl = -sum(x for x in pnl if x < 0)
        rows.append({
            "profile": profile,
            "open": open_counts.get(profile, 0),
            "closed": len(items),
            "independent_events": len({str(x.get("experiment_group_id", "")) for x in items if x.get("experiment_group_id")}),
            "win_rate_pct": wins / len(items) * 100.0 if items else 0.0,
            "profit_factor": gp / gl if gl > 0 else (math.inf if gp > 0 else 0.0),
            "expectancy_r": sum(rvals) / len(rvals) if rvals else 0.0,
            "net_pnl_eur": sum(pnl),
        })
    return rows


def fmt(value: Any) -> str:
    try:
        x = float(value)
        if math.isinf(x):
            return "∞"
        return f"{x:.2f}".replace(".", ",")
    except Exception:
        return "n/a"


def render_report(state: dict[str, Any], metrics: list[dict[str, Any]], opened: int, closed: int) -> str:
    trades = read_trades()
    independent = len({str(x.get("experiment_group_id", "")) for x in trades if x.get("experiment_group_id")})
    lines = [
        "## 🔬 Research All Signals", "",
        "Registro parallelo senza limite globale di quattro posizioni. Non modifica i conti paper e non genera ordini reali.", "",
        f"- Aperti in questo ciclo: **{opened}**",
        f"- Chiusi in questo ciclo: **{closed}**",
        f"- Posizioni research aperte: **{len(state.get('open_positions', []))}**",
        f"- Trade research chiusi: **{len(trades)}**",
        f"- Eventi di mercato indipendenti chiusi: **{independent}**",
        f"- Segnali sovrapposti saltati sullo stesso asset/profilo: **{int(state.get('skipped_overlap', 0))}**", "",
        "| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in metrics:
        lines.append(f"| {row['profile']} | {row['open']} | {row['closed']} | {row['independent_events']} | {fmt(row['win_rate_pct'])}% | {fmt(row['profit_factor'])} | {fmt(row['expectancy_r'])}R | €{fmt(row['net_pnl_eur'])} |")
    if not metrics:
        lines.append("| Nessun segnale ancora registrato | 0 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |")
    lines += ["", "Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto."]
    return "\n".join(lines)


def run_research_cycle(signals: list[Any], bundle: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    current = now_utc()
    state = load_state()
    closed_rows = update_open_positions(state, bundle, current)
    opened_rows = open_new_signals(state, signals, current)
    save_state(state)
    trades = read_trades()
    metrics = build_metrics(state, trades)
    report = render_report(state, metrics, len(opened_rows), len(closed_rows))
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report + "\n", encoding="utf-8")
    payload = {
        "generated_utc": current.isoformat(timespec="seconds"),
        "opened_this_cycle": len(opened_rows),
        "closed_this_cycle": len(closed_rows),
        "open_positions": len(state.get("open_positions", [])),
        "closed_trades": len(trades),
        "metrics": metrics,
        "report_markdown": report,
    }
    LATEST_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload
