"""Explicit, reversible retirement of secondary diagnostics; no trading authority."""
from __future__ import annotations
import csv
import hashlib
import json
import math
import re
import statistics
from datetime import datetime, timezone, date
from pathlib import Path

POLICY_VERSION = "2026-10-13-v1"
RISK_QUARANTINED = True
PAUSED = {
    "btc_2022_vs_sol_2026_report": ("BTC_SOL_FRACTAL", "Frattale BTC 2022 / SOL 2026", "btc_2022_vs_sol_2026_report.md"),
    "fractal_path_tracker": ("FRACTAL_PATH_TRACKER", "Tracking frattale SOL/BTC", "fractal_path_tracker.md"),
    "rsi_top_cycle_report": ("RSI_TOP_CYCLE", "RSI top-cycle SOL", "rsi_top_cycle_report.md"),
    "sol_onchain_metrics_report": ("SOL_ONCHAIN_METRICS", "Metriche on-chain SOL", "sol_onchain_metrics_report.md"),
    "extreme_cases_path_report": ("EXTREME_CASES_PATH", "Percorsi dei casi estremi", "extreme_cases_path_report.md"),
}
PAUSED_COMPONENTS = ("Frattale SOL", "Fractal path", "RSI top-cycle")
PAUSED_QUALITY_NAMES = ("Frattale BTC/SOL", "Fractal path", "RSI top-cycle")
PAUSED_PRICE_FILES = {
    "btc_2022_vs_sol_2026_report.md", "btc_2022_vs_sol_2026_metrics.csv",
    "fractal_path_tracker.md", "fractal_path_tracker_metrics.csv",
    "rsi_top_cycle_report.md", "rsi_top_cycle_metrics.csv",
    "sol_onchain_metrics_report.md", "sol_onchain_metrics_latest.csv",
    "sol_onchain_metrics_latest.json",
}
REVIEW_DATE = "2026-11-13"
VALIDATION_START = "2026-10-14"

def atomic_text(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name("." + path.name + ".lab-reduction.tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)

def replace_block(text, marker, body):
    start, end = "<!-- " + marker + "_START -->", "<!-- " + marker + "_END -->"
    block = start + "\n" + body.strip() + "\n" + end
    pattern = re.escape(start) + r".*?" + re.escape(end)
    if start in text and end in text:
        return re.sub(pattern, lambda _: block, text, count=1, flags=re.S)
    return text.rstrip() + "\n\n" + block + "\n"

def publish_block(root, marker, body):
    p = root / "latest_report.md"
    if p.exists():
        atomic_text(p, replace_block(p.read_text(encoding="utf-8"), marker, body))

def paused_notice(key, root=Path("reports")):
    if key not in PAUSED:
        return False
    root = Path(root)
    marker, title, filename = PAUSED[key]
    body = ("# " + title + "\n\n"
        "**SOSPESO dal 13 ottobre 2026.** Nessun nuovo calcolo o segnale.\n\n"
        "Storico e ultime metriche conservati come archivio, non come dati correnti.\n"
        "Gli input archiviati non contribuiscono a Global Confluence.\n")
    atomic_text(root / filename, "<!-- " + marker + "_START -->\n" + body + "<!-- " + marker + "_END -->\n")
    publish_block(root, marker, body)
    print("LAB_MODULE_SUSPENDED=" + key)
    return True

def quarantine_risk(root=Path("reports")):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    path = root / "risk_calibration_metrics.csv"
    fields = []
    if path.exists():
        with path.open() as f:
            fields = list(csv.DictReader(f).fieldnames or [])
    fields = list(dict.fromkeys(fields + ["asset", "calibration_stage", "stage_note",
        "can_influence_decision", "can_strongly_influence_decision", "quality_status"]))
    import io
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fields)
    writer.writeheader()
    for asset in ("BTC", "SOL", "DOGE"):
        writer.writerow({"asset": asset, "calibration_stage": "QUARANTINED",
            "stage_note": "INVALID_PRICE_PARSING_LEGACY_LOG_PRESERVED",
            "can_influence_decision": False, "can_strongly_influence_decision": False,
            "quality_status": "INVALID_NOT_FOR_DECISIONS"})
    atomic_text(path, buf.getvalue())
    body = ("# Calibrazione del rischio sospesa\n\n"
        "**QUARANTENA: errore nella lettura dei prezzi dal testo.**\n\n"
        "Le vecchie statistiche non misurano affidabilmente il rischio e non vengono utilizzate. "
        "Il diario originale e le metriche precedenti sono conservati per audit. "
        "Nessuna correzione retroattiva, nessun nuovo snapshot di rischio.\n")
    atomic_text(root / "risk_calibration_report.md", body)
    publish_block(root, "RISK_CALIBRATION", body)
    print("RISK_CALIBRATION=QUARANTINED")

def archive_once(root):
    archive = root / "lab_reduction_archive_20261013"
    manifest = archive / "manifest.json"
    if manifest.exists():
        return
    import shutil
    archive.mkdir(parents=True, exist_ok=True)
    prefixes = ("btc_2022_vs_sol_2026_", "fractal_path_", "rsi_top_cycle_",
                "sol_onchain_metrics_", "extreme_cases_path_", "risk_calibration_")
    copied = {}
    for p in sorted(root.iterdir()):
        if p.is_file() and p.name.startswith(prefixes):
            shutil.copy2(p, archive / p.name)
            copied[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    immutable = {k: v for k, v in copied.items()
        if k not in {x[2] for x in PAUSED.values()}
        and k not in {"risk_calibration_metrics.csv", "risk_calibration_report.md"}}
    atomic_text(manifest, json.dumps({"policy": POLICY_VERSION, "archived_sha256": copied,
        "frozen_source_sha256": immutable}, indent=2) + "\n")

def verify_frozen(root):
    p = root / "lab_reduction_archive_20261013/manifest.json"
    if not p.exists():
        raise RuntimeError("LAB_RETIREMENT_ARCHIVE_MISSING")
    d = json.loads(p.read_text())
    for name, digest in d["frozen_source_sha256"].items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError("SUSPENDED_ARTIFACT_CHANGED:" + name)

def read_csv(path):
    if not path.exists():
        return []
    with path.open() as f:
        return list(csv.DictReader(f))

def validation_summary(root, today=None):
    today = today or datetime.now(timezone.utc).date()
    groups = {}
    rows = read_csv(root / "market_forecast_lab/evaluation_latest.csv")
    for r in rows:
        if r.get("official_daily", "").lower() != "true" or r.get("horizon") != "7":
            continue
        # forecast_id is defined by the Lab schema as lab:mode:asset:YYYY-MM-DD:hash.
        parts = r.get("forecast_id", "").split(":")
        if len(parts) != 5:
            continue
        emitted = parts[3]
        if not VALIDATION_START <= emitted < REVIEW_DATE:
            continue
        # Evaluate only complete UTC target days, and fail on duplicate observations.
        if r["target_date"] >= today.isoformat():
            continue
        key = (r["forecast_id"], r["horizon"])
        if key in groups:
            raise RuntimeError("DUPLICATE_VALIDATION_OBSERVATION")
        e, base = float(r["p50_error_absolute"]), abs(float(r["actual_return"]))
        if not all(math.isfinite(x) for x in (e, base)):
            continue
        groups[key] = (emitted, r["coingecko_id"], e, base)
    weeks = {}
    for emitted, asset, err, base in groups.values():
        d = date.fromisoformat(emitted)
        bucket = (d - date.fromisoformat(VALIDATION_START)).days // 7
        weeks.setdefault(bucket, {}).setdefault(asset, []).append((err, base))
    # Equal weight per asset within a week, and equal weight per completed 7-day bucket.
    scores = []
    for bucket, assets in sorted(weeks.items()):
        from datetime import timedelta
        end = date.fromisoformat(VALIDATION_START) + timedelta(days=bucket * 7 + 13)
        if today <= end:
            continue
        pairs = [(statistics.mean(v[0] for v in vals), statistics.mean(v[1] for v in vals))
                 for vals in assets.values()]
        if len(pairs) >= 30:
            scores.append({"bucket": bucket, "assets": len(pairs),
                "model_mae_pct": statistics.mean(v[0] for v in pairs),
                "baseline_mae_pct": statistics.mean(v[1] for v in pairs)})
    good = [x for x in scores if x["model_mae_pct"] < x["baseline_mae_pct"]]
    improvement = None
    if scores:
        base = statistics.mean(x["baseline_mae_pct"] for x in scores)
        if base > 0:
            improvement = 100 * (1 - statistics.mean(x["model_mae_pct"] for x in scores) / base)
    enough = len(scores) >= 3
    status = "COLLECTING_FIXED_VALIDATION"
    if today.isoformat() >= REVIEW_DATE:
        status = ("REVIEW_REQUIRED_PROMISING_NOT_PROVEN" if enough and improvement is not None
            and improvement >= 5 and len(good) >= 2 else "REVIEW_REQUIRED_PAUSE_EXPANSION")
    return {"validation_start": VALIDATION_START, "review_date": REVIEW_DATE,
        "primary_horizon_days": 7, "baseline": "UNCHANGED_ANCHOR_PRICE",
        "eligible_observations": len(groups), "complete_week_buckets": scores,
        "mae_improvement_pct": improvement, "status": status,
        "minimum_complete_weeks": 3, "minimum_assets_per_week": 30,
        "minimum_improvement_pct": 5, "minimum_winning_weeks": 2,
        "automatic_promotion": False, "automatic_trading": False,
        "note": "Exploratory continuation gate; correlated assets/weeks, no statistical certification. No automatic stop; explicit review required."}

def finalize(root=Path("reports")):
    root = Path(root)
    verify_frozen(root)
    status = {"policy": POLICY_VERSION, "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "risk": "QUARANTINED", "paused_modules": list(PAUSED),
        "development_frozen": ["BTC_30D", "DOGE_30D", "SECONDARY_FRACTALS"],
        "retained": ["BTC_SOL_DOGE_FORECASTS_AND_EVALUATIONS", "SOL_7D_PRIORITY",
                     "TOP50_FIXED_VALIDATION", "DATA_COLLECTION", "BACKUP"],
        "top50_validation": validation_summary(root)}
    atomic_text(root / "lab_reduction_status.json", json.dumps(status, indent=2) + "\n")
    body = ("# Laboratorio ridotto — 13 ottobre 2026\n\n"
        "**Solo diagnostica: nessuna affidabilità operativa certificata.**\n\n"
        "Calibrazione rischio in quarantena; frattale BTC→SOL, tracking frattale, RSI top-cycle, "
        "on-chain SOL e percorsi estremi sospesi. Storici conservati.\n\n"
        "Coni BTC/SOL/DOGE e valutazioni continuano; priorità di analisi SOL a 7 giorni. "
        "Nessun nuovo sviluppo BTC/DOGE a 30 giorni.\n\n"
        "Top50: verifica separata sulle previsioni dal 14 ottobre, confronto con prezzo invariato a 7 giorni. "
        "Revisione entro il 13 novembre 2026: almeno 3 settimane complete con 30 asset ciascuna, "
        "riduzione errore almeno 5% e vantaggio in almeno 2 settimane. "
        "Criterio esplorativo, nessuna promozione automatica; se manca, proposta di sospensione dell'espansione.\n\n"
        "Stato verifica: **" + status["top50_validation"]["status"] + "**.\n")
    atomic_text(root / "lab_reduction_status.md", body)
    p = root / "latest_report.md"
    if p.exists():
        txt = replace_block(p.read_text(), "LAB_REDUCTION", body)
        start = txt.index("<!-- LAB_REDUCTION_START -->")
        end = txt.index("<!-- LAB_REDUCTION_END -->", start) + len("<!-- LAB_REDUCTION_END -->")
        block = txt[start:end]
        atomic_text(p, block + "\n\n" + (txt[:start] + txt[end:]).strip() + "\n")
    print("LAB_REDUCTION_VALIDATION=PASS")

if __name__ == "__main__":
    import sys
    root = Path("reports")
    if "--initialize" in sys.argv:
        archive_once(root)
        quarantine_risk(root)
        for key in PAUSED:
            paused_notice(key, root)
    finalize(root)
