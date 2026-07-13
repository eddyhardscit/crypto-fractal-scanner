import os
import re
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"

HISTORY_CSV_PATH = "reports/forecast_30d_history.csv"
HISTORY_MD_PATH = "reports/forecast_30d_history.md"

START_MARKER = "<!-- FORECAST_30D_HISTORY_START -->"
END_MARKER = "<!-- FORECAST_30D_HISTORY_END -->"

ASSETS = [
    ("BTC", "Bitcoin"),
    ("SOL", "Solana"),
    ("DOGE", "Dogecoin"),
]


COLUMNS = [
    "forecast_date",
    "target_date_30d",
    "generated_at_utc",
    "asset",
    "asset_name",
    "current_price",
    "direction",
    "positive_rate",
    "negative_rate",
    "signal_strength",
    "return_p10_price",
    "return_p10_pct",
    "return_p25_price",
    "return_p25_pct",
    "return_p50_price",
    "return_p50_pct",
    "return_p75_price",
    "return_p75_pct",
    "return_p90_price",
    "return_p90_pct",
    "drawdown_p10_price",
    "drawdown_p10_pct",
    "drawdown_p25_price",
    "drawdown_p25_pct",
    "drawdown_p50_price",
    "drawdown_p50_pct",
    "drawdown_p75_price",
    "drawdown_p75_pct",
    "drawdown_p90_price",
    "drawdown_p90_pct",
    "max_gain_p10_price",
    "max_gain_p10_pct",
    "max_gain_p25_price",
    "max_gain_p25_pct",
    "max_gain_p50_price",
    "max_gain_p50_pct",
    "max_gain_p75_price",
    "max_gain_p75_pct",
    "max_gain_p90_price",
    "max_gain_p90_pct",
]


def clean_text(value):
    if value is None:
        return ""
    value = str(value)
    value = value.replace("**", "")
    value = value.replace("$", "")
    value = value.replace("%", "")
    value = value.replace("€", "")
    value = value.replace("\xa0", " ")
    return value.strip()


def parse_number(value):
    if value is None:
        return None

    text = clean_text(value)
    text = text.replace(" ", "")
    text = re.sub(r"[^0-9,\.\-+]", "", text)

    if text in ["", "-", "+", ".", ","]:
        return None

    # Formato italiano: 61.846,43 -> 61846.43
    if "," in text:
        text = text.replace(".", "")
        text = text.replace(",", ".")
    else:
        # Formato americano o numero già pulito.
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


def fmt_price(value, asset=None):
    try:
        if value is None or pd.isna(value):
            return "n/a"
        value = float(value)
    except Exception:
        return "n/a"

    if asset == "BTC":
        return f"{fmt_number(value, 0)} $"
    if asset == "DOGE":
        return f"{fmt_number(value, 5)} $"
    return f"{fmt_number(value, 2)} $"


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
    def clean_cell(value):
        value = "" if value is None else str(value)
        return value.replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean_cell(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean_cell(c) for c in row) + " |")

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

    m = re.search(r"Aggiornato il:\s*\*\*([0-9\-: ]+UTC)\*\*", text)
    if m:
        generated_at_utc = m.group(1).strip()
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", generated_at_utc)
        if date_match:
            forecast_date = date_match.group(1)

    if forecast_date is None:
        m = re.search(r"Generato:\s*(\d{4}-\d{2}-\d{2})\s+[0-9:]+\s+UTC", text)
        if m:
            forecast_date = m.group(1)
            generated_at_utc = m.group(0).replace("Generato:", "").strip()

    if forecast_date is None:
        forecast_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if generated_at_utc is None:
        generated_at_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    try:
        target_date_30d = (pd.to_datetime(forecast_date) + pd.Timedelta(days=30)).strftime("%Y-%m-%d")
    except Exception:
        target_date_30d = None

    return forecast_date, target_date_30d, generated_at_utc


def get_asset_section(map_section, asset_name):
    heading = f"# {asset_name} — mappa semplice"
    start = map_section.find(heading)

    if start == -1:
        return ""

    next_starts = []

    for _, other_name in ASSETS:
        other_heading = f"# {other_name} — mappa semplice"
        pos = map_section.find(other_heading, start + 1)
        if pos != -1:
            next_starts.append(pos)

    end = min(next_starts) if next_starts else len(map_section)
    return map_section[start:end]


def extract_bold_value(section, label_regex):
    """Legge sia il vecchio sia il nuovo formato Markdown delle etichette."""
    patterns = [
        rf"(?im)^\s*[-*]?\s*\*\*{label_regex}:\*\*\s*\*\*(.*?)\*\*\s*$",
        rf"(?im)^\s*[-*]?\s*\*\*{label_regex}:\*\*\s*([^\n]+?)\s*$",
        rf"(?im)^\s*[-*]?\s*\*\*{label_regex}\*\*\s*:\s*\*\*(.*?)\*\*\s*$",
        rf"(?im)^\s*[-*]?\s*\*\*{label_regex}\*\*\s*:\s*([^\n]+?)\s*$",
        rf"(?im)^\s*[-*]?\s*{label_regex}:\s*\*\*(.*?)\*\*\s*$",
        rf"(?im)^\s*[-*]?\s*{label_regex}:\s*([^\n]+?)\s*$",
    ]

    for pattern in patterns:
        match = re.search(pattern, section, flags=re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return None

def extract_price_pct(block, label):
    pattern = rf"{re.escape(label)}:\s*\*\*(.*?)\*\*\s*\(([-+0-9\.,]+)%\)"
    m = re.search(pattern, block, flags=re.IGNORECASE)
    if not m:
        return None, None

    price = parse_number(m.group(1))
    pct = parse_number(m.group(2))
    return price, pct


def parse_asset_prediction(map_section, asset, asset_name, forecast_date, target_date_30d, generated_at_utc):
    section = get_asset_section(map_section, asset_name)

    if not section:
        return None

    direction = extract_bold_value(section, r"Direzione più probabile a 30 giorni")
    current_price = extract_bold_value(section, r"Prezzo attuale")
    positive_rate = extract_bold_value(section, r"Probabilità storica di salita")
    negative_rate = extract_bold_value(section, r"Probabilità storica di discesa")
    signal_strength = extract_bold_value(section, r"Quanto è netto il segnale")

    return_block = section_between(section, "## 1. Return 30d", "## 2. Drawdown 30d")
    drawdown_block = section_between(section, "## 2. Drawdown 30d", "## 3. Max gain 30d")
    max_gain_block = section_between(section, "## 3. Max gain 30d", "## Lettura pratica finale")

    return_p10_price, return_p10_pct = extract_price_pct(return_block, "Se va molto male")
    return_p25_price, return_p25_pct = extract_price_pct(return_block, "Se va male")
    return_p50_price, return_p50_pct = extract_price_pct(return_block, "Scenario normale")
    return_p75_price, return_p75_pct = extract_price_pct(return_block, "Se va bene")
    return_p90_price, return_p90_pct = extract_price_pct(return_block, "Se va molto bene")

    drawdown_p50_price, drawdown_p50_pct = extract_price_pct(drawdown_block, "Discesa normale")
    drawdown_p25_price, drawdown_p25_pct = extract_price_pct(drawdown_block, "Discesa brutta")
    drawdown_p10_price, drawdown_p10_pct = extract_price_pct(drawdown_block, "Discesa molto brutta")

    # Se in futuro aggiungiamo p75/p90 drawdown nel testo, il codice li leggerà.
    drawdown_p75_price, drawdown_p75_pct = extract_price_pct(drawdown_block, "Discesa contenuta")
    drawdown_p90_price, drawdown_p90_pct = extract_price_pct(drawdown_block, "Discesa molto contenuta")

    max_gain_p50_price, max_gain_p50_pct = extract_price_pct(max_gain_block, "Rialzo normale")
    max_gain_p75_price, max_gain_p75_pct = extract_price_pct(max_gain_block, "Rialzo buono")
    max_gain_p90_price, max_gain_p90_pct = extract_price_pct(max_gain_block, "Rialzo molto forte")

    # Se in futuro aggiungiamo p10/p25 max gain nel testo, il codice li leggerà.
    max_gain_p10_price, max_gain_p10_pct = extract_price_pct(max_gain_block, "Rialzo scarso")
    max_gain_p25_price, max_gain_p25_pct = extract_price_pct(max_gain_block, "Rialzo modesto")

    row = {
        "forecast_date": forecast_date,
        "target_date_30d": target_date_30d,
        "generated_at_utc": generated_at_utc,
        "asset": asset,
        "asset_name": asset_name,
        "current_price": parse_number(current_price),
        "direction": clean_text(direction),
        "positive_rate": parse_number(positive_rate),
        "negative_rate": parse_number(negative_rate),
        "signal_strength": clean_text(signal_strength),
        "return_p10_price": return_p10_price,
        "return_p10_pct": return_p10_pct,
        "return_p25_price": return_p25_price,
        "return_p25_pct": return_p25_pct,
        "return_p50_price": return_p50_price,
        "return_p50_pct": return_p50_pct,
        "return_p75_price": return_p75_price,
        "return_p75_pct": return_p75_pct,
        "return_p90_price": return_p90_price,
        "return_p90_pct": return_p90_pct,
        "drawdown_p10_price": drawdown_p10_price,
        "drawdown_p10_pct": drawdown_p10_pct,
        "drawdown_p25_price": drawdown_p25_price,
        "drawdown_p25_pct": drawdown_p25_pct,
        "drawdown_p50_price": drawdown_p50_price,
        "drawdown_p50_pct": drawdown_p50_pct,
        "drawdown_p75_price": drawdown_p75_price,
        "drawdown_p75_pct": drawdown_p75_pct,
        "drawdown_p90_price": drawdown_p90_price,
        "drawdown_p90_pct": drawdown_p90_pct,
        "max_gain_p10_price": max_gain_p10_price,
        "max_gain_p10_pct": max_gain_p10_pct,
        "max_gain_p25_price": max_gain_p25_price,
        "max_gain_p25_pct": max_gain_p25_pct,
        "max_gain_p50_price": max_gain_p50_price,
        "max_gain_p50_pct": max_gain_p50_pct,
        "max_gain_p75_price": max_gain_p75_price,
        "max_gain_p75_pct": max_gain_p75_pct,
        "max_gain_p90_price": max_gain_p90_price,
        "max_gain_p90_pct": max_gain_p90_pct,
    }

    if row["current_price"] is None:
        return None

    return row


def parse_latest_report(text):
    forecast_date, target_date_30d, generated_at_utc = extract_generated_info(text)

    map_section = section_between(
        text,
        "# Mappa semplice asset per asset",
        "# Come leggere correttamente i 30 giorni",
    )

    rows = []

    for asset, asset_name in ASSETS:
        row = parse_asset_prediction(
            map_section=map_section,
            asset=asset,
            asset_name=asset_name,
            forecast_date=forecast_date,
            target_date_30d=target_date_30d,
            generated_at_utc=generated_at_utc,
        )

        if row is not None:
            rows.append(row)

    return rows


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


def update_history(rows):
    df = load_history()

    if not rows:
        return df

    new_df = pd.DataFrame(rows)

    for col in COLUMNS:
        if col not in new_df.columns:
            new_df[col] = None

    new_df = new_df[COLUMNS]

    # Evita doppioni se lanci il workflow più volte nello stesso giorno.
    # Tiene l'ultima lettura del giorno per ogni asset.
    for _, row in new_df.iterrows():
        forecast_date = str(row["forecast_date"])
        asset = str(row["asset"])

        mask = ~(
            (df["forecast_date"].astype(str) == forecast_date)
            & (df["asset"].astype(str) == asset)
        )
        df = df[mask]

    df = pd.concat([df, new_df], ignore_index=True)

    df["forecast_date_sort"] = pd.to_datetime(df["forecast_date"], errors="coerce")
    df["asset_sort"] = df["asset"].astype(str)
    df = df.sort_values(["forecast_date_sort", "asset_sort"])
    df = df.drop(columns=["forecast_date_sort", "asset_sort"])

    df = df[COLUMNS]
    df.to_csv(HISTORY_CSV_PATH, index=False)

    return df


def latest_rows_by_asset(df):
    if df.empty:
        return pd.DataFrame(columns=COLUMNS)

    work = df.copy()
    work["forecast_date_dt"] = pd.to_datetime(work["forecast_date"], errors="coerce")
    work = work.dropna(subset=["forecast_date_dt"])

    if work.empty:
        return pd.DataFrame(columns=COLUMNS)

    idx = work.sort_values("forecast_date_dt").groupby("asset")["forecast_date_dt"].idxmax()
    latest = work.loc[idx].sort_values("asset")
    return latest[COLUMNS]


def build_compact_rows(df):
    rows = []

    for _, r in df.iterrows():
        asset = r.get("asset")

        rows.append(
            [
                r.get("forecast_date", "n/a"),
                asset,
                fmt_price(r.get("current_price"), asset),
                r.get("direction", "n/a"),
                fmt_pct(r.get("positive_rate"), force_sign=False),
                fmt_price(r.get("return_p50_price"), asset),
                fmt_pct(r.get("return_p50_pct")),
                fmt_price(r.get("drawdown_p50_price"), asset),
                fmt_pct(r.get("drawdown_p50_pct")),
                fmt_price(r.get("max_gain_p50_price"), asset),
                fmt_pct(r.get("max_gain_p50_pct")),
                r.get("target_date_30d", "n/a"),
            ]
        )

    return rows


def build_asset_history_table(df, asset):
    work = df[df["asset"] == asset].copy()

    if work.empty:
        return "Nessuna previsione salvata."

    work["forecast_date_dt"] = pd.to_datetime(work["forecast_date"], errors="coerce")
    work = work.sort_values("forecast_date_dt")

    rows = []

    for _, r in work.iterrows():
        rows.append(
            [
                r.get("forecast_date", "n/a"),
                fmt_price(r.get("current_price"), asset),
                r.get("direction", "n/a"),
                fmt_pct(r.get("positive_rate"), force_sign=False),
                fmt_price(r.get("return_p50_price"), asset),
                fmt_pct(r.get("return_p50_pct")),
                fmt_price(r.get("drawdown_p50_price"), asset),
                fmt_pct(r.get("drawdown_p50_pct")),
                fmt_price(r.get("max_gain_p50_price"), asset),
                fmt_pct(r.get("max_gain_p50_pct")),
                fmt_price(r.get("max_gain_p75_price"), asset),
                fmt_pct(r.get("max_gain_p75_pct")),
                r.get("target_date_30d", "n/a"),
            ]
        )

    return md_table(
        [
            "Data",
            "Prezzo",
            "Direzione",
            "Casi positivi",
            "Return p50",
            "Return %",
            "Drawdown p50",
            "Drawdown %",
            "Max gain p50",
            "Max gain %",
            "Max gain p75",
            "Max gain p75 %",
            "Controllo 30g",
        ],
        rows,
    )


def build_full_percentile_table(df, asset):
    work = df[df["asset"] == asset].copy()

    if work.empty:
        return "Nessuna previsione salvata."

    work["forecast_date_dt"] = pd.to_datetime(work["forecast_date"], errors="coerce")
    work = work.sort_values("forecast_date_dt")

    rows = []

    for _, r in work.iterrows():
        rows.append(
            [
                r.get("forecast_date", "n/a"),
                fmt_price(r.get("return_p10_price"), asset),
                fmt_price(r.get("return_p25_price"), asset),
                fmt_price(r.get("return_p50_price"), asset),
                fmt_price(r.get("return_p75_price"), asset),
                fmt_price(r.get("return_p90_price"), asset),
                fmt_price(r.get("drawdown_p10_price"), asset),
                fmt_price(r.get("drawdown_p25_price"), asset),
                fmt_price(r.get("drawdown_p50_price"), asset),
                fmt_price(r.get("max_gain_p50_price"), asset),
                fmt_price(r.get("max_gain_p75_price"), asset),
                fmt_price(r.get("max_gain_p90_price"), asset),
            ]
        )

    return md_table(
        [
            "Data",
            "Return p10",
            "Return p25",
            "Return p50",
            "Return p75",
            "Return p90",
            "Drawdown p10",
            "Drawdown p25",
            "Drawdown p50",
            "Max gain p50",
            "Max gain p75",
            "Max gain p90",
        ],
        rows,
    )


def build_markdown_report(df):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    latest = latest_rows_by_asset(df)

    latest_table = (
        md_table(
            [
                "Data",
                "Asset",
                "Prezzo",
                "Direzione",
                "Casi positivi",
                "Return p50",
                "Return %",
                "Drawdown p50",
                "Drawdown %",
                "Max gain p50",
                "Max gain %",
                "Controllo 30g",
            ],
            build_compact_rows(latest),
        )
        if not latest.empty
        else "Nessuna previsione salvata."
    )

    total_rows = len(df)
    first_date = "n/a"
    last_date = "n/a"

    if not df.empty:
        dates = pd.to_datetime(df["forecast_date"], errors="coerce").dropna()
        if not dates.empty:
            first_date = dates.min().strftime("%Y-%m-%d")
            last_date = dates.max().strftime("%Y-%m-%d")

    lines = []
    lines.append("# Storico previsioni scanner a 30 giorni")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{utc_now}**")
    lines.append("")
    lines.append("Questo file salva, giorno per giorno, la previsione a 30 giorni dello scanner.")
    lines.append("")
    lines.append("Serve per vedere come cambia nel tempo la lettura:")
    lines.append("")
    lines.append("- direzione prevista")
    lines.append("- casi positivi / negativi")
    lines.append("- scenario centrale a 30 giorni")
    lines.append("- drawdown atteso durante i 30 giorni")
    lines.append("- massimo rialzo atteso durante i 30 giorni")
    lines.append("")
    lines.append("Il file CSV completo è: `forecast_30d_history.csv`.")
    lines.append("")
    lines.append("## Stato archivio")
    lines.append("")
    lines.append(
        md_table(
            ["Voce", "Valore"],
            [
                ["Prima previsione salvata", first_date],
                ["Ultima previsione salvata", last_date],
                ["Righe totali salvate", total_rows],
                ["Asset seguiti", ", ".join([a for a, _ in ASSETS])],
            ],
        )
    )
    lines.append("")
    lines.append("## Ultima previsione salvata")
    lines.append("")
    lines.append(latest_table)
    lines.append("")
    lines.append("## Storico compatto per asset")
    lines.append("")

    for asset, asset_name in ASSETS:
        lines.append(f"### {asset_name} ({asset})")
        lines.append("")
        lines.append(build_asset_history_table(df, asset))
        lines.append("")

    lines.append("## Storico completo percentili")
    lines.append("")
    lines.append("Questa parte è più larga, ma è utile se vuoi vedere tutta l'evoluzione delle bande.")
    lines.append("")

    for asset, asset_name in ASSETS:
        lines.append(f"### {asset_name} ({asset}) — percentili completi")
        lines.append("")
        lines.append(build_full_percentile_table(df, asset))
        lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- **Return p50**: scenario centrale del prezzo fra 30 giorni.")
    lines.append("- **Drawdown p50**: discesa normale possibile durante quei 30 giorni.")
    lines.append("- **Drawdown p10/p25**: scenari brutti da guardare se usi leva.")
    lines.append("- **Max gain p50**: rialzo normale possibile durante il mese.")
    lines.append("- **Max gain p75/p90**: zone più ottimistiche, utili per take profit.")
    lines.append("- **Controllo 30g**: giorno in cui quella previsione potrà essere verificata.")
    lines.append("")
    lines.append("Nota: se lanci il workflow più volte nello stesso giorno, viene tenuta solo l'ultima previsione di quel giorno per ogni asset.")
    lines.append("")

    return "\n".join(lines)


def build_main_report_block(df):
    latest = latest_rows_by_asset(df)

    if latest.empty:
        latest_table = "Nessuna previsione salvata."
    else:
        latest_table = md_table(
            [
                "Data",
                "Asset",
                "Prezzo",
                "Direzione",
                "Casi positivi",
                "Return p50",
                "Drawdown p50",
                "Max gain p50",
                "Controllo 30g",
            ],
            [
                [
                    r.get("forecast_date", "n/a"),
                    r.get("asset", "n/a"),
                    fmt_price(r.get("current_price"), r.get("asset")),
                    r.get("direction", "n/a"),
                    fmt_pct(r.get("positive_rate"), force_sign=False),
                    fmt_price(r.get("return_p50_price"), r.get("asset")),
                    fmt_price(r.get("drawdown_p50_price"), r.get("asset")),
                    fmt_price(r.get("max_gain_p50_price"), r.get("asset")),
                    r.get("target_date_30d", "n/a"),
                ]
                for _, r in latest.iterrows()
            ],
        )

    total_rows = len(df)

    return "\n".join(
        [
            START_MARKER,
            "",
            "---",
            "",
            "# Storico previsioni 30 giorni",
            "",
            "Report separato completo: [forecast_30d_history.md](forecast_30d_history.md)",
            "",
            f"Righe salvate nello storico: **{total_rows}**.",
            "",
            "Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.",
            "",
            latest_table,
            "",
            END_MARKER,
        ]
    )


def inject_into_main_report(df):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # Rimuove vecchio blocco se già presente.
    if START_MARKER in text and END_MARKER in text:
        before = text.split(START_MARKER)[0].rstrip()
        after = text.split(END_MARKER, 1)[1].lstrip()
        text = before + "\n\n" + after

    block = build_main_report_block(df).strip()

    # Lo mettiamo subito dopo lo Scanner Forecast Tracker, se presente.
    insert_after = "<!-- SCANNER_FORECAST_TRACKER_END -->"

    if insert_after in text:
        pos = text.find(insert_after) + len(insert_after)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    else:
        new_text = text.rstrip() + "\n\n" + block + "\n"

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    if not os.path.exists(MAIN_REPORT_PATH):
        report = "# Storico previsioni scanner a 30 giorni\n\n`latest_report.md` non trovato.\n"
        with open(HISTORY_MD_PATH, "w", encoding="utf-8") as f:
            f.write(report)
        print("latest_report.md not found.")
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        latest_report = f.read()

    rows = parse_latest_report(latest_report)

    if not rows:
        report = "# Storico previsioni scanner a 30 giorni\n\nNessuna previsione leggibile trovata nel report principale.\n"
        with open(HISTORY_MD_PATH, "w", encoding="utf-8") as f:
            f.write(report)
        print("No readable forecast rows found.")
        return

    df = update_history(rows)

    markdown = build_markdown_report(df)

    with open(HISTORY_MD_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)

    inject_into_main_report(df)

    print(f"Wrote {HISTORY_CSV_PATH}")
    print(f"Wrote {HISTORY_MD_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")
    print(f"Rows added/updated: {len(rows)}")


if __name__ == "__main__":
    main()
