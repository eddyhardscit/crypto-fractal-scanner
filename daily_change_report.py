import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd


REPORT_DIR = "reports"

PREDICTION_LOG_PATH = "reports/prediction_log.csv"
DAILY_CHANGE_MD_PATH = "reports/daily_change_report.md"
MAIN_REPORT_PATH = "reports/latest_report.md"

TARGETS = ["BTC-USD", "SOL-USD", "DOGE-USD"]


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


def fmt_price(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    if abs(value) >= 1000:
        return f"${value:,.0f}"

    if abs(value) >= 1:
        return f"${value:,.2f}"

    return f"${value:.5f}"


def fmt_pct(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    sign = "+" if value > 0 else ""
    return f"{sign}{value:.{decimals}f}%"


def fmt_delta(value, suffix=""):
    value = safe_float(value)

    if value is None:
        return "n/d"

    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}{suffix}"


def fmt_date(value):
    try:
        return pd.to_datetime(value).date().isoformat()
    except Exception:
        return "n/d"


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")

    return "\n".join(lines)


def get_latest_two_by_asset(log, asset):
    if log.empty or "asset" not in log.columns:
        return None, None

    rows = log[log["asset"].astype(str) == asset].copy()

    if rows.empty:
        return None, None

    if "prediction_date" not in rows.columns:
        return None, None

    rows["prediction_date_dt"] = pd.to_datetime(
        rows["prediction_date"],
        errors="coerce",
    )

    rows = rows.dropna(subset=["prediction_date_dt"]).copy()

    if rows.empty:
        return None, None

    if "generated_at_utc" in rows.columns:
        rows["generated_at_dt"] = pd.to_datetime(
            rows["generated_at_utc"],
            errors="coerce",
        )
    else:
        rows["generated_at_dt"] = rows["prediction_date_dt"]

    rows = rows.sort_values(["prediction_date_dt", "generated_at_dt"])

    # Se fai più run manuali nello stesso giorno,
    # tiene solo l'ultima previsione di quel giorno.
    daily = rows.groupby("prediction_date_dt", as_index=False).tail(1)
    daily = daily.sort_values("prediction_date_dt")

    if len(daily) == 1:
        return daily.iloc[-1], None

    return daily.iloc[-1], daily.iloc[-2]


def diff_pct_points(today, yesterday, col):
    if today is None or yesterday is None:
        return None

    a = safe_float(today.get(col))
    b = safe_float(yesterday.get(col))

    if a is None or b is None:
        return None

    return a - b


def diff_price_pct(today, yesterday, col):
    if today is None or yesterday is None:
        return None

    a = safe_float(today.get(col))
    b = safe_float(yesterday.get(col))

    if a is None or b is None or b == 0:
        return None

    return ((a - b) / b) * 100


def classify_change(today, yesterday):
    if today is None:
        return {
            "level": "NESSUN DATO",
            "score": 0,
            "tone": "misto",
            "reasons": ["Non ci sono ancora dati nel prediction_log.csv."],
        }

    if yesterday is None:
        return {
            "level": "PRIMA PREVISIONE",
            "score": 0,
            "tone": "nuovo",
            "reasons": [
                "C'è solo una previsione salvata per questo asset. "
                "Da domani potrà confrontare oggi vs ieri."
            ],
        }

    score = 0
    improvement = 0
    worsening = 0
    reasons = []

    verdict_today = str(today.get("verdict", "n/d"))
    verdict_yesterday = str(yesterday.get("verdict", "n/d"))

    if verdict_today != verdict_yesterday:
        score += 3
        reasons.append(f"Verdetto cambiato: {verdict_yesterday} → {verdict_today}")

        if "RIALZISTA" in verdict_today and "RIALZISTA" not in verdict_yesterday:
            improvement += 2

        if "RIBASSISTA" in verdict_today and "RIBASSISTA" not in verdict_yesterday:
            worsening += 2

        if "NEUTRALE" in verdict_today and "RIBASSISTA" in verdict_yesterday:
            improvement += 1

        if "NEUTRALE" in verdict_today and "RIALZISTA" in verdict_yesterday:
            worsening += 1

    positive_delta = diff_pct_points(today, yesterday, "positive_cases_30d")

    if positive_delta is not None:
        if abs(positive_delta) >= 10:
            score += 3
            reasons.append(
                f"Casi positivi cambiati molto: {fmt_delta(positive_delta, ' punti')}"
            )
        elif abs(positive_delta) >= 5:
            score += 1
            reasons.append(
                f"Casi positivi cambiati: {fmt_delta(positive_delta, ' punti')}"
            )

        if positive_delta > 0:
            improvement += 1
        elif positive_delta < 0:
            worsening += 1

    return_p50_delta = diff_pct_points(today, yesterday, "return_p50_pct")

    if return_p50_delta is not None:
        if abs(return_p50_delta) >= 5:
            score += 2
            reasons.append(
                f"Scenario centrale 30 giorni cambiato molto: "
                f"{fmt_delta(return_p50_delta, ' punti')}"
            )
        elif abs(return_p50_delta) >= 2:
            score += 1
            reasons.append(
                f"Scenario centrale 30 giorni cambiato: "
                f"{fmt_delta(return_p50_delta, ' punti')}"
            )

        if return_p50_delta > 0:
            improvement += 1
        elif return_p50_delta < 0:
            worsening += 1

    drawdown_p25_delta = diff_pct_points(today, yesterday, "drawdown_p25_pct")

    if drawdown_p25_delta is not None:
        # Per il drawdown:
        # più negativo = peggio.
        # meno negativo = meglio.
        if drawdown_p25_delta <= -5:
            score += 2
            worsening += 2
            reasons.append(
                f"Drawdown brutto peggiorato: {fmt_delta(drawdown_p25_delta, ' punti')}"
            )
        elif drawdown_p25_delta >= 5:
            score += 2
            improvement += 2
            reasons.append(
                f"Drawdown brutto migliorato: {fmt_delta(drawdown_p25_delta, ' punti')}"
            )
        elif abs(drawdown_p25_delta) >= 2:
            score += 1

            if drawdown_p25_delta > 0:
                improvement += 1
                reasons.append(
                    f"Drawdown migliorato leggermente: "
                    f"{fmt_delta(drawdown_p25_delta, ' punti')}"
                )
            else:
                worsening += 1
                reasons.append(
                    f"Drawdown peggiorato leggermente: "
                    f"{fmt_delta(drawdown_p25_delta, ' punti')}"
                )

    max_gain_p75_delta = diff_pct_points(today, yesterday, "max_gain_p75_pct")

    if max_gain_p75_delta is not None:
        if abs(max_gain_p75_delta) >= 8:
            score += 2
            reasons.append(
                f"Potenziale rialzo buono cambiato molto: "
                f"{fmt_delta(max_gain_p75_delta, ' punti')}"
            )
        elif abs(max_gain_p75_delta) >= 4:
            score += 1
            reasons.append(
                f"Potenziale rialzo buono cambiato: "
                f"{fmt_delta(max_gain_p75_delta, ' punti')}"
            )

        if max_gain_p75_delta > 0:
            improvement += 1
        elif max_gain_p75_delta < 0:
            worsening += 1

    price_delta = diff_price_pct(today, yesterday, "current_price")

    if price_delta is not None:
        if abs(price_delta) >= 5:
            score += 2
            reasons.append(
                f"Prezzo attuale cambiato molto: {fmt_delta(price_delta, '%')}"
            )
        elif abs(price_delta) >= 2:
            score += 1
            reasons.append(
                f"Prezzo attuale cambiato: {fmt_delta(price_delta, '%')}"
            )

    if not reasons:
        reasons.append("Nessuna variazione importante rispetto alla previsione precedente.")

    if score >= 5:
        level = "CAMBIAMENTO FORTE"
    elif score >= 2:
        level = "CAMBIAMENTO MEDIO"
    else:
        level = "NESSUN CAMBIAMENTO FORTE"

    if improvement > worsening:
        tone = "miglioramento"
    elif worsening > improvement:
        tone = "peggioramento"
    else:
        tone = "misto"

    return {
        "level": level,
        "score": score,
        "tone": tone,
        "reasons": reasons[:6],
    }


def simple_sentence(asset, change):
    short = asset_short(asset)
    level = change["level"]
    tone = change["tone"]

    if level == "PRIMA PREVISIONE":
        return (
            f"{short}: prima previsione salvata. "
            "Da domani si potrà fare il confronto giorno su giorno."
        )

    if level == "NESSUN DATO":
        return f"{short}: nessun dato disponibile."

    if level == "NESSUN CAMBIAMENTO FORTE":
        return f"{short}: nessun cambiamento forte rispetto a ieri."

    if tone == "miglioramento":
        return f"{short}: cambiamento importante in miglioramento rispetto a ieri."

    if tone == "peggioramento":
        return f"{short}: cambiamento importante in peggioramento rispetto a ieri."

    return f"{short}: cambiamento importante, ma lettura mista."


def build_report(log):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    summaries = []
    detail_blocks = []

    for asset in TARGETS:
        today, yesterday = get_latest_two_by_asset(log, asset)
        change = classify_change(today, yesterday)

        if today is not None:
            today_date = fmt_date(today.get("prediction_date"))
            today_verdict = str(today.get("verdict", "n/d"))
            today_positive = fmt_pct(today.get("positive_cases_30d"))
            today_return_p50 = fmt_pct(today.get("return_p50_pct"))
            today_drawdown_p25 = fmt_pct(today.get("drawdown_p25_pct"))
            today_max_gain_p75 = fmt_pct(today.get("max_gain_p75_pct"))
            today_price = fmt_price(today.get("current_price"))
        else:
            today_date = "n/d"
            today_verdict = "n/d"
            today_positive = "n/d"
            today_return_p50 = "n/d"
            today_drawdown_p25 = "n/d"
            today_max_gain_p75 = "n/d"
            today_price = "n/d"

        if yesterday is not None:
            yesterday_date = fmt_date(yesterday.get("prediction_date"))
            yesterday_verdict = str(yesterday.get("verdict", "n/d"))
            yesterday_price = fmt_price(yesterday.get("current_price"))
            yesterday_positive = fmt_pct(yesterday.get("positive_cases_30d"))
            yesterday_return_p50 = fmt_pct(yesterday.get("return_p50_pct"))
            yesterday_drawdown_p25 = fmt_pct(yesterday.get("drawdown_p25_pct"))
            yesterday_max_gain_p75 = fmt_pct(yesterday.get("max_gain_p75_pct"))

            positive_delta = fmt_delta(
                diff_pct_points(today, yesterday, "positive_cases_30d"),
                " punti",
            )
            return_delta = fmt_delta(
                diff_pct_points(today, yesterday, "return_p50_pct"),
                " punti",
            )
            drawdown_delta = fmt_delta(
                diff_pct_points(today, yesterday, "drawdown_p25_pct"),
                " punti",
            )
            max_gain_delta = fmt_delta(
                diff_pct_points(today, yesterday, "max_gain_p75_pct"),
                " punti",
            )
            price_delta = fmt_delta(
                diff_price_pct(today, yesterday, "current_price"),
                "%",
            )
        else:
            yesterday_date = "n/d"
            yesterday_verdict = "n/d"
            yesterday_price = "n/d"
            yesterday_positive = "n/d"
            yesterday_return_p50 = "n/d"
            yesterday_drawdown_p25 = "n/d"
            yesterday_max_gain_p75 = "n/d"

            positive_delta = "n/d"
            return_delta = "n/d"
            drawdown_delta = "n/d"
            max_gain_delta = "n/d"
            price_delta = "n/d"

        summaries.append(
            [
                asset_short(asset),
                change["level"],
                change["tone"],
                today_verdict,
                today_positive,
                positive_delta,
                return_delta,
                drawdown_delta,
            ]
        )

        reason_text = "\n".join(f"- {reason}" for reason in change["reasons"])

        detail = f"""
## {asset_name(asset)} — {asset_short(asset)}

### Sintesi

**{simple_sentence(asset, change)}**

### Confronto

{md_table(
    ["Dato", "Ieri", "Oggi", "Differenza"],
    [
        ["Data previsione", yesterday_date, today_date, "-"],
        [
            "Verdetto",
            yesterday_verdict,
            today_verdict,
            "cambio verdetto" if today_verdict != yesterday_verdict else "uguale",
        ],
        ["Prezzo attuale", yesterday_price, today_price, price_delta],
        ["Casi positivi 30d", yesterday_positive, today_positive, positive_delta],
        ["Return 30d centrale P50", yesterday_return_p50, today_return_p50, return_delta],
        ["Drawdown brutto P25", yesterday_drawdown_p25, today_drawdown_p25, drawdown_delta],
        ["Max gain buono P75", yesterday_max_gain_p75, today_max_gain_p75, max_gain_delta],
    ],
)}

### Perché

{reason_text}

---
"""
        detail_blocks.append(detail)

    text = f"""# Mini report cambiamenti giornalieri

Generato: **{rome_now}**  
UTC: **{utc_now}**

Questo report confronta l'ultima previsione salvata con quella precedente, asset per asset.

## Lettura velocissima

{md_table(
    [
        "Asset",
        "Cambio",
        "Tono",
        "Verdetto oggi",
        "Casi positivi oggi",
        "Δ casi positivi",
        "Δ return P50",
        "Δ drawdown P25",
    ],
    summaries,
)}

## Come leggerlo

- **NESSUN CAMBIAMENTO FORTE**: il report è simile a ieri.
- **CAMBIAMENTO MEDIO**: qualcosa si è mosso, ma non è ancora un ribaltamento netto.
- **CAMBIAMENTO FORTE**: vale la pena aprire il report completo.
- **Tono miglioramento**: lo scenario statistico è migliorato rispetto a ieri.
- **Tono peggioramento**: lo scenario statistico è peggiorato rispetto a ieri.
- **Drawdown P25**: se diventa più negativo, il rischio di discesa interna ai 30 giorni peggiora.

---
"""

    text += "\n".join(detail_blocks)

    return text


def build_main_report_block(log):
    rows = []
    simple_lines = []

    for asset in TARGETS:
        today, yesterday = get_latest_two_by_asset(log, asset)
        change = classify_change(today, yesterday)

        rows.append(
            [
                asset_short(asset),
                change["level"],
                change["tone"],
                str(today.get("verdict", "n/d")) if today is not None else "n/d",
                fmt_pct(today.get("positive_cases_30d")) if today is not None else "n/d",
                (
                    fmt_delta(
                        diff_pct_points(today, yesterday, "positive_cases_30d"),
                        " punti",
                    )
                    if yesterday is not None
                    else "n/d"
                ),
            ]
        )

        simple_lines.append(f"- {simple_sentence(asset, change)}")

    return f"""
<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

{chr(10).join(simple_lines)}

{md_table(
    [
        "Asset",
        "Cambio",
        "Tono",
        "Verdetto oggi",
        "Casi positivi oggi",
        "Δ casi positivi",
    ],
    rows,
)}

<!-- DAILY_CHANGE_END -->
"""


def inject_into_main_report(log):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- DAILY_CHANGE_START -->"
    end_marker = "<!-- DAILY_CHANGE_END -->"

    # Rimuove il vecchio blocco, se esiste già.
    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    block = build_main_report_block(log).strip()

    # Lo mettiamo all'inizio del report, prima delle sezioni lunghe.
    # Così appena apri latest_report.md capisci subito se vale la pena leggere tutto.
    insertion_markers = [
        "\n# Come leggere questo report",
        "\n# Scheda veloce",
        "\n# Lettura velocissima",
        "\n## Lettura velocissima",
        "\n# Mappa semplice",
        "\n# Come leggere correttamente",
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
        # Piano B: se non trova i titoli previsti,
        # lo mette subito dopo la prima riga del report.
        first_newline = current.find("\n")

        if first_newline != -1:
            new_text = (
                current[: first_newline + 1].rstrip()
                + "\n\n"
                + block
                + "\n\n"
                + current[first_newline + 1 :].lstrip()
            )
        else:
            new_text = block + "\n\n" + current

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    log = read_csv_safe(PREDICTION_LOG_PATH)

    report = build_report(log)

    with open(DAILY_CHANGE_MD_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    inject_into_main_report(log)

    print(f"Wrote {DAILY_CHANGE_MD_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
