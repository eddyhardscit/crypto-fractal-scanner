# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-08-22 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00121330 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +2,91% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000117 | 0 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +6,00% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

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
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +1,45%; 30g +2,91%; 90g +8,62%; 180g -0,87%
- **Daily:** RSI 58.09; MA50 0.00119115; MA200 0.00117787
- **Weekly:** MA30 0.00118304; RSI 49.60
- **Livelli:** supporto 0.00119400; resistenza 0.00134900; breakout 60g 0.00134900; breakdown 60g 0.00108800
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00112700; target 0.00107050
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (0)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +5,25%; 30g +6,00%; 90g -12,90%; 180g -17,07%
- **Daily:** RSI 64.16; MA50 0.00000112; MA200 0.00000129
- **Weekly:** MA30 0.00000129; RSI 40.06
- **Livelli:** supporto 0.00000116; resistenza 0.00000121; breakout 60g 0.00000139; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000126
- **Fibonacci:** NON ATTIVO — 38.2% a 0.00000120
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 204 | 51,96% | +1,94% | -1,18% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 198 | 53,03% | +10,08% | +2,72% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 291 | 53,26% | +2,05% | -3,93% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 18 | 61,11% | -0,24% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 17 | 47,06% | -0,54% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 16 | 43,75% | -1,32% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 15 | 6,67% | -3,44% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 35 | 68,57% | +0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 34 | 61,76% | +0,57% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 34 | 64,71% | +0,58% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 29 | 72,41% | +0,82% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 13 | 84,62% | +1,88% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
