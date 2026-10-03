# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-10-03 05:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00141290 | +5 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +8,85% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000110 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | +4,28% | RIALZISTA | SALE SOLO IN USD: BTC resta più forte |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+5)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -2,63%; 30g +8,85%; 90g +9,19%; 180g +19,03%
- **Daily:** RSI 59.58; MA50 0.00131248; MA200 0.00119667
- **Weekly:** MA30 0.00120433; RSI 62.10
- **Livelli:** supporto 0.00127800; resistenza 0.00146600; breakout 60g 0.00146600; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00135815
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** SALE SOLO IN USD: BTC resta più forte
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -6,47%; 30g +4,28%; 90g -10,45%; 180g -17,66%
- **Daily:** RSI 47.50; MA50 0.00000111; MA200 0.00000123
- **Weekly:** MA30 0.00000123; RSI 41.35
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 210 | 52,86% | +1,98% | -1,04% |
| SOL | 30g | 207 | 47,83% | +4,57% | +0,63% |
| SOL | 90g | 202 | 52,97% | +9,80% | +3,12% |
| DOGE | 7g | 296 | 55,41% | +1,80% | -1,66% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 289 | 54,33% | +6,90% | -9,23% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 45 | 53,33% | +0,27% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 44 | 52,27% | +0,70% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 40 | 47,50% | +0,73% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 35 | 45,71% | +0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 31 | 51,61% | -0,79% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 54 | 66,67% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 54 | 57,41% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 54 | 53,70% | -0,56% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 54 | 50,00% | -0,66% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 44 | 52,27% | -0,64% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
