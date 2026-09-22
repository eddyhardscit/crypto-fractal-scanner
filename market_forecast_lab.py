#!/usr/bin/env python3
"""Artifact-only Forecast Lab entrypoint. Never invokes scanner.main or trading code."""
from __future__ import annotations

import argparse
import copy
import fcntl
import hashlib
import json
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

from market_forecast_lab_run import (
    MODES, CONTEXT_FIELDS, context, new_context, prepare_paths, seed_trial_store,
    freeze_run_ohlc, require_official, read_history, is_official, read_official_latest,
)

from market_forecast_lab_publication import official_transaction, runtime_root

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
             'market_forecast_lab_universe.py', 'market_forecast_lab_run.py',
             'market_forecast_lab_publication.py', 'market_forecast_lab_config.json',
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


def acquire_extra(registry, markets, raw, processed, snapshot_ids, old, as_of, ctx):
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
            sid = freeze_run_ohlc(frame, ticker=ticker, as_of=as_of, ctx=ctx)
            # Always compute from reloaded bytes: live acquisition and replay share precision.
            raw[ticker] = fp.load_frozen_ohlc(sid)
            processed[ticker] = legacy.add_indicators(raw[ticker])
            snapshot_ids[ticker] = sid
        except Exception as exc:
            errors[ticker] = type(exc).__name__ + ':' + str(exc)
    return errors, identities


def forecasts_from_manifest(manifest, manifest_id, index=None, existing=()):
    ctx = context(manifest)
    if ctx['run_mode'] == 'REPLAY':
        raise ValueError('REPLAY_IS_NOT_A_VINTAGE_SOURCE_MODE')
    if any(context(f)['run_mode'] != ctx['run_mode'] for f in existing):
        raise ValueError('MIXED_MODE_VINTAGES')
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
        forecasts[-1].update(ctx)
        forecasts[-1].pop('forecast_id')
        forecasts[-1]['forecast_id'] = f"lab:{ctx['run_mode']}:{cid}:{manifest['as_of']}:" + digest(forecasts[-1])
        event('forecast', **ctx, asset=cid, N=forecasts[-1]['N'], status=forecasts[-1]['status'])
    return forecasts, index


def append_official_history(output, name, rows, keys, ctx):
    require_official(output, ctx, rows)
    read_history(output, name, ctx)
    immutable_append(output / name, rows, keys)


def export(output, universe_record, forecasts, old, evaluations, config, run_report):
    ctx = context(run_report)
    if ctx['run_mode'] == 'REPLAY':
        raise ValueError('REPLAY_EXPORT_FORBIDDEN')
    if context(universe_record)['run_mode'] != ctx['run_mode']:
        raise ValueError('MIXED_MODE_UNIVERSE')
    if any(context(f)['run_mode'] != ctx['run_mode'] for f in forecasts + old):
        raise ValueError('MIXED_MODE_EXPORT')
    versions = [dict(**context(f), forecast_id=f['forecast_id'], coingecko_id=f['coingecko_id'],
                     forecast_date=f['forecast_date'], paths=f['paths']) for f in forecasts]
    old_evaluations = read_history(output, 'evaluation_versions.jsonl', ctx)
    done = {(e['forecast_id'], e['horizon']) for e in old_evaluations}
    new_evaluations = [{**e, **ctx} for e in evaluations if (e['forecast_id'], e['horizon']) not in done]
    if ctx['run_mode'] == 'OFFICIAL_DAILY':
        append_official_history(output, 'universe_history.jsonl', [universe_record], ('snapshot_date',), ctx)
        append_official_history(output, 'forecast_vintages.jsonl', forecasts, ('coingecko_id', 'forecast_date'), ctx)
        append_official_history(output, 'forecast_path_versions.jsonl', versions, ('forecast_id',), ctx)
        append_official_history(output, 'evaluation_versions.jsonl', new_evaluations, ('forecast_id', 'horizon'), ctx)
    else:
        # Isolated evidence only; no official-history filename is written in TRIAL.
        fp._atomic_write(output / 'trial_forecasts.jsonl', b''.join(fp.canonical_json(f) for f in forecasts))
    all_evaluations = old_evaluations + new_evaluations
    rotation_rows = [{**r, **ctx} for r in rotation(forecasts, old, config)]
    forecast_rows = []
    for f in forecasts:
        for headline in f['headlines']:
            forecast_rows.append(dict(**context(f), forecast_id=f['forecast_id'], coingecko_id=f['coingecko_id'],
                                      forecast_date=f['forecast_date'], anchor_price=f['anchor_price'],
                                      anchor_date=f['anchor_date'], status=f['status'],
                                      input_manifest_id=f['input_manifest_id'], **headline))
    write_csv(output / 'universe_latest.csv', universe_record['rows'], list(CONTEXT_FIELDS) + ['coingecko_id', 'inclusion_status'])
    write_csv(output / 'forecast_latest.csv', forecast_rows, list(CONTEXT_FIELDS) + ['forecast_id', 'coingecko_id', 'horizon', 'status'])
    write_csv(output / 'rotation_latest.csv', rotation_rows, list(CONTEXT_FIELDS) + ['coingecko_id', 'horizon', 'states'])
    write_csv(output / 'evaluation_latest.csv', all_evaluations, list(CONTEXT_FIELDS) + ['forecast_id', 'coingecko_id', 'horizon', 'actual_close'])
    fp._atomic_write(output / 'forecast_paths_latest.json', fp.canonical_json({**ctx, 'versions': versions}))
    artifacts = ['universe_latest.csv', 'forecast_latest.csv', 'forecast_paths_latest.json',
                 'rotation_latest.csv', 'evaluation_latest.csv']
    latest = dict(**ctx, schema_version=2, status='COMPLETE', forecast_date=universe_record['snapshot_date'],
                  run=run_report, forecasts=forecasts, rotation=rotation_rows,
                  artifacts={name: hashlib.sha256((output / name).read_bytes()).hexdigest() for name in artifacts})
    fp._atomic_write(output / 'latest.json', fp.canonical_json(latest))


def execute(args):
    if args.mode != 'OFFICIAL_DAILY':
        return execute_staged(args)
    if args.trial_root:
        raise ValueError('TRIAL_ROOT_NOT_ALLOWED_FOR_OFFICIAL')
    destination = Path(args.output or ROOT / 'reports/market_forecast_lab').absolute()
    reports = Path(args.legacy_reports).resolve()
    source = Path(args.provenance_root or reports / 'forecast_provenance').resolve()
    if (destination.name != 'market_forecast_lab' or destination.is_symlink()
            or source == destination or source.is_relative_to(destination)
            or destination.is_relative_to(source) or reports.is_relative_to(destination)):
        raise ValueError('UNSAFE_OUTPUT_DIRECTORY')
    runtime = runtime_root(ROOT, destination)
    with official_transaction(destination, runtime, args.run_context) as staged:
        staged_args = copy.copy(args)
        staged_args.output = str(staged)
        staged_args.runtime = runtime
        report = execute_staged(staged_args)
    event('official_published', **context(report), output=str(destination))
    return report


def execute_staged(args):
    started, cpu_started = time.perf_counter(), time.process_time()
    ctx = context(args.run_context)
    reports = Path(args.legacy_reports).resolve()
    source_root = Path(args.provenance_root or reports / 'forecast_provenance').resolve()
    configure_store(source_root)
    output, write_root = prepare_paths(args, ctx, source_root, reports, ROOT)
    yf.set_tz_cache_location(str(Path(getattr(args, 'runtime', output)) / '.yfinance-cache'))
    event('run_selected', **ctx, output=str(output), provenance_write_root=str(write_root))
    with (output / '.run.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        before = directory_bytes(output) + directory_bytes(write_root)
        config, registry = load_config(), load_registry()
        raw, processed, snapshot_ids, canonical = load_legacy_inputs(reports, args.as_of)
        if ctx['run_mode'] == 'TRIAL':
            seed_trial_store(source_root, write_root, snapshot_ids, canonical, ctx)
            configure_store(write_root)
        event('canonical_loaded', **ctx, targets=list(canonical), raw_assets=len(raw))
        library_order = [t for t in legacy.CRYPTO_TICKERS if t in processed
                         and any(r.get('ohlc_ticker') == t and r['analogue_enabled'] for r in registry.values())]
        old = read_history(output, 'forecast_vintages.jsonl', ctx)
        prior_universe = [r for r in read_history(output, 'universe_history.jsonl', ctx) if r['snapshot_date'] == args.as_of]
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
        errors, identities = acquire_extra(registry, markets, raw, processed, snapshot_ids, old, args.as_of, ctx)
        event('inputs_ready', **ctx, raw_assets=len(raw), unavailable=errors)
        universe = (prior_universe[0]['rows'] if prior_universe else
                    [{**r, **ctx} for r in select_universe(markets, registry, processed, args.as_of, config, errors)])
        evaluations = evaluate(old, raw, snapshot_ids, args.as_of)
        # Mature quality uses immutable observations only; not yet-mature values remain null.
        prior_evaluations = read_history(output, 'evaluation_versions.jsonl', ctx)
        done = {(e['forecast_id'], e['horizon']) for e in prior_evaluations}
        quality_evaluations = prior_evaluations + [e for e in evaluations if (e['forecast_id'], e['horizon']) not in done]
        manifest = dict(**ctx, schema_version=2, as_of=args.as_of, config=config, registry=registry,
                        markets=markets, universe=universe, library_order=library_order,
                        raw_snapshot_ids=snapshot_ids, canonical=canonical,
                        quality_evaluations=quality_evaluations, source_hashes=source_hashes(),
                        code_provenance=fp.code_provenance(), acquisition_errors=errors, ohlc_identity_evidence=identities)
        if prior_universe:
            if previous['source_hashes'] != source_hashes():
                raise ValueError('DAILY_SOURCE_CHANGED_REPLAY_ORIGINAL_VERSION')
            manifest = previous
        manifest_id = store_input(output, manifest)
        event('index_build_started', **ctx, library_assets=len(library_order))
        frozen_library = {t: legacy.add_indicators(fp.load_frozen_ohlc(manifest['raw_snapshot_ids'][t]))
                          for t in manifest['library_order']}
        index = SharedSignatureIndex(frozen_library)
        event('index_ready', **ctx, episodes=len(index.episodes), signature_bytes=index.signature_bytes)
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
        report = dict(**ctx, as_of=args.as_of, published=ctx['official_daily'], input_manifest_id=manifest_id,
                      universe_complete=sum(r['inclusion_status'] == 'INCLUDED' for r in universe) == config['universe_size'],
                      target_count=sum(r['inclusion_status'] == 'INCLUDED' for r in universe),
                      valid_count=sum(f['status'] == 'VALID' for f in forecasts),
                      insufficient_count=sum(f['status'] == 'INSUFFICIENT_ANALOGUES' for f in forecasts),
                      signature_index_episodes=len(index.episodes), signature_index_bytes=index.signature_bytes,
                      parity=parity, acquisition_errors=errors)
        universe_record = prior_universe[0] if prior_universe else dict(**ctx, snapshot_date=args.as_of,
                                                                      input_manifest_id=manifest_id, rows=universe)
        if not report['universe_complete'] and ctx['run_mode'] == 'OFFICIAL_DAILY':
            raise ValueError('INCOMPLETE_UNIVERSE_OFFICIAL_PUBLICATION_REFUSED')
        export(output, universe_record, forecasts, old, evaluations, config, report)
        report.update(elapsed_seconds=time.perf_counter() - started, cpu_seconds=time.process_time() - cpu_started,
                      peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      new_disk_bytes=directory_bytes(output) + directory_bytes(fp.ROOT) - before,
                      lab_output_bytes=directory_bytes(output))
        fp._atomic_write(output / 'resource_report.json', fp.canonical_json(report))
        event('complete', **report)
    return report


def replay(args):
    replay_ctx = context(args.run_context)
    if replay_ctx['run_mode'] != 'REPLAY':
        raise ValueError('EXPLICIT_REPLAY_MODE_REQUIRED')
    event('run_selected', **replay_ctx)
    manifest_path = Path(args.replay).resolve()
    manifest = json.loads(manifest_path.read_text())
    if digest(manifest) != manifest_path.stem:
        raise ValueError('INPUT_MANIFEST_HASH_MISMATCH')
    if manifest['source_hashes'] != source_hashes():
        raise ValueError('REPLAY_REQUIRES_ORIGINAL_SOURCE')
    configure_store(args.provenance_root or Path(args.legacy_reports) / 'forecast_provenance')
    manifest_id = 'sha256:' + manifest_path.stem
    forecasts, _ = forecasts_from_manifest(manifest, manifest_id)
    name = 'forecast_vintages.jsonl' if is_official(manifest) else 'trial_forecasts.jsonl'
    saved = {f['forecast_id']: f for f in read_jsonl(manifest_path.parent.parent / name)}
    for forecast in forecasts:
        if forecast['forecast_id'] not in saved or digest(forecast) != digest(saved[forecast['forecast_id']]):
            raise ValueError('REPLAY_MISMATCH:' + forecast['coingecko_id'])
    event('replay_pass', **replay_ctx, source_run_mode=manifest['run_mode'], source_run_id=manifest['run_id'], forecast_count=len(forecasts))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', required=True, choices=MODES, help='Required: TRIAL, OFFICIAL_DAILY, or read-only REPLAY')
    parser.add_argument('--trial-root', help='Parent for a fresh isolated trial directory; never official reports/provenance')
    parser.add_argument('--as-of', default=pd.Timestamp.now(tz='UTC').date().isoformat())
    parser.add_argument('--legacy-reports', default=str(ROOT / 'reports'))
    parser.add_argument('--provenance-root')
    parser.add_argument('--output', help='OFFICIAL_DAILY only; default reports/market_forecast_lab')
    parser.add_argument('--markets', help='Timestamped CoinGecko response snapshot for deterministic/offline runs')
    parser.add_argument('--replay', help='Content-addressed Lab input manifest; no downloads or writes')
    args = parser.parse_args(argv)
    if (args.mode == 'REPLAY') != bool(args.replay):
        parser.error('--mode REPLAY and --replay must be specified together')
    if args.mode == 'REPLAY' and (args.output or args.trial_root):
        parser.error('REPLAY cannot specify writable output paths')
    args.run_context = new_context(args.mode)
    try:
        if args.mode == 'REPLAY':
            replay(args)
        else:
            report = execute(args)
            if not report['universe_complete']:
                event('incomplete_universe', **args.run_context, target_count=report['target_count'])
                return 2
    except Exception as exc:
        event('failed', **args.run_context, error=type(exc).__name__, detail=str(exc))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
