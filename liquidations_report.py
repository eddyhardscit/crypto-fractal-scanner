import os
import csv
import json
import math
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


REPORT_DIR = "reports"
LIQ_REPORT_PATH = "reports/liquidation_report.md"
LIQ_CSV_PATH = "reports/liquidation_metrics.csv"
MAIN_REPORT_PATH = "reports/latest_report.md"

OKX_BASE = "https://www.okx.com"

SYMBOLS = [
    {"asset": "BTC", "name": "Bitcoin", "inst_id": "BTC-USDT-SWAP", "ccy": "BTC"},
    {"asset": "SOL", "name": "Solana", "inst_id": "SOL-USDT-SWAP", "ccy": "SOL"},
    {"asset": "DOGE", "name": "Dogecoin", "inst_id": "DOGE-USDT-SWAP", "ccy": "DOGE"},
]


def get_json(path, params=None, timeout=20):
    params = params or {}
    query = urllib.parse.urlencode(params)
    url = f"{OKX_BASE}{path}"
    if query:
        url += "?" + query

    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "crypto-fractal-scanner/1.0",
        },
    )

    with urllib.request.urlopen(req, timeout=timeout) as response:
        raw = json.loads(response.read().decode("utf-8"))

    if str(raw.get("code")) != "0":
        raise RuntimeError(f"OKX error code={raw.get('code')} msg={raw.get('msg')}")

    return raw.get("data") or []


def safe_float(value):
    try:
        if value is None:
            return None
        value = float(value)
        if math.isnan(value) or math.isinf(value):
            return None
        return value
    except Exception:
        return None


def first_data(data):
    if isinstance(data, list) and data:
        return data[0]
    return {}


def latest_data(data):
    if isinstance(data, list) and data:
        return data[-1]
    return {}


def pct_change(first, last):
    first = safe_float(first)
    last = safe_float(last)

    if first is None or last is None or first == 0:
        return None

    return ((last - first) / first) * 100


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

    return f"{value:+.{decimals}f}%"


def fmt_number(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    return f"{value:,.{decimals}f}"


def fmt_usd(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    if abs(value) >= 1_000_000_000:
        return f"${value / 1_000_000_000:,.2f}B"

    if abs(value) >= 1_000_000:
        return f"${value / 1_000_000:,.2f}M"

    if abs(value) >= 1_000:
        return f"${value / 1_000:,.2f}K"

    return f"${value:,.2f}"


def timestamp_ms_to_rome(ms):
    ms = safe_float(ms)

    if ms is None:
        return "n/d"

    dt = datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
    return dt.astimezone(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M")


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")

    return "\n".join(lines)


def extract_history_value(row):
    """
    OKX trading-data endpoints possono restituire liste.
    Qui prendiamo il primo valore numerico utile dopo il timestamp.
    Serve solo per calcolare variazione percentuale nello stesso tipo di dato.
    """
    if isinstance(row, dict):
        for key in [
            "openInterest",
            "oi",
            "oiUsd",
            "openInterestUsd",
            "sumOpenInterestValue",
            "value",
        ]:
            if key in row:
                return safe_float(row.get(key))

    if isinstance(row, list):
        for value in row[1:]:
            number = safe_float(value)
            if number is not None:
                return number

    return None


def fetch_okx_asset(cfg):
    inst_id = cfg["inst_id"]
    ccy = cfg["ccy"]
    errors = []

    def call(label, path, params):
        try:
            return get_json(path, params=params)
        except Exception as exc:
            errors.append(f"{label}: {exc}")
            return []

    ticker_data = call(
        "ticker",
        "/api/v5/market/ticker",
        {"instId": inst_id},
    )

    mark_data = call(
        "mark price",
        "/api/v5/public/mark-price",
        {"instType": "SWAP", "instId": inst_id},
    )

    funding_data = call(
        "funding rate",
        "/api/v5/public/funding-rate",
        {"instId": inst_id},
    )

    oi_data = call(
        "open interest",
        "/api/v5/public/open-interest",
        {"instType": "SWAP", "instId": inst_id},
    )

    oi_history = call(
        "open interest history",
        "/api/v5/rubik/stat/contracts/open-interest-volume",
        {"ccy": ccy, "period": "1H"},
    )

    long_short_history = call(
        "long short ratio",
        "/api/v5/rubik/stat/contracts/long-short-account-ratio",
        {"ccy": ccy, "period": "1H"},
    )

    ticker = first_data(ticker_data)
    mark = first_data(mark_data)
    funding = first_data(funding_data)
    oi = first_data(oi_data)

    price = safe_float(mark.get("markPx"))
    if price is None:
        price = safe_float(ticker.get("last"))

    open_24h = safe_float(ticker.get("open24h"))
    last_price = safe_float(ticker.get("last"))

    price_24h_pct = pct_change(open_24h, last_price)

    funding_pct = None
    funding_raw = safe_float(funding.get("fundingRate"))
    if funding_raw is not None:
        funding_pct = funding_raw * 100

    next_funding_time = timestamp_ms_to_rome(funding.get("fundingTime"))

    oi_coin = safe_float(oi.get("oiCcy"))
    oi_contracts = safe_float(oi.get("oi"))

    oi_value_usd = None
    if oi_coin is not None and price is not None:
        oi_value_usd = oi_coin * price

    first_oi_value = extract_history_value(first_data(oi_history))
    last_oi_value = extract_history_value(latest_data(oi_history))
    oi_24h_pct = pct_change(first_oi_value, last_oi_value)

    long_short_ratio = extract_history_value(latest_data(long_short_history))

    item = {
        "asset": cfg["asset"],
        "name": cfg["name"],
        "inst_id": inst_id,
        "price": price,
        "price_24h_pct": price_24h_pct,
        "funding_pct": funding_pct,
        "next_funding_time": next_funding_time,
        "open_interest_coin": oi_coin,
        "open_interest_contracts": oi_contracts,
        "open_interest_value_usd": oi_value_usd,
        "open_interest_24h_pct": oi_24h_pct,
        "long_short_ratio": long_short_ratio,
        "errors": errors,
    }

    item["score"] = score_asset(item)
    item["simple"] = simple_translation(item)

    return item


def score_asset(item):
    downside = 0
    upside = 0
    stress = 0
    reasons = []

    funding = item.get("funding_pct")
    oi_24h = item.get("open_interest_24h_pct")
    price_24h = item.get("price_24h_pct")
    long_short_ratio = item.get("long_short_ratio")

    if funding is not None:
        if funding >= 0.03:
            downside += 2
            reasons.append("funding molto positivo: molti long pagano per restare aperti")
        elif funding >= 0.01:
            downside += 1
            reasons.append("funding positivo: mercato leggermente carico di long")
        elif funding <= -0.03:
            upside += 2
            reasons.append("funding molto negativo: molti short pagano per restare aperti")
        elif funding <= -0.01:
            upside += 1
            reasons.append("funding negativo: mercato leggermente carico di short")

    if oi_24h is not None:
        if oi_24h >= 5:
            stress += 2
            reasons.append("open interest in forte aumento: entra molta leva")
        elif oi_24h >= 2:
            stress += 1
            reasons.append("open interest in aumento: leva in crescita")
        elif oi_24h <= -5:
            reasons.append("open interest in forte calo: parte della leva è già uscita")

    if oi_24h is not None and price_24h is not None and funding is not None:
        if oi_24h >= 2 and price_24h > 0 and funding > 0:
            downside += 2
            reasons.append("prezzo su + leva su + funding positivo: rischio pulizia dei long sotto")
        elif oi_24h >= 2 and price_24h < 0 and funding < 0:
            upside += 2
            reasons.append("prezzo giù + leva su + funding negativo: rischio short squeeze sopra")

    if long_short_ratio is not None:
        if long_short_ratio >= 1.25:
            downside += 1
            reasons.append("long/short ratio alto: più mercato sbilanciato long")
        elif long_short_ratio <= 0.80:
            upside += 1
            reasons.append("long/short ratio basso: più mercato sbilanciato short")

    delta = downside - upside

    if delta >= 2:
        label = "RISCHIO DISCESA / FLUSH SOTTO"
        short_label = "Rischio sotto"
    elif delta <= -2:
        label = "RISCHIO SHORT SQUEEZE SOPRA"
        short_label = "Rischio sopra"
    else:
        if stress >= 2:
            label = "MOLTA LEVA MA DIREZIONE MISTA"
            short_label = "Leva alta, direzione mista"
        else:
            label = "NEUTRALE / POCO CHIARO"
            short_label = "Misto"

    strength = min(5, max(1, abs(delta) + max(0, stress)))

    return {
        "label": label,
        "short_label": short_label,
        "strength": strength,
        "downside_score": downside,
        "upside_score": upside,
        "stress_score": stress,
        "reasons": reasons[:6],
    }


def simple_translation(item):
    asset = item["asset"]
    score = item["score"]
    label = score["label"]

    funding = item.get("funding_pct")
    oi_24h = item.get("open_interest_24h_pct")
    long_short_ratio = item.get("long_short_ratio")

    if "FLUSH SOTTO" in label:
        main = (
            f"{asset}: i futures sembrano più vulnerabili verso una discesa improvvisa. "
            "Non significa che deve scendere, ma se rompe sotto può accelerare."
        )
        action = (
            "Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale."
        )

    elif "SHORT SQUEEZE" in label:
        main = (
            f"{asset}: i futures sembrano più vulnerabili verso uno squeeze sopra. "
            "Non significa rialzo certo, ma se rompe sopra può accelerare."
        )
        action = (
            "Per uno short a leva: prudenza alta. Per un long: interessante solo se il frattale non è contrario."
        )

    elif "MOLTA LEVA" in label:
        main = (
            f"{asset}: c'è molta leva nel mercato, ma la direzione non è pulita. "
            "Può arrivare un movimento violento, ma non è chiaro se sopra o sotto."
        )
        action = (
            "Meglio non forzare. Aspetta conferma dal frattale o dal prezzo."
        )

    else:
        main = (
            f"{asset}: i futures non danno una lettura chiara. "
            "Non si vede uno sbilanciamento forte né long né short."
        )
        action = (
            "Qui pesa di più il report frattale."
        )

    details = []

    if funding is not None:
        if funding > 0:
            details.append("funding positivo: i long pagano gli short")
        elif funding < 0:
            details.append("funding negativo: gli short pagano i long")
        else:
            details.append("funding quasi neutro")

    if oi_24h is not None:
        if oi_24h > 2:
            details.append("open interest in aumento: più leva nel sistema")
        elif oi_24h < -2:
            details.append("open interest in calo: leva in uscita")
        else:
            details.append("open interest abbastanza stabile")

    if long_short_ratio is not None:
        if long_short_ratio > 1.25:
            details.append("long/short ratio alto: mercato più long")
        elif long_short_ratio < 0.80:
            details.append("long/short ratio basso: mercato più short")
        else:
            details.append("long/short ratio abbastanza equilibrato")

    return {
        "main": main,
        "action": action,
        "details": details,
        "strength_text": f"Forza segnale: {score['strength']}/5",
    }


def theoretical_liquidation_rows(price):
    price = safe_float(price)

    if price is None:
        return [["n/d", "n/d", "n/d"]]

    rows = []

    for lev in [5, 10, 20, 50]:
        long_liq = price * (1 - 1 / lev)
        short_liq = price * (1 + 1 / lev)

        rows.append(
            [
                f"{lev}x",
                fmt_price(long_liq),
                fmt_price(short_liq),
            ]
        )

    return rows


def build_report(results):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    simple_rows = []
    metric_rows = []

    for item in results:
        score = item["score"]
        simple = item["simple"]

        simple_rows.append(
            [
                item["asset"],
                score["short_label"],
                f"{score['strength']}/5",
                simple["action"],
            ]
        )

        metric_rows.append(
            [
                item["asset"],
                fmt_price(item["price"]),
                fmt_pct(item["price_24h_pct"]),
                fmt_pct(item["funding_pct"], 4),
                fmt_usd(item["open_interest_value_usd"]),
                fmt_pct(item["open_interest_24h_pct"]),
                fmt_number(item["long_short_ratio"]),
            ]
        )

    text = f"""# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **{rome_now}**  
UTC: **{utc_now}**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

{md_table(["Asset", "Lettura", "Forza", "Cosa significa in pratica"], simple_rows)}

## Numeri principali

{md_table(["Asset", "Prezzo", "Prezzo 24h", "Funding", "Open Interest", "OI 24h", "Long/Short"], metric_rows)}

## Spiegazione rapida dei termini

- **Funding positivo**: i long pagano gli short. Se è troppo positivo, tanti stanno scommettendo al rialzo.
- **Funding negativo**: gli short pagano i long. Se è troppo negativo, tanti stanno scommettendo al ribasso.
- **Open Interest / OI**: quanta leva è aperta sul mercato. Se sale, entra più leva. Se scende, la leva sta uscendo.
- **Long/Short sopra 1**: più mercato orientato long.
- **Long/Short sotto 1**: più mercato orientato short.
- **Flush sotto**: discesa rapida per pulire i long.
- **Short squeeze sopra**: salita rapida per liquidare gli short.

---
"""

    for item in results:
        simple = item["simple"]
        score = item["score"]

        text += f"""
## {item['name']} — {item['asset']}

### Lettura semplice

**{score['label']}**  
**{simple['strength_text']}**

{simple['main']}

**Tradotto operativamente:** {simple['action']}

### Perché

"""

        if simple["details"]:
            for detail in simple["details"]:
                text += f"- {detail}\n"
        else:
            text += "- Dati futures poco chiari o parziali.\n"

        text += f"""
### Numeri controllati

{md_table(
    ["Dato", "Valore", "Traduzione"],
    [
        ["Prezzo", fmt_price(item["price"]), "prezzo futures/mark usato come riferimento"],
        ["Prezzo 24h", fmt_pct(item["price_24h_pct"]), "movimento dell'ultimo giorno"],
        ["Funding", fmt_pct(item["funding_pct"], 4), "positivo = long pagano; negativo = short pagano"],
        ["Prossimo funding", item["next_funding_time"], "prossimo aggiornamento funding"],
        ["Open Interest stimato", fmt_usd(item["open_interest_value_usd"]), "leva aperta stimata in dollari"],
        ["Open Interest 24h", fmt_pct(item["open_interest_24h_pct"]), "leva entrata o uscita nelle ultime 24h"],
        ["Long/Short ratio", fmt_number(item["long_short_ratio"]), "sopra 1 = più long; sotto 1 = più short"],
    ],
)}

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

{md_table(["Leva", "Long liquidato circa sotto", "Short liquidato circa sopra"], theoretical_liquidation_rows(item["price"]))}

"""

        if score["reasons"]:
            text += "### Note tecniche usate dallo score\n\n"

            for reason in score["reasons"]:
                text += f"- {reason}\n"

            text += "\n"

        if item["errors"]:
            text += "### Dati mancanti / errori\n\n"

            for err in item["errors"]:
                text += f"- {err}\n"

            text += "\n"

        text += "---\n"

    return text


def build_main_report_summary(results):
    rows = []
    simple_lines = []

    for item in results:
        score = item["score"]
        simple = item["simple"]

        rows.append(
            [
                item["asset"],
                fmt_price(item["price"]),
                fmt_pct(item["funding_pct"], 4),
                fmt_pct(item["open_interest_24h_pct"]),
                fmt_number(item["long_short_ratio"]),
                score["short_label"],
                f"{score['strength']}/5",
            ]
        )

        simple_lines.append(
            f"**{item['asset']}** — {simple['main']} {simple['action']}"
        )

    simple_text = "\n\n".join(simple_lines)

    return f"""

<!-- LIQUIDATION_SUMMARY_START -->

---

# Sintesi semplice futures / liquidazioni

Report separato completo: [liquidation_report.md](liquidation_report.md)

{simple_text}

{md_table(["Asset", "Prezzo", "Funding", "OI 24h", "Long/Short", "Lettura futures", "Forza"], rows)}

## Come usarla insieme al frattale

- Frattale ribassista + futures con rischio sotto = prudenza alta.
- Frattale rialzista + futures con rischio sopra = segnale più interessante.
- Frattale e futures opposti = situazione sporca, meglio non forzare.
- Per posizioni a leva, il futures report serve soprattutto a capire se può arrivare una pulizia violenta prima dei 30 giorni.

<!-- LIQUIDATION_SUMMARY_END -->
"""


def append_summary_to_main_report(results):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- LIQUIDATION_SUMMARY_START -->"
    end_marker = "<!-- LIQUIDATION_SUMMARY_END -->"

    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    summary = build_main_report_summary(results)

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(current.rstrip() + "\n\n" + summary.strip() + "\n")


def write_csv(results):
    fieldnames = [
        "asset",
        "inst_id",
        "price",
        "price_24h_pct",
        "funding_pct",
        "open_interest_coin",
        "open_interest_contracts",
        "open_interest_value_usd",
        "open_interest_24h_pct",
        "long_short_ratio",
        "label",
        "strength",
        "downside_score",
        "upside_score",
        "stress_score",
    ]

    with open(LIQ_CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in results:
            score = item["score"]

            writer.writerow(
                {
                    "asset": item["asset"],
                    "inst_id": item["inst_id"],
                    "price": item["price"],
                    "price_24h_pct": item["price_24h_pct"],
                    "funding_pct": item["funding_pct"],
                    "open_interest_coin": item["open_interest_coin"],
                    "open_interest_contracts": item["open_interest_contracts"],
                    "open_interest_value_usd": item["open_interest_value_usd"],
                    "open_interest_24h_pct": item["open_interest_24h_pct"],
                    "long_short_ratio": item["long_short_ratio"],
                    "label": score["label"],
                    "strength": score["strength"],
                    "downside_score": score["downside_score"],
                    "upside_score": score["upside_score"],
                    "stress_score": score["stress_score"],
                }
            )


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    results = []

    for cfg in SYMBOLS:
        print(f"Fetching OKX futures data for {cfg['asset']}...")
        results.append(fetch_okx_asset(cfg))

    report = build_report(results)

    with open(LIQ_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    write_csv(results)
    append_summary_to_main_report(results)

    print(f"Wrote {LIQ_REPORT_PATH}")
    print(f"Wrote {LIQ_CSV_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
