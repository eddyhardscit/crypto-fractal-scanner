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

FORWARD_DAYS = 30

# Prima scende, poi rimbalza
PULLBACK_LEVELS = [-5, -10, -15]
REBOUND_TARGETS = [10, 20]

# Prima sale, poi scarica
SPIKE_LEVELS = [10, 20]
DUMP_TARGETS = [0, -5, -10]


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


def fmt_days(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    return fmt_number(value, 1)


def fmt_dump_level(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    if value == 0:
        return "0% / prezzo iniziale"

    return fmt_pct(value)


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

    return safe_float(rows.iloc[-1].get("current_price"))


def percentile_metric_pct(asset, matches, metric, percentile):
    pfile = percentiles_path(asset)
    percentiles = read_csv_safe(pfile)

    if not percentiles.empty:
        needed = {"metric", "percentile", "percent_value"}

        if needed.issubset(percentiles.columns):
            rows = percentiles[
                (percentiles["metric"].astype(str) == metric)
                & (pd.to_numeric(percentiles["percentile"], errors="coerce") == percentile)
            ]

            if not rows.empty:
                value = safe_float(rows.iloc[0].get("percent_value"))
                if value is not None:
                    return value

    if not matches.empty and metric in matches.columns:
        values = pd.to_numeric(matches[metric], errors="coerce").dropna()

        if len(values) > 0:
            return float(np.percentile(values, percentile))

    return None


def max_gain_p75_pct(asset, matches):
    return percentile_metric_pct(asset, matches, "max_gain_30d", 75)


def drawdown_p25_pct(asset, matches):
    return percentile_metric_pct(asset, matches, "drawdown_30d", 25)


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


def download_needed_data(all_matches):
    if "similar_asset" not in all_matches.columns:
        return {}

    tickers = sorted(set(all_matches["similar_asset"].dropna().astype(str).tolist()))

    if not tickers:
        return {}

    print(f"Downloading historical data for sequence report: {tickers}")

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
            print(f"{ticker}: skipped ({exc})")

    return data


def get_forward_path(row, data):
    ticker = str(row.get("similar_asset"))
    end_date = pd.to_datetime(row.get("end_date"), errors="coerce")

    if pd.isna(end_date):
        return None, None

    if ticker not in data:
        return None, None

    df = data[ticker].copy()
    idx = pd.DatetimeIndex(df.index).normalize()

    positions = np.where(idx >= end_date.normalize())[0]

    if len(positions) == 0:
        return None, None

    start_pos = int(positions[0])

    if start_pos + FORWARD_DAYS >= len(df):
        return None, None

    start_price = safe_float(df["Close"].iloc[start_pos])

    if start_price is None or start_price <= 0:
        return None, None

    path = df["Close"].iloc[start_pos:start_pos + FORWARD_DAYS + 1].copy()
    path = pd.to_numeric(path, errors="coerce").dropna()

    if len(path) < 2:
        return None, None

    return start_price, path


def analyze_bounce_match(row, data, pullback_pct, rebound_pct, p75_pct):
    """
    Sequenza:
    prima scende almeno a pullback_pct
    poi, solo dopo, controlla se sale a rebound_pct / P75.
    """
    start_price, path = get_forward_path(row, data)

    if start_price is None or path is None:
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


def analyze_dump_match(row, data, spike_pct, dump_pct, p25_pct):
    """
    Sequenza contraria:
    prima sale almeno a spike_pct
    poi, solo dopo, controlla se scarica a dump_pct / P25.
    """
    start_price, path = get_forward_path(row, data)

    if start_price is None or path is None:
        return None

    spike_price = start_price * (1 + spike_pct / 100)
    dump_price = start_price * (1 + dump_pct / 100)

    spike_positions = np.where(path.values >= spike_price)[0]
    touched_spike = len(spike_positions) > 0

    result = {
        "valid": True,
        "touched_spike": touched_spike,
        "spike_day": np.nan,
        "dump_hit": False,
        "dump_day": np.nan,
        "p25_hit": False,
        "p25_day": np.nan,
        "min_return_pct": (path.min() / start_price - 1) * 100,
        "max_return_pct": (path.max() / start_price - 1) * 100,
    }

    if not touched_spike:
        return result

    spike_day = int(spike_positions[0])
    result["spike_day"] = spike_day

    after_spike = path.iloc[spike_day:]

    dump_positions = np.where(after_spike.values <= dump_price)[0]

    if len(dump_positions) > 0:
        dump_day = spike_day + int(dump_positions[0])
        result["dump_hit"] = True
        result["dump_day"] = dump_day

    if p25_pct is not None:
        p25_price = start_price * (1 + p25_pct / 100)
        p25_positions = np.where(after_spike.values <= p25_price)[0]

        if len(p25_positions) > 0:
            p25_day = spike_day + int(p25_positions[0])
            result["p25_hit"] = True
            result["p25_day"] = p25_day

    return result


def summarize_bounce_condition(asset, matches, data, current_price, pullback_pct, rebound_pct, p75_pct):
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
        result = analyze_bounce_match(row, data, pullback_pct, rebound_pct, p75_pct)

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
        "type": "bounce_after_drawdown",
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


def summarize_dump_condition(asset, matches, data, current_price, spike_pct, dump_pct, p25_pct):
    total_matches = 0
    touched = 0
    dump_hits = 0
    p25_hits = 0

    spike_days = []
    dump_days = []
    p25_days = []

    min_returns = []
    max_returns = []

    for _, row in matches.iterrows():
        result = analyze_dump_match(row, data, spike_pct, dump_pct, p25_pct)

        if result is None or not result.get("valid"):
            continue

        total_matches += 1
        min_returns.append(result["min_return_pct"])
        max_returns.append(result["max_return_pct"])

        if result["touched_spike"]:
            touched += 1
            spike_days.append(result["spike_day"])

            if result["dump_hit"]:
                dump_hits += 1
                dump_days.append(result["dump_day"])

            if result["p25_hit"]:
                p25_hits += 1
                p25_days.append(result["p25_day"])

    touched_rate_all = (touched / total_matches * 100) if total_matches else np.nan
    dump_rate_after = (dump_hits / touched * 100) if touched else np.nan
    p25_rate_after = (p25_hits / touched * 100) if touched else np.nan

    spike_price_now = None
    dump_price_now = None
    p25_price_now = None

    if current_price is not None:
        spike_price_now = current_price * (1 + spike_pct / 100)
        dump_price_now = current_price * (1 + dump_pct / 100)

        if p25_pct is not None:
            p25_price_now = current_price * (1 + p25_pct / 100)

    return {
        "type": "dump_after_spike",
        "asset": asset,
        "spike_pct": spike_pct,
        "dump_pct": dump_pct,
        "p25_pct": p25_pct,
        "current_price": current_price,
        "spike_price_now": spike_price_now,
        "dump_price_now": dump_price_now,
        "p25_price_now": p25_price_now,
        "total_valid_matches": total_matches,
        "touched_count": touched,
        "touched_rate_all": touched_rate_all,
        "dump_hits_after_spike": dump_hits,
        "dump_rate_after_spike": dump_rate_after,
        "p25_hits_after_spike": p25_hits,
        "p25_rate_after_spike": p25_rate_after,
        "avg_days_to_spike": float(np.nanmean(spike_days)) if spike_days else np.nan,
        "avg_days_to_dump": float(np.nanmean(dump_days)) if dump_days else np.nan,
        "avg_days_to_p25": float(np.nanmean(p25_days)) if p25_days else np.nan,
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


def simple_bounce_interpretation(summary):
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


def simple_dump_interpretation(summary):
    rate = safe_float(summary.get("dump_rate_after_spike"))
    touched = int(summary.get("touched_count", 0))
    total = int(summary.get("total_valid_matches", 0))
    spike_pct = summary.get("spike_pct")
    dump_pct = summary.get("dump_pct")
    asset = asset_short(summary.get("asset"))

    if total == 0:
        return f"{asset}: dati insufficienti."

    if touched == 0:
        return (
            f"{asset}: nei casi storici simili non ci sono stati abbastanza esempi "
            f"di spike {fmt_pct(spike_pct)}."
        )

    if rate is None:
        return f"{asset}: dati insufficienti dopo lo spike."

    dump_text = "al prezzo iniziale" if dump_pct == 0 else f"a {fmt_pct(dump_pct)}"

    if rate >= 65:
        return (
            f"{asset}: quando prima faceva uno spike di {fmt_pct(spike_pct)}, "
            f"spesso poi scaricava {dump_text}."
        )

    if rate >= 50:
        return (
            f"{asset}: dopo uno spike di {fmt_pct(spike_pct)}, "
            f"lo scarico {dump_text} avveniva circa una volta su due."
        )

    if rate >= 35:
        return (
            f"{asset}: dopo uno spike di {fmt_pct(spike_pct)}, "
            f"lo scarico {dump_text} era possibile ma non dominante."
        )

    return (
        f"{asset}: dopo uno spike di {fmt_pct(spike_pct)}, "
        f"lo scarico {dump_text} era poco frequente."
    )


def best_bounce_for_asset(bounce_summaries, asset):
    rows = [
        s for s in bounce_summaries
        if s["asset"] == asset
        and s["pullback_pct"] == -5
        and s["rebound_pct"] == 10
    ]

    if rows:
        return rows[0]

    rows = [s for s in bounce_summaries if s["asset"] == asset]

    if rows:
        return rows[0]

    return None


def best_dump_for_asset(dump_summaries, asset):
    rows = [
        s for s in dump_summaries
        if s["asset"] == asset
        and s["spike_pct"] == 10
        and s["dump_pct"] == -5
    ]

    if rows:
        return rows[0]

    rows = [s for s in dump_summaries if s["asset"] == asset]

    if rows:
        return rows[0]

    return None


def build_bounce_section(bounce_summaries):
    quick_rows = []

    for asset in TARGETS:
        best = best_bounce_for_asset(bounce_summaries, asset)

        if best is None:
            quick_rows.append([asset_short(asset), "n/d", "n/d", "n/d", "dati insufficienti"])
            continue

        quick_rows.append(
            [
                asset_short(asset),
                fmt_price(best["pullback_price_now"]),
                f"{best['touched_count']}/{best['total_valid_matches']}",
                fmt_pct(best["rebound_rate_after_pullback"]),
                simple_bounce_interpretation(best),
            ]
        )

    text = f"""
# 1. Rimbalzo dopo drawdown

Questa sezione risponde alla domanda:

> Se prima scende, storicamente poi rimbalza?

Lettura base: **discesa -5%** e poi **rimbalzo +10%**.

{md_table(
    [
        "Asset",
        "Zona -5% oggi",
        "Casi scesi",
        "Poi rimbalzo +10%",
        "Traduzione",
    ],
    quick_rows,
)}

"""

    for asset in TARGETS:
        asset_summaries = [s for s in bounce_summaries if s["asset"] == asset]

        text += f"\n## {asset_name(asset)} — rimbalzo dopo discesa\n\n"

        if not asset_summaries:
            text += "Dati insufficienti.\n\n---\n"
            continue

        current_price = asset_summaries[0].get("current_price")
        p75_pct = asset_summaries[0].get("p75_pct")
        p75_price = asset_summaries[0].get("p75_price_now")

        text += f"Prezzo attuale usato: **{fmt_price(current_price)}**  \n"
        text += f"Zona rialzo P75 usata: **{fmt_pct(p75_pct)} → {fmt_price(p75_price)}**\n\n"

        detail_rows = []

        for s in asset_summaries:
            detail_rows.append(
                [
                    fmt_pct(s["pullback_pct"]),
                    fmt_price(s["pullback_price_now"]),
                    f"{s['touched_count']}/{s['total_valid_matches']}",
                    fmt_pct(s["touched_rate_all"]),
                    fmt_pct(s["rebound_pct"]),
                    fmt_price(s["rebound_price_now"]),
                    f"{s['rebound_hits_after_pullback']}/{s['touched_count']}",
                    fmt_pct(s["rebound_rate_after_pullback"]),
                    f"{s['p75_hits_after_pullback']}/{s['touched_count']}",
                    fmt_pct(s["p75_rate_after_pullback"]),
                    fmt_days(s["avg_days_to_pullback"]),
                    fmt_days(s["avg_days_to_rebound"]),
                ]
            )

        text += md_table(
            [
                "Discesa",
                "Prezzo discesa",
                "Casi scesi",
                "% casi scesi",
                "Target rimbalzo",
                "Prezzo rimbalzo",
                "Poi target",
                "% poi target",
                "Poi P75",
                "% poi P75",
                "Giorni al minimo",
                "Giorni al target",
            ],
            detail_rows,
        )

        text += "\n\n### Traduzione semplice\n\n"

        for s in asset_summaries:
            if s["pullback_pct"] == -5 and s["rebound_pct"] in REBOUND_TARGETS:
                text += f"- {simple_bounce_interpretation(s)}\n"

        text += "\n---\n"

    return text


def build_dump_section(dump_summaries):
    quick_rows = []

    for asset in TARGETS:
        best = best_dump_for_asset(dump_summaries, asset)

        if best is None:
            quick_rows.append([asset_short(asset), "n/d", "n/d", "n/d", "dati insufficienti"])
            continue

        quick_rows.append(
            [
                asset_short(asset),
                fmt_price(best["spike_price_now"]),
                f"{best['touched_count']}/{best['total_valid_matches']}",
                fmt_pct(best["dump_rate_after_spike"]),
                simple_dump_interpretation(best),
            ]
        )

    text = f"""
# 2. Dump dopo spike

Questa sezione risponde alla domanda contraria:

> Se prima sale forte, storicamente poi scarica?

Lettura base: **spike +10%** e poi **scarico -5%**.

{md_table(
    [
        "Asset",
        "Zona +10% oggi",
        "Casi con spike",
        "Poi dump -5%",
        "Traduzione",
    ],
    quick_rows,
)}

"""

    for asset in TARGETS:
        asset_summaries = [s for s in dump_summaries if s["asset"] == asset]

        text += f"\n## {asset_name(asset)} — dump dopo spike\n\n"

        if not asset_summaries:
            text += "Dati insufficienti.\n\n---\n"
            continue

        current_price = asset_summaries[0].get("current_price")
        p25_pct = asset_summaries[0].get("p25_pct")
        p25_price = asset_summaries[0].get("p25_price_now")

        text += f"Prezzo attuale usato: **{fmt_price(current_price)}**  \n"
        text += f"Zona rischio P25 usata: **{fmt_pct(p25_pct)} → {fmt_price(p25_price)}**\n\n"

        detail_rows = []

        for s in asset_summaries:
            detail_rows.append(
                [
                    fmt_pct(s["spike_pct"]),
                    fmt_price(s["spike_price_now"]),
                    f"{s['touched_count']}/{s['total_valid_matches']}",
                    fmt_pct(s["touched_rate_all"]),
                    fmt_dump_level(s["dump_pct"]),
                    fmt_price(s["dump_price_now"]),
                    f"{s['dump_hits_after_spike']}/{s['touched_count']}",
                    fmt_pct(s["dump_rate_after_spike"]),
                    f"{s['p25_hits_after_spike']}/{s['touched_count']}",
                    fmt_pct(s["p25_rate_after_spike"]),
                    fmt_days(s["avg_days_to_spike"]),
                    fmt_days(s["avg_days_to_dump"]),
                ]
            )

        text += md_table(
            [
                "Spike",
                "Prezzo spike",
                "Casi spike",
                "% casi spike",
                "Target dump",
                "Prezzo dump",
                "Poi dump",
                "% poi dump",
                "Poi P25",
                "% poi P25",
                "Giorni allo spike",
                "Giorni al dump",
            ],
            detail_rows,
        )

        text += "\n\n### Traduzione semplice\n\n"

        for s in asset_summaries:
            if s["spike_pct"] == 10 and s["dump_pct"] in [0, -5, -10]:
                text += f"- {simple_dump_interpretation(s)}\n"

        text += "\n---\n"

    return text


def build_full_report(bounce_summaries, dump_summaries):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    text = f"""# Sequenze dopo il pattern: rimbalzo e dump

Generato: **{rome_now}**  
UTC: **{utc_now}**

Questo report controlla l'ordine degli eventi nei 40 casi storici più simili.

Non guarda solo se durante i 30 giorni c'è stato un minimo e un massimo.  
Controlla proprio la sequenza temporale:

```text
1. prima scende → poi rimbalza
2. prima sale/spike → poi scarica
