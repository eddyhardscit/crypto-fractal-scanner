import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd


REPORT_DIR = "reports"

PREDICTION_LOG_PATH = "reports/prediction_log.csv"
ACCURACY_CSV_PATH = "reports/accuracy_report.csv"
CALIBRATION_CSV_PATH = "reports/calibration_report.csv"

ACCURACY_MD_PATH = "reports/accuracy_report.md"
CALIBRATION_MD_PATH = "reports/calibration_report.md"
MAIN_REPORT_PATH = "reports/latest_report.md"

TARGETS = ["BTC-USD", "SOL-USD", "DOGE-USD"]

MIN_CALIBRATION_EVALS = 30
STRONG_CALIBRATION_EVALS = 60


def asset_name(asset):
    if asset == "BTC-USD":
        return "Bitcoin"
    if asset == "SOL-USD":
        return "Solana"
    if asset == "DOGE-USD":
        return "Dogecoin"
    return asset


def asset_short(asset):
    if asset == "BTC-USD":
        return "BTC"
    if asset == "SOL-USD":
        return "SOL"
    if asset == "DOGE-USD":
        return "DOGE"
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
    except pd.errors.EmptyDataError:
        return pd.DataFrame()
    except Exception:
        return pd.DataFrame()


def bool_series(series):
    if series is None:
        return pd.Series(dtype=bool)

    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def fmt_pct(value):
    try:
        if pd.isna(value):
            return "n/d"
        return f"{float(value):.2f}%".replace(".", ",")
    except Exception:
        return "n/d"


def fmt_number(value):
    try:
        if pd.isna(value):
            return "n/d"
        return str(int(value))
    except Exception:
        return "n/d"


def fmt_date(value):
    if value is None or pd.isna(value):
        return "n/d"

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


def progress_bar(value, total):
    try:
        value = int(value)
    except Exception:
        value = 0

    value = max(0, value)
    total = max(1, int(total))

    filled = int(round(min(value, total) / total * 10))
    empty = 10 - filled

    return "[" + "█" * filled + "░" * empty + "]"


def calibration_status_label(evaluated_count):
    if evaluated_count >= STRONG_CALIBRATION_EVALS:
        return "ATTIVA FORTE"
    if evaluated_count >= MIN_CALIBRATION_EVALS:
        return "ATTIVA"
    return "RACCOLTA DATI"


def calibration_status_text(evaluated_count):
    if evaluated_count >= STRONG_CALIBRATION_EVALS:
        return (
            "La calibrazione è attiva e ha già parecchi dati. "
            "La lettura corretta dagli errori passati inizia a essere più interessante."
        )

    if evaluated_count >= MIN_CALIBRATION_EVALS:
        return (
            "La calibrazione è attiva. Lo scanner ha abbastanza previsioni controllate "
            "per iniziare a correggere i propri errori."
        )

    missing = MIN_CALIBRATION_EVALS - evaluated_count

    return (
        f"La calibrazione non è ancora attiva. Mancano ancora {missing} "
        f"previsioni controllate per arrivare a {MIN_CALIBRATION_EVALS}."
    )


def compute_asset_status(log, asset):
    today = pd.Timestamp(datetime.now(timezone.utc).date())

    if log.empty or "asset" not in log.columns:
        return {
            "asset": asset,
            "total_predictions": 0,
            "evaluated_predictions": 0,
            "pending_predictions": 0,
            "mature_waiting": 0,
            "first_prediction": None,
            "last_prediction": None,
            "next_evaluation_date": None,
            "days_to_next_evaluation": None,
            "directional_accuracy_pct": np.nan,
            "avg_central_error_pct": np.nan,
            "risk_zone_touched_pct": np.nan,
            "calibration_status": calibration_status_label(0),
        }

    asset_rows = log[log["asset"].astype(str) == asset].copy()

    if asset_rows.empty:
        return {
            "asset": asset,
            "total_predictions": 0,
            "evaluated_predictions": 0,
            "pending_predictions": 0,
            "mature_waiting": 0,
            "first_prediction": None,
            "last_prediction": None,
            "next_evaluation_date": None,
            "days_to_next_evaluation": None,
            "directional_accuracy_pct": np.nan,
            "avg_central_error_pct": np.nan,
            "risk_zone_touched_pct": np.nan,
            "calibration_status": calibration_status_label(0),
        }

    asset_rows["prediction_date_dt"] = pd.to_datetime(
        asset_rows.get("prediction_date"),
        errors="coerce",
    )

    asset_rows = asset_rows.dropna(subset=["prediction_date_dt"]).copy()

    if asset_rows.empty:
        total_predictions = 0
        evaluated_predictions = 0
        pending_predictions = 0
        mature_waiting = 0
        first_prediction = None
        last_prediction = None
        next_eval = None
        days_to_next = None
    else:
        if "evaluated" in asset_rows.columns:
            evaluated_mask = bool_series(asset_rows["evaluated"])
        else:
            evaluated_mask = pd.Series(False, index=asset_rows.index)

        total_predictions = len(asset_rows)
        evaluated_predictions = int(evaluated_mask.sum())
        pending_predictions = int(total_predictions - evaluated_predictions)

        asset_rows["due_date"] = asset_rows["prediction_date_dt"] + pd.Timedelta(days=30)

        pending_rows = asset_rows[~evaluated_mask].copy()
        mature_waiting = int((pending_rows["due_date"] <= today).sum())

        future_due = pending_rows[pending_rows["due_date"] > today].copy()

        if future_due.empty:
            next_eval = None
            days_to_next = None
        else:
            next_eval = future_due["due_date"].min()
            days_to_next = int((next_eval.normalize() - today).days)

        first_prediction = asset_rows["prediction_date_dt"].min()
        last_prediction = asset_rows["prediction_date_dt"].max()

    evaluated_rows = asset_rows[
        bool_series(asset_rows.get("evaluated", pd.Series(False, index=asset_rows.index)))
    ].copy() if not asset_rows.empty else pd.DataFrame()

    directional_accuracy = np.nan
    central_error = np.nan
    risk_zone_touched = np.nan

    if not evaluated_rows.empty:
        if "directional_correct" in evaluated_rows.columns:
            directional_valid = evaluated_rows["directional_correct"].dropna()
            directional_valid = directional_valid[
                directional_valid.astype(str).str.lower().isin(["true", "false", "1", "0"])
            ]

            if len(directional_valid) > 0:
                directional_accuracy = (
                    directional_valid.astype(str).str.lower().isin(["true", "1"]).mean()
                    * 100
                )

        if "central_error_pct" in evaluated_rows.columns:
            central_error = pd.to_numeric(
                evaluated_rows["central_error_pct"],
                errors="coerce",
            ).mean()

        if "risk_zone_touched" in evaluated_rows.columns:
            risk_valid = evaluated_rows["risk_zone_touched"].dropna()
            risk_valid = risk_valid[
                risk_valid.astype(str).str.lower().isin(["true", "false", "1", "0"])
            ]

            if len(risk_valid) > 0:
                risk_zone_touched = (
                    risk_valid.astype(str).str.lower().isin(["true", "1"]).mean()
                    * 100
                )

    return {
        "asset": asset,
        "total_predictions": total_predictions,
        "evaluated_predictions": evaluated_predictions,
        "pending_predictions": pending_predictions,
        "mature_waiting": mature_waiting,
        "first_prediction": first_prediction,
        "last_prediction": last_prediction,
        "next_evaluation_date": next_eval,
        "days_to_next_evaluation": days_to_next,
        "directional_accuracy_pct": directional_accuracy,
        "avg_central_error_pct": central_error,
        "risk_zone_touched_pct": risk_zone_touched,
        "calibration_status": calibration_status_label(evaluated_predictions),
    }


def next_eval_text(status):
    next_date = status.get("next_evaluation_date")
    days = status.get("days_to_next_evaluation")

    if next_date is None or pd.isna(next_date):
        if status.get("pending_predictions", 0) == 0:
            return "nessuna previsione in attesa"
        return "in attesa dati"

    date_text = fmt_date(next_date)

    if days is None:
        return date_text

    if days <= 0:
        return f"{date_text} / già valutabile"

    if days == 1:
        return f"{date_text} / tra 1 giorno"

    return f"{date_text} / tra {days} giorni"


def build_status_rows(statuses):
    rows = []

    for status in statuses:
        evaluated = status["evaluated_predictions"]
        total = status["total_predictions"]
        pending = status["pending_predictions"]

        progress_value = min(evaluated, MIN_CALIBRATION_EVALS)

        rows.append(
            [
                asset_short(status["asset"]),
                str(total),
                str(evaluated),
                f"{progress_value}/{MIN_CALIBRATION_EVALS} {progress_bar(progress_value, MIN_CALIBRATION_EVALS)}",
                str(pending),
                status["calibration_status"],
                next_eval_text(status),
            ]
        )

    return rows


def build_accuracy_md(statuses):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    text = f"""# Report accuratezza scanner

Generato: **{rome_now}**  
UTC: **{utc_now}**

Questo report spiega se lo scanner ha già abbastanza previsioni vecchie da controllare.

## Lettura velocissima

{md_table(
    [
        "Asset",
        "Previsioni fatte",
        "Previsioni controllate",
        "Progresso verso calibrazione",
        "Previsioni in attesa",
        "Stato",
        "Prossimo controllo",
    ],
    build_status_rows(statuses),
)}

## Come leggere questi numeri

- **Previsioni fatte**: quante previsioni lo scanner ha salvato nel diario.
- **Previsioni controllate**: quante previsioni hanno già compiuto 30 giorni e sono state confrontate con la realtà.
- **0/30**: calibrazione non ancora attiva.
- **30/30**: calibrazione attiva.
- **60+ controllate**: calibrazione più solida.
- **Previsioni in attesa**: previsioni già salvate, ma non ancora abbastanza vecchie per essere controllate.

---
"""

    for status in statuses:
        name = asset_name(status["asset"])
        evaluated = status["evaluated_predictions"]
        total = status["total_predictions"]

        text += f"""
## {name}

### Stato

- Previsioni fatte: **{total}**
- Previsioni controllate: **{evaluated}/{MIN_CALIBRATION_EVALS}**
- Barra progresso: **{progress_bar(min(evaluated, MIN_CALIBRATION_EVALS), MIN_CALIBRATION_EVALS)}**
- Previsioni in attesa: **{status["pending_predictions"]}**
- Previsioni già mature ma non ancora valutate: **{status["mature_waiting"]}**
- Prima previsione salvata: **{fmt_date(status["first_prediction"])}**
- Ultima previsione salvata: **{fmt_date(status["last_prediction"])}**
- Prossimo controllo previsto: **{next_eval_text(status)}**
- Stato calibrazione: **{status["calibration_status"]}**

### Accuratezza, quando disponibile

- Direzione corretta: **{fmt_pct(status["directional_accuracy_pct"])}**
- Errore medio scenario centrale: **{fmt_pct(status["avg_central_error_pct"])}**
- Zona rischio toccata: **{fmt_pct(status["risk_zone_touched_pct"])}**

### Traduzione semplice

{calibration_status_text(evaluated)}

---
"""

    return text


def build_calibration_md(statuses):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    text = f"""# Stato calibrazione scanner

Generato: **{rome_now}**  
UTC: **{utc_now}**

La calibrazione non serve a prevedere direttamente il prezzo.  
Serve a capire se lo scanner, col tempo, è stato troppo ottimista, troppo pessimista o abbastanza preciso.

## Stato attuale

{md_table(
    [
        "Asset",
        "Fatte",
        "Controllate",
        "Progresso",
        "In attesa",
        "Stato",
        "Prossimo controllo",
    ],
    build_status_rows(statuses),
)}

## Regola semplice

- Sotto **30/30**: lo scanner sta solo raccogliendo dati.
- Da **30/30**: la calibrazione inizia ad attivarsi.
- Da **60+ controllate**: la calibrazione diventa più interessante.
- Se il workflow non gira, non vengono salvate nuove previsioni.
- Se fai Run workflow manuale, la previsione viene salvata comunque.

---
"""

    for status in statuses:
        evaluated = status["evaluated_predictions"]
        name = asset_name(status["asset"])

        text += f"""
## {name}

**Progresso calibrazione:** {min(evaluated, MIN_CALIBRATION_EVALS)}/{MIN_CALIBRATION_EVALS}  
**Stato:** {status["calibration_status"]}

{calibration_status_text(evaluated)}

"""

        if evaluated >= MIN_CALIBRATION_EVALS:
            text += (
                "La calibrazione può iniziare a correggere la previsione grezza usando "
                "gli errori passati dello scanner.\n\n"
            )
        else:
            missing = MIN_CALIBRATION_EVALS - evaluated
            text += (
                f"Servono ancora **{missing}** previsioni controllate prima che la calibrazione "
                "inizi davvero a lavorare.\n\n"
            )

        text += "---\n"

    return text


def build_main_report_block(statuses):
    rows = build_status_rows(statuses)

    simple_lines = []

    for status in statuses:
        evaluated = status["evaluated_predictions"]
        total = status["total_predictions"]
        short = asset_short(status["asset"])

        simple_lines.append(
            f"- **{short}**: {evaluated}/{MIN_CALIBRATION_EVALS} previsioni controllate "
            f"su {total} fatte. Stato: **{status['calibration_status']}**."
        )

    simple_text = "\n".join(simple_lines)

    return f"""

<!-- CALIBRATION_READABLE_START -->

---

# Stato leggibile accuratezza / calibrazione

Report dettagliati:
- [accuracy_report.md](accuracy_report.md)
- [calibration_report.md](calibration_report.md)

## Riassunto semplice

{simple_text}

{md_table(
    [
        "Asset",
        "Previsioni fatte",
        "Controllate",
        "Progresso",
        "In attesa",
        "Stato",
        "Prossimo controllo",
    ],
    rows,
)}

## Traduzione

- **0/30** significa: lo scanner sta ancora raccogliendo dati.
- **30/30** significa: la calibrazione comincia ad attivarsi.
- **60+** significa: la calibrazione diventa più solida.
- L'email non c'entra con la calibrazione: conta solo che il workflow giri e salvi il diario delle previsioni.

<!-- CALIBRATION_READABLE_END -->
"""


def inject_into_main_report(statuses):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- CALIBRATION_READABLE_START -->"
    end_marker = "<!-- CALIBRATION_READABLE_END -->"

    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    block = build_main_report_block(statuses)

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(current.rstrip() + "\n\n" + block.strip() + "\n")


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    prediction_log = read_csv_safe(PREDICTION_LOG_PATH)

    statuses = []

    for asset in TARGETS:
        statuses.append(compute_asset_status(prediction_log, asset))

    accuracy_md = build_accuracy_md(statuses)
    calibration_md = build_calibration_md(statuses)

    with open(ACCURACY_MD_PATH, "w", encoding="utf-8") as f:
        f.write(accuracy_md)

    with open(CALIBRATION_MD_PATH, "w", encoding="utf-8") as f:
        f.write(calibration_md)

    inject_into_main_report(statuses)

    print(f"Wrote {ACCURACY_MD_PATH}")
    print(f"Wrote {CALIBRATION_MD_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
