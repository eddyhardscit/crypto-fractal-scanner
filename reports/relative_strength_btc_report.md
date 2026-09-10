# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-09-10 05:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00130020 | +3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +9,44% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000110 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | +0,43% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

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
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +0,17%; 30g +9,44%; 90g +23,71%; 180g +4,69%
- **Daily:** RSI 56.48; MA50 0.00121818; MA200 0.00118292
- **Weekly:** MA30 0.00118811; RSI 55.98
- **Livelli:** supporto 0.00127500; resistenza 0.00134900; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +3,69%; 30g +0,43%; 90g -19,04%; 180g -19,00%
- **Daily:** RSI 47.89; MA50 0.00000110; MA200 0.00000126
- **Weekly:** MA30 0.00000126; RSI 38.99
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 207 | 52,17% | +1,95% | -1,06% |
| SOL | 30g | 204 | 47,06% | +4,50% | +0,44% |
| SOL | 90g | 199 | 52,76% | +9,91% | +3,03% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 35 | 54,29% | +0,13% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 33 | 54,55% | +0,50% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 31 | 48,39% | +0,70% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 24 | 41,67% | +0,31% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 15 | 0,00% | -12,60% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 46 | 67,39% | -0,10% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 46 | 56,52% | -0,14% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 44 | 56,82% | -0,16% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 37 | 70,27% | +0,19% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 32 | 62,50% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
