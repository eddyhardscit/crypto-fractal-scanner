from pathlib import Path
from datetime import datetime, timezone
import re

import numpy as np
import pandas as pd


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"

OUTPUT_REPORT = REPORTS_DIR / "global_weight_calibration_report.md"
OUTPUT_METRICS = REPORTS_DIR / "global_weight_calibration_metrics.csv"

GLOBAL_CONFLUENCE_METRICS = REPORTS_DIR / "global_confluence_metrics.csv"

MODULE_ACCURACY_CANDIDATES = [
    REPORTS_DIR / "module_signal_accuracy_metrics.csv",
    REPORTS_DIR / "module_accuracy_metrics.csv",
    REPORTS_DIR / "module_signal_tracker_metrics.csv",
    REPORTS_DIR / "module_signal_metrics.csv",
]

START_MARKER = "<!-- GLOBAL_WEIGHT_CALIBRATION_START -->"
END_MARKER = "<!-- GLOBAL_WEIGHT_CALIBRATION_END -->"

MIN_OBSERVATION_CHECKS = 30
MIN_LIGHT_SUGGESTION_CHECKS = 60
MIN_AUTO_WEIGHT_CHECKS = 100

FOCUS_HORIZONS = [30, 60]


def utc_now():
    return datetime.now(timezone.utc)


def read_text(path):
    if not path.exists():
        return ""

    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def safe_float(x):
    try:
        if pd.isna(x):
            return np.nan
        return float(x)
    except Exception:
        return np.nan


def parse_number(value):
    if value is None:
        return np.nan

    s = str(value).strip()

    if not s or s.lower() in ["nan", "none", "null", "n/a", "nd", "n/d"]:
        return np.nan

    s = s.replace("%", "")
    s = s.replace("$", "")
    s = s.replace("€", "")
    s = s.replace("+", "")
    s = s.replace("−", "-")
    s = s.replace(" ", "")

    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")

    s = re.sub(r"[^0-9.\-]", "", s)

    if not s or s in ["-", ".", "-."]:
        return np.nan

    try:
        return float(s)
    except Exception:
        return np.nan


def parse_int(value):
    x = parse_number(value)

    if pd.isna(x):
        return 0

    return int(round(x))


def parse_horizon(value):
    if value is None:
        return np.nan

    s = str(value).strip().lower()
    m = re.search(r"([0-9]+)", s)

    if not m:
        return np.nan

    return int(m.group(1))


def clean_text(value):
    if value is None:
        return ""

    s = str(value)
    s = s.replace("**", "")
    s = s.replace("__", "")
    s = s.replace("`", "")
    s = s.replace("|", " ")
    s = re.sub(r"\s+", " ", s)

    return s.strip()


def fmt_pct(value):
    x = safe_float(value)

    if pd.isna(x):
        return "n/a"

    return f"{x:.2f}%".replace(".", ",")


def fmt_num(value, decimals=2):
    x = safe_float(value)

    if pd.isna(x):
        return "n/a"

    return f"{x:.{decimals}f}".replace(".", ",")


def fmt_int(value):
    try:
        return str(int(value))
    except Exception:
        return "0"


def fmt_delta(value):
    x = safe_float(value)

    if pd.isna(x):
        return "n/a"

    if x > 0:
        return f"+{x:.2f}".replace(".", ",")

    return f"{x:.2f}".replace(".", ",")


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


def normalize_col_name(col):
    s = str(col).strip().lower()
    s = s.replace("%", "pct")
    s = s.replace("/", "_")
    s = s.replace("-", "_")
    s = s.replace(" ", "_")
    s = re.sub(r"[^a-z0-9_àèéìòù]", "", s)
    s = re.sub(r"_+", "_", s)

    return s.strip("_")


def canonical_module_name(value):
    s = clean_text(value)
    low = s.lower()

    if "global" in low:
        return "Global confluence"

    if "market" in low or "regime" in low:
        return "Market regime"

    if "scanner" in low and "path" in low:
        return "Scanner path"

    if "scanner" in low:
        return "Scanner"

    if "tecnico" in low or "technical" in low or "struttura" in low:
        return "Tecnico"

    if "frattale" in low or "fractal" in low:
        if "path" in low or "tracker" in low:
            return "Fractal path"
        return "Frattale SOL"

    if "rsi" in low:
        return "RSI top-cycle"

    if "lifecycle" in low or "ema" in low:
        return "Lifecycle EMA"

    if "future" in low or "liquid" in low:
        return "Futures"

    if "daily" in low or "giornal" in low:
        return "Daily change"

    return s if s else "n/d"


def canonical_asset(value):
    s = clean_text(value).upper()

    if "BTC" in s:
        return "BTC"

    if "SOL" in s:
        return "SOL"

    if "DOGE" in s:
        return "DOGE"

    return s.replace("-USD", "")


def find_col(df, names):
    if df is None or df.empty:
        return None

    norm_map = {normalize_col_name(c): c for c in df.columns}

    for name in names:
        n = normalize_col_name(name)
        if n in norm_map:
            return norm_map[n]

    return None


def parse_markdown_table_after_heading(section, heading_text):
    lines = section.splitlines()
    start = None

    for i, line in enumerate(lines):
        if heading_text.lower() in line.lower():
            start = i
            break

    if start is None:
        return pd.DataFrame()

    table_lines = []
    found_table = False

    for line in lines[start + 1:]:
        if line.strip().startswith("|"):
            found_table = True
            table_lines.append(line.strip())
        elif found_table:
            break

    if len(table_lines) < 3:
        return pd.DataFrame()

    header = [clean_text(c) for c in table_lines[0].strip("|").split("|")]
    data_lines = table_lines[2:]

    rows = []

    for line in data_lines:
        cells = [clean_text(c) for c in line.strip("|").split("|")]

        if len(cells) != len(header):
            continue

        rows.append(dict(zip(header, cells)))

    return pd.DataFrame(rows)


def extract_section(text, start_marker, end_marker):
    if not text:
        return ""

    if start_marker not in text or end_marker not in text:
        return ""

    start = text.find(start_marker)
    end = text.find(end_marker)

    if start == -1 or end == -1 or end <= start:
        return ""

    return text[start:end]


def load_module_accuracy_from_csv():
    for path in MODULE_ACCURACY_CANDIDATES:
        if not path.exists():
            continue

        try:
            df = pd.read_csv(path)
        except Exception:
            continue

        if df is not None and not df.empty:
            return df, path.name

    return pd.DataFrame(), ""


def load_module_accuracy_from_latest_report():
    latest = read_text(LATEST_REPORT)

    if not latest:
        return pd.DataFrame(), ""

    section = extract_section(
        latest,
        "<!-- MODULE_ACCURACY_START -->",
        "<!-- MODULE_ACCURACY_END -->",
    )

    if not section:
        return pd.DataFrame(), ""

    df = parse_markdown_table_after_heading(section, "Accuratezza direzionale per modulo")

    if df.empty:
        return pd.DataFrame(), ""

    return df, "latest_report.md / MODULE_ACCURACY"


def normalize_module_accuracy(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    asset_col = find_col(out, ["asset", "Asset", "target"])
    horizon_col = find_col(out, ["horizon_days", "Orizzonte", "Giorno", "Horizon"])
    module_col = find_col(out, ["module", "Modulo", "Signal", "Componente"])
    checks_col = find_col(out, ["checks", "checked", "Controlli", "checked_signals", "Segnali controllati"])
    acc_col = find_col(out, ["direction_accuracy_pct", "Accuratezza direzione", "Accuracy", "accuracy_pct"])
    return_col = find_col(out, ["avg_return_pct", "Return medio", "Rendimento medio"])
    drawdown_col = find_col(out, ["avg_drawdown_pct", "Drawdown medio", "Discesa media"])
    max_gain_col = find_col(out, ["avg_max_gain_pct", "Max gain medio", "Rialzo medio"])
    status_col = find_col(out, ["status", "Stato"])

    normalized = pd.DataFrame()

    if asset_col:
        normalized["asset"] = out[asset_col].map(canonical_asset)
    else:
        normalized["asset"] = "n/d"

    if horizon_col:
        normalized["horizon_days"] = out[horizon_col].map(parse_horizon)
    else:
        normalized["horizon_days"] = np.nan

    if module_col:
        normalized["module"] = out[module_col].map(canonical_module_name)
    else:
        normalized["module"] = "n/d"

    if checks_col:
        normalized["checked"] = out[checks_col].map(parse_int)
    else:
        normalized["checked"] = 0

    if acc_col:
        normalized["direction_accuracy_pct"] = out[acc_col].map(parse_number)
    else:
        normalized["direction_accuracy_pct"] = np.nan

    if return_col:
        normalized["avg_return_pct"] = out[return_col].map(parse_number)
    else:
        normalized["avg_return_pct"] = np.nan

    if drawdown_col:
        normalized["avg_drawdown_pct"] = out[drawdown_col].map(parse_number)
    else:
        normalized["avg_drawdown_pct"] = np.nan

    if max_gain_col:
        normalized["avg_max_gain_pct"] = out[max_gain_col].map(parse_number)
    else:
        normalized["avg_max_gain_pct"] = np.nan

    if status_col:
        normalized["source_status"] = out[status_col].map(clean_text)
    else:
        normalized["source_status"] = ""

    normalized = normalized.dropna(subset=["horizon_days"])
    normalized["horizon_days"] = normalized["horizon_days"].astype(int)

    normalized = normalized[
        (normalized["asset"] != "") &
        (normalized["module"] != "") &
        (normalized["module"] != "n/d")
    ].copy()

    return normalized


def load_module_accuracy():
    df, source = load_module_accuracy_from_csv()

    if df.empty:
        df, source = load_module_accuracy_from_latest_report()

    normalized = normalize_module_accuracy(df)

    return normalized, source


def load_current_global_scores():
    if not GLOBAL_CONFLUENCE_METRICS.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(GLOBAL_CONFLUENCE_METRICS)
    except Exception:
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    out = df.copy()

    asset_col = find_col(out, ["asset", "Asset"])
    if not asset_col:
        return pd.DataFrame()

    out["asset"] = out[asset_col].map(canonical_asset)

    score_columns = {
        "scanner_score": "Scanner",
        "scanner_path_score": "Scanner path",
        "market_regime_score": "Market regime",
        "technical_score": "Tecnico",
        "fractal_score": "Frattale SOL",
        "fractal_path_score": "Fractal path",
        "rsi_top_cycle_score": "RSI top-cycle",
        "lifecycle_squeeze_score": "Lifecycle EMA",
        "futures_score": "Futures",
        "daily_change_score": "Daily change",
        "total_score": "Totale",
        "score": "Totale",
    }

    rows = []

    for _, r in out.iterrows():
        asset = canonical_asset(r.get("asset", ""))

        for col, module in score_columns.items():
            if col not in out.columns:
                continue

            value = safe_float(r.get(col, np.nan))

            if pd.isna(value):
                continue

            rows.append({
                "asset": asset,
                "module": module,
                "current_score": value,
            })

    return pd.DataFrame(rows)


def stage_from_checks(checked):
    checked = int(checked or 0)

    if checked < MIN_OBSERVATION_CHECKS:
        return "RACCOLTA DATI"

    if checked < MIN_LIGHT_SUGGESTION_CHECKS:
        return "OSSERVAZIONE 30+"

    if checked < MIN_AUTO_WEIGHT_CHECKS:
        return "SUGGERIMENTO LEGGERO"

    return "PRONTO PER PESI"


def stage_description(stage):
    if stage == "RACCOLTA DATI":
        return "troppi pochi controlli: non modificare i pesi"

    if stage == "OSSERVAZIONE 30+":
        return "dati iniziali: osservare, ma non applicare"

    if stage == "SUGGERIMENTO LEGGERO":
        return "può suggerire piccole correzioni, senza automatismi forti"

    if stage == "PRONTO PER PESI":
        return "dati sufficienti per valutare una modifica prudente dei pesi"

    return ""


def reliability_from_checks(checked):
    checked = int(checked or 0)

    if checked < MIN_OBSERVATION_CHECKS:
        return "INSUFFICIENTE"

    if checked < MIN_LIGHT_SUGGESTION_CHECKS:
        return "BASSA"

    if checked < MIN_AUTO_WEIGHT_CHECKS:
        return "MEDIA"

    return "ALTA"


def suggest_weight_delta(checked, accuracy_pct, avg_return_pct):
    """
    Suggerisce una correzione futura del peso del modulo.

    Importante:
    - sotto 60 controlli ritorna sempre 0;
    - tra 60 e 99 dà solo suggerimenti leggeri;
    - da 100 controlli può dare un suggerimento più deciso;
    - questo file NON applica i pesi, li misura soltanto.
    """
    checked = int(checked or 0)
    acc = safe_float(accuracy_pct)
    avg_ret = safe_float(avg_return_pct)

    if checked < MIN_LIGHT_SUGGESTION_CHECKS:
        return 0.0

    if pd.isna(acc):
        return 0.0

    strong_data = checked >= MIN_AUTO_WEIGHT_CHECKS

    if strong_data:
        if acc >= 70:
            return 1.0
        if acc >= 60:
            return 0.5
        if acc <= 35:
            return -1.0
        if acc <= 45:
            return -0.5
        return 0.0

    if acc >= 70:
        return 0.5

    if acc <= 40:
        return -0.5

    return 0.0


def suggestion_label(delta, checked):
    delta = safe_float(delta)
    checked = int(checked or 0)

    if checked < MIN_LIGHT_SUGGESTION_CHECKS:
        return "nessun suggerimento"

    if pd.isna(delta) or delta == 0:
        return "mantieni peso"

    if delta > 0:
        return "valuta aumento peso"

    return "valuta riduzione peso"


def build_weight_calibration_metrics(module_accuracy):
    if module_accuracy is None or module_accuracy.empty:
        return pd.DataFrame()

    rows = []

    for _, r in module_accuracy.iterrows():
        asset = canonical_asset(r.get("asset", ""))
        module = canonical_module_name(r.get("module", ""))
        horizon = parse_horizon(r.get("horizon_days", np.nan))
        checked = parse_int(r.get("checked", 0))

        accuracy = safe_float(r.get("direction_accuracy_pct", np.nan))
        avg_return = safe_float(r.get("avg_return_pct", np.nan))
        avg_drawdown = safe_float(r.get("avg_drawdown_pct", np.nan))
        avg_max_gain = safe_float(r.get("avg_max_gain_pct", np.nan))

        stage = stage_from_checks(checked)
        reliability = reliability_from_checks(checked)
        delta = suggest_weight_delta(checked, accuracy, avg_return)

        rows.append({
            "asset": asset,
            "module": module,
            "horizon_days": horizon,
            "checked": checked,
            "direction_accuracy_pct": accuracy,
            "avg_return_pct": avg_return,
            "avg_drawdown_pct": avg_drawdown,
            "avg_max_gain_pct": avg_max_gain,
            "calibration_stage": stage,
            "reliability": reliability,
            "suggested_weight_delta": delta,
            "suggestion": suggestion_label(delta, checked),
            "can_apply_to_global": checked >= MIN_AUTO_WEIGHT_CHECKS,
            "note": stage_description(stage),
        })

    metrics = pd.DataFrame(rows)

    if metrics.empty:
        return metrics

    metrics = metrics.sort_values(
        ["asset", "horizon_days", "module"],
        ascending=[True, True, True],
    )

    return metrics


def summarize_asset_stage(metrics):
    if metrics is None or metrics.empty:
        return pd.DataFrame()

    focus = metrics[metrics["horizon_days"].isin(FOCUS_HORIZONS)].copy()

    if focus.empty:
        focus = metrics.copy()

    rows = []

    for asset, d in focus.groupby("asset"):
        checked_values = pd.to_numeric(d["checked"], errors="coerce").fillna(0)

        max_checked = int(checked_values.max()) if len(checked_values) else 0
        min_checked = int(checked_values.min()) if len(checked_values) else 0

        if max_checked < MIN_OBSERVATION_CHECKS:
            general_stage = "RACCOLTA DATI"
        elif max_checked < MIN_LIGHT_SUGGESTION_CHECKS:
            general_stage = "OSSERVAZIONE 30+"
        elif max_checked < MIN_AUTO_WEIGHT_CHECKS:
            general_stage = "SUGGERIMENTO LEGGERO"
        else:
            general_stage = "PRONTO PER PESI"

        usable = int((pd.to_numeric(d["checked"], errors="coerce").fillna(0) >= MIN_AUTO_WEIGHT_CHECKS).sum())
        light = int((pd.to_numeric(d["checked"], errors="coerce").fillna(0) >= MIN_LIGHT_SUGGESTION_CHECKS).sum())

        rows.append({
            "Asset": asset,
            "Moduli monitorati": len(d),
            "Controlli max": max_checked,
            "Controlli min": min_checked,
            "Stato generale": general_stage,
            "Moduli con 60+": light,
            "Moduli con 100+": usable,
            "Lettura": stage_description(general_stage),
        })

    return pd.DataFrame(rows)


def build_focus_table(metrics):
    if metrics is None or metrics.empty:
        return pd.DataFrame()

    focus = metrics[metrics["horizon_days"].isin(FOCUS_HORIZONS)].copy()

    if focus.empty:
        focus = metrics.copy()

    rows = []

    for _, r in focus.iterrows():
        rows.append({
            "Asset": r["asset"],
            "Modulo": r["module"],
            "Orizzonte": f"{int(r['horizon_days'])}g",
            "Controlli": int(r["checked"]),
            "Accuracy": fmt_pct(r["direction_accuracy_pct"]),
            "Return medio": fmt_pct(r["avg_return_pct"]),
            "Drawdown medio": fmt_pct(r["avg_drawdown_pct"]),
            "Max gain medio": fmt_pct(r["avg_max_gain_pct"]),
            "Stato": r["calibration_stage"],
            "Delta peso": fmt_delta(r["suggested_weight_delta"]),
            "Suggerimento": r["suggestion"],
        })

    table = pd.DataFrame(rows)

    if table.empty:
        return table

    order = {"BTC": 0, "SOL": 1, "DOGE": 2}
    table["_asset_order"] = table["Asset"].map(order).fillna(9)
    table["_horizon_order"] = table["Orizzonte"].str.extract(r"([0-9]+)").astype(float)

    table = table.sort_values(["_asset_order", "_horizon_order", "Modulo"])
    table = table.drop(columns=["_asset_order", "_horizon_order"])

    return table


def build_current_score_table(current_scores):
    if current_scores is None or current_scores.empty:
        return pd.DataFrame()

    rows = []

    for _, r in current_scores.iterrows():
        module = r.get("module", "")
        score = safe_float(r.get("current_score", np.nan))

        if pd.isna(score):
            continue

        rows.append({
            "Asset": r.get("asset", ""),
            "Modulo": module,
            "Score attuale": fmt_delta(score),
        })

    out = pd.DataFrame(rows)

    if out.empty:
        return out

    order = {"BTC": 0, "SOL": 1, "DOGE": 2}
    out["_asset_order"] = out["Asset"].map(order).fillna(9)

    return out.sort_values(["_asset_order", "Modulo"]).drop(columns=["_asset_order"])


def render_report(metrics, source_name, current_scores):
    now = utc_now().strftime("%Y-%m-%d %H:%M UTC")

    lines = []

    lines.append("# Calibrazione pesi Global Confluence")
    lines.append("")
    lines.append(f"Generato: **{now}**")
    lines.append("")
    lines.append("Questo report prepara la calibrazione futura dei pesi del Global Confluence.")
    lines.append("")
    lines.append("Non modifica ancora i pesi dello scanner. Per ora legge l'accuratezza dei moduli e stabilisce quando ci saranno abbastanza dati per fidarsi.")
    lines.append("")
    lines.append("## Regola prudente")
    lines.append("")
    lines.append(f"- Sotto **{MIN_OBSERVATION_CHECKS}** controlli: solo raccolta dati.")
    lines.append(f"- Da **{MIN_OBSERVATION_CHECKS}** a **{MIN_LIGHT_SUGGESTION_CHECKS - 1}** controlli: osservazione iniziale, non applicare.")
    lines.append(f"- Da **{MIN_LIGHT_SUGGESTION_CHECKS}** a **{MIN_AUTO_WEIGHT_CHECKS - 1}** controlli: suggerimento leggero.")
    lines.append(f"- Da **{MIN_AUTO_WEIGHT_CHECKS}+** controlli: dati sufficienti per valutare una modifica prudente dei pesi.")
    lines.append("")

    if source_name:
        lines.append(f"Fonte dati letta: **{source_name}**")
    else:
        lines.append("Fonte dati letta: **nessuna fonte disponibile**")

    lines.append("")

    if metrics is None or metrics.empty:
        lines.append("## Stato")
        lines.append("")
        lines.append("_Nessun dato di accuratezza modulo disponibile._")
        lines.append("")
        lines.append("Il file si attiverà quando sarà presente un report di accuratezza moduli, per esempio `module_signal_accuracy_metrics.csv` oppure il blocco `MODULE_ACCURACY` nel `latest_report.md`.")
        lines.append("")
        return "\n".join(lines) + "\n"

    summary = summarize_asset_stage(metrics)

    lines.append("## Sintesi stato calibrazione pesi")
    lines.append("")
    lines.append(df_to_markdown(summary))
    lines.append("")

    focus_table = build_focus_table(metrics)

    lines.append("## Dettaglio moduli")
    lines.append("")
    lines.append(df_to_markdown(focus_table))
    lines.append("")

    if current_scores is not None and not current_scores.empty:
        lines.append("## Pesi / score attuali letti dal Global Confluence")
        lines.append("")
        lines.append("Questa tabella mostra gli score attuali. La calibrazione qui sotto non li modifica ancora.")
        lines.append("")
        lines.append(df_to_markdown(build_current_score_table(current_scores)))
        lines.append("")

    usable = metrics[pd.to_numeric(metrics["checked"], errors="coerce").fillna(0) >= MIN_AUTO_WEIGHT_CHECKS].copy()
    light = metrics[pd.to_numeric(metrics["checked"], errors="coerce").fillna(0) >= MIN_LIGHT_SUGGESTION_CHECKS].copy()

    lines.append("## Lettura operativa")
    lines.append("")

    if usable.empty and light.empty:
        lines.append("- Stato attuale: **RACCOLTA DATI**.")
        lines.append("- Nessun modulo ha ancora abbastanza controlli per suggerire modifiche ai pesi.")
        lines.append("- Il Global Confluence deve continuare a usare i pesi attuali.")
    elif usable.empty:
        lines.append("- Stato attuale: **SUGGERIMENTI LEGGERI POSSIBILI**, ma non ancora abbastanza forti per modificare automaticamente il Global.")
        lines.append("- I moduli con 60+ controlli possono essere osservati, ma non vanno ancora usati per cambiare in modo deciso i pesi.")
    else:
        lines.append("- Stato attuale: alcuni moduli hanno **100+ controlli**.")
        lines.append("- Da questo punto si può valutare una modifica prudente dei pesi, ma solo se il suggerimento è stabile anche a 30g e 60g.")

    lines.append("")
    lines.append("## Regola anti-autoinganno")
    lines.append("")
    lines.append("- Non aumentare il peso di un modulo solo perché ha funzionato per pochi giorni.")
    lines.append("- Non ridurre il peso di un modulo solo per una piccola serie negativa.")
    lines.append("- La modifica dei pesi deve partire solo quando ci sono abbastanza controlli e quando 30g e 60g non si contraddicono troppo.")
    lines.append("- Questo report serve a evitare che il modello si auto-saboti con pochi dati.")
    lines.append("")

    return "\n".join(lines) + "\n"


def render_latest_block(metrics):
    lines = []

    lines.append("# Calibrazione pesi Global Confluence")
    lines.append("")
    lines.append("Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)")
    lines.append("")
    lines.append("Questo blocco controlla se, col tempo, i moduli del Global Confluence meritano più peso, meno peso o peso invariato.")
    lines.append("")

    if metrics is None or metrics.empty:
        lines.append("_Dati ancora non disponibili._")
        lines.append("")
        return "\n".join(lines)

    summary = summarize_asset_stage(metrics)

    if summary.empty:
        lines.append("_Dati ancora insufficienti._")
        lines.append("")
        return "\n".join(lines)

    latest_rows = []

    for _, r in summary.iterrows():
        latest_rows.append({
            "Asset": r["Asset"],
            "Stato": r["Stato generale"],
            "Controlli max": r["Controlli max"],
            "Moduli 60+": r["Moduli con 60+"],
            "Moduli 100+": r["Moduli con 100+"],
            "Lettura": r["Lettura"],
        })

    lines.append(df_to_markdown(pd.DataFrame(latest_rows)))
    lines.append("")
    lines.append("Regola: sotto 60 controlli il report osserva soltanto; da 100+ controlli può suggerire modifiche prudenti ai pesi.")
    lines.append("")

    return "\n".join(lines)


def inject_into_latest_report(section_md):
    if not LATEST_REPORT.exists():
        return

    old = read_text(LATEST_REPORT)

    if not old:
        return

    clean = section_md.strip()
    new_section = START_MARKER + "\n" + clean + "\n" + END_MARKER

    if START_MARKER in old and END_MARKER in old:
        start = old.find(START_MARKER)
        end = old.find(END_MARKER)

        if start != -1 and end != -1 and end > start:
            end = end + len(END_MARKER)
            new = old[:start] + new_section + old[end:]
        else:
            new = old.rstrip() + "\n\n" + new_section + "\n"
    else:
        anchors = [
            "<!-- MODULE_ACCURACY_END -->",
            "<!-- CALIBRATION_READABLE_END -->",
            "<!-- GLOBAL_CONFLUENCE_END -->",
        ]

        inserted = False
        new = old

        for anchor in anchors:
            if anchor in old:
                idx = old.find(anchor) + len(anchor)
                new = old[:idx] + "\n\n" + new_section + old[idx:]
                inserted = True
                break

        if not inserted:
            new = old.rstrip() + "\n\n" + new_section + "\n"

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    module_accuracy, source_name = load_module_accuracy()
    metrics = build_weight_calibration_metrics(module_accuracy)
    current_scores = load_current_global_scores()

    if metrics is not None and not metrics.empty:
        metrics.to_csv(OUTPUT_METRICS, index=False)
    else:
        pd.DataFrame(columns=[
            "asset",
            "module",
            "horizon_days",
            "checked",
            "direction_accuracy_pct",
            "avg_return_pct",
            "avg_drawdown_pct",
            "avg_max_gain_pct",
            "calibration_stage",
            "reliability",
            "suggested_weight_delta",
            "suggestion",
            "can_apply_to_global",
            "note",
        ]).to_csv(OUTPUT_METRICS, index=False)

    report_md = render_report(metrics, source_name, current_scores)
    OUTPUT_REPORT.write_text(report_md, encoding="utf-8")

    latest_block = render_latest_block(metrics)
    inject_into_latest_report(latest_block)

    print(f"Creato {OUTPUT_REPORT}")
    print(f"Creato {OUTPUT_METRICS}")

    if source_name:
        print(f"Fonte dati calibrazione pesi: {source_name}")
    else:
        print("Nessuna fonte dati disponibile per calibrazione pesi.")


if __name__ == "__main__":
    main()
