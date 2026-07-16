# -*- coding: utf-8 -*-
"""Research ledger for every valid fresh signal, tagged by market regime."""

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
from market_regime_tagger import (
    classify_market_regime,
    persist_regime_snapshot,
)

REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "research_all_signals_state.json"
TRADES_PATH = REPORTS_DIR / "research_all_signals_trades.csv"
REPORT_PATH = REPORTS_DIR / "research_all_signals_report.md"
LATEST_PATH = REPORTS_DIR / "research_all_signals_latest.json"

TRADE_FIELDS = [
    "research_id",
    "experiment_group_id",
    "profile",
    "portfolio_source",
    "strategy",
    "asset",
    "side",
    "timeframe_minutes",
    "opened_at",
    "closed_at",
    "entry_price",
    "exit_price",
    "stop_price",
    "target_price",
    "stop_pct",
    "target_pct",
    "holding_hours",
    "close_reason",
    "normalized_risk_eur",
    "normalized_notional_eur",
    "gross_pnl_eur",
    "costs_eur",
    "net_pnl_eur",
    "r_multiple",
    "score",
    "confidence",
    "entry_regime",
    "entry_regime_family",
    "entry_regime_confidence",
    "entry_volatility_state",
    "entry_btc_trend_score",
    "entry_btc_adx",
    "entry_breadth_above_ema50_pct",
    "entry_alt_relative_median_pct",
    "entry_dispersion_pct",
    "exit_regime",
    "exit_regime_family",
    "exit_regime_confidence",
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_time(value: Any) -> datetime:
    stamp = pd.Timestamp(value)
    if stamp.tzinfo is None:
        stamp = stamp.tz_localize("UTC")
    return stamp.to_pydatetime().astimezone(
        timezone.utc
    )


def profile_name(portfolio: str) -> str:
    raw = str(portfolio)
    if raw.startswith("SHADOW_RSI_LONG_"):
        return "RSI_EXTREME_LONG_15M"
    if raw.startswith("SHADOW_RSI_SHORT_"):
        return "RSI_EXTREME_SHORT_15M"
    return raw


# RESEARCH_PROFILE_LABELS_V2
def research_profile_label(profile: Any) -> str:
    labels = {
        "SHADOW_RELATIVE_STRENGTH": "Forza relativa 1H V1",
        "SHADOW_RELATIVE_STRENGTH_V2": "Forza relativa 1H V2",
    }
    return labels.get(str(profile), str(profile))


def _empty_state() -> dict[str, Any]:
    current = now_utc().isoformat(
        timespec="seconds"
    )
    return {
        "schema_version": 2,
        "created_utc": current,
        "updated_utc": current,
        "seen_research_ids": [],
        "open_positions": [],
        "skipped_overlap": 0,
        "legacy_open_positions_discarded": 0,
    }


def load_state() -> dict[str, Any]:
    state = _empty_state()
    if STATE_PATH.exists():
        try:
            loaded = json.loads(
                STATE_PATH.read_text(
                    encoding="utf-8"
                )
            )
            if isinstance(loaded, dict):
                state.update(loaded)
        except Exception:
            pass

    schema = int(state.get("schema_version", 1))
    if schema < 2:
        old_positions = list(
            state.get("open_positions", [])
        )
        valid_positions = [
            row
            for row in old_positions
            if row.get("entry_regime")
        ]
        discarded = (
            len(old_positions) - len(valid_positions)
        )
        state["open_positions"] = valid_positions
        state["legacy_open_positions_discarded"] = (
            int(
                state.get(
                    "legacy_open_positions_discarded",
                    0,
                )
            )
            + discarded
        )
        state["schema_version"] = 2
    state.setdefault("seen_research_ids", [])
    state.setdefault("open_positions", [])
    state.setdefault("skipped_overlap", 0)
    state.setdefault(
        "legacy_open_positions_discarded",
        0,
    )
    return state


def save_state(state: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    state["schema_version"] = 2
    state["updated_utc"] = now_utc().isoformat(
        timespec="seconds"
    )
    temp = STATE_PATH.with_suffix(".json.tmp")
    temp.write_text(
        json.dumps(
            state,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    temp.replace(STATE_PATH)


def ensure_trade_schema() -> None:
    if not TRADES_PATH.exists():
        return
    try:
        with TRADES_PATH.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as handle:
            reader = csv.DictReader(handle)
            old_fields = list(
                reader.fieldnames or []
            )
            rows = list(reader)
    except Exception:
        return

    if old_fields == TRADE_FIELDS:
        return

    temp = TRADES_PATH.with_suffix(".csv.tmp")
    with temp.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=TRADE_FIELDS,
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    field: row.get(field, "")
                    for field in TRADE_FIELDS
                }
            )
    temp.replace(TRADES_PATH)


def append_trade(row: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    ensure_trade_schema()
    exists = (
        TRADES_PATH.exists()
        and TRADES_PATH.stat().st_size > 0
    )
    with TRADES_PATH.open(
        "a",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=TRADE_FIELDS,
            extrasaction="ignore",
        )
        if not exists:
            writer.writeheader()
        writer.writerow(
            {
                field: row.get(field, "")
                for field in TRADE_FIELDS
            }
        )


def read_trades() -> list[dict[str, Any]]:
    ensure_trade_schema()
    if not TRADES_PATH.exists():
        return []
    with TRADES_PATH.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        return list(csv.DictReader(handle))


def canonical_signals(
    signals: list[Any],
) -> list[Any]:
    chosen: dict[
        tuple[str, str, int, str, str],
        Any,
    ] = {}
    for signal in signals:
        key = (
            profile_name(signal.portfolio),
            str(signal.asset),
            int(signal.timeframe_minutes),
            str(signal.candle_time),
            str(signal.side),
        )
        current = chosen.get(key)
        if (
            current is None
            or abs(float(signal.score))
            > abs(float(current.score))
        ):
            chosen[key] = signal
    return list(chosen.values())


def research_id(signal: Any) -> str:
    return "|".join(
        [
            profile_name(signal.portfolio),
            str(signal.asset),
            str(signal.timeframe_minutes),
            str(signal.candle_time),
            str(signal.side),
        ]
    )


def mark_prices(
    bundle: dict[str, Any],
) -> dict[str, float]:
    output: dict[str, float] = {}
    for asset, payload in bundle.get(
        "assets",
        {},
    ).items():
        try:
            output[str(asset)] = float(
                payload.get("mark_price")
            )
        except Exception:
            pass
    return output


def _regime_entry_fields(
    regime: dict[str, Any],
) -> dict[str, Any]:
    features = dict(regime.get("features", {}))
    return {
        "entry_regime": str(
            regime.get("regime", "UNKNOWN")
        ),
        "entry_regime_family": str(
            regime.get(
                "regime_family",
                "UNKNOWN",
            )
        ),
        "entry_regime_confidence": float(
            regime.get("confidence_pct", 0.0)
        ),
        "entry_volatility_state": str(
            regime.get(
                "volatility_state",
                "UNKNOWN",
            )
        ),
        "entry_btc_trend_score": float(
            features.get(
                "btc_trend_score",
                0.0,
            )
        ),
        "entry_btc_adx": float(
            features.get("btc_adx", 0.0)
        ),
        "entry_breadth_above_ema50_pct": float(
            features.get(
                "breadth_above_ema50_pct",
                0.0,
            )
        ),
        "entry_alt_relative_median_pct": float(
            features.get(
                "alt_relative_median_pct",
                0.0,
            )
        ),
        "entry_dispersion_pct": float(
            features.get(
                "cross_asset_dispersion_pct",
                0.0,
            )
        ),
    }


def close_trade(
    position: dict[str, Any],
    exit_price: float,
    reason: str,
    when: datetime,
    exit_regime: dict[str, Any],
) -> dict[str, Any]:
    entry = float(position["entry_price"])
    direction = (
        1.0
        if position["side"] == "LONG"
        else -1.0
    )
    risk_eur = float(
        position["normalized_risk_eur"]
    )
    notional = float(
        position["normalized_notional_eur"]
    )
    gross = (
        direction
        * (float(exit_price) / entry - 1.0)
        * notional
    )
    costs = notional * 0.0008 * 2.0
    net = gross - costs
    opened = parse_time(position["opened_at"])
    row = {
        **position,
        "closed_at": when.isoformat(
            timespec="seconds"
        ),
        "exit_price": float(exit_price),
        "holding_hours": max(
            0.0,
            (when - opened).total_seconds()
            / 3600.0,
        ),
        "close_reason": reason,
        "gross_pnl_eur": gross,
        "costs_eur": costs,
        "net_pnl_eur": net,
        "r_multiple": (
            net / risk_eur
            if risk_eur > 0
            else 0.0
        ),
        "exit_regime": str(
            exit_regime.get(
                "regime",
                "UNKNOWN",
            )
        ),
        "exit_regime_family": str(
            exit_regime.get(
                "regime_family",
                "UNKNOWN",
            )
        ),
        "exit_regime_confidence": float(
            exit_regime.get(
                "confidence_pct",
                0.0,
            )
        ),
    }
    append_trade(row)
    return row


def update_open_positions(
    state: dict[str, Any],
    bundle: dict[str, Any],
    current: datetime,
    current_regime: dict[str, Any],
) -> list[dict[str, Any]]:
    frames = bundle_frames(bundle)
    prices = mark_prices(bundle)
    remaining: list[dict[str, Any]] = []
    closed: list[dict[str, Any]] = []

    for position in state.get(
        "open_positions",
        [],
    ):
        asset = str(position["asset"])
        timeframe = int(
            position["timeframe_minutes"]
        )
        frame = frames.get(
            asset,
            {},
        ).get(timeframe)
        stop = float(position["stop_price"])
        target = float(
            position["target_price"]
        )
        opened = parse_time(
            position["opened_at"]
        )
        exit_price = None
        reason = ""
        exit_time = current

        if frame is not None and not frame.empty:
            for stamp, candle in (
                frame.sort_index().iterrows()
            ):
                candle_time = parse_time(stamp)
                if candle_time <= opened:
                    continue
                if position["side"] == "LONG":
                    stop_hit = (
                        float(candle["low"]) <= stop
                    )
                    target_hit = (
                        float(candle["high"])
                        >= target
                    )
                else:
                    stop_hit = (
                        float(candle["high"])
                        >= stop
                    )
                    target_hit = (
                        float(candle["low"])
                        <= target
                    )

                if stop_hit and target_hit:
                    exit_price = stop
                    reason = (
                        "STOP_SAME_CANDLE_"
                        "CONSERVATIVE"
                    )
                    exit_time = candle_time
                    break
                if stop_hit:
                    exit_price = stop
                    reason = "STOP"
                    exit_time = candle_time
                    break
                if target_hit:
                    exit_price = target
                    reason = "TARGET"
                    exit_time = candle_time
                    break

        if (
            exit_price is None
            and (
                current - opened
            ).total_seconds()
            / 3600.0
            >= float(
                position.get(
                    "max_holding_hours",
                    168,
                )
            )
        ):
            exit_price = float(
                prices.get(
                    asset,
                    position["entry_price"],
                )
            )
            reason = "TIME_EXIT"
            exit_time = current

        if exit_price is None:
            remaining.append(position)
        else:
            closed.append(
                close_trade(
                    position,
                    float(exit_price),
                    reason,
                    exit_time,
                    current_regime,
                )
            )

    state["open_positions"] = remaining
    return closed


def open_new_signals(
    state: dict[str, Any],
    signals: list[Any],
    current: datetime,
    current_regime: dict[str, Any],
) -> list[dict[str, Any]]:
    seen = set(
        state.get("seen_research_ids", [])
    )
    active = {
        (
            str(row["profile"]),
            str(row["asset"]),
            str(row["side"]),
        )
        for row in state.get(
            "open_positions",
            [],
        )
    }
    opened: list[dict[str, Any]] = []

    for signal in canonical_signals(signals):
        rid = research_id(signal)
        if rid in seen:
            continue
        seen.add(rid)
        profile = profile_name(
            signal.portfolio
        )
        overlap_key = (
            profile,
            str(signal.asset),
            str(signal.side),
        )
        if overlap_key in active:
            state["skipped_overlap"] = (
                int(
                    state.get(
                        "skipped_overlap",
                        0,
                    )
                )
                + 1
            )
            continue

        entry = float(
            signal.entry_reference_price
        )
        stop_pct = max(
            1e-6,
            float(signal.stop_pct),
        )
        target_pct = max(
            1e-6,
            float(signal.target_pct),
        )
        direction = (
            1.0
            if str(signal.side) == "LONG"
            else -1.0
        )
        risk_eur = 10.0

        position = {
            "research_id": rid,
            "experiment_group_id": str(
                signal.experiment_group_id
            ),
            "profile": profile,
            "portfolio_source": str(
                signal.portfolio
            ),
            "strategy": str(
                signal.strategy
            ),
            "asset": str(signal.asset),
            "side": str(signal.side),
            "timeframe_minutes": int(
                signal.timeframe_minutes
            ),
            "opened_at": current.isoformat(
                timespec="seconds"
            ),
            "entry_price": entry,
            "stop_price": (
                entry
                * (
                    1.0
                    - direction * stop_pct
                )
            ),
            "target_price": (
                entry
                * (
                    1.0
                    + direction * target_pct
                )
            ),
            "stop_pct": stop_pct,
            "target_pct": target_pct,
            "max_holding_hours": int(
                signal.max_holding_hours
            ),
            "normalized_risk_eur": risk_eur,
            "normalized_notional_eur": (
                risk_eur / stop_pct
            ),
            "score": float(signal.score),
            "confidence": str(
                signal.confidence
            ),
            **_regime_entry_fields(
                current_regime
            ),
        }
        state.setdefault(
            "open_positions",
            [],
        ).append(position)
        active.add(overlap_key)
        opened.append(position)

    state["seen_research_ids"] = list(
        seen
    )[-100000:]
    return opened


def num(value: Any) -> float:
    try:
        number = float(value)
        return (
            number
            if math.isfinite(number)
            else 0.0
        )
    except Exception:
        return 0.0


def _metric_row(
    profile: str,
    regime: str,
    open_count: int,
    items: list[dict[str, Any]],
) -> dict[str, Any]:
    pnl = [
        num(row.get("net_pnl_eur"))
        for row in items
    ]
    r_values = [
        num(row.get("r_multiple"))
        for row in items
    ]
    wins = sum(value > 0 for value in pnl)
    gross_profit = sum(
        value
        for value in pnl
        if value > 0
    )
    gross_loss = -sum(
        value
        for value in pnl
        if value < 0
    )
    return {
        "profile": profile,
        "regime": regime,
        "open": open_count,
        "closed": len(items),
        "independent_events": len(
            {
                str(
                    row.get(
                        "experiment_group_id",
                        "",
                    )
                )
                for row in items
                if row.get(
                    "experiment_group_id"
                )
            }
        ),
        "win_rate_pct": (
            wins / len(items) * 100.0
            if items
            else 0.0
        ),
        "profit_factor": (
            gross_profit / gross_loss
            if gross_loss > 0
            else (
                math.inf
                if gross_profit > 0
                else 0.0
            )
        ),
        "expectancy_r": (
            sum(r_values) / len(r_values)
            if r_values
            else 0.0
        ),
        "net_pnl_eur": sum(pnl),
    }


def build_profile_metrics(
    state: dict[str, Any],
    trades: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    grouped: dict[
        str,
        list[dict[str, Any]],
    ] = defaultdict(list)
    for trade in trades:
        grouped[
            str(
                trade.get(
                    "profile",
                    "UNKNOWN",
                )
            )
        ].append(trade)

    open_counts: dict[str, int] = defaultdict(int)
    for row in state.get(
        "open_positions",
        [],
    ):
        open_counts[
            str(
                row.get(
                    "profile",
                    "UNKNOWN",
                )
            )
        ] += 1

    rows = []
    for profile in sorted(
        set(grouped) | set(open_counts)
    ):
        rows.append(
            _metric_row(
                profile,
                "ALL",
                open_counts.get(profile, 0),
                grouped.get(profile, []),
            )
        )
    return rows


def build_regime_matrix(
    state: dict[str, Any],
    trades: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    grouped: dict[
        tuple[str, str],
        list[dict[str, Any]],
    ] = defaultdict(list)
    for trade in trades:
        key = (
            str(
                trade.get(
                    "profile",
                    "UNKNOWN",
                )
            ),
            str(
                trade.get(
                    "entry_regime",
                    "LEGACY_UNKNOWN",
                )
                or "LEGACY_UNKNOWN"
            ),
        )
        grouped[key].append(trade)

    open_counts: dict[
        tuple[str, str],
        int,
    ] = defaultdict(int)
    for row in state.get(
        "open_positions",
        [],
    ):
        key = (
            str(
                row.get(
                    "profile",
                    "UNKNOWN",
                )
            ),
            str(
                row.get(
                    "entry_regime",
                    "UNKNOWN",
                )
            ),
        )
        open_counts[key] += 1

    rows = []
    for profile, regime in sorted(
        set(grouped) | set(open_counts)
    ):
        rows.append(
            _metric_row(
                profile,
                regime,
                open_counts.get(
                    (profile, regime),
                    0,
                ),
                grouped.get(
                    (profile, regime),
                    [],
                ),
            )
        )
    return rows


def fmt(value: Any) -> str:
    try:
        number = float(value)
        if math.isinf(number):
            return "∞"
        return f"{number:.2f}".replace(
            ".",
            ",",
        )
    except Exception:
        return "n/a"


def render_report(
    state: dict[str, Any],
    metrics: list[dict[str, Any]],
    regime_matrix: list[dict[str, Any]],
    opened: int,
    closed: int,
    current_regime: dict[str, Any],
) -> str:
    trades = read_trades()
    independent = len(
        {
            str(
                row.get(
                    "experiment_group_id",
                    "",
                )
            )
            for row in trades
            if row.get("experiment_group_id")
        }
    )
    regime = str(
        current_regime.get(
            "regime",
            "UNKNOWN",
        )
    )
    family = str(
        current_regime.get(
            "regime_family",
            "UNKNOWN",
        )
    )
    confidence = float(
        current_regime.get(
            "confidence_pct",
            0.0,
        )
    )
    volatility = str(
        current_regime.get(
            "volatility_state",
            "UNKNOWN",
        )
    )
    features = dict(
        current_regime.get(
            "features",
            {},
        )
    )

    lines = [
        "## 🔬 Research All Signals",
        "",
        (
            "Registro parallelo senza limite globale "
            "di quattro posizioni. Considera soltanto "
            "segnali validi con dati freschi; non "
            "modifica i conti paper e non genera "
            "ordini reali."
        ),
        "",
        "### Regime di mercato osservato",
        "",
        f"- Regime: **{regime}**",
        f"- Famiglia: **{family}**",
        f"- Confidenza: **{fmt(confidence)}%**",
        f"- Volatilità: **{volatility}**",
        (
            "- Rotazione strategie: "
            "**SOLO OSSERVAZIONE — nessun peso "
            "operativo viene ancora modificato**"
        ),
        (
            "- Motivo: "
            f"{current_regime.get('reason', 'n/a')}"
        ),
        (
            "- BTC trend score: "
            f"**{fmt(features.get('btc_trend_score', 0.0))}**; "
            "ADX: "
            f"**{fmt(features.get('btc_adx', 0.0))}**; "
            "breadth sopra EMA50: "
            f"**{fmt(features.get('breadth_above_ema50_pct', 0.0))}%**"
        ),
        (
            "- Mediana alt vs BTC: "
            f"**{fmt(features.get('alt_relative_median_pct', 0.0))}%**; "
            "dispersione: "
            f"**{fmt(features.get('cross_asset_dispersion_pct', 0.0))}%**"
        ),
        "",
        f"- Aperti in questo ciclo: **{opened}**",
        f"- Chiusi in questo ciclo: **{closed}**",
        (
            "- Posizioni research aperte: "
            f"**{len(state.get('open_positions', []))}**"
        ),
        (
            "- Trade research chiusi: "
            f"**{len(trades)}**"
        ),
        (
            "- Eventi di mercato indipendenti "
            f"chiusi: **{independent}**"
        ),
        (
            "- Segnali sovrapposti saltati sullo "
            "stesso asset/profilo: "
            f"**{int(state.get('skipped_overlap', 0))}**"
        ),
    ]

    discarded = int(
        state.get(
            "legacy_open_positions_discarded",
            0,
        )
    )
    if discarded:
        lines.append(
            (
                "- Posizioni Research V1 senza regime "
                f"scartate durante la migrazione: **{discarded}**"
            )
        )

    lines.extend(
        [
            "",
            "### Risultati complessivi per strategia",
            "",
            (
                "| Profilo | Aperte | Chiuse | "
                "Eventi indip. | Win rate | PF | "
                "Expectancy R | P&L norm. |"
            ),
            (
                "| --- | ---: | ---: | ---: | "
                "---: | ---: | ---: | ---: |"
            ),
        ]
    )
    for row in metrics:
        lines.append(
            (
                f"| {research_profile_label(row['profile'])} | {row['open']} | "
                f"{row['closed']} | "
                f"{row['independent_events']} | "
                f"{fmt(row['win_rate_pct'])}% | "
                f"{fmt(row['profit_factor'])} | "
                f"{fmt(row['expectancy_r'])}R | "
                f"€{fmt(row['net_pnl_eur'])} |"
            )
        )
    if not metrics:
        lines.append(
            (
                "| Nessun segnale ancora registrato | "
                "0 | 0 | 0 | 0,00% | 0,00 | "
                "0,00R | €0,00 |"
            )
        )

    lines.extend(
        [
            "",
            "### Matrice strategia × regime all’entrata",
            "",
            (
                "| Profilo | Regime entrata | Aperte | "
                "Chiuse | Eventi indip. | Win rate | "
                "PF | Expectancy R | P&L norm. |"
            ),
            (
                "| --- | --- | ---: | ---: | ---: | "
                "---: | ---: | ---: | ---: |"
            ),
        ]
    )
    for row in regime_matrix:
        lines.append(
            (
                f"| {research_profile_label(row['profile'])} | {row['regime']} | "
                f"{row['open']} | {row['closed']} | "
                f"{row['independent_events']} | "
                f"{fmt(row['win_rate_pct'])}% | "
                f"{fmt(row['profit_factor'])} | "
                f"{fmt(row['expectancy_r'])}R | "
                f"€{fmt(row['net_pnl_eur'])} |"
            )
        )
    if not regime_matrix:
        lines.append(
            (
                "| Nessun dato per regime | n/a | 0 | "
                "0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |"
            )
        )

    lines.extend(
        [
            "",
            (
                "Il P&L è normalizzato a **€10 di "
                "rischio per evento**, così leva e size "
                "non falsano il confronto."
            ),
            (
                "La matrice diventerà utilizzabile per "
                "una rotazione automatica soltanto dopo "
                "un campione sufficiente per ciascuna "
                "coppia strategia-regime."
            ),
        ]
    )
    return "\n".join(lines)


def run_research_cycle(
    signals: list[Any],
    bundle: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    current = now_utc()
    current_regime = classify_market_regime(
        bundle
    )
    persist_regime_snapshot(
        current_regime
    )

    state = load_state()
    closed_rows = update_open_positions(
        state,
        bundle,
        current,
        current_regime,
    )
    opened_rows = open_new_signals(
        state,
        signals,
        current,
        current_regime,
    )
    save_state(state)

    trades = read_trades()
    metrics = build_profile_metrics(
        state,
        trades,
    )
    regime_matrix = build_regime_matrix(
        state,
        trades,
    )
    report = render_report(
        state,
        metrics,
        regime_matrix,
        len(opened_rows),
        len(closed_rows),
        current_regime,
    )

    REPORTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )
    REPORT_PATH.write_text(
        report + "\n",
        encoding="utf-8",
    )
    payload = {
        "generated_utc": current.isoformat(
            timespec="seconds"
        ),
        "current_regime": current_regime,
        "opened_this_cycle": len(opened_rows),
        "closed_this_cycle": len(closed_rows),
        "open_positions": len(
            state.get("open_positions", [])
        ),
        "closed_trades": len(trades),
        "metrics": metrics,
        "regime_matrix": regime_matrix,
        "report_markdown": report,
    }
    LATEST_PATH.write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return payload
