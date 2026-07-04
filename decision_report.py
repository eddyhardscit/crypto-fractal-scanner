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

    if log.empty or "asset" not in log.columns:
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
        return str(rows.iloc[-1].get("generated_at_utc"))

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
        "return_30d_avg": None,
        "return_30d_median": None,
        "positive_rate_30d": None,
        "drawdown_30d_p25": None,
        "max_gain_30d_p75": None,
    }

    if matches.empty:
        return stats

    stats["match_count"] = len(matches)

    ret = numeric_series(matches, ["return_30d", "return_30d_pct"])
    dd = numeric_series(matches, ["drawdown_30d", "drawdown_30d_pct"])
    mg = numeric_series(matches, ["max_gain_30d", "max_gain_30d_pct"])

    if len(ret) > 0:
        stats["return_30d_avg"] = float(ret.mean())
        stats["return_30d_median"] = float(ret.median())
        stats["positive_rate_30d"] = float((ret > 0).mean() * 100)

    if len(dd) > 0:
        stats["drawdown_30d_p25"] = float(np.percentile(dd, 25))
    else:
        stats["drawdown_30d_p25"] = percentile_metric_pct(asset, matches, "drawdown_30d", 25)

    if len(mg) > 0:
        stats["max_gain_30d_p75"] = float(np.percentile(mg, 75))
    else:
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
            notes.append("funding alto: molti long affollati")
        elif funding > 0.03:
            notes.append("funding positivo: leggera pressione long")
        elif funding < -0.05:
            notes.append("funding negativo: tanti short pagano funding")
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

    score = 0.0
    risk_score = 0.0
    reasons = []
    risk_reasons = []

    # Direzione frattale.
    if positive_rate is not None:
        if positive_rate >= 70:
            score = add_score(score, 2.5, reasons, f"molti casi storici chiudevano positivi ({fmt_pct(positive_rate)})")
        elif positive_rate >= 60:
            score = add_score(score, 1.5, reasons, f"casi positivi sopra la media ({fmt_pct(positive_rate)})")
        elif positive_rate >= 52:
            score = add_score(score, 0.6, reasons, f"leggera maggioranza positiva ({fmt_pct(positive_rate)})")
        elif positive_rate <= 35:
            score = add_score(score, -2.0, reasons, f"pochi casi storici positivi ({fmt_pct(positive_rate)})")
        elif positive_rate <= 45:
            score = add_score(score, -1.0, reasons, f"casi positivi sotto la media ({fmt_pct(positive_rate)})")

    if median_return is not None:
        if median_return >= 8:
            score = add_score(score, 2.0, reasons, f"rendimento mediano forte ({fmt_pct(median_return)})")
        elif median_return >= 3:
            score = add_score(score, 1.0, reasons, f"rendimento mediano positivo ({fmt_pct(median_return)})")
        elif median_return <= -8:
            score = add_score(score, -2.0, reasons, f"rendimento mediano negativo ({fmt_pct(median_return)})")
        elif median_return <= -3:
            score = add_score(score, -1.0, reasons, f"rendimento mediano debole ({fmt_pct(median_return)})")

    if avg_return is not None:
        if avg_return >= 10:
            score = add_score(score, 0.8, reasons, f"media 30 giorni positiva ({fmt_pct(avg_return)})")
        elif avg_return <= -10:
            score = add_score(score, -0.8, reasons, f"media 30 giorni negativa ({fmt_pct(avg_return)})")

    if max_gain_p75 is not None:
        if max_gain_p75 >= 20:
            score = add_score(score, 0.7, reasons, f"zona alta storica abbastanza lontana ({fmt_pct(max_gain_p75)})")
        elif max_gain_p75 <= 8:
            score = add_score(score, -0.4, reasons, f"zona alta storica poco interessante ({fmt_pct(max_gain_p75)})")

    if bounce_rate is not None:
        if bounce_rate >= 60:
            score = add_score(score, 0.8, reasons, f"rimbalzo dopo discesa abbastanza frequente ({fmt_pct(bounce_rate)})")
        elif bounce_rate >= 45:
            score = add_score(score, 0.3, reasons, f"rimbalzo dopo discesa possibile ({fmt_pct(bounce_rate)})")
        elif bounce_rate <= 30:
            score = add_score(score, -0.6, reasons, f"rimbalzo dopo discesa debole ({fmt_pct(bounce_rate)})")

    if dump_rate is not None:
        if dump_rate >= 65:
            score = add_score(score, -1.0, reasons, f"dump dopo spike frequente ({fmt_pct(dump_rate)})")
        elif dump_rate >= 50:
            score = add_score(score, -0.5, reasons, f"dump dopo spike da monitorare ({fmt_pct(dump_rate)})")
        elif dump_rate <= 25:
            score = add_score(score, 0.3, reasons, f"dump dopo spike poco frequente ({fmt_pct(dump_rate)})")

    # Futures.
    if funding is not None:
        if funding > 0.08:
            score = add_score(score, -0.5, reasons, f"funding alto: long affollati ({fmt_pct(funding)})")
        elif funding < -0.05:
            score = add_score(score, 0.3, reasons, f"funding negativo: possibile squeeze contro short ({fmt_pct(funding)})")

    if long_short is not None:
        if long_short >= 1.4:
            score = add_score(score, -0.4, reasons, f"troppi long aperti ({fmt_number(long_short, 2)})")
        elif long_short <= 0.7:
            score = add_score(score, 0.3, reasons, f"molti short aperti: possibile squeeze ({fmt_number(long_short, 2)})")

    # Rischio.
    if drawdown_p25 is not None:
        if drawdown_p25 <= -22:
            risk_score += 3.0
            risk_reasons.append(f"zona bassa storica molto profonda ({fmt_pct(drawdown_p25)})")
        elif drawdown_p25 <= -16:
            risk_score += 2.3
            risk_reasons.append(f"zona bassa storica profonda ({fmt_pct(drawdown_p25)})")
        elif drawdown_p25 <= -10:
            risk_score += 1.4
            risk_reasons.append(f"zona bassa storica importante ({fmt_pct(drawdown_p25)})")
        elif drawdown_p25 <= -7:
            risk_score += 0.8
            risk_reasons.append(f"zona bassa storica moderata ({fmt_pct(drawdown_p25)})")

    if dump_rate is not None and dump_rate >= 60:
        risk_score += 0.8
        risk_reasons.append(f"gli spike venivano spesso scaricati ({fmt_pct(dump_rate)})")

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

    if score >= 3.2:
        direction = "BULLISH"
    elif score >= 1.3:
        direction = "LEGGERMENTE BULLISH"
    elif score <= -3.2:
        direction = "BEARISH"
    elif score <= -1.3:
        direction = "LEGGERMENTE BEARISH"
    else:
        direction = "NEUTRALE / INCERTO"

    # Spot.
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

    # Long a leva.
    long_action = "NO LONG A LEVA"
    max_long_leverage = "nessuna"

    if score >= 3.2 and risk_label == "BASSO":
        long_action = "LONG POSSIBILE"
        max_long_leverage = "max 3x isolated"
    elif score >= 2.2 and risk_label in ["BASSO", "MEDIO"]:
        long_action = "LONG PRUDENTE"
        max_long_leverage = "max 2x isolated"
    elif score >= 1.3 and risk_label == "BASSO":
        long_action = "LONG SOLO SU PULLBACK"
        max_long_leverage = "max 2x isolated"

    if risk_label in ["ALTO", "MOLTO ALTO"]:
        long_action = "NO LONG A LEVA"
        max_long_leverage = "nessuna"

    # Short a leva.
    # Nota: NO LONG non significa automaticamente SHORT.
    # Lo short viene favorito solo se il quadro è bearish o se lo spike viene spesso scaricato.
    short_action = "NO SHORT"
    max_short_leverage = "nessuna"

    if score <= -3.2 and risk_label in ["BASSO", "MEDIO"]:
        short_action = "SHORT POSSIBILE"
        max_short_leverage = "max 2x isolated"
    elif score <= -3.2 and risk_label in ["ALTO", "MOLTO ALTO"]:
        short_action = "SHORT SOLO DOPO SPIKE"
        max_short_leverage = "max 1x-2x isolated"
    elif score <= -1.3 and dump_rate is not None and dump_rate >= 55:
        short_action = "SHORT SOLO DOPO SPIKE"
        max_short_leverage = "max 2x isolated"
    elif dump_rate is not None and dump_rate >= 65 and score <= 0:
        short_action = "SHORT SOLO DOPO SPIKE"
        max_short_leverage = "max 1x-2x isolated"

    if score >= 1.3:
        short_action = "NO SHORT"
        max_short_leverage = "nessuna"

    pullback_zone = bounce.get("first_price_now")
    bounce_target = bounce.get("second_price_now")
    spike_zone = dump.get("first_price_now")
    dump_target = dump.get("second_price_now")

    zona_bassa_storica_price = price_from_pct(current_price, drawdown_p25)
    zona_alta_storica_price = price_from_pct(current_price, max_gain_p75)

    plan_parts = []

    if spot_action in ["COMPRA / ACCUMULA", "ACCUMULA SOLO SU PULLBACK"]:
        if pullback_zone is not None:
            plan_parts.append(f"spot: valutare accumulo solo verso {fmt_price(pullback_zone)}")
        else:
            plan_parts.append("spot: accumulo solo su prezzo migliore")
    elif "TAKE PROFIT" in spot_action:
        if spike_zone is not None:
            plan_parts.append(f"spot: prendere profitto su spike verso {fmt_price(spike_zone)}")
        else:
            plan_parts.append("spot: prendere profitto su spike")
    elif "VENDI" in spot_action:
        plan_parts.append("spot: ridurre esposizione o stare fuori")
    else:
        plan_parts.append("spot: aspettare, non forzare entrate")

    if long_action != "NO LONG A LEVA":
        plan_parts.append(f"long: {long_action.lower()}, {max_long_leverage}")
    else:
        plan_parts.append("long: evitato")

    if short_action != "NO SHORT":
        if spike_zone is not None and dump_target is not None:
            plan_parts.append(
                f"short: solo dopo spike verso {fmt_price(spike_zone)}, "
                f"possibile target scarico {fmt_price(dump_target)}"
            )
        else:
            plan_parts.append(f"short: {short_action.lower()}")
    else:
        plan_parts.append("short: evitato")

    if zona_bassa_storica_price is not None:
        plan_parts.append(f"zona bassa storica/rischio: {fmt_price(zona_bassa_storica_price)}")

    if zona_alta_storica_price is not None:
        plan_parts.append(f"zona alta storica/take profit: {fmt_price(zona_alta_storica_price)}")

    if not reasons:
        reasons.append("segnali misti o dati insufficienti")

    if not risk_reasons:
        risk_reasons.append("rischio non eccessivo dai dati disponibili")

    decision = {
        "asset": asset,
        "asset_short": asset_short(asset),
        "current_price": current_price,
        "generated_at_utc": latest_prediction_time(asset),
        "directional_score": score,
        "risk_score": risk_score,
        "direction": direction,
        "risk_label": risk_label,
        "spot_action": spot_action,
        "long_action": long_action,
        "short_action": short_action,
        "max_long_leverage": max_long_leverage,
        "max_short_leverage": max_short_leverage,
        "positive_rate_30d": positive_rate,
        "return_30d_median": median_return,
        "return_30d_avg": avg_return,
        "zona_bassa_storica_pct": drawdown_p25,
        "zona_alta_storica_pct": max_gain_p75,
        "bounce_rate_after_pullback": bounce_rate,
        "dump_rate_after_spike": dump_rate,
        "funding_rate_pct": funding,
        "long_short_ratio": long_short,
        "open_interest_change_pct": oi_change,
        "pullback_zone": pullback_zone,
        "bounce_target": bounce_target,
        "spike_zone": spike_zone,
        "dump_target": dump_target,
        "zona_bassa_storica_price": zona_bassa_storica_price,
        "zona_alta_storica_price": zona_alta_storica_price,
        "main_reasons": "; ".join(reasons[:7]),
        "risk_reasons": "; ".join(risk_reasons[:6]),
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
                d["long_action"],
                d["short_action"],
                d["max_long_leverage"],
                d["max_short_leverage"],
                d["risk_label"],
            ]
        )

    return md_table(
        [
            "Asset",
            "Prezzo",
            "Direzione",
            "Spot",
            "Long leva",
            "Short leva",
            "Max long",
            "Max short",
            "Rischio",
        ],
        rows,
    )


def build_simple_explanation():
    return "\n".join(
        [
            "## Spiegazione semplice",
            "",
            "### Zona alta storica",
            "",
            "Prima si chiamava `target rialzo storico P75`.",
            "",
            "Nome più chiaro: **zona alta storica**.",
            "",
            "Vuol dire:",
            "",
            "> nei casi storici simili, quella era una zona alta raggiunta nei movimenti migliori.",
            "",
            "Non vuol dire che il prezzo ci deve arrivare.",
            "",
            "Uso pratico:",
            "",
            "> se il prezzo arriva lì, non inseguire alla cieca; pensa a prendere profitto o alleggerire.",
            "",
            "### Zona bassa storica",
            "",
            "Prima si chiamava `drawdown P25`.",
            "",
            "Nome più chiaro: **zona bassa storica**.",
            "",
            "Vuol dire:",
            "",
            "> nei casi storici simili, quella era una discesa pesante ma non impossibile.",
            "",
            "Uso pratico:",
            "",
            "> se fai leva, la liquidazione non dovrebbe stare vicino a quella zona.",
            "",
            "### Long e short",
            "",
            "Il report ora separa le due cose:",
            "",
            "- **Long leva**: comprare con leva sperando che salga.",
            "- **Short leva**: vendere con leva sperando che scenda.",
            "",
            "Nota importante:",
            "",
            "> `NO LONG` non significa automaticamente `SHORT`.",
            "",
            "A volte la scelta migliore è semplicemente non fare niente.",
            "",
            "Lo short viene indicato solo se:",
            "",
            "- il quadro è bearish;",
            "- oppure gli spike vengono spesso scaricati;",
            "- e il report prova a indicare la zona dove avrebbe più senso, di solito **dopo uno spike**, non dopo che è già crollato.",
            "",
        ]
    )


def build_simple_verdict(d):
    lines = []

    lines.append(f"## {asset_name(d['asset'])} — {d['asset_short']}")
    lines.append("")
    lines.append(f"Prezzo usato: **{fmt_price(d['current_price'])}**")
    lines.append("")
    lines.append(f"- **Direzione:** {d['direction']}")
    lines.append(f"- **Spot:** {d['spot_action']}")
    lines.append(f"- **Long a leva:** {d['long_action']}")
    lines.append(f"- **Short a leva:** {d['short_action']}")
    lines.append(f"- **Max long:** {d['max_long_leverage']}")
    lines.append(f"- **Max short:** {d['max_short_leverage']}")
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
    lines.append("### Numeri semplici")
    lines.append("")
    lines.append(
        md_table(
            [
                "Dato",
                "Valore",
                "Traduzione",
            ],
            [
                [
                    "Casi positivi 30 giorni",
                    fmt_pct(d["positive_rate_30d"]),
                    "quante volte i casi simili chiudevano verdi dopo 30 giorni",
                ],
                [
                    "Rendimento mediano",
                    fmt_pct(d["return_30d_median"]),
                    "risultato centrale dei casi storici",
                ],
                [
                    "Zona bassa storica",
                    fmt_pct(d["zona_bassa_storica_pct"]),
                    "discesa pesante da rispettare",
                ],
                [
                    "Zona alta storica",
                    fmt_pct(d["zona_alta_storica_pct"]),
                    "zona alta dove non inseguire troppo",
                ],
                [
                    "Rimbalzo dopo -5% → +10%",
                    fmt_pct(d["bounce_rate_after_pullback"]),
                    "se scende prima, quante volte poi rimbalza forte",
                ],
                [
                    "Dump dopo +10% → -5%",
                    fmt_pct(d["dump_rate_after_spike"]),
                    "se fa spike prima, quante volte poi scarica",
                ],
                [
                    "Funding",
                    fmt_pct(d["funding_rate_pct"]),
                    "se è alto positivo, troppi long possono essere un rischio",
                ],
                [
                    "Long/Short ratio",
                    fmt_number(d["long_short_ratio"], 2),
                    "se è alto, ci sono molti long aperti",
                ],
            ],
        )
    )
    lines.append("")
    lines.append("### Aree operative")
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
                    "zona dove valutare accumulo, non comprare a caso",
                ],
                [
                    "Target rimbalzo +10%",
                    fmt_price(d["bounce_target"]),
                    "zona obiettivo dopo pullback",
                ],
                [
                    "Spike +10%",
                    fmt_price(d["spike_zone"]),
                    "zona dove non inseguire; possibile take profit o short solo se il quadro è bearish",
                ],
                [
                    "Dump -5%",
                    fmt_price(d["dump_target"]),
                    "zona di scarico dopo spike",
                ],
                [
                    "Zona bassa storica",
                    fmt_price(d["zona_bassa_storica_price"]),
                    "zona rischio; con leva bisogna rispettarla",
                ],
                [
                    "Zona alta storica",
                    fmt_price(d["zona_alta_storica_price"]),
                    "zona alta; se ci arriva, pensare a profitto",
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
    lines.append("Questo report prende tutti i dati dello scanner e li trasforma in una lettura pratica.")
    lines.append("")
    lines.append("Scopo:")
    lines.append("")
    lines.append("- capire se conviene spot, long, short o aspettare;")
    lines.append("- separare long e short, invece di mettere tutto dentro una sola voce;")
    lines.append("- usare parole semplici per zone alte, zone basse e rischio leva.")
    lines.append("")
    lines.append("## Dashboard veloce")
    lines.append("")
    lines.append(build_dashboard(decisions))
    lines.append("")
    lines.append(build_simple_explanation())
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
                d["long_action"],
                d["short_action"],
                d["max_long_leverage"],
                d["max_short_leverage"],
                d["risk_label"],
            ]
        )

    quick_lines = []

    for d in decisions:
        quick_lines.append(
            f"- **{d['asset_short']}**: spot = **{d['spot_action']}**, "
            f"long = **{d['long_action']}**, short = **{d['short_action']}**, "
            f"rischio = **{d['risk_label']}**."
        )

    return "\n".join(
        [
            "<!-- DECISION_REPORT_START -->",
            "",
            "# Decisione operativa sintetica",
            "",
            "Report separato completo: [decision_report.md](decision_report.md)",
            "",
            "Sintesi automatica dello scanner: spot, long, short e rischio.",
            "",
            md_table(
                [
                    "Asset",
                    "Direzione",
                    "Spot",
                    "Long leva",
                    "Short leva",
                    "Max long",
                    "Max short",
                    "Rischio",
                ],
                rows,
            ),
            "",
            "## Lettura immediata",
            "",
            "\n".join(quick_lines),
            "",
            "## Nota semplice",
            "",
            "- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.",
            "- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.",
            "- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.",
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
