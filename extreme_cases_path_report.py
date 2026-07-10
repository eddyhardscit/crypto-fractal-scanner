import os
import re
from datetime import datetime

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = "reports"
MAIN_REPORT_PATH = os.path.join(REPORTS_DIR, "latest_report.md")

START_MARKER = "<!-- EXTREME_CASES_PATH_START -->"
END_MARKER = "<!-- EXTREME_CASES_PATH_END -->"

REPORT_PATH = os.path.join(REPORTS_DIR, "extreme_cases_path_report.md")
SUMMARY_CSV_PATH = os.path.join(REPORTS_DIR, "extreme_cases_summary.csv")
TRIGGER_MATCHES_CSV_PATH = os.path.join(REPORTS_DIR, "extreme_cases_trigger_matches.csv")

FULL_MATCHES_PATH = os.path.join(REPORTS_DIR, "latest_scanner_matches.csv")

TARGETS = {
    "BTC-USD": "BTC",
    "SOL-USD": "SOL",
    "DOGE-USD": "DOGE",
}

THRESHOLD = 80.0
FORWARD_DAYS = 30
MATCH_LIMIT = 40
MAX_ASSET_LINES = 18


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
        print(f"{ticker}: errore normalizzazione dati: {e}")
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

        if not df.empty and len(df) > FORWARD_DAYS + 5:
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


def build_paths(matches, data):
    rows = []

    if matches.empty:
        return pd.DataFrame()

    required = {"similar_asset", "end_date"}

    if not required.issubset(matches.columns):
        return pd.DataFrame()

    for _, row in matches.iterrows():
        similar_asset = str(row.get("similar_asset", "")).strip()

        if similar_asset not in data:
            continue

        df = data[similar_asset].copy()
        pos = position_on_or_after(df, row.get("end_date"))

        if pos is None:
            continue

        if pos + FORWARD_DAYS >= len(df):
            continue

        base_price = float(df["Close"].iloc[pos])

        if base_price <= 0 or pd.isna(base_price):
            continue

        future = df["Close"].iloc[pos:pos + FORWARD_DAYS + 1].astype(float)
        pct_path = (future / base_price - 1.0) * 100.0

        if len(pct_path) < FORWARD_DAYS + 1:
            continue

        out = {
            "target": row.get("target", ""),
            "similar_asset": similar_asset,
            "start_date": row.get("start_date", ""),
            "end_date": row.get("end_date", ""),
            "similarity": pd.to_numeric(row.get("similarity", np.nan), errors="coerce"),
            "return_30d_report": pd.to_numeric(row.get("return_30d", np.nan), errors="coerce"),
            "drawdown_30d_report": pd.to_numeric(row.get("drawdown_30d", np.nan), errors="coerce"),
            "max_gain_30d_report": pd.to_numeric(row.get("max_gain_30d", np.nan), errors="coerce"),
        }

        for d in range(FORWARD_DAYS + 1):
            out[f"day_{d}"] = float(pct_path.iloc[d])

        out["return_path_30d"] = out[f"day_{FORWARD_DAYS}"]
        out["drawdown_path"] = min(out[f"day_{d}"] for d in range(FORWARD_DAYS + 1))
        out["max_gain_path"] = max(out[f"day_{d}"] for d in range(FORWARD_DAYS + 1))

        rows.append(out)

    return pd.DataFrame(rows)


def trigger_info(matches):
    if matches.empty or "return_30d" not in matches.columns:
        return {
            "trigger": False,
            "direction": "NESSUNO",
            "side": None,
            "positive_pct": np.nan,
            "negative_pct": np.nan,
            "trigger_pct": np.nan,
            "reason": "Dati insufficienti",
        }

    returns = pd.to_numeric(matches["return_30d"], errors="coerce").dropna()

    if len(returns) == 0:
        return {
            "trigger": False,
            "direction": "NESSUNO",
            "side": None,
            "positive_pct": np.nan,
            "negative_pct": np.nan,
            "trigger_pct": np.nan,
            "reason": "Dati insufficienti",
        }

    positive_pct = (returns > 0).mean() * 100.0
    negative_pct = 100.0 - positive_pct

    if positive_pct >= THRESHOLD:
        return {
            "trigger": True,
            "direction": "POSITIVO / RIALZISTA",
            "side": "positive",
            "positive_pct": positive_pct,
            "negative_pct": negative_pct,
            "trigger_pct": positive_pct,
            "reason": f"Casi positivi {fmt_pct(positive_pct)} >= {fmt_pct(THRESHOLD)}",
        }

    if negative_pct >= THRESHOLD:
        return {
            "trigger": True,
            "direction": "NEGATIVO / RIBASSISTA",
            "side": "negative",
            "positive_pct": positive_pct,
            "negative_pct": negative_pct,
            "trigger_pct": negative_pct,
            "reason": f"Casi negativi {fmt_pct(negative_pct)} >= {fmt_pct(THRESHOLD)}",
        }

    return {
        "trigger": False,
        "direction": "NESSUNO",
        "side": None,
        "positive_pct": positive_pct,
        "negative_pct": negative_pct,
        "trigger_pct": max(positive_pct, negative_pct),
        "reason": "Nessun lato sopra soglia estrema",
    }


def filter_trigger_paths(paths, side):
    if paths.empty:
        return paths

    if side == "positive":
        return paths[pd.to_numeric(paths["return_path_30d"], errors="coerce") > 0].copy()

    if side == "negative":
        return paths[pd.to_numeric(paths["return_path_30d"], errors="coerce") <= 0].copy()

    return pd.DataFrame()


def matrix_from_paths(paths):
    day_cols = [f"day_{d}" for d in range(FORWARD_DAYS + 1)]
    return paths[day_cols].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float)


def path_quantiles(paths):
    if paths.empty:
        return pd.DataFrame()

    matrix = matrix_from_paths(paths)
    rows = []

    for d in range(FORWARD_DAYS + 1):
        values = matrix[:, d]
        values = values[~np.isnan(values)]

        if len(values) == 0:
            continue

        rows.append({
            "day": d,
            "p10": np.percentile(values, 10),
            "p25": np.percentile(values, 25),
            "p50": np.percentile(values, 50),
            "p75": np.percentile(values, 75),
            "p90": np.percentile(values, 90),
            "mean": np.mean(values),
        })

    return pd.DataFrame(rows)


def plot_clean_bands(target, side, paths):
    short = asset_short(target)
    suffix = "positive" if side == "positive" else "negative"
    out_path = os.path.join(REPORTS_DIR, f"extreme_cases_{short}_{suffix}_clean_bands.png")

    q = path_quantiles(paths)

    if q.empty:
        return None

    fig, ax = plt.subplots(figsize=(12, 6))

    x = q["day"]

    ax.fill_between(x, q["p10"], q["p90"], alpha=0.16, label="Banda p10-p90")
    ax.fill_between(x, q["p25"], q["p75"], alpha=0.28, label="Banda p25-p75")
    ax.plot(x, q["p50"], linewidth=3, label="Mediana p50")
    ax.plot(x, q["mean"], linestyle="--", linewidth=2, label="Media")

    ax.axhline(0, linewidth=1, linestyle=":")
    ax.axvline(7, linewidth=1, linestyle=":", alpha=0.7)
    ax.axvline(14, linewidth=1, linestyle=":", alpha=0.7)
    ax.axvline(30, linewidth=1, linestyle=":", alpha=0.7)

    title_side = "rialzisti" if side == "positive" else "ribassisti"
    ax.set_title(f"{short} — percorso pulito dei casi storici {title_side}")
    ax.set_xlabel("Giorni dopo il match")
    ax.set_ylabel("Return dal giorno 0")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")

    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close(fig)

    return out_path


def asset_median_table(paths):
    if paths.empty:
        return pd.DataFrame()

    rows = []

    for asset, group in paths.groupby("similar_asset"):
        group = group.copy()

        row = {
            "similar_asset": asset,
            "cases": len(group),
            "best_similarity": pd.to_numeric(group["similarity"], errors="coerce").max(),
            "return_7d_median": pd.to_numeric(group["day_7"], errors="coerce").median(),
            "return_14d_median": pd.to_numeric(group["day_14"], errors="coerce").median(),
            "return_30d_median": pd.to_numeric(group["day_30"], errors="coerce").median(),
            "drawdown_median": pd.to_numeric(group["drawdown_path"], errors="coerce").median(),
            "max_gain_median": pd.to_numeric(group["max_gain_path"], errors="coerce").median(),
        }

        rows.append(row)

    out = pd.DataFrame(rows)

    if out.empty:
        return out

    out = out.sort_values(
        ["cases", "best_similarity"],
        ascending=[False, False]
    )

    return out


def plot_asset_medians(target, side, paths):
    short = asset_short(target)
    suffix = "positive" if side == "positive" else "negative"
    out_path = os.path.join(REPORTS_DIR, f"extreme_cases_{short}_{suffix}_asset_medians.png")

    if paths.empty:
        return None

    table = asset_median_table(paths)

    if table.empty:
        return None

    top_assets = table["similar_asset"].head(MAX_ASSET_LINES).tolist()

    fig, ax = plt.subplots(figsize=(13, 7))

    cmap = plt.get_cmap("tab20")
    x = np.arange(FORWARD_DAYS + 1)

    for i, asset in enumerate(top_assets):
        group = paths[paths["similar_asset"] == asset].copy()
        matrix = matrix_from_paths(group)
        median_path = np.nanmedian(matrix, axis=0)

        label = asset.replace("-USD", "")
        ax.plot(
            x,
            median_path,
            linewidth=2,
            color=cmap(i % 20),
            label=label,
        )

    other = paths[~paths["similar_asset"].isin(top_assets)].copy()

    if not other.empty:
        other_matrix = matrix_from_paths(other)
        other_median = np.nanmedian(other_matrix, axis=0)

        ax.plot(
            x,
            other_median,
            linewidth=3,
            linestyle="--",
            color="black",
            label="ALTRI aggregati",
        )

    total_matrix = matrix_from_paths(paths)
    total_median = np.nanmedian(total_matrix, axis=0)

    ax.plot(
        x,
        total_median,
        linewidth=4,
        color="dimgray",
        label="MEDIANA totale",
    )

    ax.axhline(0, linewidth=1, linestyle=":")
    ax.axvline(7, linewidth=1, linestyle=":", alpha=0.7)
    ax.axvline(14, linewidth=1, linestyle=":", alpha=0.7)
    ax.axvline(30, linewidth=1, linestyle=":", alpha=0.7)

    title_side = "rialzisti" if side == "positive" else "ribassisti"
    ax.set_title(f"{short} — linee colorate per asset storico nei casi {title_side}")
    ax.set_xlabel("Giorni dopo il match")
    ax.set_ylabel("Return dal giorno 0")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=8)

    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close(fig)

    return out_path


def plot_ranked_returns(target, side, paths):
    short = asset_short(target)
    suffix = "positive" if side == "positive" else "negative"
    out_path = os.path.join(REPORTS_DIR, f"extreme_cases_{short}_{suffix}_ranked_returns.png")

    if paths.empty:
        return None

    p = paths.copy()
    p["return_path_30d"] = pd.to_numeric(p["return_path_30d"], errors="coerce")
    p = p.dropna(subset=["return_path_30d"]).sort_values("return_path_30d")

    if p.empty:
        return None

    labels = [
        f"{a.replace('-USD', '')}\n{str(d)[:10]}"
        for a, d in zip(p["similar_asset"], p["end_date"])
    ]

    values = p["return_path_30d"].to_numpy(dtype=float)

    fig, ax = plt.subplots(figsize=(14, 6))

    colors = ["tab:red" if v < 0 else "tab:green" for v in values]
    ax.bar(range(len(values)), values, color=colors, alpha=0.75)

    ax.axhline(0, linewidth=1, color="black")
    ax.axhline(np.median(values), linestyle="--", linewidth=2, label="Mediana")
    ax.axhline(np.mean(values), linestyle=":", linewidth=2, label="Media")

    ax.set_title(f"{short} — return 30g ordinato dei casi estremi")
    ax.set_ylabel("Return 30 giorni")
    ax.set_xticks(range(len(values)))
    ax.set_xticklabels(labels, rotation=75, ha="right", fontsize=7)
    ax.grid(True, axis="y", alpha=0.25)
    ax.legend(loc="best")

    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close(fig)

    return out_path


def distribution_table(paths):
    values = pd.to_numeric(paths["return_path_30d"], errors="coerce").dropna()

    if values.empty:
        return pd.DataFrame()

    rows = [{
        "P10": fmt_pct(np.percentile(values, 10)),
        "P25": fmt_pct(np.percentile(values, 25)),
        "P50": fmt_pct(np.percentile(values, 50)),
        "P75": fmt_pct(np.percentile(values, 75)),
        "P90": fmt_pct(np.percentile(values, 90)),
    }]

    return pd.DataFrame(rows)


def trigger_summary_row(target, info, matches, trigger_paths):
    return {
        "Asset": asset_short(target),
        "Direzione": info["direction"],
        "Trigger": "SI" if info["trigger"] else "NO",
        "Percentuale": fmt_pct(info["trigger_pct"]),
        "Motivo": info["reason"],
        "Match disponibili": len(matches),
        "Casi usati nel grafico": len(trigger_paths) if info["trigger"] else 0,
    }


def raw_summary_csv_row(target, info, matches, trigger_paths):
    return {
        "asset": asset_short(target),
        "target": target,
        "trigger": info["trigger"],
        "direction": info["direction"],
        "side": info["side"],
        "positive_pct": info["positive_pct"],
        "negative_pct": info["negative_pct"],
        "trigger_pct": info["trigger_pct"],
        "matches_available": len(matches),
        "trigger_cases": len(trigger_paths) if info["trigger"] else 0,
    }


def format_matches_table(paths, limit=20):
    if paths.empty:
        return pd.DataFrame()

    cols = [
        "similar_asset",
        "start_date",
        "end_date",
        "similarity",
        "return_30d_report",
        "drawdown_30d_report",
        "max_gain_30d_report",
        "return_path_30d",
    ]

    available = [c for c in cols if c in paths.columns]
    out = paths[available].copy()

    if "similarity" in out.columns:
        out["similarity"] = pd.to_numeric(out["similarity"], errors="coerce")
        out = out.sort_values("similarity", ascending=False)

    out = out.head(limit)

    rename = {
        "similar_asset": "Asset storico",
        "start_date": "Start",
        "end_date": "End",
        "similarity": "Similarity",
        "return_30d_report": "Return 30g report",
        "drawdown_30d_report": "Drawdown report",
        "max_gain_30d_report": "Max gain report",
        "return_path_30d": "Return path calcolato",
    }

    out = out.rename(columns=rename)

    for c in [
        "Similarity",
        "Return 30g report",
        "Drawdown report",
        "Max gain report",
        "Return path calcolato",
    ]:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce").map(lambda x: fmt_pct(x) if not pd.isna(x) else "n/a")

    return out


def contrary_cases_table(all_paths, side):
    if all_paths.empty:
        return pd.DataFrame()

    p = all_paths.copy()
    p["return_path_30d"] = pd.to_numeric(p["return_path_30d"], errors="coerce")

    if side == "negative":
        contrary = p[p["return_path_30d"] > 0].copy()
    elif side == "positive":
        contrary = p[p["return_path_30d"] <= 0].copy()
    else:
        return pd.DataFrame()

    if contrary.empty:
        return pd.DataFrame()

    contrary = contrary.sort_values("return_path_30d", ascending=False)

    out = contrary[[
        "similar_asset",
        "end_date",
        "similarity",
        "return_path_30d",
        "drawdown_path",
        "max_gain_path",
    ]].head(10).copy()

    out = out.rename(columns={
        "similar_asset": "Asset storico",
        "end_date": "End",
        "similarity": "Similarity",
        "return_path_30d": "Return 30g",
        "drawdown_path": "Drawdown",
        "max_gain_path": "Max gain",
    })

    for c in ["Similarity", "Return 30g", "Drawdown", "Max gain"]:
        out[c] = pd.to_numeric(out[c], errors="coerce").map(lambda x: fmt_pct(x) if not pd.isna(x) else "n/a")

    return out


def format_asset_medians_for_report(paths):
    table = asset_median_table(paths)

    if table.empty:
        return table

    table = table.head(MAX_ASSET_LINES).copy()

    table = table.rename(columns={
        "similar_asset": "Asset storico",
        "cases": "Casi",
        "best_similarity": "Best similarity",
        "return_7d_median": "Return mediano 7g",
        "return_14d_median": "Return mediano 14g",
        "return_30d_median": "Return mediano 30g",
        "drawdown_median": "Drawdown mediano",
        "max_gain_median": "Max gain mediano",
    })

    for c in [
        "Best similarity",
        "Return mediano 7g",
        "Return mediano 14g",
        "Return mediano 30g",
        "Drawdown mediano",
        "Max gain mediano",
    ]:
        table[c] = pd.to_numeric(table[c], errors="coerce").map(lambda x: fmt_pct(x) if not pd.isna(x) else "n/a")

    return table


def build_report(generated_at, summaries, trigger_sections):
    lines = []

    lines.append(START_MARKER)
    lines.append("# Extreme cases path report")
    lines.append("")
    lines.append(f"Generato: {generated_at} UTC")
    lines.append("")
    lines.append(
        "Questo report crea grafici solo quando lo scanner mostra una percentuale estrema: "
        f"casi positivi o negativi almeno pari a **{fmt_pct(THRESHOLD, 0)}**."
    )
    lines.append("")
    lines.append(
        "Obiettivo: non guardare solo la percentuale finale, ma vedere **come si sono mossi dopo** "
        "i casi storici simili."
    )
    lines.append("")
    lines.append("Fonte match: **CSV completo: latest_scanner_matches.csv**, con fallback sui file `BTC_matches.csv`, `SOL_matches.csv`, `DOGE_matches.csv`.")
    lines.append("")
    lines.append("## Trigger estremi")
    lines.append("")

    summary_table = pd.DataFrame(summaries)

    if summary_table.empty:
        lines.append("Nessun dato disponibile.")
    else:
        lines.append(summary_table.to_markdown(index=False))

    lines.append("")

    if not trigger_sections:
        lines.append("## Nessun caso estremo attivo")
        lines.append("")
        lines.append(
            "Oggi nessun asset ha casi positivi o negativi sopra la soglia estrema. "
            "Il report non crea grafici extra."
        )
        lines.append(END_MARKER)
        return "\n".join(lines)

    for section in trigger_sections:
        target = section["target"]
        short = asset_short(target)
        side = section["side"]
        paths = section["trigger_paths"]
        all_paths = section["all_paths"]
        info = section["info"]

        title_side = "rialzisti" if side == "positive" else "ribassisti"

        lines.append(f"## {short} — casi {title_side}")
        lines.append("")
        lines.append(f"- Trigger: **{info['reason']}**")
        lines.append(f"- Casi disponibili: **{len(section['matches'])}**")
        lines.append(f"- Casi usati nei grafici: **{len(paths)}**")
        lines.append("")

        if paths.empty:
            lines.append("Dati insufficienti per costruire i percorsi.")
            lines.append("")
            continue

        values_7 = pd.to_numeric(paths["day_7"], errors="coerce")
        values_14 = pd.to_numeric(paths["day_14"], errors="coerce")
        values_30 = pd.to_numeric(paths["day_30"], errors="coerce")
        drawdowns = pd.to_numeric(paths["drawdown_path"], errors="coerce")
        max_gains = pd.to_numeric(paths["max_gain_path"], errors="coerce")

        lines.append(f"- Return mediano 7g: **{fmt_pct(values_7.median())}**")
        lines.append(f"- Return mediano 14g: **{fmt_pct(values_14.median())}**")
        lines.append(f"- Return mediano 30g: **{fmt_pct(values_30.median())}**")
        lines.append(f"- Return medio 30g: **{fmt_pct(values_30.mean())}**")
        lines.append(f"- Drawdown mediano durante il percorso: **{fmt_pct(drawdowns.median())}**")
        lines.append(f"- Max gain mediano durante il percorso: **{fmt_pct(max_gains.median())}**")
        lines.append("")

        lines.append("### Distribuzione 30 giorni")
        lines.append("")

        dist = distribution_table(paths)

        if not dist.empty:
            lines.append(dist.to_markdown(index=False))
            lines.append("")

        clean_img = section.get("clean_img")
        asset_img = section.get("asset_img")
        ranked_img = section.get("ranked_img")

        lines.append("### Grafico pulito: bande + mediana")
        lines.append("")
        if clean_img:
            lines.append(f"![Extreme clean {short}]({clean_img})")
        else:
            lines.append("Grafico non disponibile.")
        lines.append("")

        lines.append("### Grafico asset per asset")
        lines.append("")
        lines.append(
            "Qui non vengono più mostrate 40 linee casuali tutte insieme. "
            "Ogni linea colorata rappresenta la mediana di un asset storico. "
            "Se gli asset sono troppi, i meno importanti vengono aggregati in `ALTRI`."
        )
        lines.append("")
        if asset_img:
            lines.append(f"![Extreme asset medians {short}]({asset_img})")
        else:
            lines.append("Grafico non disponibile.")
        lines.append("")

        lines.append("### Grafico casi ordinati per risultato finale")
        lines.append("")
        if ranked_img:
            lines.append(f"![Extreme ranked {short}]({ranked_img})")
        else:
            lines.append("Grafico non disponibile.")
        lines.append("")

        lines.append("### Tabella asset storici aggregati")
        lines.append("")
        asset_table = format_asset_medians_for_report(paths)

        if not asset_table.empty:
            lines.append(asset_table.to_markdown(index=False))
        else:
            lines.append("Nessun dato aggregabile.")
        lines.append("")

        contrary = contrary_cases_table(all_paths, side)

        lines.append("### Casi contrari da non ignorare")
        lines.append("")

        if contrary.empty:
            lines.append(
                "Non ci sono casi contrari rilevanti dentro i 40 match usati."
            )
        else:
            if side == "negative":
                lines.append(
                    "Questi sono i casi che, nonostante il trigger ribassista, finirono positivi. "
                    "Sono le eccezioni da guardare per capire perché alcune linee salivano nel vecchio grafico."
                )
            else:
                lines.append(
                    "Questi sono i casi che, nonostante il trigger rialzista, finirono negativi. "
                    "Sono le eccezioni da guardare per capire il rischio."
                )
            lines.append("")
            lines.append(contrary.to_markdown(index=False))

        lines.append("")

        lines.append("### Match individuali usati")
        lines.append("")
        match_table = format_matches_table(paths, limit=20)

        if match_table.empty:
            lines.append("Nessun match individuale disponibile.")
        else:
            lines.append(match_table.to_markdown(index=False))

        lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- **Grafico pulito**: guarda prima questo. Ti dice la traiettoria centrale senza casino.")
    lines.append("- **Grafico asset per asset**: mostra se la discesa/salita è comune a più asset o dipende solo da pochi casi.")
    lines.append("- **Grafico casi ordinati**: mostra quanto sono dispersi i risultati finali a 30 giorni.")
    lines.append("- **Casi contrari**: sono le eccezioni. Servono per non trasformare una statistica forte in una certezza falsa.")
    lines.append("")
    lines.append(
        "Nota: questo report è visivo e diagnostico. Non modifica il Global Confluence e non autorizza leva."
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
        "<!-- SCANNER_FORECAST_TRACKER_END -->",
        "<!-- BOUNCE_AFTER_DRAWDOWN_END -->",
        "<!-- DAILY_CHANGE_END -->",
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

    matches_by_target = {}
    all_tickers = set()

    for target in TARGETS:
        matches = load_matches_for_target(target)
        matches_by_target[target] = matches

        if not matches.empty and "similar_asset" in matches.columns:
            all_tickers.update(matches["similar_asset"].dropna().astype(str).tolist())

    data = download_price_data(all_tickers)

    summaries = []
    raw_summary_rows = []
    trigger_sections = []
    all_trigger_rows = []

    for target, matches in matches_by_target.items():
        print(f"Controllo casi estremi {asset_short(target)}...")

        info = trigger_info(matches)
        all_paths = build_paths(matches, data)

        trigger_paths = pd.DataFrame()

        if info["trigger"]:
            trigger_paths = filter_trigger_paths(all_paths, info["side"])

        summaries.append(
            trigger_summary_row(target, info, matches, trigger_paths)
        )
        raw_summary_rows.append(
            raw_summary_csv_row(target, info, matches, trigger_paths)
        )

        if not trigger_paths.empty:
            side = info["side"]

            clean_path = plot_clean_bands(target, side, trigger_paths)
            asset_path = plot_asset_medians(target, side, trigger_paths)
            ranked_path = plot_ranked_returns(target, side, trigger_paths)

            clean_img = os.path.basename(clean_path) if clean_path else None
            asset_img = os.path.basename(asset_path) if asset_path else None
            ranked_img = os.path.basename(ranked_path) if ranked_path else None

            temp = trigger_paths.copy()
            temp["target"] = target
            temp["asset"] = asset_short(target)
            temp["trigger_side"] = side
            all_trigger_rows.append(temp)

            trigger_sections.append({
                "target": target,
                "side": side,
                "info": info,
                "matches": matches,
                "all_paths": all_paths,
                "trigger_paths": trigger_paths,
                "clean_img": clean_img,
                "asset_img": asset_img,
                "ranked_img": ranked_img,
            })

    pd.DataFrame(raw_summary_rows).to_csv(SUMMARY_CSV_PATH, index=False)

    if all_trigger_rows:
        pd.concat(all_trigger_rows, ignore_index=True).to_csv(
            TRIGGER_MATCHES_CSV_PATH,
            index=False,
        )
    else:
        pd.DataFrame().to_csv(TRIGGER_MATCHES_CSV_PATH, index=False)

    report = build_report(generated_at, summaries, trigger_sections)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    update_latest_report(report)

    print(report)
    print(f"Report salvato in {REPORT_PATH}")
    print(f"Summary salvato in {SUMMARY_CSV_PATH}")
    print(f"Trigger matches salvati in {TRIGGER_MATCHES_CSV_PATH}")


if __name__ == "__main__":
    main()
