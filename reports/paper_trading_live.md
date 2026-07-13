# Paper trading automatico KuCoin

Generato: 2026-07-13T01:07:34+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-13T01:07:30+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-13T01:07:30+00:00 | 2026-07-13T01:07:30+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-13T00:45:00+00:00 | 2026-07-13T00:45:00+00:00 | 22,5 min | 40,0 min | OK |
| 60m | 12 | 2026-07-13T00:00:00+00:00 | 2026-07-13T00:00:00+00:00 | 1,13 h | 1,42 h | OK |
| 240m | 12 | 2026-07-12T20:00:00+00:00 | 2026-07-12T20:00:00+00:00 | 5,13 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | T | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | DOGE | 240m | SHORT | -7,81 | 6,00 | 0,00 | STALE_CANDLE | 5,13 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -7,25 | 6,00 | 0,00 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | XRP | 240m | SHORT | -7,17 | 6,00 | 0,00 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 6,95 | 6,00 | 0,00 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 6,34 | 6,00 | 0,00 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -5,96 | 6,00 | 0,04 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | SOL | 240m | SHORT | -3,44 | 6,00 | 2,56 | STALE_CANDLE | 5,13 h | D: Conferma rialzista [CONTESTO] | W: Hidden bearish [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | BTC | 240m | LONG | 3,17 | 6,00 | 2,83 | STALE_CANDLE | 5,13 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Principale 4H | HYPE | 240m | SHORT | -1,24 | 6,00 | 4,76 | STALE_CANDLE | 5,13 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 307.5 minuti; limite 265. |
| Rapida 1H | T | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 1,13 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H | ADA | 60m | SHORT | -6,65 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.99%. |
| Forza relativa 1H | ADA | 60m | SHORT | -6,65 | 4,00 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-1.98%. |
| Rapida 1H | XRP | 60m | SHORT | -6,40 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.72%. |
| Forza relativa 1H | XRP | 60m | SHORT | -6,40 | 4,00 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.74%. |
| Rapida 1H | ETH | 60m | LONG | 5,95 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.28%. |
| Rapida 1H | PEPE | 60m | LONG | 5,28 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.61%. |
| Rapida 1H | DOGE | 60m | SHORT | -4,72 | 4,50 | 0,00 | STRATEGY_FILTER | 1,13 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.31%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.000,00 | 0,00% | €0,00 | €3.000,00 | 0,00% | 0 | 0 | 0,00% | 0,00 | 0,00% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 0 | 0 | CAMPIONE INSUFFICIENTE | 30 (mancano 30) |

- Trade del Principale 4H chiusi: **0**; win rate **0,00%**; profit factor **0,00**.
- Expectancy: **€0,00** per trade; P&L netto: **€0,00**; max drawdown: **0,00%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H | 3 | €10.033,49 | €1.278,88 | €3.836,65 | €100,16 | €44,30 |
| TEST | Bilanciata 1H | 4 | €10.032,18 | €1.620,10 | €4.860,29 | €150,20 | €4,94 |
| TEST | Forza relativa 1H | 4 | €10.029,32 | €2.429,88 | €4.859,76 | €150,18 | €4,95 |
| TEST | Ampia 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long prudente 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short prudente 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H | Confluenza trend | Test bilanciato a 1 ora basato sulla confluenza di trend. |
| TEST | Rapida 1H | Momentum / breakout | Test rapido a 1 ora che cerca momentum e breakout. |
| TEST | Ampia 4H | Confluenza trend | Test a 4 ore con stop più ampio, leva inferiore e durata maggiore. |
| TEST | Forza relativa 1H | Forza relativa vs BTC | Test a 1 ora che seleziona forza o debolezza rispetto a Bitcoin. |
| TEST | Scalp RSI Long €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m dopo capitolazione RSI confermata; margine fisso €10 e leva paper 15x. |
| TEST | Scalp RSI Long €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m sullo stesso segnale; margine fisso €50 e leva paper 15x. |
| TEST | Scalp RSI Long prudente 5x | Inversione RSI estrema 15m | Versione prudente long dello scalp RSI 15m, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m dopo euforia RSI confermata; margine fisso €10 e leva paper 15x. |
| TEST | Scalp RSI Short €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m sullo stesso segnale; margine fisso €50 e leva paper 15x. |
| TEST | Scalp RSI Short prudente 5x | Inversione RSI estrema 15m | Versione prudente short dello scalp RSI 15m, leva 5x e rischio ridotto. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Rapida 1H | Momentum / breakout | €10.033,49 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,58% |
| TEST | Bilanciata 1H | Confluenza trend | €10.032,18 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,43% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.029,32 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,43% |
| TEST | Ampia 4H | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long prudente 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short prudente 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,47334 | 0,42254 | 0,46866 | n/a | 0,35973 | €138,83 | €416,49 | €0,00 | €44,70 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00543 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €2,33 |
| Bilanciata 1H | ZEC | LONG | Confluenza trend | 60m | 3,0x | 544,28884 | 531,94000 | 529,54245 | 365,58067 | 573,78162 | €618,44 | €1.855,31 | €50,27 | €-42,09 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,47334 | 0,42254 | 0,45897 | n/a | 0,38813 | €138,81 | €416,44 | €0,00 | €44,69 |
| Rapida 1H | T | LONG | Momentum / breakout | 60m | 3,0x | 0,00544 | 0,00543 | 0,00502 | 0,00365 | 0,00606 | €218,67 | €656,00 | €50,17 | €-0,39 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | LAB | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,47334 | 0,42254 | 0,47334 | n/a | 0,34837 | €208,25 | €416,49 | €0,00 | €44,70 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00543 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €2,33 |
| Forza relativa 1H | ZEC | LONG | Forza relativa vs BTC | 60m | 2,0x | 544,28884 | 531,94000 | 529,54245 | 274,86586 | 576,73089 | €927,39 | €1.854,78 | €50,25 | €-42,08 |

## Ultime operazioni chiuse

_Nessuna operazione virtuale chiusa._

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🔬 Research All Signals

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **74,70%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +1.48%, 55% oltre +1%.
- BTC trend score: **1,00**; ADX: **15,02**; breadth sopra EMA50: **58,33%**
- Mediana alt vs BTC: **1,48%**; dispersione: **57,73%**

- Aperti in questo ciclo: **15**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **15**
- Trade research chiusi: **0**
- Eventi di mercato indipendenti chiusi: **0**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **0**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SHADOW_1H_BALANCED | 7 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 7 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
