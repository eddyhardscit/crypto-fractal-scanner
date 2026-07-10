import csv
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd


REPORTS_DIR = Path("reports")

LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"

MODULE_METRICS_PATH = REPORTS_DIR / "module_signal_tracker_metrics.csv"
MODULE_HISTORY_PATH = REPORTS_DIR / "module_signal_tracker_history.csv"

REPORT_PATH = REPORTS_DIR / "global_weight_calibration_report.md"
SUMMARY_CSV_PATH = REPORTS_DIR / "global_weight_calibration_metrics.csv"

START_MARKER = "<!-- GLOBAL_WEIGHT_CALIBRATION_START -->"
END_MARKER = "<!-- GLOBAL_WEIGHT_CALIBRATION_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

HORIZON_ORDER = [1, 2, 3, 5, 7, 10, 14, 21, 30, 45, 60]

MODULE_ORDER = [
    "global",
    "scanner",
    "market",
    "technical",
    "classic_technical",
    "sol_fractal",
]

MODULE_LABELS = {
    "global": "Global Confluence",
    "scanner": "Scanner",
    "market": "Market regime",
    "technical": "Tecnico",
    "classic_technical": "Classic technical",
    "sol_fractal": "Frattale SOL",
}

FAMILY_ORDER = {
    "BREVE": 1,
    "SETTIMANALE": 2,
    "SWING": 3,
    "MEDIO": 4,
}

MIN_FIRST_CALIBRATION = 30
MIN_USEFUL = 60
MIN_MATURE = 100


def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


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

    risk_start = "<!-- RISK_CALIBRATION_START -->"
    if risk_start in text:
        return text.replace(risk_start, full_block + "\n\n" + risk_start, 1)

    module_end = "<!-- MODULE_ACCURACY_END -->"
    if module_end in text:
        return text.replace(module_end, module_end + "\n\n" + full_block, 1)

    global_end = "<!-- GLOBAL_CONFLUENCE_END -->"
    if global_end in text:
        return text.replace(global_end, global_end + "\n\n" + full_block, 1)

    return text.rstrip() + "\n\n" + full_block + "\n"


def safe_str(value, default="") -> str:
    if value is None:
        return default

    try:
        if pd.isna(value):
            return default
    except Exception:
        pass

    return str(value)


def safe_float(value, default=np.nan):
    try:
        if value is None:
            return default

        if isinstance(value, str):
            s = value.strip()
            if not s or s.lower() in {"nan", "none", "n/a", "null", "-"}:
                return default

            s = s.replace("%", "")
            s = s.replace("$", "")
            s = s.replace(" ", "")

            if "," in s:
                s = s.replace(".", "")
                s = s.replace(",", ".")

            return float(s)

        if pd.isna(value):
            return default

        return float(value)

    except Exception:
        return default


def safe_int(value, default=0) -> int:
    v = safe_float(value, np.nan)
    if pd.isna(v):
        return default
    return int(v)


def fmt_pct(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):+.{decimals}f}%".replace(".", ",")


def fmt_pct_plain(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):.{decimals}f}%".replace(".", ",")


def fmt_signed(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"

    v = float(value)

    if decimals == 0:
        iv = int(round(v))
        if iv > 0:
            return f"+{iv}"
        return str(iv)

    if v > 0:
        return f"+{v:.{decimals}f}".replace(".", ",")

    return f"{v:.{decimals}f}".replace(".", ",")


def md_table(headers, rows) -> str:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")

    return "\n".join(out)


def read_module_metrics() -> pd.DataFrame:
    if not MODULE_METRICS_PATH.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(MODULE_METRICS_PATH)
    except Exception:
        return pd.DataFrame()

    if df.empty:
        return df

    required_cols = [
        "asset",
        "horizon_days",
        "horizon",
        "horizon_family",
        "module_key",
        "module",
        "controls",
        "correct",
        "accuracy_direction_pct",
        "avg_return_pct",
        "avg_direction_adjusted_return_pct",
        "avg_drawdown_pct",
        "avg_max_gain_pct",
        "status",
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = np.nan

    df["asset"] = df["asset"].astype(str).str.upper().str.strip()
    df["module_key"] = df["module_key"].astype(str).str.strip()
    df["module"] = df["module"].fillna(df["module_key"]).astype(str)
    df["horizon_family"] = df["horizon_family"].fillna("").astype(str).str.upper().str.strip()

    numeric_cols = [
        "horizon_days",
        "controls",
        "correct",
        "accuracy_direction_pct",
        "avg_return_pct",
        "avg_direction_adjusted_return_pct",
        "avg_drawdown_pct",
        "avg_max_gain_pct",
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["controls"] = df["controls"].fillna(0).astype(int)
    df["horizon_days"] = df["horizon_days"].fillna(0).astype(int)

    df = df[df["asset"].isin(ASSETS)].copy()

    return df


def read_history_counts():
    counts = {asset: 0 for asset in ASSETS}

    if not MODULE_HISTORY_PATH.exists():
        return counts

    try:
        df = pd.read_csv(MODULE_HISTORY_PATH, dtype=str)
    except Exception:
        return counts

    if df.empty or "asset" not in df.columns:
        return counts

    df["asset"] = df["asset"].astype(str).str.upper().str.strip()

    for asset in ASSETS:
        counts[asset] = int((df["asset"] == asset).sum())

    return counts


def maturity_status(max_controls: int) -> str:
    if max_controls >= MIN_MATURE:
        return "MATURO"
    if max_controls >= MIN_USEFUL:
        return "UTILE"
    if max_controls >= MIN_FIRST_CALIBRATION:
        return "PRIMA CALIBRAZIONE"
    if max_controls > 0:
        return "FEEDBACK RAPIDO"
    return "RACCOLTA DATI"


def maturity_explanation(max_controls: int) -> str:
    if max_controls >= MIN_MATURE:
        return "abbastanza controlli per valutare modifiche prudenti ai pesi"
    if max_controls >= MIN_USEFUL:
        return "lettura utile, ma modifica pesi ancora prudente"
    if max_controls >= MIN_FIRST_CALIBRATION:
        return "prima calibrazione leggera possibile, senza automatismi"
    if max_controls > 0:
        return "feedback rapido: utile da osservare, non da pesare"
    return "nessun controllo maturato: non modificare i pesi"


def recommendation_for_row(row) -> dict:
    controls = safe_int(row.get("controls"), 0)
    accuracy = safe_float(row.get("accuracy_direction_pct"))
    adjusted_return = safe_float(row.get("avg_direction_adjusted_return_pct"))
    avg_return = safe_float(row.get("avg_return_pct"))

    if controls <= 0:
        return {
            "recommendation": "NESSUN DATO",
            "suggested_weight_change": 0.0,
            "confidence": "NULLA",
            "reason": "nessun controllo maturato",
        }

    if controls < MIN_FIRST_CALIBRATION:
        return {
            "recommendation": "OSSERVA",
            "suggested_weight_change": 0.0,
            "confidence": "BASSA",
            "reason": "meno di 30 controlli: feedback rapido, non calibrazione",
        }

    if pd.isna(accuracy) or pd.isna(adjusted_return):
        return {
            "recommendation": "MANTIENI",
            "suggested_weight_change": 0.0,
            "confidence": "BASSA",
            "reason": "metriche incomplete",
        }

    confidence = "MEDIA"
    if controls >= MIN_MATURE:
        confidence = "ALTA"
    elif controls >= MIN_USEFUL:
        confidence = "MEDIA / BUONA"

    if accuracy >= 65 and adjusted_return > 0.75:
        change = 0.5 if controls < MIN_MATURE else 1.0
        return {
            "recommendation": "POSSIBILE AUMENTO LEGGERO",
            "suggested_weight_change": change,
            "confidence": confidence,
            "reason": "accuratezza alta e return corretto direzione positivo",
        }

    if accuracy >= 58 and adjusted_return > 0:
        return {
            "recommendation": "PESO OK",
            "suggested_weight_change": 0.0,
            "confidence": confidence,
            "reason": "modulo utile, ma non abbastanza forte per aumentare il peso",
        }

    if 48 <= accuracy < 58:
        return {
            "recommendation": "MANTIENI / OSSERVA",
            "suggested_weight_change": 0.0,
            "confidence": confidence,
            "reason": "risultato vicino al neutro",
        }

    if accuracy < 45 and adjusted_return < 0:
        change = -0.5 if controls < MIN_MATURE else -1.0
        return {
            "recommendation": "POSSIBILE RIDUZIONE PESO",
            "suggested_weight_change": change,
            "confidence": confidence,
            "reason": "bassa accuratezza e return corretto direzione negativo",
        }

    if accuracy < 50:
        return {
            "recommendation": "NON AUMENTARE",
            "suggested_weight_change": 0.0,
            "confidence": confidence,
            "reason": "accuratezza sotto 50%, ma prova ancora non decisiva",
        }

    return {
        "recommendation": "MANTIENI",
        "suggested_weight_change": 0.0,
        "confidence": confidence,
        "reason": "nessun segnale chiaro per cambiare peso",
    }


def enrich_metrics(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    out = df.copy()

    recommendations = []
    weight_changes = []
    confidences = []
    reasons = []

    for _, row in out.iterrows():
        r = recommendation_for_row(row)
        recommendations.append(r["recommendation"])
        weight_changes.append(r["suggested_weight_change"])
        confidences.append(r["confidence"])
        reasons.append(r["reason"])

    out["weight_recommendation"] = recommendations
    out["suggested_weight_change"] = weight_changes
    out["recommendation_confidence"] = confidences
    out["recommendation_reason"] = reasons

    out["module_order"] = out["module_key"].map(
        {k: i for i, k in enumerate(MODULE_ORDER)}
    ).fillna(999).astype(int)

    out["horizon_order"] = out["horizon_days"].map(
        {h: i for i, h in enumerate(HORIZON_ORDER)}
    ).fillna(999).astype(int)

    out["family_order"] = out["horizon_family"].map(FAMILY_ORDER).fillna(999).astype(int)

    return out


def build_asset_summary(metrics: pd.DataFrame, history_counts: dict):
    rows = []

    for asset in ASSETS:
        asset_df = metrics[metrics["asset"] == asset].copy()

        if asset_df.empty:
            max_controls = 0
            modules_30 = 0
            modules_60 = 0
            modules_100 = 0
            best_module = "n/a"
            best_horizon = "n/a"
            best_accuracy = np.nan
            best_adj_return = np.nan
        else:
            max_controls = int(asset_df["controls"].max())
            modules_30 = int(len(asset_df[asset_df["controls"] >= MIN_FIRST_CALIBRATION]))
            modules_60 = int(len(asset_df[asset_df["controls"] >= MIN_USEFUL]))
            modules_100 = int(len(asset_df[asset_df["controls"] >= MIN_MATURE]))

            usable = asset_df[asset_df["controls"] > 0].copy()

            if usable.empty:
                best_module = "n/a"
                best_horizon = "n/a"
                best_accuracy = np.nan
                best_adj_return = np.nan
            else:
                usable["rank_score"] = (
                    usable["controls"].clip(upper=100) * 0.25
                    + usable["accuracy_direction_pct"].fillna(0) * 0.50
                    + usable["avg_direction_adjusted_return_pct"].fillna(0).clip(lower=-20, upper=20) * 2.0
                )

                best = usable.sort_values("rank_score", ascending=False).iloc[0]
                best_module = safe_str(best["module"])
                best_horizon = safe_str(best["horizon"])
                best_accuracy = safe_float(best["accuracy_direction_pct"])
                best_adj_return = safe_float(best["avg_direction_adjusted_return_pct"])

        status = maturity_status(max_controls)
        explanation = maturity_explanation(max_controls)

        rows.append(
            [
                asset,
                str(history_counts.get(asset, 0)),
                status,
                str(max_controls),
                str(modules_30),
                str(modules_60),
                str(modules_100),
                best_module,
                best_horizon,
                fmt_pct_plain(best_accuracy),
                fmt_pct(best_adj_return),
                explanation,
            ]
        )

    return rows


def build_action_rows(metrics: pd.DataFrame):
    if metrics.empty:
        return []

    active = metrics[metrics["controls"] > 0].copy()

    if active.empty:
        return []

    active = active.sort_values(
        [
            "asset",
            "controls",
            "horizon_order",
            "module_order",
        ],
        ascending=[True, False, True, True],
    )

    rows = []

    for _, r in active.iterrows():
        rows.append(
            [
                r["asset"],
                safe_str(r["horizon"]),
                safe_str(r["horizon_family"]),
                safe_str(r["module"]),
                str(int(r["controls"])),
                fmt_pct_plain(r["accuracy_direction_pct"]),
                fmt_pct(r["avg_direction_adjusted_return_pct"]),
                fmt_pct(r["avg_return_pct"]),
                fmt_pct(r["avg_drawdown_pct"]),
                fmt_pct(r["avg_max_gain_pct"]),
                safe_str(r["weight_recommendation"]),
                fmt_signed(r["suggested_weight_change"], decimals=1),
                safe_str(r["recommendation_confidence"]),
            ]
        )

    return rows


def build_zero_control_rows(metrics: pd.DataFrame):
    if metrics.empty:
        return []

    zero = metrics[metrics["controls"] == 0].copy()

    if zero.empty:
        return []

    grouped = (
        zero.groupby(["asset", "horizon_family"], dropna=False)
        .agg(rows=("module_key", "count"))
        .reset_index()
    )

    grouped["family_order"] = grouped["horizon_family"].map(FAMILY_ORDER).fillna(999)
    grouped = grouped.sort_values(["asset", "family_order"])

    rows = []

    for _, r in grouped.iterrows():
        rows.append(
            [
                r["asset"],
                r["horizon_family"],
                str(int(r["rows"])),
                "in attesa di controlli maturati",
            ]
        )

    return rows


def build_family_summary(metrics: pd.DataFrame):
    if metrics.empty:
        return []

    active = metrics[metrics["controls"] > 0].copy()

    if active.empty:
        return []

    rows = []

    for (asset, family, module_key, module), g in active.groupby(
        ["asset", "horizon_family", "module_key", "module"], dropna=False
    ):
        total_controls = int(g["controls"].sum())

        if total_controls <= 0:
            continue

        weights = g["controls"].replace(0, np.nan)

        accuracy = np.average(
            g["accuracy_direction_pct"].fillna(0),
            weights=g["controls"].clip(lower=1),
        )

        adj_return = np.average(
            g["avg_direction_adjusted_return_pct"].fillna(0),
            weights=g["controls"].clip(lower=1),
        )

        rows.append(
            {
                "asset": asset,
                "family": family,
                "module": module,
                "module_key": module_key,
                "controls": total_controls,
                "accuracy": accuracy,
                "adj_return": adj_return,
            }
        )

    if not rows:
        return []

    out = pd.DataFrame(rows)
    out["family_order"] = out["family"].map(FAMILY_ORDER).fillna(999)
    out["module_order"] = out["module_key"].map(
        {k: i for i, k in enumerate(MODULE_ORDER)}
    ).fillna(999)

    out = out.sort_values(["asset", "family_order", "module_order"])

    table_rows = []

    for _, r in out.iterrows():
        table_rows.append(
            [
                r["asset"],
                r["family"],
                r["module"],
                str(int(r["controls"])),
                fmt_pct_plain(r["accuracy"]),
                fmt_pct(r["adj_return"]),
            ]
        )

    return table_rows


def build_report(metrics: pd.DataFrame, history_counts: dict) -> str:
    generated = now_utc_str()

    asset_rows = build_asset_summary(metrics, history_counts)
    active_rows = build_action_rows(metrics)
    zero_rows = build_zero_control_rows(metrics)
    family_rows = build_family_summary(metrics)

    lines = []

    lines.append("# Calibrazione pesi Global Confluence")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append("Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)")
    lines.append("")
    lines.append(
        "Questo blocco controlla se, col tempo, i moduli del Global Confluence meritano più peso, "
        "meno peso o peso invariato."
    )
    lines.append("")
    lines.append(
        "Ora legge il nuovo `module_signal_tracker_metrics.csv`, quindi include anche i nuovi orizzonti "
        "**1g / 2g / 3g / 5g / 7g / 10g / 14g / 21g / 30g / 45g / 60g** "
        "e il modulo **Classic technical**."
    )
    lines.append("")
    lines.append("Regola principale:")
    lines.append("")
    lines.append("- sotto **30 controlli**: osservazione, nessuna modifica pesi")
    lines.append("- da **30 controlli**: prima calibrazione leggera")
    lines.append("- da **60 controlli**: lettura utile")
    lines.append("- da **100+ controlli**: possibile proposta prudente di modifica pesi")
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
                "Miglior modulo attuale",
                "Orizzonte",
                "Accuratezza",
                "Return corretto direzione",
                "Lettura",
            ],
            asset_rows,
        )
    )

    lines.append("")
    lines.append("## Raccomandazioni moduli con controlli maturati")
    lines.append("")

    if active_rows:
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
                active_rows,
            )
        )
    else:
        lines.append(
            "Nessun controllo modulo ancora maturato. È normale al primo run: "
            "i controlli 1g iniziano dal giorno successivo."
        )

    lines.append("")
    lines.append("## Sintesi per famiglia temporale")
    lines.append("")

    if family_rows:
        lines.append(
            md_table(
                [
                    "Asset",
                    "Famiglia",
                    "Modulo",
                    "Controlli totali",
                    "Accuratezza media",
                    "Return corretto direzione",
                ],
                family_rows,
            )
        )
    else:
        lines.append("Nessuna famiglia temporale ha ancora controlli maturati.")

    lines.append("")
    lines.append("## Aree ancora in attesa")
    lines.append("")

    if zero_rows:
        lines.append(
            md_table(
                ["Asset", "Famiglia", "Righe senza controlli", "Stato"],
                zero_rows,
            )
        )
    else:
        lines.append("Tutte le aree hanno almeno un controllo maturato.")

    lines.append("")
    lines.append("## Come leggere le raccomandazioni")
    lines.append("")
    lines.append("- **OSSERVA**: ci sono pochi controlli, quindi il dato è rumore utile solo da monitorare.")
    lines.append("- **PESO OK**: il modulo sta aiutando, ma non abbastanza da aumentare peso.")
    lines.append("- **MANTIENI / OSSERVA**: risultato vicino al neutro.")
    lines.append("- **NON AUMENTARE**: il modulo non sta ancora dimostrando abbastanza utilità.")
    lines.append("- **POSSIBILE AUMENTO LEGGERO**: modulo buono, ma la modifica resta prudente.")
    lines.append("- **POSSIBILE RIDUZIONE PESO**: modulo debole su quell’orizzonte, da ridurre solo con dati maturi.")
    lines.append("")
    lines.append("Nota importante: questo file **non modifica automaticamente** `global_confluence_report.py`.")
    lines.append("Produce solo una raccomandazione leggibile. La modifica reale dei pesi va fatta a mano, dopo abbastanza dati.")
    lines.append("")
    lines.append("## Stato attuale")
    lines.append("")

    max_controls_all = 0
    if not metrics.empty:
        max_controls_all = int(metrics["controls"].max())

    if max_controls_all == 0:
        lines.append(
            "Per ora il sistema è ancora in **raccolta dati**. Il nuovo tracker ha salvato i segnali, "
            "ma nessun orizzonte è ancora maturato. Dal prossimo run giornaliero dovrebbero iniziare i controlli 1g."
        )
    elif max_controls_all < MIN_FIRST_CALIBRATION:
        lines.append(
            "Ci sono già alcuni controlli brevi, ma siamo ancora in feedback rapido. "
            "Non bisogna modificare pesi del Global."
        )
    elif max_controls_all < MIN_USEFUL:
        lines.append(
            "È iniziata la prima calibrazione. Le raccomandazioni sono utili, ma ancora leggere."
        )
    elif max_controls_all < MIN_MATURE:
        lines.append(
            "La calibrazione è utile. Le modifiche ai pesi possono essere considerate, ma con prudenza."
        )
    else:
        lines.append(
            "La calibrazione è matura. Le proposte di modifica peso possono essere valutate seriamente."
        )

    return "\n".join(lines).rstrip() + "\n"


def write_summary_csv(metrics: pd.DataFrame) -> None:
    SUMMARY_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "generated_utc",
        "asset",
        "horizon_days",
        "horizon",
        "horizon_family",
        "module_key",
        "module",
        "controls",
        "correct",
        "accuracy_direction_pct",
        "avg_return_pct",
        "avg_direction_adjusted_return_pct",
        "avg_drawdown_pct",
        "avg_max_gain_pct",
        "status",
        "weight_recommendation",
        "suggested_weight_change",
        "recommendation_confidence",
        "recommendation_reason",
    ]

    generated = now_utc_iso()

    rows = []

    if not metrics.empty:
        for _, r in metrics.iterrows():
            row = {k: r.get(k, "") for k in fieldnames}
            row["generated_utc"] = generated
            rows.append(row)

    with SUMMARY_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    raw_metrics = read_module_metrics()
    metrics = enrich_metrics(raw_metrics)

    history_counts = read_history_counts()

    report_md = build_report(metrics, history_counts)

    write_text(REPORT_PATH, report_md)
    write_summary_csv(metrics)

    latest_text = read_text(LATEST_REPORT_PATH)
    if latest_text:
        updated = replace_or_insert_block(latest_text, report_md)
        write_text(LATEST_REPORT_PATH, updated)
    else:
        write_text(LATEST_REPORT_PATH, f"{START_MARKER}\n{report_md}{END_MARKER}\n")

    print(f"Global weight calibration report scritto in: {REPORT_PATH}")
    print(f"Metriche global weight calibration scritte in: {SUMMARY_CSV_PATH}")


if __name__ == "__main__":
    main()
