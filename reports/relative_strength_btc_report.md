# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-07-31 05:15 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00114760 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -8,63% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |
| DOGE | DOGE/BTC | 0.00000109 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -11,44% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -1,58%; 30g -8,63%; 90g +7,25%; 180g -14,42%
- **Daily:** RSI 39.20; MA50 0.00117821; MA200 0.00120600
- **Weekly:** MA30 0.00120962; RSI 43.67
- **Livelli:** supporto 0.00114600; resistenza 0.00116300; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 61.8% a 0.00113888
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +2,44%; 30g -11,44%; 90g -21,47%; 180g -17,77%
- **Daily:** RSI 34.49; MA50 0.00000120; MA200 0.00000133
- **Weekly:** MA30 0.00000132; RSI 29.88
- **Livelli:** supporto 0.00000104; resistenza 0.00000121; breakout 60g 0.00000153; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 202 | 51,98% | +1,96% | -1,34% |
| SOL | 30g | 201 | 47,76% | +4,73% | +0,36% |
| SOL | 90g | 195 | 53,85% | +10,36% | +1,62% |
| DOGE | 7g | 292 | 55,82% | +1,85% | -1,73% |
| DOGE | 30g | 288 | 52,78% | +2,01% | -3,71% |
| DOGE | 90g | 285 | 54,04% | +6,94% | -8,47% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 6 | 66,67% | -0,09% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 4 | 75,00% | +0,41% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 1 | 100,00% | +0,91% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 20 | 85,00% | +0,65% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 18 | 72,22% | +1,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 14 | 85,71% | +2,28% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 7 | 100,00% | +3,90% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
