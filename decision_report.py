import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"

PREDICTION_LOG_PATH = "reports/prediction_log.csv"
SEQUENCE_CSV_PATH = "reports/bounce_after_drawdown_metrics.csv"
LIQUIDATION_CSV_PATH = "reports/liquidation_metrics.csv"

DECISION_REPORT_PATH = "reports/decision_report.md"
DECISION_CSV_PATH = "reports/decision_metrics.csv"

TARGETS = ["BTC-USD", "SOL-USD", "DOGE-USD"]


def asset_short(asset):
    return str(asset).replace("-USD", "")


def asset_name(asset):
    names = {
        "BTC-USD": "Bitcoin",
        "SOL-USD": "Solana",
        "DOGE-USD": "Dogecoin",
    }
    return names.get(asset, asset)


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


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")

    return "\n".join(lines)


def find_col(df, aliases):
    if df.empty:
        return None

    lower_map = {str(c).lower(): c for c in df.columns}

    for alias in aliases:
        if alias.lower() in lower_map:
            return lower_map[alias.lower()]

    for col in df.columns:
        col_lower = str(col).lower()
        for alias in aliases:
            if alias.lower() in col_lower:
                return col

    return None


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


def latest_prediction_time(asset):
    log = read_csv_safe(PREDICTION_LOG_PATH)

    if log.empty:
        return None

    if "asset" not in log.columns:
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
        value = rows.iloc[-1].get("generated_at_utc")
        return str(value)

    return None


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


def numeric_series(df, aliases):
    col = find_col(df, aliases)

    if col is None:
        return pd.Series(dtype=float)

    return pd.to_numeric(df[col], errors="coerce").dropna()


def compute_fractal_stats(asset):
    matches = read_csv_safe(matches_path(asset))
    current_price = latest_current_price(asset)

    stats = {
        "asset": asset,
        "current_price": current_price,
        "match_count": 0,
        "similarity_avg": None,
        "return_30d_avg": None,
        "return_30d_median": None,
        "positive_rate_30d": None,
        "drawdown_30d_avg": None,
        "drawdown_30d_p25": None,
        "max_gain_30d_avg": None,
        "max_gain_30d_p75": None,
    }

    if matches.empty:
        return stats

    stats["match_count"] = len(matches)

    sim = numeric_series(matches, ["similarity", "similarity_score", "score"])
    ret = numeric_series(matches, ["return_30d", "return_30d_pct"])
    dd = numeric_series(matches, ["drawdown_30d", "drawdown_30d_pct"])
    mg = numeric_series(matches, ["max_gain_30d", "max_gain_30d_pct"])

    if len(sim) > 0:
        stats["similarity_avg"] = float(sim.mean())

    if len(ret) > 0:
        stats["return_30d_avg"] = float(ret.mean())
        stats["return_30d_median"] = float(ret.median())
        stats["positive_rate_30d"] = float((ret > 0).mean() * 100)

    if len(dd) > 0:
        stats["drawdown_30d_avg"] = float(dd.mean())
        stats["drawdown_30d_p25"] = float(np.percentile(dd, 25))
    else:
        stats["drawdown_30d_p25"] = percentile_metric_pct(asset, matches, "drawdown_30d", 25)

    if len(mg) > 0:
        stats["max_gain_30d_avg"] = float(mg.mean())
        stats["max_gain_30d_p75"] = float(np.percentile(mg, 75))
    else:
        stats["max_gain_30d_p75"] = percentile_metric_pct(asset, matches, "max_gain_30d", 75)

    if stats["drawdown_30d_p25"] is None:
        stats["drawdown_30d_p25"] = percentile_metric_pct(asset, matches, "drawdown_30d", 25)

    if stats["max_gain_30d_p75"] is None:
        stats["max_gain_30d_p75"] = percentile_metric_pct(asset, matches, "max_gain_30d", 75)

    return stats


def load_sequence_summary(asset, sequence_type, first_pct, second_pct):
    df = read_csv_safe(SEQUENCE_CSV_PATH)

    if df.empty:
        return {}

    required = {"asset", "sequence_type", "first_pct", "second_pct"}

    if not required.issubset(df.columns):
        return {}

    rows = df[
        (df["asset"].astype(str) == asset)
        & (df["sequence_type"].astype(str) == sequence_type)
        & (pd.to_numeric(df["first_pct"], errors="coerce") == first_pct)
        & (pd.to_numeric(df["second_pct"], errors="coerce") == second_pct)
    ]

    if rows.empty:
        return {}

    row = rows.iloc[-1]

    return {
        "first_price_now": safe_float(row.get("first_price_now")),
        "second_price_now": safe_float(row.get("second_price_now")),
        "total_valid": safe_float(row.get("total_valid")),
        "first_hits": safe_float(row.get("first_hits")),
        "first_rate": safe_float(row.get("first_rate")),
        "second_hits_after_first": safe_float(row.get("second_hits_after_first")),
        "second_rate_after_first": safe_float(row.get("second_rate_after_first")),
        "real_move_from_first_to_second_pct": safe_float(
            row.get("real_move_from_first_to_second_pct")
        ),
        "avg_days_to_first": safe_float(row.get("avg_days_to_first")),
        "avg_days_to_second": safe_float(row.get("avg_days_to_second")),
    }


def normalize_funding_to_pct(value, col_name):
    value = safe_float(value)

    if value is None:
        return None

    name = str(col_name).lower()

    if "pct" in name or "percent" in name:
        return value

    if abs(value) < 1:
        return value * 100

    return value


def load_futures_stats(asset):
    df = read_csv_safe(LIQUIDATION_CSV_PATH)

    result = {
        "funding_rate_pct": None,
        "long_short_ratio": None,
        "open_interest_change_pct": None,
        "futures_note": "dati futures non disponibili",
    }

    if df.empty:
        return result

    asset_col = find_col(df, ["asset", "symbol", "ticker"])

    if asset_col is None:
        return result

    rows = df[df[asset_col].astype(str) == asset]

    if rows.empty:
        short = asset_short(asset)
        rows = df[df[asset_col].astype(str).str.contains(short, case=False, na=False)]

    if rows.empty:
        return result

    row = rows.iloc[-1]

    funding_col = find_col(df, ["funding_rate_pct", "funding_pct", "funding_rate", "funding"])
    ls_col = find_col(df, ["long_short_ratio", "longShortRatio", "long_short", "ls_ratio"])
    oi_col = find_col(
        df,
        [
            "open_interest_change_pct",
            "oi_change_pct",
            "open_interest_24h_change_pct",
            "open_interest_change",
            "oi_change",
        ],
    )

    if funding_col is not None:
        result["funding_rate_pct"] = normalize_funding_to_pct(row.get(funding_col), funding_col)

    if ls_col is not None:
        result["long_short_ratio"] = safe_float(row.get(ls_col))

    if oi_col is not None:
        result["open_interest_change_pct"] = safe_float(row.get(oi_col))

    notes = []

    funding = result["funding_rate_pct"]
    ratio = result["long_short_ratio"]
    oi_change = result["open_interest_change_pct"]

    if funding is not None:
        if funding > 0.08:
            notes.append("funding alto: long affollati")
        elif funding > 0.03:
            notes.append("funding positivo: leggero affollamento long")
        elif funding < -0.05:
            notes.append("funding negativo: possibile squeeze contro gli short")
        else:
            notes.append("funding neutro")

    if ratio is not None:
        if ratio >= 1.4:
            notes.append("long/short molto sbilanciato sui long")
        elif ratio >= 1.15:
            notes.append("più long che short")
        elif ratio <= 0.7:
            notes.append("molti short aperti")
        else:
            notes.append("long/short abbastanza neutro")

    if oi_change is not None:
        if oi_change > 8:
            notes.append("open interest in forte aumento")
        elif oi_change < -8:
            notes.append("open interest in forte calo")

    if notes:
        result["futures_note"] = "; ".join(notes)

    return result


def price_from_pct(current_price, pct):
    current_price = safe_float(current_price)
    pct = safe_float(pct)

    if current_price is None or pct is None:
        return None

    return current_price * (1 + pct / 100)


def add_score(score, amount, reasons, reason):
    score += amount
    reasons.append(reason)
    return score


def build_decision(asset):
    stats = compute_fractal_stats(asset)

    bounce = load_sequence_summary(
        asset=asset,
        sequence_type="bounce",
        first_pct=-5,
        second_pct=10,
    )

    dump = load_sequence_summary(
        asset=asset,
        sequence_type="dump",
        first_pct=10,
        second_pct=-5,
    )

    futures = load_futures_stats(asset)

    current_price = stats.get("current_price")
    positive_rate = safe_float(stats.get("positive_rate_30d"))
    median_return = safe_float(stats.get("return_30d_median"))
    avg_return = safe_float(stats.get("return_30d_avg"))
    drawdown_p25 = safe_float(stats.get("drawdown_30d_p25"))
    max_gain_p75 = safe_float(stats.get("max_gain_30d_p75"))

    bounce_rate = safe_float(bounce.get("second_rate_after_first"))
    dump_rate = safe_float(dump.get("second_rate_after_first"))

    funding = safe_float(futures.get("funding_rate_pct"))
    long_short = safe_float(futures.get("long_short_ratio"))
    oi_change = safe_float(futures.get("open_interest_change_pct"))

    directional_score = 0.0
    risk_score = 0.0
    reasons = []
    risk_reasons = []

    if positive_rate is not None:
        if positive_rate >= 70:
            directional_score = add_score(
                directional_score,
                2.5,
                reasons,
                f"molti casi storici positivi a 30 giorni ({fmt_pct(positive_rate)})",
            )
        elif positive_rate >= 60:
            directional_score = add_score(
                directional_score,
                1.5,
                reasons,
                f"casi positivi sopra la media ({fmt_pct(positive_rate)})",
            )
        elif positive_rate >= 52:
            directional_score = add_score(
                directional_score,
                0.7,
                reasons,
                f"leggera maggioranza di casi positivi ({fmt_pct(positive_rate)})",
            )
        elif positive_rate <= 35:
            directional_score = add_score(
                directional_score,
                -2.0,
                reasons,
                f"pochi casi storici positivi ({fmt_pct(positive_rate)})",
            )
        elif positive_rate <= 45:
            directional_score = add_score(
                directional_score,
                -1.0,
                reasons,
                f"casi positivi sotto la media ({fmt_pct(positive_rate)})",
            )

    if median_return is not None:
        if median_return >= 8:
            directional_score = add_score(
                directional_score,
                2.0,
                reasons,
                f"mediana 30 giorni forte ({fmt_pct(median_return)})",
            )
        elif median_return >= 3:
            directional_score = add_score(
                directional_score,
                1.0,
                reasons,
                f"mediana 30 giorni positiva ({fmt_pct(median_return)})",
            )
        elif median_return <= -8:
            directional_score = add_score(
                directional_score,
                -2.0,
                reasons,
                f"mediana 30 giorni negativa ({fmt_pct(median_return)})",
            )
        elif median_return <= -3:
            directional_score = add_score(
                directional_score,
                -1.0,
                reasons,
                f"mediana 30 giorni debole ({fmt_pct(median_return)})",
            )

    if avg_return is not None:
        if avg_return >= 10:
            directional_score = add_score(
                directional_score,
                0.8,
                reasons,
                f"media 30 giorni positiva ({fmt_pct(avg_return)})",
            )
        elif avg_return <= -10:
            directional_score = add_score(
                directional_score,
                -0.8,
                reasons,
                f"media 30 giorni negativa ({fmt_pct(avg_return)})",
            )

    if max_gain_p75 is not None:
        if max_gain_p75 >= 20:
            directional_score = add_score(
                directional_score,
                0.8,
                reasons,
                f"potenziale rialzo storico P75 alto ({fmt_pct(max_gain_p75)})",
            )
        elif max_gain_p75 <= 8:
            directional_score = add_score(
                directional_score,
                -0.4,
                reasons,
                f"potenziale rialzo storico P75 basso ({fmt_pct(max_gain_p75)})",
            )

    if bounce_rate is not None:
        if bounce_rate >= 60:
            directional_score = add_score(
                directional_score,
                0.8,
                reasons,
                f"rimbalzo dopo -5% abbastanza frequente ({fmt_pct(bounce_rate)})",
            )
        elif bounce_rate >= 45:
            directional_score = add_score(
                directional_score,
                0.3,
                reasons,
                f"rimbalzo dopo -5% possibile ({fmt_pct(bounce_rate)})",
            )
        elif bounce_rate <= 30:
            directional_score = add_score(
                directional_score,
                -0.6,
                reasons,
                f"rimbalzo dopo -5% debole ({fmt_pct(bounce_rate)})",
            )

    if dump_rate is not None:
        if dump_rate >= 65:
            directional_score = add_score(
                directional_score,
                -1.0,
                reasons,
                f"dump dopo spike +10% frequente ({fmt_pct(dump_rate)})",
            )
        elif dump_rate >= 50:
            directional_score = add_score(
                directional_score,
                -0.5,
                reasons,
                f"dump dopo spike +10% da monitorare ({fmt_pct(dump_rate)})",
            )
        elif dump_rate <= 25:
            directional_score = add_score(
                directional_score,
                0.3,
                reasons,
                f"dump dopo spike poco frequente ({fmt_pct(dump_rate)})",
            )

    if funding is not None:
        if funding > 0.08:
            directional_score = add_score(
                directional_score,
                -0.5,
                reasons,
                f"funding alto: mercato long affollato ({fmt_pct(funding)})",
            )
        elif funding < -0.05:
            directional_score = add_score(
                directional_score,
                0.4,
                reasons,
                f"funding negativo: possibile squeeze contro short ({fmt_pct(funding)})",
            )

    if long_short is not None:
        if long_short >= 1.4:
            directional_score = add_score(
                directional_score,
                -0.4,
                reasons,
                f"long/short molto sbilanciato sui long ({fmt_number(long_short, 2)})",
            )
        elif long_short <= 0.7:
            directional_score = add_score(
                directional_score,
                0.3,
                reasons,
                f"molti short aperti: possibile squeeze ({fmt_number(long_short, 2)})",
            )

    if drawdown_p25 is not None:
        if drawdown_p25 <= -22:
            risk_score += 3.0
            risk_reasons.append(f"drawdown P25 molto pesante ({fmt_pct(drawdown_p25)})")
        elif drawdown_p25 <= -16:
            risk_score += 2.3
            risk_reasons.append(f"drawdown P25 pesante ({fmt_pct(drawdown_p25)})")
        elif drawdown_p25 <= -10:
            risk_score += 1.4
            risk_reasons.append(f"drawdown P25 importante ({fmt_pct(drawdown_p25)})")
        elif drawdown_p25 <= -7:
            risk_score += 0.8
            risk_reasons.append(f"drawdown P25 moderato ({fmt_pct(drawdown_p25)})")

    if dump_rate is not None and dump_rate >= 60:
        risk_score += 0.8
        risk_reasons.append(f"spike spesso scaricato ({fmt_pct(dump_rate)})")

    if bounce_rate is not None and bounce_rate <= 30:
        risk_score += 0.5
        risk_reasons.append(f"rimbalzo dopo discesa debole ({fmt_pct(bounce_rate)})")

    if oi_change is not None and oi_change > 8:
        risk_score += 0.5
        risk_reasons.append(f"open interest in aumento ({fmt_pct(oi_change)})")

    if funding is not None and funding > 0.08:
        risk_score += 0.5
        risk_reasons.append(f"funding alto ({fmt_pct(funding)})")

    match_count = stats.get("match_count", 0)

    if match_count < 25:
        risk_score += 0.8
        risk_reasons.append("pochi match validi")

    if risk_score >= 3.2:
        risk_label = "MOLTO ALTO"
    elif risk_score >= 2.1:
        risk_label = "ALTO"
    elif risk_score >= 1.1:
        risk_label = "MEDIO"
    else:
        risk_label = "BASSO"

    if directional_score >= 3.2:
        direction = "BULLISH"
    elif directional_score >= 1.3:
        direction = "LEGGERMENTE BULLISH"
    elif directional_score <= -3.2:
        direction = "BEARISH"
    elif directional_score <= -1.3:
        direction = "LEGGERMENTE BEARISH"
    else:
        direction = "NEUTRALE / INCERTO"

    if direction == "BULLISH":
        if risk_label in ["BASSO", "MEDIO"]:
            spot_action = "COMPRA / ACCUMULA"
        else:
            spot_action = "ACCUMULA SOLO SU PULLBACK"
    elif direction == "LEGGERMENTE BULLISH":
        spot_action = "ACCUMULA SOLO SU PULLBACK"
    elif direction == "BEARISH":
        spot_action = "VENDI PARZIALE / STAI FUORI"
    elif direction == "LEGGERMENTE BEARISH":
        spot_action = "TAKE PROFIT SU SPIKE / NON INSEGUIRE"
    else:
        spot_action = "ASPETTA / HOLD"

    leverage_action = "NO LEVA"
    leverage_direction = "nessuna"
    max_leverage = "spot / 1x"

    if directional_score >= 3.2 and risk_label == "BASSO":
        leverage_action = "LONG POSSIBILE MA SOLO BASSO"
        leverage_direction = "long"
        max_leverage = "max 3x isolated"
    elif directional_score >= 2.2 and risk_label in ["BASSO", "MEDIO"]:
        leverage_action = "LONG PRUDENTE"
        leverage_direction = "long"
        max_leverage = "max 2x isolated"
    elif directional_score <= -3.2 and risk_label in ["BASSO", "MEDIO"]:
        leverage_action = "SHORT PRUDENTE"
        leverage_direction = "short"
        max_leverage = "max 2x isolated"
    elif directional_score <= -2.2 and dump_rate is not None and dump_rate >= 55:
        leverage_action = "SHORT SOLO DOPO SPIKE"
        leverage_direction = "short condizionato"
        max_leverage = "max 2x isolated"
    else:
        leverage_action = "NO LEVA"
        leverage_direction = "nessuna"
        max_leverage = "spot / 1x"

    if risk_label in ["ALTO", "MOLTO ALTO"] and leverage_action != "NO LEVA":
        leverage_action = "LEVA SCONSIGLIATA"
        leverage_direction = "nessuna"
        max_leverage = "spot / 1x"

    pullback_zone = bounce.get("first_price_now")
    bounce_target = bounce.get("second_price_now")
    spike_zone = dump.get("first_price_now")
    dump_target = dump.get("second_price_now")

    drawdown_p25_price = price_from_pct(current_price, drawdown_p25)
    max_gain_p75_price = price_from_pct(current_price, max_gain_p75)

    plan_parts = []

    if spot_action in ["COMPRA / ACCUMULA", "ACCUMULA SOLO SU PULLBACK"]:
        if pullback_zone is not None:
            plan_parts.append(f"zona accumulo/pullback: circa {fmt_price(pullback_zone)}")
        else:
            plan_parts.append("accumulo solo su prezzo migliore")
    elif "TAKE PROFIT" in spot_action:
        if spike_zone is not None:
            plan_parts.append(f"prendere profitto su spike verso {fmt_price(spike_zone)}")
        else:
            plan_parts.append("prendere profitto su spike")
    elif "VENDI" in spot_action:
        plan_parts.append("ridurre esposizione, evitare nuovi long")
    else:
        plan_parts.append("aspettare conferma, non forzare entrate")

    if spike_zone is not None:
        plan_parts.append(f"zona spike/attenzione: circa {fmt_price(spike_zone)}")

    if drawdown_p25_price is not None:
        plan_parts.append(f"zona rischio storica P25: circa {fmt_price(drawdown_p25_price)}")

    if max_gain_p75_price is not None:
        plan_parts.append(f"target rialzo storico P75: circa {fmt_price(max_gain_p75_price)}")

    if not reasons:
        reasons.append("dati insufficienti o segnali misti")

    if not risk_reasons:
        risk_reasons.append("rischio non eccessivo dai dati disponibili")

    decision = {
        "asset": asset,
        "asset_short": asset_short(asset),
        "current_price": current_price,
        "generated_at_utc": latest_prediction_time(asset),
        "directional_score": directional_score,
        "risk_score": risk_score,
        "direction": direction,
        "risk_label": risk_label,
        "spot_action": spot_action,
        "leverage_action": leverage_action,
        "leverage_direction": leverage_direction,
        "max_leverage": max_leverage,
        "positive_rate_30d": positive_rate,
        "return_30d_median": median_return,
        "return_30d_avg": avg_return,
        "drawdown_30d_p25": drawdown_p25,
        "max_gain_30d_p75": max_gain_p75,
        "bounce_rate_after_pullback": bounce_rate,
        "dump_rate_after_spike": dump_rate,
        "funding_rate_pct": funding,
        "long_short_ratio": long_short,
        "open_interest_change_pct": oi_change,
        "pullback_zone": pullback_zone,
        "bounce_target": bounce_target,
        "spike_zone": spike_zone,
        "dump_target": dump_target,
        "drawdown_p25_price": drawdown_p25_price,
        "max_gain_p75_price": max_gain_p75_price,
        "main_reasons": "; ".join(reasons[:6]),
        "risk_reasons": "; ".join(risk_reasons[:5]),
        "plan": "; ".join(plan_parts),
        "futures_note": futures.get("futures_note"),
    }

    return decision


def build_dashboard(decisions):
    rows = []

    for d in decisions:
        rows.append(
            [
                d["asset_short"],
                fmt_price(d["current_price"]),
                d["direction"],
                d["spot_action"],
                d["leverage_action"],
                d["max_leverage"],
                d["risk_label"],
                d["plan"],
            ]
        )

    return md_table(
        [
            "Asset",
            "Prezzo",
            "Direzione scanner",
            "Spot",
            "Leva",
            "Max leva",
            "Rischio",
            "Piano pratico",
        ],
        rows,
    )


def build_simple_verdict(d):
    asset = d["asset_short"]

    lines = []

    lines.append(f"## {asset_name(d['asset'])} — {asset}")
    lines.append("")
    lines.append(f"Prezzo usato: **{fmt_price(d['current_price'])}**")
    lines.append("")
    lines.append(f"- **Direzione scanner:** {d['direction']}")
    lines.append(f"- **Azione spot:** {d['spot_action']}")
    lines.append(f"- **Leva:** {d['leverage_action']}")
    lines.append(f"- **Max leva prudente:** {d['max_leverage']}")
    lines.append(f"- **Rischio:** {d['risk_label']}")
    lines.append("")
    lines.append("### Perché")
    lines.append("")
    lines.append(f"- {d['main_reasons']}")
    lines.append("")
    lines.append("### Rischi principali")
    lines.append("")
    lines.append(f"- {d['risk_reasons']}")
    lines.append("")
    lines.append("### Numeri utili")
    lines.append("")
    lines.append(
        md_table(
            [
                "Dato",
                "Valore",
            ],
            [
                ["Casi positivi 30 giorni", fmt_pct(d["positive_rate_30d"])],
                ["Rendimento mediano 30 giorni", fmt_pct(d["return_30d_median"])],
                ["Drawdown storico P25", fmt_pct(d["drawdown_30d_p25"])],
                ["Max gain storico P75", fmt_pct(d["max_gain_30d_p75"])],
                ["Rimbalzo dopo -5% → +10%", fmt_pct(d["bounce_rate_after_pullback"])],
                ["Dump dopo +10% → -5%", fmt_pct(d["dump_rate_after_spike"])],
                ["Funding", fmt_pct(d["funding_rate_pct"])],
                ["Long/Short ratio", fmt_number(d["long_short_ratio"], 2)],
                ["Open interest change", fmt_pct(d["open_interest_change_pct"])],
            ],
        )
    )
    lines.append("")
    lines.append("### Aree operative secondo lo scanner")
    lines.append("")
    lines.append(
        md_table(
            [
                "Area",
                "Prezzo",
                "Uso pratico",
            ],
            [
                [
                    "Pullback -5%",
                    fmt_price(d["pullback_zone"]),
                    "zona dove valutare accumulo, se il resto resta favorevole",
                ],
                [
                    "Target rimbalzo +10%",
                    fmt_price(d["bounce_target"]),
                    "zona obiettivo dopo pullback",
                ],
                [
                    "Spike +10%",
                    fmt_price(d["spike_zone"]),
                    "zona dove evitare di inseguire, valutare profitto",
                ],
                [
                    "Dump -5%",
                    fmt_price(d["dump_target"]),
                    "zona di scarico dopo spike",
                ],
                [
                    "Drawdown P25",
                    fmt_price(d["drawdown_p25_price"]),
                    "zona rischio storica; la liquidazione dovrebbe stare oltre questa zona",
                ],
                [
                    "Max gain P75",
                    fmt_price(d["max_gain_p75_price"]),
                    "zona rialzista storica favorevole",
                ],
            ],
        )
    )
    lines.append("")
    lines.append("### Piano sintetico")
    lines.append("")
    lines.append(f"> {d['plan']}")
    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def build_decision_report(decisions):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []

    lines.append("# Decisione operativa sintetica")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{utc_now}**")
    lines.append("")
    lines.append("Questo report trasforma i dati dello scanner in una lettura operativa.")
    lines.append("")
    lines.append("Non è un ordine automatico. È una bussola:")
    lines.append("")
    lines.append("- cosa favorisce lo scanner;")
    lines.append("- cosa evitare;")
    lines.append("- se ha senso spot, long, short o nessuna leva;")
    lines.append("- quanta leva massima usare in modo prudente.")
    lines.append("")
    lines.append("Regola dura usata dal file:")
    lines.append("")
    lines.append("> se il rischio è alto o i segnali sono misti, la leva viene sconsigliata.")
    lines.append("")
    lines.append("## Dashboard veloce")
    lines.append("")
    lines.append(build_dashboard(decisions))
    lines.append("")
    lines.append("## Come leggere le decisioni")
    lines.append("")
    lines.append("- **COMPRA / ACCUMULA**: il quadro statistico favorisce rialzo, ma sempre con gestione del rischio.")
    lines.append("- **ACCUMULA SOLO SU PULLBACK**: non inseguire il prezzo; comprare solo su discesa.")
    lines.append("- **HOLD / ASPETTA**: dati misti; meglio non forzare.")
    lines.append("- **TAKE PROFIT SU SPIKE**: se sale forte, lo scanner preferisce prudenza.")
    lines.append("- **SHORT PRUDENTE**: possibile solo se i dati sono ribassisti e il rischio non è alto.")
    lines.append("- **NO LEVA**: la leva non compensa il rischio storico.")
    lines.append("")
    lines.append("## Dettaglio per asset")
    lines.append("")

    for d in decisions:
        lines.append(build_simple_verdict(d))

    return "\n".join(lines)


def build_main_report_block(decisions):
    rows = []

    for d in decisions:
        rows.append(
            [
                d["asset_short"],
                d["direction"],
                d["spot_action"],
                d["leverage_action"],
                d["max_leverage"],
                d["risk_label"],
            ]
        )

    strongest = sorted(decisions, key=lambda x: x["directional_score"], reverse=True)
    riskiest = sorted(decisions, key=lambda x: x["risk_score"], reverse=True)

    best = strongest[0] if strongest else None
    worst_risk = riskiest[0] if riskiest else None

    quick_lines = []

    if best is not None:
        quick_lines.append(
            f"- Asset più forte secondo lo scanner: **{best['asset_short']}** "
            f"({best['direction']}, score {fmt_number(best['directional_score'], 2)})."
        )

    if worst_risk is not None:
        quick_lines.append(
            f"- Asset più rischioso: **{worst_risk['asset_short']}** "
            f"(rischio {worst_risk['risk_label']})."
        )

    for d in decisions:
        quick_lines.append(
            f"- **{d['asset_short']}**: spot = **{d['spot_action']}**, "
            f"leva = **{d['leverage_action']}**, max = **{d['max_leverage']}**."
        )

    return "\n".join(
        [
            "<!-- DECISION_REPORT_START -->",
            "",
            "# Decisione operativa sintetica",
            "",
            "Report separato completo: [decision_report.md](decision_report.md)",
            "",
            "Questa è la sintesi automatica dello scanner. Trasforma frattali, drawdown, sequenze e futures in una bussola operativa.",
            "",
            md_table(
                [
                    "Asset",
                    "Direzione",
                    "Spot",
                    "Leva",
                    "Max leva",
                    "Rischio",
                ],
                rows,
            ),
            "",
            "## Lettura immediata",
            "",
            "\n".join(quick_lines),
            "",
            "Nota: la leva è limitata apposta. Se i dati sono misti o il rischio è alto, il file preferisce **NO LEVA**.",
            "",
            "<!-- DECISION_REPORT_END -->",
        ]
    )


def inject_into_main_report(decisions):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- DECISION_REPORT_START -->"
    end_marker = "<!-- DECISION_REPORT_END -->"

    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    block = build_main_report_block(decisions).strip()

    new_text = block + "\n\n" + current.lstrip()

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def write_csv(decisions):
    df = pd.DataFrame(decisions)
    df.to_csv(DECISION_CSV_PATH, index=False)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    decisions = []

    for asset in TARGETS:
        decisions.append(build_decision(asset))

    report = build_decision_report(decisions)

    with open(DECISION_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    write_csv(decisions)
    inject_into_main_report(decisions)

    print(f"Wrote {DECISION_REPORT_PATH}")
    print(f"Wrote {DECISION_CSV_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
