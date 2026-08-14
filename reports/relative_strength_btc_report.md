# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-08-14 10:53 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00120050 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +0,54% | RIBASSISTA | FORZA RELATIVA NASCOSTA: debole in USD ma migliore di BTC |
| DOGE | DOGE/BTC | 0.00000111 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | -3,36% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+4)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NASCOSTA: debole in USD ma migliore di BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +5,77%; 30g +0,54%; 90g +8,35%; 180g -3,96%
- **Daily:** RSI 59.83; MA50 0.00119685; MA200 0.00118389
- **Weekly:** MA30 0.00118882; RSI 48.33
- **Livelli:** supporto 0.00119400; resistenza 0.00125100; breakout 60g 0.00134900; breakdown 60g 0.00102800
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00113300; target 0.00108600
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g +3,05%; 30g -3,36%; 90g -21,00%; 180g -25,90%
- **Daily:** RSI 48.80; MA50 0.00000114; MA200 0.00000130
- **Weekly:** MA30 0.00000130; RSI 33.23
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000146; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 204 | 51,96% | +1,94% | -1,18% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 197 | 53,30% | +10,17% | +2,42% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 290 | 53,10% | +2,05% | -3,94% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 15 | 66,67% | -0,23% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 15 | 46,67% | -0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 14 | 42,86% | -1,33% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 7 | 14,29% | -2,36% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 32 | 68,75% | +0,28% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 32 | 59,38% | +0,50% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 28 | 75,00% | +1,31% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 21 | 76,19% | +1,85% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 5 | 100,00% | +3,99% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
