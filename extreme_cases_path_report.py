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
REPORT_PATH = os.path.join(REPORT_DIR, "extreme_cases_path_report.md")
ASSETS = ["BTC", "SOL", "DOGE"]
FORECAST_DAYS = 30
THRESHOLD = 80.0
TOP_CASES_TO_PLOT = 12
TARGET_TICKERS = {asset: f"{asset}-USD" for asset in ASSETS}


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


def load_matches():
    if not os.path.exists(MATCHES_PATH):
        return pd.DataFrame()
    try:
        return pd.read_csv(MATCHES_PATH)
    except Exception:
        return pd.DataFrame()


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


def classify_asset(asset_matches):
    vals = pd.to_numeric(asset_matches.get("return_30d"), errors="coerce").dropna()
    if vals.empty:
        return None
    pos_rate = (vals > 0).mean() * 100.0
    neg_rate = (vals < 0).mean() * 100.0

    if pos_rate >= THRESHOLD:
        return {
            "direction": "rialzisti",
            "side": "positive",
            "label": "casi rialzisti",
            "rate": pos_rate,
            "mask": vals > 0,
        }

    if neg_rate >= THRESHOLD:
        return {
            "direction": "ribassisti",
            "side": "negative",
            "label": "casi ribassisti",
            "rate": neg_rate,
            "mask": vals < 0,
        }

    return None


def percentiles_table(values):
    if values.empty:
        return None
    return {
        10: np.percentile(values, 10),
        25: np.percentile(values, 25),
        50: np.percentile(values, 50),
        75: np.percentile(values, 75),
        90: np.percentile(values, 90),
    }


def plot_clean_corridor(asset, direction, matrix, out_path):
    fig, ax = plt.subplots(figsize=(11, 6.3))
    x = matrix.columns.astype(int)

    p10 = matrix.quantile(0.10, axis=0)
    p25 = matrix.quantile(0.25, axis=0)
    p50 = matrix.quantile(0.50, axis=0)
    p75 = matrix.quantile(0.75, axis=0)
    p90 = matrix.quantile(0.90, axis=0)
    mean = matrix.mean(axis=0)

    ax.fill_between(x, p10, p90, alpha=0.18, label="Banda p10-p90")
    ax.fill_between(x, p25, p75, alpha=0.28, label="Banda p25-p75")
    ax.plot(x, p50, linewidth=2.8, label="Mediana p50")
    ax.plot(x, mean, linestyle="--", linewidth=2.0, label="Media")
    ax.axhline(0, linewidth=0.8, linestyle=":")
    ax.grid(True, alpha=0.25)
    ax.set_title(f"{asset} — percorso sintetico dei casi storici {direction}")
    ax.set_xlabel("Giorni dopo il match")
    ax.set_ylabel("Return % dal giorno 0")
    ax.legend(loc="best", fontsize=9)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_top_cases(asset, direction, matrix, meta_df, out_path, top_n=TOP_CASES_TO_PLOT):
    if matrix.empty or meta_df.empty:
        return []

    order = np.argsort(pd.to_numeric(meta_df["similarity"], errors="coerce").fillna(9999).values)
    matrix = matrix.iloc[order].reset_index(drop=True)
    meta_df = meta_df.iloc[order].reset_index(drop=True)

    n = min(top_n, len(matrix))
    matrix = matrix.head(n)
    meta_df = meta_df.head(n)

    colors = plt.get_cmap("tab20")(np.linspace(0, 1, max(n, 2)))

    fig, ax = plt.subplots(figsize=(12, 7))
    x = matrix.columns.astype(int)
    legend_rows = []

    for i in range(n):
        y = matrix.iloc[i].values.astype(float)
        end_ret = y[-1]
        similar_asset = str(meta_df.loc[i, "similar_asset"])
        end_date = pd.to_datetime(meta_df.loc[i, "end_date"], errors="coerce")
        end_date_txt = end_date.strftime("%Y-%m-%d") if pd.notna(end_date) else "n/a"
        similarity = pd.to_numeric(meta_df.loc[i, "similarity"], errors="coerce")
        label = f"{i+1}. {similar_asset} {end_date_txt} | sim {fmt_number_it(similarity, 4)} | 30g {fmt_pct(end_ret)}"
        ax.plot(x, y, linewidth=2.0, color=colors[i], label=label)
        ax.scatter([x[-1]], [y[-1]], color=[colors[i]], s=28)
        legend_rows.append({
            "rank": i + 1,
            "similar_asset": similar_asset,
            "end_date": end_date_txt,
            "similarity": similarity,
            "return_30d": end_ret,
        })

    ax.axhline(0, linewidth=0.8, linestyle=":")
    ax.grid(True, alpha=0.25)
    ax.set_title(f"{asset} — top {n} casi storici {direction} (linee separate)")
    ax.set_xlabel("Giorni dopo il match")
    ax.set_ylabel("Return % dal giorno 0")
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=8, frameon=True)

    fig.tight_layout(rect=[0, 0, 0.78, 1])
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return legend_rows


def plot_distribution(asset, direction, values, out_path):
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.hist(values.values.astype(float), bins=min(12, max(5, len(values) // 2)), alpha=0.8)
    ax.axvline(np.median(values), linestyle="--", linewidth=2, label="Mediana")
    ax.axvline(np.mean(values), linestyle=":", linewidth=2, label="Media")
    ax.grid(True, alpha=0.25)
    ax.set_title(f"{asset} — distribuzione return 30g dei casi {direction}")
    ax.set_xlabel("Return 30 giorni (%)")
    ax.set_ylabel("Numero casi")
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def build_report(trigger_rows, generated_at):
    lines = []
    lines.append("# Extreme cases path report")
    lines.append("")
    lines.append(f"Generato: {generated_at.strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")
    lines.append(f"La sezione si attiva quando almeno **{fmt_pct(THRESHOLD, 0)}** dei 40 casi puliti dello scanner punta nella stessa direzione a 30 giorni.")
    lines.append("")

    if not trigger_rows:
        lines.append("Nessun asset supera la soglia prevista, quindi il report estremo oggi non viene prodotto.")
        lines.append("")
        return "\n".join(lines)

    for item in trigger_rows:
        asset = item["asset"]
        direction = item["direction"]
        lines.append(f"## {asset}")
        lines.append("")
        lines.append(f"- Direzione dominante: **{direction.upper()}**")
        lines.append(f"- Percentuale direzionale: **{fmt_pct(item['rate'])}**")
        lines.append(f"- Match totali filtrati: **{item['num_cases']}**")
        lines.append(f"- Casi visualizzati con linee separate: **{item['displayed_cases']}**")
        lines.append(f"- Drawdown mediano durante il percorso: **{fmt_pct(item['drawdown_median'])}**")
        lines.append(f"- Max gain mediano durante il percorso: **{fmt_pct(item['max_gain_median'])}**")
        lines.append("")

        lines.append("### Distribuzione 30 giorni")
        lines.append("")
        lines.append("| P10 | P25 | P50 | P75 | P90 |")
        lines.append("|----:|----:|----:|----:|----:|")
        lines.append(
            f"| {fmt_pct(item['pct'][10])} | {fmt_pct(item['pct'][25])} | {fmt_pct(item['pct'][50])} | {fmt_pct(item['pct'][75])} | {fmt_pct(item['pct'][90])} |"
        )
        lines.append("")

        lines.append("### Grafico pulito di sintesi")
        lines.append("")
        lines.append(f"![{asset} clean corridor]({item['clean_file']})")
        lines.append("")

        lines.append("### Top casi separati con colori diversi")
        lines.append("")
        lines.append(f"![{asset} top cases]({item['top_file']})")
        lines.append("")

        lines.append("### Istogramma distribuzione return 30g")
        lines.append("")
        lines.append(f"![{asset} distribution]({item['hist_file']})")
        lines.append("")

        if item["legend_rows"]:
            lines.append("### Casi mostrati nel grafico a linee")
            lines.append("")
            lines.append("| # | Asset storico | Data match | Similarità | Return 30g |")
            lines.append("|--:|:--------------|:-----------|-----------:|-----------:|")
            for row in item["legend_rows"]:
                lines.append(
                    f"| {row['rank']} | {row['similar_asset']} | {row['end_date']} | {fmt_number_it(row['similarity'], 4)} | {fmt_pct(row['return_30d'])} |"
                )
            lines.append("")

        lines.append("### Come leggerlo")
        lines.append("")
        lines.append("- Il **grafico pulito** mostra solo il corridoio statistico, senza spaghetti plot confuso.")
        lines.append("- Il **grafico top casi** mostra solo i casi più simili, ciascuno con colore diverso, per vedere meglio chi sale e chi scende.")
        lines.append("- L'**istogramma** riassume dove cadono i return a 30 giorni.")
        lines.append("- Usa il grafico pulito per il quadro generale e quello a linee colorate per il confronto caso per caso.")
        lines.append("")

    return "\n".join(lines)


def main():
    ensure_reports_dir()
    matches = load_matches()
    generated_at = datetime.now(timezone.utc)

    if matches.empty:
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write("# Extreme cases path report\n\nDati non disponibili.\n")
        return

    tickers_needed = set(matches["similar_asset"].dropna().astype(str).tolist())
    start_date = (generated_at - timedelta(days=5000)).strftime("%Y-%m-%d")
    end_date = (generated_at + timedelta(days=90)).strftime("%Y-%m-%d")
    history_map = download_history(tickers_needed, start_date, end_date)

    trigger_rows = []

    for asset in ASSETS:
        asset_matches = matches[matches["target_asset"].astype(str) == asset].copy().reset_index(drop=True)
        if asset_matches.empty:
            continue

        cls = classify_asset(asset_matches)
        if cls is None:
            continue

        vals = pd.to_numeric(asset_matches["return_30d"], errors="coerce")
        if cls["side"] == "positive":
            chosen = asset_matches[vals > 0].copy().reset_index(drop=True)
        else:
            chosen = asset_matches[vals < 0].copy().reset_index(drop=True)

        if chosen.empty:
            continue

        matrix, meta_df = build_path_matrix(chosen, history_map, horizon=FORECAST_DAYS)
        if matrix.empty:
            continue

        ret30 = pd.to_numeric(chosen["return_30d"], errors="coerce").dropna()
        dd30 = pd.to_numeric(chosen["drawdown_30d"], errors="coerce").dropna()
        mg30 = pd.to_numeric(chosen["max_gain_30d"], errors="coerce").dropna()
        pct = percentiles_table(ret30)
        if pct is None:
            continue

        clean_file = f"extreme_cases_{asset}_{cls['side']}_clean.png"
        top_file = f"extreme_cases_{asset}_{cls['side']}_top_cases.png"
        hist_file = f"extreme_cases_{asset}_{cls['side']}_distribution.png"

        plot_clean_corridor(asset, cls["label"], matrix, os.path.join(REPORT_DIR, clean_file))
        legend_rows = plot_top_cases(asset, cls["label"], matrix, meta_df, os.path.join(REPORT_DIR, top_file), top_n=TOP_CASES_TO_PLOT)
        plot_distribution(asset, cls["label"], ret30, os.path.join(REPORT_DIR, hist_file))

        trigger_rows.append({
            "asset": asset,
            "direction": cls["label"],
            "rate": cls["rate"],
            "num_cases": len(chosen),
            "displayed_cases": min(TOP_CASES_TO_PLOT, len(chosen)),
            "drawdown_median": dd30.median() if not dd30.empty else np.nan,
            "max_gain_median": mg30.median() if not mg30.empty else np.nan,
            "pct": pct,
            "clean_file": clean_file,
            "top_file": top_file,
            "hist_file": hist_file,
            "legend_rows": legend_rows,
        })

    report_md = build_report(trigger_rows, generated_at)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report_md)

    print(report_md)
    print(f"Report salvato in {REPORT_PATH}")


if __name__ == "__main__":
    main()
