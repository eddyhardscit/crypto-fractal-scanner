# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-07-11 17:36 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00121300 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +15,41% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000117 | -8 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -13,66% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-1)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -6,26%; 30g +15,41%; 90g +5,20%; 180g -20,51%
- **Daily:** RSI 51.30; MA50 0.00114612; MA200 0.00123260
- **Weekly:** MA30 0.00123683; RSI 48.17
- **Livelli:** supporto 0.00119400; resistenza 0.00125100; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / CONFERMATO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-8)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -5,04%; 30g -13,66%; 90g -9,03%; 180g -22,00%
- **Daily:** RSI 31.24; MA50 0.00000130; MA200 0.00000136
- **Weekly:** MA30 0.00000136; RSI 33.41
- **Livelli:** supporto 0.00000116; resistenza 0.00000128; breakout 60g 0.00000153; breakdown 60g 0.00000112
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000124; target 0.00000098
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000124
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 202 | 51,98% | +1,97% | -1,34% |
| SOL | 30g | 199 | 48,24% | +4,85% | +0,36% |
| SOL | 90g | 193 | 54,40% | +10,50% | +0,53% |
| DOGE | 7g | 289 | 55,71% | +1,85% | -1,77% |
| DOGE | 30g | 286 | 52,45% | +1,93% | -3,49% |
| DOGE | 90g | 283 | 53,71% | +6,91% | -8,20% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
