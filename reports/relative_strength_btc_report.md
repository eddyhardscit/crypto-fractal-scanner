# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-09-13 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00131760 | +3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +9,71% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000110 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -0,67% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (+3)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g +1,90%; 30g +9,71%; 90g +21,66%; 180g +2,54%
- **Daily:** RSI 58.46; MA50 0.00122683; MA200 0.00118426
- **Weekly:** MA30 0.00118869; RSI 57.74
- **Livelli:** supporto 0.00127500; resistenza 0.00133900; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -2,27%; 30g -0,67%; 90g -18,72%; 180g -20,30%
- **Daily:** RSI 48.83; MA50 0.00000110; MA200 0.00000126
- **Weekly:** MA30 0.00000126; RSI 39.14
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 208 | 52,40% | +1,95% | -1,06% |
| SOL | 30g | 204 | 47,06% | +4,50% | +0,44% |
| SOL | 90g | 200 | 52,50% | +9,74% | +3,06% |
| DOGE | 7g | 295 | 55,59% | +1,83% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 35 | 54,29% | +0,10% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 35 | 54,29% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 32 | 46,88% | +0,76% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 27 | 37,04% | +0,08% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 16 | 6,25% | -11,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 49 | 65,31% | -0,11% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 47 | 55,32% | -0,14% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 46 | 54,35% | -0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 40 | 65,00% | +0,18% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 33 | 66,67% | +0,25% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
