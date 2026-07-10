import csv
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"
REPORT_PATH = REPORTS_DIR / "global_weight_calibration_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "global_weight_calibration_metrics.csv"

MODULE_METRICS_CSV_PATH = REPORTS_DIR / "module_signal_tracker_metrics.csv"
MODULE_HISTORY_CSV_PATH = REPORTS_DIR / "module_signal_tracker_history.csv"

START_MARKER = "<!-- GLOBAL_WEIGHT_CALIBRATION_START -->"
END_MARKER = "<!-- GLOBAL_WEIGHT_CALIBRATION_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]
HORIZON_FAMILY_ORDER = ["BREVE", "SETTIMANALE", "SWING", "MEDIO"]

# Ruoli di fallback per compatibilità con vecchi CSV.
ROLE_FALLBACKS = {
    "global": {
        "calibration_role": "BENCHMARK",
        "calibratable": False,
        "parent_family": "",
    },
    "statistical_family": {
        "calibration_role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
    "scanner": {
        "calibration_role": "DIAGNOSTICO",
        "calibratable": False,
        "parent_family": "statistical_family",
    },
    "market": {
        "calibration_role": "DIAGNOSTICO",
        "calibratable": False,
        "parent_family": "statistical_family",
    },
    "technical": {
        "calibration_role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
    "classic_technical": {
        "calibration_role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
    "sol_fractal": {
        "calibration_role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
}


OUTPUT_COLUMNS = [
    "generated_utc",
    "asset",
    "horizon_days",
    "horizon",
    "horizon_family",
    "module_key",
    "module",
    "calibration_role",
    "calibratable",
    "parent_family",
    "controls",
    "correct",
    "accuracy_direction_pct",
    "avg_return_pct",
    "avg_direction_adjusted_return_pct",
    "avg_drawdown_pct",
    "avg_max_gain_pct",
    "metric_status",
    "recommendation",
    "suggested_weight_delta",
    "confidence",
    "recommendation_reason",
]


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def replace_or_insert_block(text: str, block: str) -> str:
    full_block = f"{START_MARKER}\n{block.rstrip()}\n{END_MARKER}"

    if START_MARKER in text and END_MARKER in text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(full_block, text)

    module_accuracy_end = "<!-- MODULE_ACCURACY_END -->"
    if module_accuracy_end in text:
        return text.replace(
            module_accuracy_end,
            module_accuracy_end + "\n\n" + full_block,
            1,
        )

    decision_end = "<!-- DECISION_REPORT_END -->"
    if decision_end in text:
        return text.replace(
            decision_end,
            decision_end + "\n\n" + full_block,
            1,
        )

    return text.rstrip() + "\n\n" + full_block + "\n"


def safe_str(value, default="") -> str:
    if value is None:
        return default
    try:
        if pd.isna(value):
            return default
    except Exception:
        pass
    return str(value).strip()


def safe_float(value, default=np.nan):
    if value is None:
        return default

    try:
        if pd.isna(value):
            return default
    except Exception:
        pass

    if isinstance(value, str):
        s = value.strip()
        if not s or s.lower() in {"n/a", "nan", "none", "null", "-"}:
            return default
        s = s.replace("%", "").replace("$", "").replace(" ", "")
        if "," in s:
            s = s.replace(".", "").replace(",", ".")
        try:
            return float(s)
        except Exception:
            return default

    try:
        return float(value)
    except Exception:
        return default


def safe_int(value, default=0) -> int:
    v = safe_float(value, np.nan)
    if pd.isna(v):
        return default
    return int(v)


def parse_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    s = safe_str(value).lower()
    return s in {"true", "1", "yes", "y", "si", "sì"}


def fmt_pct(value, decimals: int = 2, signed: bool = True) -> str:
    v = safe_float(value, np.nan)
    if pd.isna(v):
        return "n/a"
    sign = "+" if signed else ""
    return f"{v:{sign}.{decimals}f}%".replace(".", ",")


def fmt_delta(value) -> str:
    v = safe_float(value, 0.0)
    if abs(v) < 1e-12:
        return "0,0"
    return f"{v:+.2f}".replace(".", ",")


def md_table(headers, rows) -> str:
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        output.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(output)


def infer_horizon_family(days: int) -> str:
    if days <= 3:
        return "BREVE"
    if days <= 10:
        return "SETTIMANALE"
    if days <= 21:
        return "SWING"
    return "MEDIO"


def normalize_module_key(value: str) -> str:
    s = safe_str(value).strip().lower()
    aliases = {
        "famiglia statistica": "statistical_family",
        "statistical family": "statistical_family",
        "global confluence": "global",
        "market regime": "market",
        "market regime grezzo": "market",
        "scanner grezzo": "scanner",
        "tecnico": "technical",
        "classic technical": "classic_technical",
        "frattale sol": "sol_fractal",
    }
    return aliases.get(s, s.replace(" ", "_"))


def load_module_metrics() -> pd.DataFrame:
    if not MODULE_METRICS_CSV_PATH.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(MODULE_METRICS_CSV_PATH, dtype=str)
    except Exception:
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    out = df.copy()

    if "module_key" not in out.columns:
        if "module" in out.columns:
            out["module_key"] = out["module"].map(normalize_module_key)
        else:
            out["module_key"] = ""
    else:
        out["module_key"] = out["module_key"].map(normalize_module_key)

    if "module" not in out.columns:
        out["module"] = out["module_key"]

    for col in [
        "controls",
        "correct",
        "horizon_days",
        "accuracy_direction_pct",
        "avg_return_pct",
        "avg_direction_adjusted_return_pct",
        "avg_drawdown_pct",
        "avg_max_gain_pct",
    ]:
        if col not in out.columns:
            out[col] = np.nan
        out[col] = pd.to_numeric(out[col], errors="coerce")

    if "asset" not in out.columns:
        out["asset"] = ""
    out["asset"] = out["asset"].astype(str).str.upper().str.strip()

    if "horizon" not in out.columns:
        out["horizon"] = out["horizon_days"].apply(
            lambda value: f"{int(value)}g" if pd.notna(value) else "n/a"
        )

    if "horizon_family" not in out.columns:
        out["horizon_family"] = out["horizon_days"].apply(
            lambda value: infer_horizon_family(int(value)) if pd.notna(value) else "n/a"
        )
    else:
        out["horizon_family"] = out["horizon_family"].astype(str).str.upper().str.strip()

    if "status" not in out.columns:
        out["status"] = ""

    # Applica metadati prodotti dal nuovo tracker; in assenza, usa fallback sicuri.
    roles = []
    calibratables = []
    parents = []

    for _, row in out.iterrows():
        key = normalize_module_key(row.get("module_key"))
        fallback = ROLE_FALLBACKS.get(
            key,
            {
                "calibration_role": "CALIBRABILE",
                "calibratable": True,
                "parent_family": "",
            },
        )

        role = safe_str(row.get("calibration_role"), fallback["calibration_role"]).upper()
        if not role:
            role = fallback["calibration_role"]

        raw_calibratable = row.get("calibratable")
        if raw_calibratable is None or safe_str(raw_calibratable) == "":
            calibratable = bool(fallback["calibratable"])
        else:
            calibratable = parse_bool(raw_calibratable)

        parent = safe_str(row.get("parent_family"), fallback["parent_family"])

        roles.append(role)
        calibratables.append(calibratable)
        parents.append(parent)

    out["calibration_role"] = roles
    out["calibratable"] = calibratables
    out["parent_family"] = parents

    return out


def load_signal_counts() -> dict:
    counts = {asset: 0 for asset in ASSETS}

    if not MODULE_HISTORY_CSV_PATH.exists():
        return counts

    try:
        history = pd.read_csv(MODULE_HISTORY_CSV_PATH, dtype=str)
    except Exception:
        return counts

    if history.empty or "asset" not in history.columns:
        return counts

    history["asset"] = history["asset"].astype(str).str.upper().str.strip()

    for asset in ASSETS:
        counts[asset] = int((history["asset"] == asset).sum())

    return counts


def confidence_from_controls(controls: int) -> str:
    if controls >= 100:
        return "ALTA"
    if controls >= 60:
        return "MEDIA / ALTA"
    if controls >= 30:
        return "MEDIA"
    return "BASSA"


def recommendation_for_row(row: pd.Series):
    role = safe_str(row.get("calibration_role")).upper()
    calibratable = parse_bool(row.get("calibratable"))
    controls = safe_int(row.get("controls"), 0)
    accuracy = safe_float(row.get("accuracy_direction_pct"), np.nan)
    adjusted_return = safe_float(
        row.get("avg_direction_adjusted_return_pct"),
        np.nan,
    )

    if not calibratable:
        if role == "BENCHMARK":
            reason = "Aggregato finale usato come benchmark; non è un peso interno da modificare."
        else:
            parent = safe_str(row.get("parent_family"))
            if parent:
                reason = (
                    "Modulo diagnostico già incluso nella famiglia "
                    f"{parent}; nessuna modifica di peso separata."
                )
            else:
                reason = "Modulo diagnostico escluso dalle modifiche di peso."
        return "ESCLUSO", 0.0, "N/A", reason

    confidence = confidence_from_controls(controls)

    if controls < 30:
        return (
            "OSSERVA",
            0.0,
            confidence,
            "Meno di 30 controlli: dato utile solo come osservazione, nessuna modifica.",
        )

    if pd.isna(accuracy) or pd.isna(adjusted_return):
        return (
            "DATI INSUFFICIENTI",
            0.0,
            confidence,
            "Controlli presenti, ma accuratezza o return corretto non sono disponibili.",
        )

    # Prima calibrazione: proposte molto leggere.
    if controls < 60:
        if accuracy >= 65 and adjusted_return >= 0.50:
            return (
                "POSSIBILE AUMENTO LEGGERO",
                0.25,
                confidence,
                "Almeno 30 controlli, accuratezza >=65% e return corretto positivo.",
            )
        if accuracy <= 42 and adjusted_return < 0:
            return (
                "POSSIBILE RIDUZIONE LEGGERA",
                -0.25,
                confidence,
                "Almeno 30 controlli, accuratezza debole e return corretto negativo.",
            )
        if accuracy < 55 or adjusted_return <= 0:
            return (
                "NON AUMENTARE",
                0.0,
                confidence,
                "Il modulo non dimostra ancora un vantaggio abbastanza stabile.",
            )
        return (
            "PESO OK",
            0.0,
            confidence,
            "Risultato discreto, ma non abbastanza forte per cambiare il peso.",
        )

    # Lettura utile: una modifica resta comunque prudente.
    if controls < 100:
        if accuracy >= 68 and adjusted_return >= 0.75:
            return (
                "POSSIBILE AUMENTO LEGGERO",
                0.50,
                confidence,
                "Almeno 60 controlli con accuratezza e return corretto solidi.",
            )
        if accuracy <= 43 and adjusted_return < 0:
            return (
                "POSSIBILE RIDUZIONE PESO",
                -0.50,
                confidence,
                "Almeno 60 controlli con direzione debole e risultato corretto negativo.",
            )
        if accuracy < 55 or adjusted_return <= 0:
            return (
                "NON AUMENTARE",
                0.0,
                confidence,
                "Il modulo non produce ancora un vantaggio netto e persistente.",
            )
        return (
            "MANTIENI / OSSERVA",
            0.0,
            confidence,
            "Prestazione utile ma non abbastanza netta per cambiare il peso.",
        )

    # 100+ controlli: possibile revisione più seria, ma mai automatica.
    if accuracy >= 70 and adjusted_return >= 1.00:
        return (
            "AUMENTO PRUDENTE DA VALUTARE",
            0.50,
            confidence,
            "Campione maturo con accuratezza >=70% e return corretto robusto.",
        )
    if accuracy <= 42 and adjusted_return < 0:
        return (
            "RIDUZIONE PRUDENTE DA VALUTARE",
            -0.50,
            confidence,
            "Campione maturo con accuratezza debole e return corretto negativo.",
        )
    if accuracy < 55 or adjusted_return <= 0:
        return (
            "NON AUMENTARE",
            0.0,
            confidence,
            "Campione maturo, ma senza vantaggio sufficiente per aumentare il peso.",
        )
    return (
        "PESO OK",
        0.0,
        confidence,
        "Campione maturo e risultato accettabile; mantenere il peso attuale.",
    )


def build_recommendations(metrics: pd.DataFrame) -> pd.DataFrame:
    if metrics.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)

    generated = now_utc_iso()
    rows = []

    for _, row in metrics.iterrows():
        recommendation, delta, confidence, reason = recommendation_for_row(row)

        rows.append(
            {
                "generated_utc": generated,
                "asset": safe_str(row.get("asset")).upper(),
                "horizon_days": safe_int(row.get("horizon_days"), 0),
                "horizon": safe_str(row.get("horizon")),
                "horizon_family": safe_str(row.get("horizon_family")).upper(),
                "module_key": normalize_module_key(row.get("module_key")),
                "module": safe_str(row.get("module")),
                "calibration_role": safe_str(row.get("calibration_role")).upper(),
                "calibratable": parse_bool(row.get("calibratable")),
                "parent_family": safe_str(row.get("parent_family")),
                "controls": safe_int(row.get("controls"), 0),
                "correct": safe_int(row.get("correct"), 0),
                "accuracy_direction_pct": safe_float(
                    row.get("accuracy_direction_pct"),
                    np.nan,
                ),
                "avg_return_pct": safe_float(row.get("avg_return_pct"), np.nan),
                "avg_direction_adjusted_return_pct": safe_float(
                    row.get("avg_direction_adjusted_return_pct"),
                    np.nan,
                ),
                "avg_drawdown_pct": safe_float(row.get("avg_drawdown_pct"), np.nan),
                "avg_max_gain_pct": safe_float(row.get("avg_max_gain_pct"), np.nan),
                "metric_status": safe_str(row.get("status")),
                "recommendation": recommendation,
                "suggested_weight_delta": delta,
                "confidence": confidence,
                "recommendation_reason": reason,
            }
        )

    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS)


def status_from_max_controls(max_controls: int) -> str:
    if max_controls >= 100:
        return "MATURO"
    if max_controls >= 60:
        return "UTILE"
    if max_controls >= 30:
        return "PRIMA CALIBRAZIONE"
    if max_controls > 0:
        return "FEEDBACK RAPIDO"
    return "RACCOLTA DATI"


def best_calibratable_row(asset_df: pd.DataFrame):
    candidates = asset_df[
        asset_df["calibratable"].map(parse_bool)
        & (pd.to_numeric(asset_df["controls"], errors="coerce").fillna(0) > 0)
    ].copy()

    if candidates.empty:
        return None

    candidates["controls_num"] = pd.to_numeric(
        candidates["controls"],
        errors="coerce",
    ).fillna(0)
    candidates["accuracy_num"] = pd.to_numeric(
        candidates["accuracy_direction_pct"],
        errors="coerce",
    ).fillna(-999)
    candidates["adjusted_num"] = pd.to_numeric(
        candidates["avg_direction_adjusted_return_pct"],
        errors="coerce",
    ).fillna(-999)

    # Prima privilegia il campione più grande, poi qualità del risultato.
    candidates = candidates.sort_values(
        ["controls_num", "accuracy_num", "adjusted_num"],
        ascending=[False, False, False],
    )
    return candidates.iloc[0]


def summary_rows(recommendations: pd.DataFrame, signal_counts: dict):
    rows = []

    for asset in ASSETS:
        asset_df = recommendations[recommendations["asset"] == asset].copy()
        calibratable = asset_df[asset_df["calibratable"].map(parse_bool)].copy()

        if calibratable.empty:
            max_controls = 0
            rows_30 = rows_60 = rows_100 = 0
        else:
            controls = pd.to_numeric(calibratable["controls"], errors="coerce").fillna(0)
            max_controls = int(controls.max()) if len(controls) else 0
            rows_30 = int((controls >= 30).sum())
            rows_60 = int((controls >= 60).sum())
            rows_100 = int((controls >= 100).sum())

        best = best_calibratable_row(asset_df)

        if best is None:
            best_module = "n/a"
            best_horizon = "n/a"
            best_accuracy = "n/a"
            best_return = "n/a"
        else:
            best_module = safe_str(best.get("module")) or safe_str(best.get("module_key"))
            best_horizon = safe_str(best.get("horizon"))
            best_accuracy = fmt_pct(best.get("accuracy_direction_pct"), signed=False)
            best_return = fmt_pct(best.get("avg_direction_adjusted_return_pct"), signed=True)

        state = status_from_max_controls(max_controls)
        if state == "RACCOLTA DATI":
            reading = "nessun controllo calibrabile maturato"
        elif state == "FEEDBACK RAPIDO":
            reading = "feedback rapido: utile da osservare, non da pesare"
        elif state == "PRIMA CALIBRAZIONE":
            reading = "prima calibrazione possibile, solo modifiche leggere"
        elif state == "UTILE":
            reading = "campione utile, valutare con prudenza"
        else:
            reading = "campione maturo, revisione manuale possibile"

        rows.append(
            [
                asset,
                str(signal_counts.get(asset, 0)),
                state,
                str(max_controls),
                str(rows_30),
                str(rows_60),
                str(rows_100),
                best_module,
                best_horizon,
                best_accuracy,
                best_return,
                reading,
            ]
        )

    return rows


def recommendation_rows(recommendations: pd.DataFrame):
    calibratable = recommendations[
        recommendations["calibratable"].map(parse_bool)
    ].copy()

    controls = pd.to_numeric(calibratable["controls"], errors="coerce").fillna(0)
    calibratable = calibratable[controls > 0].copy()

    if calibratable.empty:
        return []

    calibratable["controls_num"] = pd.to_numeric(
        calibratable["controls"],
        errors="coerce",
    ).fillna(0)
    calibratable["horizon_days_num"] = pd.to_numeric(
        calibratable["horizon_days"],
        errors="coerce",
    ).fillna(999)

    calibratable = calibratable.sort_values(
        ["asset", "horizon_days_num", "module"],
    )

    rows = []
    for _, row in calibratable.iterrows():
        rows.append(
            [
                row["asset"],
                row["horizon"],
                row["horizon_family"],
                row["module"],
                str(int(row["controls_num"])),
                fmt_pct(row["accuracy_direction_pct"], signed=False),
                fmt_pct(row["avg_direction_adjusted_return_pct"], signed=True),
                fmt_pct(row["avg_return_pct"], signed=True),
                fmt_pct(row["avg_drawdown_pct"], signed=True),
                fmt_pct(row["avg_max_gain_pct"], signed=True),
                row["recommendation"],
                fmt_delta(row["suggested_weight_delta"]),
                row["confidence"],
            ]
        )

    return rows


def weighted_average(values, weights):
    values = pd.to_numeric(values, errors="coerce")
    weights = pd.to_numeric(weights, errors="coerce").fillna(0)
    mask = values.notna() & (weights > 0)
    if not mask.any():
        return np.nan
    return float(np.average(values[mask], weights=weights[mask]))


def family_summary_rows(recommendations: pd.DataFrame):
    data = recommendations[
        recommendations["calibratable"].map(parse_bool)
    ].copy()

    data["controls"] = pd.to_numeric(data["controls"], errors="coerce").fillna(0)
    data = data[data["controls"] > 0].copy()

    if data.empty:
        return []

    rows = []

    grouped = data.groupby(
        ["asset", "horizon_family", "module"],
        dropna=False,
    )

    for (asset, family, module), group in grouped:
        controls_total = int(group["controls"].sum())
        accuracy = weighted_average(
            group["accuracy_direction_pct"],
            group["controls"],
        )
        adjusted = weighted_average(
            group["avg_direction_adjusted_return_pct"],
            group["controls"],
        )

        rows.append(
            [
                asset,
                family,
                module,
                str(controls_total),
                fmt_pct(accuracy, signed=False),
                fmt_pct(adjusted, signed=True),
            ]
        )

    family_order = {name: index for index, name in enumerate(HORIZON_FAMILY_ORDER)}
    rows.sort(key=lambda row: (row[0], family_order.get(row[1], 999), row[2]))
    return rows


def waiting_rows(recommendations: pd.DataFrame):
    data = recommendations[
        recommendations["calibratable"].map(parse_bool)
    ].copy()

    if data.empty:
        return []

    data["controls"] = pd.to_numeric(data["controls"], errors="coerce").fillna(0)
    waiting = data[data["controls"] == 0].copy()

    rows = []
    for asset in ASSETS:
        for family in HORIZON_FAMILY_ORDER:
            count = int(
                (
                    (waiting["asset"] == asset)
                    & (waiting["horizon_family"] == family)
                ).sum()
            )
            if count > 0:
                rows.append(
                    [
                        asset,
                        family,
                        str(count),
                        "in attesa di controlli maturati",
                    ]
                )

    return rows


def excluded_rows(recommendations: pd.DataFrame):
    excluded = recommendations[
        ~recommendations["calibratable"].map(parse_bool)
    ].copy()

    if excluded.empty:
        return []

    excluded["controls"] = pd.to_numeric(excluded["controls"], errors="coerce").fillna(0)

    rows = []
    grouped = excluded.groupby(
        ["module_key", "module", "calibration_role", "parent_family"],
        dropna=False,
    )

    for (module_key, module, role, parent), group in grouped:
        max_controls = int(group["controls"].max()) if not group.empty else 0

        if role == "BENCHMARK":
            reason = "Risultato finale del Global: benchmark, non peso interno."
        elif parent:
            reason = f"Già incluso in {parent}; nessuna proposta di peso autonoma."
        else:
            reason = "Modulo diagnostico escluso dalle proposte di peso."

        rows.append(
            [
                module or module_key,
                role,
                parent or "nessuna",
                str(max_controls),
                reason,
            ]
        )

    rows.sort(key=lambda row: (row[1], row[0]))
    return rows


def build_report(recommendations: pd.DataFrame, signal_counts: dict) -> str:
    generated = now_utc_str()

    summaries = summary_rows(recommendations, signal_counts)
    rec_rows = recommendation_rows(recommendations)
    family_rows = family_summary_rows(recommendations)
    pending_rows = waiting_rows(recommendations)
    excluded = excluded_rows(recommendations)

    statistical_family_present = bool(
        (recommendations["module_key"] == "statistical_family").any()
    ) if not recommendations.empty else False

    lines = []
    lines.append("# Calibrazione pesi Global Confluence")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append("Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)")
    lines.append("")
    lines.append(
        "Questo blocco controlla se, col tempo, i moduli reali del Global Confluence "
        "meritano più peso, meno peso o peso invariato."
    )
    lines.append("")
    lines.append(
        "Correzione anti-doppio-conteggio: **la Famiglia statistica Scanner + Market Regime "
        "è il modulo calibrabile**. Scanner grezzo e Market Regime grezzo restano visibili "
        "solo come diagnostica e non ricevono proposte di peso separate."
    )
    lines.append("")
    lines.append("Regola principale:")
    lines.append("")
    lines.append("- sotto **30 controlli**: osservazione, nessuna modifica pesi")
    lines.append("- da **30 controlli**: prima calibrazione leggera")
    lines.append("- da **60 controlli**: lettura utile")
    lines.append("- da **100+ controlli**: possibile proposta prudente di modifica pesi")
    lines.append("")
    lines.append(
        "Il file continua a produrre solo raccomandazioni: **non modifica automaticamente** "
        "`global_confluence_report.py`."
    )

    if not statistical_family_present:
        lines.append("")
        lines.append(
            "**Avviso:** nel CSV non è ancora presente `statistical_family`. "
            "Esegui prima il nuovo `module_signal_tracker.py`; Scanner e Market sono comunque "
            "esclusi dalle proposte autonome per evitare il doppio conteggio."
        )

    lines.append("")
    lines.append("## Sintesi per asset")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Segnali salvati",
                "Stato",
                "Controlli max",
                "Righe 30+",
                "Righe 60+",
                "Righe 100+",
                "Miglior modulo calibrabile",
                "Orizzonte",
                "Accuratezza",
                "Return corretto direzione",
                "Lettura",
            ],
            summaries,
        )
    )

    lines.append("")
    lines.append("## Raccomandazioni per moduli calibrabili")
    lines.append("")

    if rec_rows:
        lines.append(
            md_table(
                [
                    "Asset",
                    "Orizzonte",
                    "Famiglia",
                    "Modulo",
                    "Controlli",
                    "Accuratezza",
                    "Return corretto direzione",
                    "Return medio",
                    "Drawdown medio",
                    "Max gain medio",
                    "Raccomandazione",
                    "Δ peso suggerito",
                    "Confidenza",
                ],
                rec_rows,
            )
        )
    else:
        lines.append("Nessun controllo calibrabile è ancora maturato.")

    lines.append("")
    lines.append("## Moduli esclusi dalle proposte di peso")
    lines.append("")

    if excluded:
        lines.append(
            md_table(
                [
                    "Modulo",
                    "Ruolo",
                    "Famiglia madre",
                    "Controlli max",
                    "Motivo esclusione",
                ],
                excluded,
            )
        )
    else:
        lines.append("Nessun modulo escluso trovato nel CSV.")

    lines.append("")
    lines.append("## Sintesi per famiglia temporale")
    lines.append("")

    if family_rows:
        lines.append(
            md_table(
                [
                    "Asset",
                    "Famiglia",
                    "Modulo calibrabile",
                    "Controlli totali",
                    "Accuratezza media ponderata",
                    "Return corretto direzione",
                ],
                family_rows,
            )
        )
    else:
        lines.append("Nessun controllo calibrabile ancora disponibile.")

    lines.append("")
    lines.append("## Aree ancora in attesa")
    lines.append("")

    if pending_rows:
        lines.append(
            md_table(
                ["Asset", "Famiglia", "Righe senza controlli", "Stato"],
                pending_rows,
            )
        )
    else:
        lines.append("Tutte le righe calibrabili hanno almeno un controllo.")

    lines.append("")
    lines.append("## Come leggere le raccomandazioni")
    lines.append("")
    lines.append("- **OSSERVA**: meno di 30 controlli, nessuna modifica.")
    lines.append("- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.")
    lines.append("- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.")
    lines.append("- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.")
    lines.append("- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.")
    lines.append("- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.")
    lines.append("")
    lines.append(
        "Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre "
        "modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto "
        "a capire quale parte della famiglia sta funzionando o fallendo."
    )

    lines.append("")
    lines.append("## Stato attuale")
    lines.append("")

    max_controls = 0
    if not recommendations.empty:
        calibratable = recommendations[
            recommendations["calibratable"].map(parse_bool)
        ]
        if not calibratable.empty:
            max_controls = int(
                pd.to_numeric(calibratable["controls"], errors="coerce").fillna(0).max()
            )

    if max_controls < 30:
        lines.append(
            "Siamo ancora in feedback rapido. Non bisogna modificare i pesi del Global. "
            "La nuova struttura serve ad accumulare dati corretti senza doppio conteggio."
        )
    elif max_controls < 60:
        lines.append(
            "È iniziata la prima calibrazione, ma sono ammesse solo valutazioni leggere e manuali."
        )
    elif max_controls < 100:
        lines.append(
            "Il campione comincia a essere utile. Le proposte restano prudenti e vanno verificate tra orizzonti diversi."
        )
    else:
        lines.append(
            "Il campione è maturo. Una revisione manuale dei pesi può essere valutata, evitando sovrapposizioni tra moduli."
        )

    return "\n".join(lines).rstrip() + "\n"


def save_recommendation_metrics(recommendations: pd.DataFrame) -> None:
    METRICS_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    if recommendations.empty:
        recommendations = pd.DataFrame(columns=OUTPUT_COLUMNS)

    recommendations.to_csv(METRICS_CSV_PATH, index=False)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    module_metrics = load_module_metrics()

    if module_metrics.empty:
        raise RuntimeError(
            "Global Weight Calibration: module_signal_tracker_metrics.csv non disponibile o vuoto. "
            "Esegui prima module_signal_tracker.py."
        )

    recommendations = build_recommendations(module_metrics)
    signal_counts = load_signal_counts()
    report_md = build_report(recommendations, signal_counts)

    write_text(REPORT_PATH, report_md)
    save_recommendation_metrics(recommendations)

    latest_text = read_text(LATEST_REPORT_PATH)
    if latest_text:
        updated = replace_or_insert_block(latest_text, report_md)
        write_text(LATEST_REPORT_PATH, updated)
    else:
        write_text(
            LATEST_REPORT_PATH,
            f"{START_MARKER}\n{report_md}{END_MARKER}\n",
        )

    print(f"Global Weight Calibration report scritto in: {REPORT_PATH}")
    print(f"Metriche calibrazione scritte in: {METRICS_CSV_PATH}")
    print(f"Latest report aggiornato: {LATEST_REPORT_PATH}")

    calibratable_rows = recommendations[
        recommendations["calibratable"].map(parse_bool)
    ]
    excluded_rows_count = len(recommendations) - len(calibratable_rows)

    print(
        f"Righe calibrabili: {len(calibratable_rows)} | "
        f"righe benchmark/diagnostiche escluse: {excluded_rows_count}"
    )


if __name__ == "__main__":
    main()
