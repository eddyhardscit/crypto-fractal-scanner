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

TARGETS = ["BTC-USD", "SOL-USD", "DOGE-USD"]

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

PREDICTION_LOG_PATH = "reports/prediction_log.csv"
ACCURACY_REPORT_PATH = "reports/accuracy_report.csv"


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
                    print(
                        f"{ticker}: OK "
                        f"{processed.index[0].date()} -> {processed.index[-1].date()}"
                    )

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

        too_close = any(
            abs((end_date - prev_date).days) < MIN_GAP_DAYS
            for prev_date in previous_dates
        )

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


def fmt_number_it(value):
    try:
        s = f"{float(value):,.2f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return str(value)


def fmt_price(value):
    return f"{fmt_number_it(value)} $"


def fmt_pct(value):
    return f"{fmt_number_it(value)}%"


def semaforo(verdict_value):
    if verdict_value == "RIALZISTA":
        return "🟢 VERDE / Favorevole"
    if verdict_value == "RIBASSISTA":
        return "🔴 ROSSO / Prudenza"
    return "🟡 GIALLO / Incerto"


def asset_name(target):
    if target == "BTC-USD":
        return "Bitcoin"
    if target == "SOL-USD":
        return "Solana"
    if target == "DOGE-USD":
        return "Dogecoin"
    return target


def simple_verdict_text(target, verdict_value):
    name = asset_name(target)

    if verdict_value == "RIALZISTA":
        return (
            f"{name} ha un segnale abbastanza favorevole. "
            "Nei casi storici più simili, il prezzo è salito più spesso che sceso. "
            "Questo non vuol dire certezza, ma il contesto è più positivo."
        )

    if verdict_value == "RIBASSISTA":
        return (
            f"{name} richiede prudenza. "
            "Nei casi storici più simili, il prezzo non ha avuto una partenza pulita. "
            "Spesso ha fatto prima una discesa importante. "
            "Con leva, questa è la parte più pericolosa."
        )

    return (
        f"{name} è in una situazione incerta. "
        "Lo scanner non vede un vantaggio chiaro né per il rialzo né per il ribasso. "
        "In questi casi è meglio non forzare la previsione."
    )


def get_percentile_price(percentiles, metric, q):
    row = percentiles[
        (percentiles["metric"] == metric) &
        (percentiles["percentile"] == q)
    ]

    if len(row) == 0:
        return None, None

    percent_value = float(row["percent_value"].iloc[0])
    price_level = float(row["price_level"].iloc[0])

    return percent_value, price_level


def percentile_lines(percentiles, metric):
    labels = {
        10: "scenario brutto",
        25: "scenario negativo",
        50: "scenario centrale",
        75: "scenario buono",
        90: "scenario molto buono",
    }

    lines = []

    for q in [10, 25, 50, 75, 90]:
        percent_value, price_level = get_percentile_price(percentiles, metric, q)

        if percent_value is None:
            continue

        lines.append(
            f"- **{labels[q]}**: {fmt_pct(percent_value)} → **{fmt_price(price_level)}**"
        )

    return lines


def load_prediction_log():
    if os.path.exists(PREDICTION_LOG_PATH):
        return pd.read_csv(PREDICTION_LOG_PATH)

    return pd.DataFrame()


def percentile_value(percentiles, metric, q, column):
    row = percentiles[
        (percentiles["metric"] == metric) &
        (percentiles["percentile"] == q)
    ]

    if len(row) == 0:
        return np.nan

    return float(row[column].iloc[0])


def update_prediction_log(log, all_results, generated_at):
    prediction_date = generated_at[:10]

    for target, result in all_results.items():
        summary = result["summary"]
        prices = result["prices"]
        percentiles = result["percentiles"]

        row = {
            "prediction_date": prediction_date,
            "generated_at_utc": generated_at,
            "asset": target,
            "verdict": result["verdict"],
            "current_price": prices["current_price"],
            "scenario_avg_30d": prices["scenario_avg_30d"],
            "scenario_median_30d": prices["scenario_median_30d"],
            "drawdown_avg_30d": prices["drawdown_avg_30d"],
            "max_gain_avg_30d": prices["max_gain_avg_30d"],
            "similarity_avg": summary["similarity_avg"],
            "positive_cases_30d": summary["positive_cases_30d"],
            "return_30d_avg": summary["return_30d_avg"],
            "return_30d_median": summary["return_30d_median"],
            "drawdown_30d_avg": summary["drawdown_30d_avg"],
            "max_gain_30d_avg": summary["max_gain_30d_avg"],
            "evaluated": False,
            "evaluation_date": "",
            "actual_30d_price": np.nan,
            "actual_30d_return_pct": np.nan,
            "actual_min_price_30d": np.nan,
            "actual_drawdown_pct": np.nan,
            "actual_max_price_30d": np.nan,
            "actual_max_gain_pct": np.nan,
            "directional_correct": np.nan,
            "central_error_pct": np.nan,
            "risk_zone_touched": np.nan,
            "upside_zone_touched": np.nan,
            "return_within_p10_p90": np.nan,
            "drawdown_within_p10_p90": np.nan,
            "max_gain_within_p10_p90": np.nan,
        }

        for metric, prefix in [
            ("return_30d", "return"),
            ("drawdown_30d", "drawdown"),
            ("max_gain_30d", "max_gain"),
        ]:
            for q in [10, 25, 50, 75, 90]:
                row[f"{prefix}_p{q}_pct"] = percentile_value(
                    percentiles, metric, q, "percent_value"
                )
                row[f"{prefix}_p{q}_price"] = percentile_value(
                    percentiles, metric, q, "price_level"
                )

        if not log.empty and {"prediction_date", "asset"}.issubset(log.columns):
            duplicate_mask = (
                (log["prediction_date"].astype(str) == prediction_date) &
                (log["asset"].astype(str) == target)
            )
            log = log[~duplicate_mask].copy()

        log = pd.concat([log, pd.DataFrame([row])], ignore_index=True)

    return log


def to_float(value):
    try:
        return float(value)
    except Exception:
        return np.nan


def bool_is_true(value):
    return str(value).lower() in ["true", "1", "yes"]


def evaluate_prediction_log(log, data):
    if log.empty:
        return log

    if "evaluated" not in log.columns:
        log["evaluated"] = False

    for idx, row in log.iterrows():
        if bool_is_true(row.get("evaluated", False)):
            continue

        asset = row.get("asset")

        if asset not in data:
            continue

        prediction_date = pd.to_datetime(row.get("prediction_date"), errors="coerce")

        if pd.isna(prediction_date):
            continue

        due_date = prediction_date + pd.Timedelta(days=30)

        df = data[asset].copy()
        df_index = pd.DatetimeIndex(df.index)

        if df_index.tz is not None:
            df_index = df_index.tz_convert(None)

        df_index = df_index.normalize()

        future_positions = np.where(df_index >= due_date.normalize())[0]

        if len(future_positions) == 0:
            continue

        actual_pos = future_positions[0]
        actual_date = df_index[actual_pos]

        path_mask = (
            (df_index >= prediction_date.normalize()) &
            (df_index <= actual_date)
        )

        path = df.loc[path_mask]

        if len(path) == 0:
            continue

        prediction_price = to_float(row.get("current_price"))

        if np.isnan(prediction_price) or prediction_price <= 0:
            continue

        actual_price = float(df["Close"].iloc[actual_pos])
        actual_return = (actual_price / prediction_price - 1) * 100

        actual_min = float(path["Close"].min())
        actual_drawdown = (actual_min / prediction_price - 1) * 100

        actual_max = float(path["Close"].max())
        actual_max_gain = (actual_max / prediction_price - 1) * 100

        scenario_median_price = to_float(row.get("scenario_median_30d"))
        drawdown_avg_price = to_float(row.get("drawdown_avg_30d"))
        max_gain_avg_price = to_float(row.get("max_gain_avg_30d"))

        verdict_value = str(row.get("verdict", ""))

        if verdict_value == "RIALZISTA":
            directional_correct = actual_return > 0
        elif verdict_value == "RIBASSISTA":
            directional_correct = actual_return < 0
        else:
            directional_correct = np.nan

        if not np.isnan(scenario_median_price):
            central_error_pct = abs(actual_price - scenario_median_price) / prediction_price * 100
        else:
            central_error_pct = np.nan

        risk_zone_touched = (
            actual_min <= drawdown_avg_price
            if not np.isnan(drawdown_avg_price)
            else np.nan
        )

        upside_zone_touched = (
            actual_max >= max_gain_avg_price
            if not np.isnan(max_gain_avg_price)
            else np.nan
        )

        return_p10 = to_float(row.get("return_p10_pct"))
        return_p90 = to_float(row.get("return_p90_pct"))
        drawdown_p10 = to_float(row.get("drawdown_p10_pct"))
        drawdown_p90 = to_float(row.get("drawdown_p90_pct"))
        max_gain_p10 = to_float(row.get("max_gain_p10_pct"))
        max_gain_p90 = to_float(row.get("max_gain_p90_pct"))

        return_within = (
            return_p10 <= actual_return <= return_p90
            if not np.isnan(return_p10) and not np.isnan(return_p90)
            else np.nan
        )

        drawdown_within = (
            drawdown_p10 <= actual_drawdown <= drawdown_p90
            if not np.isnan(drawdown_p10) and not np.isnan(drawdown_p90)
            else np.nan
        )

        max_gain_within = (
            max_gain_p10 <= actual_max_gain <= max_gain_p90
            if not np.isnan(max_gain_p10) and not np.isnan(max_gain_p90)
            else np.nan
        )

        log.at[idx, "evaluated"] = True
        log.at[idx, "evaluation_date"] = actual_date.date().isoformat()
        log.at[idx, "actual_30d_price"] = actual_price
        log.at[idx, "actual_30d_return_pct"] = actual_return
        log.at[idx, "actual_min_price_30d"] = actual_min
        log.at[idx, "actual_drawdown_pct"] = actual_drawdown
        log.at[idx, "actual_max_price_30d"] = actual_max
        log.at[idx, "actual_max_gain_pct"] = actual_max_gain
        log.at[idx, "directional_correct"] = directional_correct
        log.at[idx, "central_error_pct"] = central_error_pct
        log.at[idx, "risk_zone_touched"] = risk_zone_touched
        log.at[idx, "upside_zone_touched"] = upside_zone_touched
        log.at[idx, "return_within_p10_p90"] = return_within
        log.at[idx, "drawdown_within_p10_p90"] = drawdown_within
        log.at[idx, "max_gain_within_p10_p90"] = max_gain_within

    return log


def boolean_rate(series):
    if series is None or len(series) == 0:
        return np.nan

    valid = series.dropna()

    if len(valid) == 0:
        return np.nan

    valid = valid[
        valid.astype(str).str.lower().isin(["true", "false", "1", "0"])
    ]

    if len(valid) == 0:
        return np.nan

    return valid.astype(str).str.lower().isin(["true", "1"]).mean() * 100


def accuracy_summary(log):
    if log.empty or "evaluated" not in log.columns:
        return pd.DataFrame()

    evaluated_mask = log["evaluated"].astype(str).str.lower().isin(["true", "1"])
    evaluated = log[evaluated_mask].copy()

    if evaluated.empty:
        return pd.DataFrame()

    rows = []

    for asset in sorted(evaluated["asset"].unique()):
        asset_rows = evaluated[evaluated["asset"] == asset].copy()

        central_error = pd.to_numeric(
            asset_rows.get("central_error_pct"),
            errors="coerce"
        ).mean()

        rows.append({
            "asset": asset,
            "evaluated_predictions": len(asset_rows),
            "directional_accuracy_pct": boolean_rate(asset_rows.get("directional_correct")),
            "avg_central_error_pct": central_error,
            "risk_zone_touched_pct": boolean_rate(asset_rows.get("risk_zone_touched")),
            "upside_zone_touched_pct": boolean_rate(asset_rows.get("upside_zone_touched")),
            "return_inside_p10_p90_pct": boolean_rate(asset_rows.get("return_within_p10_p90")),
            "drawdown_inside_p10_p90_pct": boolean_rate(asset_rows.get("drawdown_within_p10_p90")),
            "max_gain_inside_p10_p90_pct": boolean_rate(asset_rows.get("max_gain_within_p10_p90")),
        })

    return pd.DataFrame(rows)


def append_accuracy_section(lines, prediction_log):
    lines.append("## Controllo accuratezza dello scanner")
    lines.append("")
    lines.append(
        "Questa sezione serve a controllare se lo scanner sta funzionando davvero. "
        "Ogni giorno viene salvata una previsione. Dopo 30 giorni, lo scanner confronta "
        "quella previsione con quello che è successo realmente."
    )
    lines.append("")

    summary = accuracy_summary(prediction_log)

    if summary.empty:
        lines.append(
            "Per ora non ci sono ancora previsioni vecchie di 30 giorni da controllare."
        )
        lines.append(
            "Il controllo vero inizierà automaticamente dopo il primo mese di utilizzo."
        )
        lines.append("")
        return

    lines.append("### Riassunto accuratezza")
    lines.append("")

    for _, row in summary.iterrows():
        name = asset_name(row["asset"])

        lines.append(f"#### {name}")
        lines.append("")
        lines.append(
            f"- Previsioni già controllate: **{int(row['evaluated_predictions'])}**"
        )

        if not np.isnan(row["directional_accuracy_pct"]):
            lines.append(
                f"- Direzione corretta: **{fmt_pct(row['directional_accuracy_pct'])}**"
            )
        else:
            lines.append(
                "- Direzione corretta: non ancora calcolabile, perché molti segnali erano neutrali."
            )

        if not np.isnan(row["avg_central_error_pct"]):
            lines.append(
                f"- Errore medio dello scenario centrale: **{fmt_pct(row['avg_central_error_pct'])}**"
            )

        if not np.isnan(row["risk_zone_touched_pct"]):
            lines.append(
                f"- Zona rischio toccata: **{fmt_pct(row['risk_zone_touched_pct'])}**"
            )

        if not np.isnan(row["upside_zone_touched_pct"]):
            lines.append(
                f"- Zona rialzo media toccata: **{fmt_pct(row['upside_zone_touched_pct'])}**"
            )

        if not np.isnan(row["return_inside_p10_p90_pct"]):
            lines.append(
                f"- Prezzo finale dentro lo scenario 10%-90%: **{fmt_pct(row['return_inside_p10_p90_pct'])}**"
            )

        lines.append("")

    lines.append(
        "Spiegazione semplice: se col tempo la direzione corretta è bassa o l'errore medio è alto, "
        "lo scanner va preso con più cautela. Se invece molte previsioni finiscono dentro i livelli "
        "previsti, allora lo scanner sta diventando più affidabile."
    )
    lines.append("")


def build_markdown_report(all_results, generated_at, prediction_log):
    lines = []

    lines.append("# Report giornaliero BTC / SOL / DOGE")
    lines.append("")
    lines.append(f"Aggiornato il: **{generated_at} UTC**")
    lines.append("")
    lines.append(
        "Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin "
        "con tanti grafici storici di altre crypto."
    )
    lines.append("")
    lines.append(
        "Non è una previsione certa. È uno scanner statistico: "
        "guarda situazioni simili già successe e mostra cosa accadde dopo."
    )
    lines.append("")

    lines.append("## Riassunto veloce")
    lines.append("")

    for target, result in all_results.items():
        name = asset_name(target)
        verdict_value = result["verdict"]
        prices = result["prices"]

        lines.append(f"### {name}: {semaforo(verdict_value)}")
        lines.append(f"- Prezzo attuale: **{fmt_price(prices['current_price'])}**")
        lines.append(f"- Scenario centrale: **{fmt_price(prices['scenario_median_30d'])}**")
        lines.append(f"- Zona rischio media: **{fmt_price(prices['drawdown_avg_30d'])}**")
        lines.append(f"- Zona rialzo media: **{fmt_price(prices['max_gain_avg_30d'])}**")
        lines.append("")

    verdicts = [result["verdict"] for result in all_results.values()]

    lines.append("### Messaggio del giorno")
    lines.append("")

    if "RIBASSISTA" in verdicts:
        lines.append(
            "Lo scanner oggi invita alla prudenza. "
            "Uno o più asset possono anche salire, ma nei casi storici simili "
            "il prezzo spesso ha fatto prima una discesa importante."
        )
    elif all(v == "RIALZISTA" for v in verdicts):
        lines.append(
            "Lo scanner oggi è più favorevole. "
            "Nei casi storici simili, gli asset analizzati sono saliti più spesso che scesi."
        )
    else:
        lines.append(
            "Lo scanner oggi è misto o incerto. "
            "Non c'è un segnale abbastanza pulito per forzare la previsione."
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    append_accuracy_section(lines, prediction_log)

    lines.append("---")
    lines.append("")

    lines.append("## Come leggere il report")
    lines.append("")
    lines.append("- **🟢 Verde** = situazione più favorevole.")
    lines.append("- **🟡 Giallo** = situazione incerta, meglio non forzare.")
    lines.append("- **🔴 Rosso** = prudenza, rischio più alto.")
    lines.append("")

    lines.append("## Percentili spiegati semplice")
    lines.append("")
    lines.append("- **10%** = scenario brutto.")
    lines.append("- **25%** = scenario negativo.")
    lines.append("- **50%** = scenario centrale, cioè la via di mezzo.")
    lines.append("- **75%** = scenario buono.")
    lines.append("- **90%** = scenario molto buono.")
    lines.append("")
    lines.append(
        "Quando leggi per esempio **+12% → 70.000 $**, significa che in quello scenario "
        "il prezzo sarebbe circa il 12% sopra il prezzo attuale."
    )
    lines.append("")
    lines.append(
        "Quando leggi per esempio **-15% → 52.000 $**, significa che in quello scenario "
        "il prezzo sarebbe circa il 15% sotto il prezzo attuale."
    )
    lines.append("")
    lines.append(
        "La parte più importante per chi usa leva è il **drawdown**: "
        "significa la discesa che il prezzo può fare durante il percorso, "
        "anche se poi recupera."
    )
    lines.append("")

    lines.append("## Spiegazione tecnica dei percentili")
    lines.append("")
    lines.append(
        "I percentili servono a dividere i risultati storici in scenari. "
        "Lo scanner trova 40 casi storici simili, guarda cosa è successo dopo "
        "quei 40 casi e poi li ordina dal peggiore al migliore."
    )
    lines.append("")
    lines.append(
        "- Il **percentile 10** indica un risultato molto debole: "
        "solo il 10% dei casi è andato peggio o uguale a quel livello."
    )
    lines.append(
        "- Il **percentile 25** indica uno scenario negativo: "
        "il 25% dei casi è andato peggio o uguale a quel livello."
    )
    lines.append(
        "- Il **percentile 50** è la mediana: "
        "metà dei casi è andata peggio e metà meglio."
    )
    lines.append(
        "- Il **percentile 75** indica uno scenario buono: "
        "il 75% dei casi è stato sotto quel livello e il 25% sopra."
    )
    lines.append(
        "- Il **percentile 90** indica uno scenario molto forte: "
        "solo il 10% dei casi è andato meglio di quel livello."
    )
    lines.append("")
    lines.append(
        "Quindi il percentile non è una previsione sicura. "
        "È un modo per dire: nei casi storici simili, questo livello era "
        "uno scenario brutto, normale, buono o molto buono."
    )
    lines.append("")
    lines.append(
        "- Per **return_30d**, il percentile indica dove era il prezzo dopo 30 giorni."
    )
    lines.append(
        "- Per **drawdown_30d**, indica quanto il prezzo è sceso durante quei 30 giorni, "
        "anche se poi ha recuperato."
    )
    lines.append(
        "- Per **max_gain_30d**, indica il massimo rialzo toccato durante quei 30 giorni, "
        "anche solo temporaneamente."
    )
    lines.append("")

    for target, result in all_results.items():
        name = asset_name(target)
        verdict_value = result["verdict"]
        summary = result["summary"]
        prices = result["prices"]
        percentiles = result["percentiles"]

        lines.append("---")
        lines.append("")
        lines.append(f"# {name} ({target})")
        lines.append("")
        lines.append(f"## Semaforo: {semaforo(verdict_value)}")
        lines.append("")
        lines.append(f"**Prezzo attuale:** {fmt_price(prices['current_price'])}")
        lines.append("")

        lines.append("## Spiegazione semplice")
        lines.append("")
        lines.append(simple_verdict_text(target, verdict_value))
        lines.append("")

        lines.append("## Cosa dicono i 40 casi storici più simili")
        lines.append("")
        lines.append(f"- Somiglianza media dei pattern: **{fmt_pct(summary['similarity_avg'])}**")
        lines.append(f"- Casi positivi dopo 30 giorni: **{fmt_number_it(summary['positive_cases_30d'])}%**")
        lines.append(f"- Rendimento medio dopo 30 giorni: **{fmt_pct(summary['return_30d_avg'])}**")
        lines.append(f"- Rendimento centrale dopo 30 giorni: **{fmt_pct(summary['return_30d_median'])}**")
        lines.append(f"- Discesa media durante i 30 giorni: **{fmt_pct(summary['drawdown_30d_avg'])}**")
        lines.append(f"- Massimo rialzo medio durante i 30 giorni: **{fmt_pct(summary['max_gain_30d_avg'])}**")
        lines.append("")

        lines.append("## Livelli principali")
        lines.append("")
        lines.append(f"- Scenario medio a 30 giorni: **{fmt_price(prices['scenario_avg_30d'])}**")
        lines.append(f"- Scenario centrale a 30 giorni: **{fmt_price(prices['scenario_median_30d'])}**")
        lines.append(f"- Zona di rischio media: **{fmt_price(prices['drawdown_avg_30d'])}**")
        lines.append(f"- Zona di rialzo media: **{fmt_price(prices['max_gain_avg_30d'])}**")
        lines.append("")

        lines.append("## Percentili — dove potrebbe essere il prezzo tra 30 giorni")
        lines.append("")
        lines.extend(percentile_lines(percentiles, "return_30d"))
        lines.append("")
        lines.append(
            "Spiegazione: questi livelli indicano dove il prezzo si trovava "
            "dopo 30 giorni nei casi storici simili."
        )
        lines.append("")

        lines.append("## Percentili drawdown — quanto potrebbe scendere durante il percorso")
        lines.append("")
        lines.extend(percentile_lines(percentiles, "drawdown_30d"))
        lines.append("")
        lines.append(
            "Spiegazione: questa è la parte più importante se usi leva. "
            "Il prezzo può scendere a questi livelli anche se poi recupera."
        )
        lines.append("")

        lines.append("## Percentili max gain — quanto potrebbe salire durante il percorso")
        lines.append("")
        lines.extend(percentile_lines(percentiles, "max_gain_30d"))
        lines.append("")
        lines.append(
            "Spiegazione: questi livelli indicano il massimo rialzo toccato "
            "nei casi simili, anche solo temporaneamente."
        )
        lines.append("")

        if target == "BTC-USD":
            lines.append("## Nota personale sulla leva")
            lines.append("")
            lines.append(
                "Se hai una posizione long con liquidazione vicino a 51.000 $, "
                "controlla soprattutto la zona di rischio e i percentili drawdown."
            )
            lines.append(
                "Se lo scanner mostra una zona di rischio vicina alla liquidazione, "
                "non significa che Bitcoin ci arriverà sicuramente, ma significa che "
                "il rischio non è remoto."
            )
            lines.append("")

        lines.append("## Dati tecnici per controllo")
        lines.append("")
        lines.append(
            "Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. "
            "Non è obbligatorio leggerla ogni giorno."
        )
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

        if target not in data:
            raise RuntimeError(f"Target {target} not found in downloaded data.")

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
        all_results[target]["percentiles"].to_csv(
            f"reports/{safe_target}_percentiles.csv",
            index=False
        )

    prediction_log = load_prediction_log()
    prediction_log = update_prediction_log(prediction_log, all_results, generated_at)
    prediction_log = evaluate_prediction_log(prediction_log, data)
    prediction_log.to_csv(PREDICTION_LOG_PATH, index=False)

    accuracy = accuracy_summary(prediction_log)
    accuracy.to_csv(ACCURACY_REPORT_PATH, index=False)

    report_md = build_markdown_report(all_results, generated_at, prediction_log)

    with open("reports/latest_report.md", "w", encoding="utf-8") as f:
        f.write(report_md)

    print(report_md)
    print("Report saved in reports/latest_report.md")
    print("Prediction log saved in reports/prediction_log.csv")
    print("Accuracy report saved in reports/accuracy_report.csv")


if __name__ == "__main__":
    main()
