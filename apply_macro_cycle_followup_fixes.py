# -*- coding: utf-8 -*-
"""Apply and verify the four Macro Cycle / Relative Strength follow-up fixes.

Fixes
-----
1. Power Law classifies prices below p10 and above p90 outside the corridor.
2. Power Law freezes at most one live forecast per UTC calendar month.
3. ALT/BTC double patterns keep their lifecycle and become TARGET RAGGIUNTO
   after the objective is touched following confirmation.
4. Exchange history is versioned; transition rows through 2026-07-11 remain
   visible but are excluded from calibration.

The patch supports both the original exchange tracker and the later V2.1.3
variant that uses ``candidate_global_score``. It is idempotent and does not
change any Global Confluence weight or activation threshold.
"""

from __future__ import annotations

import argparse
import csv
import py_compile
from datetime import date
from pathlib import Path
from typing import Callable


PATCH_VERSION = "2.0"
ROOT = Path(".")
BTC_MACRO = ROOT / "btc_macro_cycle_report.py"
RELATIVE = ROOT / "relative_strength_btc_report.py"
EXCHANGE_REPORT = ROOT / "exchange_microstructure_report.py"
EXCHANGE_TRACKER = ROOT / "exchange_signal_tracker.py"
EXCHANGE_HISTORY = ROOT / "reports" / "exchange_microstructure_history.csv"
STATUS_PATH = ROOT / "reports" / "macro_cycle_followup_fix_status.md"
TRANSITION_CUTOFF = date(2026, 7, 11)
MODULE_VERSION = "V2.1.3"


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"File mancante: {path}")
    return path.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Punto patch non univoco ({count} occorrenze): {label}")
    return text.replace(old, new, 1)


def replace_one_of(text: str, old_versions: tuple[str, ...], new: str, label: str) -> str:
    if new in text:
        return text
    matches = [old for old in old_versions if old in text]
    if len(matches) != 1:
        raise RuntimeError(f"Punto patch non trovato o ambiguo ({len(matches)} varianti): {label}")
    return text.replace(matches[0], new, 1)


def patch_btc_macro_text(text: str) -> str:
    original_zone = '''    if percentile <= 20:\n        zone = "BASSA NEL CORRIDOIO"\n    elif percentile >= 80:\n        zone = "ALTA NEL CORRIDOIO"\n    else:\n        zone = "CENTRALE NEL CORRIDOIO"\n'''
    previous_zone = '''    # Classify the price against the actual p10-p90 corridor first.\n    # A low residual percentile does not necessarily mean the price is still\n    # inside the corridor: it can be below the lower band.\n    if current_price < q10_price:\n        zone = "SOTTO LA BANDA P10 / FUORI CORRIDOIO INFERIORE"\n    elif current_price > q90_price:\n        zone = "SOPRA LA BANDA P90 / FUORI CORRIDOIO SUPERIORE"\n    elif percentile <= 20:\n        zone = "BASSA NEL CORRIDOIO"\n    elif percentile >= 80:\n        zone = "ALTA NEL CORRIDOIO"\n    else:\n        zone = "CENTRALE NEL CORRIDOIO"\n'''
    final_zone = '''    # The corridor is defined by the actual p10 and p90 price bands.\n    # Residual percentile is used only after confirming that price is inside.\n    if current_price < q10_price:\n        zone = "SOTTO LA BANDA P10"\n    elif current_price > q90_price:\n        zone = "SOPRA LA BANDA P90"\n    elif percentile <= 20:\n        zone = "BASSA NEL CORRIDOIO"\n    elif percentile >= 80:\n        zone = "ALTA NEL CORRIDOIO"\n    else:\n        zone = "CENTRALE NEL CORRIDOIO"\n'''
    text = replace_one_of(text, (original_zone, previous_zone), final_zone, "Power Law p10/p90")

    original_month = '''    rows = read_csv(HISTORY_PATH)\n    today = position["current_date"].date().isoformat()\n    if not any(row.get("signal_date") == today for row in rows):\n        rows.append(\n'''
    previous_month = '''    rows = read_csv(HISTORY_PATH)\n    today = position["current_date"].date().isoformat()\n    month_key = position["current_date"].strftime("%Y-%m")\n\n    # Power Law is a macro model. One live forecast per calendar month avoids\n    # treating nearly identical daily forecasts as independent observations.\n    def row_month(row: dict[str, str]) -> str:\n        try:\n            return pd.Timestamp(row.get("signal_date", "")).strftime("%Y-%m")\n        except Exception:\n            return ""\n\n    if not any(row_month(row) == month_key for row in rows):\n        rows.append(\n'''
    final_month = '''    rows = read_csv(HISTORY_PATH)\n    today = position["current_date"].date().isoformat()\n    month_key = today[:7]\n\n    # Power Law is a macro model. Freeze the first valid live forecast of each\n    # UTC calendar month so daily reruns are not counted as independent calls.\n    def row_month(row: dict[str, str]) -> str:\n        value = str(row.get("signal_date", "")).strip()\n        try:\n            return datetime.fromisoformat(value[:10]).strftime("%Y-%m")\n        except (TypeError, ValueError):\n            return ""\n\n    if not any(row_month(row) == month_key for row in rows):\n        rows.append(\n'''
    text = replace_one_of(
        text,
        (original_month, previous_month),
        final_month,
        "Power Law monthly live snapshot",
    )

    note = (
        "Il modulo resta a peso 0 anche con un buon backtest. Prima si osserva la verifica live, "
        "poi si decide se usarlo soltanto per il rischio macro di lungo periodo."
    )
    monthly_note = (
        note
        + " Le fotografie live della Power Law vengono salvate una sola volta per mese, così non si "
        "contano come indipendenti previsioni giornaliere quasi identiche."
    )
    if monthly_note not in text:
        text = replace_once(text, note, monthly_note, "Nota mensile Power Law")
    return text


def patch_relative_text(text: str) -> str:
    original_lifecycle = '''            if bullish:\n                confirmed = close > neckline * 1.005\n                target = neckline + (neckline - average)\n            else:\n                confirmed = close < neckline * 0.995\n                target = neckline - (average - neckline)\n            candidates.append(\n                {\n                    "family": family,\n                    "state": "CONFERMATO" if confirmed else "CANDIDATO",\n'''
    previous_lifecycle = '''            if bullish:\n                confirmed = close > neckline * 1.005\n                target = neckline + (neckline - average)\n                target_reached = confirmed and close >= target\n            else:\n                confirmed = close < neckline * 0.995\n                target = neckline - (average - neckline)\n                target_reached = confirmed and close <= target\n\n            if target_reached:\n                state = "TARGET RAGGIUNTO"\n            elif confirmed:\n                state = "CONFERMATO"\n            else:\n                state = "CANDIDATO"\n\n            candidates.append(\n                {\n                    "family": family,\n                    "state": state,\n'''
    final_lifecycle = '''            post_pattern = frame.loc[second["date"]:].copy()\n            if bullish:\n                target = neckline + (neckline - average)\n                confirmation_mask = post_pattern["Close"] > neckline * 1.005\n                confirmed = bool(confirmation_mask.any())\n                if confirmed:\n                    confirmation_date = confirmation_mask[confirmation_mask].index[0]\n                    target_column = "High" if "High" in post_pattern.columns else "Close"\n                    target_path = post_pattern.loc[confirmation_date:, target_column]\n                    target_reached = bool((target_path >= target).any())\n                else:\n                    target_reached = False\n            else:\n                target = neckline - (average - neckline)\n                confirmation_mask = post_pattern["Close"] < neckline * 0.995\n                confirmed = bool(confirmation_mask.any())\n                if confirmed:\n                    confirmation_date = confirmation_mask[confirmation_mask].index[0]\n                    target_column = "Low" if "Low" in post_pattern.columns else "Close"\n                    target_path = post_pattern.loc[confirmation_date:, target_column]\n                    target_reached = bool((target_path <= target).any())\n                else:\n                    target_reached = False\n\n            if target_reached:\n                state = "TARGET RAGGIUNTO"\n            elif confirmed:\n                state = "CONFERMATO"\n            else:\n                state = "CANDIDATO"\n\n            candidates.append(\n                {\n                    "family": family,\n                    "state": state,\n'''
    text = replace_one_of(
        text,
        (original_lifecycle, previous_lifecycle),
        final_lifecycle,
        "ALT/BTC pattern lifecycle",
    )

    original_sort = '''    candidates.sort(\n        key=lambda item: (\n            item["state"] == "CONFERMATO",\n            -item["age_days"],\n            -item["similarity_pct"],\n        ),\n        reverse=True,\n    )\n'''
    previous_sort = '''    state_priority = {"CONFERMATO": 2, "TARGET RAGGIUNTO": 1, "CANDIDATO": 0}\n    candidates.sort(\n        key=lambda item: (\n            state_priority.get(item["state"], 0),\n            -item["age_days"],\n            -item["similarity_pct"],\n        ),\n        reverse=True,\n    )\n'''
    final_sort = '''    state_priority = {"TARGET RAGGIUNTO": 3, "CONFERMATO": 2, "CANDIDATO": 1}\n    candidates.sort(\n        key=lambda item: (\n            state_priority.get(item["state"], 0),\n            -item["age_days"],\n            -item["similarity_pct"],\n        ),\n        reverse=True,\n    )\n'''
    return replace_one_of(text, (original_sort, previous_sort), final_sort, "ALT/BTC lifecycle priority")


def patch_exchange_report_text(text: str) -> str:
    constants = '''ASSETS = ("BTC", "SOL", "DOGE")\nLIQ_MIN_USD = {"BTC": 250_000.0, "SOL": 50_000.0, "DOGE": 20_000.0}\nHISTORY_KEY = ("signal_date", "asset")\n'''
    constants_with_version = constants + f'MODULE_VERSION = "{MODULE_VERSION}"\n'
    text = replace_once(text, constants, constants_with_version, "Exchange module version")

    fields = '''    "adjusted_return_p50_30d",\n    "created_utc",\n]\n'''
    versioned_fields = '''    "adjusted_return_p50_30d",\n    "module_version",\n    "calibration_eligible",\n    "calibration_note",\n    "created_utc",\n]\n'''
    text = replace_once(text, fields, versioned_fields, "Exchange history schema")

    row_tail = '''            "adjusted_positive_rate_30d": overlay.get("adjusted_positive_rate_30d"),\n            "adjusted_return_p50_30d": overlay.get("adjusted_return_p50_30d"),\n            "created_utc": now,\n'''
    versioned_row_tail = '''            "adjusted_positive_rate_30d": overlay.get("adjusted_positive_rate_30d"),\n            "adjusted_return_p50_30d": overlay.get("adjusted_return_p50_30d"),\n            "module_version": MODULE_VERSION,\n            "calibration_eligible": True,\n            "calibration_note": "",\n            "created_utc": now,\n'''
    return replace_once(text, row_tail, versioned_row_tail, "Exchange history row version")


def patch_exchange_tracker_text(text: str) -> str:
    fields = '''    "adjusted_return_p50_30d",\n    "created_utc",\n]\n'''
    versioned_fields = '''    "adjusted_return_p50_30d",\n    "module_version",\n    "calibration_eligible",\n    "calibration_note",\n    "created_utc",\n]\n'''
    text = replace_once(text, fields, versioned_fields, "Tracker history schema")

    parse_bool = '''def parse_bool(value: Any) -> bool:\n    if isinstance(value, bool):\n        return value\n    return safe_str(value).lower() in {"true", "1", "yes", "y", "si", "sì"}\n\n\n'''
    eligibility_helper = parse_bool + '''def is_calibration_eligible(value: Any) -> bool:\n    """Blank legacy rows stay eligible unless migration explicitly excludes them."""\n    text = safe_str(value)\n    return True if text == "" else parse_bool(text)\n\n\n'''
    text = replace_once(text, parse_bool, eligibility_helper, "Tracker eligibility helper")

    # An earlier draft skipped outcome maturation for excluded rows. Outcomes
    # are useful for audit; only build_metrics must exclude those rows.
    old_outcome_skip = '''        if not is_calibration_eligible(row.get("calibration_eligible")):\n            # Keep the row for audit, but do not mature outcomes that must never\n            # enter calibration (for example the 2026-07-11 transition day).\n            continue\n'''
    if old_outcome_skip in text:
        text = text.replace(old_outcome_skip, "", 1)

    original_metrics = '''def build_metrics(history: pd.DataFrame) -> pd.DataFrame:\n    rows: list[dict[str, Any]] = []\n    for asset in ASSETS:\n        asset_df = history[history["asset"].astype(str).str.upper() == asset].copy()\n        for h in HORIZONS:\n            checked = asset_df[asset_df[f"checked_{h}d"].map(parse_bool)].copy()\n'''
    filtered_metrics = '''def build_metrics(history: pd.DataFrame) -> pd.DataFrame:\n    history = ensure_columns(history)\n    rows: list[dict[str, Any]] = []\n    for asset in ASSETS:\n        asset_df = history.loc[history["asset"].astype(str).str.upper() == asset].copy()\n        eligibility_mask = asset_df["calibration_eligible"].map(is_calibration_eligible)\n        asset_df = asset_df.loc[eligibility_mask].copy()\n        for h in HORIZONS:\n            checked_mask = asset_df[f"checked_{h}d"].map(parse_bool)\n            checked = asset_df.loc[checked_mask].copy()\n'''
    text = replace_once(text, original_metrics, filtered_metrics, "Tracker calibration exclusion")

    price_cell = '                    safe_str(row.get("price")),\n'
    audit_cells = price_cell + '''                    safe_str(row.get("module_version"), "LEGACY"),\n                    "OK" if is_calibration_eligible(row.get("calibration_eligible")) else "ESCLUSA",\n'''
    text = replace_once(text, price_cell, audit_cells, "Tracker audit cells")

    header_start = '["Data", "Asset", "Prezzo", '
    versioned_header_start = '["Data", "Asset", "Prezzo", "Versione", "Calibrazione", '
    return replace_once(text, header_start, versioned_header_start, "Tracker audit header")


SOURCE_PATCHERS: tuple[tuple[Path, Callable[[str], str]], ...] = (
    (BTC_MACRO, patch_btc_macro_text),
    (RELATIVE, patch_relative_text),
    (EXCHANGE_REPORT, patch_exchange_report_text),
    (EXCHANGE_TRACKER, patch_exchange_tracker_text),
)


def compile_text(path: Path, text: str) -> None:
    try:
        compile(text, str(path), "exec")
    except SyntaxError as exc:
        raise RuntimeError(f"Sintassi non valida dopo la patch in {path}: {exc}") from exc


def validate_source_texts(texts: dict[Path, str]) -> None:
    btc = texts[BTC_MACRO]
    relative = texts[RELATIVE]
    exchange = texts[EXCHANGE_REPORT]
    tracker = texts[EXCHANGE_TRACKER]
    checks = {
        "Power Law sotto p10": 'zone = "SOTTO LA BANDA P10"' in btc,
        "Power Law sopra p90": 'zone = "SOPRA LA BANDA P90"' in btc,
        "Power Law guardia mensile": "if not any(row_month(row) == month_key for row in rows):" in btc,
        "Power Law chiave calendario": "month_key = today[:7]" in btc,
        "Pattern target dopo conferma": "target_path = post_pattern.loc[confirmation_date:, target_column]" in relative,
        "Pattern target raggiunto": 'state = "TARGET RAGGIUNTO"' in relative,
        "Pattern priorità lifecycle": 'state_priority = {"TARGET RAGGIUNTO": 3' in relative,
        "Exchange versione": f'MODULE_VERSION = "{MODULE_VERSION}"' in exchange,
        "Exchange eleggibilità nuova riga": '"calibration_eligible": True' in exchange,
        "Tracker helper eleggibilità": "def is_calibration_eligible" in tracker,
        "Tracker filtro calibrazione": 'asset_df["calibration_eligible"].map(is_calibration_eligible)' in tracker,
        "Tracker audit esclusione": 'else "ESCLUSA"' in tracker,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validazione sorgenti fallita: " + ", ".join(failed))
    for path, text in texts.items():
        compile_text(path, text)


def write_if_changed(path: Path, old: str, new: str) -> bool:
    if old == new:
        print(f"{path}: già corretto.")
        return False
    backup = path.with_name(path.name + ".bak_followup_fix_v2")
    if not backup.exists():
        backup.write_text(old, encoding="utf-8", newline="\n")
    path.write_text(new, encoding="utf-8", newline="\n")
    print(f"{path}: corretto.")
    return True


def parse_iso_date(value: str) -> date | None:
    try:
        return date.fromisoformat((value or "").strip()[:10])
    except (TypeError, ValueError):
        return None


def csv_bool(value: str) -> bool:
    return str(value or "").strip().lower() in {"true", "1", "yes", "y", "si", "sì"}


def migrate_exchange_history() -> tuple[int, int, bool]:
    if not EXCHANGE_HISTORY.exists():
        return 0, 0, False

    with EXCHANGE_HISTORY.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fields = list(reader.fieldnames or [])

    for field in ("module_version", "calibration_eligible", "calibration_note"):
        if field not in fields:
            fields.append(field)

    changed = False
    for row in rows:
        before = tuple(row.get(field, "") for field in fields)
        signal_date = parse_iso_date(row.get("signal_date", ""))
        if signal_date is None:
            row["module_version"] = row.get("module_version", "").strip() or "UNVERSIONED_LEGACY"
            row["calibration_eligible"] = "False"
            row["calibration_note"] = row.get("calibration_note", "").strip() or (
                "Esclusa: signal_date mancante o non valida; impossibile assegnare una versione affidabile."
            )
        elif signal_date <= TRANSITION_CUTOFF:
            row["module_version"] = "TRANSITION_PRE_V2.1.3"
            row["calibration_eligible"] = "False"
            row["calibration_note"] = (
                "Esclusa: fotografia raccolta prima/durante il completamento della configurazione "
                "primaria Kraken + Bitget + KuCoin V2.1.3."
            )
        else:
            row["module_version"] = row.get("module_version", "").strip() or MODULE_VERSION
            # Preserve any later explicit manual exclusion; initialize only blanks.
            if not str(row.get("calibration_eligible", "")).strip():
                row["calibration_eligible"] = "True"
        after = tuple(row.get(field, "") for field in fields)
        changed = changed or before != after

    if changed:
        tmp = EXCHANGE_HISTORY.with_suffix(EXCHANGE_HISTORY.suffix + ".tmp")
        with tmp.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        tmp.replace(EXCHANGE_HISTORY)

    excluded = sum(not csv_bool(row.get("calibration_eligible", "")) for row in rows)
    eligible = len(rows) - excluded
    return excluded, eligible, changed


def validate_exchange_history() -> None:
    if not EXCHANGE_HISTORY.exists():
        return
    with EXCHANGE_HISTORY.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        signal_date = parse_iso_date(row.get("signal_date", ""))
        if signal_date is None or signal_date <= TRANSITION_CUTOFF:
            if csv_bool(row.get("calibration_eligible", "")):
                raise RuntimeError("Storico exchange: riga transitoria ancora eleggibile alla calibrazione.")
        if signal_date is not None and signal_date > TRANSITION_CUTOFF:
            if not str(row.get("module_version", "")).strip():
                raise RuntimeError("Storico exchange: riga successiva al cutoff senza versione.")


def write_status(changed_files: list[str], excluded: int, eligible: int, history_changed: bool) -> None:
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(
        "\n".join(
            [
                "# Stato correzioni Macro Cycle / Relative Strength",
                "",
                f"- Patch: **v{PATCH_VERSION}**",
                "- Power Law sotto p10: **SOTTO LA BANDA P10 — OK**",
                "- Power Law una previsione live per mese UTC: **OK**",
                "- Pattern ALT/BTC TARGET RAGGIUNTO persistente dopo conferma: **OK**",
                "- Versionamento storico exchange V2.1.3: **OK**",
                f"- File sorgente modificati: **{', '.join(changed_files) if changed_files else 'nessuno, patch già presente'}**",
                f"- Righe exchange escluse: **{excluded}**",
                f"- Righe exchange eleggibili: **{eligible}**",
                f"- Storico exchange modificato: **{'SI' if history_changed else 'NO'}**",
                "- Pesi e soglie Global modificati: **NO**",
                "",
            ]
        ),
        encoding="utf-8",
        newline="\n",
    )


def current_source_texts() -> dict[Path, str]:
    return {path: read(path) for path, _ in SOURCE_PATCHERS}


def apply_fixes() -> int:
    originals = current_source_texts()
    patched: dict[Path, str] = {}
    for path, patcher in SOURCE_PATCHERS:
        patched[path] = patcher(originals[path])

    # Validate every transformed source before writing any of them.
    validate_source_texts(patched)

    changed_files: list[str] = []
    for path, _ in SOURCE_PATCHERS:
        if write_if_changed(path, originals[path], patched[path]):
            changed_files.append(path.name)

    excluded, eligible, history_changed = migrate_exchange_history()
    validate_exchange_history()
    for path, _ in SOURCE_PATCHERS:
        py_compile.compile(str(path), doraise=True)
    write_status(changed_files, excluded, eligible, history_changed)
    print("Correzioni Macro Cycle / Relative Strength completate e verificate.")
    return 0


def verify_only() -> int:
    texts = current_source_texts()
    validate_source_texts(texts)
    validate_exchange_history()
    for path, _ in SOURCE_PATCHERS:
        py_compile.compile(str(path), doraise=True)
    print("Verifica follow-up: OK.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-only", action="store_true", help="Verifica senza modificare file o storico.")
    args = parser.parse_args()
    return verify_only() if args.verify_only else apply_fixes()


if __name__ == "__main__":
    raise SystemExit(main())
