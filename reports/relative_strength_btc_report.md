# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-09-24 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00137300 | +6 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +10,02% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000112 | -2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -1,55% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+6)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +6,02%; 30g +10,02%; 90g +21,29%; 180g +9,75%
- **Daily:** RSI 62.01; MA50 0.00126758; MA200 0.00118878
- **Weekly:** MA30 0.00119607; RSI 61.09
- **Livelli:** supporto 0.00127800; resistenza 0.00140500; breakout 60g 0.00140500; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00131154
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +5,56%; 30g -1,55%; 90g -10,49%; 180g -17,39%
- **Daily:** RSI 54.15; MA50 0.00000110; MA200 0.00000124
- **Weekly:** MA30 0.00000124; RSI 42.02
- **Livelli:** supporto 0.00000112; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 209 | 52,63% | +1,96% | -1,05% |
| SOL | 30g | 206 | 47,57% | +4,57% | +0,58% |
| SOL | 90g | 200 | 52,50% | +9,74% | +3,06% |
| DOGE | 7g | 295 | 55,59% | +1,83% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 288 | 54,17% | +6,90% | -9,24% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 37 | 56,76% | +0,13% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 35 | 54,29% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 35 | 42,86% | +0,55% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 35 | 45,71% | +0,61% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 22 | 31,82% | -4,88% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 54 | 66,67% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 54 | 57,41% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 54 | 53,70% | -0,57% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 47 | 57,45% | +0,08% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 35 | 65,71% | +0,39% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
