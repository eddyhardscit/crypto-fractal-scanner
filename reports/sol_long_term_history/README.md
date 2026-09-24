# SOL Long-Term Cone History

Ultimo aggiornamento: **2026-09-23T11:03:45.244992Z**  
SOL spot: **$117.42**  
Cohort: **40** analoghi / **30.0** distinct assets  
**LOG_ROBUST_TAIL · DIAGNOSTIC ONLY**

## Current cone

![SOL Long-Term Probability Cone — Current](sol_long_term_cone_current.png)

<!-- SOL_FORWARD_VIEWS_START -->
## Short-term context (30 giorni)

Questa pagina resta il **Long-Term Cone** (3M/6M/1Y/2Y). Il blocco seguente riporta, senza ricalcolarli o mescolarli, gli ultimi output dello scanner SOL a 30 giorni.

| Modello short-term | Snapshot | Campione | P10 | P25 | P50 | P75 | P90 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-09-24 | 40 analoghi correnti | $77.07 | $93.26 | $115.80 | $141.86 | $194.70 |
| Conditional -5% → +10% corrente | 2026-09-24 | 8 | $92.29 | $97.96 | $144.44 | $185.20 | $247.54 |
| Conditional vintage 18 Sep | 2026-09-18 | 8 | $96.70 | $109.70 | $168.54 | $188.19 | $214.50 |

- **Standard:** usa i 40 analoghi SOL correnti.
- **Conditional corrente:** filtra quei 40 e mantiene solo gli episodi che fanno prima -5% e poi +10% entro 30 giorni.
- **Vintage 18 Sep:** resta congelato per la verifica fuori campione della previsione originale.
- Questi numeri non vengono mediati con il Long-Term Cone e non ne modificano il modello.

[Apri il dettaglio short-term](../latest_report.md)
## Forward calendar

![SOL Long-Term Cone — Forward Calendar](sol_long_term_forward_calendar.svg)

Asse X = date future reali. Le linee mostrano esplicitamente p10, p25, p50, p75 e p90 ai soli orizzonti registrati 90/180/365/730 giorni; i segmenti collegano i punti per leggibilità e non creano previsioni intermedie.

| Horizon | Target date | p10 | p25 | p50 | p75 | p90 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 3M | 2026-12-22 | $78.52 | $97.10 | $140.72 | $190.90 | $245.33 |
| 6M | 2027-03-22 | $52.13 | $82.16 | $111.68 | $141.94 | $235.76 |
| 1Y | 2027-09-23 | $50.05 | $97.58 | $137.97 | $220.92 | $386.68 |
| 2Y | 2028-09-22 | $25.18 | $35.96 | $53.17 | $151.67 | $426.15 |

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
| 6M | $111.68 | $141.94 | $235.76 | 10.00% | 6.67% |
| 1Y | $137.97 | $220.92 | $386.68 | 16.67% | 10.00% |
| 2Y | $53.17 | $151.67 | $426.15 | 17.24% | 6.90% |

## Recent drift

Ultime 7 daily observations reali (non necessariamente consecutive).

| Date | Spot | 6M p50 | 1Y p50 | 2Y p50 | 2Y P≥300 | 2Y P≥500 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-09-13 | $101.78 | $178.95 | $172.81 | $109.93 | 31.03% | 17.24% |
| 2026-09-14 | $101.11 | $164.06 | $175.95 | $98.11 | 21.43% | 14.29% |
| 2026-09-15 | $101.41 | $147.38 | $158.14 | $85.66 | 18.52% | 11.11% |
| 2026-09-16 | $97.26 | $151.69 | $141.78 | $92.83 | 17.86% | 7.14% |
| 2026-09-17 | $99.50 | $134.66 | $146.76 | $85.63 | 18.52% | 7.41% |
| 2026-09-22 | $116.89 | $134.72 | $155.34 | $75.72 | 23.33% | 6.67% |
| 2026-09-23 | $118.57 | $114.69 | $151.20 | $53.69 | 14.81% | 0.00% |

## 30-day stability

Finestra: 17 osservazioni reali disponibili negli ultimi 30 giorni di calendario; i giorni mancanti non vengono interpolati.

**storico <30 giorni**: statistiche sullo storico disponibile. Campione insufficiente per interpretare lo status come prova di stabilità duratura.

| Metric | Median | Min | Max | range_pct | Range (pp) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 6M p50 | $134.66 | $114.69 | $178.95 | 47.72% | — |
| 1Y p50 | $151.20 | $124.98 | $184.43 | 39.32% | — |
| 2Y p50 | $127.85 | $53.69 | $198.98 | 113.64% | — |
| 2Y P≥300 | 24.00% | 14.81% | 32.14% | — | 17.33 |
| 2Y P≥500 | 14.29% | 0.00% | 22.22% | — | 22.22 |

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
LATEST_SNAPSHOT=2026-09-23T11:03:45.244992Z  
DAILY_ROWS=17

Fonti autoritative: `sol_long_term_probability_cone.json`, `sol_long_term_probability_cone_history.jsonl` e snapshot immutabili in `sol_long_term_probability_cone_history/` nel publisher canonico.

Download: [daily observation ledger](sol_long_term_daily_history.csv) · [forecast vintages](forecast_vintages.csv).
