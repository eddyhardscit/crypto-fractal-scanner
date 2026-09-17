# SOL Long-Term Cone History

Ultimo aggiornamento: **2026-09-16T06:01:23.612361Z**  
SOL spot: **$97.26**  
Cohort: **40** analoghi / **29.0** distinct assets  
**LOG_ROBUST_TAIL · DIAGNOSTIC ONLY**

## Current cone

![SOL Long-Term Probability Cone — Current](sol_long_term_cone_current.png)

## Forecast history

![SOL Long-Term Cone — Forecast History](sol_long_term_cone_history.png)

Linee tra osservazioni reali consecutive, con marker; i giorni mancanti restano gap.

- p50 = mediana degli analoghi
- p75 = 25% degli analoghi sopra questo livello
- p90 = 10% degli analoghi sopra questo livello
- SOL spot = prezzo osservato nel giorno dello snapshot

## Probability history

![SOL Long-Term Cone — Probability History](sol_long_term_probability_history.png)

Le percentuali rappresentano la frequenza empirica degli analoghi che terminano sopra la soglia all'orizzonte indicato.

## Latest snapshot

| Horizon | p50 | p75 | p90 | P≥300 | P≥500 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 6M | $151.69 | $218.32 | $326.68 | 13.79% | 3.45% |
| 1Y | $141.78 | $275.28 | $537.85 | 24.14% | 13.79% |
| 2Y | $92.83 | $282.08 | $441.80 | 17.86% | 7.14% |

## Recent drift

Ultime 7 daily observations reali (non necessariamente consecutive).

| Date | Spot | 6M p50 | 1Y p50 | 2Y p50 | 2Y P≥300 | 2Y P≥500 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-09-10 | $102.05 | $140.00 | $175.40 | $134.54 | 29.63% | 11.11% |
| 2026-09-11 | $99.82 | $128.08 | $181.18 | $142.30 | 26.92% | 11.54% |
| 2026-09-12 | $101.61 | $139.40 | $184.43 | $198.98 | 29.63% | 14.81% |
| 2026-09-13 | $101.78 | $178.95 | $172.81 | $109.93 | 31.03% | 17.24% |
| 2026-09-14 | $101.11 | $164.06 | $175.95 | $98.11 | 21.43% | 14.29% |
| 2026-09-15 | $101.41 | $147.38 | $158.14 | $85.66 | 18.52% | 11.11% |
| 2026-09-16 | $97.26 | $151.69 | $141.78 | $92.83 | 17.86% | 7.14% |

## 30-day stability

Finestra: 14 osservazioni reali disponibili negli ultimi 30 giorni di calendario; i giorni mancanti non vengono interpolati.

**storico <30 giorni**: statistiche sullo storico disponibile. Campione insufficiente per interpretare lo status come prova di stabilità duratura.

| Metric | Median | Min | Max | range_pct | Range (pp) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 6M p50 | $134.96 | $128.08 | $178.95 | 37.70% | — |
| 1Y p50 | $154.40 | $124.98 | $184.43 | 38.50% | — |
| 2Y p50 | $134.64 | $85.66 | $198.98 | 84.16% | — |
| 2Y P≥300 | 26.42% | 17.86% | 32.14% | — | 14.29 |
| 2Y P≥500 | 14.81% | 7.14% | 22.22% | — | 15.08 |

**FORECAST_DRIFT_STATUS=VOLATILE**

`range_pct = 100 × (max − min) / median` per i prezzi. Le variazioni delle probabilità sono punti percentuali (pp).

- **STABLE**: 2Y p50 range_pct <20% e 2Y P≥300 range <10 pp.
- **VOLATILE**: 2Y p50 range_pct ≥40% oppure 2Y P≥300 range ≥20 pp.
- **CAUTION**: gli altri casi, inclusi dati insufficienti per classificare.

Indicatore diagnostico; non va usato per decisioni operative. Una sola osservazione ha range zero e non dimostra stabilità temporale.

## Methodology

- Stesso cohort canonico Legacy, con massimo 40 analoghi; il cohort non viene modificato.
- Vista LOG_ROBUST_TAIL e asset-level robustification già prodotte dal Long-Term Cone.
- Probabilities = empirical analog frequencies, espresse in percentuale; non probabilità calibrate.
- Diagnostic only. Nessun modello ricalcolato per questa pagina, nessun segnale o decisione operativa.
- Daily observation in Europe/Madrid: all'importazione iniziale si sceglie l'ultimo snapshot qualificante disponibile per ogni data locale. Alla prima pubblicazione la riga diventa immutabile: i successivi run non la sostituiscono e non duplicano la giornata.
- I giorni senza snapshot reale restano assenti; i valori mancanti sono indicati con —, senza stime o interpolazione.
- Ogni osservazione produce forecast vintages con target_date = forecast_date + target_horizon_days. Nessun outcome futuro viene inventato o maturato anticipatamente.

## Data availability

FIRST_REAL_SNAPSHOT=2026-09-03T17:03:34.597672Z  
FIRST_AVAILABLE_LONG_TERM_SNAPSHOT=2026-09-03T17:03:34.597672Z  
LATEST_SNAPSHOT=2026-09-16T06:01:23.612361Z  
DAILY_ROWS=14

Fonti autoritative: `sol_long_term_probability_cone.json`, `sol_long_term_probability_cone_history.jsonl` e snapshot immutabili in `sol_long_term_probability_cone_history/` nel publisher canonico.

Download: [daily observation ledger](sol_long_term_daily_history.csv) · [forecast vintages](forecast_vintages.csv).
