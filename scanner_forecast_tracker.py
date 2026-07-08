from pathlib import Path
from datetime import datetime, timezone
import re

import numpy as np
import pandas as pd
import yfinance as yf

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"

FORECAST_LOG = REPORTS_DIR / "scanner_forecast_path_log.csv"
ACCURACY_METRICS = REPORTS_DIR / "scanner_forecast_path_accuracy_metrics.csv"
OUTPUT_REPORT = REPORTS_DIR / "scanner_forecast_path_report.md"

START_MARKER = "<!-- SCANNER_FORECAST_TRACKER_START -->"
END_MARKER = "<!-- SCANNER_FORECAST_TRACKER_END -->"

ASSETS = {
    "BTC": {
        "name": "Bitcoin",
        "ticker": "BTC-USD",
        "chart": REPORTS_DIR / "scanner_forecast_BTC.png",
    },
    "SOL": {
        "name": "Solana",
        "ticker": "SOL-USD",
        "chart": REPORTS_DIR / "scanner_forecast_SOL.png",
    },
    "DOGE": {
        "name": "Dogecoin",
        "ticker": "DOGE-USD",
        "chart": REPORTS_DIR / "scanner_forecast_DOGE.png",
    },
}

PERCENTILES = [10, 25, 50, 75, 90]
FORECAST_DAYS = 30

NUMBER_PATTERN = r"([0-9]{1,3}(?:\.[0-9]{3})*(?:,[0-9]+)?|[0-9]+(?:[.,][0-9]+)?)"


def utc_now():
    return datetime.now(timezone.utc)


def today_str():
    return utc_now().strftime("%Y-%m-%d")


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

    if not s or s.lower() == "nan":
        return np.nan

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


def parse_pct(value):
    if value is None:
        return np.nan

    s = str(value).strip()
    s = s.replace("%", "")
    s = s.replace("+", "")
    s = s.replace("−", "-")
    s = s.replace(",", ".")
    s = re.sub(r"[^0-9.\-]", "", s)

    if not s or s in ["-", ".", "-."]:
        return np.nan

    try:
        return float(s)
    except Exception:
        return np.nan


def fmt_pct(x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return f"{x:.2f}%".replace(".", ",")


def fmt_price(asset, x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    if asset == "DOGE":
        return f"{x:.5f} $"

    if x >= 1000:
        return f"{x:,.2f} $".replace(",", "X").replace(".", ",").replace("X", ".")

    return f"{x:.2f} $".replace(".", ",")


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


def read_text(path):
    if not path.exists():
        return ""

    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def clean_text(s):
    if s is None:
        return ""

    s = str(s)
    s = s.replace("**", "")
    s = s.replace("__", "")
    s = s.replace("`", "")
    s = s.replace("|", " ")
    s = re.sub(r"\s+", " ", s)

    return s.strip()


def first_price(text):
    if not text:
        return np.nan

    m = re.search(NUMBER_PATTERN + r"\s*\$", str(text))

    if not m:
        return np.nan

    return parse_number(m.group(1))


def first_pct(text):
    if not text:
        return np.nan

    m = re.search(r"([+\-]?[0-9]+(?:[.,][0-9]+)?)\s*%", str(text))

    if not m:
        return np.nan

    return parse_pct(m.group(1))


def normalize_ohlcv(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

        if any(f in level0 for f in fields):
            tmp = {}

            for field in fields:
                if field in level0:
                    part = out.xs(field, axis=1, level=0)
                    tmp[field] = part.iloc[:, 0]

            out = pd.DataFrame(tmp)

        elif any(f in level1 for f in fields):
            tmp = {}

            for field in fields:
                if field in level1:
                    part = out.xs(field, axis=1, level=1)
                    tmp[field] = part.iloc[:, 0]

            out = pd.DataFrame(tmp)

    needed = ["Open", "High", "Low", "Close", "Volume"]

    for col in needed:
        if col not in out.columns:
            if col in ["Open", "High", "Low"] and "Close" in out.columns:
                out[col] = out["Close"]
            elif col == "Volume":
                out[col] = np.nan
            else:
                return pd.DataFrame()

    out = out[needed].copy()
    out.index = pd.to_datetime(out.index)

    try:
        if out.index.tz is not None:
            out.index = out.index.tz_convert(None)
    except Exception:
        pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")]
    out = out.sort_index()
    out = out.dropna(subset=["Close"])

    return out


def download_prices(ticker, start=None):
    try:
        kwargs = {
            "tickers": ticker,
            "interval": "1d",
            "progress": False,
            "auto_adjust": False,
            "actions": False,
            "threads": False,
        }

        if start:
            kwargs["start"] = start
        else:
            kwargs["period"] = "max"

        raw = yf.download(**kwargs)

        return normalize_ohlcv(raw)

    except Exception as e:
        print(f"Download prezzi fallito per {ticker}: {e}")
        return pd.DataFrame()


def current_price_from_market(ticker):
    df = download_prices(ticker, start="2020-01-01")

    if df.empty:
        return np.nan

    return safe_float(df["Close"].iloc[-1])


def actual_price_on_or_after(df, date):
    if df.empty:
        return np.nan

    date = pd.to_datetime(date).normalize()
    d = df[df.index >= date]

    if d.empty:
        return np.nan

    return safe_float(d.iloc[0]["Close"])


def extract_asset_block(text, asset_name):
    heading = f"# {asset_name} — mappa semplice"

    start = text.find(heading)

    if start == -1:
        heading = f"# {asset_name}"
        start = text.find(heading)

    if start == -1:
        return ""

    rest = text[start:]

    possible_stops = []

    for other in ["# Bitcoin", "# Solana", "# Dogecoin", "# Come leggere correttamente"]:
        pos = rest.find("\n" + other, len(heading))

        if pos != -1:
            possible_stops.append(pos)

    if possible_stops:
        return rest[:min(possible_stops)]

    return rest


def extract_between_headings(block, start_label, end_label):
    start = block.lower().find(start_label.lower())

    if start == -1:
        return ""

    rest = block[start:]

    end = rest.lower().find(end_label.lower())

    if end == -1:
        return rest

    return rest[:end]


def parse_current_price(block):
    for line in block.splitlines():
        clean = clean_text(line)

        if "Prezzo attuale" in clean:
            price = first_price(clean)

            if not pd.isna(price):
                return price

    return np.nan


def parse_direction_stats(block):
    direction = ""
    positive = np.nan
    negative = np.nan

    for line in block.splitlines():
        clean = clean_text(line)
        low = clean.lower()

        if "direzione più probabile" in low:
            if ":" in clean:
                direction = clean.split(":", 1)[-1].strip()

        if "probabilità storica di salita" in low or "casi positivi" in low:
            pct = first_pct(clean)

            if not pd.isna(pct):
                positive = pct

        if "probabilità storica di discesa" in low or "casi negativi" in low:
            pct = first_pct(clean)

            if not pd.isna(pct):
                negative = pct

    return direction, positive, negative


def parse_return_percentiles(block):
    section = extract_between_headings(
        block,
        "## 1. Return 30d",
        "## 2. Drawdown 30d",
    )

    if not section:
        section = block

    out = {}

    for p in PERCENTILES:
        out[p] = {
            "return_pct": np.nan,
            "price": np.nan,
        }

    # Formato dettagliato:
    # Percentile 10%: -12,81% → 54.134,13 $
    for line in section.splitlines():
        clean = clean_text(line)

        m = re.search(
            rf"Percentile\s+([0-9]+)%\s*:\s*([+\-]?[0-9]+(?:[.,][0-9]+)?)\s*%.*?{NUMBER_PATTERN}\s*\$",
            clean,
            flags=re.IGNORECASE,
        )

        if not m:
            continue

        p = int(m.group(1))

        if p not in PERCENTILES:
            continue

        out[p] = {
            "return_pct": parse_pct(m.group(2)),
            "price": parse_number(m.group(3)),
        }

    # Formato mappa semplice:
    # Se va molto male: 54.134,13 $ (-12,81%)
    # Se va male: 60.493,40 $ (-2,57%)
    # Scenario normale: 64.188,68 $ (3,39%)
    # Se va bene: 74.215,01 $ (19,54%)
    # Se va molto bene: 89.248,60 $ (43,75%)
    label_to_percentile = {
        "se va molto male": 10,
        "se va male": 25,
        "scenario normale": 50,
        "se va bene": 75,
        "se va molto bene": 90,
    }

    ordered_labels = [
        "se va molto male",
        "se va molto bene",
        "se va male",
        "se va bene",
        "scenario normale",
    ]

    for line in section.splitlines():
        clean = clean_text(line)
        low = clean.lower()

        matched_label = None

        for label in ordered_labels:
            if label in low:
                matched_label = label
                break

        if matched_label is None:
            continue

        p = label_to_percentile[matched_label]
        price = first_price(clean)

        pct = np.nan
        pct_match = re.search(r"$begin:math:text$\(\[\+\\\-\]\?\[0\-9\]\+\(\?\:\[\.\,\]\[0\-9\]\+\)\?\)\\s\*\%$end:math:text$", clean)

        if pct_match:
            pct = parse_pct(pct_match.group(1))
        else:
            pct = first_pct(clean)

        if not pd.isna(price):
            out[p] = {
                "return_pct": pct,
                "price": price,
            }

    return out


def parse_scanner_forecast_from_latest():
    text = read_text(LATEST_REPORT)

    rows = []
    meta = []

    if not text:
        return pd.DataFrame(), pd.DataFrame()

    forecast_date = today_str()
    created_at = utc_now().strftime("%Y-%m-%d %H:%M:%S UTC")

    for asset, cfg in ASSETS.items():
        block = extract_asset_block(text, cfg["name"])

        if not block:
            continue

        start_price = parse_current_price(block)

        if pd.isna(start_price):
            start_price = current_price_from_market(cfg["ticker"])

        direction, positive, negative = parse_direction_stats(block)
        percentiles = parse_return_percentiles(block)

        meta.append({
            "forecast_date": forecast_date,
            "created_at_utc": created_at,
            "asset": asset,
            "ticker": cfg["ticker"],
            "start_price": start_price,
            "direction": direction,
            "positive_rate": positive,
            "negative_rate": negative,
            "p10_30d": percentiles[10]["price"],
            "p25_30d": percentiles[25]["price"],
            "p50_30d": percentiles[50]["price"],
            "p75_30d": percentiles[75]["price"],
            "p90_30d": percentiles[90]["price"],
        })

        for day in range(0, FORECAST_DAYS + 1):
            target_date = pd.to_datetime(forecast_date) + pd.Timedelta(days=day)
            t = day / FORECAST_DAYS if FORECAST_DAYS > 0 else 1.0

            row = {
                "forecast_date": forecast_date,
                "created_at_utc": created_at,
                "asset": asset,
                "ticker": cfg["ticker"],
                "day_index": day,
                "target_date": target_date.strftime("%Y-%m-%d"),
                "start_price": start_price,
                "direction": direction,
                "positive_rate": positive,
                "negative_rate": negative,
                "checked": 0.0,
                "actual_price": np.nan,
                "inside_p10_p90": np.nan,
                "inside_p25_p75": np.nan,
                "error_vs_p50_pct": np.nan,
            }

            for p in PERCENTILES:
                target_price = safe_float(percentiles[p]["price"])

                if day == 0:
                    projected = start_price
                elif pd.isna(start_price) or pd.isna(target_price):
                    projected = np.nan
                else:
                    projected = start_price + (target_price - start_price) * t

                row[f"p{p}"] = projected

            rows.append(row)

    return pd.DataFrame(rows), pd.DataFrame(meta)


def append_today_forecast(today_df):
    if FORECAST_LOG.exists():
        old = pd.read_csv(FORECAST_LOG)
    else:
        old = pd.DataFrame()

    if old.empty:
        combined = today_df
    else:
        keys = ["forecast_date", "asset", "day_index"]

        for k in keys:
            if k not in old.columns:
                old[k] = np.nan

        old_marker = old[keys].astype(str).agg("|".join, axis=1)
        today_marker = today_df[keys].astype(str).agg("|".join, axis=1)

        old = old[~old_marker.isin(set(today_marker))]
        combined = pd.concat([old, today_df], ignore_index=True)

    combined.to_csv(FORECAST_LOG, index=False)

    return combined


def update_checks(log_df):
    if log_df.empty:
        return log_df

    today = pd.to_datetime(today_str()).normalize()

    for asset, cfg in ASSETS.items():
        asset_df = log_df[log_df["asset"].astype(str) == asset]

        if asset_df.empty:
            continue

        min_date = pd.to_datetime(asset_df["forecast_date"], errors="coerce").min()

        if pd.isna(min_date):
            min_date = today - pd.Timedelta(days=10)

        dl_start = (min_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d")
        prices = download_prices(cfg["ticker"], start=dl_start)

        if prices.empty:
            continue

        idxs = log_df.index[log_df["asset"].astype(str) == asset].tolist()

        for idx in idxs:
            row = log_df.loc[idx]

            checked = safe_float(row.get("checked", 0.0))

            if not pd.isna(checked) and checked >= 1:
                continue

            target_date = pd.to_datetime(row.get("target_date", ""), errors="coerce")

            if pd.isna(target_date):
                continue

            if target_date.normalize() > today:
                continue

            actual = actual_price_on_or_after(prices, target_date)

            if pd.isna(actual):
                continue

            p10 = safe_float(row.get("p10", np.nan))
            p25 = safe_float(row.get("p25", np.nan))
            p50 = safe_float(row.get("p50", np.nan))
            p75 = safe_float(row.get("p75", np.nan))
            p90 = safe_float(row.get("p90", np.nan))

            inside_wide = np.nan
            inside_mid = np.nan

            if not pd.isna(p10) and not pd.isna(p90):
                lo = min(p10, p90)
                hi = max(p10, p90)
                inside_wide = 1.0 if lo <= actual <= hi else 0.0

            if not pd.isna(p25) and not pd.isna(p75):
                lo = min(p25, p75)
                hi = max(p25, p75)
                inside_mid = 1.0 if lo <= actual <= hi else 0.0

            error = np.nan

            if not pd.isna(p50) and p50 != 0:
                error = (actual / p50 - 1) * 100

            log_df.at[idx, "checked"] = 1.0
            log_df.at[idx, "actual_price"] = actual
            log_df.at[idx, "inside_p10_p90"] = inside_wide
            log_df.at[idx, "inside_p25_p75"] = inside_mid
            log_df.at[idx, "error_vs_p50_pct"] = error

    log_df.to_csv(FORECAST_LOG, index=False)

    return log_df


def latest_forecast(log_df, asset):
    if log_df.empty:
        return pd.DataFrame()

    d = log_df[log_df["asset"].astype(str) == asset].copy()

    if d.empty:
        return pd.DataFrame()

    d["forecast_date_dt"] = pd.to_datetime(d["forecast_date"], errors="coerce")
    max_date = d["forecast_date_dt"].max()

    latest = d[d["forecast_date_dt"] == max_date].copy()
    latest["day_index"] = pd.to_numeric(latest["day_index"], errors="coerce")

    return latest.sort_values("day_index")


def summarize_accuracy(log_df):
    rows = []

    if log_df.empty:
        return pd.DataFrame()

    checked = log_df[pd.to_numeric(log_df["checked"], errors="coerce").fillna(0) >= 1].copy()

    for asset in ASSETS.keys():
        d_asset = checked[checked["asset"].astype(str) == asset].copy()

        for day in [1, 3, 7, 14, 30]:
            d = d_asset[pd.to_numeric(d_asset["day_index"], errors="coerce") == day].copy()
            n = len(d)

            if n == 0:
                wide_rate = np.nan
                mid_rate = np.nan
                avg_abs_error = np.nan
                avg_error = np.nan
            else:
                wide_values = pd.to_numeric(d["inside_p10_p90"], errors="coerce").dropna()
                mid_values = pd.to_numeric(d["inside_p25_p75"], errors="coerce").dropna()

                wide_rate = wide_values.mean() * 100 if len(wide_values) else np.nan
                mid_rate = mid_values.mean() * 100 if len(mid_values) else np.nan

                errors = pd.to_numeric(d["error_vs_p50_pct"], errors="coerce")
                avg_abs_error = errors.abs().mean()
                avg_error = errors.mean()

            rows.append({
                "asset": asset,
                "day_index": day,
                "checked_predictions": n,
                "inside_p10_p90_rate": wide_rate,
                "inside_p25_p75_rate": mid_rate,
                "avg_abs_error_vs_p50": avg_abs_error,
                "avg_error_vs_p50": avg_error,
            })

    return pd.DataFrame(rows)


def plot_asset_chart(log_df, asset):
    cfg = ASSETS[asset]
    latest = latest_forecast(log_df, asset)

    if latest.empty:
        return

    latest["target_date_dt"] = pd.to_datetime(latest["target_date"], errors="coerce")
    latest = latest.dropna(subset=["target_date_dt"])

    if latest.empty:
        return

    start_date = pd.to_datetime(latest["forecast_date"].iloc[0]).normalize()
    end_date = latest["target_date_dt"].max()

    for col in ["p10", "p25", "p50", "p75", "p90"]:
        latest[col] = pd.to_numeric(latest[col], errors="coerce")

    if latest[["p10", "p25", "p50", "p75", "p90"]].isna().all().all():
        return

    actual = download_prices(
        cfg["ticker"],
        start=(start_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d"),
    )

    if not actual.empty:
        actual = actual[(actual.index >= start_date) & (actual.index <= end_date)]

    plt.figure(figsize=(11, 6))

    plt.fill_between(
        latest["target_date_dt"],
        latest["p10"],
        latest["p90"],
        alpha=0.12,
        label="Banda larga p10-p90",
    )

    plt.fill_between(
        latest["target_date_dt"],
        latest["p25"],
        latest["p75"],
        alpha=0.20,
        label="Banda centrale p25-p75",
    )

    plt.plot(latest["target_date_dt"], latest["p50"], marker="o", label="Scenario centrale p50")
    plt.plot(latest["target_date_dt"], latest["p10"], linestyle="--", label="p10")
    plt.plot(latest["target_date_dt"], latest["p90"], linestyle="--", label="p90")

    if not actual.empty:
        plt.plot(actual.index, actual["Close"], marker="o", label=f"{asset} reale")

    plt.title(f"{asset} — cono previsionale scanner 40 casi")
    plt.xlabel("Data")
    plt.ylabel("Prezzo")
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(cfg["chart"], dpi=160)
    plt.close()


def render_report(log_df, metrics):
    now = utc_now().strftime("%Y-%m-%d %H:%M UTC")

    lines = []

    lines.append("# Scanner forecast path / cono probabilistico")
    lines.append("")
    lines.append(f"Generato: {now}")
    lines.append("")
    lines.append("Questo report trasforma lo scanner dei 40 casi simili in un grafico a percorso.")
    lines.append("")
    lines.append("Per ogni asset crea:")
    lines.append("")
    lines.append("- banda larga p10-p90")
    lines.append("- banda centrale p25-p75")
    lines.append("- scenario centrale p50")
    lines.append("- prezzo reale sovrapposto")
    lines.append("")
    lines.append("Serve a vedere se il prezzo reale sta camminando dentro il percorso previsto dallo scanner.")
    lines.append("")

    if log_df.empty:
        lines.append("_Nessuna previsione scanner salvata._")
        return "\n".join(lines) + "\n"

    lines.append("## Ultimo cono previsionale salvato")
    lines.append("")

    summary_rows = []

    for asset in ASSETS.keys():
        latest = latest_forecast(log_df, asset)

        if latest.empty:
            continue

        first = latest.iloc[0]
        final = latest[latest["day_index"] == FORECAST_DAYS]

        if final.empty:
            final_row = latest.iloc[-1]
        else:
            final_row = final.iloc[0]

        summary_rows.append({
            "Asset": asset,
            "Data": first.get("forecast_date", ""),
            "Prezzo iniziale": fmt_price(asset, first.get("start_price", np.nan)),
            "Direzione scanner": first.get("direction", ""),
            "Casi positivi": fmt_pct(first.get("positive_rate", np.nan)),
            "P10 30g": fmt_price(asset, final_row.get("p10", np.nan)),
            "P25 30g": fmt_price(asset, final_row.get("p25", np.nan)),
            "P50 30g": fmt_price(asset, final_row.get("p50", np.nan)),
            "P75 30g": fmt_price(asset, final_row.get("p75", np.nan)),
            "P90 30g": fmt_price(asset, final_row.get("p90", np.nan)),
        })

    lines.append(df_to_markdown(pd.DataFrame(summary_rows)))
    lines.append("")

    lines.append("## Grafici")
    lines.append("")

    for asset, cfg in ASSETS.items():
        if cfg["chart"].exists():
            lines.append(f"### {asset}")
            lines.append("")
            lines.append(f"![Scanner forecast {asset}]({cfg['chart'].name})")
            lines.append("")

    lines.append("## Accuratezza percorso scanner")
    lines.append("")

    if metrics.empty:
        lines.append("_Dati insufficienti._")
    else:
        metric_rows = []

        for _, r in metrics.iterrows():
            metric_rows.append({
                "Asset": r["asset"],
                "Giorno": f"{int(r['day_index'])}g",
                "Controlli": int(r["checked_predictions"]),
                "Dentro p10-p90": fmt_pct(r["inside_p10_p90_rate"]),
                "Dentro p25-p75": fmt_pct(r["inside_p25_p75_rate"]),
                "Errore medio abs vs p50": fmt_pct(r["avg_abs_error_vs_p50"]),
                "Errore medio vs p50": fmt_pct(r["avg_error_vs_p50"]),
            })

        lines.append(df_to_markdown(pd.DataFrame(metric_rows)))

    lines.append("")
    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.")
    lines.append("- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.")
    lines.append("- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.")
    lines.append("- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.")
    lines.append("- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.")
    lines.append("")

    return "\n".join(lines) + "\n"


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
        anchor = "<!-- MODULE_ACCURACY_END -->"

        if anchor in old:
            idx = old.find(anchor) + len(anchor)
            new = old[:idx] + "\n\n" + new_section + old[idx:]
        else:
            anchor = "<!-- BOUNCE_AFTER_DRAWDOWN_END -->"

            if anchor in old:
                idx = old.find(anchor) + len(anchor)
                new = old[:idx] + "\n\n" + new_section + old[idx:]
            else:
                new = old.rstrip() + "\n\n" + new_section + "\n"

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    today_df, meta_df = parse_scanner_forecast_from_latest()

    if today_df.empty:
        md = "# Scanner forecast path / cono probabilistico\n\nNessuna previsione scanner trovata.\n"
        OUTPUT_REPORT.write_text(md, encoding="utf-8")
        inject_into_latest_report(md)
        print("Nessuna previsione scanner trovata.")
        return

    log_df = append_today_forecast(today_df)
    log_df = update_checks(log_df)

    metrics = summarize_accuracy(log_df)
    metrics.to_csv(ACCURACY_METRICS, index=False)

    for asset in ASSETS.keys():
        plot_asset_chart(log_df, asset)

    md = render_report(log_df, metrics)

    OUTPUT_REPORT.write_text(md, encoding="utf-8")
    inject_into_latest_report(md)

    print(f"Creato/aggiornato {FORECAST_LOG}")
    print(f"Creato {ACCURACY_METRICS}")
    print(f"Creato {OUTPUT_REPORT}")

    for asset, cfg in ASSETS.items():
        if cfg["chart"].exists():
            print(f"Creato {cfg['chart']}")


if __name__ == "__main__":
    main()
