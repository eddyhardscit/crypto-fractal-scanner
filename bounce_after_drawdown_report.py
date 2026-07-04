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

# Prima scende, poi rimbalza.
PULLBACK_LEVELS = [-5, -10, -15]
REBOUND_TARGETS = [10, 20]

# Prima sale, poi scarica.
SPIKE_LEVELS = [10, 20]
DUMP_TARGETS = [0, -5, -10]


def asset_name(asset):
    names = {
        "BTC-USD": "Bitcoin",
        "SOL-USD": "Solana",
        "DOGE-USD": "Dogecoin",
    }
    return names.get(asset, asset)


def asset_short(asset):
    return str(asset).replace("-USD", "")


def matches_path(asset):
    return f"reports/{asset_short(asset)}_matches.csv"


def percentiles_path(asset):
    return f"reports/{asset_short(asset)}_percentiles.csv"


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
    all_rows = []

    for asset in TARGETS:
        path = matches_path(asset)
        matches = read_csv_safe(path)

        if matches.empty:
            continue

        matches["target_asset"] = asset
        all_rows.append(matches)

    if not all_rows:
        return pd.DataFrame()

    return pd.concat(all_rows, ignore_index=True)


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
    prima scende almeno a pullback_pct,
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
    prima sale almeno a spike_pct,
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

    text = []
    text.append("# 1. Rimbalzo dopo drawdown\n")
    text.append("Questa sezione risponde alla domanda:\n")
    text.append("> Se prima scende, storicamente poi rimbalza?\n")
    text.append("Lettura base: **discesa -5%** e poi **rimbalzo +10%**.\n")
    text.append(md_table(
        [
            "Asset",
            "Zona -5% oggi",
            "Casi scesi",
            "Poi rimbalzo +10%",
            "Traduzione",
        ],
        quick_rows,
    ))
    text.append("")

    for asset in TARGETS:
        asset_summaries = [s for s in bounce_summaries if s["asset"] == asset]

        text.append(f"\n## {asset_name(asset)} — rimbalzo dopo discesa\n")

        if not asset_summaries:
            text.append("Dati insufficienti.\n\n---")
            continue

        current_price = asset_summaries[0].get("current_price")
        p75_pct = asset_summaries[0].get("p75_pct")
        p75_price = asset_summaries[0].get("p75_price_now")

        text.append(f"Prezzo attuale usato: **{fmt_price(current_price)}**  ")
        text.append(f"Zona rialzo P75 usata: **{fmt_pct(p75_pct)} → {fmt_price(p75_price)}**\n")

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

        text.append(md_table(
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
        ))

        text.append("\n### Traduzione semplice\n")

        for s in asset_summaries:
            if s["pullback_pct"] == -5 and s["rebound_pct"] in REBOUND_TARGETS:
                text.append(f"- {simple_bounce_interpretation(s)}")

        text.append("\n---")

    return "\n".join(text)


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

    text = []
    text.append("# 2. Dump dopo spike\n")
    text.append("Questa sezione risponde alla domanda contraria:\n")
    text.append("> Se prima sale forte, storicamente poi scarica?\n")
    text.append("Lettura base: **spike +10%** e poi **scarico -5%**.\n")
    text.append(md_table(
        [
            "Asset",
            "Zona +10% oggi",
            "Casi con spike",
            "Poi dump -5%",
            "Traduzione",
        ],
        quick_rows,
    ))
    text.append("")

    for asset in TARGETS:
        asset_summaries = [s for s in dump_summaries if s["asset"] == asset]

        text.append(f"\n## {asset_name(asset)} — dump dopo spike\n")

        if not asset_summaries:
            text.append("Dati insufficienti.\n\n---")
            continue

        current_price = asset_summaries[0].get("current_price")
        p25_pct = asset_summaries[0].get("p25_pct")
        p25_price = asset_summaries[0].get("p25_price_now")

        text.append(f"Prezzo attuale usato: **{fmt_price(current_price)}**  ")
        text.append(f"Zona rischio P25 usata: **{fmt_pct(p25_pct)} → {fmt_price(p25_price)}**\n")

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

        text.append(md_table(
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
        ))

        text.append("\n### Traduzione semplice\n")

        for s in asset_summaries:
            if s["spike_pct"] == 10 and s["dump_pct"] in [0, -5, -10]:
                text.append(f"- {simple_dump_interpretation(s)}")

        text.append("\n---")

    return "\n".join(text)


def build_full_report(bounce_summaries, dump_summaries):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    parts = []
    parts.append("# Sequenze dopo il pattern: rimbalzo e dump\n")
    parts.append(f"Generato: **{rome_now}**  ")
    parts.append(f"UTC: **{utc_now}**\n")
    parts.append("Questo report controlla l'ordine degli eventi nei 40 casi storici più simili.\n")
    parts.append("Non guarda solo se durante i 30 giorni c'è stato un minimo e un massimo.")
    parts.append("Controlla proprio la sequenza temporale:\n")
    parts.append("- prima scende → poi rimbalza")
    parts.append("- prima sale/spike → poi scarica\n")
    parts.append("## Come usarlo\n")
    parts.append("- **Rimbalzo dopo drawdown**: utile per capire se una discesa può diventare zona di rimbalzo.")
    parts.append("- **Dump dopo spike**: utile per capire se una salita forte può diventare zona da prendere profitto.")
    parts.append("- Non è una certezza. È una statistica storica sui casi più simili.\n")
    parts.append("---\n")
    parts.append(build_bounce_section(bounce_summaries))
    parts.append("\n\n")
    parts.append(build_dump_section(dump_summaries))

    return "\n".join(parts)


def build_main_report_block(bounce_summaries, dump_summaries):
    bounce_rows = []
    dump_rows = []
    simple_lines = []

    for asset in TARGETS:
        best_bounce = best_bounce_for_asset(bounce_summaries, asset)

        if best_bounce is None:
            bounce_rows.append([asset_short(asset), "n/d", "n/d", "n/d", "n/d"])
            simple_lines.append(f"- **{asset_short(asset)} rimbalzo**: dati insufficienti.")
        else:
            bounce_rows.append(
                [
                    asset_short(asset),
                    fmt_price(best_bounce["pullback_price_now"]),
                    f"{best_bounce['touched_count']}/{best_bounce['total_valid_matches']}",
                    fmt_pct(best_bounce["rebound_rate_after_pullback"]),
                    simple_strength(best_bounce["rebound_rate_after_pullback"]),
                ]
            )
            simple_lines.append(f"- **{simple_bounce_interpretation(best_bounce)}**")

    for asset in TARGETS:
        best_dump = best_dump_for_asset(dump_summaries, asset)

        if best_dump is None:
            dump_rows.append([asset_short(asset), "n/d", "n/d", "n/d", "n/d"])
            simple_lines.append(f"- **{asset_short(asset)} dump**: dati insufficienti.")
        else:
            dump_rows.append(
                [
                    asset_short(asset),
                    fmt_price(best_dump["spike_price_now"]),
                    f"{best_dump['touched_count']}/{best_dump['total_valid_matches']}",
                    fmt_pct(best_dump["dump_rate_after_spike"]),
                    simple_strength(best_dump["dump_rate_after_spike"]),
                ]
            )
            simple_lines.append(f"- **{simple_dump_interpretation(best_dump)}**")

    return "\n".join([
        "<!-- BOUNCE_AFTER_DRAWDOWN_START -->",
        "",
        "---",
        "",
        "# Sequenze: rimbalzo dopo discesa / dump dopo spike",
        "",
        "Report separato completo: [bounce_after_drawdown_report.md](bounce_after_drawdown_report.md)",
        "",
        "Questa sezione controlla l'ordine degli eventi:",
        "",
        "- prima scende → poi rimbalza",
        "- prima sale → poi scarica",
        "",
        "## 1. Rimbalzo dopo drawdown",
        "",
        "Lettura base: **discesa -5%** e poi **rimbalzo +10%**.",
        "",
        md_table(
            [
                "Asset",
                "Zona -5% oggi",
                "Casi scesi",
                "Poi rimbalzo +10%",
                "Forza",
            ],
            bounce_rows,
        ),
        "",
        "## 2. Dump dopo spike",
        "",
        "Lettura base: **spike +10%** e poi **dump -5%**.",
        "",
        md_table(
            [
                "Asset",
                "Zona +10% oggi",
                "Casi spike",
                "Poi dump -5%",
                "Forza",
            ],
            dump_rows,
        ),
        "",
        "## Traduzione veloce",
        "",
        "\n".join(simple_lines),
        "",
        "<!-- BOUNCE_AFTER_DRAWDOWN_END -->",
    ])


def inject_into_main_report(bounce_summaries, dump_summaries):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- BOUNCE_AFTER_DRAWDOWN_START -->"
    end_marker = "<!-- BOUNCE_AFTER_DRAWDOWN_END -->"

    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    block = build_main_report_block(bounce_summaries, dump_summaries).strip()

    daily_end = "<!-- DAILY_CHANGE_END -->"

    if daily_end in current:
        insert_pos = current.find(daily_end) + len(daily_end)
        new_text = (
            current[:insert_pos].rstrip()
            + "\n\n"
            + block
            + "\n\n"
            + current[insert_pos:].lstrip()
        )
    else:
        insertion_markers = [
            "\n# Come leggere questo report",
            "\n# Scheda veloce",
            "\n# Lettura velocissima",
            "\n## Lettura velocissima",
            "\n# Mappa semplice",
        ]

        insert_pos = None

        for marker in insertion_markers:
            pos = current.find(marker)
            if pos != -1:
                insert_pos = pos
                break

        if insert_pos is not None:
            new_text = (
                current[:insert_pos].rstrip()
                + "\n\n"
                + block
                + "\n\n"
                + current[insert_pos:].lstrip()
            )
        else:
            new_text = block + "\n\n" + current

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def write_csv(bounce_summaries, dump_summaries):
    rows = []

    for item in bounce_summaries:
        rows.append(item)

    for item in dump_summaries:
        rows.append(item)

    df = pd.DataFrame(rows)
    df.to_csv(BOUNCE_CSV_PATH, index=False)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    all_matches = build_all_matches()

    if all_matches.empty:
        report = "# Sequenze dopo il pattern\n\nNessun match disponibile.\n"

        with open(BOUNCE_REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)

        print("No matches available for sequence report.")
        return

    market_data = download_needed_data(all_matches)

    bounce_summaries = []
    dump_summaries = []

    for asset in TARGETS:
        path = matches_path(asset)
        matches = read_csv_safe(path)

        if matches.empty:
            continue

        current_price = latest_current_price(asset)
        p75_pct = max_gain_p75_pct(asset, matches)
        p25_pct = drawdown_p25_pct(asset, matches)

        for pullback_pct in PULLBACK_LEVELS:
            for rebound_pct in REBOUND_TARGETS:
                summary = summarize_bounce_condition(
                    asset=asset,
                    matches=matches,
                    data=market_data,
                    current_price=current_price,
                    pullback_pct=pullback_pct,
                    rebound_pct=rebound_pct,
                    p75_pct=p75_pct,
                )
                bounce_summaries.append(summary)

        for spike_pct in SPIKE_LEVELS:
            for dump_pct in DUMP_TARGETS:
                summary = summarize_dump_condition(
                    asset=asset,
                    matches=matches,
                    data=market_data,
                    current_price=current_price,
                    spike_pct=spike_pct,
                    dump_pct=dump_pct,
                    p25_pct=p25_pct,
                )
                dump_summaries.append(summary)

    report = build_full_report(bounce_summaries, dump_summaries)

    with open(BOUNCE_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    write_csv(bounce_summaries, dump_summaries)
    inject_into_main_report(bounce_summaries, dump_summaries)

    print(f"Wrote {BOUNCE_REPORT_PATH}")
    print(f"Wrote {BOUNCE_CSV_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
