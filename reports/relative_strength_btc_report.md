# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-10-26 06:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00126280 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -12,97% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000096 | -7 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -18,50% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -0,41%; 30g -12,97%; 90g +8,49%; 180g +14,70%
- **Daily:** RSI 33.10; MA50 0.00133838; MA200 0.00120564
- **Weekly:** MA30 0.00120969; RSI 49.09
- **Livelli:** supporto 0.00124400; resistenza 0.00129400; breakout 60g 0.00146600; breakdown 60g 0.00118000
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** VICINO — 50.0% a 0.00124300
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in salita; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-7)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -0,78%; 30g -18,50%; 90g -13,05%; 180g -26,27%
- **Daily:** RSI 30.99; MA50 0.00000107; MA200 0.00000119
- **Weekly:** MA30 0.00000118; RSI 34.00
- **Livelli:** supporto 0.00000092; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000092
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000105
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 212 | 52,36% | +1,92% | -1,06% |
| SOL | 30g | 210 | 47,62% | +4,51% | +0,58% |
| SOL | 90g | 203 | 52,71% | +9,70% | +3,16% |
| DOGE | 7g | 298 | 55,70% | +1,81% | -1,68% |
| DOGE | 30g | 296 | 53,04% | +1,98% | -3,49% |
| DOGE | 90g | 292 | 54,79% | +6,92% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 52 | 48,08% | -0,01% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 52 | 44,23% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 52 | 36,54% | -0,67% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 52 | 34,62% | -1,85% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 40 | 50,00% | -1,25% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 74 | 64,86% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 72 | 65,28% | +0,52% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 68 | 63,24% | +0,45% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 62 | 56,45% | +0,56% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 54 | 57,41% | +0,39% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
