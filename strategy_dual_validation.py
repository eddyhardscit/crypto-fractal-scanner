# -*- coding: utf-8 -*-
"""Joint qualification view for Research All Signals and realistic paper accounts."""

from __future__ import annotations

import math
from typing import Any

from research_all_signals import profile_name

MIN_INDEPENDENT_EVENTS = 30
MIN_PROFIT_FACTOR = 1.10
MAX_PAPER_DRAWDOWN_PCT = 15.0


def _number(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if math.isfinite(number) else number
    except Exception:
        return default


def _integer(value: Any) -> int:
    try:
        return max(0, int(float(value)))
    except Exception:
        return 0


def _fmt(value: Any, digits: int = 2) -> str:
    try:
        number = float(value)
        if math.isinf(number):
            return "∞"
        return f"{number:.{digits}f}".replace(".", ",")
    except Exception:
        return "n/a"


def _paper_profile(row: dict[str, Any]) -> str:
    return profile_name(str(row.get("portfolio", "UNKNOWN")))


def _paper_representatives(
    paper_metrics: list[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], dict[str, int]]:
    """Select the most mature paper account for every research profile.

    Most profiles map one-to-one. RSI experiments intentionally map many
    leverage/margin variants to one research family; selecting one mature
    account prevents duplicated market events from being added together.
    """
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in paper_metrics:
        grouped.setdefault(_paper_profile(row), []).append(row)

    representatives: dict[str, dict[str, Any]] = {}
    variant_counts: dict[str, int] = {}
    for profile, candidates in grouped.items():
        variant_counts[profile] = len(candidates)
        representatives[profile] = max(
            candidates,
            key=lambda row: (
                _integer(row.get("unique_market_events")),
                _integer(row.get("closed_trades")),
                int(bool(row.get("is_main"))),
                str(row.get("portfolio", "")),
            ),
        )
    return representatives, variant_counts


def _agreement(
    research_pf: float,
    research_expectancy: float,
    paper_pf: float,
    paper_expectancy: float,
    research_events: int,
    paper_events: int,
) -> str:
    if research_events == 0 or paper_events == 0:
        return "n/a"
    research_positive = research_pf >= 1.0 and research_expectancy > 0.0
    paper_positive = paper_pf >= 1.0 and paper_expectancy > 0.0
    if research_positive and paper_positive:
        return "COERENTE +"
    if not research_positive and not paper_positive:
        return "COERENTE −"
    return "DIVERGENTE"


def _status(
    research_events: int,
    paper_events: int,
    research_pf: float,
    research_expectancy: float,
    paper_pf: float,
    paper_expectancy: float,
    paper_drawdown: float,
    min_events: int,
    min_profit_factor: float,
    max_paper_drawdown_pct: float,
) -> str:
    research_complete = research_events >= min_events
    paper_complete = paper_events >= min_events
    research_edge = (
        research_pf >= min_profit_factor
        and research_expectancy > 0.0
    )
    paper_edge = (
        paper_pf >= min_profit_factor
        and paper_expectancy > 0.0
        and paper_drawdown <= max_paper_drawdown_pct
    )

    if not research_complete:
        return "RACCOLTA RESEARCH"
    if not research_edge:
        return "BOCCIATA RESEARCH"
    if not paper_complete:
        return "SEGNALE VALIDATO · PAPER IN RACCOLTA"
    if not paper_edge:
        return "BOCCIATA PAPER"
    return "PRONTA PER REVISIONE LIVE"


def build_dual_validation_report(
    paper_metrics: list[dict[str, Any]],
    research_metrics: list[dict[str, Any]],
    *,
    min_events: int = MIN_INDEPENDENT_EVENTS,
    min_profit_factor: float = MIN_PROFIT_FACTOR,
    max_paper_drawdown_pct: float = MAX_PAPER_DRAWDOWN_PCT,
) -> dict[str, Any]:
    """Build one qualification row per strategy profile.

    Research and paper counters remain separate. The function never adds
    them because many paper trades are a subset of the research events.
    """
    paper_by_profile, variant_counts = _paper_representatives(paper_metrics)
    research_by_profile = {
        str(row.get("profile", "UNKNOWN")): row
        for row in research_metrics
    }
    profiles = sorted(set(paper_by_profile) | set(research_by_profile))

    rows: list[dict[str, Any]] = []
    for profile in profiles:
        paper = paper_by_profile.get(profile, {})
        research = research_by_profile.get(profile, {})

        research_events = _integer(research.get("independent_events"))
        paper_events = _integer(paper.get("unique_market_events"))
        research_pf = _number(research.get("profit_factor"))
        paper_pf = _number(paper.get("profit_factor"))
        research_expectancy = _number(research.get("expectancy_r"))
        paper_expectancy = _number(paper.get("expectancy_eur"))
        paper_drawdown = _number(paper.get("max_drawdown_pct"))

        status = _status(
            research_events,
            paper_events,
            research_pf,
            research_expectancy,
            paper_pf,
            paper_expectancy,
            paper_drawdown,
            min_events,
            min_profit_factor,
            max_paper_drawdown_pct,
        )
        rows.append(
            {
                "profile": profile,
                "paper_portfolio": str(paper.get("portfolio", "n/a")),
                "paper_label": str(
                    paper.get("portfolio_label", paper.get("portfolio", "n/a"))
                ),
                "paper_variants": variant_counts.get(profile, 0),
                "research_events": research_events,
                "paper_events": paper_events,
                "research_closed_trades": _integer(research.get("closed")),
                "paper_closed_trades": _integer(paper.get("closed_trades")),
                "research_profit_factor": research_pf,
                "paper_profit_factor": paper_pf,
                "research_expectancy_r": research_expectancy,
                "paper_expectancy_eur": paper_expectancy,
                "paper_max_drawdown_pct": paper_drawdown,
                "agreement": _agreement(
                    research_pf,
                    research_expectancy,
                    paper_pf,
                    paper_expectancy,
                    research_events,
                    paper_events,
                ),
                "status": status,
            }
        )

    status_counts: dict[str, int] = {}
    for row in rows:
        status = str(row["status"])
        status_counts[status] = status_counts.get(status, 0) + 1

    lines = [
        "## 🧪 Validazione congiunta Research + Paper",
        "",
        (
            "I due campioni vengono letti insieme ma **non sommati**: "
            "il paper è normalmente un sottoinsieme dei segnali Research. "
            "La soglia usa gli **eventi di mercato indipendenti**."
        ),
        "",
        (
            f"Requisiti per la revisione live: almeno **{min_events} eventi "
            "indipendenti per lato**, PF almeno "
            f"**{_fmt(min_profit_factor)}**, expectancy positiva e max drawdown "
            f"paper non superiore a **{_fmt(max_paper_drawdown_pct)}%**."
        ),
        "",
        (
            "| Profilo | Conto paper di riferimento | Research eventi | "
            "Paper eventi | PF Research | PF Paper | Exp. Research | "
            "Exp. Paper | DD Paper | Accordo | Stato |"
        ),
        (
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | "
            "---: | --- | --- |"
        ),
    ]

    for row in rows:
        account = row["paper_label"]
        if row["paper_variants"] > 1:
            account = (
                f"{account} (riferimento tra "
                f"{row['paper_variants']} varianti)"
            )
        lines.append(
            (
                f"| {row['profile']} | {account} | "
                f"{row['research_events']}/{min_events} | "
                f"{row['paper_events']}/{min_events} | "
                f"{_fmt(row['research_profit_factor'])} | "
                f"{_fmt(row['paper_profit_factor'])} | "
                f"{_fmt(row['research_expectancy_r'])}R | "
                f"€{_fmt(row['paper_expectancy_eur'])} | "
                f"{_fmt(row['paper_max_drawdown_pct'])}% | "
                f"{row['agreement']} | {row['status']} |"
            )
        )

    if not rows:
        lines.append(
            "| Nessuna strategia | n/a | 0/30 | 0/30 | 0,00 | 0,00 | "
            "0,00R | €0,00 | 0,00% | n/a | RACCOLTA DATI |"
        )

    lines.extend(
        [
            "",
            (
                "Per le famiglie RSI con più configurazioni di leva o margine, "
                "il lato paper usa il conto con il maggior numero di eventi "
                "indipendenti; i conti duplicati non vengono aggregati."
            ),
            (
                "`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta "
                "capitale: abilita soltanto una revisione manuale finale."
            ),
        ]
    )

    return {
        "rows": rows,
        "status_counts": status_counts,
        "ready_for_live_review": status_counts.get(
            "PRONTA PER REVISIONE LIVE", 0
        ),
        "report_markdown": "\n".join(lines),
        "thresholds": {
            "min_independent_events": min_events,
            "min_profit_factor": min_profit_factor,
            "max_paper_drawdown_pct": max_paper_drawdown_pct,
        },
    }
