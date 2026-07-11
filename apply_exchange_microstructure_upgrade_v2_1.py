# -*- coding: utf-8 -*-
"""Install the Exchange Microstructure upgrade v2.1 in an existing scanner repo.

This patch is idempotent. It:
- adds a candidate exchange signal to calibration while Global stays weight 0 until the 7-day gate matures;
- adds the module to module-signal calibration;
- adds compact report sections;
- adds exchange files to Data Quality;
- restores intraday state from redundant GitHub Release assets;
- archives completed months permanently;
- prepares .github/workflows/daily.yml with dependency-safe execution order.

The one-time GitHub workflow commits only Python source patches. The prepared
``daily.yml`` is uploaded as an artifact so GitHub's workflow-file permission
restriction is not triggered.
"""

from __future__ import annotations

import argparse
import py_compile
import re
import shutil
from pathlib import Path


GLOBAL_PATH = Path("global_confluence_report.py")
MODULE_TRACKER_PATH = Path("module_signal_tracker.py")
COMPACT_PATH = Path("compact_latest_report.py")
QUALITY_PATH = Path("data_quality_coherence_report.py")
WORKFLOW_PATH = Path(".github/workflows/daily.yml")
GITIGNORE_PATH = Path(".gitignore")

NEW_FILES = (
    Path("exchange_market_data.py"),
    Path("exchange_microstructure_report.py"),
    Path("exchange_signal_tracker.py"),
    Path("exchange_microstructure_selftest.py"),
    Path("exchange_persistent_storage.py"),
    Path("requirements-exchange.txt"),
    Path("requirements-exchange-collector.txt"),
)

PATCHED_FILES = (GLOBAL_PATH, MODULE_TRACKER_PATH, COMPACT_PATH, QUALITY_PATH)

GLOBAL_MARKER = "# EXCHANGE_MICROSTRUCTURE_GLOBAL_PATCH_V2_1"
TRACKER_MARKER = "# EXCHANGE_MICROSTRUCTURE_TRACKER_PATCH_V2_1"
COMPACT_MARKER = "# EXCHANGE_MICROSTRUCTURE_COMPACT_PATCH_V2_1"
QUALITY_MARKER = "# EXCHANGE_MICROSTRUCTURE_QUALITY_PATCH_V2_1"


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"File mancante nella radice del repository: {path}")
    return path.read_text(encoding="utf-8")


def backup(path: Path, suffix: str) -> None:
    target = path.with_name(path.name + suffix)
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def write_if_changed(path: Path, original: str, updated: str, backup_suffix: str) -> bool:
    if updated == original:
        print(f"{path}: già aggiornato.")
        return False
    backup(path, backup_suffix)
    path.write_text(updated, encoding="utf-8", newline="\n")
    print(f"{path}: aggiornato.")
    return True


def replace_once(text: str, old: str, new: str, description: str) -> str:
    if old not in text:
        raise RuntimeError(f"Punto patch non trovato ({description}).")
    return text.replace(old, new, 1)


def patch_global() -> bool:
    original = read(GLOBAL_PATH)
    if GLOBAL_MARKER in original:
        print("Global Confluence: patch exchange già presente.")
        return False
    text = original

    text = replace_once(
        text,
        'CLASSIC_TECH_METRICS_PATH = REPORTS_DIR / "classic_technical_confirmation_metrics.csv"\n',
        'CLASSIC_TECH_METRICS_PATH = REPORTS_DIR / "classic_technical_confirmation_metrics.csv"\n'
        'EXCHANGE_MICROSTRUCTURE_METRICS_PATH = REPORTS_DIR / "exchange_microstructure_metrics.csv"\n'
        f'{GLOBAL_MARKER}\n',
        "costante metriche exchange",
    )

    text = replace_once(
        text,
        '    "Lifecycle EMA",\n    "Futures",\n',
        '    "Lifecycle EMA",\n    "Exchange flow",\n',
        "weighted components; Futures precedente resta diagnostico",
    )

    parser_code = r'''
def parse_exchange_microstructure_component(asset: str):
    """Read structured exchange metrics; Global score is already calibration-gated."""
    if not EXCHANGE_MICROSTRUCTURE_METRICS_PATH.exists():
        return component_template(
            0,
            "Dati exchange non disponibili; modulo neutrale.",
            {"raw_score": None, "candidate_score": 0, "confidence": "MANCANTE", "bias": "n/a", "data_coverage": 0},
        )

    try:
        with EXCHANGE_MICROSTRUCTURE_METRICS_PATH.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except Exception as exc:
        return component_template(
            0,
            f"Metriche exchange non leggibili: {type(exc).__name__}.",
            {"raw_score": None, "candidate_score": 0, "confidence": "ERRORE", "bias": "n/a", "data_coverage": 0},
        )

    row = next((item for item in rows if clean_cell(item.get("asset", "")).upper() == asset), None)
    if row is None:
        return component_template(
            0,
            f"Riga exchange {asset} mancante; modulo neutrale.",
            {"raw_score": None, "candidate_score": 0, "confidence": "MANCANTE", "bias": "n/a", "data_coverage": 0},
        )

    raw_score = parse_number(row.get("raw_score"))
    candidate_score = max(-1, min(1, parse_int(row.get("candidate_global_score"), 0)))
    reported_score = max(-1, min(1, parse_int(row.get("global_score"), 0)))
    score = reported_score
    confidence = clean_cell(row.get("confidence", "")) or "n/a"
    bias = clean_cell(row.get("bias", "")) or "n/a"
    activation = clean_cell(row.get("global_activation_status", "")) or "n/a"
    coverage = parse_number(row.get("data_coverage"))
    exchange_count = parse_int(row.get("exchange_count"), 0)
    kucoin_available = clean_cell(row.get("kucoin_available", "")).lower() in {"true", "1", "yes", "si", "sì"}
    flow = parse_number(row.get("flow_score"))
    derivatives = parse_number(row.get("derivatives_score"))
    crowding = parse_number(row.get("crowding_score"))
    technical_confirmation = parse_number(row.get("technical_confirmation_score"))
    detail_text = clean_cell(row.get("detail", ""))
    if not detail_text:
        detail_text = (
            f"Raw {raw_score if raw_score is not None else 'n/a'}, candidato {candidate_score:+d}, "
            f"flow {flow if flow is not None else 'n/a'}, derivati {derivatives if derivatives is not None else 'n/a'}, "
            f"affollamento {crowding if crowding is not None else 'n/a'}, "
            f"conferme tecniche {technical_confirmation if technical_confirmation is not None else 'n/a'}."
        )
    detail = (
        f"{detail_text} Bias {bias}; confidenza {confidence}; fonti {exchange_count}/3; "
        f"KuCoin {'OK' if kucoin_available else 'mancante'}; "
        f"copertura {fmt_pct_plain(coverage * 100 if coverage is not None and coverage <= 1.0 else coverage)}. "
        f"Attivazione: {activation}. Il Global usa {score:+d}; il candidato {candidate_score:+d} resta misurato separatamente."
    )
    return component_template(
        score,
        detail,
        {
            "raw_score": raw_score,
            "candidate_score": candidate_score,
            "reported_score": reported_score,
            "confidence": confidence,
            "bias": bias,
            "activation_status": activation,
            "data_coverage": coverage,
            "exchange_count": exchange_count,
            "kucoin_available": kucoin_available,
            "flow_score": flow,
            "derivatives_score": derivatives,
            "crowding_score": crowding,
            "technical_confirmation_score": technical_confirmation,
        },
    )


'''

    text = replace_once(
        text,
        "def parse_futures_component(block: str, asset: str):\n",
        parser_code + "def parse_futures_component(block: str, asset: str):\n",
        "parser exchange",
    )

    text = replace_once(
        text,
        '            "Futures": parse_futures_component(futures_block, asset),\n',
        '            "Exchange flow": parse_exchange_microstructure_component(asset),\n'
        '            "Futures": parse_futures_component(futures_block, asset),\n',
        "build components exchange",
    )

    text = replace_once(
        text,
        '        "Lifecycle EMA",\n        "Futures",\n',
        '        "Lifecycle EMA",\n        "Exchange flow",\n        "Futures",\n',
        "component order exchange",
    )

    text = replace_once(
        text,
        '                fmt_signed_int(components[asset]["Lifecycle EMA"]["score"]),\n'
        '                fmt_signed_int(components[asset]["Futures"]["score"]),\n',
        '                fmt_signed_int(components[asset]["Lifecycle EMA"]["score"]),\n'
        '                fmt_signed_int(components[asset]["Exchange flow"]["score"]),\n'
        '                fmt_signed_int(components[asset]["Futures"]["score"]),\n',
        "score rows exchange",
    )

    text = replace_once(
        text,
        '    lines.append("- Futures / liquidazioni")\n',
        '    lines.append("- Exchange microstructure: OI, funding, taker flow, order book e liquidazioni campionate")\n'
        '    lines.append("- Futures / liquidazioni precedente, mantenuto come diagnostica")\n',
        "moduli report exchange",
    )

    text = replace_once(
        text,
        '    lines.append(\n        "Nota Classic technical: **pesa massimo ±1** perché è un filtro di conferma "\n'
        '        "e in parte si sovrappone alla struttura tecnica già esistente."\n'
        '    )\n',
        '    lines.append(\n        "Nota Classic technical: **pesa massimo ±1** perché è un filtro di conferma "\n'
        '        "e in parte si sovrappone alla struttura tecnica già esistente."\n'
        '    )\n'
        '    lines.append("")\n'
        '    lines.append(\n'
        '        "Nota exchange: **candidato massimo ±1, peso iniziale 0** e più conferme indipendenti. "\n'
        '        "Order book, funding o una singola liquidazione non bastano da soli."\n'
        '    )\n',
        "nota exchange",
    )

    text = replace_once(
        text,
        '                "Lifecycle EMA",\n                "Futures",\n',
        '                "Lifecycle EMA",\n                "Exchange flow",\n                "Futures",\n',
        "header score exchange",
    )

    text = replace_once(
        text,
        '        "futures_score",\n        "futures_reading",\n',
        '        "exchange_flow_score_component",\n'
        '        "exchange_candidate_score_component",\n'
        '        "exchange_global_activation_status",\n'
        '        "exchange_count",\n'
        '        "exchange_kucoin_available",\n'
        '        "exchange_raw_score",\n'
        '        "exchange_confidence",\n'
        '        "exchange_bias",\n'
        '        "exchange_data_coverage",\n'
        '        "exchange_flow_score",\n'
        '        "exchange_derivatives_score",\n'
        '        "exchange_crowding_score",\n'
        '        "exchange_technical_confirmation_score",\n'
        '        "futures_score",\n'
        '        "futures_reading",\n',
        "metric fields exchange",
    )

    text = replace_once(
        text,
        '            "futures_score": c["Futures"]["score"],\n'
        '            "futures_reading": c["Futures"]["data"].get("reading"),\n',
        '            "exchange_flow_score_component": c["Exchange flow"]["score"],\n'
        '            "exchange_candidate_score_component": c["Exchange flow"]["data"].get("candidate_score"),\n'
        '            "exchange_global_activation_status": c["Exchange flow"]["data"].get("activation_status"),\n'
        '            "exchange_count": c["Exchange flow"]["data"].get("exchange_count"),\n'
        '            "exchange_kucoin_available": c["Exchange flow"]["data"].get("kucoin_available"),\n'
        '            "exchange_raw_score": c["Exchange flow"]["data"].get("raw_score"),\n'
        '            "exchange_confidence": c["Exchange flow"]["data"].get("confidence"),\n'
        '            "exchange_bias": c["Exchange flow"]["data"].get("bias"),\n'
        '            "exchange_data_coverage": c["Exchange flow"]["data"].get("data_coverage"),\n'
        '            "exchange_flow_score": c["Exchange flow"]["data"].get("flow_score"),\n'
        '            "exchange_derivatives_score": c["Exchange flow"]["data"].get("derivatives_score"),\n'
        '            "exchange_crowding_score": c["Exchange flow"]["data"].get("crowding_score"),\n'
        '            "exchange_technical_confirmation_score": c["Exchange flow"]["data"].get("technical_confirmation_score"),\n'
        '            "futures_score": c["Futures"]["score"],\n'
        '            "futures_reading": c["Futures"]["data"].get("reading"),\n',
        "metric row exchange",
    )

    text = replace_once(
        text,
        '    lines.append(\n        "Nota Classic technical: il modulo è utile per capire se il setup è confermato davvero, "\n'
        '        "ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente."\n'
        '    )\n',
        '    lines.append(\n        "Nota Classic technical: il modulo è utile per capire se il setup è confermato davvero, "\n'
        '        "ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente."\n'
        '    )\n'
        '    lines.append("")\n'
        '    lines.append(\n'
        '        "Nota exchange: il modulo salva OI, funding, taker flow, order book e liquidazioni campionate. "\n'
        '        "Il candidato è limitato a ±1; il peso Global resta 0 finché il gate storico a 7 giorni non matura."\n'
        '    )\n',
        "nota finale exchange",
    )

    return write_if_changed(GLOBAL_PATH, original, text, ".bak_exchange_microstructure")


def patch_module_tracker() -> bool:
    original = read(MODULE_TRACKER_PATH)
    if TRACKER_MARKER in original:
        print("Module tracker: patch exchange già presente.")
        return False
    text = original

    module_block = '''    {
        "key": "exchange_microstructure",
        "label": "Microstruttura exchange",
        "score_col": "exchange_candidate_score_component",
        "role": "CALIBRABILE / NON PESATO FINO AL GATE",
        "calibratable": True,
        "parent_family": "",
    },
'''
    anchor = '''    {
        "key": "sol_fractal",
        "label": "Frattale SOL",
'''
    if anchor not in text:
        raise RuntimeError("Punto patch module tracker: sol_fractal non trovato.")
    text = text.replace(anchor, module_block + anchor, 1)

    text = replace_once(
        text,
        '    "classic_technical_score_component",\n    "sol_fractal_score",\n',
        '    "classic_technical_score_component",\n'
        '    "exchange_flow_score_component",\n'
        '    "exchange_candidate_score_component",\n'
        '    "exchange_global_activation_status",\n'
        '    "exchange_count",\n'
        '    "exchange_kucoin_available",\n'
        '    "exchange_raw_score",\n'
        '    "exchange_confidence",\n'
        '    "sol_fractal_score",\n',
        "history columns exchange",
    )

    text = replace_once(
        text,
        '            "classic_technical_score_component": safe_int(row.get("classic_technical_score_component"), 0),\n'
        '            "sol_fractal_score": safe_int(row.get("sol_fractal_score"), 0),\n',
        '            "classic_technical_score_component": safe_int(row.get("classic_technical_score_component"), 0),\n'
        '            "exchange_flow_score_component": safe_int(row.get("exchange_flow_score_component"), 0),\n'
        '            "exchange_candidate_score_component": safe_int(row.get("exchange_candidate_score_component"), 0),\n'
        '            "exchange_global_activation_status": safe_str(row.get("exchange_global_activation_status")),\n'
        '            "exchange_count": safe_int(row.get("exchange_count"), 0),\n'
        '            "exchange_kucoin_available": safe_str(row.get("exchange_kucoin_available")),\n'
        '            "exchange_raw_score": safe_float(row.get("exchange_raw_score")),\n'
        '            "exchange_confidence": safe_str(row.get("exchange_confidence")),\n'
        '            "sol_fractal_score": safe_int(row.get("sol_fractal_score"), 0),\n',
        "signal rows exchange",
    )

    text = replace_once(
        text,
        '    lines.append("- Classic technical confirmation")\n'
        '    lines.append("- Frattale SOL/BTC, solo per SOL")\n',
        '    lines.append("- Classic technical confirmation")\n'
        '    lines.append("- Microstruttura exchange, OI/funding/taker flow/order book")\n'
        '    lines.append("- Frattale SOL/BTC, solo per SOL")\n'
        f'    lines.append("{TRACKER_MARKER}")\n',
        "report list exchange",
    )

    return write_if_changed(MODULE_TRACKER_PATH, original, text, ".bak_exchange_microstructure")


def patch_compact() -> bool:
    original = read(COMPACT_PATH)
    if COMPACT_MARKER in original:
        print("Compact report: patch exchange già presente.")
        return False
    text = original

    anchor = '''    (
        "liquidations",
        "<!-- LIQUIDATION_SUMMARY_START -->",
'''
    insert = '''    (
        "exchange_microstructure",
        "<!-- EXCHANGE_MICROSTRUCTURE_START -->",
        "<!-- EXCHANGE_MICROSTRUCTURE_END -->",
        "🏦 Dati exchange, liquidità e leva",
        False,
    ),
    (
        "exchange_signal_tracker",
        "<!-- EXCHANGE_SIGNAL_TRACKER_START -->",
        "<!-- EXCHANGE_SIGNAL_TRACKER_END -->",
        "🧠 Accuratezza segnali exchange",
        False,
    ),
'''
    if anchor not in text:
        raise RuntimeError("Punto patch compact: sezione liquidations non trovata.")
    text = text.replace(anchor, insert + anchor, 1)

    # Marker as a harmless module-level comment, outside the tuple.
    text = replace_once(
        text,
        'SECTION_END = "<!-- COMPACT_SECTION_END:{key} -->"\n',
        'SECTION_END = "<!-- COMPACT_SECTION_END:{key} -->"\n'
        f'{COMPACT_MARKER}\n',
        "compact marker",
    )
    return write_if_changed(COMPACT_PATH, original, text, ".bak_exchange_microstructure")


def patch_quality() -> bool:
    original = read(QUALITY_PATH)
    if QUALITY_MARKER in original:
        print("Data Quality: patch exchange già presente.")
        return False
    text = original

    # The project has existed in two Data Quality layouts. Prefer the richer
    # MODULE_SPECS layout, but support the older compact checker as well.
    advanced_spec_anchor = '''    "RSI top-cycle": {
        "path": REPORTS_DIR / "rsi_top_cycle_metrics.csv",
'''

    if advanced_spec_anchor in text:
        spec = '''    "Exchange Microstructure": {
        "path": REPORTS_DIR / "exchange_microstructure_metrics.csv",
        "asset_columns": ("asset",),
        "price_columns": ("price",),
    },
'''
        text = text.replace(advanced_spec_anchor, spec + advanced_spec_anchor, 1)

        if 'PRICE_TOLERANCE_PCT = 0.02\n' in text:
            text = replace_once(
                text,
                'PRICE_TOLERANCE_PCT = 0.02\n',
                'PRICE_TOLERANCE_PCT = 0.02\n' + QUALITY_MARKER + '\n',
                "quality marker",
            )
        else:
            text = text.replace('MOJIBAKE_TOKENS = ', QUALITY_MARKER + '\nMOJIBAKE_TOKENS = ', 1)

        main_anchor = '''    price_sync_available = (REPORTS_DIR / "price_coherence_sync_metrics.csv").exists()
    if not price_sync_available:
        warnings.append("price_coherence_sync.py non risulta eseguito in questo workflow.")
'''
        main_replace = main_anchor + '''
    exchange_required_files = (
        REPORTS_DIR / "exchange_market_data_snapshot.json",
        REPORTS_DIR / "exchange_market_data_intraday.csv",
        REPORTS_DIR / "exchange_storage_status.json",
        REPORTS_DIR / "exchange_microstructure_metrics.csv",
        REPORTS_DIR / "exchange_microstructure_history.csv",
        REPORTS_DIR / "exchange_signal_tracker_metrics.csv",
        REPORTS_DIR / "exchange_prediction_overlay.csv",
    )
    exchange_missing_files = [path.name for path in exchange_required_files if not path.exists()]
    exchange_data_available = not exchange_missing_files
    if exchange_missing_files:
        warnings.append("File exchange mancanti: " + ", ".join(exchange_missing_files))
    else:
        try:
            exchange_metrics = pd.read_csv(REPORTS_DIR / "exchange_microstructure_metrics.csv")
            required_exchange_columns = {
                "asset", "price", "raw_score", "candidate_global_score", "global_score", "data_coverage",
                "exchange_count", "kucoin_available", "global_activation_status",
                "funding_rate_pct", "oi_change_24h_pct", "taker_buy_sell_ratio_4h",
                "orderbook_imbalance_0_5pct",
            }
            missing_exchange_columns = sorted(required_exchange_columns - set(exchange_metrics.columns))
            if missing_exchange_columns:
                warnings.append("Campi exchange mancanti: " + ", ".join(missing_exchange_columns))
                exchange_data_available = False
            if "global_score" in exchange_metrics.columns:
                exchange_scores = pd.to_numeric(exchange_metrics["global_score"], errors="coerce").dropna()
                if (exchange_scores.abs() > 1).any():
                    critical.append("Exchange Global score supera il limite prudente ±1.")
        except Exception:
            warnings.append("exchange_microstructure_metrics.csv non leggibile.")
            exchange_data_available = False
'''
        if main_anchor not in text:
            raise RuntimeError("Punto patch Data Quality avanzato: price sync main non trovato.")
        text = text.replace(main_anchor, main_replace, 1)

        payload_anchor = '''        "price_sync_available": price_sync_available,
        "snapshot_metadata": snapshot,
'''
        payload_replace = '''        "price_sync_available": price_sync_available,
        "exchange_data_available": exchange_data_available,
        "exchange_missing_files": exchange_missing_files,
        "snapshot_metadata": snapshot,
'''
        text = replace_once(text, payload_anchor, payload_replace, "quality payload exchange")

        render_anchor = '''    lines.append(f"- Price coherence sync: **{'OK' if payload['price_sync_available'] else 'MANCANTE'}**")
    lines.append("")
'''
        render_replace = '''    lines.append(f"- Price coherence sync: **{'OK' if payload['price_sync_available'] else 'MANCANTE'}**")
    lines.append(f"- Dati exchange / microstruttura: **{'OK' if payload.get('exchange_data_available') else 'MANCANTE'}**")
    lines.append("")
'''
        text = replace_once(text, render_anchor, render_replace, "quality render exchange")

    else:
        # Legacy checker: add the same file/schema validation without relying on
        # MODULE_SPECS or price_coherence_sync fields that did not exist yet.
        marker_anchor = 'MOJIBAKE_TOKENS = ["Ã", "Â", "â€", "â†", "ðŸ", "�"]\n'
        if marker_anchor not in text:
            raise RuntimeError("Punto patch Data Quality legacy: costanti non trovate.")
        text = text.replace(marker_anchor, marker_anchor + QUALITY_MARKER + '\n', 1)

        main_anchor = '''    warnings.extend(detect_risk_naming_ambiguity(text))

    price_checks = scanner_vs_snapshot_checks(summary, snapshot)
'''
        main_replace = '''    warnings.extend(detect_risk_naming_ambiguity(text))

    exchange_required_files = (
        REPORTS_DIR / "exchange_market_data_snapshot.json",
        REPORTS_DIR / "exchange_market_data_intraday.csv",
        REPORTS_DIR / "exchange_storage_status.json",
        REPORTS_DIR / "exchange_microstructure_metrics.csv",
        REPORTS_DIR / "exchange_microstructure_history.csv",
        REPORTS_DIR / "exchange_signal_tracker_metrics.csv",
        REPORTS_DIR / "exchange_prediction_overlay.csv",
    )
    exchange_missing_files = [path.name for path in exchange_required_files if not path.exists()]
    exchange_data_available = not exchange_missing_files
    if exchange_missing_files:
        warnings.append("File exchange mancanti: " + ", ".join(exchange_missing_files))
    else:
        try:
            exchange_metrics = pd.read_csv(REPORTS_DIR / "exchange_microstructure_metrics.csv")
            required_exchange_columns = {
                "asset", "price", "raw_score", "candidate_global_score", "global_score", "data_coverage",
                "exchange_count", "kucoin_available", "global_activation_status",
                "funding_rate_pct", "oi_change_24h_pct", "taker_buy_sell_ratio_4h",
                "orderbook_imbalance_0_5pct",
            }
            missing_exchange_columns = sorted(required_exchange_columns - set(exchange_metrics.columns))
            if missing_exchange_columns:
                warnings.append("Campi exchange mancanti: " + ", ".join(missing_exchange_columns))
                exchange_data_available = False
            if "global_score" in exchange_metrics.columns:
                exchange_scores = pd.to_numeric(exchange_metrics["global_score"], errors="coerce").dropna()
                if (exchange_scores.abs() > 1).any():
                    critical.append("Exchange Global score supera il limite prudente ±1.")
        except Exception:
            warnings.append("exchange_microstructure_metrics.csv non leggibile.")
            exchange_data_available = False

    price_checks = scanner_vs_snapshot_checks(summary, snapshot)
'''
        if main_anchor not in text:
            raise RuntimeError("Punto patch Data Quality legacy: main non trovato.")
        text = text.replace(main_anchor, main_replace, 1)

        payload_anchor = '''        "scanner_summary_available": not summary.empty,
        "price_checks": price_checks,
'''
        payload_replace = '''        "scanner_summary_available": not summary.empty,
        "exchange_data_available": exchange_data_available,
        "exchange_missing_files": exchange_missing_files,
        "price_checks": price_checks,
'''
        text = replace_once(text, payload_anchor, payload_replace, "legacy quality payload exchange")

        render_anchor = '''    lines.append(f"- Scanner summary: **{'OK' if payload['scanner_summary_available'] else 'MANCANTE'}**")
    lines.append("")
'''
        render_replace = '''    lines.append(f"- Scanner summary: **{'OK' if payload['scanner_summary_available'] else 'MANCANTE'}**")
    lines.append(f"- Dati exchange / microstruttura: **{'OK' if payload.get('exchange_data_available') else 'MANCANTE'}**")
    lines.append("")
'''
        text = replace_once(text, render_anchor, render_replace, "legacy quality render exchange")

    return write_if_changed(QUALITY_PATH, original, text, ".bak_exchange_microstructure")


def split_step_blocks(text: str):
    lines = text.splitlines(keepends=True)
    starts = []
    step_indent = None
    for index, line in enumerate(lines):
        match = re.match(r"^(\s*)-\s+name:\s*", line)
        if match:
            indent = len(match.group(1))
            if step_indent is None:
                step_indent = indent
            if indent == step_indent:
                starts.append(index)
    if not starts:
        raise RuntimeError("Nessun blocco '- name:' trovato nel workflow daily.yml.")
    preamble = "".join(lines[: starts[0]])
    blocks = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        blocks.append("".join(lines[start:end]))
    return preamble, blocks, step_indent or 6


def new_step(indent: int, name: str, command: str) -> str:
    pad = " " * indent
    child = " " * (indent + 2)
    return f"{pad}- name: {name}\n{child}run: {command}\n\n"


def block_runs(block: str, script_or_fragment: str) -> bool:
    return script_or_fragment in block


def patch_workflow() -> bool:
    original = read(WORKFLOW_PATH)
    preamble, blocks, indent = split_step_blocks(original)

    managed_fragments = (
        "requirements-exchange.txt",
        "exchange_market_data.py",
        "exchange_persistent_storage.py",
        "exchange_signal_tracker.py",
        "exchange_microstructure_report.py",
    )
    clean = [block for block in blocks if not any(fragment in block for fragment in managed_fragments)]

    global_index = next(
        (i for i, block in enumerate(clean) if "python global_confluence_report.py" in block),
        None,
    )
    if global_index is None:
        raise RuntimeError("Step global_confluence_report.py non trovato nel daily workflow.")

    technical_index = next(
        (i for i, block in enumerate(clean) if "python technical_structure_report.py" in block),
        None,
    )
    if technical_index is not None and technical_index > global_index:
        raise RuntimeError("technical_structure_report.py deve precedere Global Confluence.")

    additions = [
        new_step(indent, "Install exchange microstructure dependencies", "python -m pip install -r requirements-exchange.txt"),
        new_step(
            indent,
            "Restore persistent exchange state",
            'GITHUB_TOKEN="${{ github.token }}" EXCHANGE_STORAGE_RELEASE_TAG="exchange-data-v2-1" python exchange_persistent_storage.py restore',
        ),
        new_step(
            indent,
            "Audit persistent exchange state",
            'GITHUB_TOKEN="${{ github.token }}" EXCHANGE_STORAGE_RELEASE_TAG="exchange-data-v2-1" python exchange_persistent_storage.py audit',
        ),
        new_step(
            indent,
            "Archive completed exchange months",
            'GITHUB_TOKEN="${{ github.token }}" EXCHANGE_STORAGE_RELEASE_TAG="exchange-data-v2-1" python exchange_persistent_storage.py archive-completed-months',
        ),
        new_step(indent, "Update exchange signal tracker", "python exchange_signal_tracker.py"),
        new_step(indent, "Build exchange microstructure report", "python exchange_microstructure_report.py"),
    ]
    clean[global_index:global_index] = additions

    updated = preamble + "".join(clean)
    if not updated.endswith("\n"):
        updated += "\n"

    order = [
        "python exchange_persistent_storage.py restore",
        "python exchange_persistent_storage.py audit",
        "python exchange_persistent_storage.py archive-completed-months",
        "python exchange_signal_tracker.py",
        "python exchange_microstructure_report.py",
        "python global_confluence_report.py",
    ]
    positions = [updated.find(item) for item in order]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        raise RuntimeError(f"Ordine workflow exchange non valido: {dict(zip(order, positions))}")

    return write_if_changed(WORKFLOW_PATH, original, updated, ".bak_exchange_microstructure")



def patch_gitignore() -> bool:
    entries = [
        "/reports/exchange_market_data_intraday.csv",
        "/reports/exchange_market_data_snapshot.json",
        "/reports/exchange_market_data_health.json",
        "/reports/exchange_market_data_raw.json",
        "/reports/exchange_storage_status.json",
        "/.exchange_storage/",
    ]
    original = GITIGNORE_PATH.read_text(encoding="utf-8") if GITIGNORE_PATH.exists() else ""
    lines = original.splitlines()
    existing = {line.strip() for line in lines}
    missing = [entry for entry in entries if entry not in existing]
    if not missing:
        print(".gitignore: storage exchange già escluso dalla cronologia Git.")
        return False
    updated = original
    if updated and not updated.endswith("\n"):
        updated += "\n"
    updated += "\n# Exchange Microstructure v2.1 - raw state stored in GitHub Releases\n"
    updated += "\n".join(missing) + "\n"
    GITIGNORE_PATH.write_text(updated, encoding="utf-8", newline="\n")
    print(".gitignore: aggiunte esclusioni storage exchange.")
    return True

def compile_all() -> None:
    missing = [str(path) for path in NEW_FILES if not path.exists()]
    if missing:
        raise RuntimeError("Nuovi file mancanti: " + ", ".join(missing))
    for path in (*[item for item in NEW_FILES if item.suffix == ".py"], *PATCHED_FILES):
        py_compile.compile(str(path), doraise=True)


def validate() -> None:
    global_text = read(GLOBAL_PATH)
    tracker_text = read(MODULE_TRACKER_PATH)
    compact_text = read(COMPACT_PATH)
    quality_text = read(QUALITY_PATH)
    workflow_text = read(WORKFLOW_PATH)

    checks = {
        "Global parser": "parse_exchange_microstructure_component" in global_text,
        "Global score field": "exchange_flow_score_component" in global_text,
        "Global candidate field": "exchange_candidate_score_component" in global_text,
        "Tracker module": '"key": "exchange_microstructure"' in tracker_text,
        "Tracker candidate column": '"score_col": "exchange_candidate_score_component"' in tracker_text,
        "Compact current section": "EXCHANGE_MICROSTRUCTURE_START" in compact_text,
        "Compact accuracy section": "EXCHANGE_SIGNAL_TRACKER_START" in compact_text,
        "Data Quality exchange": "exchange_data_available" in quality_text,
        "Workflow restore": "python exchange_persistent_storage.py restore" in workflow_text,
        "Workflow audit": "python exchange_persistent_storage.py audit" in workflow_text,
        "Workflow archive": "python exchange_persistent_storage.py archive-completed-months" in workflow_text,
        "Workflow tracker": "python exchange_signal_tracker.py" in workflow_text,
        "Workflow report": "python exchange_microstructure_report.py" in workflow_text,
        "Gitignore intraday": "/reports/exchange_market_data_intraday.csv" in (GITIGNORE_PATH.read_text(encoding="utf-8") if GITIGNORE_PATH.exists() else ""),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validazione exchange fallita: " + ", ".join(failed))

    exchange_pos = workflow_text.find("python exchange_microstructure_report.py")
    global_pos = workflow_text.find("python global_confluence_report.py")
    if not (0 <= exchange_pos < global_pos):
        raise RuntimeError("Exchange report deve precedere Global Confluence.")
    print("Validazione upgrade exchange v2.1: OK")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-workflow", action="store_true", help="Patch source files only")
    args = parser.parse_args()

    compile_all()
    changed = []
    changed.append(patch_global())
    changed.append(patch_module_tracker())
    changed.append(patch_compact())
    changed.append(patch_quality())
    changed.append(patch_gitignore())
    if not args.skip_workflow:
        changed.append(patch_workflow())
    compile_all()
    validate()
    print("Upgrade exchange v2.1 completato." if any(changed) else "Upgrade exchange v2.1 già installato.")


if __name__ == "__main__":
    main()
