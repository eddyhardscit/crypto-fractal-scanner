"""Point-in-time, append-only provenance primitives for forecast artifacts."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
import uuid
import fcntl
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent
ROOT = Path(os.getenv("SCANNER_FORECAST_PROVENANCE_DIR", REPO_ROOT / "reports" / "forecast_provenance")).resolve()
RAW_DIR = ROOT / "raw_ohlc"
COHORT_DIR = ROOT / "cohorts"
RAW_INDEX = ROOT / "raw_market_snapshots.jsonl"
FORECAST_LOG = ROOT / "forecast_versions.jsonl"
EVALUATION_LOG = ROOT / "evaluation_versions.jsonl"
LATEST_DAILY = ROOT / "forecast_latest_daily.csv"
LEGACY_TRACKER_BASELINE = ROOT / "legacy_tracker_aggregate_baseline.json"
LEGACY_SHADOW_BASELINE = ROOT / "legacy_shadow_aggregate_baseline.json"
SCHEMA_VERSION = 1


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def source_worktree_dirty() -> bool:
    """Report whether tracked/untracked source or config differs from HEAD.

    Runtime products under reports/ are deliberately excluded: they are
    expected to change before provenance records are emitted by a daily run.
    """
    try:
        git = ["git", "-c", f"safe.directory={REPO_ROOT}", "-C", str(REPO_ROOT)]
        status = subprocess.check_output([
            *git, "status", "--porcelain", "--untracked-files=all", "--", ".",
            ":(exclude)reports/**", ":(exclude)**/__pycache__/**",
            ":(exclude)**/*.pyc",
        ], text=True, stderr=subprocess.DEVNULL)
        return bool(status.strip())
    except Exception:
        return True


def code_version() -> str:
    """Return the exact source commit; dirtiness is a separate provenance fact."""
    try:
        git = ["git", "-c", f"safe.directory={REPO_ROOT}", "-C", str(REPO_ROOT)]
        return subprocess.check_output(
            [*git, "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "UNKNOWN"


def code_provenance() -> dict:
    return {
        "code_version": code_version(),
        "source_worktree_dirty": source_worktree_dirty(),
    }


def new_run_id(generated_at_utc: str) -> str:
    return f"run-{generated_at_utc.replace(':', '').replace(' ', 'T')}-{uuid.uuid4().hex[:12]}"


def _json_default(value):
    try:
        if pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass
    if isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "isoformat"):
        return value.isoformat()
    if hasattr(value, "item"):
        return value.item()
    return str(value)


def _json_clean(value):
    if isinstance(value, dict):
        return {str(key): _json_clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_clean(item) for item in value]
    try:
        if pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass
    return _json_default(value)


def canonical_json(value) -> bytes:
    return (json.dumps(_json_clean(value), sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def _write_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise OSError("short write while persisting provenance")
        view = view[written:]


def _fsync_directory(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _atomic_write(path: Path, payload: bytes, *, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp = Path(temp_name)
    try:
        os.fchmod(fd, mode); _write_all(fd, payload); os.fsync(fd)
        os.close(fd); fd = -1
        os.replace(temp, path); _fsync_directory(path.parent)
    finally:
        if fd >= 0:
            os.close(fd)
        temp.unlink(missing_ok=True)


def _install_content_addressed(path: Path, payload: bytes, digest: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_fd = os.open(path.parent / ".content-store.lock", os.O_RDWR | os.O_CREAT, 0o644)
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX)
        if path.exists():
            existing = path.read_bytes()
            if existing != payload or hashlib.sha256(existing).hexdigest() != digest:
                raise RuntimeError(f"CONTENT_ADDRESS_COLLISION:{digest}")
            return
        fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        temp = Path(temp_name)
        try:
            _write_all(fd, payload); os.fsync(fd); os.close(fd); fd = -1
            os.replace(temp, path)
            path.chmod(0o444); _fsync_directory(path.parent)
        finally:
            if fd >= 0:
                os.close(fd)
            temp.unlink(missing_ok=True)
    finally:
        fcntl.flock(lock_fd, fcntl.LOCK_UN)
        os.close(lock_fd)


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        _write_all(fd, canonical_json(record)); os.fsync(fd)
    finally:
        os.close(fd)


def append_jsonl_once(path: Path, record: dict, key_fields: tuple[str, ...]) -> bool:
    wanted = tuple(str(record.get(field, "")) for field in key_fields)
    for existing in _read_jsonl(path):
        if tuple(str(existing.get(field, "")) for field in key_fields) == wanted:
            # Volatile acquisition metadata may differ for the same content snapshot.
            return False
    append_jsonl(path, record)
    return True


def append_csv_atomic(path: Path | str, rows: pd.DataFrame) -> None:
    """Append rows semantically while publishing a complete CSV atomically."""
    target = Path(path)
    old = pd.read_csv(target) if target.exists() else pd.DataFrame()
    combined = rows.copy() if old.empty else pd.concat([old, rows], ignore_index=True, sort=False)
    _atomic_write(target, combined.to_csv(index=False, lineterminator="\n").encode("utf-8"))


def append_csv_idempotent_atomic(path: Path | str, rows: pd.DataFrame,
                                 *, key: str, hash_field: str) -> None:
    """Atomically append unique immutable CSV records, hard-failing on key reuse."""
    target = Path(path)
    old = pd.read_csv(target, dtype=str, keep_default_na=False) if target.exists() else pd.DataFrame()
    incoming = rows.copy()
    if not old.empty and key in old.columns:
        hashes = dict(zip(old[key].astype(str), old.get(hash_field, pd.Series("", index=old.index)).astype(str)))
        keep = []
        for _, row in incoming.iterrows():
            record_key = str(row[key]); record_hash = str(row[hash_field])
            if record_key not in hashes:
                keep.append(True)
            elif hashes[record_key] == record_hash:
                keep.append(False)
            else:
                raise RuntimeError(f"IMMUTABLE_CSV_KEY_COLLISION:{record_key}")
        incoming = incoming.loc[keep]
    if incoming.empty:
        return
    combined = incoming if old.empty else pd.concat([old, incoming], ignore_index=True, sort=False)
    _atomic_write(target, combined.to_csv(index=False, lineterminator="\n").encode("utf-8"))


def freeze_legacy_aggregate_baseline(metrics_path: Path | str, baseline_path: Path,
                                     *, kind: str, rows: list[dict]) -> dict:
    """Freeze aggregate-only legacy evidence; never manufactures row provenance."""
    source = Path(metrics_path)
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    body = {
        "schema_version": SCHEMA_VERSION,
        "provenance_type": "LEGACY_AGGREGATE_BASELINE",
        "raw_point_in_time_replay_available": "NO",
        "aggregate_kind": kind,
        "source_path": str(source),
        "source_sha256": source_hash,
        "rows": rows,
    }
    digest = hashlib.sha256(canonical_json(body)).hexdigest()
    manifest = {**body, "manifest_sha256": digest}
    if baseline_path.exists():
        existing = json.loads(baseline_path.read_text(encoding="utf-8"))
        check = dict(existing); expected = check.pop("manifest_sha256", None)
        if expected != hashlib.sha256(canonical_json(check)).hexdigest():
            raise RuntimeError("LEGACY_AGGREGATE_BASELINE_INTEGRITY_ERROR")
        return existing
    _atomic_write(baseline_path, canonical_json(manifest), mode=0o444)
    return manifest


def _canonical_ohlc(frame: pd.DataFrame) -> bytes:
    wanted = [c for c in ["Open", "High", "Low", "Close", "Adj Close", "Volume"] if c in frame]
    out = frame[wanted].copy()
    idx = pd.DatetimeIndex(out.index)
    idx = idx.tz_convert("UTC") if idx.tz is not None else idx.tz_localize("UTC")
    out.insert(0, "timestamp_utc", idx.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
    out = out.sort_values("timestamp_utc").drop_duplicates("timestamp_utc", keep="last")
    return out.to_csv(index=False, lineterminator="\n", float_format="%.17g").encode("utf-8")


def freeze_ohlc(frame: pd.DataFrame, *, ticker: str, source: str,
                downloaded_at_utc: str, requested_interval: str,
                requested_range: str, run_id: str, purpose: str) -> str:
    payload = _canonical_ohlc(frame)
    digest = hashlib.sha256(payload).hexdigest(); snapshot_id = f"sha256:{digest}"
    target = RAW_DIR / f"{digest}.csv"
    _install_content_addressed(target, payload, digest)
    record = {
        "schema_version": SCHEMA_VERSION, "snapshot_id": snapshot_id, "sha256": digest,
        "source": source, "ticker": ticker, "downloaded_at_utc": downloaded_at_utc,
        "requested_interval": requested_interval, "requested_range": requested_range,
        "timezone": "UTC", "run_id": run_id, "purpose": purpose,
        "row_count": len(frame), "dataset_path": str(target),
    }
    append_jsonl_once(RAW_INDEX, record, ("snapshot_id",))
    return snapshot_id


def load_frozen_ohlc(snapshot_id: str) -> pd.DataFrame:
    if not snapshot_id or not str(snapshot_id).startswith("sha256:"):
        raise RuntimeError("HISTORICAL_RAW_DATA_NOT_FROZEN")
    digest = str(snapshot_id).split(":", 1)[1]; path = RAW_DIR / f"{digest}.csv"
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError("HISTORICAL_RAW_DATA_NOT_FROZEN")
    out = pd.read_csv(path)
    out.index = pd.to_datetime(out.pop("timestamp_utc"), utc=True).dt.tz_convert(None)
    return out


def freeze_cohort(matches: pd.DataFrame, *, target: str, run_id: str,
                  generated_at_utc: str) -> tuple[str, str]:
    rows = []
    for rank, (_, row) in enumerate(matches.reset_index(drop=True).iterrows(), 1):
        item = {k: _json_default(v) for k, v in row.to_dict().items()}; item["rank"] = rank; rows.append(item)
    body = {"schema_version": SCHEMA_VERSION, "target": target, "cases_used": len(rows), "matches": rows}
    digest = hashlib.sha256(canonical_json(body)).hexdigest(); cohort_id = f"sha256:{digest}"
    manifest = {**body, "cohort_id": cohort_id, "manifest_sha256": digest,
                "run_id": run_id, "generated_at_utc": generated_at_utc,
                **code_provenance()}
    payload = canonical_json(manifest)
    path = COHORT_DIR / f"{digest}.json"
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        existing_body = {key: existing[key] for key in ("schema_version", "target", "cases_used", "matches")}
        if hashlib.sha256(canonical_json(existing_body)).hexdigest() != digest:
            raise RuntimeError(f"CONTENT_ADDRESS_COLLISION:{digest}")
    else:
        # The filename addresses the deterministic cohort body. Run metadata is
        # immutable metadata of the first materialization and is never rewritten.
        _atomic_write(path, payload, mode=0o444)
    return cohort_id, digest


def canonical_forecast_date(record: dict) -> str:
    value = record.get("forecast_date", record.get("prediction_date"))
    if value is None or not str(value).strip():
        raise ValueError("FORECAST_DATE_REQUIRED")
    return pd.to_datetime(value, errors="raise").date().isoformat()


def append_forecast(record: dict) -> None:
    immutable = {"schema_version": SCHEMA_VERSION, **record}
    immutable["forecast_date"] = canonical_forecast_date(immutable)
    immutable.setdefault("prediction_date", immutable["forecast_date"])
    immutable.pop("official_daily", None)
    immutable["official_daily_candidate"] = True
    append_jsonl(FORECAST_LOG, immutable)
    frame = pd.DataFrame(_read_jsonl(FORECAST_LOG))
    latest = (frame.sort_values(["generated_at_utc", "forecast_id"], kind="stable")
              .drop_duplicates(["forecast_date", "asset"], keep="last"))
    latest["official_daily"] = True
    _atomic_write(LATEST_DAILY, latest.to_csv(index=False, lineterminator="\n").encode("utf-8"))


EVALUATION_REQUIRED = {
    "forecast_id", "asset", "forecast_generated_at_utc", "forecast_date", "horizon_days",
    "requested_target_date", "actual_candle_date", "on_or_after_shift_days", "actual_close",
    "raw_market_snapshot_id", "raw_market_snapshot_sha256", "p10", "p25", "p50", "p75", "p90",
    "inside_p10_p90", "inside_p25_p75", "direction_forecast", "direction_result", "drawdown",
    "max_gain", "drawdown_classifications", "max_gain_classifications",
    "evaluation_generated_at_utc", "code_version", "path_price_semantics",
}


def evaluation_key(record: dict) -> tuple[str, str, str]:
    return (str(record.get("forecast_id", "")), str(record.get("horizon_days", "")), str(record.get("requested_target_date", "")))


def _validated_evaluation(record: dict) -> dict:
    missing = sorted(EVALUATION_REQUIRED - set(record))
    if missing:
        raise ValueError("EVALUATION_MANIFEST_MISSING:" + ",".join(missing))
    body = {"schema_version": SCHEMA_VERSION, **record}; body.pop("evaluation_manifest_sha256", None)
    return {**body, "evaluation_manifest_sha256": hashlib.sha256(canonical_json(body)).hexdigest()}


def find_evaluation(forecast_id: str, horizon_days, requested_target_date: str) -> dict | None:
    key = (str(forecast_id), str(horizon_days), str(requested_target_date))
    for record in _read_jsonl(EVALUATION_LOG):
        if evaluation_key(record) != key:
            continue
        expected = record.get("evaluation_manifest_sha256"); body = dict(record); body.pop("evaluation_manifest_sha256", None)
        if not expected or hashlib.sha256(canonical_json(body)).hexdigest() != expected:
            raise RuntimeError("EVALUATION_MANIFEST_INTEGRITY_ERROR")
        snapshot_id = str(record.get("raw_market_snapshot_id", ""))
        if snapshot_id != f"sha256:{record.get('raw_market_snapshot_sha256', '')}":
            raise RuntimeError("EVALUATION_RAW_SNAPSHOT_HASH_MISMATCH")
        load_frozen_ohlc(snapshot_id)
        return record
    return None


def append_evaluation(record: dict) -> dict:
    candidate = _validated_evaluation(record); existing = find_evaluation(*evaluation_key(candidate))
    if existing is not None:
        left = dict(existing); right = dict(candidate)
        for item in (left, right):
            item.pop("evaluation_manifest_sha256", None); item.pop("evaluation_generated_at_utc", None); item.pop("code_version", None)
            item.pop("source_worktree_dirty", None)
        if canonical_json(left) != canonical_json(right):
            raise RuntimeError("EVALUATION_KEY_COLLISION")
        return existing
    append_jsonl(EVALUATION_LOG, candidate)
    return candidate
