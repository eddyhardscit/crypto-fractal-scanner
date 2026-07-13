<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-13 06:28 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +5 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | -5 | BEARISH | STAI FUORI / VENDI PARZIALE | NO LONG A LEVA | SHORT SOLO DOPO ROTTURA | nessuna | max 1x-2x isolated | MOLTO ALTO |
| DOGE | -7 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+5**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **-5**, spot = **STAI FUORI / VENDI PARZIALE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO ROTTURA**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-7**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+5**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Global Confluence: **-5**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot dal Global: **STAI FUORI / VENDI PARZIALE**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO ROTTURA**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo confermato recente finché mantiene 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 82,66 / 114,44, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 72,48 / 64,42 / 62,19.

### DOGE

- Global Confluence: **-7**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot dal Global: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.07107 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 113,13 $; upside verso EMA200 +48,14%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-07-13T06:28:58+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-13T04:49:50+00:00**; stato dati: **UNKNOWN**; età: **n/a**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| UNKNOWN | n/a | 2026-07-13T04:49:50+00:00 | n/a | n/a | n/a | BLOCCATE |

> ⚠️ I prezzi non vengono marcati come aggiornati artificialmente. Se KuCoin non risponde e viene usata la cache, il report mostra l'età reale e blocca le nuove entrate.

## Segnali quasi entrati / motivi di esclusione

_Diagnostica non ancora disponibile: verrà creata alla prossima esecuzione del Paper Trading._

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
| TEST | Ampia 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long prudente 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short prudente 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H | 3 | €9.988,78 | €1.001,66 | €3.004,98 | €99,93 | €13,01 |
| TEST | Forza relativa 1H | 3 | €9.985,92 | €1.502,49 | €3.004,98 | €99,93 | €13,01 |
| TEST | Rapida 1H | 3 | €9.983,81 | €1.278,88 | €3.836,65 | €100,16 | €-5,38 |

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
| TEST | Ampia 4H | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long prudente 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short prudente 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Bilanciata 1H | Confluenza trend | €9.988,78 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,86% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €9.985,92 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,86% |
| TEST | Rapida 1H | Momentum / breakout | €9.983,81 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 1,07% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,47334 | 0,42468 | 0,46866 | n/a | 0,35973 | €138,83 | €416,49 | €0,00 | €42,81 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00504 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €-29,80 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,47334 | 0,42468 | 0,45897 | n/a | 0,38813 | €138,81 | €416,44 | €0,00 | €42,81 |
| Rapida 1H | T | LONG | Momentum / breakout | 60m | 3,0x | 0,00544 | 0,00504 | 0,00502 | 0,00365 | 0,00606 | €218,67 | €656,00 | €50,17 | €-48,19 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | LAB | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,47334 | 0,42468 | 0,47334 | n/a | 0,34837 | €208,25 | €416,49 | €0,00 | €42,81 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00504 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €-29,80 |

## Ultime operazioni chiuse

_Nessuna operazione virtuale chiusa._

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
<!-- PAPER_TRADING_END -->

</details>
<!-- COMPACT_SECTION_END:decision -->

<!-- COMPACT_SECTION_START:module_accuracy -->
<details>
<summary><strong>🧪 Accuratezza moduli e raccolta dati</strong></summary>

<!-- MODULE_ACCURACY_START -->
# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-13 06:28 UTC

Questo report salva ogni giorno i segnali dei moduli e controlla ogni giorno quali orizzonti sono maturati.

La calibrazione ora controlla questi orizzonti:

- **1g / 2g / 3g** = feedback rapidissimo
- **5g / 7g / 10g** = feedback settimanale
- **14g / 21g** = feedback swing
- **30g / 45g / 60g** = feedback più serio

Moduli controllati:

- Global Confluence = benchmark dell'aggregato finale
- **Famiglia statistica Scanner + Market Regime = modulo calibrabile reale**
- Scanner grezzo = diagnostico, già incluso nella famiglia statistica
- Market Regime grezzo = diagnostico, già incluso nella famiglia statistica
- Struttura tecnica
- Classic technical confirmation
- Microstruttura exchange, OI/funding/taker flow/order book
- Frattale SOL/BTC, solo per SOL

Regola anti-doppio-conteggio: **Scanner e Market Regime continuano a essere misurati separatamente solo per diagnosi, ma non devono ricevere due modifiche di peso autonome**. La calibrazione dei pesi deve agire sulla Famiglia statistica.

Nota: i controlli vengono aggiornati **ogni giorno**, ma i pesi del Global non devono cambiare automaticamente sotto 30 controlli. Prima si osserva, poi si calibra.

Segnali totali salvati: **15**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | BTC | 62.759,92 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-13 | DOGE | 0.07220 | -7 | -4 | -3 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-13 | SOL | 76,37 | -5 | -3 | -2 | -1 | -2 | 0 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-12 | BTC | 63.818,10 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-12 | DOGE | 0.07283 | -7 | -4 | -3 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-12 | SOL | 76,48 | -2 | -2 | -1 | -1 | +1 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-11 | BTC | 64.040,99 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-11 | DOGE | 0.07401 | -8 | -4 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-11 | SOL | 77,80 | +1 | 0 | -1 | +1 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-10 | BTC | 63.864,39 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-10 | DOGE | 0.07388 | -8 | -4 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-10 | SOL | 77,70 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 5 | 4 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 5 | 4 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 5 | 4 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 5g | 2026-07-14 | domani |
| SOL | 2026-07-09 | 5g | 2026-07-14 | domani |
| DOGE | 2026-07-09 | 5g | 2026-07-14 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 4 | 25,00% | -0,51% | -0,51% | FEEDBACK RAPIDO |
| BTC | 2g | 3 | 33,33% | -0,27% | -0,27% | FEEDBACK RAPIDO |
| BTC | 3g | 2 | 50,00% | -0,40% | -0,40% | FEEDBACK RAPIDO |
| BTC | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 3 | 33,33% | -0,65% | -0,55% | FEEDBACK RAPIDO |
| SOL | 2g | 2 | 0,00% | -1,06% | -1,06% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | 0,00% | -1,97% | -1,97% | FEEDBACK RAPIDO |
| SOL | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | 75,00% | -0,60% | +0,60% | FEEDBACK RAPIDO |
| DOGE | 2g | 3 | 66,67% | -0,76% | +0,76% | FEEDBACK RAPIDO |
| DOGE | 3g | 2 | 100,00% | -1,15% | +1,15% | FEEDBACK RAPIDO |
| DOGE | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 4 | 25,00% | -0,51% | -0,51% | -0,67% | +0,30% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 4 | 25,00% | -0,51% | -0,51% | -0,67% | +0,30% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 4 | 25,00% | -0,51% | -0,51% | -0,67% | +0,30% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 4 | 25,00% | -0,51% | -0,51% | -0,67% | +0,30% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 3 | 66,67% | -0,77% | -0,33% | -0,97% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 3 | 33,33% | -0,27% | -0,27% | -0,47% | +0,88% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 3 | 33,33% | -0,27% | -0,27% | -0,47% | +0,88% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 3 | 33,33% | -0,27% | -0,27% | -0,47% | +0,88% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -0,27% | -0,27% | -0,47% | +0,88% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 2 | 50,00% | -0,36% | +0,36% | -0,52% | +0,87% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 2 | 50,00% | -0,40% | -0,40% | -1,26% | +1,58% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 2 | 50,00% | -0,40% | -0,40% | -1,26% | +1,58% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 2 | 50,00% | -0,40% | -0,40% | -1,26% | +1,58% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 2 | 50,00% | -0,40% | -0,40% | -1,26% | +1,58% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 1 | 0,00% | +0,92% | -0,92% | -0,53% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 4 | 75,00% | -0,60% | +0,60% | -0,89% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -0,60% | +0,60% | -0,89% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 4 | 75,00% | -0,60% | +0,60% | -0,89% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 4 | 75,00% | -0,60% | +0,60% | -0,89% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 4 | 75,00% | -0,60% | +0,60% | -0,89% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 4 | 75,00% | -0,60% | +0,60% | -0,89% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 3 | 66,67% | -0,76% | +0,76% | -1,14% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 3 | 66,67% | -0,76% | +0,76% | -1,14% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 3 | 66,67% | -0,76% | +0,76% | -1,14% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 3 | 66,67% | -0,76% | +0,76% | -1,14% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 3 | 66,67% | -0,76% | +0,76% | -1,14% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 3 | 66,67% | -0,76% | +0,76% | -1,14% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 2 | 100,00% | -1,15% | +1,15% | -1,67% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -1,15% | +1,15% | -1,67% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -1,15% | +1,15% | -1,67% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | -1,15% | +1,15% | -1,67% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 2 | 100,00% | -1,15% | +1,15% | -1,67% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 2 | 100,00% | -1,15% | +1,15% | -1,67% | +2,87% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 3 | 33,33% | -0,65% | -0,55% | -1,25% | +0,29% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 3 | 66,67% | -0,04% | +0,04% | -0,40% | +0,80% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 4 | 75,00% | -0,45% | +0,45% | -0,92% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -0,65% | -0,55% | -1,25% | +0,29% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 4 | 25,00% | -0,45% | -0,45% | -0,92% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 2 | 0,00% | -1,06% | -1,06% | -1,54% | +0,11% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -0,93% | +0,93% | -1,33% | +0,68% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -1,23% | +1,23% | -1,81% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | -1,06% | -1,06% | -1,54% | +0,11% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 3 | 0,00% | -1,23% | -1,23% | -1,81% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -1,84% | +1,84% | -2,69% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -1,84% | +1,84% | -2,69% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 2 | 0,00% | -1,84% | -1,84% | -2,69% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |

## Come leggerlo

- **CALIBRABILE** = modulo reale sul quale, con dati maturi, si può valutare una modifica di peso.
- **DIAGNOSTICO** = resta misurato, ma è già incluso in una famiglia e il suo peso separato deve restare 0.
- **BENCHMARK** = risultato complessivo del Global; serve per confrontare l'aggregato, non è un peso interno.
- **Controlli** = segnali non neutrali già verificati su quell'orizzonte.
- **Accuratezza direzione** = quante volte un segnale positivo ha avuto return positivo o un segnale negativo ha avuto return negativo.
- **Return medio** = rendimento reale medio dell'asset su quell'orizzonte.
- **Return corretto direzione** = return visto dal lato del modulo: se il modulo era ribassista, un calo conta positivo.
- **Drawdown medio** = peggior discesa media durante l'orizzonte.
- **Max gain medio** = massimo rialzo medio durante l'orizzonte.

Regole operative:

- Sotto **30 controlli**: solo osservazione, nessuna modifica ai pesi.
- Da **30 controlli**: possibile calibrazione leggera.
- Da **60 controlli**: lettura più utile.
- Da **100+ controlli**: possibile revisione più seria dei pesi.

Questo report non cambia ancora automaticamente i pesi del Global Confluence. Produce però i metadati `calibratable` e `calibration_role`, così il report di calibrazione può escludere Scanner e Market dalle proposte di peso separate.

Nota tecnica: le colonne data sono forzate come testo, quindi non deve più apparire l'errore `Invalid value 'YYYY-MM-DD' for dtype 'float64'`.
<!-- MODULE_ACCURACY_END -->

</details>
<!-- COMPACT_SECTION_END:module_accuracy -->

<!-- COMPACT_SECTION_START:global_weight_calibration -->
<details>
<summary><strong>⚖️ Calibrazione pesi Global Confluence</strong></summary>

<!-- GLOBAL_WEIGHT_CALIBRATION_START -->
# Calibrazione pesi Global Confluence

Generato: 2026-07-13 06:28 UTC

Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)

Questo blocco controlla se, col tempo, i moduli reali del Global Confluence meritano più peso, meno peso o peso invariato.

Correzione anti-doppio-conteggio: **la Famiglia statistica Scanner + Market Regime è il modulo calibrabile**. Scanner grezzo e Market Regime grezzo restano visibili solo come diagnostica e non ricevono proposte di peso separate.

Regola principale:

- sotto **30 controlli**: osservazione, nessuna modifica pesi
- da **30 controlli**: prima calibrazione leggera
- da **60 controlli**: lettura utile
- da **100+ controlli**: possibile proposta prudente di modifica pesi

Il file continua a produrre solo raccomandazioni: **non modifica automaticamente** `global_confluence_report.py`.

## Sintesi per asset

| Asset | Segnali salvati | Stato | Controlli max | Righe 30+ | Righe 60+ | Righe 100+ | Miglior modulo calibrabile | Orizzonte | Accuratezza | Return corretto direzione | Lettura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 5 | FEEDBACK RAPIDO | 4 | 0 | 0 | 0 | Famiglia statistica | 1g | 25,00% | -0,51% | feedback rapido: utile da osservare, non da pesare |
| SOL | 5 | FEEDBACK RAPIDO | 4 | 0 | 0 | 0 | Tecnico | 1g | 25,00% | -0,45% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 5 | FEEDBACK RAPIDO | 4 | 0 | 0 | 0 | Famiglia statistica | 1g | 75,00% | +0,60% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 4 | 25,00% | -0,51% | -0,51% | -0,67% | +0,30% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 3 | 66,67% | -0,33% | -0,77% | -0,97% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 3 | 33,33% | -0,27% | -0,27% | -0,47% | +0,88% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 2 | 50,00% | +0,36% | -0,36% | -0,52% | +0,87% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 2 | 50,00% | -0,40% | -0,40% | -1,26% | +1,58% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 1 | 0,00% | -0,92% | +0,92% | -0,53% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 4 | 75,00% | +0,60% | -0,60% | -0,89% | +0,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 4 | 75,00% | +0,60% | -0,60% | -0,89% | +0,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 4 | 75,00% | +0,60% | -0,60% | -0,89% | +0,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 3 | 66,67% | +0,76% | -0,76% | -1,14% | +1,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 3 | 66,67% | +0,76% | -0,76% | -1,14% | +1,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 3 | 66,67% | +0,76% | -0,76% | -1,14% | +1,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 2 | 100,00% | +1,15% | -1,15% | -1,67% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 2 | 100,00% | +1,15% | -1,15% | -1,67% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 2 | 100,00% | +1,15% | -1,15% | -1,67% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 3 | 66,67% | +0,04% | -0,04% | -0,40% | +0,80% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 4 | 25,00% | -0,45% | -0,45% | -0,92% | +0,33% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 2 | 100,00% | +0,93% | -0,93% | -1,33% | +0,68% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 3 | 0,00% | -1,23% | -1,23% | -1,81% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 2 | 100,00% | +1,84% | -1,84% | -2,69% | +1,64% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 2 | 0,00% | -1,84% | -1,84% | -2,69% | +1,64% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 4 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 4 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 4 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 9 | 33,33% | -0,41% |
| BTC | BREVE | Tecnico | 6 | 50,00% | -0,20% |
| DOGE | BREVE | Classic technical | 9 | 77,78% | +0,77% |
| DOGE | BREVE | Famiglia statistica | 9 | 77,78% | +0,77% |
| DOGE | BREVE | Tecnico | 9 | 77,78% | +0,77% |
| SOL | BREVE | Famiglia statistica | 7 | 85,71% | +0,81% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 9 | 11,11% | -1,02% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 15 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 6 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 15 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 15 | in attesa di controlli maturati |
| DOGE | SWING | 10 | in attesa di controlli maturati |
| DOGE | MEDIO | 15 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

Siamo ancora in feedback rapido. Non bisogna modificare i pesi del Global. La nuova struttura serve ad accumulare dati corretti senza doppio conteggio.
<!-- GLOBAL_WEIGHT_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:global_weight_calibration -->

<!-- COMPACT_SECTION_START:risk_calibration -->
<details>
<summary><strong>🛡️ Calibrazione rischio spot / leva</strong></summary>

<!-- RISK_CALIBRATION_START -->
# Calibrazione rischio spot / leva

Report completo: [risk_calibration_report.md](risk_calibration_report.md)

Questo blocco controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio   |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:---------------|
| BTC     |          5 |               0 |           5 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |          5 |               0 |           5 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |          5 |               0 |           5 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | ALTO           | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-13 06:28 UTC

Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.

Moduli letti:

- Famiglia statistica Scanner + Market Regime, conteggiata una sola volta
- Scanner path / cono previsionale
- Struttura tecnica classica precedente
- Classic technical confirmation, filtro tecnico completo
- Frattale BTC 2022 vs SOL 2026, solo per SOL
- Fractal path tracker, solo per SOL
- RSI top-cycle, soprattutto per SOL
- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL
- Exchange microstructure: OI, funding, taker flow, order book e liquidazioni campionate
- Futures / liquidazioni precedente, mantenuto come diagnostica
- Cambiamento giornaliero

Nota statistica: **Scanner e Market Regime non vengono più sommati come due prove indipendenti**. Lo Scanner è il punteggio principale; il Market Regime può aggiungere al massimo 1 punto di conferma con almeno 10 match. La famiglia statistica è limitata a ±4.

Nota importante: **Lifecycle EMA200 viene letto e mostrato, ma vale sempre 0 punti nel Global Confluence**. Serve come contesto, non come conferma operativa.

Nota Classic technical: **pesa massimo ±1** perché è un filtro di conferma e in parte si sovrappone alla struttura tecnica già esistente.

Nota exchange: **candidato massimo ±1, peso iniziale 0** e più conferme indipendenti. Order book, funding o una singola liquidazione non bastano da soli.

## Sintesi operativa

| Asset | Punteggio | Confluenza | Bias | Affidabilità | Azione coerente | Conferme | Invalidazioni |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | -5 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE | Doppio minimo confermato recente finché mantiene 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 82,66 / 114,44, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 72,48 / 64,42 / 62,19. |
| DOGE | -7 | NEGATIVA | Ribassista | MEDIA / ALTA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.07107 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +3 | +4 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +5 |
| SOL | -2 | -1 | -3 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -5 |
| DOGE | -3 | -3 | -4 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -7 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 12. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +8,25%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 12, positivi 30g 100,00%, return p50 +20,68%.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 3. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Tecnico: **+1** — Score tecnico 1/12, verdetto neutrale / misto, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza rialzista rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / TARGET RAGGIUNTO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -1/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SPRING / TEST POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 2 su 3.78h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in misto rispetto a ieri.

Conferme: Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-5**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE**

SOL è fragile nel breve. Il frattale da solo non basta: se non recupera le conferme e il gap non rientra, il rischio è di inseguire uno spike scaricato.

Dettaglio moduli:

- Famiglia statistica: **-3** — Scanner grezzo -2, Market Regime grezzo -1, match regime 18. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: -3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 35,00%, return centrale 30g -2,61%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **-1** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 18, positivi 30g 38,89%, return p50 -0,79%.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 3. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend ribassista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +64,96%, aderenza live +59,98%, errore live +20,01%, gap corrente +17,00%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Tracking operativo, ma nessuna milestone settimanale ancora verificata. Gap corrente +17,00%, errore live +20,01%. Il modulo non pesa finché non maturano abbastanza controlli.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 113,13 $, upside EMA200 +48,14%, gap EMA50/EMA200 -2,16%, hit EMA200 12w +23,33%, trend PEGGIORAMENTO. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 2 su 3.78h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Doppio minimo confermato recente finché mantiene 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 82,66 / 114,44, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 72,48 / 64,42 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-7**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **-4** — Scanner grezzo -3, Market Regime grezzo -3, match regime 30. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: -4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-3** — Casi positivi 17,50%, return centrale 30g -19,69%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **-3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 30, positivi 30g 13,33%, return p50 -22,23%.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 3. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Tecnico: **-2** — Score tecnico -5/12, verdetto debole, trend ribassista, struttura compressione / triangolo, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Triplo minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -9/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 2 su 3.78h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Leva alta, direzione mista, forza 3/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in misto rispetto a ieri.

Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.07107 il rischio ribassista aumenta.


## Come leggere il punteggio

- +7 o più: confluenza positiva forte.
- Da +3 a +6: confluenza moderatamente positiva.
- Da 0 a +2: confluenza parziale o mista.
- Da -1 a -3: confluenza debole o fragile.
- -4 o meno: confluenza negativa.

Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0.
Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero.

Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze resta nel report, ma pesa **0** nel Global perché EMA50/EMA200 e target EMA200 sono contesto, non conferme dirette di prezzo.

Nota Classic technical: il modulo è utile per capire se il setup è confermato davvero, ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente.

Nota exchange: il modulo salva OI, funding, taker flow, order book e liquidazioni campionate. Il candidato è limitato a ±1; il peso Global resta 0 finché il gate storico a 7 giorni non matura.
<!-- GLOBAL_CONFLUENCE_END -->

</details>
<!-- COMPACT_SECTION_END:global_confluence -->

<!-- COMPACT_SECTION_START:btc_macro_cycle -->
<details>
<summary><strong>🌀 Bitcoin Macro Cycle — Power Law e Spiral</strong></summary>

<!-- BTC_MACRO_CYCLE_START -->
# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-07-13 06:28 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 62.759 $ | prezzo corrente |
| Power Law centrale | 122.133 $ | deviazione -48,61% |
| Banda p10-p90 | 76.182 $ / 306.630 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 0,67% | posizione storica nel corridoio |
| Esponente β | 5,8463 | R² log-log 92,00% |
| Stabilità β | BASSA | range 1,3051 cambiando finestra |
| Ultimo halving | 2024-04-19 | 815 giorni fa |
| Fase ciclo | 55,78% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-13 (4318 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.4036) × giorni^5.8463
- Prezzo centrale oggi: **122.133 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 0,67%
- Scarto dal centro: **-48,61%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8463 | 92,00% |
| 2015 | 5,9335 | 91,57% |
| 2016 | 5,6242 | 87,81% |
| 2017 | 4,8936 | 82,89% |
| 2018 | 4,6284 | 78,36% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 79 | 26,58% | 55,14% | 20,89% |
| 180g | 79 | 40,51% | 60,84% | 45,16% |
| 365g | 79 | 56,96% | 73,12% | 81,57% |
| 730g | 79 | 59,49% | 72,50% | 109,89% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2014-12-04 | -23,95% | -26,11% | -38,91% | -1,74% |
| 2016-07-09 → 2020-05-11 | 2018-08-30 | -5,39% | -38,99% | -44,77% | +37,54% |
| 2020-05-11 → 2024-04-19 | 2022-07-23 | -4,75% | -14,66% | -6,14% | +33,91% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 14.003739665281433 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -8 | -1 | -15.657078270557435 | 0 |

## Tracker live Power Law

| Orizzonte | Controlli | Vittorie vs naive | Errore modello | Errore naive | Stato |
| --- | --- | --- | --- | --- | --- |
| 90g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 180g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 365g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |

Il modulo resta a peso 0 anche con un buon backtest. Prima si osserva la verifica live, poi si decide se usarlo soltanto per il rischio macro di lungo periodo. Le fotografie live della Power Law vengono salvate una sola volta per mese, così non si contano come indipendenti previsioni giornaliere quasi identiche.

## File prodotti

- `reports/btc_power_law_metrics.csv`
- `reports/btc_power_law_backtest.csv`
- `reports/btc_cycle_phase_metrics.csv`
- `reports/btc_macro_cycle_history.csv`
- `reports/btc_macro_cycle_tracker_metrics.csv`
<!-- BTC_MACRO_CYCLE_END -->

</details>
<!-- COMPACT_SECTION_END:btc_macro_cycle -->

<!-- COMPACT_SECTION_START:relative_strength_btc -->
<details>
<summary><strong>₿ Forza relativa SOL/BTC e DOGE/BTC</strong></summary>

<!-- RELATIVE_STRENGTH_BTC_START -->
# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-07-13 06:28 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00121870 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +14,00% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000115 | -8 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -15,66% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Rendimenti relativi:** 7g -4,79%; 30g +14,00%; 90g +7,95%; 180g -19,50%
- **Daily:** RSI 52.70; MA50 0.00114995; MA200 0.00123082
- **Weekly:** MA30 0.00122982; RSI 48.67
- **Livelli:** supporto 0.00119400; resistenza 0.00125100; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-8)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -3,87%; 30g -15,66%; 90g -8,25%; 180g -24,26%
- **Daily:** RSI 28.55; MA50 0.00000129; MA200 0.00000136
- **Weekly:** MA30 0.00000135; RSI 33.17
- **Livelli:** supporto 0.00000112; resistenza 0.00000128; breakout 60g 0.00000153; breakdown 60g 0.00000112
- **Pattern:** DOPPIO MASSIMO / TARGET RAGGIUNTO; neckline 0.00000131; target 0.00000113
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000124
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 202 | 51,98% | +1,96% | -1,34% |
| SOL | 30g | 200 | 48,00% | +4,75% | +0,44% |
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
| DOGE | 1g | 2 | 50,00% | +0,79% | LOCKED / RACCOLTA LIVE | 0 |
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
<!-- RELATIVE_STRENGTH_BTC_END -->

</details>
<!-- COMPACT_SECTION_END:relative_strength_btc -->

<!-- COMPACT_SECTION_START:btc_sol_fractal -->
<details>
<summary><strong>🧬 Frattale mirato BTC 2022 / SOL 2026</strong></summary>

<!-- BTC_SOL_FRACTAL_START -->

---

# Frattale mirato: BTC 2022 vs SOL 2026

Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)

Ultima candela SOL usata: **13 luglio 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +64,96%
- **Somiglianza strutturale:** +64,96%
- **Aderenza prezzo live:** +59,98%
- **Errore medio live:** +20,01%
- **Gap prezzo corrente:** +17,00%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 37 dal bottom usato.
- **Giorno BTC equivalente:** 2022-12-28
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **76,27 $** intorno al **16 luglio 2026**; zona alta **82,66 $** intorno al **27 luglio 2026**; fine step circa **82,66 $** entro il **27 luglio 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 13 luglio 2026 | 11 | +59,98% | +20,01% | +17,00% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 13 luglio 2026 | 38 | +79,85% | +10,07% | +17,00% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +59,98% | Errore medio live +20,01%. |
| Gap corrente | +17,00% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 82,66 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 114,44 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 72,48 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 574,98 $ |
| Massimo percorso base | 574,98 $ (21 aprile 2029) |

## Grafici

### Grafico frattale sovrapposto

![Frattale BTC 2022 vs SOL 2026](btc_2022_vs_sol_2026_fractal_chart.png)

### Grafico proiezione condizionale

![Proiezione SOL BTC 2022](btc_2022_vs_sol_2026_projection_chart.png)

### Grafico ciclo base

![Ciclo base SOL BTC 2025](btc_2022_vs_sol_2026_cycle_base_chart.png)

### Grafico struttura vs aderenza

![Tracking frattale BTC SOL](btc_2022_vs_sol_2026_tracking_chart.png)

## Livelli chiave

| Livello | Prezzo / soglia | Lettura |
| --- | --- | --- |
| Rientro gap | entro ±12% | Condizione necessaria per tornare operativo. |
| Prima conferma | 82,66 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 114,44 $ | Scenario più credibile. |
| Invalidazione soft | 72,48 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 20 luglio 2026 | +1,88% | 77,72 $ | 76,27 $ | 77,72 $ |
| 14 giorni | 27 luglio 2026 | +8,35% | 82,66 $ | 76,27 $ | 82,66 $ |
| 30 giorni | 12 agosto 2026 | +39,43% | 106,37 $ | 76,27 $ | 106,55 $ |
| 60 giorni | 11 settembre 2026 | +42,34% | 108,59 $ | 76,27 $ | 114,44 $ |
| 90 giorni | 11 ottobre 2026 | +64,74% | 125,68 $ | 76,27 $ | 130,59 $ |
| 120 giorni | 10 novembre 2026 | +78,06% | 135,84 $ | 76,27 $ | 140,51 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 13 luglio 2026 -> 27 luglio 2026 | +8,35% | 76,27 $ (16 luglio 2026) | 82,66 $ (27 luglio 2026) | 82,66 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 28 luglio 2026 -> 12 agosto 2026 | +39,43% | 86,97 $ (28 luglio 2026) | 106,55 $ (10 agosto 2026) | 106,37 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 13 agosto 2026 -> 11 settembre 2026 | +42,34% | 99,79 $ (26 agosto 2026) | 114,44 $ (5 settembre 2026) | 108,59 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 12 settembre 2026 -> 11 ottobre 2026 | +64,74% | 93,04 $ (23 settembre 2026) | 130,59 $ (6 ottobre 2026) | 125,68 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali. La forma simile non compensa un prezzo non aderente.

<!-- BTC_SOL_FRACTAL_END -->

</details>
<!-- COMPACT_SECTION_END:btc_sol_fractal -->

<!-- COMPACT_SECTION_START:rsi_top_cycle -->
<details>
<summary><strong>📈 RSI top-cycle SOL</strong></summary>

<!-- RSI_TOP_CYCLE_START -->

---

# RSI top-cycle warning - SOL

Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)

Filtro prudente: usa almeno 3 picchi RSI, separa vicinanza matematica e rischio reale, e non proietta la top-line oltre 12 mesi.

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 76,29 $ |  |
| Weekly RSI | 39,81 / linea grezza 54,13 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 41,01 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 574,98 $ | Avanzamento +13,27% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 41,0, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
- Confluenza prezzo + RSI: **BASSO**

Questo non è un segnale di entrata. RSI bassi o trendline non affidabili restano neutrali e non penalizzano il Global Confluence.

## Grafici RSI

![SOL weekly RSI top-line](rsi_top_cycle_SOL_weekly.png)

![SOL monthly RSI top-line](rsi_top_cycle_SOL_monthly.png)

<!-- RSI_TOP_CYCLE_END -->

</details>
<!-- COMPACT_SECTION_END:rsi_top_cycle -->

<!-- COMPACT_SECTION_START:sol_onchain -->
<details>
<summary><strong>⛓️ Metriche on-chain SOL</strong></summary>

<!-- SOL_ONCHAIN_METRICS_START -->

---

# SOL on-chain metrics

Report separato completo: **[sol_onchain_metrics_report.md](sol_onchain_metrics_report.md)**

| Voce | Valore |
| --- | --- |
| Score on-chain | 0 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 76,29 $ |
| TVL Solana | 4,86 mld $ |
| TVL 7g | -4,87% |
| DEX volume 24h | 1,14 mld $ |
| Fees 24h | 5,41 mln $ |
| Stablecoin su Solana | 15,56 mld $ |
| Stake ratio | 68,07% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE**

Questo blocco non sostituisce il frattale SOL/BTC: serve come filtro per capire se il movimento è sostenuto anche da attività on-chain.

<!-- SOL_ONCHAIN_METRICS_END -->

</details>
<!-- COMPACT_SECTION_END:sol_onchain -->

<!-- COMPACT_SECTION_START:major_alt_lifecycle -->
<details>
<summary><strong>🔄 Lifecycle squeeze / EMA200 SOL</strong></summary>

<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->

---

# Major alt lifecycle squeeze - SOL

Report separato completo: **[major_alt_lifecycle_squeeze_report.md](major_alt_lifecycle_squeeze_report.md)**

| Voce                      | Valore                                            |
|:--------------------------|:--------------------------------------------------|
| Lifecycle squeeze score | 4 |
| Bias | SQUEEZE SETUP MODERATO |
| Azione coerente | CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO |
| Peso suggerito Global | 0 |
| Trend squeeze | PEGGIORAMENTO |
| Trend squeeze score | -1 |
| Confronto precedente | 2026-07-09 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 76,29 $ |
| EMA200 weekly target | 113,13 $ |
| Upside verso EMA200 | +48,14% |
| Distanza prezzo da EMA200 | -32,49% |
| Gap EMA50/EMA200 | -2,16% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 39,85 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +23,33% |
| Max gain mediano 12w | +24,49% |
| Drawdown mediano 12w | -21,62% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **PEGGIORAMENTO**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-13 06:28 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-13 06:25:05 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: nessun cambiamento forte rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | misto | RIALZISTA | +70.00% | 0.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | RIBASSISTA | +35.00% | -2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | misto | RIBASSISTA | +17.50% | 0.00 punti |

<!-- DAILY_CHANGE_END -->

</details>
<!-- COMPACT_SECTION_END:daily_change -->

<!-- COMPACT_SECTION_START:bounce_after_drawdown -->
<details>
<summary><strong>↕️ Sequenze rimbalzo / dump</strong></summary>

<!-- BOUNCE_AFTER_DRAWDOWN_START -->

---

# Sequenze pratiche: rimbalzo / dump

Report separato completo: [bounce_after_drawdown_report.md](bounce_after_drawdown_report.md)

Questa sezione risponde subito a due domande:

- **Se scende, è una zona di rimbalzo?**
- **Se sale forte, è una zona da prendere profitto?**

| Asset | Scende a | Target rimbalzo | % casi rimbalzo | Movimento reale | Lettura discesa | Sale a | Target dump | % casi dump | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.548 $ | 68.950 $ | +23,53% | +15,79% | rimbalzo poco frequente | 68.950 $ | 59.548 $ | +8,00% | -13,64% | spike storicamente più resistente |
| SOL | 72,48 $ | 83,92 $ | +12,90% | +15,79% | rimbalzo poco frequente | 83,92 $ | 72,48 $ | +43,75% | -13,64% | scarico possibile |
| DOGE | 0,06853 $ | 0,07935 $ | +13,89% | +15,79% | rimbalzo poco frequente | 0,07935 $ | 0,06853 $ | +56,25% | -13,64% | attenzione a prendere profitto |

## Spiegazione ultra semplice

`% casi rimbalzo` e `% casi dump` non sono percentuali assolute.

Sono percentuali **condizionate**:

- prima deve succedere la prima cosa;
- solo dopo si controlla se succede la seconda.

Esempio rimbalzo:

- prezzo iniziale 100 $
- scende a -5% = 95 $
- poi target +10% = 110 $
- da 95 $ a 110 $ il movimento reale è circa +15,79%

Quindi `poi +10%` non vuol dire +10% dal minimo. Vuol dire +10% dal prezzo iniziale.

Esempio dump:

- prezzo iniziale 100 $
- sale a +10% = 110 $
- poi target -5% = 95 $
- da 110 $ a 95 $ il movimento reale è circa -13,64%

Quindi `dump -5%` non vuol dire -5% dallo spike. Vuol dire che torna fino a 5% sotto il prezzo iniziale.

Nel report principale vedi solo la sintesi. Nel report separato ci sono anche soglie intermedie: -8%, +5%, +15%, ecc.

## Traduzione veloce

- **BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +23,53% (4/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 2 poi sono scaricati a -5,00%. Percentuale: +8,00% (2/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +12,90% (4/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 7 poi sono scaricati a -5,00%. Percentuale: +43,75% (7/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +13,89% (5/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 9 poi sono scaricati a -5,00%. Percentuale: +56,25% (9/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-13 06:27:43 UTC

Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto quando sono disponibili dati successivi

Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g     | P90 30g     |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:------------|:------------|
| BTC | 2026-07-13 | 62.682 $ | SALITA | 70,00% | 50.624,84 $ | 60.170,10 $ | 67.851,87 $ | 75.078,83 $ | 87.726,25 $ |
| SOL | 2026-07-13 | 76,29 $ | DISCESA | 35,00% | 58,88 $ | 66,61 $ | 74,30 $ | 79,02 $ | 98,31 $ |
| DOGE | 2026-07-13 | 0.07214 $ | DISCESA | 17,50% | 0.05048 $ | 0.05386 $ | 0.05793 $ | 0.06739 $ | 0.07785 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 3 | 100,00% | 66,67% | 2,19% | -2,19% |
| BTC | 3g | 1 | 100,00% | 0,00% | 3,77% | -3,77% |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 3 | 100,00% | 100,00% | 1,88% | -1,88% |
| SOL | 3g | 1 | 100,00% | 100,00% | 2,55% | -2,55% |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 3 | 100,00% | 66,67% | 1,84% | -1,84% |
| DOGE | 3g | 1 | 100,00% | 100,00% | 2,13% | -2,13% |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Come leggerlo

- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.
- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.
- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.
- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.
- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.

Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. Sotto 5 controlli resta solo osservazione.
<!-- SCANNER_FORECAST_TRACKER_END -->

<!-- FORECAST_30D_HISTORY_START -->

---

# Storico previsioni 30 giorni

Report separato completo: [forecast_30d_history.md](forecast_30d_history.md)

Righe salvate nello storico: **3**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | BTC | 62.682 $ | SALITA | 70,00% | 67.852 $ | 59.777 $ | 72.306 $ | 2026-08-12 |
| 2026-07-13 | DOGE | 0,07000 $ | DISCESA | 17,50% | 0,06000 $ | 0,05000 $ | 0,08000 $ | 2026-08-12 |
| 2026-07-13 | SOL | 76,29 $ | DISCESA | 35,00% | 74,30 $ | 67,07 $ | 82,25 $ | 2026-08-12 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-13 06:27 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione             | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:----------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO               | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO               | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NEGATIVO / RIBASSISTA | SI        | +82,50%       | Casi negativi 82.50% >= 80%      |                  40 |

## DOGE — casi ribassisti

- Trigger: **Casi negativi 82.50% >= 80%**
- Casi usati nei grafici: **33**
- Return mediano 7g: **-9,62%**
- Return mediano 14g: **-25,16%**
- Return mediano 30g: **-21,97%**
- Drawdown mediano: **-28,94%**
- Max gain mediano: **+3,20%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+3,20%**
- Spike massimo medio prima del minimo: **+5,61%**
- Spike p75 prima del minimo: **+7,55%**
- Giorno mediano dello spike: **giorno 2**
- Giorno mediano del minimo: **giorno 14**
- Scarico mediano dal picco al minimo: **-31,99%**
- Casi con almeno +5% prima del minimo: **+36,36%**
- Casi con almeno +10% prima del minimo: **+21,21%**
- Casi con almeno +15% prima del minimo: **+9,09%**
- Discesa quasi immediata: **+3,03%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90    |
|:--------|:--------|:--------|:--------|:-------|
| -31,26% | -25,78% | -21,97% | -13,04% | -7,07% |

### Grafico pulito: bande + mediana

![Extreme clean DOGE](extreme_cases_DOGE_negative_clean_bands.png)

### Grafico asset per asset

![Extreme asset medians DOGE](extreme_cases_DOGE_negative_asset_medians.png)

### Spike massimo prima della discesa

La sigla `g7` sopra una barra significa che il massimo rialzo è avvenuto al giorno 7.

![Extreme spike before dump DOGE](extreme_cases_DOGE_negative_spike_before_dump.png)

### Spike iniziale contro minimo successivo

![Extreme spike vs low DOGE](extreme_cases_DOGE_negative_spike_vs_low.png)

### Casi ordinati per risultato finale

![Extreme ranked DOGE](extreme_cases_DOGE_negative_ranked_returns.png)

### Casi con spike maggiore prima del dump

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                      |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------------|
| WAVES-USD       | 2022-05-30 | +85,21%      | +28,83%                  |              4 | -42,96%      |              17 | -55,72%          | -29,04%      | SPIKE PRIMA DEL DUMP          |
| LINK-USD        | 2022-06-04 | +84,91%      | +25,42%                  |              5 | -20,40%      |               9 | -36,54%          | -13,04%      | SPIKE PRIMA DEL DUMP          |
| ZEC-USD         | 2019-08-29 | +88,27%      | +17,47%                  |             20 | -21,74%      |              28 | -33,38%          | -9,79%       | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2022-06-04 | +85,68%      | +13,35%                  |              4 | -20,84%      |              27 | -30,16%          | -17,03%      | SPIKE PRIMA DEL DUMP          |
| AVAX-USD        | 2025-11-21 | +86,64%      | +12,94%                  |              6 | -14,04%      |              27 | -23,89%          | -8,75%       | SPIKE PRIMA DEL DUMP          |
| OMG-USD         | 2022-06-04 | +87,58%      | +11,92%                  |              5 | -29,18%      |              14 | -36,72%          | -22,91%      | SPIKE PRIMA DEL DUMP          |
| RUNE-USD        | 2022-06-05 | +84,34%      | +10,76%                  |              1 | -44,40%      |              13 | -49,80%          | -25,64%      | SPIKE PRIMA DEL DUMP          |
| BAT-USD         | 2019-01-01 | +85,61%      | +7,93%                   |              8 | -13,95%      |              27 | -20,27%          | -13,42%      | RIALZO MODESTO PRIMA DEL DUMP |
| AVAX-USD        | 2022-06-05 | +85,64%      | +7,55%                   |              1 | -38,58%      |              13 | -42,89%          | -25,24%      | RIALZO MODESTO PRIMA DEL DUMP |
| THETA-USD       | 2022-06-08 | +85,66%      | +7,31%                   |              1 | -17,72%      |               4 | -23,32%          | -6,39%       | RIALZO MODESTO PRIMA DEL DUMP |
| CHZ-USD         | 2022-06-03 | +86,11%      | +5,97%                   |              3 | -28,71%      |              15 | -32,73%          | -19,17%      | RIALZO MODESTO PRIMA DEL DUMP |
| ENJ-USD         | 2022-06-04 | +86,46%      | +5,00%                   |              2 | -33,46%      |              14 | -36,63%          | -16,55%      | RIALZO MODESTO PRIMA DEL DUMP |
| QTUM-USD        | 2022-06-04 | +87,25%      | +4,84%                   |              2 | -33,01%      |              14 | -36,10%          | -24,73%      | RIALZO MODESTO PRIMA DEL DUMP |
| XTZ-USD         | 2026-03-15 | +86,24%      | +4,26%                   |              5 | -12,14%      |              14 | -15,73%          | -10,41%      | RIALZO MODESTO PRIMA DEL DUMP |
| NEO-USD         | 2022-05-30 | +84,51%      | +3,34%                   |              7 | -27,65%      |              19 | -29,99%          | -26,97%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2022-06-01 | +86,64%      | +3,20%                   |              1 | -42,93%      |              30 | -44,70%          | -42,93%      | RIALZO MODESTO PRIMA DEL DUMP |
| ETH-USD         | 2022-06-04 | +86,27%      | +3,20%                   |              2 | -44,85%      |              14 | -46,56%          | -36,11%      | RIALZO MODESTO PRIMA DEL DUMP |
| ICP-USD         | 2023-06-27 | +84,58%      | +3,15%                   |              6 | -7,38%       |              27 | -10,21%          | -2,56%       | PERCORSO RIBASSISTA MISTO     |
| ETC-USD         | 2022-06-04 | +84,07%      | +2,52%                   |              2 | -37,57%      |              14 | -39,10%          | -29,85%      | PERCORSO RIBASSISTA MISTO     |
| DASH-USD        | 2022-06-04 | +87,60%      | +2,36%                   |              2 | -29,01%      |              14 | -30,65%          | -24,48%      | PERCORSO RIBASSISTA MISTO     |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
<!-- EXTREME_CASES_PATH_END -->

</details>
<!-- COMPACT_SECTION_END:extreme_cases -->

<!-- COMPACT_SECTION_START:scanner_full_detail -->
<details>
<summary><strong>📚 Scanner statistico completo — percentili, mappe e 40 casi storici</strong></summary>

# Come leggere questo report

Leggilo sempre in questo ordine:

1. **Direzione più probabile**: ti dice se storicamente era più facile salita, discesa o incertezza.
2. **Casi positivi / negativi**: ti dice la percentuale storica di salita o discesa dopo 30 giorni.
3. **Return 30d**: ti dice dove potrebbe stare il prezzo fra 30 giorni.
4. **Drawdown 30d**: ti dice quanto potrebbe scendere durante quei 30 giorni.
5. **Max gain 30d**: ti dice quanto potrebbe salire durante quei 30 giorni.
6. **Scanner autocalibrato**: dopo abbastanza dati, confronta previsione e realtà e corregge la lettura.

La frase più importante è questa:

> **Return = prezzo finale dopo 30 giorni. Drawdown = discesa durante il mese. Max gain = rialzo durante il mese.**

---

# Scheda veloce: cosa sono i percentili

I **percentili** sono solo un modo per trasformare i 40 casi storici simili in scenari semplici.

## Traduzione semplice

- **Percentile 10%** = molto male / scenario brutto.
- **Percentile 25%** = male / scenario negativo.
- **Percentile 50%** = normale / scenario centrale. È il più importante.
- **Percentile 75%** = bene / scenario buono.
- **Percentile 90%** = molto bene / scenario molto forte.

## Cosa guardare davvero

- Per capire la situazione normale: guarda sempre il **Percentile 50%**.
- Per capire il rischio con leva: guarda **Drawdown 25%** e **Drawdown 10%**.
- Per capire un possibile take profit: guarda **Max gain 50%** e **Max gain 75%**.

## I tre tipi di percentili

- **Percentili Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.
- **Percentili Drawdown 30d** = quanto potrebbe scendere durante i 30 giorni.
- **Percentili Max gain 30d** = quanto potrebbe salire durante i 30 giorni.

## Esempio semplice

Se SOL oggi vale 82 $ e il report dice:

- **Return 50% → 81 $**: fra 30 giorni lo scenario normale è circa 81 $.
- **Drawdown 50% → 77 $**: durante il mese può scendere normalmente verso 77 $.
- **Max gain 50% → 92 $**: durante il mese può fare uno spike normale verso 92 $.

Quindi può salire e scendere durante il mese, ma il **return** guarda solo dove finisce dopo 30 giorni.

---

# Lettura velocissima

Questa è la parte da leggere per prima. Ti dice subito se lo scenario è più da salita, discesa o incertezza.

## Bitcoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **62.681,78 $**
- Return normale fra 30 giorni: **67.851,87 $** (8,25%)
- Drawdown normale durante il mese: **59.777,26 $** (-4,63%)
- Drawdown brutto da rispettare: **55.303,69 $** (-11,77%)
- Max gain normale durante il mese: **72.306,43 $** (15,35%)
- Max gain buono / take profit ottimistico: **79.171,64 $** (26,31%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **35,00%**
- Casi negativi / discesa storica: **65,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **76,29 $**
- Return normale fra 30 giorni: **74,30 $** (-2,61%)
- Drawdown normale durante il mese: **67,07 $** (-12,08%)
- Drawdown brutto da rispettare: **59,84 $** (-21,56%)
- Max gain normale durante il mese: **82,25 $** (7,81%)
- Max gain buono / take profit ottimistico: **88,12 $** (15,50%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **17,50%**
- Casi negativi / discesa storica: **82,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,06 $** (-19,69%)
- Drawdown normale durante il mese: **0,05 $** (-26,99%)
- Drawdown brutto da rispettare: **0,05 $** (-34,27%)
- Max gain normale durante il mese: **0,08 $** (4,92%)
- Max gain buono / take profit ottimistico: **0,08 $** (15,20%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è prudente/debole. Lo scanner vede più rischio di discesa che salita pulita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 62.681,78 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **70,00%**
- Probabilità storica di discesa: **30,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **50.624,84 $** (-19,24%)
- Se va male: **60.170,10 $** (-4,01%)
- Scenario normale: **67.851,87 $** (8,25%)
- Se va bene: **75.078,83 $** (19,78%)
- Se va molto bene: **87.726,25 $** (39,95%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **59.777,26 $** (-4,63%)
- Discesa brutta: **55.303,69 $** (-11,77%)
- Discesa molto brutta: **47.284,07 $** (-24,56%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **72.306,43 $** (15,35%)
- Rialzo buono: **79.171,64 $** (26,31%)
- Rialzo molto forte: **96.237,25 $** (53,53%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **59.777,26 $** e uno spike normale intorno a **72.306,43 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 76,29 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **35,00%**
- Probabilità storica di discesa: **65,00%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **58,88 $** (-22,83%)
- Se va male: **66,61 $** (-12,69%)
- Scenario normale: **74,30 $** (-2,61%)
- Se va bene: **79,02 $** (3,58%)
- Se va molto bene: **98,31 $** (28,87%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **67,07 $** (-12,08%)
- Discesa brutta: **59,84 $** (-21,56%)
- Discesa molto brutta: **56,98 $** (-25,31%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **82,25 $** (7,81%)
- Rialzo buono: **88,12 $** (15,50%)
- Rialzo molto forte: **110,60 $** (44,97%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **67,07 $** e uno spike normale intorno a **82,25 $**.

La chiusura a 30 giorni era più spesso negativa: salita 35,00%, discesa 65,00%. Quindi la lettura principale è prudente/debole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,07 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **17,50%**
- Probabilità storica di discesa: **82,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-30,03%)
- Se va male: **0,05 $** (-25,34%)
- Scenario normale: **0,06 $** (-19,69%)
- Se va bene: **0,07 $** (-6,59%)
- Se va molto bene: **0,08 $** (7,92%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,05 $** (-26,99%)
- Discesa brutta: **0,05 $** (-34,27%)
- Discesa molto brutta: **0,04 $** (-43,10%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (4,92%)
- Rialzo buono: **0,08 $** (15,20%)
- Rialzo molto forte: **0,09 $** (26,69%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,05 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni era più spesso negativa: salita 17,50%, discesa 82,50%. Quindi la lettura principale è prudente/debole.

---

# Come leggere correttamente i 30 giorni

Ogni report giornaliero è una previsione statistica sui **prossimi 30 giorni**.

Ci sono tre dati diversi:

1. **Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.
2. **Drawdown 30d** = quanto potrebbe scendere durante quei 30 giorni.
3. **Max gain 30d** = quanto potrebbe salire al massimo durante quei 30 giorni.

Il prezzo può salire durante il mese e poi chiudere sotto, oppure scendere prima e poi recuperare. Per chi usa leva, il drawdown è spesso più importante del prezzo finale.

# Controllo accuratezza dello scanner

Questa sezione controlla se lo scanner sta funzionando davvero. Ogni giorno viene salvata una previsione. Dopo 30 giorni, lo scanner confronta quella previsione con quello che è successo realmente.

## Come leggerla

- **Previsioni già controllate** = quante vecchie previsioni hanno già compiuto 30 giorni.
- **Direzione corretta** = quante volte lo scanner ha indovinato salita o discesa finale a 30 giorni.
- **Errore medio scenario centrale** = quanto era distante il prezzo reale dal prezzo centrale previsto.
- **Zona rischio toccata** = quante volte il prezzo è sceso fino alla zona di rischio prevista.
- **Zona rialzo toccata** = quante volte il prezzo è salito fino alla zona rialzo prevista.

Per ora non ci sono ancora previsioni vecchie di 30 giorni da controllare.
Il controllo vero inizierà automaticamente dopo il primo mese di utilizzo.

---

# Scanner autocalibrato

Questa è una sezione separata dalla previsione storica grezza. La previsione grezza resta quella basata sui pattern storici. Qui invece lo scanner guarda i propri errori passati e prova a correggere leggermente la lettura.

## Come funziona

Lo scanner confronta le sue vecchie previsioni con la realtà dopo 30 giorni.

- Se in passato è stato troppo ottimista, abbassa la stima.
- Se in passato è stato troppo pessimista, alza la stima.
- Se ha sottostimato il drawdown, rende la zona rischio più prudente.
- Se ha sovrastimato gli spike, riduce la zona rialzo calibrata.

La calibrazione non modifica il codice. Crea solo una seconda lettura: **scanner grezzo** contro **scanner corretto dai suoi errori reali**.

Regola: servono almeno **30 previsioni controllate per asset** prima di applicare la calibrazione. Prima di allora mostra solo dati insufficienti.

## Bitcoin

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 62.681,78 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,20%**
- Rendimento medio dopo 30 giorni: **11,84%**
- Rendimento centrale dopo 30 giorni: **8,25%**
- Discesa media durante i 30 giorni: **-8,83%**
- Massimo rialzo medio durante i 30 giorni: **25,07%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **70.100,35 $**
- Scenario centrale a 30 giorni: **67.851,87 $**
- Zona di rischio media: **57.147,51 $**
- Zona di rialzo media: **78.393,83 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -19,24% → **50.624,84 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -4,01% → **60.170,10 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 8,25% → **67.851,87 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,78% → **75.078,83 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 39,95% → **87.726,25 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -24,56% → **47.284,07 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -11,77% → **55.303,69 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,63% → **59.777,26 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **62.681,78 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **62.681,78 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,69% → **65.624,02 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,15% → **67.791,93 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 15,35% → **72.306,43 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,31% → **79.171,64 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 53,53% → **96.237,25 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-09-19   | 2018-12-27 |        89.54 |        95.69 |           0    |         178.55 |
| FIL-USD         | 2023-06-19   | 2023-09-26 |        89.29 |        17.86 |           0    |          21.6  |
| SAND-USD        | 2023-06-19   | 2023-09-26 |        87.66 |        11.11 |          -6.72 |          11.11 |
| XLM-USD         | 2020-07-05   | 2020-10-12 |        86.95 |         3.87 |          -4.69 |           9.98 |
| DOT-USD         | 2023-06-20   | 2023-09-27 |        86.72 |         3.72 |          -8.57 |           8.96 |
| XRP-USD         | 2019-09-24   | 2020-01-01 |        86.57 |        24.17 |          -2.4  |          26.46 |
| EOS-USD         | 2023-06-20   | 2023-09-27 |        86.32 |         7.44 |          -4.58 |           7.75 |
| NEAR-USD        | 2024-04-15   | 2024-07-23 |        86.17 |       -25.43 |         -38.83 |           0    |
| ONE-USD         | 2020-01-12   | 2020-04-20 |        86.01 |         7.21 |          -4.79 |          10.77 |
| THETA-USD       | 2023-06-19   | 2023-09-26 |        86    |         1.86 |         -11.53 |           5.02 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 76,29 $

Solana richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **35,00%**
- Casi negativi dopo 30 giorni: **65,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **75,96%**
- Rendimento medio dopo 30 giorni: **-1,06%**
- Rendimento centrale dopo 30 giorni: **-2,61%**
- Discesa media durante i 30 giorni: **-14,31%**
- Massimo rialzo medio durante i 30 giorni: **15,42%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **75,48 $**
- Scenario centrale a 30 giorni: **74,30 $**
- Zona di rischio media: **65,38 $**
- Zona di rialzo media: **88,05 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -22,83% → **58,88 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -12,69% → **66,61 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -2,61% → **74,30 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 3,58% → **79,02 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 28,87% → **98,31 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -25,31% → **56,98 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -21,56% → **59,84 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,08% → **67,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,73% → **70,40 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **76,29 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **76,29 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 1,59% → **77,50 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 7,81% → **82,25 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 15,50% → **88,12 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 44,97% → **110,60 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-02-26   | 2019-06-05 |        81.54 |       -22.79 |         -22.79 |           7.37 |
| QTUM-USD        | 2018-09-24   | 2019-01-01 |        78.98 |       -18.48 |         -18.48 |           7.86 |
| VET-USD         | 2020-01-09   | 2020-04-17 |        78.43 |        16.09 |          -3.73 |          26.08 |
| SOL-USD         | 2025-12-04   | 2026-03-13 |        78.07 |        -7.51 |         -10.44 |           9.16 |
| ZIL-USD         | 2018-09-21   | 2018-12-29 |        77.71 |        -0.39 |         -12.5  |          14.85 |
| NEAR-USD        | 2024-04-15   | 2024-07-23 |        77.7  |       -25.43 |         -38.83 |           0    |
| APT-USD         | 2024-09-06   | 2024-12-14 |        77.61 |         0    |         -12.27 |           2.27 |
| TRX-USD         | 2018-09-24   | 2019-01-01 |        77.48 |        30    |           0    |          49.7  |
| LRC-USD         | 2018-09-24   | 2019-01-01 |        77.35 |        30.68 |          -8.53 |         146.68 |
| BNB-USD         | 2025-12-11   | 2026-03-20 |        77.31 |        -4    |          -9.19 |           0.8  |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,07 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **17,50%**
- Casi negativi dopo 30 giorni: **82,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,85%**
- Rendimento medio dopo 30 giorni: **-13,78%**
- Rendimento centrale dopo 30 giorni: **-19,69%**
- Discesa media durante i 30 giorni: **-25,12%**
- Massimo rialzo medio durante i 30 giorni: **10,26%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,06 $**
- Scenario centrale a 30 giorni: **0,06 $**
- Zona di rischio media: **0,05 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -30,03% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -25,34% → **0,05 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -19,69% → **0,06 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: -6,59% → **0,07 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 7,92% → **0,08 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -43,10% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -34,27% → **0,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -26,99% → **0,05 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -14,01% → **0,06 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -6,89% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,83% → **0,07 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 4,92% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 15,20% → **0,08 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 26,69% → **0,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2019-09-24   | 2020-01-01 |        89.03 |        24.17 |          -2.4  |          26.46 |
| NEAR-USD        | 2022-03-07   | 2022-06-14 |        88.45 |         2.98 |          -8.55 |          23.41 |
| ZEC-USD         | 2019-05-22   | 2019-08-29 |        88.27 |        -9.79 |         -21.74 |          17.47 |
| VET-USD         | 2022-02-27   | 2022-06-06 |        88.07 |       -25.78 |         -31.87 |           0.17 |
| DASH-USD        | 2022-02-25   | 2022-06-04 |        87.6  |       -24.48 |         -29.01 |           2.36 |
| OMG-USD         | 2022-02-25   | 2022-06-04 |        87.58 |       -22.91 |         -29.18 |          11.92 |
| QTUM-USD        | 2022-02-25   | 2022-06-04 |        87.25 |       -24.73 |         -33.01 |           4.84 |
| AVAX-USD        | 2025-08-14   | 2025-11-21 |        86.64 |        -8.75 |         -14.04 |          12.94 |
| INJ-USD         | 2022-02-22   | 2022-06-01 |        86.64 |       -42.93 |         -42.93 |           3.2  |
| ENJ-USD         | 2022-02-25   | 2022-06-04 |        86.46 |       -16.55 |         -33.46 |           5    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-07-13 06:28 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 62.682 $ | False | -15.39% | -10.18% | BEAR | -15.39% | -10.18% |
| DOGE-USD | BEAR | 0.07214 $ | False | -22.38% | -16.45% | BEAR | -15.39% | -10.18% |
| SOL-USD | BEAR | 76,29 $ | False | -8.90% | -18.22% | BEAR | -15.39% | -10.18% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 8.25% | 19.78% | 39.95% | -4.63% | -24.56% | 15.35% | 26.31% | 53.53% | 65.00% | 21.86% | 44.19% | 67.36% |
| BTC-USD | SAME_BTC_REGIME | 14 | 100.00% | 30.09% | 43.77% | 81.69% | 0.00% | -4.66% | 36.06% | 55.99% | 100.38% | 92.86% | 29.27% | 46.62% | 63.09% |
| BTC-USD | SAME_ASSET_REGIME | 26 | 88.46% | 11.31% | 21.79% | 47.13% | -4.01% | -10.14% | 19.29% | 26.41% | 57.87% | 84.62% | 31.05% | 51.37% | 68.64% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 100.00% | 20.68% | 46.19% | 91.02% | 0.00% | -4.75% | 29.97% | 55.51% | 111.18% | 91.67% | 19.97% | 45.70% | 65.72% |
| DOGE-USD | ALL_MATCHES | 40 | 17.50% | -19.69% | -6.59% | 7.92% | -26.99% | -43.10% | 4.92% | 15.20% | 26.69% | 37.50% | -2.71% | 7.38% | 39.33% |
| DOGE-USD | SAME_BTC_REGIME | 32 | 15.62% | -22.23% | -13.00% | 6.19% | -28.98% | -44.26% | 3.80% | 12.28% | 28.49% | 34.38% | -2.71% | 4.46% | 37.90% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 18.18% | -21.58% | -12.89% | 16.31% | -28.71% | -44.11% | 4.26% | 13.35% | 28.35% | 39.39% | -1.48% | 11.61% | 38.83% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 30 | 13.33% | -22.23% | -13.92% | 6.57% | -28.98% | -44.45% | 3.27% | 11.69% | 28.93% | 33.33% | -2.92% | 3.35% | 26.83% |
| SOL-USD | ALL_MATCHES | 40 | 35.00% | -2.61% | 3.58% | 28.87% | -12.08% | -25.31% | 7.81% | 15.50% | 44.97% | 52.50% | 6.06% | 27.92% | 54.41% |
| SOL-USD | SAME_BTC_REGIME | 22 | 40.91% | -0.79% | 6.00% | 27.61% | -10.90% | -22.45% | 9.50% | 16.08% | 42.61% | 68.18% | 8.58% | 39.53% | 65.72% |
| SOL-USD | SAME_ASSET_REGIME | 30 | 40.00% | -0.28% | 6.00% | 28.87% | -11.83% | -24.07% | 9.50% | 16.81% | 44.97% | 63.33% | 7.70% | 33.85% | 54.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 38.89% | -0.79% | 2.00% | 20.85% | -11.56% | -20.76% | 9.50% | 11.64% | 27.16% | 72.22% | 8.58% | 31.73% | 57.83% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 100.00% | 30.09% | 0.00% | 55.99% | 92.86% | 29.27% | 81.65% |
| BTC-USD | HISTORICAL_BTC_BULL | 16 | 50.00% | 0.49% | -8.66% | 10.72% | 50.00% | 10.60% | 43.61% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 100.00% | 11.51% | -5.57% | 21.60% | 100.00% | 50.78% | 73.78% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -7.78% | -12.50% | 16.64% | 0.00% | -25.42% | 16.64% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 32 | 15.62% | -22.23% | -28.98% | 12.28% | 34.38% | -2.71% | 25.43% |
| DOGE-USD | HISTORICAL_BTC_BULL | 3 | 0.00% | -6.66% | -14.04% | 15.24% | 33.33% | -9.16% | 15.89% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 21.44% | -1.83% | 24.78% | 100.00% | 76.22% | 136.08% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -9.79% | -13.95% | 12.70% | 33.33% | -15.37% | 27.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 40.91% | -0.79% | -10.90% | 16.08% | 68.18% | 8.58% | 68.69% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 10.00% | -6.31% | -22.26% | 3.09% | 20.00% | -4.03% | 3.09% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 9.86% | -5.76% | 17.45% | 100.00% | 54.98% | 64.19% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 6 | 33.33% | -9.44% | -15.49% | 40.99% | 33.33% | -9.05% | 40.99% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 88.46% | 11.31% | -4.01% | 26.41% | 84.62% | 31.05% | 79.85% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 28.57% | -17.97% | -17.97% | 9.09% | 28.57% | -5.68% | 20.47% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 9.86% | -10.72% | 31.08% | 50.00% | 11.71% | 64.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -7.78% | -11.48% | 32.20% | 20.00% | -25.42% | 32.20% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 18.18% | -21.58% | -28.71% | 13.35% | 39.39% | -1.48% | 28.83% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -3.74% | -10.00% | 13.15% | 50.00% | -11.83% | 16.71% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -25.24% | -38.58% | 7.55% | 0.00% | -3.26% | 7.55% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -8.75% | -14.04% | 12.94% | 0.00% | -9.16% | 12.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -2.56% | -8.55% | 20.44% | 33.33% | -15.37% | 47.15% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 40.00% | -0.28% | -11.83% | 16.81% | 63.33% | 7.70% | 58.94% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 0.00% | -13.12% | -21.16% | 2.39% | 0.00% | -8.98% | 2.39% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -5.30% | -20.18% | 1.03% | 0.00% | -2.08% | 4.45% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -6.02% | -22.79% | 26.08% | 40.00% | -4.13% | 70.92% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-09-19 | 89.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| BTC-USD | ONE-USD | 2020-01-12 | 86.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.21% | -4.79% | 10.77% | -15.61% | -15.61% | 10.81% |
| BTC-USD | KSM-USD | 2022-03-10 | 85.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.02% | -4.93% | 16.96% | 14.38% | -4.93% | 37.01% |
| BTC-USD | LTC-USD | 2020-01-08 | 85.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.23% | -4.36% | 15.86% | 2.87% | -4.36% | 15.86% |
| BTC-USD | BAT-USD | 2019-10-04 | 84.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.15% | -1.02% | 43.98% | 5.38% | -1.02% | 63.91% |
| BTC-USD | XLM-USD | 2019-10-04 | 84.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 49.02% | 0.00% | 53.16% | 5.97% | 0.00% | 80.44% |
| BTC-USD | MKR-USD | 2020-01-13 | 84.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 2.37% | 0.00% | 19.75% | 67.03% | 0.00% | 121.83% |
| BTC-USD | XLM-USD | 2020-01-07 | 84.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| BTC-USD | QTUM-USD | 2020-01-12 | 83.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.33% | 0.00% | 26.00% | 25.57% | 0.00% | 43.16% |
| BTC-USD | EOS-USD | 2020-01-07 | 83.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.83% | 0.00% | 25.64% | 7.27% | 0.00% | 25.64% |
| DOGE-USD | VET-USD | 2022-02-27 | 88.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | DASH-USD | 2022-02-25 | 87.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 87.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | INJ-USD | 2022-02-22 | 86.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -42.93% | -42.93% | 3.20% | -31.40% | -43.70% | 3.20% |
| DOGE-USD | ENJ-USD | 2022-02-25 | 86.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.55% | -33.46% | 5.00% | 1.45% | -33.46% | 5.00% |
| DOGE-USD | DOT-USD | 2022-02-25 | 86.45% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.93% | -28.64% | 0.66% | -15.09% | -33.21% | 0.66% |
| DOGE-USD | OP-USD | 2025-12-07 | 86.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -12.89% | -25.94% | 0.00% | -0.67% | -25.94% | 25.30% |
| DOGE-USD | ETH-USD | 2022-02-25 | 86.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.11% | -44.85% | 3.20% | -10.14% | -44.85% | 3.20% |
| DOGE-USD | XTZ-USD | 2025-12-06 | 86.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.41% | -12.14% | 4.26% | -2.16% | -12.14% | 4.26% |
| SOL-USD | SOL-USD | 2025-12-04 | 78.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.51% | -10.44% | 9.16% | 6.95% | -10.44% | 10.43% |
| SOL-USD | APT-USD | 2024-09-06 | 77.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | ENJ-USD | 2018-09-19 | 76.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -16.11% | -19.37% | 5.11% | 93.16% | -38.09% | 93.16% |
| SOL-USD | NEAR-USD | 2025-12-06 | 76.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.76% | -13.93% | 10.53% | 16.47% | -13.93% | 18.85% |
| SOL-USD | OMG-USD | 2025-12-06 | 76.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -8.00% | 2.31% | 8.91% | -8.00% | 14.55% |
| SOL-USD | CRV-USD | 2025-12-05 | 75.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.77% | -11.77% | 8.67% | 13.61% | -11.77% | 20.25% |
| SOL-USD | XLM-USD | 2020-01-07 | 75.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| SOL-USD | RUNE-USD | 2025-12-07 | 75.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.46% | -17.52% | 0.00% | 8.26% | -17.52% | 37.02% |
| SOL-USD | BTC-USD | 2025-12-07 | 75.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.07% | -11.90% | 0.00% | 5.62% | -11.90% | 9.72% |
| SOL-USD | LINK-USD | 2025-12-06 | 75.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.84% | -11.36% | 4.69% | 10.45% | -11.36% | 12.98% |

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the cleanest filter, but it needs enough matches to matter.
- If SAME_BTC_AND_ASSET_REGIME has fewer than 5 matches, treat it as useful context, not a strong statistic.
- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.
- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.

## Regime definitions

- BULL: price above MA200, MA200 rising, positive 90d trend.
- BEAR: price below MA200, MA200 falling, weak 90d trend.
- RECOVERY: improving 90d trend, but not yet a clean bull structure.
- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.
- MIXED: unclear regime.
- UNKNOWN: not enough historical data.
<!-- MARKET_REGIME_MATCH_END -->

</details>
<!-- COMPACT_SECTION_END:market_regime -->

<!-- COMPACT_SECTION_START:classic_technical -->
<details>
<summary><strong>📐 Conferma tecnica classica</strong></summary>

<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->
# Classic technical confirmation report

Generato: 2026-07-13 06:28 UTC

Questo modulo controlla se il setup è confermato secondo analisi tecnica classica. Non sostituisce lo scanner frattale: serve come filtro di conferma.

Cosa controlla:

- trend daily e weekly
- stage analysis stile Weinstein
- struttura massimi/minimi
- breakout o breakdown con volume
- RSI e MACD
- OBV, CMF e volume relativo
- candele principali
- Wyckoff semplificato
- volatilità tecnica locale tramite ATR e distanza dai livelli

## Sintesi

| Asset | Prezzo | Score | Verdetto | Stage | Struttura | Wyckoff | Volatilità locale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.682 $ | -1 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | SPRING / TEST POSSIBILE | MEDIO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 76,29 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07214 $ | -9 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | 0 | 0 | +2 | 0 | 0 | +1 | -1 |
| SOL | -4 | +2 | -2 | +2 | 0 | 0 | 0 | -2 |
| DOGE | -4 | 0 | -1 | -1 | 0 | -1 | -2 | -9 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.553 $ | 64.186 $ | 82.430 $ | 57.748 $ | 2,97% | -2,60% | -15,42% |
| SOL | 76,26 $ | 83,22 $ | 98,27 $ | 60,41 $ | 4,02% | 10,83% | -8,89% |
| DOGE | 0.07206 $ | 0.07923 $ | 0.11825 $ | 0.06961 $ | 3,90% | -17,83% | -22,38% |

## Lettura dettagliata

### BTC

- Prezzo: **62.682 $**
- Score classico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,97%; distanza supporto 0,31%; distanza resistenza 2,29%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI neutrale 47.6; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.10; volume ratio 0.74
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 47.63 |
| MACD histogram | 433.09547 |
| CMF20 | 0.102 |
| Volume ratio 20 | 0.74 |
| MA20 | 61.837 $ |
| MA50 | 64.592 $ |
| MA100 | 70.682 $ |
| MA200 | 73.743 $ |
| Pendenza MA50 20g | -9,62% |
| Pendenza MA200 60g | -10,18% |
| Bollinger width | 11,51% |
| Bollinger position | 0.63 |

### SOL

- Prezzo: **76,29 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 4,02%; distanza supporto 0,10%; distanza resistenza 9,02%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-2** — RSI sano 50.0; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.11; volume ratio 0.60
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 50.05 |
| MACD histogram | -0.24684 |
| CMF20 | 0.105 |
| Volume ratio 20 | 0.60 |
| MA20 | 76,37 $ |
| MA50 | 74,18 $ |
| MA100 | 80,31 $ |
| MA200 | 91,52 $ |
| Pendenza MA50 20g | -6,35% |
| Pendenza MA200 60g | -18,22% |
| Bollinger width | 24,17% |
| Bollinger position | 0.50 |

### DOGE

- Prezzo: **0.07214 $**
- Score classico: **-9 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,90%; distanza supporto 0,20%; distanza resistenza 9,74%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-1** — RSI debole 33.8; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.01; volume ratio 0.71
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **-1** — Shooting star / rejection alto
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 33.77 |
| MACD histogram | 0.00038 |
| CMF20 | 0.012 |
| Volume ratio 20 | 0.71 |
| MA20 | 0.07432 $ |
| MA50 | 0.08339 $ |
| MA100 | 0.09273 $ |
| MA200 | 0.10075 $ |
| Pendenza MA50 20g | -14,10% |
| Pendenza MA200 60g | -16,45% |
| Bollinger width | 10,60% |
| Bollinger position | 0.22 |

## Come leggere lo score

- **+8 a +12**: conferma tecnica rialzista forte.
- **+5 a +7**: setup costruttivo, ma può mancare ancora una rottura pulita.
- **+2 a +4**: setup anticipato, interessante ma non confermato.
- **-1 a +1**: neutrale / misto.
- **-4 a -2**: debole / non confermato.
- **-8 o meno**: conferma tecnica ribassista.

Nota: questo modulo deve pesare poco nel Global finché non viene verificato dalla calibrazione. La funzione principale è evitare di confondere un contesto interessante con una conferma vera.
<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->

</details>
<!-- COMPACT_SECTION_END:classic_technical -->

<!-- COMPACT_SECTION_START:classic_visual -->
<details>
<summary><strong>🖼️ Grafici e pattern Classic Visual</strong></summary>

<!-- CLASSIC_TECHNICAL_VISUAL_START -->
# Classic technical visual report

Generato: 2026-07-13 06:28 UTC

Questo report crea grafici visivi dei pattern tecnici principali. Serve per vedere il grafico e il ciclo di vita dei pattern; non aggiunge automaticamente punteggio al Global.

Regola anti-pattern-zombie: dopo il breakout un pattern passa da ATTIVO a CONFERMATO RECENTE, poi a MATURO. Quando raggiunge il target o viene invalidato vale 0 e non resta confermato per sempre.

Pattern controllati:

- doppio minimo
- doppio massimo
- testa e spalle
- testa e spalle inverso
- triangolo / compressione
- candela giornaliera principale
- pivot high / pivot low
- supporto, resistenza, breakout e breakdown 60 giorni
- data breakout, età, target teorico, progresso e invalidazione
- livelli Fibonacci 23,6 / 38,2 / 50 / 61,8 / 78,6 letti dal Technical Structure

## Sintesi visiva

| Asset | Prezzo | Pattern principale | Stato | Famiglia | Breakout | Target | Progresso | Distanza neckline | Fibonacci | Stato prezzo | Supporto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.682 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 76.748 $ | n/a | 7,28% | Fib 23,6% TESTATO (0) @ 63.658 $ | NEL RANGE | 62.553 $ |
| SOL | 76,29 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-07-01 | 91,46 $ | 2,26% | n/a | Fib 38,2% TENUTO (+1) @ 74,87 $ | NEL RANGE | 76,02 $ |
| DOGE | 0.07214 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 30,34% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08220 $ | NEL RANGE | 0.07107 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-05 -> 2026-07-01**
- Età formazione: **12 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **67.248 $**
- Target teorico: **76.748 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **7,28%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 63.658 $** — Swing DOWN 2026-05-06 82.792 -> 2026-07-01 57.748; livello più vicino 23.6% a 63.658; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65.903 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.544 $**
- Breakout 60g: **82.430 $**
- Breakdown 60g: **57.748 $**
- RSI14: **47.36**
- ATR14: **2,98%**
- Volume ratio 20g: **0.74**
- Rendimento 30g: **-2,70%**
- Rendimento 90g: **-15,50%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 7,28% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 12 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | TARGET RAGGIUNTO | 0 | ribassista | 74.959 $ | 2026-05-27 | 47g | 71.596 $ | 365,15% | n/a | 76.458 $ | Due massimi simili a 78.321 $ e 77.991 $. Neckline circa 74.959 $. Breakout neckline: 2026-05-27 (47 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.596 $; progresso: 365,15%; prezzo sotto neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-06 -> 2026-06-25**
- Età formazione: **18 giorni**
- Breakout pattern: **2026-07-01**
- Età breakout: **12 giorni**
- Neckline: **75,94 $**
- Target teorico: **91,46 $**
- Progresso verso target: **2,26%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (+1) @ 74,87 $** — Swing UP 2026-06-06 60,41 -> 2026-07-04 83,81; livello più vicino 38.2% a 74,87; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **74,42 $**
- Relazione prezzo/neckline: **vicino alla neckline**
- Dettaglio: Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (12 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 2,26%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76,02 $**
- Resistenza: **83,81 $**
- Breakout 60g: **98,27 $**
- Breakdown 60g: **60,41 $**
- RSI14: **49.94**
- ATR14: **4,02%**
- Volume ratio 20g: **0.60**
- Rendimento 30g: **+10,77%**
- Rendimento 90g: **-8,93%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 75,94 $ | 2026-07-01 | 12g | 91,46 $ | 2,26% | n/a | 74,42 $ | Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (12 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 2,26%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 60,41 $ | n/a | n/a | 33,04 $ | n/a | 26,28% | 61,62 $ | Due massimi simili a 87,79 $ e 83,81 $. Neckline circa 60,41 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 9 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 28,81% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 51 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 46g | 66,88 $ | 40,03% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (46 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 40,03%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **31 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **19 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **30,34%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08220 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-08 0.07107; livello più vicino 23.6% a 0.08220; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (19 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 30,34%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Shooting star / rejection alto**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07107 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.11825 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **33.65**
- ATR14: **3,90%**
- Volume ratio 20g: **0.71**
- Rendimento 30g: **-17,90%**
- Rendimento 90g: **-22,44%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 19g | 0.05847 $ | 30,34% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (19 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 30,34%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 19g | 0.06035 $ | 33,56% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (19 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 33,56%; prezzo sotto neckline. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.11825 $ | n/a | n/a | 0.14377 $ | n/a | 63,92% | 0.11589 $ | Due minimi simili a 0.09274 $ e 0.09675 $. Neckline circa 0.11825 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 46 giorni. |

## Stati del ciclo di vita

- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; score 0.
- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; score prudente ±1.
- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; score ±2.
- **MATURO**: breakout più vecchio di 14 giorni e ancora valido; score ridotto ±1.
- **TARGET RAGGIUNTO**: movimento teorico già completato; score 0.
- **INVALIDATO**: due chiusure consecutive oltre la soglia opposta; score 0.

## Come leggerlo

- Il grafico in alto mostra prezzo, MA20, MA50, MA200, supporti, resistenze, neckline, target, invalidazione e livelli Fibonacci.
- Il pannello centrale mostra RSI14.
- Il pannello basso mostra volume e media volume 20 giorni.
- Un pattern CANDIDATO non è un segnale operativo: il progresso target resta n/a e viene mostrata soltanto la distanza dalla neckline.
- TARGET RAGGIUNTO e INVALIDATO restano visibili per memoria storica, ma valgono 0.
- Il pattern principale usa come fonte autorevole il lifecycle di technical_structure_metrics.csv; il detector visuale resta di supporto grafico.
- Fibonacci non crea un segnale autonomo: pesa al massimo ±1 nel Technical Structure solo con una confluenza indipendente.

Nota: questi pattern sono riconosciuti con regole algoritmiche semplici. Sono utili per visualizzare il grafico, ma vanno sempre controllati a occhio.
<!-- CLASSIC_TECHNICAL_VISUAL_END -->

</details>
<!-- COMPACT_SECTION_END:classic_visual -->

<!-- COMPACT_SECTION_START:fractal_path -->
<details>
<summary><strong>🛤️ Tracking percorso frattale SOL/BTC</strong></summary>

<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-13 06:28 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-13**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-28**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **76,29 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,96%**
- Aderenza live principale: **+59,98%**
- Errore medio live principale: **20,01%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **37**
- Osservazioni inclusive dal bottom: **38**
- Osservazioni da inizio programma/scanner: **11**
- Errore assoluto medio dal bottom: **10,07%**
- Errore assoluto medio da inizio programma: **20,01%**
- Gap firmato medio ultimi 7 giorni: **+17,64%**
- Errore assoluto medio ultimi 7 giorni: **17,64%**
- Gap ultimo giorno: **+17,00%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+17,00%**
- Gap firmato medio 7g: **+17,64%**
- Errore assoluto medio 7g: **17,64%**
- Variazione recente gap: **-0,67%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 28 | 2026-07-04 | 2022-12-19 | 81,65 $ | 64,76 $ | +26,08% | da inizio programma |
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 76,29 $ | 65,20 $ | +17,00% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-20 | 66,43 $ | 77,72 $ | 76,27 $ / 77,72 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-27 | 70,65 $ | 82,66 $ | 76,27 $ / 82,66 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-03 | 81,50 $ | 95,35 $ | 76,27 $ / 97,57 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-10 | 91,07 $ | 106,55 $ | 76,27 $ / 106,55 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-17 | 93,45 $ | 109,34 $ | 76,27 $ / 109,58 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-24 | 90,36 $ | 105,73 $ | 76,27 $ / 109,58 $ | no | n/a | n/a | n/a |
| 49g | 2026-08-31 | 95,75 $ | 112,03 $ | 76,27 $ / 112,03 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-07 | 95,29 $ | 111,49 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-14 | 93,15 $ | 108,99 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-21 | 85,55 $ | 100,10 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-28 | 96,02 $ | 112,35 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-05 | 107,57 $ | 125,86 $ | 76,27 $ / 129,86 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-12 | 111,67 $ | 130,66 $ | 76,27 $ / 130,66 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-19 | 111,00 $ | 129,87 $ | 76,27 $ / 131,26 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-26 | 118,72 $ | 138,91 $ | 76,27 $ / 139,35 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-02 | 113,54 $ | 132,84 $ | 76,27 $ / 140,51 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-09 | 111,96 $ | 131,00 $ | 76,27 $ / 140,51 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-16 | 114,26 $ | 133,69 $ | 76,27 $ / 140,51 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 0 | n/a | n/a | n/a |
| 14g | 0 | n/a | n/a | n/a |
| 21g | 0 | n/a | n/a | n/a |
| 28g | 0 | n/a | n/a | n/a |
| 35g | 0 | n/a | n/a | n/a |
| 42g | 0 | n/a | n/a | n/a |
| 49g | 0 | n/a | n/a | n/a |
| 56g | 0 | n/a | n/a | n/a |
| 63g | 0 | n/a | n/a | n/a |
| 70g | 0 | n/a | n/a | n/a |
| 77g | 0 | n/a | n/a | n/a |
| 84g | 0 | n/a | n/a | n/a |
| 91g | 0 | n/a | n/a | n/a |
| 98g | 0 | n/a | n/a | n/a |
| 105g | 0 | n/a | n/a | n/a |
| 112g | 0 | n/a | n/a | n/a |
| 119g | 0 | n/a | n/a | n/a |
| 126g | 0 | n/a | n/a | n/a |

## Regola di lettura

- La somiglianza strutturale descrive la forma.
- Il gap ancorato descrive la distanza reale dal percorso.
- Lo scenario riancorato non dimostra che il frattale sia valido.
- Prima di pesare il modulo servono milestone maturate e un errore ancorato accettabile.
<!-- FRACTAL_PATH_TRACKER_END -->

<!-- SOL_BTC_FRACTAL_HISTORY_START -->

---

# Storico frattale SOL/BTC

Per vedere la tabella giorno per giorno devi aprire/cliccare questo file:

**[sol_btc_fractal_history.md](sol_btc_fractal_history.md)**

Ultima lettura salvata: **2026-07-13** — SOL 76,29 $, gap +17,00%, somiglianza +64,96%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-07-13 06:28 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.839 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0064% | n/a | 2,14 | -6,30% | 0 $ | 0 $ |
| SOL | 75,84 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0006% | n/a | 1,09 | -7,85% | 0 $ | 0 $ |
| DOGE | 0.07198 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0024% | n/a | 1,86 | -3,33% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0023% | 114,20 mln $ | 1,72 | -2,88% |
| BTC | Bitget | OK | +0,0100% | 2,14 mld $ | 756,57 | -41,79% |
| BTC | Kucoin | OK | +0,0026% | 1,89 mld $ | 2,14 | -2,46% |
| SOL | Kraken | OK | -0,0415% | 16,69 mln $ | 2,21 | -18,32% |
| SOL | Bitget | OK | +0,0060% | 309,66 mln $ | 1,09 | +2,04% |
| SOL | Kucoin | OK | -0,0025% | 302,97 mln $ | 0,72 | -7,48% |
| DOGE | Kraken | OK | -0,0127% | 3,07 mln $ | 0,14 | +2,46% |
| DOGE | Bitget | OK | -0,0051% | 81,61 mln $ | 1,86 | +1,94% |
| DOGE | Kucoin | OK | +0,0092% | 97,19 mln $ | 3,97 | -26,86% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+1,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI debole/ipervenduto con flusso exchange in recupero: possibile esaurimento della vendita.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +70,00% | +8,25% | 0 | n/a | RACCOLTA DATI | 0,00 | +70,00% | +8,25% |
| SOL | +35,00% | -2,61% | 0 | n/a | RACCOLTA DATI | 0,00 | +35,00% | -2,61% |
| DOGE | +17,50% | -19,69% | 0 | n/a | RACCOLTA DATI | 0,00 | +17,50% | -19,69% |

## Dati salvati

- `exchange_market_data_snapshot.json`: fotografia derivata Kraken + Bitget + KuCoin, con OKX e Coinbase ausiliari.
- `exchange_market_data_intraday.csv`: memoria operativa mobile degli ultimi 180 giorni, ripristinata da due copie ridondanti su GitHub Releases.
- `exchange_intraday_YYYY-MM.csv.gz`: archivio mensile permanente dei dati intraday, creato dopo la chiusura del mese.
- `exchange_microstructure_metrics.csv`: score e conferme correnti lette dal Global.
- `exchange_microstructure_history.csv`: prima fotografia giornaliera congelata, usata per valutare le previsioni.
- `exchange_signal_tracker_metrics.csv`: accuratezza a 1/3/7/14/30 giorni.
- `exchange_prediction_overlay.csv`: confronto scanner grezzo vs overlay calibrato.

## Regole di prudenza

- Un muro dell'order book può essere cancellato: non è un supporto garantito.
- Funding, OI e flusso misurano pressione/affollamento, non direzione certa.
- OI in aumento conta soltanto insieme alla direzione del prezzo e al taker flow.
- La componente liquidazioni resta neutrale finché non esiste un feed pubblico completo e verificato.
- Prima dei 30 controlli a 7g il modulo non pesa nel Global; prima dei 30 controlli a 30g l'overlay non altera le previsioni.

Salute fonti: **OK** — coppie exchange/asset disponibili: 9/9. Kraken OK; Bitget OK; KuCoin OK.
Fonti ausiliarie non pesate: OKX OK; Coinbase PARZIALE. Copertura ausiliaria: 3/6.
Storage persistente: **OK** — ultimo asset: exchange_state_B.tar.gz.
<!-- EXCHANGE_MICROSTRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_microstructure -->

<!-- COMPACT_SECTION_START:exchange_signal_tracker -->
<details>
<summary><strong>🧠 Accuratezza segnali exchange</strong></summary>

<!-- EXCHANGE_SIGNAL_TRACKER_START -->
# Accuratezza dati exchange e microstruttura

Generato: 2026-07-13 06:28 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **3**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | BTC | 62.838,58 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 2,14 | n/a | -6,30% |
| 2026-07-13 | DOGE | 0.07198 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,86 | n/a | -3,33% |
| 2026-07-13 | SOL | 75,84 | V2.1.3 | OK | 0 | 0 | 1,50 | BASSA | 1,09 | n/a | -7,85% |
| 2026-07-12 | BTC | 63.743,50 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 1,82 | n/a | -6,53% |
| 2026-07-12 | DOGE | 0.07276 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 1,82 | n/a | -7,68% |
| 2026-07-12 | SOL | 76,17 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 3,31 | n/a | -21,30% |
| 2026-07-11 | BTC | 64.152,13 | TRANSITION_PRE_V2.1.3 | ESCLUSA | 0 | 0 | -1,50 | BASSA | 0,06 | +1,72% | +2,84% |
| 2026-07-11 | DOGE | 0.07422 | TRANSITION_PRE_V2.1.3 | ESCLUSA | 0 | 0 | 1,38 | BASSA | 1,14 | -7,68% | +4,98% |
| 2026-07-11 | SOL | 77,77 | TRANSITION_PRE_V2.1.3 | ESCLUSA | 0 | 0 | -3,00 | BASSA | 0,41 | +17,81% | -9,72% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
<!-- EXCHANGE_SIGNAL_TRACKER_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_signal_tracker -->

<!-- COMPACT_SECTION_START:liquidations -->
<details>
<summary><strong>💥 Futures e liquidazioni</strong></summary>

<!-- LIQUIDATION_SUMMARY_START -->

---

# Sintesi semplice futures / liquidazioni

Report separato completo: [liquidation_report.md](liquidation_report.md)

**BTC** — BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto. Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.682 $ | +0.0029% | +1.10% | 1.53 | Misto | 1/5 |
| SOL | 76,29 $ | -0.0016% | -23.85% | 2.64 | Misto | 1/5 |
| DOGE | 0.07214 $ | +0.0046% | +17.25% | 4.12 | Leva alta, direzione mista | 3/5 |

## Come usarla insieme al frattale

- Frattale ribassista + futures con rischio sotto = prudenza alta.
- Frattale rialzista + futures con rischio sopra = segnale più interessante.
- Frattale e futures opposti = situazione sporca, meglio non forzare.
- Per posizioni a leva, il futures report serve soprattutto a capire se può arrivare una pulizia violenta prima dei 30 giorni.

<!-- LIQUIDATION_SUMMARY_END -->

</details>
<!-- COMPACT_SECTION_END:liquidations -->

<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_START -->
# Divergenze RSI multi-timeframe — diagnostica

Generato: 2026-07-13 06:28 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D       | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:-----------------------------------------------------|:--------------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bearish                                       | IN_FORMAZIONE | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Momentum in indebolimento, divergenza non confermata | CONTESTO      | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Hidden bearish                                       | CONFERMATA    | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bearish                                       | IN_FORMAZIONE | 62.759 $ / 47,68  | 2026-06-22 65.544 $ / RSI 40,88 → 2026-07-10 64.659 $ / RSI 53,80   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare                                     | CONFERMATA    | 62.759 $ / 37,63  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Momentum in indebolimento, divergenza non confermata | CONTESTO      | 76,37 $ / 50,15   | n/a                                                                 | +1,90%              | -5,47            |      0 |
| SOL     | 1W   | Hidden bearish                                       | CONFERMATA    | 76,37 $ / 39,85   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bearish                                       | CONFERMATA    | 0.07220 $ / 33,77 | 2026-06-12 0.09169 $ / RSI 35,18 → 2026-07-04 0.07923 $ / RSI 41,65 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Conferma ribassista                                  | CONTESTO      | 0.07220 $ / 33,23 | n/a                                                                 | -16,13%             | -2,56            |      0 |

### BTC

- **1D — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Momentum in indebolimento, divergenza non confermata / CONTESTO**: Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **3**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

_Nessun controllo maturato: il tracker ha appena iniziato a raccogliere dati._

## Regole di prudenza

- Una divergenza **in formazione** può scomparire prima che il pivot sia confermato.
- Una divergenza weekly può anticipare il prezzo di diverse settimane.
- Prezzo in calo e RSI in calo non è bullish divergence: è conferma ribassista.
- Le divergenze restano dentro la famiglia tecnica e non vengono sommate come prova indipendente.
- Nessuna statistica di questo modulo autorizza automaticamente il trading reale.
<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_END -->

<!-- COMPACT_SECTION_START:technical_structure -->
<details>
<summary><strong>🧱 Struttura tecnica completa e Fibonacci</strong></summary>

<!-- TECHNICAL_STRUCTURE_START -->
# Report struttura tecnica

Generato: 2026-07-13 06:28 UTC

Questo report aggiunge al tuo scanner una lettura classica di analisi tecnica.

Moduli inclusi:

- Struttura trend con MA20 / MA50 / MA200
- Massimi e minimi crescenti oppure decrescenti
- Doppio minimo, triplo minimo, doppio massimo, triplo massimo
- Pattern Adam and Eve Bottom / Top
- Ciclo di vita pattern: candidato, attivo, confermato recente, maturo, target raggiunto, invalidato
- Data breakout, età, target teorico, progresso e recupero della neckline
- Divergenze RSI e divergenze RSI nascoste
- Momentum MACD
- Conferma volume con OBV / CMF
- Candidato fase Wyckoff
- Fibonacci automatico su swing pivot, con lifecycle e confluenza
- Punteggio tecnico di confluenza

Regola anti-pattern-zombie: un pattern vecchio non resta indefinitamente confermato. Dopo il target vale 0; se viene recuperata stabilmente la neckline viene invalidato; se resta valido ma invecchia passa a MATURO con peso ridotto.

## Sintesi

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista                  | Pattern ribassista                | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:-----------------------------------|:----------------------------------|:-----------|:-------------|
| BTC | 62.682 $ | 1 | NEUTRALE / MISTO | Trend ribassista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / TARGET RAGGIUNTO | 57.748 | 65.544 |
| SOL | 76,29 $ | -3 | DEBOLE | Trend ribassista | Momentum debole | Volatilità in espansione | +2 | +1 / TENUTO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 64,42 | 83,81 |
| DOGE | 0.07214 $ | -5 | DEBOLE | Trend ribassista | Momentum misto | Compressione / triangolo | -1 | 0 / NON ATTIVO | Triplo minimo / CANDIDATO | Triplo massimo / MATURO | 0.07107 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo      | Triplo minimo   | Adam/Eve Bottom                          | Doppio massimo   | Triplo massimo   | Adam/Eve Top                        |   Punteggio pattern |
|:--------|:-------------------|:----------------|:-----------------------------------------|:-----------------|:-----------------|:------------------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Eve and Adam Top — TARGET RAGGIUNTO | 0 |
| SOL | CONFERMATO RECENTE | CANDIDATO | Adam and Eve Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Eve and Adam Top — CANDIDATO | 2 |
| DOGE | ASSENTE | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 47.36 | 428.977 | 61.834 | 64.590 | 73.743 | -9,11% | -9,99% | -4,61% | -16,21% |
| SOL | 49.94 | -0.24939 | 76,37 | 74,18 | 91,52 | -5,92% | -17,82% | 7,20% | -10,16% |
| DOGE | 33.65 | 0.00037 | 0.07432 | 0.08339 | 0.10075 | -13,40% | -16,15% | -18,73% | -24,00% |

## Dettaglio asset

### BTC

- Prezzo: **62.682 $**
- Punteggio tecnico: **1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.725e+04 -> 6.554e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 47.4.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-06 82.792 -> 2026-07-01 57.748; livello più vicino 23.6% a 63.658; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (TARGET RAGGIUNTO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **65.544**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 7,28%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 7,28%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 7,28%; prezzo sotto neckline.
- Doppio massimo: **TARGET RAGGIUNTO** (0)
  - Due massimi simili vicino a 79.488 tra 2026-04-27 e 2026-05-26. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (47 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 70.429; progresso corrente: 271,03%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 70.429; breakout 2026-05-27 (47g); progresso 271,03%; prezzo sotto neckline.
- Triplo massimo: **TARGET RAGGIUNTO** (0)
  - Tre massimi simili vicino a 79.468 dal 2026-04-17 al 2026-05-26. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (47 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 70.449; progresso corrente: 272,25%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 70.449; breakout 2026-05-27 (47g); progresso 272,25%; prezzo sotto neckline.
- Eve and Adam Top: **TARGET RAGGIUNTO** (0)
  - Pattern Eve and Adam Top vicino a 82.792 dal 2026-04-22 al 2026-05-06. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (47 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 67.125; progresso corrente: 156,72%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 67.125; breakout 2026-05-27 (47g); progresso 156,72%; prezzo sotto neckline.

### SOL

- Prezzo: **76,29 $**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 67.92 -> 64.42. Ultimi massimi: 74.89 -> 83.81.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-06-06 60,41 -> 2026-07-04 83,81; livello più vicino 38.2% a 74,87; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+2**
  - rialzista dominante: Doppio minimo (CONFERMATO RECENTE, +2); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **64,42**
- Resistenza più vicina: **83,81**

Pattern classici e ciclo di vita:

- Doppio minimo: **CONFERMATO RECENTE** (+2)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (12 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 2,26%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (12g); progresso 2,26%; prezzo vicino alla neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,41 dal 2026-04-12 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 51 giorni.
  - neckline 98,27; target 115,13; distanza dalla neckline 28,81%; prezzo sotto neckline.
- Adam and Eve Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Adam and Eve Bottom vicino a 60,41 dal 2026-06-06 al 2026-06-25. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (12 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 2,26%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (12g); progresso 2,26%; prezzo vicino alla neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 87,79 tra 2026-05-21 e 2026-07-04. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 60,41; target 33,04; distanza dalla neckline 26,28%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 88,05 dal 2026-04-27 al 2026-07-04. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 60,41; target 32,78; distanza dalla neckline 26,28%; prezzo sopra neckline.
- Eve and Adam Top: **CANDIDATO** (0)
  - Pattern Eve and Adam Top vicino a 87,79 dal 2026-05-21 al 2026-07-04. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 60,41; target 33,04; distanza dalla neckline 26,28%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07214 $**
- Punteggio tecnico: **-5 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 0.06961 -> 0.07107. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 33.7.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-08 0.07107; livello più vicino 23.6% a 0.08220; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **-1**
  - rialzista dominante: Triplo minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.07107**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **ASSENTE** (0)
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.09274 dal 2026-04-19 al 2026-05-28. Neckline stimata: 0.11825. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 46 giorni.
  - neckline 0.11825; target 0.14377; distanza dalla neckline 63,92%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.09818 dal 2026-05-08 al 2026-05-23. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.11825. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 51 giorni.
  - neckline 0.11825; target 0.13833; distanza dalla neckline 63,92%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (19 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 30,34%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (19g); progresso 30,34%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (19 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 33,56%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (19g); progresso 33,56%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                  |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-07-01 | 63.658 | 67.315 | 70.270 | 73.225 | 77.433 | 23.6% / 63.658 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-07-04 | 78,29 | 74,87 | 72,11 | 69,35 | 65,42 | 38.2% / 74,87 | TENUTO | neckline rialzista, invalidazione rialzista | +1 |
| DOGE | DOWN 2026-05-14 -> 2026-07-08 | 0.08220 | 0.08909 | 0.09466 | 0.10023 | 0.10816 | 23.6% / 0.08220 | NON ATTIVO | nessuna confluenza indipendente | 0 |

## Stati del ciclo di vita

- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; punteggio 0.
- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; peso prudente ±1.
- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; peso massimo prudente ±2.
- **MATURO**: breakout più vecchio di 14 giorni e ancora valido; peso ridotto ±1.
- **TARGET RAGGIUNTO**: movimento teorico già sviluppato; punteggio 0.
- **INVALIDATO**: recupero stabile della neckline contro il pattern; punteggio 0.

Per evitare doppio conteggio, nel punteggio entra soltanto il miglior pattern rialzista e il miglior pattern ribassista. Doppio, triplo e Adam/Eve che descrivono la stessa struttura non vengono più sommati tutti insieme.

## Come leggere il punteggio

- Da +7 a +12: forte confluenza tecnica rialzista.
- Da +3 a +6: struttura costruttiva, ma serve ancora conferma.
- Da -2 a +2: situazione mista / neutrale.
- Da -6 a -3: struttura tecnica debole.
- Da -12 a -7: forte confluenza tecnica ribassista.

Nota importante: questo report non è una previsione da solo. È un filtro tecnico da leggere insieme a scanner frattale, market regime, futures e RSI.
<!-- TECHNICAL_STRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:technical_structure -->

<!-- COMPACT_SECTION_START:calibration_readable -->
<details>
<summary><strong>🎯 Stato leggibile accuratezza / calibrazione</strong></summary>

<!-- CALIBRATION_READABLE_START -->

---

# Stato leggibile accuratezza / calibrazione

Report dettagliati:
- [accuracy_report.md](accuracy_report.md)
- [calibration_report.md](calibration_report.md)

## Riassunto semplice

- **BTC**: 0/30 previsioni controllate su 11 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 11 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 11 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 11 | 0 | 0/30 [░░░░░░░░░░] | 11 | RACCOLTA DATI | 2026-08-02 / tra 20 giorni |
| SOL | 11 | 0 | 0/30 [░░░░░░░░░░] | 11 | RACCOLTA DATI | 2026-08-02 / tra 20 giorni |
| DOGE | 11 | 0 | 0/30 [░░░░░░░░░░] | 11 | RACCOLTA DATI | 2026-08-02 / tra 20 giorni |

## Traduzione

- **0/30** significa: lo scanner sta ancora raccogliendo dati.
- **30/30** significa: la calibrazione comincia ad attivarsi.
- **60+** significa: la calibrazione diventa più solida.
- L'email non c'entra con la calibrazione: conta solo che il workflow giri e salvi il diario delle previsioni.

<!-- CALIBRATION_READABLE_END -->

</details>
<!-- COMPACT_SECTION_END:calibration_readable -->

<!-- COMPACT_SECTION_START:data_quality -->
<details>
<summary><strong>✅ Controllo qualità e coerenza dati</strong></summary>

<!-- DATA_QUALITY_COHERENCE_START -->
# Data quality / coherence check

Generato: 2026-07-13 06:28 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 3 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 62.682 $          | 62.682 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07214 $         | 0.07214 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 62.682 $          | 62.682 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07214 $         | 0.07214 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 62.682 $          | 62.682 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07214 $         | 0.07214 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 62.682 $          | 62.682 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07214 $         | 0.07214 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 62.682 $          | 62.682 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07214 $         | 0.07214 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | WARN    | 62.682 $          | 62.839 $        | +0,2502%     |
| Exchange Microstructure | SOL     | price             | WARN    | 76,29 $           | 75,84 $         | -0,5872%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.07214 $         | 0.07198 $       | -0,2218%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 76,29 $           | 76,29 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 76,29 $           | 76,29 $         | +0,0000%     |

## Integrità Technical / Classic Visual

- Fibonacci strutturato: **OK**
- Candidati senza falso progresso target: **OK**
- Classic Visual allineato al lifecycle Technical: **OK**

## Controllo codifica UTF-8

Nessun indicatore comune di mojibake trovato.

## File strutturati

- Snapshot condiviso completo: **OK**
- Scanner summary: **OK**
- Price coherence sync: **OK**
- Dati exchange / microstruttura: **OK**

Il workflow può continuare, ma gli avvisi sopra vanno verificati.
<!-- DATA_QUALITY_COHERENCE_END -->

</details>
<!-- COMPACT_SECTION_END:data_quality -->
