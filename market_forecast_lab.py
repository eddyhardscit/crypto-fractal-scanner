#!/usr/bin/env python3
"""Artifact-only Forecast Lab entrypoint. Never invokes scanner.main or trading code."""
from __future__ import annotations

import argparse
import contextlib
import fcntl
import hashlib
import json
import os
from pathlib import Path
import resource
import re
import sys
import time

import pandas as pd
import yfinance as yf

import forecast_provenance as fp
import scanner as legacy
from market_forecast_lab_engine import (
    LEGACY_IDS, SharedSignatureIndex, build_forecast, digest, evaluate,
    load_legacy_inputs, read_jsonl, rotation, verify_canonical,
)
from market_forecast_lab_universe import (
    CONFIG_PATH, REGISTRY_PATH, fetch_markets, load_config, load_registry, select_universe,
)

ROOT = Path(__file__).resolve().parent


def event(phase, **fields):
    print(json.dumps(dict(phase=phase, **fields)), flush=True)


def configure_store(root):
    """Point the existing provenance module at its existing volume; no new raw store."""
    fp.ROOT = Path(root).resolve()
    fp.RAW_DIR = fp.ROOT / 'raw_ohlc'
    fp.RAW_INDEX = fp.ROOT / 'raw_market_snapshots.jsonl'
    fp.COHORT_DIR = fp.ROOT / 'cohorts'
    if not fp.RAW_INDEX.is_file() or not fp.RAW_DIR.is_dir():
        raise ValueError('EXISTING_PROVENANCE_STORE_REQUIRED')


def source_hashes():
    names = ['market_forecast_lab.py', 'market_forecast_lab_engine.py',
             'market_forecast_lab_universe.py', 'market_forecast_lab_config.json',
             'market_forecast_lab_registry.json', 'scanner.py', 'forecast_provenance.py']
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names}


def store_input(output, manifest):
    checksum = digest(manifest)
    fp._install_content_addressed(output / 'inputs' / (checksum + '.json'),
                                 fp.canonical_json(manifest), checksum)
    return 'sha256:' + checksum


def immutable_append(path, rows, keys):
    """Caller holds the Lab-wide exclusive lock. Reused keys must be byte-identical."""
    existing = {tuple(r[k] for k in keys): r for r in read_jsonl(path)}
    additions = []
    for row in rows:
        key = tuple(row[k] for k in keys)
        if key in existing:
            if digest(existing[key]) != digest(row):
                raise ValueError('IMMUTABLE_VINTAGE_CONFLICT:' + str(key))
        else:
            additions.append(row)
            existing[key] = row
    if additions:
        # Atomic whole-file replacement avoids truncated last records after interruption.
        fp._atomic_write(path, b''.join(fp.canonical_json(r) for r in existing.values()))
    elif not path.exists():
        fp._atomic_write(path, b'')


def write_csv(path, rows, columns):
    # Nested cells contain strict JSON, never Python repr; null is the N/A marker.
    flat = [{k: fp.canonical_json(v).decode().strip() if isinstance(v, (dict, list)) else v
             for k, v in row.items()} for row in rows]
    frame = pd.DataFrame(flat) if flat else pd.DataFrame(columns=columns)
    fp._atomic_write(path, frame.to_csv(index=False, lineterminator='\n').encode())


def directory_bytes(root):
    return sum(p.stat().st_size for p in root.rglob('*') if p.is_file())


def acquire_extra(registry, markets, raw, processed, snapshot_ids, old, as_of):
    """Only explicitly mapped targets and outstanding vintages; no microcap discovery."""
    ids = {r['id'] for r in markets['rows']}
    needed = {r['ohlc_ticker'] for cid, r in registry.items()
              if cid in ids and r['target_enabled'] and r.get('ohlc_ticker')}
    needed |= {f['ohlc_ticker'] for f in old
               if (pd.Timestamp(as_of) - pd.Timestamp(f['anchor_date'])).days <= 62}
    # Exited assets with older *unresolved* evaluations must also remain trackable.
    needed |= {f['ohlc_ticker'] for f in old}
    errors, identities = {}, {}
    markets_by_id = {r['id']: r for r in markets['rows']}
    by_ticker = {r['ohlc_ticker']: (cid, r) for cid, r in registry.items() if r.get('ohlc_ticker')}
    for ticker in sorted(needed - set(raw)):
        try:
            cid, entry = by_ticker[ticker]
            metadata = yf.Ticker(ticker).get_history_metadata()
            normal = lambda value: re.sub(r'[^a-z0-9]', '', str(value).lower().removesuffix(' usd'))
            expected = entry.get('ohlc_name_aliases', []) + [markets_by_id.get(cid, {}).get('name', cid)]
            if (metadata.get('symbol') != ticker or metadata.get('currency') != 'USD'
                    or metadata.get('instrumentType') != 'CRYPTOCURRENCY'
                    or not any(normal(metadata.get('longName')) == normal(name) or
                               normal(metadata.get('shortName')) == normal(name) for name in expected)):
                raise ValueError('OHLC_IDENTITY_NOT_VERIFIED')
            identities[ticker] = {k: metadata.get(k) for k in ('symbol', 'currency', 'instrumentType', 'shortName', 'longName')}
            frame = yf.download(ticker, period='10y', interval='1d', auto_adjust=True,
                                progress=False, threads=False)
            if isinstance(frame.columns, pd.MultiIndex):
                frame = frame.xs(ticker, axis=1, level=1)
            frame = frame.dropna()
            frame.index = pd.DatetimeIndex(frame.index).tz_localize(None)
            frame = frame.loc[:as_of]
            if frame.empty:
                raise ValueError('EMPTY_OHLC')
            sid = fp.freeze_ohlc(frame, ticker=ticker, source='Yahoo Finance/yfinance',
                                 downloaded_at_utc=fp.utc_now(), requested_interval='1d',
                                 requested_range='period=10y', run_id='market-lab:' + as_of,
                                 purpose='market_forecast_lab_generation_and_evaluation')
            # Always compute from reloaded bytes: live acquisition and replay share precision.
            raw[ticker] = fp.load_frozen_ohlc(sid)
            processed[ticker] = legacy.add_indicators(raw[ticker])
            snapshot_ids[ticker] = sid
        except Exception as exc:
            errors[ticker] = type(exc).__name__ + ':' + str(exc)
    return errors, identities


def forecasts_from_manifest(manifest, manifest_id, index=None, existing=()):
    raw = {ticker: fp.load_frozen_ohlc(sid) for ticker, sid in manifest['raw_snapshot_ids'].items()}
    processed = {ticker: legacy.add_indicators(frame) for ticker, frame in raw.items()}
    library = {ticker: processed[ticker] for ticker in manifest['library_order']}
    if index is None:
        index = SharedSignatureIndex(library)
    saved = {(f['coingecko_id'], f['forecast_date']): f for f in existing}
    forecasts = []
    for member in manifest['universe']:
        if member['inclusion_status'] != 'INCLUDED':
            continue
        cid, ticker = member['coingecko_id'], member['ohlc_ticker']
        key = (cid, manifest['as_of'])
        if key in saved:
            forecasts.append(saved[key])
            continue
        canonical = manifest['canonical'].get(ticker)
        if canonical:
            cohort = canonical['cohort']
            anchor, anchor_date = canonical['current_price'], canonical['anchor_date']
        else:
            _, clean = index.match(ticker, processed[ticker])
            cohort = clean.to_dict('records')
            for rank, row in enumerate(cohort, 1):
                row['rank'] = rank
                row['start_date'] = str(row['start_date'])
                row['end_date'] = str(row['end_date'])
            anchor = float(raw[ticker].Close.iloc[-1])
            anchor_date = raw[ticker].index[-1].date().isoformat()
        forecasts.append(build_forecast(cid, ticker, cohort, library, anchor, anchor_date,
                                        manifest['as_of'], manifest_id, manifest['config'],
                                        manifest['quality_evaluations'], canonical, member.get('data_quality', 'GOOD')))
        event('forecast', asset=cid, N=forecasts[-1]['N'], status=forecasts[-1]['status'])
    return forecasts, index


def export(output, universe_record, forecasts, old, evaluations, config, run_report):
    immutable_append(output / 'universe_history.jsonl', [universe_record], ('snapshot_date',))
    immutable_append(output / 'forecast_vintages.jsonl', forecasts, ('coingecko_id', 'forecast_date'))
    versions = [dict(forecast_id=f['forecast_id'], coingecko_id=f['coingecko_id'],
                     forecast_date=f['forecast_date'], paths=f['paths']) for f in forecasts]
    immutable_append(output / 'forecast_path_versions.jsonl', versions, ('forecast_id',))
    # Preserve first completed actual observation; never silently revise an evaluation.
    old_evaluations = read_jsonl(output / 'evaluation_versions.jsonl')
    done = {(e['forecast_id'], e['horizon']) for e in old_evaluations}
    new_evaluations = [e for e in evaluations if (e['forecast_id'], e['horizon']) not in done]
    immutable_append(output / 'evaluation_versions.jsonl', new_evaluations, ('forecast_id', 'horizon'))
    all_evaluations = old_evaluations + new_evaluations
    rotation_rows = rotation(forecasts, old, config)
    forecast_rows = []
    for f in forecasts:
        for headline in f['headlines']:
            forecast_rows.append(dict(forecast_id=f['forecast_id'], coingecko_id=f['coingecko_id'],
                                      forecast_date=f['forecast_date'], anchor_price=f['anchor_price'],
                                      anchor_date=f['anchor_date'], status=f['status'],
                                      input_manifest_id=f['input_manifest_id'], **headline))
    write_csv(output / 'universe_latest.csv', universe_record['rows'], ['coingecko_id', 'inclusion_status'])
    write_csv(output / 'forecast_latest.csv', forecast_rows, ['forecast_id', 'coingecko_id', 'horizon', 'status'])
    write_csv(output / 'rotation_latest.csv', rotation_rows, ['coingecko_id', 'horizon', 'states'])
    write_csv(output / 'evaluation_latest.csv', all_evaluations, ['forecast_id', 'coingecko_id', 'horizon', 'actual_close'])
    fp._atomic_write(output / 'forecast_paths_latest.json', fp.canonical_json(versions))
    artifacts = ['universe_latest.csv', 'forecast_latest.csv', 'forecast_paths_latest.json',
                 'rotation_latest.csv', 'evaluation_latest.csv']
    latest = dict(schema_version=1, status='COMPLETE', forecast_date=universe_record['snapshot_date'],
                  run=run_report, forecasts=forecasts, rotation=rotation_rows,
                  artifacts={name: hashlib.sha256((output / name).read_bytes()).hexdigest() for name in artifacts})
    # Commit marker last: consumers must verify these checksums before reading latest CSVs.
    fp._atomic_write(output / 'latest.json', fp.canonical_json(latest))


def execute(args):
    started, cpu_started = time.perf_counter(), time.process_time()
    reports, output = Path(args.legacy_reports).resolve(), Path(args.output).resolve()
    configure_store(args.provenance_root or reports / 'forecast_provenance')
    if output.name != 'market_forecast_lab' or output == reports or reports.is_relative_to(output) or output.is_relative_to(fp.ROOT):
        raise ValueError('UNSAFE_OUTPUT_DIRECTORY')
    output.mkdir(parents=True, exist_ok=True)
    yf.set_tz_cache_location(str(output / '.yfinance-cache'))
    if output.stat().st_dev != fp.ROOT.stat().st_dev:
        raise ValueError('OUTPUT_MUST_USE_PROVENANCE_VOLUME')
    with (output / '.run.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        before = directory_bytes(output) + directory_bytes(fp.ROOT)
        config, registry = load_config(), load_registry()
        raw, processed, snapshot_ids, canonical = load_legacy_inputs(reports, args.as_of)
        event('canonical_loaded', targets=list(canonical), raw_assets=len(raw))
        library_order = [t for t in legacy.CRYPTO_TICKERS if t in processed
                         and any(r.get('ohlc_ticker') == t and r['analogue_enabled'] for r in registry.values())]
        old = read_jsonl(output / 'forecast_vintages.jsonl')
        prior_universe = [r for r in read_jsonl(output / 'universe_history.jsonl') if r['snapshot_date'] == args.as_of]
        if prior_universe:
            previous_id = prior_universe[0]['input_manifest_id'].split(':')[1]
            previous = json.loads((output / 'inputs' / (previous_id + '.json')).read_text())
            markets = previous['markets']
        elif args.markets:
            markets = json.loads(Path(args.markets).read_text())
            if not isinstance(markets, dict) or not {'generated_at', 'rows'}.issubset(markets):
                raise ValueError('MARKET_SNAPSHOT_TIMESTAMP_REQUIRED')
        else:
            markets = fetch_markets(config)
        errors, identities = acquire_extra(registry, markets, raw, processed, snapshot_ids, old, args.as_of)
        event('inputs_ready', raw_assets=len(raw), unavailable=errors)
        universe = (prior_universe[0]['rows'] if prior_universe else
                    select_universe(markets, registry, processed, args.as_of, config, errors))
        evaluations = evaluate(old, raw, snapshot_ids, args.as_of)
        # Mature quality uses immutable observations only; not yet-mature values remain null.
        prior_evaluations = read_jsonl(output / 'evaluation_versions.jsonl')
        done = {(e['forecast_id'], e['horizon']) for e in prior_evaluations}
        quality_evaluations = prior_evaluations + [e for e in evaluations if (e['forecast_id'], e['horizon']) not in done]
        manifest = dict(schema_version=1, as_of=args.as_of, config=config, registry=registry,
                        markets=markets, universe=universe, library_order=library_order,
                        raw_snapshot_ids=snapshot_ids, canonical=canonical,
                        quality_evaluations=quality_evaluations, source_hashes=source_hashes(),
                        code_provenance=fp.code_provenance(), acquisition_errors=errors, ohlc_identity_evidence=identities)
        if prior_universe:
            if previous['source_hashes'] != source_hashes():
                raise ValueError('DAILY_SOURCE_CHANGED_REPLAY_ORIGINAL_VERSION')
            manifest = previous
        manifest_id = store_input(output, manifest)
        event('index_build_started', library_assets=len(library_order))
        frozen_library = {t: legacy.add_indicators(fp.load_frozen_ohlc(manifest['raw_snapshot_ids'][t]))
                          for t in manifest['library_order']}
        index = SharedSignatureIndex(frozen_library)
        event('index_ready', episodes=len(index.episodes), signature_bytes=index.signature_bytes)
        forecasts, _ = forecasts_from_manifest(manifest, manifest_id, index, old)
        parity = {}
        for ticker, record in canonical.items():
            # Verify canonical adapters even if a canonical target is outside Top50.
            f = next((f for f in forecasts if f['ohlc_ticker'] == ticker), None)
            if f is None:
                f = build_forecast(LEGACY_IDS[ticker], ticker, record['cohort'], processed,
                                   record['current_price'], record['anchor_date'], args.as_of,
                                   manifest_id, config, canonical=record)
            parity[ticker] = verify_canonical(f, record, reports)
        report = dict(as_of=args.as_of, published=False, input_manifest_id=manifest_id,
                      universe_complete=sum(r['inclusion_status'] == 'INCLUDED' for r in universe) == config['universe_size'],
                      target_count=sum(r['inclusion_status'] == 'INCLUDED' for r in universe),
                      valid_count=sum(f['status'] == 'VALID' for f in forecasts),
                      insufficient_count=sum(f['status'] == 'INSUFFICIENT_ANALOGUES' for f in forecasts),
                      signature_index_episodes=len(index.episodes), signature_index_bytes=index.signature_bytes,
                      parity=parity, acquisition_errors=errors)
        universe_record = prior_universe[0] if prior_universe else dict(snapshot_date=args.as_of,
                                                                      input_manifest_id=manifest_id, rows=universe)
        export(output, universe_record, forecasts, old, evaluations, config, report)
        report.update(elapsed_seconds=time.perf_counter() - started, cpu_seconds=time.process_time() - cpu_started,
                      peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      new_disk_bytes=directory_bytes(output) + directory_bytes(fp.ROOT) - before,
                      lab_output_bytes=directory_bytes(output))
        fp._atomic_write(output / 'resource_report.json', fp.canonical_json(report))
        event('complete', **report)
    return report


def replay(args):
    manifest_path = Path(args.replay).resolve()
    manifest = json.loads(manifest_path.read_text())
    if digest(manifest) != manifest_path.stem:
        raise ValueError('INPUT_MANIFEST_HASH_MISMATCH')
    if manifest['source_hashes'] != source_hashes():
        raise ValueError('REPLAY_REQUIRES_ORIGINAL_SOURCE')
    configure_store(args.provenance_root or Path(args.legacy_reports) / 'forecast_provenance')
    manifest_id = 'sha256:' + manifest_path.stem
    forecasts, _ = forecasts_from_manifest(manifest, manifest_id)
    saved = {f['forecast_id']: f for f in read_jsonl(manifest_path.parent.parent / 'forecast_vintages.jsonl')}
    for forecast in forecasts:
        if forecast['forecast_id'] not in saved or digest(forecast) != digest(saved[forecast['forecast_id']]):
            raise ValueError('REPLAY_MISMATCH:' + forecast['coingecko_id'])
    event('replay_pass', forecast_count=len(forecasts))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of', default=pd.Timestamp.now(tz='UTC').date().isoformat())
    parser.add_argument('--legacy-reports', default=str(ROOT / 'reports'))
    parser.add_argument('--provenance-root')
    parser.add_argument('--output', default=str(ROOT / 'reports/market_forecast_lab'))
    parser.add_argument('--markets', help='Timestamped CoinGecko response snapshot for deterministic/offline runs')
    parser.add_argument('--replay', help='Content-addressed Lab input manifest; no downloads or writes')
    args = parser.parse_args(argv)
    try:
        if args.replay:
            replay(args)
        else:
            report = execute(args)
            if not report['universe_complete']:
                event('incomplete_universe', target_count=report['target_count'])
                return 2
    except Exception as exc:
        event('failed', error=type(exc).__name__, detail=str(exc))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
