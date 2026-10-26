# SOL Long-Term Cone History

Ultimo aggiornamento: **2026-10-25T07:10:07.174263Z**  
SOL spot: **$101.48**  
Cohort: **40** analoghi / **29.0** distinct assets  
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
| 3M | 2027-01-23 | $60.42 | $65.18 | $79.97 | $113.13 | $140.51 |
| 6M | 2027-04-23 | $55.39 | $60.06 | $73.48 | $103.50 | $158.22 |
| 1Y | 2027-10-25 | $56.83 | $86.66 | $141.85 | $215.45 | $290.96 |
| 2Y | 2028-10-24 | $41.56 | $54.65 | $89.43 | $216.51 | $391.87 |

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
| 6M | $73.48 | $103.50 | $158.22 | 3.45% | 0.00% |
| 1Y | $141.85 | $215.45 | $290.96 | 10.34% | 3.45% |
| 2Y | $89.43 | $216.51 | $391.87 | 21.43% | 7.14% |

## Recent drift

Ultime 7 daily observations reali (non necessariamente consecutive).

| Date | Spot | 6M p50 | 1Y p50 | 2Y p50 | 2Y P≥300 | 2Y P≥500 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-10-09 | $110.26 | $74.24 | $100.10 | $66.03 | 18.52% | 3.70% |
| 2026-10-10 | $109.93 | $80.22 | $127.67 | $65.83 | 17.24% | 3.45% |
| 2026-10-11 | $109.32 | $78.67 | $126.96 | $60.23 | 16.13% | 3.23% |
| 2026-10-12 | $112.71 | $89.78 | $113.48 | $62.61 | 21.43% | 3.57% |
| 2026-10-13 | $108.24 | $87.38 | $148.95 | $78.71 | 17.86% | 3.57% |
| 2026-10-18 | $103.53 | $77.08 | $149.46 | $84.79 | 17.86% | 7.14% |
| 2026-10-25 | $101.48 | $73.48 | $141.85 | $89.43 | 21.43% | 7.14% |

## 30-day stability

Finestra: 20 osservazioni reali disponibili negli ultimi 30 giorni di calendario; i giorni mancanti non vengono interpolati.

**storico <30 giorni**: statistiche sullo storico disponibile. Campione insufficiente per interpretare lo status come prova di stabilità duratura.

| Metric | Median | Min | Max | range_pct | Range (pp) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 6M p50 | $89.73 | $73.48 | $118.50 | 50.16% | — |
| 1Y p50 | $142.93 | $100.10 | $161.36 | 42.86% | — |
| 2Y p50 | $67.58 | $54.57 | $89.43 | 51.59% | — |
| 2Y P≥300 | 16.67% | 10.34% | 21.43% | — | 11.08 |
| 2Y P≥500 | 3.64% | 3.23% | 10.00% | — | 6.77 |

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
LATEST_SNAPSHOT=2026-10-25T07:10:07.174263Z  
DAILY_ROWS=39

Fonti autoritative: `sol_long_term_probability_cone.json`, `sol_long_term_probability_cone_history.jsonl` e snapshot immutabili in `sol_long_term_probability_cone_history/` nel publisher canonico.

Download: [daily observation ledger](sol_long_term_daily_history.csv) · [forecast vintages](forecast_vintages.csv).
