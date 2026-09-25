"""Reviewed identity registry and fail-closed CoinGecko membership selection."""
from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

CONFIG_PATH = Path(__file__).with_name('market_forecast_lab_config.json')
REGISTRY_PATH = Path(__file__).with_name('market_forecast_lab_registry.json')


def load_config():
    return json.loads(CONFIG_PATH.read_text())


def load_registry():
    records = json.loads(REGISTRY_PATH.read_text())['assets']
    if len({r['coingecko_id'] for r in records}) != len(records):
        raise ValueError('DUPLICATE_REGISTRY_ID')
    targets = [r['ohlc_ticker'] for r in records if r['target_enabled']]
    if len(targets) != len(set(targets)):
        raise ValueError('DUPLICATE_TARGET_MAPPING')
    return {r['coingecko_id']: r for r in records}


def dedupe_market_rows(rows):
    """Remove live pagination overlaps while preserving explicit evidence."""
    unique, seen, duplicates = [], set(), []
    for row in rows:
        cid = row.get('id') if isinstance(row, dict) else None
        if not cid:
            raise ValueError('INVALID_MARKET_ROW')
        if cid in seen:
            duplicates.append(cid)
            continue
        seen.add(cid)
        unique.append(row)
    return unique, sorted(set(duplicates))


def fetch_markets(config):
    """Bounded pagination with explicit de-duplication of provider page overlap."""
    rows = []
    for page in range(1, config['market_pages'] + 1):
        params = urllib.parse.urlencode(dict(vs_currency='usd', order='market_cap_desc',
                                            per_page=config['market_per_page'], page=page,
                                            sparkline='false'))
        headers = {'User-Agent': 'MarketForecastLab/1.0'}
        if os.getenv('COINGECKO_DEMO_API_KEY'):
            headers['x-cg-demo-api-key'] = os.environ['COINGECKO_DEMO_API_KEY']
        request = urllib.request.Request('https://api.coingecko.com/api/v3/coins/markets?' + params,
                                         headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            part = json.load(response)
        if not isinstance(part, list):
            raise ValueError('INVALID_MARKET_RESPONSE')
        rows.extend(part)
        if len(part) < config['market_per_page']:
            break
    unique, duplicates = dedupe_market_rows(rows)
    return {'provider': 'CoinGecko', 'generated_at': datetime.now(timezone.utc).isoformat(),
            'raw_row_count': len(rows), 'duplicate_ids_removed': duplicates, 'rows': unique}


def data_quality(frame, as_of, config):
    if frame is None or len(frame) < config['minimum_processed_rows']:
        return 'INSUFFICIENT_HISTORY'
    idx = pd.DatetimeIndex(frame.index)
    if idx.has_duplicates or not idx.is_monotonic_increasing:
        return 'INVALID_DATES'
    if not {'Open', 'High', 'Low', 'Close', 'Volume'}.issubset(frame.columns):
        return 'MISSING_OHLC'
    numbers = frame[['Open', 'High', 'Low', 'Close', 'Volume']].to_numpy(float)
    if not np.isfinite(numbers).all() or (numbers[:, :4] <= 0).any() or (numbers[:, 4] < 0).any():
        return 'INVALID_OHLC'
    # V1 uses Close and Volume, never intraday High/Low extrema. Report but do
    # not reinterpret an inconsistent High/Low as a close-path observation.
    recent = frame.tail(100)
    daily_gaps = np.asarray((recent.index[1:] - recent.index[:-1]).total_seconds()) / 86400
    missing = int(np.maximum(daily_gaps - 1, 0).sum())
    if (missing > config['current_signature_max_missing_days'] or
            (len(daily_gaps) and max(daily_gaps) > config['current_signature_max_gap_days'])):
        return 'GAPPED_DAILY_HISTORY'
    bad_range = ((recent.High < recent[['Open', 'Close', 'Low']].max(axis=1)) |
                 (recent.Low > recent[['Open', 'Close', 'High']].min(axis=1))).any()
    as_of_date = pd.Timestamp(as_of).date()
    age = (as_of_date - idx[-1].date()).days
    if age < 0 or age > config['max_close_age_days']:
        return 'STALE_OR_FUTURE_CLOSE'
    # A row stamped with today's UTC date is still an in-progress crypto candle.
    partial_current_day = idx[-1].date() == as_of_date
    return 'LIMITED_CLOSE_ONLY_INPUT' if missing or bad_range or age or partial_current_day else 'GOOD'


def select_universe(snapshot, registry, processed, as_of, config, acquisition_errors=None):
    generated = pd.Timestamp(snapshot['generated_at'])
    age = (pd.Timestamp(as_of, tz='UTC') - generated.tz_convert('UTC')).total_seconds() / 3600
    if age < -24 or age > config['max_market_age_hours']:
        raise ValueError('STALE_OR_FUTURE_UNIVERSE')
    rows, seen, eligible = [], set(), 0
    markets = sorted(snapshot['rows'], key=lambda x: (x.get('market_cap_rank') or 10**12, x['id']))
    for coin in markets:
        cid = coin['id']
        if cid in seen:
            raise ValueError('DUPLICATE_MARKET_ID:' + cid)
        seen.add(cid)
        reg = registry.get(cid)
        reason, status, quality = '', 'EXCLUDED', None
        if reg is None or reg['classification'] == 'PENDING_CLASSIFICATION':
            status, reason = 'PENDING_CLASSIFICATION', 'UNREVIEWED_IDENTITY'
        elif reg['classification'] != 'NATIVE':
            reason = reg['classification']
        elif not reg.get('ohlc_ticker'):
            reason = 'NO_RELIABLE_OHLC_MAPPING'
        elif 'OHLC_IDENTITY_NOT_VERIFIED' in (acquisition_errors or {}).get(reg['ohlc_ticker'], ''):
            reason = 'NO_RELIABLE_OHLC_MAPPING'
        elif not reg['target_enabled']:
            reason = 'TARGET_DISABLED'
        elif not coin.get('market_cap_rank') or not coin.get('market_cap') or coin['market_cap'] <= 0:
            reason = 'INVALID_MARKET_DATA'
        else:
            quality = data_quality(processed.get(reg['ohlc_ticker']), as_of, config)
            if quality not in ('GOOD', 'LIMITED_CLOSE_ONLY_INPUT'):
                reason = quality
            else:
                eligible += 1
                status = 'INCLUDED' if eligible <= config['universe_size'] else 'OUTSIDE_TOP50'
        rows.append(dict(provider_rank=coin.get('market_cap_rank'),
                         eligible_rank=eligible if status in ('INCLUDED', 'OUTSIDE_TOP50') else None,
                         coingecko_id=cid, symbol=coin['symbol'], name=coin['name'],
                         market_cap=coin.get('market_cap'), volume=coin.get('total_volume'),
                         inclusion_status=status, exclusion_reason=reason,
                         snapshot_date=str(as_of), generated_at=snapshot['generated_at'],
                         ohlc_ticker=reg.get('ohlc_ticker') if reg else None, data_quality=quality))
    return rows
