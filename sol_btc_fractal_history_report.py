import os
import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pandas as pd


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"

HISTORY_CSV_PATH = "reports/sol_btc_fractal_history.csv"
HISTORY_MD_PATH = "reports/sol_btc_fractal_history.md"

START_MARKER = "<!-- SOL_BTC_FRACTAL_HISTORY_START -->"
END_MARKER = "<!-- SOL_BTC_FRACTAL_HISTORY_END -->"

BTC_SOL_START = "<!-- BTC_SOL_FRACTAL_START -->"
BTC_SOL_END = "<!-- BTC_SOL_FRACTAL_END -->"

PATH_TRACKER_START = "<!-- FRACTAL_PATH_TRACKER_START -->"
PATH_TRACKER_END = "<!-- FRACTAL_PATH_TRACKER_END -->"

COLUMNS = [
    "forecast_date",
    "generated_at_utc",

    "sol_last_candle",
    "sol_price",
    "btc_scaled_today",
    "gap_pct",
    "sol_day_from_bottom",
    "btc_equiv_date",

    "verdict",
    "phase",
    "total_similarity_pct",
    "reliability",
    "phase_risk",
    "trend_tracking",

    "program_start_date",

    "pre_period_dates",
    "pre_days",
    "pre_price_adherence_pct",
    "pre_avg_error_pct",
    "pre_last_error_pct",
    "pre_status",

    "live_period_dates",
    "live_days",
    "live_price_adherence_pct",
    "live_avg_error_pct",
    "live_last_error_pct",
    "live_status",

    "total_period_dates",
    "total_days",
    "total_price_adherence_pct",
    "total_avg_error_pct",
    "total_last_error_pct",
    "total_status",

    "tracker_days_from_bottom",
    "tracker_days_from_program",
    "tracker_avg_error_from_bottom_pct",
    "tracker_avg_error_last_7d_pct",
    "tracker_avg_error_from_program_pct",
    "tracker_last_error_pct",
    "tracker_status",

    "first_confirmation",
    "second_confirmation",
    "soft_invalidation",
    "hard_invalidation",

    "target_cycle_base_from_bottom",
    "target_cycle_base_from_today",
    "max_path_base",
    "max_path_beta",

    "next_step_text",

    "proj_7d_date",
    "proj_7d_base",
    "proj_7d_min",
    "proj_7d_max",

    "proj_14d_date",
    "proj_14d_base",
    "proj_14d_min",
    "proj_14d_max",

    "proj_30d_date",
    "proj_30d_base",
    "proj_30d_min",
    "proj_30d_max",

    "proj_60d_date",
    "proj_60d_base",
    "proj_60d_min",
    "proj_60d_max",

    "proj_90d_date",
    "proj_90d_base",
    "proj_90d_min",
    "proj_90d_max",

    "proj_120d_date",
    "proj_120d_base",
    "proj_120d_min",
    "proj_120d_max",
]


def clean_text(value):
    if value is None:
        return ""
    value = str(value)
    value = value.replace("**", "")
    value = value.replace("\xa0", " ")
    value = value.strip()
    return value


def parse_number(value):
    if value is None:
        return None

    text = clean_text(value)
    text = text.replace("$", "")
    text = text.replace("%", "")
    text = text.replace("€", "")
    text = text.replace("+", "")
    text = text.replace(" ", "")
    text = re.sub(r"[^0-9,\.\-]", "", text)

    if text in ["", "-", ".", ","]:
        return None

    # Formato italiano: 1.234,56 -> 1234.56
    if "," in text:
        text = text.replace(".", "")
        text = text.replace(",", ".")
    else:
        # Se ci sono più punti, li tratto come separatori migliaia.
        if text.count(".") > 1:
            text = text.replace(".", "")

    try:
        return float(text)
    except Exception:
        return None


def fmt_number(value, decimals=2):
    try:
        if value is None or pd.isna(value):
            return "n/a"
        value = float(value)
    except Exception:
        return "n/a"

    formatted = f"{value:,.{decimals}f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_price(value, decimals=2):
    try:
        if value is None or pd.isna(value):
            return "n/a"
        value = float(value)
    except Exception:
        return "n/a"

    return f"{fmt_number(value, decimals)} $"


def fmt_pct(value, decimals=2, force_sign=True):
    try:
        if value is None or pd.isna(value):
            return "n/a"
        value = float(value)
    except Exception:
        return "n/a"

    sign = "+" if force_sign and value > 0 else ""
    return f"{sign}{fmt_number(value, decimals)}%"


def md_table(headers, rows):
    def cell(value):
        value = "" if value is None else str(value)
        return value.replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(cell(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(cell(v) for v in row) + " |")

    return "\n".join(lines)


def section_between(text, start_marker, end_marker=None):
    start = text.find(start_marker)
    if start == -1:
        return ""

    start += len(start_marker)

    if end_marker is None:
        return text[start:]

    end = text.find(end_marker, start)
    if end == -1:
        return text[start:]

    return text[start:end]


def extract_generated_info(text):
    generated_at_utc = None
    forecast_date = None

    candidates = [
        r"Generato:\s*(\d{4}-\d{2}-\d{2})\s+([0-9:]+)\s+UTC",
        r"Generated:\s*(\d{4}-\d{2}-\d{2})\s+([0-9:]+)\s+UTC",
        r"Aggiornato il:\s*\*\*(\d{4}-\d{2}-\d{2})\s+([0-9:]+)\s+UTC\*\*",
    ]

    for pattern in candidates:
        m = re.search(pattern, text)
        if m:
            forecast_date = m.group(1)
            generated_at_utc = f"{m.group(1)} {m.group(2)} UTC"
            break

    if forecast_date is None:
        forecast_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if generated_at_utc is None:
        generated_at_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    return forecast_date, generated_at_utc


def extract_bold_field(block, label):
    pattern = rf"\*\*{re.escape(label)}:\*\*\s*(.+)"
    m = re.search(pattern, block)
    if not m:
        return None

    value = m.group(1).strip()
    value = value.replace("- ", "").strip()
    value = value.replace("**", "").strip()
    return value


def extract_bullet_bold_field(block, label):
    pattern = rf"-\s*\*\*{re.escape(label)}:\*\*\s*(.+)"
    m = re.search(pattern, block)
    if not m:
        return None

    value = m.group(1).strip()
    value = value.replace("**", "").strip()
    return value


def extract_table_value(block, key):
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue

        parts = [p.strip() for p in line.strip("|").split("|")]

        if len(parts) >= 2 and parts[0].lower() == key.lower():
            return parts[1]

    return None


def extract_level_value(block, key):
    return parse_number(extract_table_value(block, key))


def parse_alignment_table(fractal_block):
    result = {}

    for line in fractal_block.splitlines():
        line = line.strip()

        if not line.startswith("|"):
            continue

        parts = [p.strip() for p in line.strip("|").split("|")]

        if len(parts) < 7:
            continue

        period = parts[0]

        if period == "Prima del programma":
            prefix = "pre"
        elif period == "Da inizio programma":
            prefix = "live"
        elif period == "Totale dal bottom":
            prefix = "total"
        else:
            continue

        result[f"{prefix}_period_dates"] = parts[1]
        result[f"{prefix}_days"] = parse_number(parts[2])
        result[f"{prefix}_price_adherence_pct"] = parse_number(parts[3])
        result[f"{prefix}_avg_error_pct"] = parse_number(parts[4])
        result[f"{prefix}_last_error_pct"] = parse_number(parts[5])
        result[f"{prefix}_status"] = parts[6]

    return result


def parse_projection_table(fractal_block):
    projections = {}

    horizon_map = {
        "7 giorni": "7d",
        "14 giorni": "14d",
        "30 giorni": "30d",
        "60 giorni": "60d",
        "90 giorni": "90d",
        "120 giorni": "120d",
    }

    for line in fractal_block.splitlines():
        line = line.strip()

        if not line.startswith("|"):
            continue

        parts = [p.strip() for p in line.strip("|").split("|")]

        if len(parts) < 6:
            continue

        horizon = parts[0]

        if horizon not in horizon_map:
            continue

        key = horizon_map[horizon]

        # Tabella breve:
        # | Orizzonte | Data SOL prevista | BTC fece | SOL base | Min percorso | Max percorso |
        projections[f"proj_{key}_date"] = parts[1]
        projections[f"proj_{key}_base"] = parse_number(parts[3])
        projections[f"proj_{key}_min"] = parse_number(parts[4])
        projections[f"proj_{key}_max"] = parse_number(parts[5])

    return projections


def parse_last_tracker_row(path_block):
    last = {}

    rows = []

    for line in path_block.splitlines():
        line = line.strip()

        if not line.startswith("|"):
            continue

        parts = [p.strip() for p in line.strip("|").split("|")]

        if len(parts) < 7:
            continue

        day = parse_number(parts[0])
        if day is None:
            continue

        # | Giorno | Data SOL | Data BTC eq. | SOL reale | BTC scalato | Errore | Fase |
        rows.append(parts)

    if not rows:
        return last

    parts = rows[-1]

    last["sol_day_from_bottom"] = parse_number(parts[0])
    last["forecast_date_from_table"] = parts[1]
    last["btc_equiv_date"] = parts[2]
    last["sol_price"] = parse_number(parts[3])
    last["btc_scaled_today"] = parse_number(parts[4])
    last["gap_pct"] = parse_number(parts[5])

    return last


def parse_tracker_summary(path_block):
    result = {}

    field_map = {
        "Bottom SOL usato": "sol_bottom_date",
        "Bottom BTC 2022 equivalente": "btc_bottom_date",
        "Inizio programma/scanner rilevato": "program_start_date",
        "Prezzo iniziale SOL": "sol_price",
        "Verdetto": "verdict",
        "Somiglianza": "total_similarity_pct",
        "Tracking": "trend_tracking",
        "Fase": "phase",
        "Rischio fase": "phase_risk",
        "Giorni controllati dal bottom": "tracker_days_from_bottom",
        "Giorni controllati da inizio programma/scanner": "tracker_days_from_program",
        "Errore medio assoluto dal bottom": "tracker_avg_error_from_bottom_pct",
        "Errore medio assoluto ultimi 7 giorni": "tracker_avg_error_last_7d_pct",
        "Errore medio assoluto da inizio programma/scanner": "tracker_avg_error_from_program_pct",
        "Errore ultimo giorno": "tracker_last_error_pct",
        "Stato": "tracker_status",
    }

    for label, key in field_map.items():
        value = extract_bullet_bold_field(path_block, label)

        if value is None:
            continue

        if key.endswith("_pct") or key.startswith("tracker_days") or key == "sol_price":
            result[key] = parse_number(value)
        else:
            result[key] = clean_text(value)

    return result


def parse_fractal_report(latest_report):
    forecast_date, generated_at_utc = extract_generated_info(latest_report)

    fractal_block = section_between(latest_report, BTC_SOL_START, BTC_SOL_END)
    path_block = section_between(latest_report, PATH_TRACKER_START, PATH_TRACKER_END)

    if not fractal_block:
        return None

    row = {col: None for col in COLUMNS}
    row["forecast_date"] = forecast_date
    row["generated_at_utc"] = generated_at_utc

    row["sol_last_candle"] = extract_bullet_bold_field(fractal_block, "Ultima candela SOL usata")
    row["verdict"] = extract_bold_field(fractal_block, "Verdetto")
    row["phase"] = extract_bullet_bold_field(fractal_block, "Fase attuale")
    row["total_similarity_pct"] = parse_number(extract_bullet_bold_field(fractal_block, "Somiglianza totale"))
    row["reliability"] = extract_bullet_bold_field(fractal_block, "Affidabilita")
    row["phase_risk"] = extract_bullet_bold_field(fractal_block, "Rischio fase")
    row["trend_tracking"] = extract_bullet_bold_field(fractal_block, "Trend tracking")
    row["sol_day_from_bottom"] = parse_number(extract_bullet_bold_field(fractal_block, "SOL e al giorno"))
    row["btc_equiv_date"] = extract_bullet_bold_field(fractal_block, "Giorno BTC equivalente")
    row["next_step_text"] = extract_bullet_bold_field(fractal_block, "Prossimo step")

    program_start = re.search(r"\*\*Inizio programma/scanner:\*\*\s*(.+)", fractal_block)
    if program_start:
        row["program_start_date"] = clean_text(program_start.group(1))

    alignment = parse_alignment_table(fractal_block)
    row.update(alignment)

    row["first_confirmation"] = extract_level_value(fractal_block, "Prima conferma")
    row["second_confirmation"] = extract_level_value(fractal_block, "Seconda conferma")
    row["soft_invalidation"] = extract_level_value(fractal_block, "Invalidazione soft")
    row["hard_invalidation"] = extract_level_value(fractal_block, "Invalidazione forte")

    row["target_cycle_base_from_bottom"] = extract_level_value(fractal_block, "Target ciclo base dal bottom")
    row["target_cycle_base_from_today"] = extract_level_value(fractal_block, "Target ciclo base da oggi")

    max_base = extract_table_value(fractal_block, "Massimo percorso base")
    max_beta = extract_table_value(fractal_block, "Massimo percorso beta")

    row["max_path_base"] = parse_number(max_base)
    row["max_path_beta"] = parse_number(max_beta)

    projections = parse_projection_table(fractal_block)
    row.update(projections)

    if path_block:
        tracker = parse_tracker_summary(path_block)
        row.update({k: v for k, v in tracker.items() if k in row})

        last_tracker = parse_last_tracker_row(path_block)

        for key in ["sol_price", "btc_scaled_today", "gap_pct", "sol_day_from_bottom", "btc_equiv_date"]:
            if last_tracker.get(key) is not None:
                row[key] = last_tracker.get(key)

        if last_tracker.get("forecast_date_from_table"):
            row["forecast_date"] = last_tracker["forecast_date_from_table"]

    if row["sol_price"] is None:
        row["sol_price"] = parse_number(extract_table_value(fractal_block, "Prezzo SOL attuale"))

    if row["total_similarity_pct"] is None:
        row["total_similarity_pct"] = parse_number(row.get("total_price_adherence_pct"))

    return row


def load_history():
    if os.path.exists(HISTORY_CSV_PATH):
        try:
            df = pd.read_csv(HISTORY_CSV_PATH)
        except Exception:
            df = pd.DataFrame(columns=COLUMNS)
    else:
        df = pd.DataFrame(columns=COLUMNS)

    for col in COLUMNS:
        if col not in df.columns:
            df[col] = None

    return df[COLUMNS]


def update_history(row):
    df = load_history()

    if row is None:
        return df

    new_df = pd.DataFrame([row])

    for col in COLUMNS:
        if col not in new_df.columns:
            new_df[col] = None

    new_df = new_df[COLUMNS]

    forecast_date = str(row.get("forecast_date"))

    # Tiene una sola riga per giorno: se rilanci il workflow, aggiorna quella del giorno.
    df = df[df["forecast_date"].astype(str) != forecast_date]

    df = pd.concat([df, new_df], ignore_index=True)

    df["forecast_date_dt"] = pd.to_datetime(df["forecast_date"], errors="coerce")
    df = df.sort_values("forecast_date_dt")
    df = df.drop(columns=["forecast_date_dt"])

    df = df[COLUMNS]
    df.to_csv(HISTORY_CSV_PATH, index=False)

    return df


def latest_row(df):
    if df.empty:
        return None

    work = df.copy()
    work["forecast_date_dt"] = pd.to_datetime(work["forecast_date"], errors="coerce")
    work = work.dropna(subset=["forecast_date_dt"])

    if work.empty:
        return None

    work = work.sort_values("forecast_date_dt")
    return work.iloc[-1]


def build_latest_summary_table(row):
    if row is None:
        return "Nessun dato salvato."

    return md_table(
        ["Voce", "Valore"],
        [
            ["Data", row.get("forecast_date", "n/a")],
            ["Prezzo SOL", fmt_price(row.get("sol_price"))],
            ["BTC scalato", fmt_price(row.get("btc_scaled_today"))],
            ["Gap SOL vs BTC-scalato", fmt_pct(row.get("gap_pct"))],
            ["Somiglianza totale", fmt_pct(row.get("total_similarity_pct"))],
            ["Fase", row.get("phase", "n/a")],
            ["Tracking", row.get("trend_tracking", "n/a")],
            ["Errore medio da inizio programma", fmt_pct(row.get("live_avg_error_pct"))],
            ["Errore ultimo giorno", fmt_pct(row.get("tracker_last_error_pct"))],
            ["Conferma 1", fmt_price(row.get("first_confirmation"))],
            ["Conferma 2", fmt_price(row.get("second_confirmation"))],
            ["Invalidazione soft", fmt_price(row.get("soft_invalidation"))],
            ["Invalidazione forte", fmt_price(row.get("hard_invalidation"))],
            ["Target ciclo base da oggi", fmt_price(row.get("target_cycle_base_from_today"))],
        ],
    )


def build_history_rows(df):
    rows = []

    work = df.copy()
    work["forecast_date_dt"] = pd.to_datetime(work["forecast_date"], errors="coerce")
    work = work.sort_values("forecast_date_dt")

    for _, r in work.iterrows():
        rows.append(
            [
                r.get("forecast_date", "n/a"),
                fmt_price(r.get("sol_price")),
                fmt_price(r.get("btc_scaled_today")),
                fmt_pct(r.get("gap_pct")),
                fmt_pct(r.get("total_similarity_pct")),
                r.get("phase", "n/a"),
                r.get("trend_tracking", "n/a"),
                fmt_pct(r.get("live_avg_error_pct")),
                fmt_pct(r.get("tracker_last_error_pct")),
                fmt_price(r.get("proj_30d_base")),
                fmt_price(r.get("proj_60d_base")),
                fmt_price(r.get("soft_invalidation")),
                fmt_price(r.get("first_confirmation")),
                fmt_price(r.get("target_cycle_base_from_today")),
            ]
        )

    return rows


def build_alignment_history_rows(df):
    rows = []

    work = df.copy()
    work["forecast_date_dt"] = pd.to_datetime(work["forecast_date"], errors="coerce")
    work = work.sort_values("forecast_date_dt")

    for _, r in work.iterrows():
        rows.append(
            [
                r.get("forecast_date", "n/a"),
                fmt_pct(r.get("pre_price_adherence_pct")),
                fmt_pct(r.get("pre_avg_error_pct")),
                r.get("pre_status", "n/a"),
                fmt_pct(r.get("live_price_adherence_pct")),
                fmt_pct(r.get("live_avg_error_pct")),
                r.get("live_status", "n/a"),
                fmt_pct(r.get("total_price_adherence_pct")),
                fmt_pct(r.get("total_avg_error_pct")),
                r.get("total_status", "n/a"),
            ]
        )

    return rows


def build_projection_history_rows(df):
    rows = []

    work = df.copy()
    work["forecast_date_dt"] = pd.to_datetime(work["forecast_date"], errors="coerce")
    work = work.sort_values("forecast_date_dt")

    for _, r in work.iterrows():
        rows.append(
            [
                r.get("forecast_date", "n/a"),
                fmt_price(r.get("proj_7d_base")),
                fmt_price(r.get("proj_14d_base")),
                fmt_price(r.get("proj_30d_base")),
                fmt_price(r.get("proj_60d_base")),
                fmt_price(r.get("proj_90d_base")),
                fmt_price(r.get("proj_120d_base")),
                fmt_price(r.get("proj_30d_min")),
                fmt_price(r.get("proj_30d_max")),
                fmt_price(r.get("target_cycle_base_from_today")),
            ]
        )

    return rows


def build_markdown_report(df):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    latest = latest_row(df)

    first_date = "n/a"
    last_date = "n/a"

    if not df.empty:
        dates = pd.to_datetime(df["forecast_date"], errors="coerce").dropna()
        if not dates.empty:
            first_date = dates.min().strftime("%Y-%m-%d")
            last_date = dates.max().strftime("%Y-%m-%d")

    lines = []

    lines.append("# Storico frattale SOL/BTC")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{utc_now}**")
    lines.append("")
    lines.append("Questo file salva giorno per giorno la lettura del frattale **BTC novembre 2022 vs SOL giugno 2026**.")
    lines.append("")
    lines.append("Serve per vedere se SOL sta seguendo il percorso BTC-scalato, se si sta avvicinando, se si sta staccando sopra, oppure se sta perdendo aderenza.")
    lines.append("")
    lines.append("Il CSV completo è: `sol_btc_fractal_history.csv`.")
    lines.append("")
    lines.append("## Stato archivio")
    lines.append("")
    lines.append(
        md_table(
            ["Voce", "Valore"],
            [
                ["Prima rilevazione salvata", first_date],
                ["Ultima rilevazione salvata", last_date],
                ["Righe salvate", len(df)],
            ],
        )
    )
    lines.append("")
    lines.append("## Ultima lettura")
    lines.append("")
    lines.append(build_latest_summary_table(latest))
    lines.append("")
    lines.append("## Storico compatto giorno per giorno")
    lines.append("")
    lines.append(
        md_table(
            [
                "Data",
                "SOL",
                "BTC scalato",
                "Gap",
                "Somiglianza",
                "Fase",
                "Tracking",
                "Errore live medio",
                "Errore ultimo",
                "Base 30g",
                "Base 60g",
                "Soft invalid.",
                "Conferma 1",
                "Target ciclo oggi",
            ],
            build_history_rows(df),
        )
        if not df.empty
        else "Nessun dato salvato."
    )
    lines.append("")
    lines.append("## Aderenza prima e dopo inizio programma")
    lines.append("")
    lines.append(
        md_table(
            [
                "Data",
                "Aderenza pre",
                "Errore pre",
                "Stato pre",
                "Aderenza live",
                "Errore live",
                "Stato live",
                "Aderenza totale",
                "Errore totale",
                "Stato totale",
            ],
            build_alignment_history_rows(df),
        )
        if not df.empty
        else "Nessun dato salvato."
    )
    lines.append("")
    lines.append("## Storico proiezioni frattali")
    lines.append("")
    lines.append(
        md_table(
            [
                "Data",
                "Base 7g",
                "Base 14g",
                "Base 30g",
                "Base 60g",
                "Base 90g",
                "Base 120g",
                "Min 30g",
                "Max 30g",
                "Target ciclo oggi",
            ],
            build_projection_history_rows(df),
        )
        if not df.empty
        else "Nessun dato salvato."
    )
    lines.append("")
    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- **Gap**: quanto SOL è sopra o sotto la linea BTC-scalata.")
    lines.append("- **Gap 0-5%**: frattale molto pulito.")
    lines.append("- **Gap 5-10%**: frattale buono.")
    lines.append("- **Gap 10-15%**: ancora accettabile, ma SOL è in anticipo.")
    lines.append("- **Gap 15-25%**: frattale valido, ma meno preciso per prevedere ritracciamenti e date.")
    lines.append("- **Gap oltre 25%**: SOL troppo accelerata rispetto al frattale.")
    lines.append("- **Errore live medio**: la parte più importante, perché misura da quando abbiamo iniziato a monitorarlo davvero.")
    lines.append("- **Base 30g / 60g**: dove dovrebbe andare SOL se segue il percorso BTC equivalente.")
    lines.append("- **Soft invalidation**: primo livello dove il frattale si sporca.")
    lines.append("- **Invalidazione forte**: sotto il bottom SOL usato, il frattale è quasi rotto.")
    lines.append("")
    lines.append("Nota: se il workflow gira più volte nello stesso giorno, viene tenuta solo l'ultima lettura del giorno.")
    lines.append("")

    return "\n".join(lines)


def build_main_report_block(df):
    latest = latest_row(df)

    if latest is None:
        latest_line = "Nessuna lettura salvata."
    else:
        latest_line = (
            f"Ultima lettura salvata: **{latest.get('forecast_date', 'n/a')}** — "
            f"SOL {fmt_price(latest.get('sol_price'))}, "
            f"gap {fmt_pct(latest.get('gap_pct'))}, "
            f"somiglianza {fmt_pct(latest.get('total_similarity_pct'))}."
        )

    return "\n".join(
        [
            START_MARKER,
            "",
            "---",
            "",
            "# Storico frattale SOL/BTC",
            "",
            "Per vedere la tabella giorno per giorno devi aprire/cliccare questo file:",
            "",
            "**[sol_btc_fractal_history.md](sol_btc_fractal_history.md)**",
            "",
            latest_line,
            "",
            "Nel report principale lascio solo il link, così non diventa troppo lungo.",
            "",
            END_MARKER,
        ]
    )


def inject_into_main_report(df):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # Rimuove il vecchio blocco se già presente.
    if START_MARKER in text and END_MARKER in text:
        before = text.split(START_MARKER)[0].rstrip()
        after = text.split(END_MARKER, 1)[1].lstrip()
        text = before + "\n\n" + after

    block = build_main_report_block(df).strip()

    # Lo metto dopo il Fractal Path Tracker, così resta vicino al frattale SOL/BTC.
    insert_after = PATH_TRACKER_END

    if insert_after in text:
        pos = text.find(insert_after) + len(insert_after)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    elif BTC_SOL_END in text:
        pos = text.find(BTC_SOL_END) + len(BTC_SOL_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    else:
        new_text = text.rstrip() + "\n\n" + block + "\n"

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    if not os.path.exists(MAIN_REPORT_PATH):
        with open(HISTORY_MD_PATH, "w", encoding="utf-8") as f:
            f.write("# Storico frattale SOL/BTC\n\n`latest_report.md` non trovato.\n")
        print("latest_report.md not found.")
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        latest_report = f.read()

    row = parse_fractal_report(latest_report)

    if row is None:
        with open(HISTORY_MD_PATH, "w", encoding="utf-8") as f:
            f.write("# Storico frattale SOL/BTC\n\nBlocco frattale SOL/BTC non trovato nel report principale.\n")
        print("SOL/BTC fractal block not found.")
        return

    df = update_history(row)

    markdown = build_markdown_report(df)

    with open(HISTORY_MD_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)

    inject_into_main_report(df)

    print(f"Wrote {HISTORY_CSV_PATH}")
    print(f"Wrote {HISTORY_MD_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
