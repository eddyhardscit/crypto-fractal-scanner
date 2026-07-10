import os
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


REPORT_DIR = "reports"
MATCHES_PATH = os.path.join(REPORT_DIR, "latest_scanner_matches.csv")
REPORT_PATH = os.path.join(REPORT_DIR, "scanner_forecast_tracker_report.md")
SNAPSHOT_PATH = os.path.join(REPORT_DIR, "scanner_forecast_snapshots.csv")

ASSETS = ["BTC", "SOL", "DOGE"]
TARGET_TICKERS = {asset: f"{asset}-USD" for asset in ASSETS}
FORECAST_DAYS = 30
DISPLAY_HORIZONS = [1, 3, 7, 14, 30]


# -----------------------------
# helpers
# -----------------------------

def ensure_reports_dir():
    os.makedirs(REPORT_DIR, exist_ok=True)


def fmt_number_it(value, decimals=2):
    try:
        s = f"{float(value):,.{decimals}f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "n/a"


def fmt_pct(value, decimals=2):
    if pd.isna(value):
        return "n/a"
    return f"{fmt_number_it(value, decimals)}%"


def fmt_price(value):
    if pd.isna(value):
        return "n/a"
    return f"{fmt_number_it(value, 2)} $"


def load_matches():
    if not os.path.exists(MATCHES_PATH):
        return pd.DataFrame()
    try:
        df = pd.read_csv(MATCHES_PATH)
    except Exception:
        return pd.DataFrame()
    return df


def download_history(tickers, start_date, end_date):
    data = {}
    tickers = sorted(set(tickers))
    if not tickers:
        return data

    raw = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        interval="1d",
        auto_adjust=False,
        group_by="ticker",
        progress=False,
        threads=True,
    )

    if isinstance(raw.columns, pd.MultiIndex):
        for ticker in tickers:
            if ticker not in raw.columns.get_level_values(0):
                continue
            part = raw[ticker].copy()
            if "Close" not in part.columns:
                continue
            part = part[["Close"]].dropna().copy()
            part.index = pd.to_datetime(part.index).tz_localize(None)
            data[ticker] = part
    else:
        if "Close" in raw.columns and len(tickers) == 1:
            part = raw[["Close"]].dropna().copy()
            part.index = pd.to_datetime(part.index).tz_localize(None)
            data[tickers[0]] = part

    return data


def get_index_pos_on_or_after(index, dt):
    dt = pd.Timestamp(dt).tz_localize(None)
    pos = index.searchsorted(dt)
    if pos >= len(index):
        return None
    return int(pos)


def build_forward_path(close_series, start_dt, horizon=FORECAST_DAYS):
    if close_series is None or close_series.empty:
        return None
    idx = get_index_pos_on_or_after(close_series.index, start_dt)
    if idx is None:
        return None
    if idx + horizon >= len(close_series):
        return None

    base = float(close_series.iloc[idx])
    if base == 0 or np.isnan(base):
        return None

    future = close_series.iloc[idx: idx + horizon + 1].astype(float)
    returns = (future / base - 1.0) * 100.0
    returns.index = range(0, len(returns))
    return returns


def build_current_actual_path(close_series, anchor_date, horizon=FORECAST_DAYS):
    if close_series is None or close_series.empty:
        return None
    idx = get_index_pos_on_or_after(close_series.index, anchor_date)
    if idx is None:
        return None
    base = float(close_series.iloc[idx])
    if base == 0 or np.isnan(base):
        return None

    max_len = min(horizon, len(close_series) - 1 - idx)
    future = close_series.iloc[idx: idx + max_len + 1].astype(float)
    returns = (future / base - 1.0) * 100.0
    returns.index = range(0, len(returns))
    return returns


def build_path_matrix(asset_matches, history_map, horizon=FORECAST_DAYS):
    rows = []
    meta = []

    for _, row in asset_matches.iterrows():
        ticker = row.get("similar_asset")
        end_date = pd.to_datetime(row.get("end_date"), errors="coerce")
        if pd.isna(end_date):
            continue
        hist = history_map.get(ticker)
        if hist is None or hist.empty:
            continue
        path = build_forward_path(hist["Close"], end_date, horizon=horizon)
        if path is None or len(path) != horizon + 1:
            continue
        rows.append(path.values)
        meta.append(row)

    if not rows:
        return pd.DataFrame(), pd.DataFrame()

    matrix = pd.DataFrame(rows, columns=list(range(0, horizon + 1)))
    meta_df = pd.DataFrame(meta).reset_index(drop=True)
    return matrix, meta_df


def percentiles_from_matrix(matrix):
    if matrix.empty:
        return pd.DataFrame()

    out = []
    for day in matrix.columns:
        values = matrix[day].dropna().astype(float)
        if values.empty:
            continue
        out.append({
            "day": int(day),
            "p10": np.percentile(values, 10),
            "p25": np.percentile(values, 25),
            "p50": np.percentile(values, 50),
            "p75": np.percentile(values, 75),
            "p90": np.percentile(values, 90),
            "mean": values.mean(),
        })
    return pd.DataFrame(out)


def current_price_from_history(history_map, ticker):
    hist = history_map.get(ticker)
    if hist is None or hist.empty:
        return np.nan
    return float(hist["Close"].iloc[-1])


def positive_case_rate(asset_matches):
    if asset_matches.empty:
        return np.nan
    vals = pd.to_numeric(asset_matches.get("return_30d"), errors="coerce")
    vals = vals.dropna()
    if vals.empty:
        return np.nan
    return (vals > 0).mean() * 100.0


def save_snapshot_rows(snapshot_rows):
    new_df = pd.DataFrame(snapshot_rows)
    if new_df.empty:
        return

    if os.path.exists(SNAPSHOT_PATH):
        old = pd.read_csv(SNAPSHOT_PATH)
        all_df = pd.concat([old, new_df], ignore_index=True)
    else:
        all_df = new_df.copy()

    all_df["prediction_date"] = all_df["prediction_date"].astype(str)
    all_df["asset"] = all_df["asset"].astype(str)
    all_df["day"] = pd.to_numeric(all_df["day"], errors="coerce").fillna(0).astype(int)

    all_df = all_df.sort_values(["prediction_date", "asset", "day"])
    all_df = all_df.drop_duplicates(subset=["prediction_date", "asset", "day"], keep="last")
    all_df.to_csv(SNAPSHOT_PATH, index=False)


def compute_accuracy(history_map):
    if not os.path.exists(SNAPSHOT_PATH):
        return pd.DataFrame()

    snap = pd.read_csv(SNAPSHOT_PATH)
    if snap.empty:
        return pd.DataFrame()

    snap["prediction_date"] = pd.to_datetime(snap["prediction_date"], errors="coerce")
    snap["target_date"] = snap["prediction_date"] + pd.to_timedelta(pd.to_numeric(snap["day"], errors="coerce"), unit="D")

    rows = []
    today = pd.Timestamp.utcnow().tz_localize(None).normalize()

    for asset in ASSETS:
        ticker = TARGET_TICKERS[asset]
        hist = history_map.get(ticker)
        if hist is None or hist.empty:
            continue
        close_series = hist["Close"].copy()
        close_series.index = pd.to_datetime(close_series.index).tz_localize(None)

        asset_snap = snap[snap["asset"].astype(str) == asset].copy()
        if asset_snap.empty:
            continue

        for horizon in DISPLAY_HORIZONS:
            sub = asset_snap[asset_snap["day"] == horizon].copy()
            if sub.empty:
                rows.append({
                    "asset": asset,
                    "day_label": f"{horizon}g",
                    "checks": 0,
                    "inside_p10_p90": np.nan,
                    "inside_p25_p75": np.nan,
                    "abs_error_mean": np.nan,
                    "error_mean": np.nan,
                })
                continue

            results = []
            for _, row in sub.iterrows():
                pred_date = pd.Timestamp(row["prediction_date"]).normalize()
                tgt_date = pd.Timestamp(row["target_date"]).normalize()
                if tgt_date > today:
                    continue

                anchor_idx = get_index_pos_on_or_after(close_series.index, pred_date)
                target_idx = get_index_pos_on_or_after(close_series.index, tgt_date)
                if anchor_idx is None or target_idx is None:
                    continue
                if target_idx < anchor_idx:
                    continue

                base = float(close_series.iloc[anchor_idx])
                actual = float(close_series.iloc[target_idx])
                actual_ret = (actual / base - 1.0) * 100.0

                p10 = pd.to_numeric(row.get("p10"), errors="coerce")
                p25 = pd.to_numeric(row.get("p25"), errors="coerce")
                p50 = pd.to_numeric(row.get("p50"), errors="coerce")
                p75 = pd.to_numeric(row.get("p75"), errors="coerce")
                p90 = pd.to_numeric(row.get("p90"), errors="coerce")

                results.append({
                    "actual": actual_ret,
                    "inside_10_90": int(p10 <= actual_ret <= p90) if pd.notna(p10) and pd.notna(p90) else np.nan,
                    "inside_25_75": int(p25 <= actual_ret <= p75) if pd.notna(p25) and pd.notna(p75) else np.nan,
                    "abs_error": abs(actual_ret - p50) if pd.notna(p50) else np.nan,
                    "error": actual_ret - p50 if pd.notna(p50) else np.nan,
                })

            if not results:
                rows.append({
                    "asset": asset,
                    "day_label": f"{horizon}g",
                    "checks": 0,
                    "inside_p10_p90": np.nan,
                    "inside_p25_p75": np.nan,
                    "abs_error_mean": np.nan,
                    "error_mean": np.nan,
                })
            else:
                df = pd.DataFrame(results)
                rows.append({
                    "asset": asset,
                    "day_label": f"{horizon}g",
                    "checks": len(df),
                    "inside_p10_p90": df["inside_10_90"].mean() * 100.0,
                    "inside_p25_p75": df["inside_25_75"].mean() * 100.0,
                    "abs_error_mean": df["abs_error"].mean(),
                    "error_mean": df["error"].mean(),
                })

    return pd.DataFrame(rows)


def plot_forecast(asset, percentiles, actual_path, generated_at):
    if percentiles.empty:
        return None

    fig, ax = plt.subplots(figsize=(11, 6.5))
    x = percentiles["day"].values

    ax.fill_between(x, percentiles["p10"], percentiles["p90"], alpha=0.18, label="Banda larga p10-p90")
    ax.fill_between(x, percentiles["p25"], percentiles["p75"], alpha=0.28, label="Banda centrale p25-p75")
    ax.plot(x, percentiles["p50"], marker="o", linewidth=2.4, label="Scenario centrale p50")
    ax.plot(x, percentiles["p10"], linestyle="--", linewidth=1.2, label="p10")
    ax.plot(x, percentiles["p90"], linestyle="--", linewidth=1.2, label="p90")
    ax.plot(x, percentiles["mean"], linestyle=":", linewidth=1.8, label="Media")

    if actual_path is not None and len(actual_path) > 0:
        ax.plot(actual_path.index, actual_path.values, marker="o", linewidth=2.2, label=f"{asset} reale")

    ax.axhline(0, linewidth=0.8, linestyle=":")
    ax.set_title(f"{asset} — cono previsionale scanner 40 casi")
    ax.set_xlabel("Giorni da oggi")
    ax.set_ylabel("Return % dal giorno 0")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best", fontsize=9)

    subtitle = generated_at.strftime("Generato: %Y-%m-%d %H:%M UTC")
    fig.text(0.99, 0.01, subtitle, ha="right", va="bottom", fontsize=8)
    fig.tight_layout(rect=[0, 0.02, 1, 1])

    out = os.path.join(REPORT_DIR, f"scanner_forecast_{asset}.png")
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def build_report(asset_rows, accuracy_df, generated_at):
    lines = []
    lines.append("# Scanner forecast path / cono probabilistico")
    lines.append("")
    lines.append(f"Generato: {generated_at.strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")
    lines.append("Questo report costruisce il cono usando direttamente **i 40 match reali** del file `latest_scanner_matches.csv`, senza più leggere il markdown del report principale.")
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

    lines.append("## Ultimo cono previsionale salvato")
    lines.append("")
    lines.append("| Asset | Data | Prezzo iniziale | Direzione scanner | Casi positivi | P10 30g | P25 30g | P50 30g | P75 30g | P90 30g |")
    lines.append("|:------|:-----|----------------:|:------------------|--------------:|--------:|--------:|--------:|--------:|--------:|")
    for row in asset_rows:
        lines.append(
            f"| {row['asset']} | {row['date']} | {row['current_price_fmt']} | {row['direction']} | {row['positive_rate_fmt']} | {row['p10_30_fmt']} | {row['p25_30_fmt']} | {row['p50_30_fmt']} | {row['p75_30_fmt']} | {row['p90_30_fmt']} |"
        )
    lines.append("")

    lines.append("## Grafici")
    lines.append("")
    for row in asset_rows:
        lines.append(f"### {row['asset']}")
        lines.append("")
        lines.append(f"![Scanner forecast {row['asset']}](scanner_forecast_{row['asset']}.png)")
        lines.append("")

    if not accuracy_df.empty:
        lines.append("## Accuratezza percorso scanner")
        lines.append("")
        lines.append("| Asset | Giorno | Controlli | Dentro p10-p90 | Dentro p25-p75 | Errore medio abs vs p50 | Errore medio vs p50 |")
        lines.append("|:------|:-------|----------:|:---------------|:---------------|------------------------:|--------------------:|")
        for asset in ASSETS:
            sub = accuracy_df[accuracy_df["asset"] == asset]
            for _, row in sub.iterrows():
                lines.append(
                    f"| {asset} | {row['day_label']} | {int(row['checks'])} | {fmt_pct(row['inside_p10_p90'])} | {fmt_pct(row['inside_p25_p75'])} | {fmt_pct(row['abs_error_mean'])} | {fmt_pct(row['error_mean'])} |"
                )
        lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.")
    lines.append("- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.")
    lines.append("- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.")
    lines.append("- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.")
    lines.append("- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.")
    lines.append("")
    return "\n".join(lines)


def main():
    ensure_reports_dir()
    matches = load_matches()

    generated_at = datetime.now(timezone.utc)
    if matches.empty:
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write("# Scanner forecast path / cono probabilistico\n\nDati non disponibili.\n")
        return

    tickers_needed = set(matches["similar_asset"].dropna().astype(str).tolist())
    tickers_needed.update(TARGET_TICKERS.values())

    start_date = (generated_at - timedelta(days=5000)).strftime("%Y-%m-%d")
    end_date = (generated_at + timedelta(days=90)).strftime("%Y-%m-%d")
    history_map = download_history(tickers_needed, start_date, end_date)

    snapshot_rows = []
    asset_rows = []

    today = pd.Timestamp(generated_at).tz_localize(None).normalize()

    for asset in ASSETS:
        asset_matches = matches[matches["target_asset"].astype(str) == asset].copy()
        matrix, meta = build_path_matrix(asset_matches, history_map, horizon=FORECAST_DAYS)
        pct_df = percentiles_from_matrix(matrix)

        current_ticker = TARGET_TICKERS[asset]
        current_price = current_price_from_history(history_map, current_ticker)
        actual_path = build_current_actual_path(history_map.get(current_ticker, pd.DataFrame()).get("Close") if current_ticker in history_map else None, today, FORECAST_DAYS)
        if actual_path is None:
            hist = history_map.get(current_ticker)
            if hist is not None and not hist.empty:
                actual_path = pd.Series([0.0], index=[0])

        plot_forecast(asset, pct_df, actual_path, generated_at)

        if not pct_df.empty:
            for _, row in pct_df.iterrows():
                snapshot_rows.append({
                    "prediction_date": today.strftime("%Y-%m-%d"),
                    "asset": asset,
                    "day": int(row["day"]),
                    "p10": row["p10"],
                    "p25": row["p25"],
                    "p50": row["p50"],
                    "p75": row["p75"],
                    "p90": row["p90"],
                    "mean": row["mean"],
                    "current_price": current_price,
                })

        p30 = pct_df[pct_df["day"] == FORECAST_DAYS]
        if not p30.empty:
            p30 = p30.iloc[0]
            p10_30 = current_price * (1 + p30["p10"] / 100.0)
            p25_30 = current_price * (1 + p30["p25"] / 100.0)
            p50_30 = current_price * (1 + p30["p50"] / 100.0)
            p75_30 = current_price * (1 + p30["p75"] / 100.0)
            p90_30 = current_price * (1 + p30["p90"] / 100.0)
        else:
            p10_30 = p25_30 = p50_30 = p75_30 = p90_30 = np.nan

        pos_rate = positive_case_rate(asset_matches)
        if pd.isna(pos_rate):
            direction = "n/a"
        elif pos_rate >= 60:
            direction = "SALITA"
        elif pos_rate <= 40:
            direction = "DISCESA"
        else:
            direction = "INCERTO"

        asset_rows.append({
            "asset": asset,
            "date": today.strftime("%Y-%m-%d"),
            "current_price_fmt": fmt_price(current_price),
            "direction": direction,
            "positive_rate_fmt": fmt_pct(pos_rate),
            "p10_30_fmt": fmt_price(p10_30),
            "p25_30_fmt": fmt_price(p25_30),
            "p50_30_fmt": fmt_price(p50_30),
            "p75_30_fmt": fmt_price(p75_30),
            "p90_30_fmt": fmt_price(p90_30),
        })

    save_snapshot_rows(snapshot_rows)
    accuracy_df = compute_accuracy(history_map)
    report_md = build_report(asset_rows, accuracy_df, generated_at)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report_md)

    print(report_md)
    print(f"Report salvato in {REPORT_PATH}")


if __name__ == "__main__":
    main()
