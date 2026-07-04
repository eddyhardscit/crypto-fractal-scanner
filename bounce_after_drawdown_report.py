import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"
PREDICTION_LOG_PATH = "reports/prediction_log.csv"
SEQUENCE_REPORT_PATH = "reports/bounce_after_drawdown_report.md"
SEQUENCE_CSV_PATH = "reports/bounce_after_drawdown_metrics.csv"

TARGETS = ["BTC-USD", "SOL-USD", "DOGE-USD"]

FORWARD_DAYS = 30

BOUNCE_PULLBACKS = [-5, -10, -15]
BOUNCE_REBOUNDS = [10, 20]

DUMP_SPIKES = [10, 20]
DUMP_DUMPS = [0, -5, -10]


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


def first_touch_day(path, start_price, level_pct, direction):
    level_price = start_price * (1 + level_pct / 100)

    if direction == "down":
        positions = np.where(path.values <= level_price)[0]
    else:
        positions = np.where(path.values >= level_price)[0]

    if len(positions) == 0:
        return None

    return int(positions[0])


def summarize_sequence(asset, matches, data, current_price, sequence_type, first_pct, second_pct):
    total_valid = 0
    first_hits = 0
    second_hits_after_first = 0

    first_days = []
    second_days = []

    if sequence_type == "bounce":
        first_direction = "down"
        second_direction = "up"
    else:
        first_direction = "up"
        second_direction = "down"

    for _, row in matches.iterrows():
        start_price, path = get_forward_path(row, data)

        if start_price is None or path is None:
            continue

        total_valid += 1

        first_day = first_touch_day(
            path=path,
            start_price=start_price,
            level_pct=first_pct,
            direction=first_direction,
        )

        if first_day is None:
            continue

        first_hits += 1
        first_days.append(first_day)

        after_first = path.iloc[first_day:]

        second_day_partial = first_touch_day(
            path=after_first,
            start_price=start_price,
            level_pct=second_pct,
            direction=second_direction,
        )

        if second_day_partial is not None:
            second_hits_after_first += 1
            second_days.append(first_day + second_day_partial)

    first_rate = (first_hits / total_valid * 100) if total_valid else np.nan
    second_rate = (
        second_hits_after_first / first_hits * 100
        if first_hits
        else np.nan
    )

    first_price_now = None
    second_price_now = None

    if current_price is not None:
        first_price_now = current_price * (1 + first_pct / 100)
        second_price_now = current_price * (1 + second_pct / 100)

    return {
        "asset": asset,
        "sequence_type": sequence_type,
        "first_pct": first_pct,
        "second_pct": second_pct,
        "current_price": current_price,
        "first_price_now": first_price_now,
        "second_price_now": second_price_now,
        "total_valid": total_valid,
        "first_hits": first_hits,
        "first_rate": first_rate,
        "second_hits_after_first": second_hits_after_first,
        "second_rate_after_first": second_rate,
        "avg_days_to_first": float(np.nanmean(first_days)) if first_days else np.nan,
        "avg_days_to_second": float(np.nanmean(second_days)) if second_days else np.nan,
    }


def strength_label(rate):
    value = safe_float(rate)

    if value is None:
        return "n/d"

    if value >= 65:
        return "ALTA"
    if value >= 50:
        return "MEDIA"
    if value >= 35:
        return "BASSA"

    return "DEBOLE"


def bounce_verdict(summary):
    rate = safe_float(summary.get("second_rate_after_first"))

    if rate is None:
        return "dati insufficienti"

    if rate >= 65:
        return "buona zona storica di rimbalzo"
    if rate >= 50:
        return "rimbalzo possibile"
    if rate >= 35:
        return "rimbalzo debole"
    return "rimbalzo poco frequente"


def dump_verdict(summary):
    rate = safe_float(summary.get("second_rate_after_first"))

    if rate is None:
        return "dati insufficienti"

    if rate >= 65:
        return "spike spesso scaricato"
    if rate >= 50:
        return "attenzione a prendere profitto"
    if rate >= 35:
        return "scarico possibile"
    return "spike storicamente più resistente"


def simple_bounce_sentence(summary):
    asset = asset_short(summary["asset"])
    first_pct = summary["first_pct"]
    second_pct = summary["second_pct"]
    rate = summary["second_rate_after_first"]

    return (
        f"{asset}: se prima scende a {fmt_pct(first_pct)}, "
        f"poi il rimbalzo a {fmt_pct(second_pct)} è avvenuto nel "
        f"{fmt_pct(rate)} dei casi. Lettura: {bounce_verdict(summary)}."
    )


def simple_dump_sentence(summary):
    asset = asset_short(summary["asset"])
    first_pct = summary["first_pct"]
    second_pct = summary["second_pct"]
    rate = summary["second_rate_after_first"]

    if second_pct == 0:
        dump_text = "al prezzo iniziale"
    else:
        dump_text = f"a {fmt_pct(second_pct)}"

    return (
        f"{asset}: se prima sale a {fmt_pct(first_pct)}, "
        f"poi lo scarico {dump_text} è avvenuto nel "
        f"{fmt_pct(rate)} dei casi. Lettura: {dump_verdict(summary)}."
    )


def get_summary(summaries, asset, sequence_type, first_pct, second_pct):
    rows = [
        item for item in summaries
        if item["asset"] == asset
        and item["sequence_type"] == sequence_type
        and item["first_pct"] == first_pct
        and item["second_pct"] == second_pct
    ]

    if rows:
        return rows[0]

    return None


def build_quick_dashboard(summaries):
    rows = []

    for asset in TARGETS:
        bounce = get_summary(
            summaries,
            asset=asset,
            sequence_type="bounce",
            first_pct=-5,
            second_pct=10,
        )

        dump = get_summary(
            summaries,
            asset=asset,
            sequence_type="dump",
            first_pct=10,
            second_pct=-5,
        )

        if bounce is None:
            bounce_zone = "n/d"
            bounce_rate = "n/d"
            bounce_reading = "n/d"
        else:
            bounce_zone = fmt_price(bounce["first_price_now"])
            bounce_rate = fmt_pct(bounce["second_rate_after_first"])
            bounce_reading = bounce_verdict(bounce)

        if dump is None:
            spike_zone = "n/d"
            dump_rate = "n/d"
            dump_reading = "n/d"
        else:
            spike_zone = fmt_price(dump["first_price_now"])
            dump_rate = fmt_pct(dump["second_rate_after_first"])
            dump_reading = dump_verdict(dump)

        rows.append(
            [
                asset_short(asset),
                bounce_zone,
                bounce_rate,
                bounce_reading,
                spike_zone,
                dump_rate,
                dump_reading,
            ]
        )

    return md_table(
        [
            "Asset",
            "Se scende a -5%",
            "Poi +10%",
            "Lettura discesa",
            "Se sale a +10%",
            "Poi dump -5%",
            "Lettura spike",
        ],
        rows,
    )


def build_full_report(summaries):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    parts = []

    parts.append("# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike")
    parts.append("")
    parts.append(f"Generato: **{rome_now}**  ")
    parts.append(f"UTC: **{utc_now}**")
    parts.append("")
    parts.append("Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.")
    parts.append("")
    parts.append("- **Prima scende → poi rimbalza**: utile per capire se comprare/accumulare una discesa.")
    parts.append("- **Prima sale → poi scarica**: utile per capire se prendere profitto dopo uno spike.")
    parts.append("")
    parts.append("## Lettura pratica veloce")
    parts.append("")
    parts.append(build_quick_dashboard(summaries))
    parts.append("")
    parts.append("## Come leggere")
    parts.append("")
    parts.append("- **Se scende a -5%**: prezzo che corrisponde a una discesa del 5% da oggi.")
    parts.append("- **Poi +10%**: tra i casi che prima sono scesi, quanti poi sono saliti almeno del 10% dal prezzo iniziale.")
    parts.append("- **Se sale a +10%**: prezzo che corrisponde a uno spike del 10% da oggi.")
    parts.append("- **Poi dump -5%**: tra i casi che prima sono saliti, quanti poi sono tornati a -5% dal prezzo iniziale.")
    parts.append("- **Non è una certezza**: è una statistica storica sui casi più simili.")
    parts.append("")
    parts.append("---")
    parts.append("")

    for asset in TARGETS:
        parts.append(f"# {asset_name(asset)} — {asset_short(asset)}")
        parts.append("")
        parts.append("## Lettura semplice")
        parts.append("")

        base_bounce = get_summary(summaries, asset, "bounce", -5, 10)
        base_dump = get_summary(summaries, asset, "dump", 10, -5)

        if base_bounce is not None:
            parts.append(f"- {simple_bounce_sentence(base_bounce)}")

        if base_dump is not None:
            parts.append(f"- {simple_dump_sentence(base_dump)}")

        parts.append("")
        parts.append("## Tabella rimbalzo dopo discesa")
        parts.append("")

        bounce_rows = []

        for first_pct in BOUNCE_PULLBACKS:
            for second_pct in BOUNCE_REBOUNDS:
                item = get_summary(summaries, asset, "bounce", first_pct, second_pct)

                if item is None:
                    continue

                bounce_rows.append(
                    [
                        fmt_pct(first_pct),
                        fmt_price(item["first_price_now"]),
                        f"{item['first_hits']}/{item['total_valid']}",
                        fmt_pct(item["first_rate"]),
                        fmt_pct(second_pct),
                        fmt_price(item["second_price_now"]),
                        f"{item['second_hits_after_first']}/{item['first_hits']}",
                        fmt_pct(item["second_rate_after_first"]),
                        strength_label(item["second_rate_after_first"]),
                        fmt_days(item["avg_days_to_first"]),
                        fmt_days(item["avg_days_to_second"]),
                    ]
                )

        parts.append(
            md_table(
                [
                    "Prima scende",
                    "Prezzo",
                    "Casi scesi",
                    "% casi scesi",
                    "Poi rimbalzo",
                    "Prezzo target",
                    "Casi riusciti",
                    "% riusciti",
                    "Forza",
                    "Giorni discesa",
                    "Giorni target",
                ],
                bounce_rows,
            )
        )

        parts.append("")
        parts.append("## Tabella dump dopo spike")
        parts.append("")

        dump_rows = []

        for first_pct in DUMP_SPIKES:
            for second_pct in DUMP_DUMPS:
                item = get_summary(summaries, asset, "dump", first_pct, second_pct)

                if item is None:
                    continue

                dump_rows.append(
                    [
                        fmt_pct(first_pct),
                        fmt_price(item["first_price_now"]),
                        f"{item['first_hits']}/{item['total_valid']}",
                        fmt_pct(item["first_rate"]),
                        "prezzo iniziale" if second_pct == 0 else fmt_pct(second_pct),
                        fmt_price(item["second_price_now"]),
                        f"{item['second_hits_after_first']}/{item['first_hits']}",
                        fmt_pct(item["second_rate_after_first"]),
                        strength_label(item["second_rate_after_first"]),
                        fmt_days(item["avg_days_to_first"]),
                        fmt_days(item["avg_days_to_second"]),
                    ]
                )

        parts.append(
            md_table(
                [
                    "Prima sale",
                    "Prezzo",
                    "Casi spike",
                    "% casi spike",
                    "Poi scarica",
                    "Prezzo target",
                    "Casi scarico",
                    "% scarico",
                    "Forza",
                    "Giorni spike",
                    "Giorni dump",
                ],
                dump_rows,
            )
        )

        parts.append("")
        parts.append("---")
        parts.append("")

    return "\n".join(parts)


def build_main_report_block(summaries):
    rows = []
    fast_lines = []

    for asset in TARGETS:
        bounce = get_summary(summaries, asset, "bounce", -5, 10)
        dump = get_summary(summaries, asset, "dump", 10, -5)

        if bounce is None:
            bounce_zone = "n/d"
            bounce_rate = "n/d"
            bounce_reading = "n/d"
        else:
            bounce_zone = fmt_price(bounce["first_price_now"])
            bounce_rate = fmt_pct(bounce["second_rate_after_first"])
            bounce_reading = bounce_verdict(bounce)
            fast_lines.append(f"- **{simple_bounce_sentence(bounce)}**")

        if dump is None:
            spike_zone = "n/d"
            dump_rate = "n/d"
            dump_reading = "n/d"
        else:
            spike_zone = fmt_price(dump["first_price_now"])
            dump_rate = fmt_pct(dump["second_rate_after_first"])
            dump_reading = dump_verdict(dump)
            fast_lines.append(f"- **{simple_dump_sentence(dump)}**")

        rows.append(
            [
                asset_short(asset),
                bounce_zone,
                bounce_rate,
                bounce_reading,
                spike_zone,
                dump_rate,
                dump_reading,
            ]
        )

    return "\n".join(
        [
            "<!-- BOUNCE_AFTER_DRAWDOWN_START -->",
            "",
            "---",
            "",
            "# Sequenze pratiche: rimbalzo / dump",
            "",
            "Report separato completo: [bounce_after_drawdown_report.md](bounce_after_drawdown_report.md)",
            "",
            "Questa sezione serve a rispondere subito a due domande:",
            "",
            "- **Se scende, è una zona di rimbalzo?**",
            "- **Se sale forte, è una zona da prendere profitto?**",
            "",
            md_table(
                [
                    "Asset",
                    "Se scende a -5%",
                    "Poi +10%",
                    "Lettura discesa",
                    "Se sale a +10%",
                    "Poi dump -5%",
                    "Lettura spike",
                ],
                rows,
            ),
            "",
            "## Traduzione veloce",
            "",
            "\n".join(fast_lines),
            "",
            "<!-- BOUNCE_AFTER_DRAWDOWN_END -->",
        ]
    )


def inject_into_main_report(summaries):
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

    block = build_main_report_block(summaries).strip()

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
        marker = "\n# Come leggere questo report"
        insert_pos = current.find(marker)

        if insert_pos != -1:
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


def write_csv(summaries):
    df = pd.DataFrame(summaries)
    df.to_csv(SEQUENCE_CSV_PATH, index=False)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    all_matches = build_all_matches()

    if all_matches.empty:
        report = "# Sequenze pratiche\n\nNessun match disponibile.\n"

        with open(SEQUENCE_REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)

        print("No matches available for sequence report.")
        return

    market_data = download_needed_data(all_matches)

    summaries = []

    for asset in TARGETS:
        path = matches_path(asset)
        matches = read_csv_safe(path)

        if matches.empty:
            continue

        current_price = latest_current_price(asset)

        for first_pct in BOUNCE_PULLBACKS:
            for second_pct in BOUNCE_REBOUNDS:
                summaries.append(
                    summarize_sequence(
                        asset=asset,
                        matches=matches,
                        data=market_data,
                        current_price=current_price,
                        sequence_type="bounce",
                        first_pct=first_pct,
                        second_pct=second_pct,
                    )
                )

        for first_pct in DUMP_SPIKES:
            for second_pct in DUMP_DUMPS:
                summaries.append(
                    summarize_sequence(
                        asset=asset,
                        matches=matches,
                        data=market_data,
                        current_price=current_price,
                        sequence_type="dump",
                        first_pct=first_pct,
                        second_pct=second_pct,
                    )
                )

    report = build_full_report(summaries)

    with open(SEQUENCE_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    write_csv(summaries)
    inject_into_main_report(summaries)

    print(f"Wrote {SEQUENCE_REPORT_PATH}")
    print(f"Wrote {SEQUENCE_CSV_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
