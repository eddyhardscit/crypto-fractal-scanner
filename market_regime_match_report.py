import os
from pathlib import Path
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")

OUTPUT_REPORT = REPORTS_DIR / "market_regime_match_report.md"
OUTPUT_MATCHES = REPORTS_DIR / "market_regime_match_matches.csv"
OUTPUT_SUMMARY = REPORTS_DIR / "market_regime_match_summary.csv"

LATEST_REPORT = REPORTS_DIR / "latest_report.md"

START_MARKER = "<!-- MARKET_REGIME_MATCH_START -->"
END_MARKER = "<!-- MARKET_REGIME_MATCH_END -->"

BTC_TICKER = "BTC-USD"

REQUIRED_MATCH_COLUMNS = [
    "target",
    "similar_asset",
    "start_date",
    "end_date",
    "similarity",
    "return_7d",
    "drawdown_7d",
    "max_gain_7d",
    "return_14d",
    "drawdown_14d",
    "max_gain_14d",
    "return_30d",
    "drawdown_30d",
    "max_gain_30d",
    "return_60d",
    "drawdown_60d",
    "max_gain_60d",
]


def safe_float(x):
    try:
        if pd.isna(x):
            return np.nan
        return float(x)
    except Exception:
        return np.nan


def fmt_pct(x):
    x = safe_float(x)
    if pd.isna(x):
        return "n/a"
    return f"{x:.2f}%"


def fmt_num(x):
    x = safe_float(x)
    if pd.isna(x):
        return "n/a"
    return f"{x:.2f}"


def df_to_markdown(df):
    if df is None or df.empty:
        return "_No data._"

    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


def normalize_index(series):
    s = series.copy()
    idx = pd.to_datetime(s.index)

    try:
        if idx.tz is not None:
            idx = idx.tz_convert(None)
    except Exception:
        pass

    idx = idx.normalize()
    s.index = idx
    s = s[~s.index.duplicated(keep="last")]
    s = s.sort_index()
    return s.dropna()


def extract_close_series(data, ticker):
    if data is None or data.empty:
        return pd.Series(dtype=float)

    if isinstance(data.columns, pd.MultiIndex):
        for field in ["Adj Close", "Close"]:
            if field in data.columns.get_level_values(0):
                tmp = data.xs(field, axis=1, level=0)
                if ticker in tmp.columns:
                    return normalize_index(tmp[ticker])
                return normalize_index(tmp.iloc[:, 0])

        for field in ["Adj Close", "Close"]:
            if field in data.columns.get_level_values(-1):
                tmp = data.xs(field, axis=1, level=-1)
                if ticker in tmp.columns:
                    return normalize_index(tmp[ticker])
                return normalize_index(tmp.iloc[:, 0])

        return pd.Series(dtype=float)

    for col in ["Adj Close", "Close"]:
        if col in data.columns:
            return normalize_index(data[col])

    return pd.Series(dtype=float)


def download_close(ticker):
    try:
        data = yf.download(
            ticker,
            period="max",
            interval="1d",
            progress=False,
            auto_adjust=False,
            actions=False,
            threads=False,
        )
        close = extract_close_series(data, ticker)
        return close
    except Exception as e:
        print(f"Download failed for {ticker}: {e}")
        return pd.Series(dtype=float)


def build_history(close):
    if close is None or close.empty:
        return None

    close = close.dropna().sort_index()

    hist = pd.DataFrame(index=close.index)
    hist["close"] = close
    hist["ma50"] = close.rolling(50, min_periods=30).mean()
    hist["ma200"] = close.rolling(200, min_periods=120).mean()

    return hist


def value_on_or_before(series, date):
    if series is None or series.empty:
        return np.nan

    date = pd.Timestamp(date).normalize()
    tmp = series.loc[series.index <= date].dropna()

    if tmp.empty:
        return np.nan

    return safe_float(tmp.iloc[-1])


def date_on_or_before(series, date):
    if series is None or series.empty:
        return pd.NaT

    date = pd.Timestamp(date).normalize()
    tmp = series.loc[series.index <= date].dropna()

    if tmp.empty:
        return pd.NaT

    return tmp.index[-1]


def pct_return_from_days(series, date, days):
    if series is None or series.empty:
        return np.nan

    date = pd.Timestamp(date).normalize()
    current = value_on_or_before(series, date)
    past = value_on_or_before(series, date - pd.Timedelta(days=days))

    if pd.isna(current) or pd.isna(past) or past == 0:
        return np.nan

    return (current / past - 1.0) * 100.0


def metrics_at_date(hist, date=None):
    if hist is None or hist.empty:
        return {
            "date_used": "",
            "price": np.nan,
            "ma50": np.nan,
            "ma200": np.nan,
            "above_ma200": False,
            "ma200_slope_60d": np.nan,
            "return_90d": np.nan,
            "return_365d": np.nan,
            "regime": "UNKNOWN",
        }

    if date is None:
        date = hist.index[-1]

    date = pd.Timestamp(date).normalize()

    used_date = date_on_or_before(hist["close"], date)
    if pd.isna(used_date):
        return {
            "date_used": "",
            "price": np.nan,
            "ma50": np.nan,
            "ma200": np.nan,
            "above_ma200": False,
            "ma200_slope_60d": np.nan,
            "return_90d": np.nan,
            "return_365d": np.nan,
            "regime": "UNKNOWN",
        }

    price = value_on_or_before(hist["close"], used_date)
    ma50 = value_on_or_before(hist["ma50"], used_date)
    ma200 = value_on_or_before(hist["ma200"], used_date)

    ma200_old = value_on_or_before(hist["ma200"], used_date - pd.Timedelta(days=60))

    if pd.isna(ma200) or pd.isna(ma200_old) or ma200_old == 0:
        ma200_slope_60d = np.nan
    else:
        ma200_slope_60d = (ma200 / ma200_old - 1.0) * 100.0

    ret_90d = pct_return_from_days(hist["close"], used_date, 90)
    ret_365d = pct_return_from_days(hist["close"], used_date, 365)

    above_ma200 = False
    if not pd.isna(price) and not pd.isna(ma200):
        above_ma200 = price >= ma200

    regime = classify_regime(
        price=price,
        ma200=ma200,
        above_ma200=above_ma200,
        ma200_slope_60d=ma200_slope_60d,
        return_90d=ret_90d,
        return_365d=ret_365d,
    )

    return {
        "date_used": str(pd.Timestamp(used_date).date()),
        "price": price,
        "ma50": ma50,
        "ma200": ma200,
        "above_ma200": above_ma200,
        "ma200_slope_60d": ma200_slope_60d,
        "return_90d": ret_90d,
        "return_365d": ret_365d,
        "regime": regime,
    }


def classify_regime(price, ma200, above_ma200, ma200_slope_60d, return_90d, return_365d):
    price = safe_float(price)
    ma200 = safe_float(ma200)
    slope = safe_float(ma200_slope_60d)
    ret90 = safe_float(return_90d)
    ret365 = safe_float(return_365d)

    if pd.isna(price) or pd.isna(ma200) or pd.isna(ret90):
        return "UNKNOWN"

    slope_up = False
    slope_down = False

    if not pd.isna(slope):
        slope_up = slope >= 2.0
        slope_down = slope <= -2.0

    strong_up_90d = ret90 >= 10.0
    weak_down_90d = ret90 <= -10.0

    if above_ma200 and slope_up and ret90 >= 0:
        return "BULL"

    if (not above_ma200) and slope_down and ret90 <= 0:
        return "BEAR"

    if strong_up_90d and (not above_ma200 or not slope_up):
        return "RECOVERY"

    if above_ma200 and weak_down_90d:
        return "DISTRIBUTION"

    if (not above_ma200) and ret90 > 0:
        return "RECOVERY"

    if (not above_ma200) and ret90 < 0:
        return "BEAR"

    if above_ma200 and ret90 < 0:
        return "DISTRIBUTION"

    return "MIXED"


def find_match_files():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    candidates = []
    for path in REPORTS_DIR.glob("*.csv"):
        name = path.name.lower()

        if name.startswith("market_regime_match_"):
            continue

        try:
            df_head = pd.read_csv(path, nrows=5)
        except Exception:
            continue

        cols = set(df_head.columns)
        if all(c in cols for c in REQUIRED_MATCH_COLUMNS):
            candidates.append(path)

    return sorted(candidates)


def load_all_matches():
    files = find_match_files()
    frames = []

    for path in files:
        try:
            df = pd.read_csv(path)
            if not all(c in df.columns for c in REQUIRED_MATCH_COLUMNS):
                continue

            df = df[REQUIRED_MATCH_COLUMNS].copy()
            df["source_file"] = path.name
            frames.append(df)
        except Exception as e:
            print(f"Could not read {path}: {e}")

    if not frames:
        return pd.DataFrame(columns=REQUIRED_MATCH_COLUMNS + ["source_file"])

    out = pd.concat(frames, ignore_index=True)

    for col in [
        "similarity",
        "return_7d",
        "drawdown_7d",
        "max_gain_7d",
        "return_14d",
        "drawdown_14d",
        "max_gain_14d",
        "return_30d",
        "drawdown_30d",
        "max_gain_30d",
        "return_60d",
        "drawdown_60d",
        "max_gain_60d",
    ]:
        out[col] = pd.to_numeric(out[col], errors="coerce")

    out["start_date"] = pd.to_datetime(out["start_date"], errors="coerce")
    out["end_date"] = pd.to_datetime(out["end_date"], errors="coerce")

    out = out.dropna(subset=["target", "similar_asset", "start_date"])
    out = out.sort_values(["target", "similarity"], ascending=[True, False])
    out = out.reset_index(drop=True)

    return out


def summarize(df, label):
    if df is None or df.empty:
        return {
            "group": label,
            "matches": 0,
            "positive_30d_rate": np.nan,
            "return_30d_p50": np.nan,
            "return_30d_p75": np.nan,
            "return_30d_p90": np.nan,
            "drawdown_30d_p50": np.nan,
            "drawdown_30d_p10": np.nan,
            "max_gain_30d_p50": np.nan,
            "max_gain_30d_p75": np.nan,
            "max_gain_30d_p90": np.nan,
            "positive_60d_rate": np.nan,
            "return_60d_p50": np.nan,
            "return_60d_p75": np.nan,
            "return_60d_p90": np.nan,
            "drawdown_60d_p50": np.nan,
            "drawdown_60d_p10": np.nan,
            "max_gain_60d_p50": np.nan,
            "max_gain_60d_p75": np.nan,
            "max_gain_60d_p90": np.nan,
        }

    def q(col, p):
        s = pd.to_numeric(df[col], errors="coerce").dropna()
        if s.empty:
            return np.nan
        return float(s.quantile(p))

    return {
        "group": label,
        "matches": int(len(df)),
        "positive_30d_rate": float((df["return_30d"] > 0).mean() * 100.0),
        "return_30d_p50": q("return_30d", 0.50),
        "return_30d_p75": q("return_30d", 0.75),
        "return_30d_p90": q("return_30d", 0.90),
        "drawdown_30d_p50": q("drawdown_30d", 0.50),
        "drawdown_30d_p10": q("drawdown_30d", 0.10),
        "max_gain_30d_p50": q("max_gain_30d", 0.50),
        "max_gain_30d_p75": q("max_gain_30d", 0.75),
        "max_gain_30d_p90": q("max_gain_30d", 0.90),
        "positive_60d_rate": float((df["return_60d"] > 0).mean() * 100.0),
        "return_60d_p50": q("return_60d", 0.50),
        "return_60d_p75": q("return_60d", 0.75),
        "return_60d_p90": q("return_60d", 0.90),
        "drawdown_60d_p50": q("drawdown_60d", 0.50),
        "drawdown_60d_p10": q("drawdown_60d", 0.10),
        "max_gain_60d_p50": q("max_gain_60d", 0.50),
        "max_gain_60d_p75": q("max_gain_60d", 0.75),
        "max_gain_60d_p90": q("max_gain_60d", 0.90),
    }


def classify_outcome(row):
    r30 = safe_float(row.get("return_30d"))
    r60 = safe_float(row.get("return_60d"))
    mg60 = safe_float(row.get("max_gain_60d"))

    if not pd.isna(r60) and r60 >= 50:
        return "EXPLOSIVE_60D"

    if not pd.isna(mg60) and mg60 >= 75:
        return "HIGH_SPIKE_60D"

    if not pd.isna(r30) and r30 >= 10:
        return "BULLISH_30D"

    if not pd.isna(r30) and r30 <= -10:
        return "BEARISH_30D"

    return "MIXED"


def build_regime_report(matches):
    if matches.empty:
        md = "# Market Regime Match Report\n\nNo valid match CSV files found in reports/.\n"
        OUTPUT_REPORT.write_text(md, encoding="utf-8")
        OUTPUT_MATCHES.write_text("", encoding="utf-8")
        OUTPUT_SUMMARY.write_text("", encoding="utf-8")
        inject_into_latest_report(md)
        return

    tickers = set(matches["target"].dropna().astype(str).unique())
    tickers.update(matches["similar_asset"].dropna().astype(str).unique())
    tickers.add(BTC_TICKER)

    print(f"Downloading {len(tickers)} tickers for market regime report...")

    histories = {}
    for ticker in sorted(tickers):
        close = download_close(ticker)
        histories[ticker] = build_history(close)

    btc_hist = histories.get(BTC_TICKER)

    current_btc_metrics = metrics_at_date(btc_hist, None)
    current_btc_regime = current_btc_metrics["regime"]

    current_target_metrics = {}
    for target in sorted(matches["target"].dropna().astype(str).unique()):
        current_target_metrics[target] = metrics_at_date(histories.get(target), None)

    enriched_rows = []

    for _, row in matches.iterrows():
        target = str(row["target"])
        similar_asset = str(row["similar_asset"])
        start_date = pd.Timestamp(row["start_date"]).normalize()

        btc_at_match = metrics_at_date(btc_hist, start_date)
        asset_at_match = metrics_at_date(histories.get(similar_asset), start_date)
        target_today = current_target_metrics.get(target, metrics_at_date(histories.get(target), None))

        same_btc_regime = (
            btc_at_match["regime"] == current_btc_regime
            and btc_at_match["regime"] != "UNKNOWN"
        )

        same_asset_regime = (
            asset_at_match["regime"] == target_today["regime"]
            and asset_at_match["regime"] != "UNKNOWN"
            and target_today["regime"] != "UNKNOWN"
        )

        same_full_regime = same_btc_regime and same_asset_regime

        if same_full_regime:
            alignment = "SAME_BTC_AND_ASSET"
        elif same_btc_regime:
            alignment = "SAME_BTC_ONLY"
        elif same_asset_regime:
            alignment = "SAME_ASSET_ONLY"
        else:
            alignment = "DIFFERENT"

        out = row.to_dict()

        out["btc_regime_today"] = current_btc_regime
        out["btc_price_today"] = current_btc_metrics["price"]
        out["btc_above_ma200_today"] = current_btc_metrics["above_ma200"]
        out["btc_return_90d_today"] = current_btc_metrics["return_90d"]
        out["btc_ma200_slope_60d_today"] = current_btc_metrics["ma200_slope_60d"]

        out["target_regime_today"] = target_today["regime"]
        out["target_price_today"] = target_today["price"]
        out["target_above_ma200_today"] = target_today["above_ma200"]
        out["target_return_90d_today"] = target_today["return_90d"]
        out["target_ma200_slope_60d_today"] = target_today["ma200_slope_60d"]

        out["btc_regime_at_match"] = btc_at_match["regime"]
        out["btc_price_at_match"] = btc_at_match["price"]
        out["btc_above_ma200_at_match"] = btc_at_match["above_ma200"]
        out["btc_return_90d_at_match"] = btc_at_match["return_90d"]
        out["btc_ma200_slope_60d_at_match"] = btc_at_match["ma200_slope_60d"]

        out["similar_asset_regime_at_match"] = asset_at_match["regime"]
        out["similar_asset_price_at_match"] = asset_at_match["price"]
        out["similar_asset_above_ma200_at_match"] = asset_at_match["above_ma200"]
        out["similar_asset_return_90d_at_match"] = asset_at_match["return_90d"]
        out["similar_asset_ma200_slope_60d_at_match"] = asset_at_match["ma200_slope_60d"]

        out["same_btc_regime_as_today"] = bool(same_btc_regime)
        out["same_asset_regime_as_today"] = bool(same_asset_regime)
        out["same_full_regime_as_today"] = bool(same_full_regime)
        out["regime_alignment"] = alignment
        out["outcome_family"] = classify_outcome(out)

        enriched_rows.append(out)

    enriched = pd.DataFrame(enriched_rows)

    enriched = enriched.sort_values(
        ["target", "same_full_regime_as_today", "same_btc_regime_as_today", "similarity"],
        ascending=[True, False, False, False],
    ).reset_index(drop=True)

    summary_rows = []

    for target, g in enriched.groupby("target"):
        summary_rows.append({"target": target, **summarize(g, "ALL_MATCHES")})

        same_btc = g[g["same_btc_regime_as_today"] == True]
        summary_rows.append({"target": target, **summarize(same_btc, "SAME_BTC_REGIME")})

        same_asset = g[g["same_asset_regime_as_today"] == True]
        summary_rows.append({"target": target, **summarize(same_asset, "SAME_ASSET_REGIME")})

        same_full = g[g["same_full_regime_as_today"] == True]
        summary_rows.append({"target": target, **summarize(same_full, "SAME_BTC_AND_ASSET_REGIME")})

        for regime, rg in g.groupby("btc_regime_at_match"):
            summary_rows.append({"target": target, **summarize(rg, f"HISTORICAL_BTC_{regime}")})

        for regime, rg in g.groupby("similar_asset_regime_at_match"):
            summary_rows.append({"target": target, **summarize(rg, f"HISTORICAL_ASSET_{regime}")})

    summary = pd.DataFrame(summary_rows)

    enriched.to_csv(OUTPUT_MATCHES, index=False)
    summary.to_csv(OUTPUT_SUMMARY, index=False)

    md = render_markdown_report(enriched, summary, current_btc_metrics, current_target_metrics)

    OUTPUT_REPORT.write_text(md, encoding="utf-8")
    inject_into_latest_report(md)

    print(f"Wrote {OUTPUT_REPORT}")
    print(f"Wrote {OUTPUT_MATCHES}")
    print(f"Wrote {OUTPUT_SUMMARY}")


def render_markdown_report(enriched, summary, current_btc_metrics, current_target_metrics):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = []
    lines.append("# Market Regime Match Report")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append("")
    lines.append("This report adds market regime context to the raw fractal matches.")
    lines.append("")
    lines.append("Main idea:")
    lines.append("")
    lines.append("- A chart match during a bull market is not the same as a chart match during a bear market.")
    lines.append("- This report separates matches by BTC regime and by similar-asset regime.")
    lines.append("- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.")
    lines.append("")

    lines.append("## Current regime snapshot")
    lines.append("")

    current_rows = []

    for target, m in current_target_metrics.items():
        current_rows.append({
            "target": target,
            "target_regime_today": m["regime"],
            "target_price": fmt_num(m["price"]),
            "target_above_ma200": m["above_ma200"],
            "target_return_90d": fmt_pct(m["return_90d"]),
            "target_ma200_slope_60d": fmt_pct(m["ma200_slope_60d"]),
            "btc_regime_today": current_btc_metrics["regime"],
            "btc_return_90d": fmt_pct(current_btc_metrics["return_90d"]),
            "btc_ma200_slope_60d": fmt_pct(current_btc_metrics["ma200_slope_60d"]),
        })

    current_df = pd.DataFrame(current_rows)
    lines.append(df_to_markdown(current_df))
    lines.append("")

    lines.append("## Summary by regime filter")
    lines.append("")

    main_groups = summary[
        summary["group"].isin([
            "ALL_MATCHES",
            "SAME_BTC_REGIME",
            "SAME_ASSET_REGIME",
            "SAME_BTC_AND_ASSET_REGIME",
        ])
    ].copy()

    display_cols = [
        "target",
        "group",
        "matches",
        "positive_30d_rate",
        "return_30d_p50",
        "return_30d_p75",
        "return_30d_p90",
        "drawdown_30d_p50",
        "drawdown_30d_p10",
        "max_gain_30d_p50",
        "max_gain_30d_p75",
        "max_gain_30d_p90",
        "positive_60d_rate",
        "return_60d_p50",
        "return_60d_p75",
        "return_60d_p90",
    ]

    main_display = main_groups[display_cols].copy()

    pct_cols = [c for c in main_display.columns if c not in ["target", "group", "matches"]]
    for col in pct_cols:
        main_display[col] = main_display[col].apply(fmt_pct)

    lines.append(df_to_markdown(main_display))
    lines.append("")

    lines.append("## Breakdown by historical BTC regime")
    lines.append("")

    btc_breakdown = summary[summary["group"].astype(str).str.startswith("HISTORICAL_BTC_")].copy()
    btc_display = btc_breakdown[
        [
            "target",
            "group",
            "matches",
            "positive_30d_rate",
            "return_30d_p50",
            "drawdown_30d_p50",
            "max_gain_30d_p75",
            "positive_60d_rate",
            "return_60d_p50",
            "max_gain_60d_p75",
        ]
    ].copy()

    for col in [
        "positive_30d_rate",
        "return_30d_p50",
        "drawdown_30d_p50",
        "max_gain_30d_p75",
        "positive_60d_rate",
        "return_60d_p50",
        "max_gain_60d_p75",
    ]:
        btc_display[col] = btc_display[col].apply(fmt_pct)

    lines.append(df_to_markdown(btc_display))
    lines.append("")

    lines.append("## Breakdown by historical asset regime")
    lines.append("")

    asset_breakdown = summary[summary["group"].astype(str).str.startswith("HISTORICAL_ASSET_")].copy()
    asset_display = asset_breakdown[
        [
            "target",
            "group",
            "matches",
            "positive_30d_rate",
            "return_30d_p50",
            "drawdown_30d_p50",
            "max_gain_30d_p75",
            "positive_60d_rate",
            "return_60d_p50",
            "max_gain_60d_p75",
        ]
    ].copy()

    for col in [
        "positive_30d_rate",
        "return_30d_p50",
        "drawdown_30d_p50",
        "max_gain_30d_p75",
        "positive_60d_rate",
        "return_60d_p50",
        "max_gain_60d_p75",
    ]:
        asset_display[col] = asset_display[col].apply(fmt_pct)

    lines.append(df_to_markdown(asset_display))
    lines.append("")

    lines.append("## Top regime-adjusted matches")
    lines.append("")

    top_cols = [
        "target",
        "similar_asset",
        "start_date",
        "similarity",
        "btc_regime_at_match",
        "similar_asset_regime_at_match",
        "regime_alignment",
        "outcome_family",
        "return_30d",
        "drawdown_30d",
        "max_gain_30d",
        "return_60d",
        "drawdown_60d",
        "max_gain_60d",
    ]

    top = enriched[top_cols].copy()
    top["start_date"] = pd.to_datetime(top["start_date"]).dt.date.astype(str)
    top = top.head(30)

    for col in [
        "similarity",
        "return_30d",
        "drawdown_30d",
        "max_gain_30d",
        "return_60d",
        "drawdown_60d",
        "max_gain_60d",
    ]:
        top[col] = top[col].apply(fmt_pct)

    lines.append(df_to_markdown(top))
    lines.append("")

    lines.append("## Interpretation rules")
    lines.append("")
    lines.append("- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.")
    lines.append("- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.")
    lines.append("- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.")
    lines.append("- SAME_BTC_AND_ASSET_REGIME is the cleanest filter, but it needs enough matches to matter.")
    lines.append("- If SAME_BTC_AND_ASSET_REGIME has fewer than 5 matches, treat it as useful context, not a strong statistic.")
    lines.append("- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.")
    lines.append("- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.")
    lines.append("")

    lines.append("## Regime definitions")
    lines.append("")
    lines.append("- BULL: price above MA200, MA200 rising, positive 90d trend.")
    lines.append("- BEAR: price below MA200, MA200 falling, weak 90d trend.")
    lines.append("- RECOVERY: improving 90d trend, but not yet a clean bull structure.")
    lines.append("- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.")
    lines.append("- MIXED: unclear regime.")
    lines.append("- UNKNOWN: not enough historical data.")
    lines.append("")

    return "\n".join(lines) + "\n"


def inject_into_latest_report(section_md):
    if not LATEST_REPORT.exists():
        return

    try:
        old = LATEST_REPORT.read_text(encoding="utf-8")
    except Exception:
        return

    clean_section = section_md.strip()

    if START_MARKER in old and END_MARKER in old:
        start = old.find(START_MARKER)
        end = old.find(END_MARKER)

        if start != -1 and end != -1 and end > start:
            end = end + len(END_MARKER)
            new = old[:start] + START_MARKER + "\n" + clean_section + "\n" + END_MARKER + old[end:]
        else:
            new = old.rstrip() + "\n\n" + START_MARKER + "\n" + clean_section + "\n" + END_MARKER + "\n"
    else:
        new = old.rstrip() + "\n\n" + START_MARKER + "\n" + clean_section + "\n" + END_MARKER + "\n"

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    matches = load_all_matches()

    if matches.empty:
        md = "# Market Regime Match Report\n\nNo valid match CSV files found in reports/.\n"
        OUTPUT_REPORT.write_text(md, encoding="utf-8")
        inject_into_latest_report(md)
        print("No valid match CSV files found.")
        return

    build_regime_report(matches)


if __name__ == "__main__":
    main()
