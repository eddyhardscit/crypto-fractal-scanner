import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"
PREDICTION_LOG_PATH = "reports/prediction_log.csv"
BOUNCE_REPORT_PATH = "reports/bounce_after_drawdown_report.md"
BOUNCE_CSV_PATH = "reports/bounce_after_drawdown_metrics.csv"

TARGETS = ["BTC-USD", "SOL-USD", "DOGE-USD"]

PULLBACK_LEVELS = [-5, -10, -15]
REBOUND_TARGETS = [10, 20]
FORWARD_DAYS = 30


def asset_name(asset):
    if asset == "BTC-USD":
        return "Bitcoin"
    if asset == "SOL-USD":
        return "Solana"
    if asset == "DOGE-USD":
        return "Dogecoin"
    return asset


def asset_short(asset):
    return asset.replace("-USD", "")


def matches_path(asset):
    short = asset_short(asset)
    return f"reports/{short}_matches.csv"


def percentiles_path(asset):
    short = asset_short(asset)
    return f"reports/{short}_percentiles.csv"


def read_csv_safe(path):
    if not os.path.exists(path):
        return pd.DataFrame()

    try:
        if os.path.getsize(path) <= 1:
            return pd.DataFrame()
    except Exception:
        pass

    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def safe_float(value):
    try:
        if pd.isna(value):
            return None
        value = float(value)
        if np.isnan(value) or np.isinf(value):
            return None
        return value
    except Exception:
        return None


def fmt_number(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    s = f"{value:,.{decimals}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_pct(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    sign = "+" if value > 0 else ""
    return f"{sign}{fmt_number(value, decimals)}%"


def fmt_price(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    if abs(value) >= 1000:
        return f"{fmt_number(value, 0)} $"

    if abs(value) >= 1:
        return f"{fmt_number(value, 2)} $"

    return f"{fmt_number(value, 5)} $"


def fmt_int(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    return str(int(round(value)))


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")

    return "\n".join(lines)


def latest_current_price(asset):
    log = read_csv_safe(PREDICTION_LOG_PATH)

    if log.empty:
        return None

    if "asset" not in log.columns or "current_price" not in log.columns:
        return None

    rows = log[log["asset"].astype(str) == asset].copy()

    if rows.empty:
        return None

    if "generated_at_utc" in rows.columns:
        rows["generated_at_dt"] = pd.to_datetime(
            rows["generated_at_utc"],
            errors="coerce",
        )
        rows = rows.sort_values("generated_at_dt")

    price = safe_float(rows.iloc[-1].get("current_price"))

    return price


def max_gain_p75_pct(asset, matches):
    pfile = percentiles_path(asset)
    percentiles = read_csv_safe(pfile)

    if not percentiles.empty:
        needed = {"metric", "percentile", "percent_value"}
        if needed.issubset(percentiles.columns):
            rows = percentiles[
                (percentiles["metric"].astype(str) == "max_gain_30d")
                & (pd.to_numeric(percentiles["percentile"], errors="coerce") == 75)
            ]

            if not rows.empty:
                value = safe_float(rows.iloc[0].get("percent_value"))
                if value is not None:
                    return value

    if not matches.empty and "max_gain_30d" in matches.columns:
        values = pd.to_numeric(matches["max_gain_30d"], errors="coerce").dropna()
        if len(values) > 0:
            return float(np.percentile(values, 75))

    return None


def download_needed_data(all_matches):
    tickers = sorted(set(all_matches["similar_asset"].dropna().astype(str).tolist()))

    if not tickers:
        return {}

    print(f"Downloading data for bounce report: {tickers}")

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
        try:
            if len(tickers) == 1:
                df = raw.dropna().copy()
            else:
                df = raw[ticker].dropna().copy()

            if len(df) == 0:
                continue

            df.index = pd.to_datetime(df.index)

            if getattr(df.index, "tz", None) is not None:
                df.index = df.index.tz_convert(None)

            df.index = df.index.normalize()

            if "Close" in df.columns:
                data[ticker] = df[["Close"]].copy()

        except Exception as exc:
            print(f"{ticker}: skipped in bounce report ({exc})")

    return data


def build_all_matches():
    rows = []

    for asset in TARGETS:
        path = matches_path(asset)
        matches = read_csv_safe(path)

        if matches.empty:
            continue

        matches["target_asset"] = asset
        rows.append(matches)

    if not rows:
        return pd.DataFrame()

    return pd.concat(rows, ignore_index=True)


def analyze_one_match(row, data, pullback_pct, rebound_pct, p75_pct):
    ticker = str(row.get("similar_asset"))
    end_date = pd.to_datetime(row.get("end_date"), errors="coerce")

    if pd.isna(end_date):
        return None

    if ticker not in data:
        return None

    df = data[ticker].copy()
    idx = pd.DatetimeIndex(df.index).normalize()

    positions = np.where(idx >= end_date.normalize())[0]

    if len(positions) == 0:
        return None

    start_pos = int(positions[0])

    if start_pos + FORWARD_DAYS >= len(df):
        return None

    start_price = safe_float(df["Close"].iloc[start_pos])

    if start_price is None or start_price <= 0:
        return None

    path = df["Close"].iloc[start_pos:start_pos + FORWARD_DAYS + 1].copy()
    path = pd.to_numeric(path, errors="coerce").dropna()

    if len(path) < 2:
        return None

    pullback_price = start_price * (1 + pullback_pct / 100)
    rebound_price = start_price * (1 + rebound_pct / 100)

    touched_positions = np.where(path.values <= pullback_price)[0]
    touched_pullback = len(touched_positions) > 0

    result = {
        "valid": True,
        "touched_pullback": touched_pullback,
        "pullback_day": np.nan,
        "rebound_hit": False,
        "rebound_day": np.nan,
        "p75_hit": False,
        "p75_day": np.nan,
        "min_return_pct": (path.min() / start_price - 1) * 100,
        "max_return_pct": (path.max() / start_price - 1) * 100,
    }

    if not touched_pullback:
        return result

    pullback_day = int(touched_positions[0])
    result["pullback_day"] = pullback_day

    after_pullback = path.iloc[pullback_day:]

    rebound_positions = np.where(after_pullback.values >= rebound_price)[0]

    if len(rebound_positions) > 0:
        rebound_day = pullback_day + int(rebound_positions[0])
        result["rebound_hit"] = True
        result["rebound_day"] = rebound_day

    if p75_pct is not None:
        p75_price = start_price * (1 + p75_pct / 100)
        p75_positions = np.where(after_pullback.values >= p75_price)[0]

        if len(p75_positions) > 0:
            p75_day = pullback_day + int(p75_positions[0])
            result["p75_hit"] = True
            result["p75_day"] = p75_day

    return result


def summarize_condition(asset, matches, data, current_price, pullback_pct, rebound_pct, p75_pct):
    total_matches = 0
    touched = 0
    rebound_hits = 0
    p75_hits = 0

    pullback_days = []
    rebound_days = []
    p75_days = []

    min_returns = []
    max_returns = []

    for _, row in matches.iterrows():
        result = analyze_one_match(row, data, pullback_pct, rebound_pct, p75_pct)

        if result is None or not result.get("valid"):
            continue

        total_matches += 1
        min_returns.append(result["min_return_pct"])
        max_returns.append(result["max_return_pct"])

        if result["touched_pullback"]:
            touched += 1
            pullback_days.append(result["pullback_day"])

            if result["rebound_hit"]:
                rebound_hits += 1
                rebound_days.append(result["rebound_day"])

            if result["p75_hit"]:
                p75_hits += 1
                p75_days.append(result["p75_day"])

    touched_rate_all = (touched / total_matches * 100) if total_matches else np.nan
    rebound_rate_after = (rebound_hits / touched * 100) if touched else np.nan
    p75_rate_after = (p75_hits / touched * 100) if touched else np.nan

    pullback_price_now = None
    rebound_price_now = None
    p75_price_now = None

    if current_price is not None:
        pullback_price_now = current_price * (1 + pullback_pct / 100)
        rebound_price_now = current_price * (1 + rebound_pct / 100)

        if p75_pct is not None:
            p75_price_now = current_price * (1 + p75_pct / 100)

    return {
        "asset": asset,
        "pullback_pct": pullback_pct,
        "rebound_pct": rebound_pct,
        "p75_pct": p75_pct,
        "current_price": current_price,
        "pullback_price_now": pullback_price_now,
        "rebound_price_now": rebound_price_now,
        "p75_price_now": p75_price_now,
        "total_valid_matches": total_matches,
        "touched_count": touched,
        "touched_rate_all": touched_rate_all,
        "rebound_hits_after_pullback": rebound_hits,
        "rebound_rate_after_pullback": rebound_rate_after,
        "p75_hits_after_pullback": p75_hits,
        "p75_rate_after_pullback": p75_rate_after,
        "avg_days_to_pullback": float(np.nanmean(pullback_days)) if pullback_days else np.nan,
        "avg_days_to_rebound": float(np.nanmean(rebound_days)) if rebound_days else np.nan,
        "avg_days_to_p75": float(np.nanmean(p75_days)) if p75_days else np.nan,
        "avg_min_return_pct": float(np.nanmean(min_returns)) if min_returns else np.nan,
        "avg_max_return_pct": float(np.nanmean(max_returns)) if max_returns else np.nan,
    }


def simple_strength(rate):
    value = safe_float(rate)

    if value is None:
        return "n/d"

    if value >= 65:
        return "alta"
    if value >= 50:
        return "media"
    if value >= 35:
        return "bassa"
    return "debole"


def simple_interpretation(summary):
    rate = safe_float(summary.get("rebound_rate_after_pullback"))
    touched = int(summary.get("touched_count", 0))
    total = int(summary.get("total_valid_matches", 0))
    pullback_pct = summary.get("pullback_pct")
    rebound_pct = summary.get("rebound_pct")
    asset = asset_short(summary.get("asset"))

    if total == 0:
        return f"{asset}: dati insufficienti."

    if touched == 0:
        return (
            f"{asset}: nei casi storici simili non ci sono stati abbastanza esempi "
            f"di discesa {fmt_pct(pullback_pct)}."
        )

    if rate is None:
        return f"{asset}: dati insufficienti dopo la discesa."

    if rate >= 65:
        return (
            f"{asset}: quando prima scendeva di {fmt_pct(pullback_pct)}, "
            f"spesso poi riusciva a rimbalzare fino a {fmt_pct(rebound_pct)}."
        )

    if rate >= 50:
        return (
            f"{asset}: dopo una discesa di {fmt_pct(pullback_pct)}, "
            f"il rimbalzo a {fmt_pct(rebound_pct)} avveniva circa una volta su due."
        )

    if rate >= 35:
        return (
            f"{asset}: dopo una discesa di {fmt_pct(pullback_pct)}, "
            f"il rimbalzo a {fmt_pct(rebound_pct)} era possibile ma non dominante."
        )

    return (
        f"{asset}: dopo una discesa di {fmt_pct(pullback_pct)}, "
        f"il rimbalzo a {fmt_pct(rebound_pct)} era poco frequente."
    )


def best_summary_for_asset(summaries, asset):
    rows = [
        s for s in summaries
        if s["asset"] == asset and s["pullback_pct"] == -5 and s["rebound_pct"] == 10
    ]

    if rows:
        return rows[0]

    rows = [s for s in summaries if s["asset"] == asset]

    if rows:
        return rows[0]

    return None


def build_report(summaries):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    quick_rows = []

    for asset in TARGETS:
        best = best_summary_for_asset(summaries, asset)

        if best is None:
            quick_rows.append([asset_short(asset), "n/d", "n/d", "n/d", "dati insufficienti"])
            continue

        quick_rows.append(
            [
                asset_short(asset),
                fmt_price(best["pullback_price_now"]),
                f"{best['touched_count']}/{best['total_valid_matches']}",
                fmt_pct(best["rebound_rate_after_pullback"]),
                simple_interpretation(best),
            ]
        )

    text = f"""# Rimbalzo dopo drawdown

Generato: **{rome_now}**  
UTC: **{utc_now}**

Questa sezione risponde a una domanda molto pratica:

> Se prima scende, storicamente poi rimbalza?

Lo scanner controlla i 40 casi storici più simili e guarda l'ordine degli eventi:

```text
prima scende almeno di X%
poi prova a rimbalzare a +10%, +20% o alla zona rialzo P75
