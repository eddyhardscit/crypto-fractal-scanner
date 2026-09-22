# Market Forecast Lab V1 — engine only

Baseline: `c1ab39f582db495f1de19a45490ce56247d81109` (remote main verified
2026-09-22). Operational publisher HEAD at start:
`d38bb24c98818c3778cd868175b3f239180d7109`. Implementation is isolated in the
`market-forecast-lab-v1` worktree on the publisher data volume. No daily publisher,
service, timer, strategy, trading, Astro, or Conditional Successor changes.

## Invocation and failure boundary

```sh
python market_forecast_lab.py --as-of 2026-09-22 \
  --legacy-reports /path/to/authoritative/reports \
  --provenance-root /path/to/existing/reports/forecast_provenance
```

Default output is `reports/market_forecast_lab/` relative to this source checkout.
An override must retain the directory name `market_forecast_lab` and share the
existing provenance filesystem. No scheduler integration is installed. An error
returns nonzero without invoking or modifying Legacy/trading code. Input artifacts
must contain canonical scanner and tracker versions for the requested date.
Use a coherent, completed Legacy daily report snapshot. The Lab must run after
that step if integrated later; integration is not part of V1.

The Lab holds its own exclusive advisory run lock. JSONL histories use atomic
replacement and immutable daily keys; repeated identical writes are no-ops,
conflicting writes fail. CSVs are atomic individually. `latest.json` is written
last and contains checksums of all latest CSV/path artifacts. Consumers MUST
verify those hashes; a partially interrupted multi-file update is not a valid
publication. No cross-directory transaction with Legacy is attempted.

## Canonical assets and shared index

BTC, SOL, DOGE come from the existing frozen cohort manifest and frozen shared
price anchor referenced by `forecast_versions.jsonl`, not a second selection.
The 18/09/2026 SOL successor and its dynamic output are not read or incorporated.
The standard paths extend those exact 40 ranked episodes through day 60.

The historical library is the existing ordered `scanner.CRYPTO_TICKERS` library,
restricted to available frames in the canonical run. Historical signatures are
built once per run with the unchanged `add_indicators`, `make_signature_v2`,
WINDOW=100 and STEP=5. Distances remain scalar SciPy cosine. Candidate enumeration,
pandas default sorting, top 200 and the Legacy 90-day de-overlap/40 cutoff are
preserved, including tie behavior. No distance vectorization is used.

New targets may query the shared library without being library members. Reviewed
older Legacy assets may remain analogue-enabled while target-disabled. V1 needs
no new historical library assets; this preserves a comparable reference sample.
A clean cohort with invalid/gapped forward paths is reduced to its actual N,
marked `INSUFFICIENT_ANALOGUES` and excluded from rotation if N<40. It is never
backfilled with unranked episodes or reported as 40.

Parity tests compare the original per-target Legacy algorithm against the shared
index, then compare ranked cohort identities against production frozen manifests.
They check all 7/14/30/60 distributions, canonical anchors and N, and tracker
7/14/30 return/price percentiles. Float serialization comparisons tolerate only
1e-10 percentage points and 1e-8 USD (tracker CSV); cohort identity/order and
shared-index versus original calculations are exact. Tests hash Legacy outputs
before and after. Input/output code is never patched to make parity pass.

## Universe and identity

CoinGecko `/coins/markets` supplies IDs, rank, capitalization and volume, not
OHLC. See the [provider endpoint documentation](https://docs.coingecko.com/reference/coins-markets).
Pagination is bounded in config; incomplete coverage is explicitly reported.
`--markets` accepts a captured object with `provider`, `generated_at`, `rows` for
an offline/reproducible run; never an undated inferred membership list.

`market_forecast_lab_registry.json` is an explicit identity allowlist. Unknown
IDs remain `PENDING_CLASSIFICATION`. Stablecoin, wrapped, bridged, liquid-staking
and synthetic duplicates are classified separately. Unknown tokenized instruments
are pending, not implicitly assumed to be native tokens. Provider rank and
eligible rank remain separate; the first 50 *eligible* assets are selected after
classification, mapping and quality checks. Every scanned market row, including
excluded/pending/outside-50 rows, is exported with its reason.

Existing Legacy mappings are inherited. New Yahoo mappings must also agree with
Yahoo's symbol, USD currency, cryptocurrency type and CoinGecko name or a reviewed
explicit alias. For example, TON-USD is NOT Toncoin; TON11419-USD is required.
Wrong or unverifiable mappings cannot generate forecasts. Yahoo metadata evidence
and acquisition errors are preserved in each input manifest.

## Close-only semantics and data quality

Returns, positive/negative close frequencies and excursions use Close, never
High/Low. Zero returns are neither positive nor negative. Drawdown means minimum
close relative to the initial close (including day 0), not peak-to-trough drawdown.
Max gain uses the maximum close relative to that same anchor. Units are percent
and percentage points, not fractions, except empirical interval coverage (0–1).

Targets require >250 processed rows, finite positive OHLC, nonnegative volume,
monotonic unique dates and an anchor no older than two days. The current 100-row
signature may contain at most ONE missing day, and no gap may exceed two days
(configured thresholds). Such an input, a delayed anchor, or High/Low inconsistent with Close,
receives `LIMITED_CLOSE_ONLY_INPUT` and a limited quality label. This preserves
Legacy input semantics without inventing a missing candle. Larger gaps fail
eligibility. Historical 60-day output paths must contain all 61 consecutive daily
closes. No interpolation or data repair is performed.

The 22/09/2026 frozen Legacy inputs contain a missing 21/09 row; this limitation
is surfaced, not silently labeled GOOD. Canonical anchors can be the same-day
partial candle because that is the existing Legacy convention. Evaluations accept
only completed daily candles strictly before the evaluation run date and require
the exact target date, never the next available close. A target date preceding
the forecast issue date is never counted as a future result.

Headline quality exposes data quality, N, distinct assets, mean/median similarity,
cone width P75−P25 and evaluation controls. Before 30 matured observations at the
same horizon, MAE and coverages are JSON null / empty CSV fields (N/A), never zero.
Quality thresholds and labels are in config; no aggregate 0–100 score exists.
Provisional quality does not imply validated predictive skill.

## Vintages, evaluation and rotation

One immutable forecast per CoinGecko ID per forecast day. Its content-derived ID
includes anchor, input manifest, ranked cohort, all 61 paths and headline results.
Retrying a day uses its first captured universe/input manifest; changing engine
source/config for an existing day requires replay with the original version.
An asset exiting Top50 receives no new vintage. Old vintages remain evaluable at
1/3/7/14/30/60 days, including after exit. Reentry starts new daily vintages.
First completed evaluations are immutable and reference their actual OHLC hash.
Quality controls mature from these evaluations; no fabricated historical controls.

Rotation is descriptive, by horizon and benchmark. Edge is target P50 minus SOL,
BTC or the median P50 of the current rotation-ready eligible subset. The actual
benchmark count is exported; an absent SOL/BTC yields null, never zero. All
comparisons use the same forecast day. Last-three records include daily gaps and
forecast IDs. Same-day retries do not count as persistence.

Defaults: ordinary edge ≥3 percentage points; strong current edge ≥10; ordinary
persistence needs at least 2 of the last 3 daily snapshots AND the current edge.
A single strong edge is `STRONG_CURRENT_EDGE`, not `PERSISTENT_EDGE`. Negative
persistence uses ≤−3. Sparse history yields WARMUP/ONE_DAY_EDGE as appropriate;
missing inputs yield INSUFFICIENT_DATA. No action labels are emitted. Thresholds
are initial descriptive policy, not optimized trading recommendations.

V1 does not possess a comparable paired historical design for P(A outperforms B).
It emits null and `N_PAIR=0` with a reason. It never subtracts independent samples
or pretends that coincidentally shared analogue dates create paired observations.

## Provenance, replay and restore

The existing `forecast_provenance` content-addressed OHLC store is reused directly.
Existing objects are hash-verified; new target OHLC use its existing `freeze_ohlc`.
There is no second raw store. Small content-addressed Lab manifests contain exact
CoinGecko input, registry, config, raw IDs, ordered library, canonical cohorts,
quality controls, source hashes and source commit/dirty status. Each forecast
references its manifest. Canonical price anchors retain their original snapshot ID.

```sh
python market_forecast_lab.py --replay reports/market_forecast_lab/inputs/HASH.json \
  --provenance-root /path/to/existing/reports/forecast_provenance
```

Replay performs no downloads or writes. It verifies the manifest/source hashes,
loads referenced frozen bytes, reconstructs forecasts and compares their complete
immutable content with the saved vintage log. Restore requires Lab histories and
input manifests plus the referenced existing raw/cohort objects and the matching
source/config. Existing absolute `dataset_path` metadata is not used for loading;
`--provenance-root` can point at a restored volume.

Storage deliberately uses the existing whole-asset snapshots. Content-identical
snapshots deduplicate; changed daily histories remain whole-file versions. Growth
is linear in new versions times retained history size. No retention/deletion or
monthly chunk subsystem is introduced. Capacity planning and restore backups are
required before publisher integration; resource measurements in the acceptance report are one run,
not an extrapolated monthly-growth claim.

## Verification

```sh
SCANNER_FORECAST_PROVENANCE_DIR=/path/to/existing/reports/forecast_provenance \
LAB_REAL_PARITY_REPORTS=/path/to/authoritative/reports \
python -m unittest discover -s tests -p test_market_forecast_lab.py -v
```

Without LAB_REAL_PARITY_REPORTS the four real-artifact tests are explicitly skipped;
that is not sufficient for release acceptance. The acceptance run enables them.
The fixture date is explicitly 2026-09-22. The resource report records elapsed and
CPU seconds, peak RSS (KiB on Linux), new logical bytes in the Lab plus the existing
provenance store, targets, valid/insufficient forecasts, signature matrix bytes,
episode count and total Lab output bytes. A non-published trial and replay are
required before any later publisher integration. Resource logs/reports are not a
live publication or permission to deploy.

Dependency versions used for acceptance are recorded in `requirements-market-forecast-lab.txt`
(Python 3.14). They are not installed into or changed in the publisher environment.
The self-reported byte counters are sampled before writing the resource report;
the acceptance report also records the final measured Lab directory size.
