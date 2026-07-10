import os
import re
from datetime import datetime, timedelta

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = "reports"
MAIN_REPORT_PATH = os.path.join(REPORTS_DIR, "latest_report.md")

START_MARKER = "<!-- SCANNER_FORECAST_TRACKER_START -->"
END_MARKER = "<!-- SCANNER_FORECAST_TRACKER_END -->"

HISTORY_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_history.csv")
LATEST_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_latest.csv")
METRICS_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_tracker_metrics.csv")
REPORT_PATH = os.path.join(REPORTS_DIR, "scanner_forecast_tracker_report.md")

FULL_MATCHES_PATH = os.path.join(REPORTS_DIR, "latest_scanner_matches.csv")

TARGETS = {
    "BTC-USD": "BTC",
    "SOL-USD": "SOL",
    "DOGE-USD": "DOGE",
}

FORECAST_DAYS = 30
MATCH_LIMIT = 40
ACCURACY_HORIZONS = [1, 3, 7, 14, 30]


def ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)


def asset_short(ticker):
    return TARGETS.get(ticker, ticker.replace("-USD", ""))


def asset_name(ticker):
    names = {
        "BTC-USD": "Bitcoin",
        "SOL-USD": "Solana",
        "DOGE-USD": "Dogecoin",
    }
    return names.get(ticker, ticker)


def fmt_number_it(value, decimals=2):
    try:
        if pd.isna(value):
            return "n/a"
        s = f"{float(value):,.{decimals}f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "n/a"


def fmt_pct(value, decimals=2):
    if pd.isna(value):
        return "n/a"
    return f"{fmt_number_it(value, decimals)}%"


def fmt_price(value, ticker=None):
    if pd.isna(value):
        return "n/a"

    if ticker == "DOGE-USD" or (ticker and "DOGE" in str(ticker)):
        return f"{float(value):.5f} $"

    if abs(float(value)) < 1:
        return f"{float(value):.5f} $"

    return f"{fmt_number_it(value, 2)} $"


def safe_read_csv(path):
    if not os.path.exists(path):
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Errore lettura CSV {path}: {e}")
        return pd.DataFrame()


def load_matches_for_target(target):
    all_matches = safe_read_csv(FULL_MATCHES_PATH)

    if not all_matches.empty and "target" in all_matches.columns:
        out = all_matches[all_matches["target"].astype(str) == target].copy()
        if not out.empty:
            if "similarity" in out.columns:
                out["similarity"] = pd.to_numeric(out["similarity"], errors="coerce")
                out = out.sort_values("similarity", ascending=False)
            return out.head(MATCH_LIMIT).reset_index(drop=True)

    short = asset_short(target)
    fallback_path = os.path.join(REPORTS_DIR, f"{short}_matches.csv")
    out = safe_read_csv(fallback_path)

    if out.empty:
        return out

    out["target"] = target

    if "similarity" in out.columns:
        out["similarity"] = pd.to_numeric(out["similarity"], errors="coerce")
        out = out.sort_values("similarity", ascending=False)

    return out.head(MATCH_LIMIT).reset_index(drop=True)


def normalize_yfinance_df(raw, ticker):
    if raw is None or raw.empty:
        return pd.DataFrame()

    try:
        if isinstance(raw.columns, pd.MultiIndex):
            if ticker not in raw.columns.get_level_values(0):
                return pd.DataFrame()
            df = raw[ticker].copy()
        else:
            df = raw.copy()

        df = df.dropna(how="all").copy()

        if "Close" not in df.columns:
            return pd.DataFrame()

        df.index = pd.to_datetime(df.index)

        if df.index.tz is not None:
            df.index = df.index.tz_convert(None)

        df = df.sort_index()
        df = df[~df.index.duplicated(keep="last")]

        return df
    except Exception as e:
        print(f"{ticker}: errore normalizzazione dati yfinance: {e}")
        return pd.DataFrame()


def download_price_data(tickers):
    tickers = sorted(set([t for t in tickers if isinstance(t, str) and t.strip()]))

    if not tickers:
        return {}

    print(f"Download prezzi per {len(tickers)} ticker...")

    raw = yf.download(
        tickers,
        period="10y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )

    data = {}

    for ticker in tickers:
        df = normalize_yfinance_df(raw, ticker)

        if not df.empty and len(df) > FORECAST_DAYS + 5:
            data[ticker] = df
            print(f"{ticker}: OK {df.index[0].date()} -> {df.index[-1].date()}")
        else:
            print(f"{ticker}: dati insufficienti")

    return data


def position_on_or_after(df, date_value):
    if df.empty:
        return None

    dt = pd.to_datetime(date_value, errors="coerce")

    if pd.isna(dt):
        return None

    idx = pd.DatetimeIndex(df.index)

    if idx.tz is not None:
        idx = idx.tz_convert(None)

    idx_norm = idx.normalize()
    dt_norm = dt.normalize()

    positions = np.where(idx_norm >= dt_norm)[0]

    if len(positions) == 0:
        return None

    return int(positions[0])


def close_on_or_after(df, date_value):
    pos = position_on_or_after(df, date_value)

    if pos is None:
        return np.nan

    try:
        return float(df["Close"].iloc[pos])
    except Exception:
        return np.nan


def current_price_for_target(target, data):
    if target in data and not data[target].empty:
        return float(data[target]["Close"].iloc[-1])
    return np.nan


def build_path_matrix(matches, data):
    rows = []

    if matches.empty:
        return pd.DataFrame()

    required = {"similar_asset", "end_date"}

    if not required.issubset(matches.columns):
        print("Match senza colonne richieste similar_asset/end_date.")
        return pd.DataFrame()

    for _, row in matches.iterrows():
        similar_asset = str(row.get("similar_asset", "")).strip()

        if similar_asset not in data:
            continue

        df = data[similar_asset].copy()
        pos = position_on_or_after(df, row.get("end_date"))

        if pos is None:
            continue

        if pos + FORECAST_DAYS >= len(df):
            continue

        base_price = float(df["Close"].iloc[pos])

        if base_price <= 0 or pd.isna(base_price):
            continue

        future = df["Close"].iloc[pos:pos + FORECAST_DAYS + 1].astype(float)
        pct_path = (future / base_price - 1.0) * 100.0

        if len(pct_path) < FORECAST_DAYS + 1:
            continue

        out = {
            "similar_asset": similar_asset,
            "start_date": row.get("start_date", ""),
            "end_date": row.get("end_date", ""),
            "similarity": pd.to_numeric(row.get("similarity", np.nan), errors="coerce"),
            "return_30d": pd.to_numeric(row.get("return_30d", np.nan), errors="coerce"),
        }

        for d in range(FORECAST_DAYS + 1):
            out[f"day_{d}"] = float(pct_path.iloc[d])

        rows.append(out)

    return pd.DataFrame(rows)


def quantile_paths(paths):
    if paths.empty:
        return pd.DataFrame()

    day_cols = [f"day_{d}" for d in range(FORECAST_DAYS + 1)]
    matrix = paths[day_cols].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float)

    rows = []

    for d in range(FORECAST_DAYS + 1):
        values = matrix[:, d]
        values = values[~np.isnan(values)]

        if len(values) == 0:
            continue

        rows.append({
            "day": d,
            "count": len(values),
            "p10_pct": np.percentile(values, 10),
            "p25_pct": np.percentile(values, 25),
            "p50_pct": np.percentile(values, 50),
            "p75_pct": np.percentile(values, 75),
            "p90_pct": np.percentile(values, 90),
            "mean_pct": np.mean(values),
        })

    return pd.DataFrame(rows)


def add_price_levels(quantiles, current_price):
    q = quantiles.copy()

    for col in ["p10", "p25", "p50", "p75", "p90", "mean"]:
        q[f"{col}_price"] = current_price * (1 + q[f"{col}_pct"] / 100.0)

    return q


def direction_from_matches(matches):
    if matches.empty or "return_30d" not in matches.columns:
        return "n/a", np.nan

    returns = pd.to_numeric(matches["return_30d"], errors="coerce").dropna()

    if len(returns) == 0:
        return "n/a", np.nan

    positive = (returns > 0).mean() * 100.0
    negative = 100.0 - positive

    if positive >= 60:
        return "SALITA", positive

    if negative >= 60:
        return "DISCESA", positive

    return "INCERTO", positive


def plot_forecast_cone(target, quantiles_price, current_price, generated_date, data):
    short = asset_short(target)
    out_path = os.path.join(REPORTS_DIR, f"scanner_forecast_{short}.png")

    if quantiles_price.empty:
        return None

    future_dates = [
        generated_date + timedelta(days=int(d))
        for d in quantiles_price["day"].tolist()
    ]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.fill_between(
        future_dates,
        quantiles_price["p10_price"],
        quantiles_price["p90_price"],
        alpha=0.16,
        label="Banda larga p10-p90",
    )

    ax.fill_between(
        future_dates,
        quantiles_price["p25_price"],
        quantiles_price["p75_price"],
        alpha=0.28,
        label="Banda centrale p25-p75",
    )

    ax.plot(
        future_dates,
        quantiles_price["p50_price"],
        linewidth=2.5,
        marker="o",
        markersize=3,
        label="Scenario centrale p50",
    )

    ax.plot(
        future_dates,
        quantiles_price["p10_price"],
        linestyle="--",
        linewidth=1,
        label="p10",
    )

    ax.plot(
        future_dates,
        quantiles_price["p90_price"],
        linestyle="--",
        linewidth=1,
        label="p90",
    )

    if target in data and not data[target].empty:
        target_df = data[target].copy()
        idx = pd.DatetimeIndex(target_df.index)

        if idx.tz is not None:
            idx = idx.tz_convert(None)

        target_df.index = idx.normalize()

        start = pd.to_datetime(generated_date).normalize()
        end = start + pd.Timedelta(days=FORECAST_DAYS)

        real = target_df[(target_df.index >= start) & (target_df.index <= end)].copy()

        if not real.empty:
            ax.plot(
                real.index,
                real["Close"],
                color="red",
                marker="o",
                linewidth=2,
                label=f"{short} reale",
            )
        else:
            ax.scatter(
                [generated_date],
                [current_price],
                color="red",
                zorder=5,
                label=f"{short} reale oggi",
            )

    ax.set_title(f"{short} — cono previsionale scanner 40 casi")
    ax.set_xlabel("Data")
    ax.set_ylabel("Prezzo")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")
    fig.autofmt_xdate()

    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close(fig)

    return out_path


def build_snapshot_rows(target, quantiles_price, current_price, generated_at):
    rows = []
    snapshot_date = generated_at[:10]
    generated_date = pd.to_datetime(snapshot_date)

    for _, row in quantiles_price.iterrows():
        day = int(row["day"])
        target_date = generated_date + pd.Timedelta(days=day)

        rows.append({
            "snapshot_date": snapshot_date,
            "generated_at_utc": generated_at,
            "target_ticker": target,
            "asset": asset_short(target),
            "current_price": current_price,
            "horizon_day": day,
            "target_date": target_date.date().isoformat(),
            "p10_pct": row["p10_pct"],
            "p25_pct": row["p25_pct"],
            "p50_pct": row["p50_pct"],
            "p75_pct": row["p75_pct"],
            "p90_pct": row["p90_pct"],
            "mean_pct": row["mean_pct"],
            "p10_price": row["p10_price"],
            "p25_price": row["p25_price"],
            "p50_price": row["p50_price"],
            "p75_price": row["p75_price"],
            "p90_price": row["p90_price"],
            "mean_price": row["mean_price"],
            "cases_used": row["count"],
        })

    return rows


def update_forecast_history(new_rows):
    new_df = pd.DataFrame(new_rows)

    if new_df.empty:
        return new_df

    old = safe_read_csv(HISTORY_PATH)

    if old.empty:
        history = new_df.copy()
    else:
        history = pd.concat([old, new_df], ignore_index=True, sort=False)

    key_cols = ["snapshot_date", "target_ticker", "horizon_day"]

    if set(key_cols).issubset(history.columns):
        history = history.drop_duplicates(subset=key_cols, keep="last")

    history.to_csv(HISTORY_PATH, index=False)
    return history


def evaluate_forecast_history(history, data):
    if history.empty:
        return pd.DataFrame()

    required = {
        "target_ticker",
        "asset",
        "snapshot_date",
        "target_date",
        "horizon_day",
        "current_price",
        "p10_price",
        "p25_price",
        "p50_price",
        "p75_price",
        "p90_price",
    }

    if not required.issubset(history.columns):
        return pd.DataFrame()

    rows = []

    hist = history.copy()
    hist["horizon_day"] = pd.to_numeric(hist["horizon_day"], errors="coerce")
    hist["target_date_dt"] = pd.to_datetime(hist["target_date"], errors="coerce")
    hist["snapshot_date_dt"] = pd.to_datetime(hist["snapshot_date"], errors="coerce")

    for target in TARGETS:
        if target not in data or data[target].empty:
            continue

        target_df = data[target].copy()
        idx = pd.DatetimeIndex(target_df.index)

        if idx.tz is not None:
            idx = idx.tz_convert(None)

        target_df.index = idx.normalize()
        last_available_date = target_df.index.max().normalize()

        for horizon in ACCURACY_HORIZONS:
            hrows = hist[
                (hist["target_ticker"].astype(str) == target) &
                (hist["horizon_day"] == horizon) &
                (hist["target_date_dt"].notna()) &
                (hist["target_date_dt"].dt.normalize() <= last_available_date)
            ].copy()

            inside_p10_p90 = []
            inside_p25_p75 = []
            abs_errors = []
            signed_errors = []

            for _, row in hrows.iterrows():
                actual_price = close_on_or_after(target_df, row["target_date_dt"])

                if pd.isna(actual_price):
                    continue

                current_price = pd.to_numeric(row.get("current_price"), errors="coerce")
                p10 = pd.to_numeric(row.get("p10_price"), errors="coerce")
                p25 = pd.to_numeric(row.get("p25_price"), errors="coerce")
                p50 = pd.to_numeric(row.get("p50_price"), errors="coerce")
                p75 = pd.to_numeric(row.get("p75_price"), errors="coerce")
                p90 = pd.to_numeric(row.get("p90_price"), errors="coerce")

                if pd.isna(current_price) or current_price <= 0:
                    continue

                if not pd.isna(p10) and not pd.isna(p90):
                    inside_p10_p90.append(p10 <= actual_price <= p90)

                if not pd.isna(p25) and not pd.isna(p75):
                    inside_p25_p75.append(p25 <= actual_price <= p75)

                if not pd.isna(p50):
                    signed_error = (actual_price - p50) / current_price * 100.0
                    signed_errors.append(signed_error)
                    abs_errors.append(abs(signed_error))

            count = len(abs_errors)

            rows.append({
                "asset": asset_short(target),
                "target_ticker": target,
                "horizon": f"{horizon}g",
                "horizon_day": horizon,
                "controls": count,
                "inside_p10_p90_pct": np.mean(inside_p10_p90) * 100.0 if inside_p10_p90 else np.nan,
                "inside_p25_p75_pct": np.mean(inside_p25_p75) * 100.0 if inside_p25_p75 else np.nan,
                "avg_abs_error_vs_p50_pct": np.mean(abs_errors) if abs_errors else np.nan,
                "avg_error_vs_p50_pct": np.mean(signed_errors) if signed_errors else np.nan,
            })

    return pd.DataFrame(rows)


def format_latest_table(latest_rows):
    out = []

    for row in latest_rows:
        target = row["target_ticker"]
        q30 = row["q30"]

        if q30 is None:
            out.append({
                "Asset": row["asset"],
                "Data": row["snapshot_date"],
                "Prezzo iniziale": fmt_price(row["current_price"], target),
                "Direzione scanner": row["direction"],
                "Casi positivi": fmt_pct(row["positive_cases"]),
                "P10 30g": "n/a",
                "P25 30g": "n/a",
                "P50 30g": "n/a",
                "P75 30g": "n/a",
                "P90 30g": "n/a",
            })
            continue

        out.append({
            "Asset": row["asset"],
            "Data": row["snapshot_date"],
            "Prezzo iniziale": fmt_price(row["current_price"], target),
            "Direzione scanner": row["direction"],
            "Casi positivi": fmt_pct(row["positive_cases"]),
            "P10 30g": fmt_price(q30["p10_price"], target),
            "P25 30g": fmt_price(q30["p25_price"], target),
            "P50 30g": fmt_price(q30["p50_price"], target),
            "P75 30g": fmt_price(q30["p75_price"], target),
            "P90 30g": fmt_price(q30["p90_price"], target),
        })

    return pd.DataFrame(out)


def format_accuracy_table(metrics):
    rows = []

    if metrics.empty:
        for target in TARGETS:
            for horizon in ACCURACY_HORIZONS:
                rows.append({
                    "Asset": asset_short(target),
                    "Giorno": f"{horizon}g",
                    "Controlli": 0,
                    "Dentro p10-p90": "n/a",
                    "Dentro p25-p75": "n/a",
                    "Errore medio abs vs p50": "n/a",
                    "Errore medio vs p50": "n/a",
                })
        return pd.DataFrame(rows)

    for _, row in metrics.iterrows():
        rows.append({
            "Asset": row["asset"],
            "Giorno": row["horizon"],
            "Controlli": int(row["controls"]) if not pd.isna(row["controls"]) else 0,
            "Dentro p10-p90": fmt_pct(row["inside_p10_p90_pct"]),
            "Dentro p25-p75": fmt_pct(row["inside_p25_p75_pct"]),
            "Errore medio abs vs p50": fmt_pct(row["avg_abs_error_vs_p50_pct"]),
            "Errore medio vs p50": fmt_pct(row["avg_error_vs_p50_pct"]),
        })

    return pd.DataFrame(rows)


def build_report(generated_at, latest_rows, metrics):
    lines = []

    lines.append(START_MARKER)
    lines.append("# Scanner forecast path / cono probabilistico")
    lines.append("")
    lines.append(f"Generato: {generated_at} UTC")
    lines.append("")
    lines.append(
        "Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile."
    )
    lines.append("")
    lines.append("Per ogni asset crea:")
    lines.append("")
    lines.append("- banda larga p10-p90")
    lines.append("- banda centrale p25-p75")
    lines.append("- scenario centrale p50")
    lines.append("- prezzo reale sovrapposto quando sono disponibili dati successivi")
    lines.append("")
    lines.append(
        "Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, "
        "non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini."
    )
    lines.append("")

    latest_table = format_latest_table(latest_rows)

    lines.append("## Ultimo cono previsionale salvato")
    lines.append("")

    if latest_table.empty:
        lines.append("Nessun cono disponibile.")
    else:
        lines.append(latest_table.to_markdown(index=False))

    lines.append("")
    lines.append("## Grafici")
    lines.append("")

    for row in latest_rows:
        asset = row["asset"]
        img = row.get("chart_filename")

        lines.append(f"### {asset}")
        lines.append("")

        if img:
            lines.append(f"![Scanner forecast {asset}]({img})")
        else:
            lines.append("Grafico non disponibile: dati insufficienti.")

        lines.append("")

    lines.append("## Accuratezza percorso scanner")
    lines.append("")

    accuracy_table = format_accuracy_table(metrics)
    lines.append(accuracy_table.to_markdown(index=False))
    lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append(
        "- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo."
    )
    lines.append(
        "- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale."
    )
    lines.append(
        "- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale."
    )
    lines.append(
        "- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza."
    )
    lines.append(
        "- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto."
    )
    lines.append("")
    lines.append(
        "Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. "
        "Sotto 5 controlli resta solo osservazione."
    )
    lines.append(END_MARKER)

    return "\n".join(lines)


def update_marked_block(text, block):
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        flags=re.DOTALL,
    )

    if pattern.search(text):
        return pattern.sub(block, text)

    preferred_anchors = [
        "<!-- BOUNCE_AFTER_DRAWDOWN_END -->",
        "<!-- DAILY_CHANGE_END -->",
        "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->",
    ]

    for anchor in preferred_anchors:
        pos = text.find(anchor)
        if pos != -1:
            insert_pos = pos + len(anchor)
            return text[:insert_pos] + "\n\n" + block + "\n\n" + text[insert_pos:]

    return text.rstrip() + "\n\n" + block + "\n"


def update_latest_report(block):
    if os.path.exists(MAIN_REPORT_PATH):
        with open(MAIN_REPORT_PATH, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    else:
        text = ""

    updated = update_marked_block(text, block)

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)


def main():
    ensure_reports_dir()

    generated_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    snapshot_date = generated_at[:10]
    generated_date = pd.to_datetime(snapshot_date)

    matches_by_target = {}
    all_tickers = set(TARGETS.keys())

    for target in TARGETS:
        matches = load_matches_for_target(target)
        matches_by_target[target] = matches

        if not matches.empty and "similar_asset" in matches.columns:
            all_tickers.update(matches["similar_asset"].dropna().astype(str).tolist())

    data = download_price_data(all_tickers)

    latest_rows = []
    snapshot_rows = []

    for target, matches in matches_by_target.items():
        short = asset_short(target)
        print(f"Costruzione cono {short}...")

        current_price = current_price_for_target(target, data)
        direction, positive_cases = direction_from_matches(matches)

        paths = build_path_matrix(matches, data)
        quant = quantile_paths(paths)

        if quant.empty or pd.isna(current_price):
            latest_rows.append({
                "target_ticker": target,
                "asset": short,
                "snapshot_date": snapshot_date,
                "current_price": current_price,
                "direction": direction,
                "positive_cases": positive_cases,
                "q30": None,
                "chart_filename": None,
            })
            continue

        quant_price = add_price_levels(quant, current_price)

        chart_path = plot_forecast_cone(
            target=target,
            quantiles_price=quant_price,
            current_price=current_price,
            generated_date=generated_date,
            data=data,
        )

        chart_filename = os.path.basename(chart_path) if chart_path else None

        q30_rows = quant_price[quant_price["day"] == FORECAST_DAYS]
        q30 = q30_rows.iloc[0].to_dict() if not q30_rows.empty else None

        latest_rows.append({
            "target_ticker": target,
            "asset": short,
            "snapshot_date": snapshot_date,
            "current_price": current_price,
            "direction": direction,
            "positive_cases": positive_cases,
            "q30": q30,
            "chart_filename": chart_filename,
        })

        asset_snapshot_rows = build_snapshot_rows(
            target=target,
            quantiles_price=quant_price,
            current_price=current_price,
            generated_at=generated_at,
        )
        snapshot_rows.extend(asset_snapshot_rows)

    latest_df = pd.DataFrame([
        {
            "snapshot_date": r["snapshot_date"],
            "asset": r["asset"],
            "target_ticker": r["target_ticker"],
            "current_price": r["current_price"],
            "direction": r["direction"],
            "positive_cases": r["positive_cases"],
            "chart_filename": r["chart_filename"],
            **({
                "p10_30d_price": r["q30"]["p10_price"],
                "p25_30d_price": r["q30"]["p25_price"],
                "p50_30d_price": r["q30"]["p50_price"],
                "p75_30d_price": r["q30"]["p75_price"],
                "p90_30d_price": r["q30"]["p90_price"],
                "p10_30d_pct": r["q30"]["p10_pct"],
                "p25_30d_pct": r["q30"]["p25_pct"],
                "p50_30d_pct": r["q30"]["p50_pct"],
                "p75_30d_pct": r["q30"]["p75_pct"],
                "p90_30d_pct": r["q30"]["p90_pct"],
            } if r["q30"] is not None else {})
        }
        for r in latest_rows
    ])
    latest_df.to_csv(LATEST_PATH, index=False)

    history = update_forecast_history(snapshot_rows)
    metrics = evaluate_forecast_history(history, data)
    metrics.to_csv(METRICS_PATH, index=False)

    report = build_report(generated_at, latest_rows, metrics)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    update_latest_report(report)

    print(report)
    print(f"Report salvato in {REPORT_PATH}")
    print(f"Latest salvato in {LATEST_PATH}")
    print(f"History salvata in {HISTORY_PATH}")
    print(f"Metrics salvate in {METRICS_PATH}")


if __name__ == "__main__":
    main()
