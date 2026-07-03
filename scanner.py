import os
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.spatial.distance import cosine


WINDOW = 100
FORWARD_DAYS = [7, 14, 30, 60]
STEP = 5
TOP_N = 200
CLEAN_TOP_N = 40
MIN_GAP_DAYS = 90

TARGETS = ["BTC-USD", "SOL-USD"]

CRYPTO_TICKERS = [
    "BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD", "XRP-USD",
    "ADA-USD", "AVAX-USD", "DOGE-USD", "LINK-USD", "DOT-USD",
    "LTC-USD", "NEAR-USD", "UNI-USD", "ATOM-USD", "ETC-USD",
    "FIL-USD", "APT-USD", "ARB-USD", "OP-USD", "SUI-USD",
    "ICP-USD", "INJ-USD", "AAVE-USD", "MATIC-USD", "TRX-USD",
    "BCH-USD", "XLM-USD", "HBAR-USD", "VET-USD", "ALGO-USD",
    "EOS-USD", "XTZ-USD", "MANA-USD", "SAND-USD", "GRT-USD",
    "CHZ-USD", "EGLD-USD", "FTM-USD", "RUNE-USD", "THETA-USD",
    "KSM-USD", "ZEC-USD", "DASH-USD", "COMP-USD", "MKR-USD",
    "SNX-USD", "CRV-USD", "ENJ-USD", "BAT-USD", "ZIL-USD",
    "WAVES-USD", "KAVA-USD", "ONE-USD", "IOTA-USD", "NEO-USD",
    "QTUM-USD", "OMG-USD", "YFI-USD", "1INCH-USD", "LRC-USD"
]


def add_indicators(df):
    df = df.copy()

    df["return"] = df["Close"].pct_change()

    df["ma20"] = df["Close"].rolling(20).mean()
    df["ma50"] = df["Close"].rolling(50).mean()
    df["ma200"] = df["Close"].rolling(200).mean()

    df["dist_ma20"] = (df["Close"] / df["ma20"]) - 1
    df["dist_ma50"] = (df["Close"] / df["ma50"]) - 1
    df["dist_ma200"] = (df["Close"] / df["ma200"]) - 1

    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))

    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["macd"] = ema12 - ema26
    df["macd_signal"] = df["macd"].ewm(span=9, adjust=False).mean()
    df["macd_hist"] = df["macd"] - df["macd_signal"]

    df["volatility"] = df["return"].rolling(20).std()
    df["volume_norm"] = df["Volume"] / df["Volume"].rolling(20).mean()

    rolling_max = df["Close"].rolling(100).max()
    df["drawdown"] = (df["Close"] / rolling_max) - 1

    return df.replace([np.inf, -np.inf], np.nan).dropna()


def zscore_array(x):
    x = np.array(x, dtype=float)
    mean = np.nanmean(x)
    std = np.nanstd(x)
    if std == 0 or np.isnan(std):
        std = 1
    return (x - mean) / std


def make_signature_v2(df, start_idx=None, window=WINDOW):
    if start_idx is None:
        w = df.tail(window).copy()
    else:
        w = df.iloc[start_idx:start_idx + window].copy()

    w = w.replace([np.inf, -np.inf], np.nan).dropna()

    if len(w) < window:
        return None

    price_shape = np.log(w["Close"] / w["Close"].iloc[0])

    features = np.column_stack([
        zscore_array(price_shape),
        zscore_array(w["rsi"]),
        zscore_array(w["dist_ma20"]),
        zscore_array(w["dist_ma50"]),
        zscore_array(w["drawdown"]),
    ])

    weights = np.array([3.0, 1.5, 1.0, 1.0, 1.0])
    return (features * weights).flatten()


def future_stats(df, end_idx):
    close_now = df["Close"].iloc[end_idx]
    results = {}

    for d in FORWARD_DAYS:
        if end_idx + d < len(df):
            future_close = df["Close"].iloc[end_idx + d]
            future_slice = df["Close"].iloc[end_idx:end_idx + d + 1]

            results[f"return_{d}d"] = (future_close / close_now - 1) * 100
            results[f"drawdown_{d}d"] = (future_slice.min() / close_now - 1) * 100
            results[f"max_gain_{d}d"] = (future_slice.max() / close_now - 1) * 100
        else:
            results[f"return_{d}d"] = np.nan
            results[f"drawdown_{d}d"] = np.nan
            results[f"max_gain_{d}d"] = np.nan

    return results


def download_data():
    print("Downloading data...")
    raw = yf.download(
        CRYPTO_TICKERS,
        period="10y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )

    asset_data = {}

    for ticker in CRYPTO_TICKERS:
        try:
            df = raw[ticker].dropna().copy()
            if len(df) > 300:
                processed = add_indicators(df)
                if len(processed) > 250:
                    asset_data[ticker] = processed
                    print(f"{ticker}: OK {processed.index[0].date()} -> {processed.index[-1].date()}")
        except Exception as e:
            print(f"{ticker}: skipped ({e})")

    return asset_data


def find_similar_patterns(target_ticker, data_with_indicators):
    target_sig = make_signature_v2(data_with_indicators[target_ticker])
    matches = []

    for ticker, df in data_with_indicators.items():
        max_start = len(df) - WINDOW - max(FORWARD_DAYS)

        for start_idx in range(0, max_start, STEP):
            end_idx = start_idx + WINDOW - 1

            if ticker == target_ticker and end_idx >= len(df) - max(FORWARD_DAYS) - 5:
                continue

            sig = make_signature_v2(df, start_idx=start_idx)

            if sig is None:
                continue

            similarity = 1 - cosine(target_sig, sig)

            if np.isnan(similarity):
                continue

            stats = future_stats(df, end_idx)

            matches.append({
                "target": target_ticker,
                "similar_asset": ticker,
                "start_date": df.index[start_idx].date(),
                "end_date": df.index[end_idx].date(),
                "similarity": similarity * 100,
                **stats
            })

    results = pd.DataFrame(matches)
    return results.sort_values("similarity", ascending=False).head(TOP_N)


def deoverlap_matches(matches):
    m = matches.copy()
    m["end_date_dt"] = pd.to_datetime(m["end_date"])
    m = m.sort_values("similarity", ascending=False)

    kept_rows = []
    kept_dates_by_asset = {}

    for _, row in m.iterrows():
        asset = row["similar_asset"]
        end_date = row["end_date_dt"]
        previous_dates = kept_dates_by_asset.get(asset, [])

        too_close = any(abs((end_date - prev_date).days) < MIN_GAP_DAYS for prev_date in previous_dates)

        if not too_close:
            kept_rows.append(row)
            kept_dates_by_asset.setdefault(asset, []).append(end_date)

        if len(kept_rows) >= CLEAN_TOP_N:
            break

    clean = pd.DataFrame(kept_rows)
    return clean.drop(columns=["end_date_dt"], errors="ignore")


def verdict(matches):
    ret30 = matches["return_30d"].mean()
    win30 = (matches["return_30d"] > 0).mean() * 100

    if win30 >= 65 and ret30 > 5:
        return "RIALZISTA"
    if win30 <= 40 and ret30 < 0:
        return "RIBASSISTA"
    return "NEUTRALE / INCERTO"


def summary_table(matches):
    return {
        "match_count": len(matches),
        "similarity_avg": matches["similarity"].mean(),
        "similarity_median": matches["similarity"].median(),
        "return_30d_avg": matches["return_30d"].mean(),
        "return_30d_median": matches["return_30d"].median(),
        "positive_cases_30d": (matches["return_30d"] > 0).mean() * 100,
        "drawdown_30d_avg": matches["drawdown_30d"].mean(),
        "max_gain_30d_avg": matches["max_gain_30d"].mean(),
    }


def price_scenarios(matches, current_price):
    avg_ret = matches["return_30d"].mean()
    med_ret = matches["return_30d"].median()
    avg_dd = matches["drawdown_30d"].mean()
    avg_gain = matches["max_gain_30d"].mean()

    return {
        "current_price": current_price,
        "scenario_avg_30d": current_price * (1 + avg_ret / 100),
        "scenario_median_30d": current_price * (1 + med_ret / 100),
        "drawdown_avg_30d": current_price * (1 + avg_dd / 100),
        "max_gain_avg_30d": current_price * (1 + avg_gain / 100),
    }


def percentile_report(matches, current_price):
    rows = []

    for metric in ["return_30d", "drawdown_30d", "max_gain_30d"]:
        values = matches[metric].dropna()

        for q in [10, 25, 50, 75, 90]:
            pct = np.percentile(values, q)
            price = current_price * (1 + pct / 100)
            rows.append({
                "metric": metric,
                "percentile": q,
                "percent_value": pct,
                "price_level": price,
            })

    return pd.DataFrame(rows)


def build_markdown_report(all_results, generated_at):
    lines = []
    lines.append(f"# Crypto Fractal Scanner Report")
    lines.append("")
    lines.append(f"Generated at: **{generated_at} UTC**")
    lines.append("")
    lines.append("This report compares the latest 100 daily candles of BTC and SOL against historical crypto patterns.")
    lines.append("It is not financial advice. It is a statistical pattern scanner.")
    lines.append("")

    for target, result in all_results.items():
        lines.append(f"## {target}")
        lines.append("")
        lines.append(f"**Verdict:** {result['verdict']}")
        lines.append("")
        lines.append("### Summary")
        lines.append("")
        s = result["summary"]
        lines.append(f"- Matches: **{s['match_count']}**")
        lines.append(f"- Average similarity: **{s['similarity_avg']:.2f}%**")
        lines.append(f"- Median similarity: **{s['similarity_median']:.2f}%**")
        lines.append(f"- Average 30d return: **{s['return_30d_avg']:.2f}%**")
        lines.append(f"- Median 30d return: **{s['return_30d_median']:.2f}%**")
        lines.append(f"- Positive cases 30d: **{s['positive_cases_30d']:.1f}%**")
        lines.append(f"- Average 30d drawdown: **{s['drawdown_30d_avg']:.2f}%**")
        lines.append(f"- Average 30d max gain: **{s['max_gain_30d_avg']:.2f}%**")
        lines.append("")
        lines.append("### Price scenarios")
        lines.append("")
        p = result["prices"]
        lines.append(f"- Current price: **{p['current_price']:.2f}**")
        lines.append(f"- Average 30d scenario: **{p['scenario_avg_30d']:.2f}**")
        lines.append(f"- Median 30d scenario: **{p['scenario_median_30d']:.2f}**")
        lines.append(f"- Average drawdown level: **{p['drawdown_avg_30d']:.2f}**")
        lines.append(f"- Average max-gain level: **{p['max_gain_avg_30d']:.2f}**")
        lines.append("")
        lines.append("### Top similar patterns")
        lines.append("")
        top = result["matches"].head(10)[[
            "similar_asset", "start_date", "end_date", "similarity",
            "return_30d", "drawdown_30d", "max_gain_30d"
        ]].round(2)
        lines.append(top.to_markdown(index=False))
        lines.append("")

    return "\n".join(lines)


def main():
    generated_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs("reports", exist_ok=True)

    data = download_data()
    all_results = {}

    for target in TARGETS:
        print(f"Scanning {target}...")
        matches_raw = find_similar_patterns(target, data)
        matches_clean = deoverlap_matches(matches_raw)

        current_price = data[target]["Close"].iloc[-1]

        all_results[target] = {
            "matches": matches_clean,
            "summary": summary_table(matches_clean),
            "prices": price_scenarios(matches_clean, current_price),
            "percentiles": percentile_report(matches_clean, current_price),
            "verdict": verdict(matches_clean),
        }

        safe_target = target.replace("-USD", "")
        matches_clean.to_csv(f"reports/{safe_target}_matches.csv", index=False)
        all_results[target]["percentiles"].to_csv(f"reports/{safe_target}_percentiles.csv", index=False)

    report_md = build_markdown_report(all_results, generated_at)

    with open("reports/latest_report.md", "w", encoding="utf-8") as f:
        f.write(report_md)

    print(report_md)
    print("Report saved in reports/latest_report.md")


if __name__ == "__main__":
    main()
