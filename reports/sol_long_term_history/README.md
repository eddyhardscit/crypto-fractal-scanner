# SOL Long-Term Cone History

Ultimo aggiornamento: **2026-10-04T06:00:54.223784Z**  
SOL spot: **$120.80**  
Cohort: **40** analoghi / **30.0** distinct assets  
**LOG_ROBUST_TAIL · DIAGNOSTIC ONLY**

## Current cone

![SOL Long-Term Probability Cone — Current](sol_long_term_cone_current.png)

<!-- SOL_FORWARD_VIEWS_START -->
## Short-term context (30 giorni)

Questa pagina resta il **Long-Term Cone** (3M/6M/1Y/2Y). Il blocco seguente riporta, senza ricalcolarli o mescolarli, gli ultimi output dello scanner SOL a 30 giorni.

Dati short-term non disponibili in questo snapshot; il Long-Term Cone resta invariato.

[Apri il report short-term](../latest_report.md)

## Forward calendar

![SOL Long-Term Cone — Forward Calendar](sol_long_term_forward_calendar.svg)

Asse X = date future reali. Le linee mostrano esplicitamente p10, p25, p50, p75 e p90 ai soli orizzonti registrati 90/180/365/730 giorni; i segmenti collegano i punti per leggibilità e non creano previsioni intermedie.

| Horizon | Target date | p10 | p25 | p50 | p75 | p90 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 3M | 2027-01-02 | $98.44 | $121.84 | $141.16 | $182.49 | $237.86 |
| 6M | 2027-04-02 | $65.46 | $75.60 | $91.28 | $121.56 | $186.02 |
| 1Y | 2027-10-04 | $71.24 | $95.27 | $144.00 | $201.69 | $327.18 |
| 2Y | 2028-10-03 | $17.81 | $34.52 | $70.28 | $129.90 | $368.12 |

## Forward vintages

![SOL Long-Term Cone — Forward Vintages](sol_long_term_forward_vintages.svg)

Ogni linea è un vero snapshot giornaliero proiettato sulle sue date target esatte. La linea più marcata è l'ultimo vintage; sono usati spot e p50 registrati, senza punti sintetici.

<!-- SOL_FORWARD_VIEWS_END -->

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
| 6M | $91.28 | $121.56 | $186.02 | 10.00% | 0.00% |
| 1Y | $144.00 | $201.69 | $327.18 | 13.33% | 3.33% |
| 2Y | $70.28 | $129.90 | $368.12 | 17.86% | 7.14% |

## Recent drift

Ultime 7 daily observations reali (non necessariamente consecutive).

| Date | Spot | 6M p50 | 1Y p50 | 2Y p50 | 2Y P≥300 | 2Y P≥500 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-09-28 | $119.03 | $110.90 | $149.78 | $69.13 | 14.29% | 7.14% |
| 2026-09-29 | $118.35 | $104.61 | $161.36 | $76.61 | 16.67% | 10.00% |
| 2026-09-30 | $118.99 | $98.97 | $136.06 | $72.83 | 16.67% | 3.33% |
| 2026-10-01 | $119.33 | $99.99 | $153.62 | $62.05 | 16.67% | 3.33% |
| 2026-10-02 | $120.31 | $100.26 | $154.09 | $64.17 | 13.33% | 3.33% |
| 2026-10-03 | $119.62 | $104.33 | $153.21 | $69.35 | 13.79% | 3.45% |
| 2026-10-04 | $120.80 | $91.28 | $144.00 | $70.28 | 17.86% | 7.14% |

## 30-day stability

Finestra: 26 osservazioni reali disponibili negli ultimi 30 giorni di calendario; i giorni mancanti non vengono interpolati.

**storico <30 giorni**: statistiche sullo storico disponibile. Campione insufficiente per interpretare lo status come prova di stabilità duratura.

| Metric | Median | Min | Max | range_pct | Range (pp) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 6M p50 | $129.84 | $91.28 | $178.95 | 67.52% | — |
| 1Y p50 | $153.42 | $124.98 | $205.66 | 52.59% | — |
| 2Y p50 | $85.49 | $53.69 | $198.98 | 169.94% | — |
| 2Y P≥300 | 19.60% | 13.33% | 32.14% | — | 18.81 |
| 2Y P≥500 | 9.53% | 0.00% | 17.24% | — | 17.24 |

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
LATEST_SNAPSHOT=2026-10-04T06:00:54.223784Z  
DAILY_ROWS=28

Fonti autoritative: `sol_long_term_probability_cone.json`, `sol_long_term_probability_cone_history.jsonl` e snapshot immutabili in `sol_long_term_probability_cone_history/` nel publisher canonico.

Download: [daily observation ledger](sol_long_term_daily_history.csv) · [forecast vintages](forecast_vintages.csv).
