<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-10 00:57 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: spot, long, short e rischio. Ora segue il Global Confluence aggiornato e non assegna più punti automatici al Lifecycle EMA200.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | NEUTRALE / COSTRUTTIVO | HOLD / ACCUMULA SOLO SU PULLBACK | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +4 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -10 | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+2**, spot = **HOLD / ACCUMULA SOLO SU PULLBACK**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+4**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-10**, spot = **VENDI PARZIALE / STAI FUORI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot: **HOLD / ACCUMULA SOLO SU PULLBACK**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Conferme sopra 83,81 / 106,11 / 114,88.
- Invalidazioni: Allarmi sotto 74,05 / 64,42 / 62,19.

### DOGE

- Global Confluence: **-10**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot: **VENDI PARZIALE / STAI FUORI**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07923 migliora, ma resta asset debole finché scanner e struttura non girano.
- Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.

## Nota semplice

- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 5; EMA200 circa 113,51 $; upside verso EMA200 +45,58%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- MODULE_ACCURACY_START -->
# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-10 00:57 UTC

Questo report salva ogni giorno i segnali dei moduli e controlla ogni giorno quali orizzonti sono maturati.

La calibrazione ora controlla questi orizzonti:

- **1g / 2g / 3g** = feedback rapidissimo
- **5g / 7g / 10g** = feedback settimanale
- **14g / 21g** = feedback swing
- **30g / 45g / 60g** = feedback più serio

Moduli controllati:

- Global Confluence
- Scanner grezzo
- Market regime
- Struttura tecnica
- Classic technical confirmation
- Frattale SOL/BTC, solo per SOL

Nota: i controlli vengono aggiornati **ogni giorno**, ma i pesi del Global non devono cambiare automaticamente sotto 30 controlli. Prima si osserva, poi si calibra.

Segnali totali salvati: **6**.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Scanner | Market | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-10 | BTC | 63.045,46 | +2 | +1 | +3 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-10 | DOGE | 0.07278 | -10 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-10 | SOL | 78,00 | +4 | -1 | +2 | +1 | 0 | +1 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-07-09 | BTC | 63.234,86 | +6 | +3 | +3 | -1 | 0 | 0 | ACCUMULA SU PULLBACK / NO SHORT |
| 2026-07-09 | DOGE | 0.07285 | -10 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-09 | SOL | 78,02 | +4 | -1 | +2 | +1 | 0 | +1 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 2g | 2026-07-11 | domani |
| SOL | 2026-07-09 | 2g | 2026-07-11 | domani |
| DOGE | 2026-07-09 | 2g | 2026-07-11 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | 0,00% | -0,31% | -0,31% | FEEDBACK RAPIDO |
| BTC | 2g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 3g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | 0,00% | -0,10% | -0,10% | FEEDBACK RAPIDO |
| SOL | 2g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 3g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 1 | 100,00% | -0,11% | +0,11% | FEEDBACK RAPIDO |
| DOGE | 2g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 3g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | 1 | 100,00% | -0,31% | +0,31% | -0,34% | -0,08% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | 1 | 100,00% | -0,11% | +0,11% | -0,13% | +0,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner | 1 | 100,00% | -0,11% | +0,11% | -0,13% | +0,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime | 1 | 100,00% | -0,11% | +0,11% | -0,13% | +0,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | 1 | 100,00% | -0,11% | +0,11% | -0,13% | +0,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | 1 | 100,00% | -0,11% | +0,11% | -0,13% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner | 1 | 100,00% | -0,10% | +0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |

## Come leggerlo

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

Questo report non cambia ancora automaticamente i pesi del Global Confluence. Serve prima a capire quali moduli funzionano davvero sui vari orizzonti.

Nota tecnica: le colonne data sono forzate come testo, quindi non deve più apparire l'errore `Invalid value 'YYYY-MM-DD' for dtype 'float64'`.
<!-- MODULE_ACCURACY_END -->

<!-- GLOBAL_WEIGHT_CALIBRATION_START -->
# Calibrazione pesi Global Confluence

Generato: 2026-07-10 00:57 UTC

Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)

Questo blocco controlla se, col tempo, i moduli del Global Confluence meritano più peso, meno peso o peso invariato.

Ora legge il nuovo `module_signal_tracker_metrics.csv`, quindi include anche i nuovi orizzonti **1g / 2g / 3g / 5g / 7g / 10g / 14g / 21g / 30g / 45g / 60g** e il modulo **Classic technical**.

Regola principale:

- sotto **30 controlli**: osservazione, nessuna modifica pesi
- da **30 controlli**: prima calibrazione leggera
- da **60 controlli**: lettura utile
- da **100+ controlli**: possibile proposta prudente di modifica pesi

## Sintesi per asset

| Asset | Segnali salvati | Stato | Controlli max | Righe 30+ | Righe 60+ | Righe 100+ | Miglior modulo attuale | Orizzonte | Accuratezza | Return corretto direzione | Lettura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 2 | FEEDBACK RAPIDO | 1 | 0 | 0 | 0 | Tecnico | 1g | 100,00% | +0,31% | feedback rapido: utile da osservare, non da pesare |
| SOL | 2 | FEEDBACK RAPIDO | 1 | 0 | 0 | 0 | Scanner | 1g | 100,00% | +0,10% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 2 | FEEDBACK RAPIDO | 1 | 0 | 0 | 0 | Global confluence | 1g | 100,00% | +0,11% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni moduli con controlli maturati

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Global confluence | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Scanner | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Market regime | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 1 | 100,00% | +0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Global confluence | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Scanner | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Market regime | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Global confluence | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Scanner | 1 | 100,00% | +0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Market regime | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo | Controlli totali | Accuratezza media | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Global confluence | 1 | 0,00% | -0,31% |
| BTC | BREVE | Scanner | 1 | 0,00% | -0,31% |
| BTC | BREVE | Market regime | 1 | 0,00% | -0,31% |
| BTC | BREVE | Tecnico | 1 | 100,00% | +0,31% |
| DOGE | BREVE | Global confluence | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Scanner | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Market regime | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Tecnico | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Classic technical | 1 | 100,00% | +0,11% |
| SOL | BREVE | Global confluence | 1 | 0,00% | -0,10% |
| SOL | BREVE | Scanner | 1 | 100,00% | +0,10% |
| SOL | BREVE | Market regime | 1 | 0,00% | -0,10% |
| SOL | BREVE | Tecnico | 1 | 0,00% | -0,10% |
| SOL | BREVE | Frattale SOL | 1 | 0,00% | -0,10% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 14 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 18 | in attesa di controlli maturati |
| BTC | SWING | 12 | in attesa di controlli maturati |
| BTC | MEDIO | 18 | in attesa di controlli maturati |
| DOGE | BREVE | 13 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 18 | in attesa di controlli maturati |
| DOGE | SWING | 12 | in attesa di controlli maturati |
| DOGE | MEDIO | 18 | in attesa di controlli maturati |
| SOL | BREVE | 13 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 18 | in attesa di controlli maturati |
| SOL | SWING | 12 | in attesa di controlli maturati |
| SOL | MEDIO | 18 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: ci sono pochi controlli, quindi il dato è rumore utile solo da monitorare.
- **PESO OK**: il modulo sta aiutando, ma non abbastanza da aumentare peso.
- **MANTIENI / OSSERVA**: risultato vicino al neutro.
- **NON AUMENTARE**: il modulo non sta ancora dimostrando abbastanza utilità.
- **POSSIBILE AUMENTO LEGGERO**: modulo buono, ma la modifica resta prudente.
- **POSSIBILE RIDUZIONE PESO**: modulo debole su quell’orizzonte, da ridurre solo con dati maturi.

Nota importante: questo file **non modifica automaticamente** `global_confluence_report.py`.
Produce solo una raccomandazione leggibile. La modifica reale dei pesi va fatta a mano, dopo abbastanza dati.

## Stato attuale

Ci sono già alcuni controlli brevi, ma siamo ancora in feedback rapido. Non bisogna modificare pesi del Global.
<!-- GLOBAL_WEIGHT_CALIBRATION_END -->

<!-- RISK_CALIBRATION_START -->
# Calibrazione rischio spot / leva

Report completo: [risk_calibration_report.md](risk_calibration_report.md)

Questo blocco controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio   |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:---------------|
| BTC     |          2 |               0 |           2 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |          2 |               0 |           2 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |          2 |               0 |           2 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | MEDIO          | rischio leva relativamente più gestibile, ma non nullo                  |
| SOL     | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-10 00:57 UTC

Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.

Moduli letti:

- Scanner frattale/statistico a 30 giorni
- Scanner path / cono previsionale
- Market regime match
- Struttura tecnica classica precedente
- Classic technical confirmation, nuovo filtro tecnico completo
- Frattale BTC 2022 vs SOL 2026, solo per SOL
- Fractal path tracker, solo per SOL
- RSI top-cycle, soprattutto per SOL
- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL
- Futures / liquidazioni
- Cambiamento giornaliero

Nota importante: **Lifecycle EMA200 viene letto e mostrato, ma ora vale sempre 0 punti nel Global Confluence**. Serve come contesto, non come conferma operativa.

Nota nuovo modulo: **Classic technical confirmation pesa massimo ±1** perché è un filtro di conferma e in parte si sovrappone alla struttura tecnica già esistente.

## Sintesi operativa

| Asset | Punteggio | Confluenza | Bias | Affidabilità | Azione coerente | Conferme | Invalidazioni |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Conferme sopra 83,81 / 106,11 / 114,88. | Allarmi sotto 74,05 / 64,42 / 62,19. |
| DOGE | -10 | NEGATIVA | Ribassista | MEDIA / ALTA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.07923 migliora, ma resta asset debole finché scanner e struttura non girano. | Sotto 0.06961 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner | Scanner path | Market regime | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | 0 | +3 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |
| SOL | -1 | 0 | +2 | +1 | 0 | +1 | 0 | +1 | 0 | 0 | 0 | +4 |
| DOGE | -3 | 0 | -3 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | -10 |

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Scanner: **+1** — Casi positivi 72,50%, return centrale 30g n/a. Direzione scanner: n/a.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 0. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 16, positivi 30g 100,00%, return p50 +23,86%.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend trend ribassista, struttura struttura ribassista con massimi e minimi decrescenti, divergenza divergenza rialzista rsi, Wyckoff possibile accumulazione.
- Classic technical: **0** — Score classico -3/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff SPRING / TEST POSSIBILE, rischio MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Futures: **0** — Lettura futures Rischio sotto, forza 4/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e frattali. Il modulo lifecycle/EMA200 resta utile come contesto, ma non viene più usato per aumentare il punteggio Global.

Dettaglio moduli:

- Scanner: **-1** — Casi positivi 42,50%, return centrale 30g n/a. Direzione scanner: n/a.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 0. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 19, positivi 30g 63,16%, return p50 +0,92%.
- Tecnico: **+1** — Score tecnico 1/12, verdetto neutrale / misto, trend trend misto, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff RANGE / FASE NON CHIARA, rischio MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **+1** — Verdetto PARZIALMENTE SI, somiglianza +73,76%, tracking FRATTALE STABILE, fase FASE ANTICIPATA, rischio MEDIO / ALTO.
- Fractal path: **0** — Tracking operativo, ma nessuna milestone settimanale ancora verificata. Il modulo non pesa finché non maturano abbastanza controlli.
- RSI top-cycle: **+1** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 5, bias SQUEEZE SETUP FORTE, EMA200 113,51 $, upside EMA200 +45,58%, gap EMA50/EMA200 -1,22%, hit EMA200 12w +23,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Conferme sopra 83,81 / 106,11 / 114,88.

Invalidazioni: Allarmi sotto 74,05 / 64,42 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-10**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche se può fare rimbalzi o spike, la confluenza generale resta negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Scanner: **-3** — Casi positivi 12,50%, return centrale 30g n/a. Direzione scanner: n/a.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 0. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **-3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 30, positivi 30g 6,67%, return p50 -27,25%.
- Tecnico: **-3** — Score tecnico -10/12, verdetto ribassista tecnico, trend trend ribassista, struttura struttura ribassista con massimi e minimi decrescenti, divergenza divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione.
- Classic technical: **-1** — Score classico -9/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, rischio BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.07923 migliora, ma resta asset debole finché scanner e struttura non girano.

Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.


## Come leggere il punteggio

- +7 o più: confluenza positiva forte.
- Da +3 a +6: confluenza moderatamente positiva.
- Da 0 a +2: confluenza parziale o mista.
- Da -1 a -3: confluenza debole o fragile.
- -4 o meno: confluenza negativa.

Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0.
Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero.

Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze resta nel report, ma pesa **0** nel Global perché EMA50/EMA200 e target EMA200 sono contesto, non conferme dirette di prezzo.

Nota Classic technical: il nuovo modulo è utile per capire se il setup è confermato davvero, ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente.
<!-- GLOBAL_CONFLUENCE_END -->

<!-- BTC_SOL_FRACTAL_START -->

---

# Frattale mirato: BTC 2022 vs SOL 2026

Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)

Ultima candela SOL usata: **10 luglio 2026**

## Verdetto: PARZIALMENTE SI

- **Fase attuale:** FASE ANTICIPATA
- **Somiglianza totale:** +73,76%
- **Affidabilita:** MEDIA
- **Rischio fase:** MEDIO / ALTO
- **Trend tracking:** FRATTALE STABILE
- **Sintesi:** SOL sta seguendo abbastanza il frattale BTC 2022, ma non in modo perfetto.
- **SOL e al giorno:** 33 dal bottom usato.
- **Giorno BTC equivalente:** 2022-12-24
- **Prossimo step:** Prossimo step previsto dal frattale: **Laterale / movimento non forte.** Zona bassa stimata: **76,56 $** intorno al **17 luglio 2026**. Zona alta stimata: **78,45 $** intorno al **24 luglio 2026**. Fine step: circa **78,45 $** entro il **24 luglio 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la parte gia successa prima del programma dalla parte che stiamo monitorando davvero.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo: utile, ma gia conosciuto.
- **Da inizio programma** = verifica reale: serve a capire se il frattale sta reggendo dopo che lo abbiamo iniziato a seguire.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Errore ultimo giorno | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 10 luglio 2026 | 7 | +56,20% | +21,90% | +17,45% | STACCATO / MOLTO IN ANTICIPO |
| Totale dal bottom | 6 giugno 2026 -> 10 luglio 2026 | 34 | +81,41% | +9,29% | +17,45% | ABBASTANZA ALLINEATO |

Nota: **Aderenza prezzo** è uno score semplice basato sulla distanza media dalla linea BTC-scalata. Non sostituisce la somiglianza totale ufficiale, ma rende chiaro se SOL è vicino, sopra o sotto il percorso BTC equivalente.

## Lettura operativa veloce

Fase anticipata: ingresso migliore come prezzo, ma certezza ancora bassa. Ha senso ragionare a tranche, non tutto insieme.

| Voce | Risposta | Perche |
| --- | --- | --- |
| Spot anticipato | SI, ma a tranche | La zona e ancora prima della conferma piena. |
| Aggiunta su conferma | SI | Aggiunta sensata se rompe e tiene 106,11 $. |
| Seconda conferma | 114,88 $ | Sopra questa zona il frattale diventa molto piu credibile. |
| Rischio inseguimento | BASSO / MEDIO | Non sei ancora troppo in ritardo, ma serve invalidazione chiara. |
| Invalidazione soft | 74,05 $ | Sotto questa zona il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Sotto questa zona il frattale e quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dal bottom | 491,43 $ |
| Target ciclo base da oggi | 577,20 $ |
| Massimo percorso base | 577,20 $ (22 aprile 2029) |
| Massimo percorso beta | 2.330 $ (22 aprile 2029) |

## Grafici

### Grafico frattale sovrapposto

![Frattale BTC 2022 vs SOL 2026](btc_2022_vs_sol_2026_fractal_chart.png)

### Grafico proiezione SOL

![Proiezione SOL BTC 2022](btc_2022_vs_sol_2026_projection_chart.png)

### Grafico ciclo BASE fino al top BTC 2025

![Ciclo base SOL BTC 2025](btc_2022_vs_sol_2026_cycle_base_chart.png)

Nel report completo trovi anche il grafico beta separato e il grafico in scala logaritmica.

### Grafico tracking giornaliero

![Tracking frattale BTC SOL](btc_2022_vs_sol_2026_tracking_chart.png)

## Livelli chiave

| Livello | Prezzo | Lettura |
| --- | --- | --- |
| Prima conferma | 106,11 $ | Migliora il frattale. |
| Seconda conferma | 114,88 $ | Scenario rialzista piu credibile. |
| Invalidazione soft | 74,05 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone BTC 2022 si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL prevista | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 17 luglio 2026 | -1,78% | 76,56 $ | 76,56 $ | 78,28 $ |
| 14 giorni | 24 luglio 2026 | +0,64% | 78,45 $ | 76,56 $ | 78,45 $ |
| 30 giorni | 9 agosto 2026 | +36,13% | 106,11 $ | 76,56 $ | 106,11 $ |
| 60 giorni | 8 settembre 2026 | +43,57% | 111,92 $ | 76,56 $ | 114,88 $ |
| 90 giorni | 8 ottobre 2026 | +63,19% | 127,20 $ | 76,56 $ | 131,09 $ |
| 120 giorni | 7 novembre 2026 | +63,77% | 127,66 $ | 76,56 $ | 141,05 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 10 luglio 2026 -> 24 luglio 2026 | +0,64% | 76,56 $ (17 luglio 2026) | 78,45 $ (24 luglio 2026) | 78,45 $ | Laterale / movimento non forte. |
| Step 2 - primo mese | 25 luglio 2026 -> 9 agosto 2026 | +36,13% | 79,08 $ (25 luglio 2026) | 106,11 $ (9 agosto 2026) | 106,11 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 10 agosto 2026 -> 8 settembre 2026 | +43,57% | 100,17 $ (27 agosto 2026) | 114,88 $ (6 settembre 2026) | 111,92 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 9 settembre 2026 -> 8 ottobre 2026 | +63,19% | 93,40 $ (24 settembre 2026) | 131,09 $ (7 ottobre 2026) | 127,20 $ | Spinta rialzista abbastanza pulita. |

Nota: questa e una proiezione analogica. Conta soprattutto se SOL rispetta i livelli di conferma e invalidazione.

<!-- BTC_SOL_FRACTAL_END -->

<!-- RSI_TOP_CYCLE_START -->

---

# RSI top-cycle warning - SOL

Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)

Questo filtro controlla se RSI weekly/monthly si stanno avvicinando alla trendline alta che puo segnalare esaurimento ciclo.

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 77,95 $ |  |
| Weekly RSI | 40,58 / top-line 56,32 | LONTANO DALLA TOP-LINE - normale |
| Monthly RSI | 41,39 / top-line 48,69 | IN AVVICINAMENTO - troppo ripida per proiezione 2029 |
| Target ciclo base | 577,20 $ | Avanzamento +13,50% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI serve piu avanti. |

## Lettura semplice

- Weekly: RSI weekly e ancora basso e lontano dalla trendline di esaurimento ciclo.
- Monthly: RSI monthly si sta avvicinando alla trendline, ma non la sta ancora testando.
- Confluenza prezzo + RSI: **BASSO**

Questo non e un segnale di entrata. Serve soprattutto per riconoscere piu avanti una possibile zona top, per esempio se SOL si avvicina ai target 500/600 e RSI weekly/monthly tornano sulla top-line.

## Grafici RSI

![SOL weekly RSI top-line](rsi_top_cycle_SOL_weekly.png)

![SOL monthly RSI top-line](rsi_top_cycle_SOL_monthly.png)

<!-- RSI_TOP_CYCLE_END -->

<!-- SOL_ONCHAIN_METRICS_START -->

---

# SOL on-chain metrics

Report separato completo: **[sol_onchain_metrics_report.md](sol_onchain_metrics_report.md)**

| Voce | Valore |
| --- | --- |
| Score on-chain | 0 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 77,88 $ |
| TVL Solana | 4,94 mld $ |
| TVL 7g | +0,66% |
| DEX volume 24h | 1,79 mld $ |
| Fees 24h | 8,25 mln $ |
| Stablecoin su Solana | 15,39 mld $ |
| Stake ratio | 68,16% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE**

Questo blocco non sostituisce il frattale SOL/BTC: serve come filtro per capire se il movimento è sostenuto anche da attività on-chain.

<!-- SOL_ONCHAIN_METRICS_END -->

<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->

---

# Major alt lifecycle squeeze - SOL

Report separato completo: **[major_alt_lifecycle_squeeze_report.md](major_alt_lifecycle_squeeze_report.md)**

| Voce                      | Valore                                              |
|:--------------------------|:----------------------------------------------------|
| Lifecycle squeeze score   | 5                                                   |
| Bias                      | SQUEEZE SETUP FORTE                                 |
| Azione coerente           | CONTESTO BUONO VERSO EMA200, MA NON PESA NEL GLOBAL |
| Peso suggerito Global     | 0                                                   |
| Trend squeeze             | STABILE / DA CONFERMARE                             |
| Trend squeeze score       | 0                                                   |
| Confronto precedente      | 2026-07-09                                          |
| Fonte prezzi              | Yahoo Finance SOL-USD weekly                        |
| Prezzo SOL                | 77,97 $                                             |
| EMA200 weekly target      | 113,51 $                                            |
| Upside verso EMA200       | +45,58%                                             |
| Distanza prezzo da EMA200 | -31,31%                                             |
| Gap EMA50/EMA200          | -1,22%                                              |
| Stato cross               | EMA50/EMA200 SOVRAPPOSTE / INCROCIO IN CORSO        |
| RSI weekly                | 40,59                                               |
| Età SOL                   | 6,2 anni                                            |
| Analoghi storici usati    | 30                                                  |
| Max analoghi per asset    | 3                                                   |
| Hit EMA200 12w analoghi   | +23,33%                                             |
| Max gain mediano 12w      | +23,06%                                             |
| Drawdown mediano 12w      | -24,14%                                             |

Lettura semplice:

**CONTESTO BUONO VERSO EMA200, MA NON PESA NEL GLOBAL**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-10 00:57 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-10 00:53:46 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non Ã¨ una previsione certa. Ã uno scanner statistico: guarda situazioni simili giÃ  successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: nessun cambiamento forte rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +72.50% | +2.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +42.50% | 0.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | RIBASSISTA | +12.50% | 0.00 punti |

<!-- DAILY_CHANGE_END -->

<!-- BOUNCE_AFTER_DRAWDOWN_START -->

---

# Sequenze pratiche: rimbalzo / dump

Report separato completo: [bounce_after_drawdown_report.md](bounce_after_drawdown_report.md)

Questa sezione risponde subito a due domande:

- **Se scende, è una zona di rimbalzo?**
- **Se sale forte, è una zona da prendere profitto?**

| Asset | Scende a | Target rimbalzo | % casi rimbalzo | Movimento reale | Lettura discesa | Sale a | Target dump | % casi dump | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.817 $ | 69.262 $ | +12,50% | +15,79% | rimbalzo poco frequente | 69.262 $ | 59.817 $ | +16,00% | -13,64% | spike storicamente più resistente |
| SOL | 73,93 $ | 85,60 $ | +11,11% | +15,79% | rimbalzo poco frequente | 85,60 $ | 73,93 $ | +26,32% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06905 $ | 0,07995 $ | +8,33% | +15,79% | rimbalzo poco frequente | 0,07995 $ | 0,06905 $ | +69,23% | -13,64% | spike spesso scaricato |

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

- **BTC: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 2 poi sono rimbalzati fino a +10,00%. Percentuale: +12,50% (2/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 4 poi sono scaricati a -5,00%. Percentuale: +16,00% (4/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +11,11% (3/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 5 poi sono scaricati a -5,00%. Percentuale: +26,32% (5/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +8,33% (3/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 13 prima sono saliti a +10,00%. Tra quei 13, 9 poi sono scaricati a -5,00%. Percentuale: +69,23% (9/13). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike spesso scaricato.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

# Come leggere questo report

Leggilo sempre in questo ordine:

1. **Direzione piÃ¹ probabile**: ti dice se storicamente era piÃ¹ facile salita, discesa o incertezza.
2. **Casi positivi / negativi**: ti dice la percentuale storica di salita o discesa dopo 30 giorni.
3. **Return 30d**: ti dice dove potrebbe stare il prezzo fra 30 giorni.
4. **Drawdown 30d**: ti dice quanto potrebbe scendere durante quei 30 giorni.
5. **Max gain 30d**: ti dice quanto potrebbe salire durante quei 30 giorni.
6. **Scanner autocalibrato**: dopo abbastanza dati, confronta previsione e realtÃ  e corregge la lettura.

La frase piÃ¹ importante Ã¨ questa:

> **Return = prezzo finale dopo 30 giorni. Drawdown = discesa durante il mese. Max gain = rialzo durante il mese.**

---

# Scheda veloce: cosa sono i percentili

I **percentili** sono solo un modo per trasformare i 40 casi storici simili in scenari semplici.

## Traduzione semplice

- **Percentile 10%** = molto male / scenario brutto.
- **Percentile 25%** = male / scenario negativo.
- **Percentile 50%** = normale / scenario centrale. Ã il piÃ¹ importante.
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

- **Return 50% â 81 $**: fra 30 giorni lo scenario normale Ã¨ circa 81 $.
- **Drawdown 50% â 77 $**: durante il mese puÃ² scendere normalmente verso 77 $.
- **Max gain 50% â 92 $**: durante il mese puÃ² fare uno spike normale verso 92 $.

Quindi puÃ² salire e scendere durante il mese, ma il **return** guarda solo dove finisce dopo 30 giorni.

---

# Lettura velocissima

Questa Ã¨ la parte da leggere per prima. Ti dice subito se lo scenario Ã¨ piÃ¹ da salita, discesa o incertezza.

## Bitcoin
- Direzione piÃ¹ probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto Ã¨ netto il segnale: **forte**
- Prezzo attuale: **62.965,47 $**
- Return normale fra 30 giorni: **67.303,54 $** (6,89%)
- Drawdown normale durante il mese: **60.486,53 $** (-3,94%)
- Drawdown brutto da rispettare: **57.053,21 $** (-9,39%)
- Max gain normale durante il mese: **73.630,62 $** (16,94%)
- Max gain buono / take profit ottimistico: **83.515,53 $** (32,64%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione piÃ¹ probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione piÃ¹ probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **42,50%**
- Casi negativi / discesa storica: **57,50%**
- Quanto Ã¨ netto il segnale: **debole**
- Prezzo attuale: **77,82 $**
- Return normale fra 30 giorni: **76,62 $** (-1,54%)
- Drawdown normale durante il mese: **69,74 $** (-10,39%)
- Drawdown brutto da rispettare: **58,13 $** (-25,30%)
- Max gain normale durante il mese: **83,88 $** (7,79%)
- Max gain buono / take profit ottimistico: **96,59 $** (24,12%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione piÃ¹ probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione piÃ¹ probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **12,50%**
- Casi negativi / discesa storica: **87,50%**
- Quanto Ã¨ netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,06 $** (-20,25%)
- Drawdown normale durante il mese: **0,05 $** (-28,61%)
- Drawdown brutto da rispettare: **0,05 $** (-37,60%)
- Max gain normale durante il mese: **0,08 $** (4,88%)
- Max gain buono / take profit ottimistico: **0,08 $** (11,33%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione piÃ¹ probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi Ã¨ misto. Alcuni asset possono avere lettura diversa, quindi Ã¨ meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin â mappa semplice dei prossimi 30 giorni

**Semaforo:** ð¢ VERDE / Favorevole
**Prezzo attuale:** 62.965,47 $

**Direzione piÃ¹ probabile a 30 giorni:** **SALITA**
- ProbabilitÃ  storica di salita: **72,50%**
- ProbabilitÃ  storica di discesa: **27,50%**
- Quanto Ã¨ netto il segnale: **forte**

## Come leggere questa parte

- **ProbabilitÃ  storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **ProbabilitÃ  storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto Ã¨ netto il segnale** = quanto Ã¨ grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non Ã¨ vicino al 50/50.

La lettura principale Ã¨ rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni piÃ¹ spesso di quanto abbia chiuso sotto.

## 1. Return 30d â prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **48.588,16 $** (-22,83%)
- Se va male: **61.923,79 $** (-1,65%)
- Scenario normale: **67.303,54 $** (6,89%)
- Se va bene: **77.168,98 $** (22,56%)
- Se va molto bene: **90.512,82 $** (43,75%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d â discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non Ã¨ il prezzo finale: Ã¨ il punto piÃ¹ basso che il prezzo puÃ² toccare durante il mese.

- Discesa normale: **60.486,53 $** (-3,94%)
- Discesa brutta: **57.053,21 $** (-9,39%)
- Discesa molto brutta: **42.556,58 $** (-32,41%)

**Come leggerlo:** se usi leva, questa Ã¨ la parte piÃ¹ importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese puÃ² prima scendere qui.

## 3. Max gain 30d â rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non Ã¨ il prezzo finale: puÃ² essere anche solo uno spike temporaneo.

- Rialzo normale: **73.630,62 $** (16,94%)
- Rialzo buono: **83.515,53 $** (32,64%)
- Rialzo molto forte: **102.392,60 $** (62,62%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale Ã¨ piÃ¹ realistico; il rialzo molto forte Ã¨ possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **60.486,53 $** e uno spike normale intorno a **73.630,62 $**.

La chiusura a 30 giorni era piÃ¹ spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale Ã¨ favorevole.

Nota leva BTC: se la liquidazione Ã¨ vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo puÃ² recuperare dopo, ma la leva puÃ² saltare prima.

---

# Solana â mappa semplice dei prossimi 30 giorni

**Semaforo:** ð¡ GIALLO / Incerto
**Prezzo attuale:** 77,82 $

**Direzione piÃ¹ probabile a 30 giorni:** **INCERTO**
- ProbabilitÃ  storica di salita: **42,50%**
- ProbabilitÃ  storica di discesa: **57,50%**
- Quanto Ã¨ netto il segnale: **debole**

## Come leggere questa parte

- **ProbabilitÃ  storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **ProbabilitÃ  storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto Ã¨ netto il segnale** = quanto Ã¨ grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non Ã¨ vicino al 50/50.

La lettura principale Ã¨ incerta, con segnale debole. Nei casi storici simili non c'Ã¨ stato un vantaggio chiaro nÃ© per salita nÃ© per discesa.

## 1. Return 30d â prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **62,60 $** (-19,56%)
- Se va male: **69,81 $** (-10,29%)
- Scenario normale: **76,62 $** (-1,54%)
- Se va bene: **87,15 $** (11,99%)
- Se va molto bene: **111,87 $** (43,75%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d â discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non Ã¨ il prezzo finale: Ã¨ il punto piÃ¹ basso che il prezzo puÃ² toccare durante il mese.

- Discesa normale: **69,74 $** (-10,39%)
- Discesa brutta: **58,13 $** (-25,30%)
- Discesa molto brutta: **53,71 $** (-30,98%)

**Come leggerlo:** se usi leva, questa Ã¨ la parte piÃ¹ importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese puÃ² prima scendere qui.

## 3. Max gain 30d â rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non Ã¨ il prezzo finale: puÃ² essere anche solo uno spike temporaneo.

- Rialzo normale: **83,88 $** (7,79%)
- Rialzo buono: **96,59 $** (24,12%)
- Rialzo molto forte: **121,22 $** (55,77%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale Ã¨ piÃ¹ realistico; il rialzo molto forte Ã¨ possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **69,74 $** e uno spike normale intorno a **83,88 $**.

La chiusura a 30 giorni Ã¨ incerta: salita 42,50%, discesa 57,50%. Non c'Ã¨ un vantaggio netto.

---

# Dogecoin â mappa semplice dei prossimi 30 giorni

**Semaforo:** ð´ ROSSO / Prudenza
**Prezzo attuale:** 0,07 $

**Direzione piÃ¹ probabile a 30 giorni:** **DISCESA**
- ProbabilitÃ  storica di salita: **12,50%**
- ProbabilitÃ  storica di discesa: **87,50%**
- Quanto Ã¨ netto il segnale: **forte**

## Come leggere questa parte

- **ProbabilitÃ  storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **ProbabilitÃ  storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto Ã¨ netto il segnale** = quanto Ã¨ grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non Ã¨ vicino al 50/50.

La lettura principale Ã¨ ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni piÃ¹ spesso di quanto abbia chiuso sopra.

## 1. Return 30d â prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-36,38%)
- Se va male: **0,05 $** (-29,99%)
- Scenario normale: **0,06 $** (-20,25%)
- Se va bene: **0,07 $** (-4,52%)
- Se va molto bene: **0,07 $** (2,99%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d â discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non Ã¨ il prezzo finale: Ã¨ il punto piÃ¹ basso che il prezzo puÃ² toccare durante il mese.

- Discesa normale: **0,05 $** (-28,61%)
- Discesa brutta: **0,05 $** (-37,60%)
- Discesa molto brutta: **0,04 $** (-43,86%)

**Come leggerlo:** se usi leva, questa Ã¨ la parte piÃ¹ importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese puÃ² prima scendere qui.

## 3. Max gain 30d â rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non Ã¨ il prezzo finale: puÃ² essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (4,88%)
- Rialzo buono: **0,08 $** (11,33%)
- Rialzo molto forte: **0,09 $** (23,46%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale Ã¨ piÃ¹ realistico; il rialzo molto forte Ã¨ possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,05 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni era piÃ¹ spesso negativa: salita 12,50%, discesa 87,50%. Quindi la lettura principale Ã¨ prudente/debole.

---

# Come leggere correttamente i 30 giorni

Ogni report giornaliero Ã¨ una previsione statistica sui **prossimi 30 giorni**.

Ci sono tre dati diversi:

1. **Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.
2. **Drawdown 30d** = quanto potrebbe scendere durante quei 30 giorni.
3. **Max gain 30d** = quanto potrebbe salire al massimo durante quei 30 giorni.

Il prezzo puÃ² salire durante il mese e poi chiudere sotto, oppure scendere prima e poi recuperare. Per chi usa leva, il drawdown Ã¨ spesso piÃ¹ importante del prezzo finale.

# Controllo accuratezza dello scanner

Questa sezione controlla se lo scanner sta funzionando davvero. Ogni giorno viene salvata una previsione. Dopo 30 giorni, lo scanner confronta quella previsione con quello che Ã¨ successo realmente.

## Come leggerla

- **Previsioni giÃ  controllate** = quante vecchie previsioni hanno giÃ  compiuto 30 giorni.
- **Direzione corretta** = quante volte lo scanner ha indovinato salita o discesa finale a 30 giorni.
- **Errore medio scenario centrale** = quanto era distante il prezzo reale dal prezzo centrale previsto.
- **Zona rischio toccata** = quante volte il prezzo Ã¨ sceso fino alla zona di rischio prevista.
- **Zona rialzo toccata** = quante volte il prezzo Ã¨ salito fino alla zona rialzo prevista.

Per ora non ci sono ancora previsioni vecchie di 30 giorni da controllare.
Il controllo vero inizierÃ  automaticamente dopo il primo mese di utilizzo.

---

# Scanner autocalibrato

Questa Ã¨ una sezione separata dalla previsione storica grezza. La previsione grezza resta quella basata sui pattern storici. Qui invece lo scanner guarda i propri errori passati e prova a correggere leggermente la lettura.

## Come funziona

Lo scanner confronta le sue vecchie previsioni con la realtÃ  dopo 30 giorni.

- Se in passato Ã¨ stato troppo ottimista, abbassa la stima.
- Se in passato Ã¨ stato troppo pessimista, alza la stima.
- Se ha sottostimato il drawdown, rende la zona rischio piÃ¹ prudente.
- Se ha sovrastimato gli spike, riduce la zona rialzo calibrata.

La calibrazione non modifica il codice. Crea solo una seconda lettura: **scanner grezzo** contro **scanner corretto dai suoi errori reali**.

Regola: servono almeno **30 previsioni controllate per asset** prima di applicare la calibrazione. Prima di allora mostra solo dati insufficienti.

## Bitcoin

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirÃ  la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirÃ  la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirÃ  la lettura autocalibrata.

---

# Approfondimento tecnico â Bitcoin (BTC-USD)

## Semaforo: ð¢ VERDE / Favorevole

**Prezzo attuale:** 62.965,47 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica piÃ¹ possibilitÃ  di salita che di discesa, ma resta comunque una probabilitÃ , non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte piÃ¹ semplice per capire se storicamente era piÃ¹ probabile salita o discesa.

## Cosa dicono i 40 casi storici piÃ¹ simili

- Somiglianza media dei pattern: **84,89%**
- Rendimento medio dopo 30 giorni: **11,75%**
- Rendimento centrale dopo 30 giorni: **6,89%**
- Discesa media durante i 30 giorni: **-8,02%**
- Massimo rialzo medio durante i 30 giorni: **26,41%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **70.363,42 $**
- Scenario centrale a 30 giorni: **67.303,54 $**
- Zona di rischio media: **57.912,97 $**
- Zona di rialzo media: **79.595,97 $**

**Come leggerli:** scenario centrale = prezzo finale piÃ¹ normale a 30 giorni. Zona rischio = dove puÃ² scendere durante il mese. Zona rialzo = dove puÃ² arrivare durante uno spike.

## Percentili return â prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -22,83% â **48.588,16 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 25%**: -1,65% â **61.923,79 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 50%**: 6,89% â **67.303,54 $**
  - Percentile 50: scenario normale. Ã il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,56% â **77.168,98 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 90%**: 43,75% â **90.512,82 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo puÃ² arrivare circa in questa zona.

## Percentili drawdown â discesa durante i 30 giorni

**Drawdown** significa quanto puÃ² scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,41% â **42.556,58 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo puÃ² scendere fino a questa zona o peggio.
- **Percentile 25%**: -9,39% â **57.053,21 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo puÃ² scendere fino a questa zona.
- **Percentile 50%**: -3,94% â **60.486,53 $**
  - Percentile 50: discesa normale durante il mese. Ã il drawdown centrale.
- **Percentile 75%**: 0,00% â **62.965,47 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% â **62.965,47 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain â rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo puÃ² toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,69% â **66.550,49 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo Ã¨ salito poco.
- **Percentile 25%**: 7,92% â **67.949,98 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,94% â **73.630,62 $**
  - Percentile 50: rialzo normale. Ã lo spike centrale piÃ¹ realistico.
- **Percentile 75%**: 32,64% â **83.515,53 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 62,62% â **102.392,60 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non Ã¨ obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2019-09-24   | 2020-01-01 |        88.92 |        24.17 |          -2.4  |          26.46 |
| LRC-USD         | 2018-09-19   | 2018-12-27 |        87.73 |        95.69 |           0    |         178.55 |
| FIL-USD         | 2023-06-14   | 2023-09-21 |        87.68 |         3.93 |          -1.43 |           7.62 |
| DOT-USD         | 2023-06-15   | 2023-09-22 |        87.32 |        -1.36 |          -9.22 |           6.01 |
| ETH-USD         | 2023-06-15   | 2023-09-22 |        86.71 |         4.4  |          -3.37 |           8.82 |
| KSM-USD         | 2022-03-10   | 2022-06-17 |        86.21 |        11.02 |          -4.93 |          16.96 |
| SAND-USD        | 2023-06-14   | 2023-09-21 |        86.05 |         5.52 |          -3.95 |           9.97 |
| YFI-USD         | 2023-06-14   | 2023-09-21 |        86.05 |         2.83 |          -3.99 |           8.79 |
| ONE-USD         | 2020-01-07   | 2020-04-15 |        85.71 |        14.92 |           0    |          14.92 |
| EOS-USD         | 2023-06-15   | 2023-09-22 |        85.7  |        -2.54 |          -7.18 |           4.82 |

---

# Approfondimento tecnico â Solana (SOL-USD)

## Semaforo: ð¡ GIALLO / Incerto

**Prezzo attuale:** 77,82 $

Solana Ã¨ in una situazione incerta. Lo scanner non vede un vantaggio chiaro nÃ© per la salita nÃ© per la discesa. In questi casi Ã¨ meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **42,50%**
- Casi negativi dopo 30 giorni: **57,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte piÃ¹ semplice per capire se storicamente era piÃ¹ probabile salita o discesa.

## Cosa dicono i 40 casi storici piÃ¹ simili

- Somiglianza media dei pattern: **76,29%**
- Rendimento medio dopo 30 giorni: **6,84%**
- Rendimento centrale dopo 30 giorni: **-1,54%**
- Discesa media durante i 30 giorni: **-13,77%**
- Massimo rialzo medio durante i 30 giorni: **22,35%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **83,15 $**
- Scenario centrale a 30 giorni: **76,62 $**
- Zona di rischio media: **67,11 $**
- Zona di rialzo media: **95,22 $**

**Come leggerli:** scenario centrale = prezzo finale piÃ¹ normale a 30 giorni. Zona rischio = dove puÃ² scendere durante il mese. Zona rialzo = dove puÃ² arrivare durante uno spike.

## Percentili return â prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -19,56% â **62,60 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 25%**: -10,29% â **69,81 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 50%**: -1,54% â **76,62 $**
  - Percentile 50: scenario normale. Ã il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 11,99% â **87,15 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 90%**: 43,75% â **111,87 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo puÃ² arrivare circa in questa zona.

## Percentili drawdown â discesa durante i 30 giorni

**Drawdown** significa quanto puÃ² scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,98% â **53,71 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo puÃ² scendere fino a questa zona o peggio.
- **Percentile 25%**: -25,30% â **58,13 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo puÃ² scendere fino a questa zona.
- **Percentile 50%**: -10,39% â **69,74 $**
  - Percentile 50: discesa normale durante il mese. Ã il drawdown centrale.
- **Percentile 75%**: -1,85% â **76,38 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% â **77,82 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain â rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo puÃ² toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% â **77,82 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo Ã¨ salito poco.
- **Percentile 25%**: 1,40% â **78,91 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 7,79% â **83,88 $**
  - Percentile 50: rialzo normale. Ã lo spike centrale piÃ¹ realistico.
- **Percentile 75%**: 24,12% â **96,59 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 55,77% â **121,22 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non Ã¨ obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-02-21   | 2019-05-31 |        82.23 |       -30.84 |         -30.84 |           0.49 |
| QTUM-USD        | 2018-09-19   | 2018-12-27 |        79.51 |        -2.21 |          -3.68 |          15.25 |
| TRX-USD         | 2018-09-19   | 2018-12-27 |        79.01 |        55.01 |           0    |          55.01 |
| LRC-USD         | 2018-09-19   | 2018-12-27 |        78.4  |        95.69 |           0    |         178.55 |
| ALGO-USD        | 2024-04-14   | 2024-07-22 |        78.39 |       -10.79 |         -27.41 |           0    |
| XLM-USD         | 2020-01-07   | 2020-04-15 |        78.15 |        45.24 |           0    |          62.58 |
| DASH-USD        | 2024-04-15   | 2024-07-23 |        77.74 |        -1.21 |         -16.66 |           1.64 |
| APT-USD         | 2024-09-01   | 2024-12-09 |        77.72 |         0.92 |         -11.47 |           6.42 |
| NEAR-USD        | 2025-12-01   | 2026-03-10 |        77.66 |         6.36 |          -9.61 |          16.07 |
| NEO-USD         | 2023-06-15   | 2023-09-22 |        77.63 |        -5.34 |         -13.04 |           0.22 |

---

# Approfondimento tecnico â Dogecoin (DOGE-USD)

## Semaforo: ð´ ROSSO / Prudenza

**Prezzo attuale:** 0,07 $

Dogecoin richiede prudenza. La statistica dei casi simili indica piÃ¹ possibilitÃ  di discesa che di salita. Con leva, il rischio principale Ã¨ il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **12,50%**
- Casi negativi dopo 30 giorni: **87,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte piÃ¹ semplice per capire se storicamente era piÃ¹ probabile salita o discesa.

## Cosa dicono i 40 casi storici piÃ¹ simili

- Somiglianza media dei pattern: **85,32%**
- Rendimento medio dopo 30 giorni: **-16,88%**
- Rendimento centrale dopo 30 giorni: **-20,25%**
- Discesa media durante i 30 giorni: **-26,07%**
- Massimo rialzo medio durante i 30 giorni: **8,21%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,06 $**
- Scenario centrale a 30 giorni: **0,06 $**
- Zona di rischio media: **0,05 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale piÃ¹ normale a 30 giorni. Zona rischio = dove puÃ² scendere durante il mese. Zona rialzo = dove puÃ² arrivare durante uno spike.

## Percentili return â prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -36,38% â **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 25%**: -29,99% â **0,05 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 50%**: -20,25% â **0,06 $**
  - Percentile 50: scenario normale. Ã il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: -4,52% â **0,07 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo puÃ² stare circa in questa zona.
- **Percentile 90%**: 2,99% â **0,07 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo puÃ² arrivare circa in questa zona.

## Percentili drawdown â discesa durante i 30 giorni

**Drawdown** significa quanto puÃ² scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -43,86% â **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo puÃ² scendere fino a questa zona o peggio.
- **Percentile 25%**: -37,60% â **0,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo puÃ² scendere fino a questa zona.
- **Percentile 50%**: -28,61% â **0,05 $**
  - Percentile 50: discesa normale durante il mese. Ã il drawdown centrale.
- **Percentile 75%**: -13,56% â **0,06 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -5,34% â **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain â rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo puÃ² toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% â **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo Ã¨ salito poco.
- **Percentile 25%**: 0,73% â **0,07 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 4,88% â **0,08 $**
  - Percentile 50: rialzo normale. Ã lo spike centrale piÃ¹ realistico.
- **Percentile 75%**: 11,33% â **0,08 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 23,46% â **0,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non Ã¨ obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2022-02-20   | 2022-05-30 |        88.63 |       -29.45 |         -33.95 |           2.32 |
| NEAR-USD        | 2022-03-02   | 2022-06-09 |        88.5  |       -25.05 |         -39.1  |           0    |
| VET-USD         | 2022-02-22   | 2022-06-01 |        87.39 |       -27.52 |         -29    |           4.39 |
| QTUM-USD        | 2022-02-20   | 2022-05-30 |        87.3  |       -31.65 |         -37.87 |           0    |
| ZEC-USD         | 2019-05-17   | 2019-08-24 |        87.28 |       -11.71 |         -11.71 |           5.15 |
| XLM-USD         | 2019-09-29   | 2020-01-06 |        87.23 |        39.92 |          -5.54 |          39.92 |
| XRP-USD         | 2019-09-24   | 2020-01-01 |        86.82 |        24.17 |          -2.4  |          26.46 |
| 1INCH-USD       | 2022-02-22   | 2022-06-01 |        86.51 |       -31.62 |         -42.19 |           0    |
| OMG-USD         | 2022-02-20   | 2022-05-30 |        86.48 |       -32.46 |         -37.5  |           0    |
| CHZ-USD         | 2022-02-24   | 2022-06-03 |        86.13 |       -19.17 |         -28.71 |           5.97 |

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-07-10 00:56 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       63024.4  | False                | -13.73%             | -10.12%                  | BEAR               | -13.73%          | -10.12%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -21.81%             | -16.44%                  | BEAR               | -13.73%          | -10.12%               |
| SOL-USD  | BEAR                  |          77.95 | False                | -8.24%              | -18.52%                  | BEAR               | -13.73%          | -10.12%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 72.50%              | 6.89%            | 22.56%           | 43.75%           | -3.94%             | -32.41%            | 16.94%             | 32.64%             | 62.62%             | 72.50%              | 21.61%           | 45.40%           | 63.22%           |
| BTC-USD  | SAME_BTC_REGIME           |        18 | 100.00%             | 23.86%           | 40.45%           | 64.86%           | 0.00%              | -6.02%             | 34.09%             | 58.92%             | 68.90%             | 94.44%              | 41.68%           | 53.55%           | 93.67%           |
| BTC-USD  | SAME_ASSET_REGIME         |        30 | 80.00%              | 12.97%           | 25.32%           | 46.56%           | -2.89%             | -9.92%             | 19.88%             | 34.16%             | 62.73%             | 86.67%              | 30.82%           | 45.61%           | 69.24%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        16 | 100.00%             | 23.86%           | 34.59%           | 69.18%           | 0.00%              | -4.50%             | 34.09%             | 51.61%             | 72.07%             | 93.75%              | 36.92%           | 47.97%           | 97.66%           |
| DOGE-USD | ALL_MATCHES               |        40 | 12.50%              | -20.25%          | -4.52%           | 2.99%            | -28.61%            | -43.86%            | 4.88%              | 11.33%             | 23.46%             | 42.50%              | -6.79%           | 10.58%           | 21.93%           |
| DOGE-USD | SAME_BTC_REGIME           |        31 | 6.45%               | -26.97%          | -13.48%          | -2.33%           | -30.96%            | -44.75%            | 4.26%              | 10.33%             | 23.35%             | 41.94%              | -5.40%           | 9.13%            | 15.56%           |
| DOGE-USD | SAME_ASSET_REGIME         |        34 | 11.76%              | -24.71%          | -5.98%           | 0.71%            | -29.12%            | -44.46%            | 4.57%              | 10.78%             | 24.08%             | 44.12%              | -4.54%           | 12.10%           | 23.67%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        30 | 6.67%               | -27.25%          | -11.95%          | -2.27%           | -30.74%            | -44.76%            | 4.32%              | 10.33%             | 23.46%             | 40.00%              | -6.79%           | 9.20%            | 16.46%           |
| SOL-USD  | ALL_MATCHES               |        40 | 42.50%              | -1.54%           | 11.99%           | 43.75%           | -10.39%            | -30.98%            | 7.79%              | 24.12%             | 55.77%             | 50.00%              | 0.28%            | 32.61%           | 55.73%           |
| SOL-USD  | SAME_BTC_REGIME           |        23 | 65.22%              | 6.36%            | 22.56%           | 44.91%           | -3.73%             | -18.86%            | 15.25%             | 34.69%             | 61.06%             | 65.22%              | 13.31%           | 44.14%           | 76.28%           |
| SOL-USD  | SAME_ASSET_REGIME         |        28 | 50.00%              | 0.14%            | 15.66%           | 48.17%           | -7.71%             | -20.49%            | 11.22%             | 24.12%             | 57.28%             | 60.71%              | 6.46%            | 36.01%           | 59.43%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        19 | 63.16%              | 0.92%            | 21.98%           | 47.20%           | -6.43%             | -17.32%            | 14.92%             | 32.57%             | 56.53%             | 63.16%              | 6.95%            | 37.61%           | 59.48%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        18 | 100.00%             | 23.86%           | 0.00%              | 58.92%             | 94.44%              | 41.68%           | 77.34%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |         8 | 37.50%              | -11.59%          | -12.33%            | 9.57%              | 37.50%              | -14.20%          | 53.66%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |         9 | 66.67%              | 3.65%            | -5.75%             | 16.92%             | 100.00%             | 21.58%           | 73.78%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         5 | 40.00%              | -3.60%           | -11.70%            | 16.38%             | 0.00%               | -24.31%          | 16.38%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        31 | 6.45%               | -26.97%          | -30.96%            | 10.33%             | 41.94%              | -5.40%           | 18.89%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         3 | 33.33%              | -8.75%           | -14.04%            | 14.60%             | 33.33%              | -9.16%           | 15.40%             |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION |         3 | 66.67%              | 18.71%           | -2.40%             | 23.10%             | 100.00%             | 21.64%           | 115.31%            |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         3 | 0.00%               | -11.71%          | -11.71%            | 6.53%              | 0.00%               | -34.20%          | 6.53%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        23 | 65.22%              | 6.36%            | -3.73%             | 34.69%             | 65.22%              | 13.31%           | 71.73%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |        10 | 0.00%               | -14.80%          | -28.59%            | 1.40%              | 0.00%               | -8.45%           | 1.40%              |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         5 | 40.00%              | -2.54%           | -7.18%             | 21.60%             | 100.00%             | 33.69%           | 80.74%             |
| SOL-USD  | HISTORICAL_BTC_RECOVERY     |         2 | 0.00%               | -16.77%          | -29.03%            | 11.14%             | 0.00%               | -35.08%          | 11.14%             |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        30 | 80.00%              | 12.97%           | -2.89%             | 34.16%             | 86.67%              | 30.82%           | 71.82%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -11.76%          | -12.91%            | 8.72%              | 0.00%               | -23.03%          | 8.72%              |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         1 | 100.00%             | 4.40%            | -3.37%             | 8.82%              | 100.00%             | 21.58%           | 33.10%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 66.67%              | 4.46%            | -10.12%            | 30.00%             | 33.33%              | -22.26%          | 65.67%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        34 | 11.76%              | -24.71%          | -29.12%            | 10.78%             | 44.12%              | -4.54%           | 24.30%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         3 | 33.33%              | -12.18%          | -17.30%            | 8.26%              | 66.67%              | 5.41%            | 15.40%             |
| DOGE-USD | HISTORICAL_ASSET_MIXED        |         1 | 0.00%               | -8.75%           | -14.04%            | 12.94%             | 0.00%               | -9.16%           | 12.94%             |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         2 | 0.00%               | -6.05%           | -7.15%             | 7.22%              | 0.00%               | -24.95%          | 7.22%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        28 | 50.00%              | 0.14%            | -7.71%             | 24.12%             | 60.71%              | 6.46%            | 65.11%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -19.43%          | -30.96%            | 0.00%              | 0.00%               | -7.77%           | 0.00%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         3 | 0.00%               | -10.79%          | -27.41%            | 0.55%              | 0.00%               | -12.07%          | 0.55%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 50.00%              | 3.47%            | -17.29%            | 28.80%             | 50.00%              | 10.69%           | 67.73%             |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-19   | 87.73%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| BTC-USD  | KSM-USD         | 2022-03-10   | 86.21%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 11.02%       | -4.93%         | 16.96%         | 14.38%       | -4.93%         | 37.01%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 85.71%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | LTC-USD         | 2020-01-05   | 84.89%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 4.68%        | -3.92%         | 20.03%         | 8.79%        | -3.92%         | 20.03%         |
| BTC-USD  | XLM-USD         | 2020-01-07   | 84.84%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| BTC-USD  | MKR-USD         | 2021-07-21   | 84.83%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 29.66%       | -0.21%         | 38.63%         | 12.58%       | -6.23%         | 38.63%         |
| BTC-USD  | TRX-USD         | 2020-01-07   | 84.53%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 22.02%       | 0.00%          | 33.95%         | 32.98%       | 0.00%          | 48.70%         |
| BTC-USD  | OMG-USD         | 2020-01-07   | 84.49%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 79.99%       | 0.00%          | 79.99%         | 195.80%      | 0.00%          | 253.59%        |
| BTC-USD  | ADA-USD         | 2020-01-07   | 84.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 58.37%       | 0.00%          | 64.15%         | 140.87%      | 0.00%          | 179.32%        |
| BTC-USD  | QTUM-USD        | 2020-01-07   | 84.21%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 16.10%       | 0.00%          | 28.06%         | 33.45%       | 0.00%          | 45.51%         |
| DOGE-USD | DASH-USD        | 2022-02-20   | 88.63%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | VET-USD         | 2022-02-22   | 87.39%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 87.30%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XLM-USD         | 2019-09-29   | 87.23%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | 1INCH-USD       | 2022-02-22   | 86.51%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.62%      | -42.19%        | 0.00%          | -20.09%      | -42.19%        | 0.00%          |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.48%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | CHZ-USD         | 2022-02-24   | 86.13%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -19.17%      | -28.71%        | 5.97%          | 11.61%       | -28.71%        | 22.22%         |
| DOGE-USD | THETA-USD       | 2022-02-24   | 86.09%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 1.59%        | -8.56%         | 23.35%         | 14.81%       | -8.85%         | 24.03%         |
| DOGE-USD | XTZ-USD         | 2025-12-06   | 85.93%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.41%      | -12.14%        | 4.26%          | -2.16%       | -12.14%        | 4.26%          |
| DOGE-USD | ENJ-USD         | 2022-02-25   | 85.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -16.55%      | -33.46%        | 5.00%          | 1.45%        | -33.46%        | 5.00%          |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 79.51%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | TRX-USD         | 2018-09-19   | 79.01%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 55.01%       | 0.00%          | 55.01%         | 32.25%       | 0.00%          | 58.38%         |
| SOL-USD  | LRC-USD         | 2018-09-19   | 78.40%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| SOL-USD  | XLM-USD         | 2020-01-07   | 78.15%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| SOL-USD  | APT-USD         | 2024-09-01   | 77.72%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.92%        | -11.47%        | 6.42%          | -34.40%      | -34.40%        | 6.42%          |
| SOL-USD  | NEAR-USD        | 2025-12-01   | 77.66%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 6.36%        | -9.61%         | 16.07%         | 21.89%       | -9.61%         | 24.08%         |
| SOL-USD  | ENJ-USD         | 2018-09-19   | 77.20%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | -16.11%      | -19.37%        | 5.11%          | 93.16%       | -38.09%        | 93.16%         |
| SOL-USD  | SOL-USD         | 2025-12-04   | 76.83%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -7.51%       | -10.44%        | 9.16%          | 6.95%        | -10.44%        | 10.43%         |
| SOL-USD  | XRP-USD         | 2020-01-07   | 76.29%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 9.73%        | 0.00%          | 25.47%         | 5.71%        | 0.00%          | 25.47%         |
| SOL-USD  | OMG-USD         | 2025-12-01   | 75.75%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -5.35%       | -7.41%         | 2.96%          | 13.31%       | -7.41%         | 15.03%         |

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

<!-- TECHNICAL_STRUCTURE_START -->
# Report struttura tecnica

Generato: 2026-07-10 00:56 UTC

Questo report aggiunge al tuo scanner una lettura classica di analisi tecnica.

Moduli inclusi:

- Struttura trend con MA20 / MA50 / MA200
- Massimi e minimi crescenti oppure decrescenti
- Doppio minimo, triplo minimo, doppio massimo, triplo massimo
- Pattern Adam and Eve Bottom / Top
- Divergenze RSI e divergenze RSI nascoste
- Momentum MACD
- Conferma volume con OBV / CMF
- Candidato fase Wyckoff
- Punteggio tecnico di confluenza

## Sintesi

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             | Divergenza                         | Wyckoff                 | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|:-----------------------------------|:------------------------|:-----------|:-------------|
| BTC     | 63.026   |          -3 | DEBOLE             | Trend ribassista | Momentum misto  | Struttura ribassista con massimi e minimi decrescenti | Divergenza rialzista RSI           | Possibile accumulazione | 57.748     | 65.544       |
| SOL     | 77,95    |           1 | NEUTRALE / MISTO   | Trend misto      | Momentum misto  | Volatilità in espansione                              | Nessuna                            | Range / fase non chiara | 64,42      | 83,81        |
| DOGE    | 0.07280  |         -10 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | Divergenza ribassista nascosta RSI | Possibile accumulazione | 0.06961    | 0.07923      |

## Riepilogo pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom     | Doppio massimo   | Triplo massimo   | Adam/Eve Top     |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------|:-----------------|:-----------------|:-----------------|--------------------:|
| BTC     | Possibile       | Possibile       | Adam and Eve Bottom | Confermato       | Confermato       | Eve and Adam Top |                  -4 |
| SOL     | Confermato      | Possibile       | Adam and Eve Bottom | Possibile        | Confermato       | Eve and Adam Top |                   1 |
| DOGE    | Assente         | Possibile       | Adam and Eve Bottom | Assente          | Confermato       | Eve and Adam Top |                  -4 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC     |    49.52 |         580.539   | 61.812  | 65.633  | 74.224  | -9,36%              | -10,12%              | 2,57%            | -13,73%          |
| SOL     |    54.31 |           0.53818 | 75,32   | 74,87   | 92,44   | -6,40%              | -18,52%              | 23,41%           | -8,24%           |
| DOGE    |    33.17 |           0.00045 | 0.07606 | 0.08580 | 0.10185 | -13,10%             | -16,44%              | -12,24%          | -21,81%          |

## Dettaglio asset

### BTC

- Prezzo: **63.026**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.725e+04 -> 6.554e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 49.5.
- Supporto più vicino: **57.748**
- Resistenza più vicina: **65.544**

Pattern classici:

- Doppio minimo: **Possibile**
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248.
- Triplo minimo: **Possibile**
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248.
- Adam/Eve Bottom: **Adam and Eve Bottom**
  - Possibile pattern Adam and Eve Bottom vicino a 62.201 dal 2026-03-29 al 2026-06-18. Nel modello Adam/Eve un minimo è più appuntito e violento, l'altro è più arrotondato. Neckline stimata: 82.792.
- Doppio massimo: **Confermato**
  - Due massimi simili vicino a 79.488 tra 2026-04-27 e 2026-05-26. Neckline ribassista stimata: 74.959.
- Triplo massimo: **Confermato**
  - Tre massimi simili vicino a 79.468 dal 2026-04-17 al 2026-05-26. Neckline ribassista stimata: 74.959.
- Adam/Eve Top: **Eve and Adam Top**
  - Possibile pattern Eve and Adam Top vicino a 82.792 dal 2026-04-22 al 2026-05-06. Nel modello Adam/Eve un massimo è più appuntito e violento, l'altro è più arrotondato. Neckline ribassista stimata: 74.959.

### SOL

- Prezzo: **77,95**
- Punteggio tecnico: **1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 67.92 -> 64.42. Ultimi massimi: 74.89 -> 83.81.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 46,33%. Fase non abbastanza chiara.
- Supporto più vicino: **64,42**
- Resistenza più vicina: **83,81**

Pattern classici:

- Doppio minimo: **Confermato**
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94.
- Triplo minimo: **Possibile**
  - Tre minimi simili vicino a 81,41 dal 2026-04-12 al 2026-05-23. Neckline stimata: 98,27.
- Adam/Eve Bottom: **Adam and Eve Bottom**
  - Possibile pattern Adam and Eve Bottom vicino a 60,41 dal 2026-06-06 al 2026-06-25. Nel modello Adam/Eve un minimo è più appuntito e violento, l'altro è più arrotondato. Neckline stimata: 75,94.
- Doppio massimo: **Possibile**
  - Due massimi simili vicino a 87,79 tra 2026-05-21 e 2026-07-04. Neckline ribassista stimata: 60,41.
- Triplo massimo: **Confermato**
  - Tre massimi simili vicino a 89,26 dal 2026-04-22 al 2026-05-21. Neckline ribassista stimata: 81,63.
- Adam/Eve Top: **Eve and Adam Top**
  - Possibile pattern Eve and Adam Top vicino a 88,05 dal 2026-04-27 al 2026-07-04. Nel modello Adam/Eve un massimo è più appuntito e violento, l'altro è più arrotondato. Neckline ribassista stimata: 60,41.

### DOGE

- Prezzo: **0.07280**
- Punteggio tecnico: **-10 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07809 -> 0.06961. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 33.2.
- Supporto più vicino: **0.06961**
- Resistenza più vicina: **0.07923**

Pattern classici:

- Doppio minimo: **Assente**
- Triplo minimo: **Possibile**
  - Tre minimi simili vicino a 0.09274 dal 2026-04-19 al 2026-05-28. Neckline stimata: 0.11825.
- Adam/Eve Bottom: **Adam and Eve Bottom**
  - Possibile pattern Adam and Eve Bottom vicino a 0.09274 dal 2026-04-19 al 2026-05-23. Nel modello Adam/Eve un minimo è più appuntito e violento, l'altro è più arrotondato. Neckline stimata: 0.11825.
- Doppio massimo: **Assente**
- Triplo massimo: **Confermato**
  - Tre massimi simili vicino a 0.10200 dal 2026-03-25 al 2026-04-17. Neckline ribassista stimata: 0.08862.
- Adam/Eve Top: **Eve and Adam Top**
  - Possibile pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Nel modello Adam/Eve un massimo è più appuntito e violento, l'altro è più arrotondato. Neckline ribassista stimata: 0.07809.

## Come leggere il punteggio

- Da +7 a +12: forte confluenza tecnica rialzista.
- Da +3 a +6: struttura costruttiva, ma serve ancora conferma.
- Da -2 a +2: situazione mista / neutrale.
- Da -6 a -3: struttura tecnica debole.
- Da -12 a -7: forte confluenza tecnica ribassista.

Nota importante: questo report non è una previsione da solo. È un filtro tecnico da leggere insieme a scanner frattale, market regime, futures e RSI.
<!-- TECHNICAL_STRUCTURE_END -->

<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->
# Classic technical confirmation report

Generato: 2026-07-10 00:56 UTC

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
- volatilità e rischio tramite ATR

## Sintesi

| Asset | Prezzo | Score | Verdetto | Stage | Struttura | Wyckoff | Rischio | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.026 $ | -3 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | SPRING / TEST POSSIBILE | MEDIO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 77,95 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | RANGE / FASE NON CHIARA | MEDIO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07280 $ | -9 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | -2 | 0 | +2 | 0 | 0 | +1 | -3 |
| SOL | -4 | 0 | 0 | +2 | 0 | 0 | 0 | -2 |
| DOGE | -4 | -2 | -2 | +1 | 0 | 0 | -2 | -9 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.553 $ | 64.186 $ | 82.792 $ | 57.748 $ | 3,10% | 2,24% | -13,64% |
| SOL | 77,45 $ | 83,22 $ | 98,27 $ | 60,41 $ | 4,69% | 19,99% | -8,11% |
| DOGE | 0.07206 $ | 0.07923 $ | 0.11825 $ | 0.06961 $ | 4,03% | -14,14% | -22,33% |

## Lettura dettagliata

### BTC

- Prezzo: **63.026 $**
- Score classico: **-3 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Rischio: **MEDIO** — ATR14 3,10%; distanza supporto 0,76%; distanza resistenza 1,84%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **0** — RSI neutrale 49.5; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.08; volume ratio 0.93
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 49.52 |
| MACD histogram | 580.53865 |
| CMF20 | 0.075 |
| Volume ratio 20 | 0.93 |
| MA20 | 61.812 $ |
| MA50 | 65.633 $ |
| MA100 | 70.827 $ |
| MA200 | 74.224 $ |
| Pendenza MA50 20g | -9,70% |
| Pendenza MA200 60g | -10,28% |
| Bollinger width | 11,35% |
| Bollinger position | 0.67 |

### SOL

- Prezzo: **77,95 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Rischio: **MEDIO** — ATR14 4,69%; distanza supporto 0,65%; distanza resistenza 6,76%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 54.3; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.08; volume ratio 0.66
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 54.31 |
| MACD histogram | 0.53818 |
| CMF20 | 0.077 |
| Volume ratio 20 | 0.66 |
| MA20 | 75,32 $ |
| MA50 | 74,87 $ |
| MA100 | 80,44 $ |
| MA200 | 92,44 $ |
| Pendenza MA50 20g | -6,64% |
| Pendenza MA200 60g | -18,86% |
| Bollinger width | 25,51% |
| Bollinger position | 0.63 |

### DOGE

- Prezzo: **0.07280 $**
- Score classico: **-9 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Rischio: **BASSO** — ATR14 4,03%; distanza supporto 1,03%; distanza resistenza 8,84%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-2** — RSI debole 33.2; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale -0.02; volume ratio 0.77
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 33.17 |
| MACD histogram | 0.00045 |
| CMF20 | -0.018 |
| Volume ratio 20 | 0.77 |
| MA20 | 0.07606 $ |
| MA50 | 0.08580 $ |
| MA100 | 0.09347 $ |
| MA200 | 0.10185 $ |
| Pendenza MA50 20g | -13,54% |
| Pendenza MA200 60g | -16,72% |
| Bollinger width | 19,29% |
| Bollinger position | 0.27 |

## Come leggere lo score

- **+8 a +12**: conferma tecnica rialzista forte.
- **+5 a +7**: setup costruttivo, ma può mancare ancora una rottura pulita.
- **+2 a +4**: setup anticipato, interessante ma non confermato.
- **-1 a +1**: neutrale / misto.
- **-4 a -2**: debole / non confermato.
- **-8 o meno**: conferma tecnica ribassista.

Nota: questo modulo deve pesare poco nel Global finché non viene verificato dalla calibrazione. La funzione principale è evitare di confondere un contesto interessante con una conferma vera.
<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->

<!-- CLASSIC_TECHNICAL_VISUAL_START -->
# Classic technical visual report

Generato: 2026-07-10 00:57 UTC

Questo report crea grafici visivi dei pattern tecnici principali. Serve per vedere il grafico, non per aggiungere automaticamente punteggio al Global.

Pattern controllati:

- doppio minimo
- doppio massimo
- testa e spalle
- testa e spalle inverso
- triangolo / compressione
- candela giornaliera principale
- pivot high / pivot low
- supporto, resistenza, breakout e breakdown 60 giorni

## Sintesi visiva

| Asset | Prezzo | Pattern principale | Stato | Famiglia | Prezzo | Supporto | Resistenza |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.018 $ | Doppio massimo | CONFERMATO | ribassista | NEL RANGE | 62.553 $ | 65.544 $ |
| SOL | 77,95 $ | Testa e spalle | CONFERMATO | ribassista | NEL RANGE | 76,82 $ | 83,81 $ |
| DOGE | 0.07279 $ | Doppio massimo | CONFERMATO | ribassista | NEL RANGE | 0.06961 $ | 0.07923 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CONFERMATO**
- Famiglia: **ribassista**
- Dettaglio: Due massimi simili a 78.321 $ e 77.991 $. Neckline circa 74.959 $.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.544 $**
- Breakout 60g: **82.792 $**
- Breakdown 60g: **57.748 $**
- RSI14: **49.48**
- ATR14: **3,10%**
- Volume ratio 20g: **0.93**
- Rendimento 30g: **+2,23%**
- Rendimento 90g: **-13,65%**

### Pattern trovati

| Pattern | Stato | Famiglia | Neckline | Dettaglio |
| --- | --- | --- | --- | --- |
| Doppio massimo | CONFERMATO | ribassista | 74.959 $ | Due massimi simili a 78.321 $ e 77.991 $. Neckline circa 74.959 $. |
| Doppio minimo | CANDIDATO | rialzista | 67.248 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. |
| Triangolo discendente possibile | CANDIDATO | ribassista | n/a | Massimi decrescenti e supporto quasi piatto. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Testa e spalle**
- Stato pattern: **CONFERMATO**
- Famiglia: **ribassista**
- Dettaglio: Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76,82 $**
- Resistenza: **83,81 $**
- Breakout 60g: **98,27 $**
- Breakdown 60g: **60,41 $**
- RSI14: **54.31**
- ATR14: **4,69%**
- Volume ratio 20g: **0.66**
- Rendimento 30g: **+19,99%**
- Rendimento 90g: **-8,11%**

### Pattern trovati

| Pattern | Stato | Famiglia | Neckline | Dettaglio |
| --- | --- | --- | --- | --- |
| Testa e spalle | CONFERMATO | ribassista | 82,57 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. |
| Doppio massimo | CONFERMATO | ribassista | 81,63 $ | Due massimi simili a 90,67 $ e 87,79 $. Neckline circa 81,63 $. |
| Doppio minimo | CANDIDATO | rialzista | 98,27 $ | Due minimi simili a 78,43 $ e 81,69 $. Neckline circa 98,27 $. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CONFERMATO**
- Famiglia: **ribassista**
- Dettaglio: Due massimi simili a 0.09772 $ e 0.09169 $. Neckline circa 0.07809 $.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.11825 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **33.14**
- ATR14: **4,03%**
- Volume ratio 20g: **0.77**
- Rendimento 30g: **-14,15%**
- Rendimento 90g: **-22,34%**

### Pattern trovati

| Pattern | Stato | Famiglia | Neckline | Dettaglio |
| --- | --- | --- | --- | --- |
| Doppio massimo | CONFERMATO | ribassista | 0.07809 $ | Due massimi simili a 0.09772 $ e 0.09169 $. Neckline circa 0.07809 $. |
| Doppio minimo | CANDIDATO | rialzista | 0.11825 $ | Due minimi simili a 0.09044 $ e 0.09675 $. Neckline circa 0.11825 $. |

## Come leggerlo

- Il grafico in alto mostra prezzo, MA20, MA50, MA200, supporti, resistenze e pattern.
- Il pannello centrale mostra RSI14.
- Il pannello basso mostra volume e media volume 20 giorni.
- Un pattern **candidato** non è un segnale operativo: serve rottura della neckline o conferma del prezzo.
- Un pattern **confermato** è più interessante, ma va comunque letto insieme a scanner, market regime, futures e rischio leva.

Nota: questi pattern sono riconosciuti con regole algoritmiche semplici. Sono utili per visualizzare il grafico, ma vanno sempre controllati a occhio.
<!-- CLASSIC_TECHNICAL_VISUAL_END -->

<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-10 00:57 UTC

Questo report controlla se SOL sta seguendo il percorso previsto dal frattale BTC 2022 vs SOL 2026.

Ora il controllo è diviso in cinque parti:

- confronto dal bottom: BTC 2022 scalato contro SOL reale
- tratto da inizio programma/scanner: verifica se il tracking recente sta reggendo
- proiezione futura giornaliera: BTC 2022 viene scalato giorno per giorno su SOL
- controllo settimanale: ogni previsione viene verificata a 7, 14, 21, 28 giorni e così via fino a 126 giorni
- grafico gap: differenza leggibile tra SOL reale e BTC scalato

## Stato ultimo frattale salvato

- Data previsione: **2026-07-10**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC 2022 equivalente: **2022-11-21**
- Giorno BTC equivalente oggi: **2022-12-25**
- Inizio programma/scanner rilevato: **2026-07-03**
- Prezzo SOL corrente: **77,95 $**
- Verdetto: **PARZIALMENTE SI**
- Somiglianza: **+73,76%**
- Tracking: **FRATTALE STABILE**
- Fase: **FASE ANTICIPATA**
- Rischio fase: **MEDIO / ALTO**

## Confronto dal bottom a oggi

- Giorni controllati dal bottom: **35**
- Giorni controllati da inizio programma/scanner: **8**
- Errore medio assoluto dal bottom: **9,52%**
- Errore medio assoluto ultimi 7 giorni: **20,84%**
- Errore medio assoluto da inizio programma/scanner: **21,32%**
- Errore ultimo giorno: **+17,49%**
- Stato: **DEVIAZIONE MODERATA**

## Grafico completo: bottom, inizio programma e proiezione giornaliera

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato - ultimi 60 giorni

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap: **+17,49%**
- Media mobile 7g gap: **+20,84%**
- Variazione recente gap: **-4,15%**
- Stato gap: **SOPRA FRATTALE / MOLTO IN ANTICIPO**
- Trend gap: **SOL resta sopra il frattale, ma sta perdendo anticipo e si sta riavvicinando al percorso BTC scalato**

Come leggerlo:

- **Sopra 0%** = SOL è sopra il percorso BTC scalato.
- **Sotto 0%** = SOL è sotto il percorso BTC scalato.
- Se il gap sale, SOL si sta allontanando sopra il frattale.
- Se il gap scende mentre resta positivo, SOL resta più forte del frattale ma sta perdendo anticipo.
- Questo è il grafico più leggibile per capire subito se SOL si sta orientando sopra o sotto il frattale.

## Ultimi giorni del confronto dal bottom

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | BTC scalato   | Errore   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------|:---------|:--------------------|
|       25 | 2026-07-01 | 2022-12-16     | 77,38 $     | 65,58 $       | +18,00%  | prima programma     |
|       26 | 2026-07-02 | 2022-12-17     | 80,64 $     | 66,16 $       | +21,89%  | prima programma     |
|       27 | 2026-07-03 | 2022-12-18     | 82,28 $     | 66,01 $       | +24,64%  | da inizio programma |
|       28 | 2026-07-04 | 2022-12-19     | 81,65 $     | 64,76 $       | +26,08%  | da inizio programma |
|       29 | 2026-07-05 | 2022-12-20     | 81,42 $     | 66,60 $       | +22,26%  | da inizio programma |
|       30 | 2026-07-06 | 2022-12-21     | 81,92 $     | 66,25 $       | +23,65%  | da inizio programma |
|       31 | 2026-07-07 | 2022-12-22     | 80,65 $     | 66,30 $       | +21,64%  | da inizio programma |
|       32 | 2026-07-08 | 2022-12-23     | 77,79 $     | 66,17 $       | +17,56%  | da inizio programma |
|       33 | 2026-07-09 | 2022-12-24     | 77,79 $     | 66,37 $       | +17,21%  | da inizio programma |
|       34 | 2026-07-10 | 2022-12-25     | 77,95 $     | 66,34 $       | +17,49%  | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Base frattale   | Min percorso   | Max percorso   | Controllato   | Prezzo reale   | Errore   | Dentro banda   |
|:------------|:--------------|:----------------|:---------------|:---------------|:--------------|:---------------|:---------|:---------------|
| 7g          | 2026-07-17    | 76,95 $         | 76,59 $        | 78,31 $        | no            | n/a            | n/a      | n/a            |
| 14g         | 2026-07-24    | 79,10 $         | 76,59 $        | 79,10 $        | no            | n/a            | n/a      | n/a            |
| 21g         | 2026-07-31    | 96,64 $         | 76,59 $        | 97,08 $        | no            | n/a            | n/a      | n/a            |
| 28g         | 2026-08-07    | 105,16 $        | 76,59 $        | 105,42 $       | no            | n/a            | n/a      | n/a            |
| 35g         | 2026-08-14    | 110,04 $        | 76,59 $        | 110,04 $       | no            | n/a            | n/a      | n/a            |
| 42g         | 2026-08-21    | 106,25 $        | 76,59 $        | 110,04 $       | no            | n/a            | n/a      | n/a            |
| 49g         | 2026-08-28    | 100,84 $        | 76,59 $        | 110,04 $       | no            | n/a            | n/a      | n/a            |
| 56g         | 2026-09-04    | 112,60 $        | 76,59 $        | 114,05 $       | no            | n/a            | n/a      | n/a            |
| 63g         | 2026-09-11    | 109,05 $        | 76,59 $        | 114,92 $       | no            | n/a            | n/a      | n/a            |
| 70g         | 2026-09-18    | 103,84 $        | 76,59 $        | 114,92 $       | no            | n/a            | n/a      | n/a            |
| 77g         | 2026-09-25    | 102,58 $        | 76,59 $        | 114,92 $       | no            | n/a            | n/a      | n/a            |
| 84g         | 2026-10-02    | 129,77 $        | 76,59 $        | 129,77 $       | no            | n/a            | n/a      | n/a            |
| 91g         | 2026-10-09    | 129,57 $        | 76,59 $        | 131,14 $       | no            | n/a            | n/a      | n/a            |
| 98g         | 2026-10-16    | 130,52 $        | 76,59 $        | 131,81 $       | no            | n/a            | n/a      | n/a            |
| 105g        | 2026-10-23    | 131,13 $        | 76,59 $        | 131,81 $       | no            | n/a            | n/a      | n/a            |
| 112g        | 2026-10-30    | 140,31 $        | 76,59 $        | 141,10 $       | no            | n/a            | n/a      | n/a            |
| 119g        | 2026-11-06    | 127,70 $        | 76,59 $        | 141,10 $       | no            | n/a            | n/a      | n/a            |
| 126g        | 2026-11-13    | 135,47 $        | 76,59 $        | 141,10 $       | no            | n/a            | n/a      | n/a            |

Nota: la tabella sopra mostra le milestone settimanali principali. Il grafico invece usa la proiezione giornaliera del frattale BTC scalato su SOL.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda   | Errore medio assoluto   | Errore medio   |
|:------------|------------:|:---------------|:------------------------|:---------------|
| 7g          |           0 | n/a            | n/a                     | n/a            |
| 14g         |           0 | n/a            | n/a                     | n/a            |
| 21g         |           0 | n/a            | n/a                     | n/a            |
| 28g         |           0 | n/a            | n/a                     | n/a            |
| 35g         |           0 | n/a            | n/a                     | n/a            |
| 42g         |           0 | n/a            | n/a                     | n/a            |
| 49g         |           0 | n/a            | n/a                     | n/a            |
| 56g         |           0 | n/a            | n/a                     | n/a            |
| 63g         |           0 | n/a            | n/a                     | n/a            |
| 70g         |           0 | n/a            | n/a                     | n/a            |
| 77g         |           0 | n/a            | n/a                     | n/a            |
| 84g         |           0 | n/a            | n/a                     | n/a            |
| 91g         |           0 | n/a            | n/a                     | n/a            |
| 98g         |           0 | n/a            | n/a                     | n/a            |
| 105g        |           0 | n/a            | n/a                     | n/a            |
| 112g        |           0 | n/a            | n/a                     | n/a            |
| 119g        |           0 | n/a            | n/a                     | n/a            |
| 126g        |           0 | n/a            | n/a                     | n/a            |

## Come leggerlo

- BTC 2022 scalato su SOL è il percorso che SOL dovrebbe seguire se il frattale resta valido.
- SOL reale mostra cosa ha fatto davvero dal bottom.
- La linea di inizio programma/scanner separa il backtest retroattivo dalla parte che stiamo monitorando davvero giorno per giorno.
- Se SOL resta vicino a BTC scalato, il frattale è in linea.
- Se SOL sta sopra BTC scalato, il frattale è in anticipo o più forte.
- Se SOL sta sotto BTC scalato, il frattale è in ritardo o più debole.
- Il grafico gap ultimi 60 giorni serve proprio per vedere meglio questa differenza.
- Le milestone settimanali servono a controllare il percorso passo passo.
- La proiezione futura va letta insieme alle conferme e invalidazioni del report frattale principale.
<!-- FRACTAL_PATH_TRACKER_END -->

<!-- LIQUIDATION_SUMMARY_START -->

---

# Sintesi semplice futures / liquidazioni

Report separato completo: [liquidation_report.md](liquidation_report.md)

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $63,071 | +0.0068% | +3.30% | 1.90 | Rischio sotto | 4/5 |
| SOL | $78.00 | +0.0010% | -28.14% | 2.61 | Misto | 1/5 |
| DOGE | $0.07280 | +0.0021% | -3.75% | 3.04 | Misto | 1/5 |

## Come usarla insieme al frattale

- Frattale ribassista + futures con rischio sotto = prudenza alta.
- Frattale rialzista + futures con rischio sopra = segnale più interessante.
- Frattale e futures opposti = situazione sporca, meglio non forzare.
- Per posizioni a leva, il futures report serve soprattutto a capire se può arrivare una pulizia violenta prima dei 30 giorni.

<!-- LIQUIDATION_SUMMARY_END -->

<!-- CALIBRATION_READABLE_START -->

---

# Stato leggibile accuratezza / calibrazione

Report dettagliati:
- [accuracy_report.md](accuracy_report.md)
- [calibration_report.md](calibration_report.md)

## Riassunto semplice

- **BTC**: 0/30 previsioni controllate su 8 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 8 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 8 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 8 | 0 | 0/30 [░░░░░░░░░░] | 8 | RACCOLTA DATI | 2026-08-02 / tra 23 giorni |
| SOL | 8 | 0 | 0/30 [░░░░░░░░░░] | 8 | RACCOLTA DATI | 2026-08-02 / tra 23 giorni |
| DOGE | 8 | 0 | 0/30 [░░░░░░░░░░] | 8 | RACCOLTA DATI | 2026-08-02 / tra 23 giorni |

## Traduzione

- **0/30** significa: lo scanner sta ancora raccogliendo dati.
- **30/30** significa: la calibrazione comincia ad attivarsi.
- **60+** significa: la calibrazione diventa più solida.
- L'email non c'entra con la calibrazione: conta solo che il workflow giri e salvi il diario delle previsioni.

<!-- CALIBRATION_READABLE_END -->
