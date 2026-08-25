# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-08-25 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00127300 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +10,03% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000115 | -2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +3,25% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

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
- **Rendimenti relativi:** 7g +8,06%; 30g +10,03%; 90g +15,52%; 180g -1,55%
- **Daily:** RSI 69.33; MA50 0.00118740; MA200 0.00117740
- **Weekly:** MA30 0.00118227; RSI 54.72
- **Livelli:** supporto 0.00122200; resistenza 0.00134900; breakout 60g 0.00134900; breakdown 60g 0.00109300
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00126876
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +5,52%; 30g +3,25%; 90g -13,53%; 180g -22,37%
- **Daily:** RSI 55.57; MA50 0.00000112; MA200 0.00000129
- **Weekly:** MA30 0.00000128; RSI 39.64
- **Livelli:** supporto 0.00000112; resistenza 0.00000115; breakout 60g 0.00000135; breakdown 60g 0.00000100
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 205 | 52,20% | +1,94% | -1,06% |
| SOL | 30g | 203 | 47,29% | +4,59% | +0,36% |
| SOL | 90g | 198 | 53,03% | +10,08% | +2,72% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 292 | 53,08% | +2,00% | -3,71% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 21 | 66,67% | +0,18% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 19 | 52,63% | -0,18% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 16 | 37,50% | -1,41% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 15 | 6,67% | -3,37% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 3 | 0,00% | -8,42% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 35 | 68,57% | +0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 35 | 60,00% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 34 | 64,71% | +0,52% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 32 | 65,62% | -0,06% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 16 | 68,75% | +0,10% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
