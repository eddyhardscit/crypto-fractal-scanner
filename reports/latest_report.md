<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-10 12:10 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: spot, long, short e rischio. Ora segue il Global Confluence aggiornato e non assegna più punti automatici al Lifecycle EMA200.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +6 | BULLISH | COMPRA / ACCUMULA | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | 0 | NEUTRALE / INCERTO | HOLD LEGGERO / ASPETTA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -10 | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+6**, spot = **COMPRA / ACCUMULA**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **0**, spot = **HOLD LEGGERO / ASPETTA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-10**, spot = **VENDI PARZIALE / STAI FUORI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+6**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot: **COMPRA / ACCUMULA**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Sopra 64.598 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Global Confluence: **0**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot: **HOLD LEGGERO / ASPETTA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Conferme sopra 83,81 / 83,17 / 116,77.
- Invalidazioni: Allarmi sotto 75,25 / 64,42 / 62,19.

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
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo accumulo spot prudente.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 5; EMA200 circa 113,52 $; upside verso EMA200 +43,30%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- MODULE_ACCURACY_START -->
# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-10 12:10 UTC

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
| 2026-07-10 | BTC | 64.366,37 | +6 | +3 | +3 | -1 | 0 | 0 | ACCUMULA SU PULLBACK / NO SHORT |
| 2026-07-10 | DOGE | 0.07417 | -10 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-10 | SOL | 79,22 | 0 | -1 | 0 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
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

Generato: 2026-07-10 12:10 UTC

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
| BTC     | BASSO          | MEDIO          | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-10 12:10 UTC

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
| BTC | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA SU PULLBACK / NO SHORT | Sopra 64.598 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Conferme sopra 83,81 / 83,17 / 116,77. | Allarmi sotto 75,25 / 64,42 / 62,19. |
| DOGE | -10 | NEGATIVA | Ribassista | MEDIA / ALTA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.07923 migliora, ma resta asset debole finché scanner e struttura non girano. | Sotto 0.06961 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner | Scanner path | Market regime | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +6 |
| SOL | -1 | 0 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | -3 | 0 | -3 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | -10 |

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+6**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA SU PULLBACK / NO SHORT**

BTC è l'asset messo meglio nel breve. La struttura macro non è ancora pienamente rialzista, ma scanner, regime e segnali interni sono abbastanza coerenti per un recupero prudente.

Dettaglio moduli:

- Scanner: **+3** — Casi positivi 77,50%, return centrale 30g +9,01%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 0. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 15, positivi 30g 100,00%, return p50 +22,02%.
- Tecnico: **-1** — Score tecnico -2/12, verdetto neutrale / misto, trend trend ribassista, struttura struttura ribassista con massimi e minimi decrescenti, divergenza divergenza rialzista rsi, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff SPRING / TEST POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Sopra 64.598 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta vivo, ma serve conferma di prezzo. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Scanner: **-1** — Casi positivi 37,50%, return centrale 30g -2,05%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 0. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 20, positivi 30g 50,00%, return p50 +0,22%.
- Tecnico: **+1** — Score tecnico 2/12, verdetto neutrale / misto, trend trend misto, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto STRUTTURA ANALOGA, PREZZO NON ADERENTE, somiglianza +65,04%, tracking STORICO INIZIALE, fase FRATTALE NON CONFERMATO DAL PREZZO, rischio ALTO.
- Fractal path: **0** — Tracking operativo, ma nessuna milestone settimanale ancora verificata. Il modulo non pesa finché non maturano abbastanza controlli.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 5, bias SQUEEZE SETUP FORTE, EMA200 113,52 $, upside EMA200 +43,30%, gap EMA50/EMA200 -1,18%, hit EMA200 12w +20,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Conferme sopra 83,81 / 83,17 / 116,77.

Invalidazioni: Allarmi sotto 75,25 / 64,42 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-10**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche se può fare rimbalzi o spike, la confluenza generale resta negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Scanner: **-3** — Casi positivi 15,00%, return centrale 30g -22,37%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 0. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **-3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 31, positivi 30g 9,68%, return p50 -26,97%.
- Tecnico: **-3** — Score tecnico -10/12, verdetto ribassista tecnico, trend trend ribassista, struttura struttura ribassista con massimi e minimi decrescenti, divergenza divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione.
- Classic technical: **-1** — Score classico -9/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in miglioramento rispetto a ieri.

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

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +65,04%
- **Somiglianza strutturale:** +65,04%
- **Aderenza prezzo live:** +56,79%
- **Errore medio live:** +21,60%
- **Gap prezzo corrente:** +19,39%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STORICO INIZIALE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 34 dal bottom usato.
- **Giorno BTC equivalente:** 2022-12-25
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Laterale / movimento non forte.** Zona bassa **77,82 $** intorno al **16 luglio 2026**; zona alta **80,38 $** intorno al **24 luglio 2026**; fine step circa **80,38 $** entro il **24 luglio 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 10 luglio 2026 | 8 | +56,79% | +21,60% | +19,39% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 10 luglio 2026 | 35 | +80,83% | +9,59% | +19,39% | ABBASTANZA ALLINEATO |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +56,79% | Errore medio live +21,60%. |
| Gap corrente | +19,39% | Deve rientrare circa entro ±12%. |
| Milestone analogica breve (prima conferma) | 83,17 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Milestone analogica estesa (seconda conferma) | 116,77 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 75,25 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 586,73 $ |
| Massimo percorso base | 586,73 $ (21 aprile 2029) |

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
| Milestone analogica breve (prima conferma) | 83,17 $ | Deve accompagnarsi al rientro del gap. |
| Milestone analogica estesa (seconda conferma) | 116,77 $ | Scenario più credibile. |
| Invalidazione soft | 75,25 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 17 luglio 2026 | -1,29% | 78,19 $ | 77,82 $ | 79,58 $ |
| 14 giorni | 24 luglio 2026 | +1,48% | 80,38 $ | 77,82 $ | 80,38 $ |
| 30 giorni | 9 agosto 2026 | +34,40% | 106,46 $ | 77,82 $ | 107,86 $ |
| 60 giorni | 8 settembre 2026 | +42,19% | 112,63 $ | 77,82 $ | 116,77 $ |
| 90 giorni | 8 ottobre 2026 | +63,25% | 129,31 $ | 77,82 $ | 133,26 $ |
| 120 giorni | 7 novembre 2026 | +63,43% | 129,46 $ | 77,82 $ | 143,38 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 10 luglio 2026 -> 24 luglio 2026 | +1,48% | 77,82 $ (16 luglio 2026) | 80,38 $ (24 luglio 2026) | 80,38 $ | Laterale / movimento non forte. |
| Step 2 - primo mese | 25 luglio 2026 -> 9 agosto 2026 | +34,40% | 80,88 $ (25 luglio 2026) | 107,86 $ (8 agosto 2026) | 106,46 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 10 agosto 2026 -> 8 settembre 2026 | +42,19% | 101,83 $ (26 agosto 2026) | 116,77 $ (5 settembre 2026) | 112,63 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 9 settembre 2026 -> 8 ottobre 2026 | +63,25% | 94,94 $ (23 settembre 2026) | 133,26 $ (6 ottobre 2026) | 129,31 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali. La forma simile non compensa un prezzo non aderente.

<!-- BTC_SOL_FRACTAL_END -->

<!-- RSI_TOP_CYCLE_START -->

---

# RSI top-cycle warning - SOL

Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)

Questo filtro controlla se RSI weekly/monthly si stanno avvicinando alla trendline alta che puo segnalare esaurimento ciclo.

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 79,21 $ |  |
| Weekly RSI | 41,17 / top-line 56,32 | LONTANO DALLA TOP-LINE - normale |
| Monthly RSI | 41,67 / top-line 48,69 | IN AVVICINAMENTO - troppo ripida per proiezione 2029 |
| Target ciclo base | 586,73 $ | Avanzamento +13,50% |
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
| Score on-chain | -2 |
| Bias | NEGATIVA |
| Azione coerente | PRUDENZA / POSSIBILE PRESSIONE |
| Prezzo SOL | 79,17 $ |
| TVL Solana | 4,99 mld $ |
| TVL 7g | -1,11% |
| DEX volume 24h | 1,79 mld $ |
| Fees 24h | 6,10 mln $ |
| Stablecoin su Solana | 15,36 mld $ |
| Stake ratio | 67,94% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**PRUDENZA / POSSIBILE PRESSIONE**

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
| Prezzo SOL                | 79,22 $                                             |
| EMA200 weekly target      | 113,52 $                                            |
| Upside verso EMA200       | +43,30%                                             |
| Distanza prezzo da EMA200 | -30,22%                                             |
| Gap EMA50/EMA200          | -1,18%                                              |
| Stato cross               | EMA50/EMA200 SOVRAPPOSTE / INCROCIO IN CORSO        |
| RSI weekly                | 41,18                                               |
| Età SOL                   | 6,2 anni                                            |
| Analoghi storici usati    | 30                                                  |
| Max analoghi per asset    | 3                                                   |
| Hit EMA200 12w analoghi   | +20,00%                                             |
| Max gain mediano 12w      | +19,27%                                             |
| Drawdown mediano 12w      | -26,97%                                             |

Lettura semplice:

**CONTESTO BUONO VERSO EMA200, MA NON PESA NEL GLOBAL**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-10 12:10 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-10 12:06:33 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante in miglioramento rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +77.50% | +7.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +37.50% | -5.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | miglioramento | RIBASSISTA | +15.00% | +2.50 punti |

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
| BTC | 61.119 $ | 70.769 $ | +7,14% | +15,79% | rimbalzo poco frequente | 70.769 $ | 61.119 $ | +8,33% | -13,64% | spike storicamente più resistente |
| SOL | 75,18 $ | 87,05 $ | +10,71% | +15,79% | rimbalzo poco frequente | 87,05 $ | 75,18 $ | +27,78% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07043 $ | 0,08155 $ | +10,81% | +15,79% | rimbalzo poco frequente | 0,08155 $ | 0,07043 $ | +61,54% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 1 poi sono rimbalzati fino a +10,00%. Percentuale: +7,14% (1/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 2 poi sono scaricati a -5,00%. Percentuale: +8,33% (2/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +10,71% (3/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 18 prima sono saliti a +10,00%. Tra quei 18, 5 poi sono scaricati a -5,00%. Percentuale: +27,78% (5/18). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 37 prima sono scesi a -5,00%. Tra quei 37, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +10,81% (4/37). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 13 prima sono saliti a +10,00%. Tra quei 13, 8 poi sono scaricati a -5,00%. Percentuale: +61,54% (8/13). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-10 12:09:17 UTC

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
| BTC     | 2026-07-10 | 64.327,47 $       | SALITA              | 77,50%          | 51.998,31 $ | 65.991,54 $ | 70.121,34 $ | 78.838,22 $ | 92.470,69 $ |
| SOL     | 2026-07-10 | 79,19 $           | DISCESA             | 37,50%          | 62,60 $     | 70,30 $     | 77,57 $     | 86,35 $     | 113,84 $    |
| DOGE    | 2026-07-10 | 0.07409 $         | DISCESA             | 15,00%          | 0.04510 $   | 0.05066 $   | 0.05752 $   | 0.06838 $   | 0.07961 $   |

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
| BTC     | 1g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 1g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 1g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |

## Come leggerlo

- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.
- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.
- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.
- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.
- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.

Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. Sotto 5 controlli resta solo osservazione.
<!-- SCANNER_FORECAST_TRACKER_END -->

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-10 12:09 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione             | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:----------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO               | NO        | +77,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO               | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NEGATIVO / RIBASSISTA | SI        | +85,00%       | Casi negativi 85.00% >= 80%      |                  40 |

## DOGE — casi ribassisti

- Trigger: **Casi negativi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **-4,87%**
- Return mediano 14g: **-26,68%**
- Return mediano 30g: **-25,53%**
- Drawdown mediano: **-29,87%**
- Max gain mediano: **+3,27%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+3,20%**
- Spike massimo medio prima del minimo: **+5,08%**
- Spike p75 prima del minimo: **+5,77%**
- Giorno mediano dello spike: **giorno 2**
- Giorno mediano del minimo: **giorno 18**
- Scarico mediano dal picco al minimo: **-34,09%**
- Casi con almeno +5% prima del minimo: **+32,35%**
- Casi con almeno +10% prima del minimo: **+20,59%**
- Casi con almeno +15% prima del minimo: **+5,88%**
- Discesa quasi immediata: **+0,00%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90    |
|:--------|:--------|:--------|:--------|:-------|
| -40,82% | -32,25% | -25,53% | -13,28% | -5,81% |

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
| WAVES-USD       | 2022-05-30 | +84,44%      | +28,83%                  |              4 | -42,96%      |              17 | -55,72%          | -29,04%      | SPIKE PRIMA DEL DUMP          |
| LINK-USD        | 2022-05-30 | +84,37%      | +24,39%                  |             10 | -21,06%      |              14 | -36,54%          | -16,73%      | SPIKE PRIMA DEL DUMP          |
| OP-USD          | 2026-03-11 | +84,46%      | +14,28%                  |              5 | -15,36%      |              18 | -25,94%          | -4,42%       | SPIKE PRIMA DEL DUMP          |
| AVAX-USD        | 2025-11-21 | +86,16%      | +12,94%                  |              6 | -14,04%      |              27 | -23,89%          | -8,75%       | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2022-05-30 | +84,55%      | +12,55%                  |              9 | -19,98%      |              19 | -28,90%          | -18,34%      | SPIKE PRIMA DEL DUMP          |
| LTC-USD         | 2022-05-28 | +83,98%      | +10,92%                  |              2 | -30,51%      |              16 | -37,36%          | -10,25%      | SPIKE PRIMA DEL DUMP          |
| BAT-USD         | 2018-12-27 | +84,12%      | +10,32%                  |             13 | -6,08%       |              17 | -14,87%          | -1,76%       | PERCORSO RIBASSISTA MISTO     |
| DOT-USD         | 2023-09-22 | +83,31%      | +6,01%                   |              9 | -9,22%       |              27 | -14,37%          | -1,36%       | PERCORSO RIBASSISTA MISTO     |
| CHZ-USD         | 2022-06-03 | +86,77%      | +5,97%                   |              3 | -28,71%      |              15 | -32,73%          | -19,17%      | RIALZO MODESTO PRIMA DEL DUMP |
| ZEC-USD         | 2019-08-24 | +86,88%      | +5,15%                   |             25 | -11,71%      |              30 | -16,03%          | -11,71%      | RIALZO MODESTO PRIMA DEL DUMP |
| ENJ-USD         | 2022-06-04 | +86,27%      | +5,00%                   |              2 | -33,46%      |              14 | -36,63%          | -16,55%      | RIALZO MODESTO PRIMA DEL DUMP |
| XLM-USD         | 2022-05-30 | +83,81%      | +4,76%                   |              1 | -25,70%      |              14 | -29,08%          | -23,40%      | RIALZO MODESTO PRIMA DEL DUMP |
| VET-USD         | 2022-06-01 | +86,54%      | +4,39%                   |              8 | -29,00%      |              17 | -31,99%          | -27,52%      | RIALZO MODESTO PRIMA DEL DUMP |
| XTZ-USD         | 2026-03-15 | +87,30%      | +4,26%                   |              5 | -12,14%      |              14 | -15,73%          | -10,41%      | RIALZO MODESTO PRIMA DEL DUMP |
| BCH-USD         | 2022-05-30 | +85,04%      | +3,48%                   |              1 | -47,58%      |              29 | -49,34%          | -46,95%      | RIALZO MODESTO PRIMA DEL DUMP |
| NEO-USD         | 2022-05-30 | +85,51%      | +3,34%                   |              7 | -27,65%      |              19 | -29,99%          | -26,97%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2022-06-01 | +85,96%      | +3,20%                   |              1 | -42,93%      |              30 | -44,70%          | -42,93%      | RIALZO MODESTO PRIMA DEL DUMP |
| ETH-USD         | 2022-06-04 | +86,03%      | +3,20%                   |              2 | -44,85%      |              14 | -46,56%          | -36,11%      | RIALZO MODESTO PRIMA DEL DUMP |
| BTC-USD         | 2022-06-02 | +83,75%      | +2,96%                   |              4 | -37,58%      |              16 | -39,38%          | -36,84%      | PERCORSO RIBASSISTA MISTO     |
| FIL-USD         | 2022-06-03 | +84,97%      | +2,37%                   |              3 | -30,96%      |              15 | -32,56%          | -28,22%      | PERCORSO RIBASSISTA MISTO     |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
<!-- EXTREME_CASES_PATH_END -->



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
- Casi positivi / salita storica: **77,50%**
- Casi negativi / discesa storica: **22,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **64.335,35 $**
- Return normale fra 30 giorni: **70.129,94 $** (9,01%)
- Drawdown normale durante il mese: **62.294,55 $** (-3,17%)
- Drawdown brutto da rispettare: **58.555,97 $** (-8,98%)
- Max gain normale durante il mese: **76.139,89 $** (18,35%)
- Max gain buono / take profit ottimistico: **86.221,24 $** (34,02%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **37,50%**
- Casi negativi / discesa storica: **62,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **79,14 $**
- Return normale fra 30 giorni: **77,52 $** (-2,05%)
- Drawdown normale durante il mese: **69,03 $** (-12,77%)
- Drawdown brutto da rispettare: **59,12 $** (-25,30%)
- Max gain normale durante il mese: **85,30 $** (7,79%)
- Max gain buono / take profit ottimistico: **97,00 $** (22,56%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **15,00%**
- Casi negativi / discesa storica: **85,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,06 $** (-22,37%)
- Drawdown normale durante il mese: **0,05 $** (-28,67%)
- Drawdown brutto da rispettare: **0,05 $** (-38,18%)
- Max gain normale durante il mese: **0,08 $** (4,32%)
- Max gain buono / take profit ottimistico: **0,08 $** (12,65%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è prudente/debole. Lo scanner vede più rischio di discesa che salita pulita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 64.335,35 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **77,50%**
- Probabilità storica di discesa: **22,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **52.004,68 $** (-19,17%)
- Se va male: **65.999,63 $** (2,59%)
- Scenario normale: **70.129,94 $** (9,01%)
- Se va bene: **78.847,88 $** (22,56%)
- Se va molto bene: **92.482,02 $** (43,75%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **62.294,55 $** (-3,17%)
- Discesa brutta: **58.555,97 $** (-8,98%)
- Discesa molto brutta: **45.713,87 $** (-28,94%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **76.139,89 $** (18,35%)
- Rialzo buono: **86.221,24 $** (34,02%)
- Rialzo molto forte: **104.620,27 $** (62,62%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **62.294,55 $** e uno spike normale intorno a **76.139,89 $**.

La chiusura a 30 giorni era più spesso positiva: salita 77,50%, discesa 22,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 79,14 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **37,50%**
- Probabilità storica di discesa: **62,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **62,56 $** (-20,95%)
- Se va male: **70,25 $** (-11,23%)
- Scenario normale: **77,52 $** (-2,05%)
- Se va bene: **86,30 $** (9,05%)
- Se va molto bene: **113,76 $** (43,75%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **69,03 $** (-12,77%)
- Discesa brutta: **59,12 $** (-25,30%)
- Discesa molto brutta: **54,63 $** (-30,98%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **85,30 $** (7,79%)
- Rialzo buono: **97,00 $** (22,56%)
- Rialzo molto forte: **123,28 $** (55,77%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **69,03 $** e uno spike normale intorno a **85,30 $**.

La chiusura a 30 giorni era più spesso negativa: salita 37,50%, discesa 62,50%. Quindi la lettura principale è prudente/debole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,07 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **15,00%**
- Probabilità storica di discesa: **85,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-39,13%)
- Se va male: **0,05 $** (-31,62%)
- Scenario normale: **0,06 $** (-22,37%)
- Se va bene: **0,07 $** (-7,70%)
- Se va molto bene: **0,08 $** (7,45%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,05 $** (-28,67%)
- Discesa brutta: **0,05 $** (-38,18%)
- Discesa molto brutta: **0,04 $** (-44,76%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (4,32%)
- Rialzo buono: **0,08 $** (12,65%)
- Rialzo molto forte: **0,09 $** (24,59%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,05 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni era più spesso negativa: salita 15,00%, discesa 85,00%. Quindi la lettura principale è prudente/debole.

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

**Prezzo attuale:** 64.335,35 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **77,50%**
- Casi negativi dopo 30 giorni: **22,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,84%**
- Rendimento medio dopo 30 giorni: **13,63%**
- Rendimento centrale dopo 30 giorni: **9,01%**
- Discesa media durante i 30 giorni: **-7,49%**
- Massimo rialzo medio durante i 30 giorni: **26,23%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **73.106,48 $**
- Scenario centrale a 30 giorni: **70.129,94 $**
- Zona di rischio media: **59.514,34 $**
- Zona di rialzo media: **81.207,59 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -19,17% → **52.004,68 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 2,59% → **65.999,63 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 9,01% → **70.129,94 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,56% → **78.847,88 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 43,75% → **92.482,02 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,94% → **45.713,87 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -8,98% → **58.555,97 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,17% → **62.294,55 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **64.335,35 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **64.335,35 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,58% → **65.348,64 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,51% → **69.170,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 18,35% → **76.139,89 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 34,02% → **86.221,24 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 62,62% → **104.620,27 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-09-19   | 2018-12-27 |        88.93 |        95.69 |           0    |         178.55 |
| XRP-USD         | 2019-09-24   | 2020-01-01 |        88.87 |        24.17 |          -2.4  |          26.46 |
| FIL-USD         | 2023-06-19   | 2023-09-26 |        87.82 |        17.86 |           0    |          21.6  |
| KSM-USD         | 2022-03-10   | 2022-06-17 |        86.38 |        11.02 |          -4.93 |          16.96 |
| YFI-USD         | 2023-06-14   | 2023-09-21 |        86.08 |         2.83 |          -3.99 |           8.79 |
| ETC-USD         | 2019-05-12   | 2019-08-19 |        86.04 |        15.03 |           0    |          32.2  |
| XLM-USD         | 2020-01-07   | 2020-04-15 |        85.75 |        45.24 |           0    |          62.58 |
| ONE-USD         | 2020-01-07   | 2020-04-15 |        85.68 |        14.92 |           0    |          14.92 |
| ETH-USD         | 2023-06-15   | 2023-09-22 |        85.47 |         4.4  |          -3.37 |           8.82 |
| DOT-USD         | 2023-06-15   | 2023-09-22 |        85.35 |        -1.36 |          -9.22 |           6.01 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 79,14 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **37,50%**
- Casi negativi dopo 30 giorni: **62,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,42%**
- Rendimento medio dopo 30 giorni: **5,22%**
- Rendimento centrale dopo 30 giorni: **-2,05%**
- Discesa media durante i 30 giorni: **-14,71%**
- Massimo rialzo medio durante i 30 giorni: **21,63%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **83,27 $**
- Scenario centrale a 30 giorni: **77,52 $**
- Zona di rischio media: **67,50 $**
- Zona di rialzo media: **96,26 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -20,95% → **62,56 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -11,23% → **70,25 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -2,05% → **77,52 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 9,05% → **86,30 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 43,75% → **113,76 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,98% → **54,63 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -25,30% → **59,12 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,77% → **69,03 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,76% → **76,95 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **79,14 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **79,14 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,43% → **79,48 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 7,79% → **85,30 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 22,56% → **97,00 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 55,77% → **123,28 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| TRX-USD         | 2018-09-19   | 2018-12-27 |        79.81 |        55.01 |           0    |          55.01 |
| QTUM-USD        | 2018-09-19   | 2018-12-27 |        79.71 |        -2.21 |          -3.68 |          15.25 |
| DASH-USD        | 2024-04-15   | 2024-07-23 |        79.55 |        -1.21 |         -16.66 |           1.64 |
| WAVES-USD       | 2019-02-21   | 2019-05-31 |        79.46 |       -30.84 |         -30.84 |           0.49 |
| XLM-USD         | 2020-01-07   | 2020-04-15 |        79.39 |        45.24 |           0    |          62.58 |
| NEAR-USD        | 2024-04-15   | 2024-07-23 |        79.09 |       -25.43 |         -38.83 |           0    |
| LRC-USD         | 2018-09-19   | 2018-12-27 |        78    |        95.69 |           0    |         178.55 |
| ENJ-USD         | 2018-09-19   | 2018-12-27 |        77.84 |       -16.11 |         -19.37 |           5.11 |
| BNB-USD         | 2025-12-06   | 2026-03-15 |        77.61 |        -8.86 |         -13.44 |           0.84 |
| VET-USD         | 2020-01-09   | 2020-04-17 |        77.42 |        16.09 |          -3.73 |          26.08 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,07 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **15,00%**
- Casi negativi dopo 30 giorni: **85,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,41%**
- Rendimento medio dopo 30 giorni: **-17,76%**
- Rendimento centrale dopo 30 giorni: **-22,37%**
- Discesa media durante i 30 giorni: **-26,64%**
- Massimo rialzo medio durante i 30 giorni: **8,61%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,06 $**
- Scenario centrale a 30 giorni: **0,06 $**
- Zona di rischio media: **0,05 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -39,13% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -31,62% → **0,05 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -22,37% → **0,06 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: -7,70% → **0,07 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 7,45% → **0,08 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -44,76% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -38,18% → **0,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -28,67% → **0,05 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -13,56% → **0,06 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -6,03% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,56% → **0,07 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 4,32% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 12,65% → **0,08 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 24,59% → **0,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2022-02-20   | 2022-05-30 |        88.77 |       -29.45 |         -33.95 |           2.32 |
| NEAR-USD        | 2022-03-02   | 2022-06-09 |        88.63 |       -25.05 |         -39.1  |           0    |
| XRP-USD         | 2019-09-24   | 2020-01-01 |        88.32 |        24.17 |          -2.4  |          26.46 |
| XTZ-USD         | 2025-12-06   | 2026-03-15 |        87.3  |       -10.41 |         -12.14 |           4.26 |
| QTUM-USD        | 2022-02-20   | 2022-05-30 |        87.26 |       -31.65 |         -37.87 |           0    |
| XLM-USD         | 2019-09-29   | 2020-01-06 |        87.22 |        39.92 |          -5.54 |          39.92 |
| ZEC-USD         | 2019-05-17   | 2019-08-24 |        86.88 |       -11.71 |         -11.71 |           5.15 |
| CHZ-USD         | 2022-02-24   | 2022-06-03 |        86.77 |       -19.17 |         -28.71 |           5.97 |
| VET-USD         | 2022-02-22   | 2022-06-01 |        86.54 |       -27.52 |         -29    |           4.39 |
| 1INCH-USD       | 2022-02-22   | 2022-06-01 |        86.46 |       -31.62 |         -42.19 |           0    |

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-07-10 12:09 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       64327.2  | False                | -11.95%             | -10.27%                  | BEAR               | -11.95%          | -10.27%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -20.39%             | -16.68%                  | BEAR               | -11.95%          | -10.27%               |
| SOL-USD  | BEAR                  |          79.2  | False                | -6.77%              | -18.73%                  | BEAR               | -11.95%          | -10.27%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 77.50%              | 9.01%            | 22.56%           | 43.75%           | -3.17%             | -28.94%            | 18.35%             | 34.02%             | 62.62%             | 75.00%              | 30.82%           | 51.81%           | 65.33%           |
| BTC-USD  | SAME_BTC_REGIME           |        17 | 100.00%             | 25.70%           | 43.58%           | 67.02%           | 0.00%              | -4.32%             | 37.70%             | 62.58%             | 70.49%             | 94.12%              | 42.97%           | 52.55%           | 89.02%           |
| BTC-USD  | SAME_ASSET_REGIME         |        29 | 86.21%              | 14.92%           | 24.17%           | 47.87%           | -1.26%             | -9.42%             | 21.60%             | 34.23%             | 62.89%             | 89.66%              | 40.39%           | 53.88%           | 76.40%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        15 | 100.00%             | 22.02%           | 37.45%           | 71.35%           | 0.00%              | -4.53%             | 34.23%             | 55.26%             | 73.66%             | 93.33%              | 40.39%           | 49.94%           | 106.30%          |
| DOGE-USD | ALL_MATCHES               |        40 | 15.00%              | -22.37%          | -7.70%           | 7.45%            | -28.67%            | -44.76%            | 4.32%              | 12.65%             | 24.59%             | 42.50%              | -6.79%           | 11.78%           | 25.66%           |
| DOGE-USD | SAME_BTC_REGIME           |        32 | 9.38%               | -26.01%          | -15.02%          | -2.03%           | -30.74%            | -44.84%            | 3.41%              | 10.47%             | 24.28%             | 40.62%              | -6.79%           | 10.58%           | 23.65%           |
| DOGE-USD | SAME_ASSET_REGIME         |        35 | 14.29%              | -23.93%          | -7.40%           | 4.57%            | -29.00%            | -44.81%            | 4.26%              | 11.74%             | 25.63%             | 42.86%              | -5.40%           | 13.54%           | 31.24%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        31 | 9.68%               | -26.97%          | -13.48%          | -1.76%           | -30.51%            | -44.85%            | 3.48%              | 10.62%             | 24.39%             | 38.71%              | -8.19%           | 10.93%           | 24.54%           |
| SOL-USD  | ALL_MATCHES               |        40 | 37.50%              | -2.05%           | 9.05%            | 43.75%           | -12.77%            | -30.98%            | 7.79%              | 22.56%             | 55.77%             | 55.00%              | 5.83%            | 32.43%           | 52.68%           |
| SOL-USD  | SAME_BTC_REGIME           |        25 | 52.00%              | 0.89%            | 16.09%           | 44.58%           | -8.00%             | -22.16%            | 11.93%             | 29.71%             | 59.55%             | 76.00%              | 8.91%            | 32.98%           | 53.35%           |
| SOL-USD  | SAME_ASSET_REGIME         |        27 | 44.44%              | -0.45%           | 13.80%           | 49.15%           | -9.99%             | -23.47%            | 10.51%             | 23.53%             | 58.04%             | 66.67%              | 8.26%            | 33.34%           | 52.02%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        20 | 50.00%              | 0.22%            | 12.80%           | 46.22%           | -8.81%             | -19.84%            | 11.22%             | 27.59%             | 55.77%             | 75.00%              | 8.58%            | 32.43%           | 46.16%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        17 | 100.00%             | 25.70%           | 0.00%              | 62.58%             | 94.12%              | 42.97%           | 78.05%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |         9 | 44.44%              | -2.75%           | -8.75%             | 9.98%              | 44.44%              | -3.75%           | 83.14%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |        10 | 80.00%              | 4.33%            | -4.56%             | 17.31%             | 100.00%             | 25.15%           | 71.54%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         4 | 50.00%              | -8.18%           | -24.68%            | 12.51%             | 0.00%               | -29.87%          | 12.51%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        32 | 9.38%               | -26.01%          | -30.74%            | 10.47%             | 40.62%              | -6.79%           | 22.67%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         3 | 33.33%              | -8.75%           | -14.04%            | 14.60%             | 33.33%              | -9.16%           | 15.40%             |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION |         3 | 66.67%              | 18.71%           | -2.40%             | 23.10%             | 100.00%             | 21.64%           | 115.31%            |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         2 | 0.00%               | -18.86%          | -18.86%            | 3.86%              | 0.00%               | -38.05%          | 3.86%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        25 | 52.00%              | 0.89%            | -8.00%             | 29.71%             | 76.00%              | 8.91%            | 58.38%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |        10 | 0.00%               | -14.80%          | -28.59%            | 1.40%              | 0.00%               | -8.45%           | 1.40%              |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         3 | 66.67%              | 17.86%           | -5.48%             | 97.60%             | 100.00%             | 50.78%           | 127.37%            |
| SOL-USD  | HISTORICAL_BTC_RECOVERY     |         2 | 0.00%               | -16.77%          | -29.03%            | 11.14%             | 0.00%               | -35.08%          | 11.14%             |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        29 | 86.21%              | 14.92%           | -1.26%             | 34.23%             | 89.66%              | 40.39%           | 78.05%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         4 | 25.00%              | -15.12%          | -20.59%            | 8.51%              | 25.00%              | -12.33%          | 47.44%             |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         2 | 100.00%             | 21.29%           | -3.17%             | 30.83%             | 100.00%             | 34.70%           | 69.81%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         5 | 60.00%              | 5.95%            | -11.70%            | 32.20%             | 20.00%              | -24.31%          | 32.20%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        35 | 14.29%              | -23.93%          | -29.00%            | 11.74%             | 42.86%              | -5.40%           | 26.61%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         3 | 33.33%              | -12.18%          | -17.30%            | 8.26%              | 66.67%              | 5.41%            | 15.40%             |
| DOGE-USD | HISTORICAL_ASSET_MIXED        |         1 | 0.00%               | -8.75%           | -14.04%            | 12.94%             | 0.00%               | -9.16%           | 12.94%             |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         1 | 0.00%               | -11.71%          | -11.71%            | 5.15%              | 0.00%               | -34.20%          | 5.15%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        27 | 44.44%              | -0.45%           | -9.99%             | 23.53%             | 66.67%              | 8.26%            | 61.61%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         4 | 0.00%               | -19.12%          | -29.62%            | 0.21%              | 25.00%              | -6.73%           | 0.21%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         3 | 0.00%               | -10.79%          | -27.41%            | 0.55%              | 0.00%               | -12.07%          | 0.55%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 50.00%              | 3.47%            | -17.29%            | 28.80%             | 50.00%              | 10.69%           | 67.73%             |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-19   | 88.93%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| BTC-USD  | KSM-USD         | 2022-03-10   | 86.38%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 11.02%       | -4.93%         | 16.96%         | 14.38%       | -4.93%         | 37.01%         |
| BTC-USD  | XLM-USD         | 2020-01-07   | 85.75%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 85.68%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | TRX-USD         | 2020-01-07   | 85.35%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 22.02%       | 0.00%          | 33.95%         | 32.98%       | 0.00%          | 48.70%         |
| BTC-USD  | EOS-USD         | 2020-01-07   | 84.94%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 7.83%        | 0.00%          | 25.64%         | 7.27%        | 0.00%          | 25.64%         |
| BTC-USD  | MKR-USD         | 2021-07-21   | 84.89%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 29.66%       | -0.21%         | 38.63%         | 12.58%       | -6.23%         | 38.63%         |
| BTC-USD  | ADA-USD         | 2020-01-07   | 84.40%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 58.37%       | 0.00%          | 64.15%         | 140.87%      | 0.00%          | 179.32%        |
| BTC-USD  | OMG-USD         | 2020-01-07   | 84.31%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 79.99%       | 0.00%          | 79.99%         | 195.80%      | 0.00%          | 253.59%        |
| BTC-USD  | SOL-USD         | 2022-03-10   | 84.11%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 25.70%       | 0.00%          | 37.70%         | 40.39%       | 0.00%          | 51.21%         |
| DOGE-USD | DASH-USD        | 2022-02-20   | 88.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | XTZ-USD         | 2025-12-06   | 87.30%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.41%      | -12.14%        | 4.26%          | -2.16%       | -12.14%        | 4.26%          |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 87.26%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XLM-USD         | 2019-09-29   | 87.22%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | CHZ-USD         | 2022-02-24   | 86.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -19.17%      | -28.71%        | 5.97%          | 11.61%       | -28.71%        | 22.22%         |
| DOGE-USD | VET-USD         | 2022-02-22   | 86.54%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | 1INCH-USD       | 2022-02-22   | 86.46%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.62%      | -42.19%        | 0.00%          | -20.09%      | -42.19%        | 0.00%          |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.43%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | THETA-USD       | 2022-02-24   | 86.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 1.59%        | -8.56%         | 23.35%         | 14.81%       | -8.85%         | 24.03%         |
| DOGE-USD | ENJ-USD         | 2022-02-25   | 86.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -16.55%      | -33.46%        | 5.00%          | 1.45%        | -33.46%        | 5.00%          |
| SOL-USD  | TRX-USD         | 2018-09-19   | 79.81%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 55.01%       | 0.00%          | 55.01%         | 32.25%       | 0.00%          | 58.38%         |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 79.71%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | XLM-USD         | 2020-01-07   | 79.39%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| SOL-USD  | LRC-USD         | 2018-09-19   | 78.00%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| SOL-USD  | ENJ-USD         | 2018-09-19   | 77.84%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | -16.11%      | -19.37%        | 5.11%          | 93.16%       | -38.09%        | 93.16%         |
| SOL-USD  | NEAR-USD        | 2025-12-01   | 77.39%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 6.36%        | -9.61%         | 16.07%         | 21.89%       | -9.61%         | 24.08%         |
| SOL-USD  | SOL-USD         | 2025-12-04   | 77.29%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -7.51%       | -10.44%        | 9.16%          | 6.95%        | -10.44%        | 10.43%         |
| SOL-USD  | XRP-USD         | 2020-01-07   | 77.26%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 9.73%        | 0.00%          | 25.47%         | 5.71%        | 0.00%          | 25.47%         |
| SOL-USD  | APT-USD         | 2024-09-01   | 76.90%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.92%        | -11.47%        | 6.42%          | -34.40%      | -34.40%        | 6.42%          |
| SOL-USD  | ONE-USD         | 2020-04-16   | 75.70%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.89%        | -24.91%        | 11.93%         | -10.01%      | -24.91%        | 11.93%         |

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

Generato: 2026-07-10 12:09 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             | Divergenza                                                   | Wyckoff                 | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|:-------------------------------------------------------------|:------------------------|:-----------|:-------------|
| BTC     | 64.345   |          -2 | NEUTRALE / MISTO   | Trend ribassista | Momentum misto  | Struttura ribassista con massimi e minimi decrescenti | Divergenza rialzista RSI, Divergenza ribassista nascosta RSI | Possibile accumulazione | 57.748     | 64.598       |
| SOL     | 79,21    |           2 | NEUTRALE / MISTO   | Trend misto      | Momentum misto  | Volatilità in espansione                              | Nessuna                                                      | Range / fase non chiara | 64,42      | 83,81        |
| DOGE    | 0.07414  |         -10 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | Divergenza ribassista nascosta RSI                           | Possibile accumulazione | 0.06961    | 0.07923      |

## Riepilogo pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom     | Doppio massimo   | Triplo massimo   | Adam/Eve Top     |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------|:-----------------|:-----------------|:-----------------|--------------------:|
| BTC     | Possibile       | Possibile       | Adam and Eve Bottom | Possibile        | Confermato       | Adam and Eve Top |                  -2 |
| SOL     | Confermato      | Possibile       | Adam and Eve Bottom | Possibile        | Confermato       | Eve and Adam Top |                   1 |
| DOGE    | Assente         | Possibile       | Adam and Eve Bottom | Assente          | Confermato       | Eve and Adam Top |                  -4 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC     |    54.57 |         630.44    | 61.826  | 65.373  | 74.104  | -9,33%              | -10,10%              | 1,23%            | -9,06%           |
| SOL     |    56.8  |           0.39481 | 75,63   | 74,71   | 92,21   | -6,31%              | -18,37%              | 18,54%           | -2,85%           |
| DOGE    |    37.85 |           0.00049 | 0.07559 | 0.08518 | 0.10156 | -13,28%             | -16,38%              | -13,77%          | -18,38%          |

## Dettaglio asset

### BTC

- Prezzo: **64.345**
- Punteggio tecnico: **-2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.554e+04 -> 6.46e+04.
- Divergenza: **Divergenza rialzista RSI, Divergenza ribassista nascosta RSI** (1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 54.6.
- Supporto più vicino: **57.748**
- Resistenza più vicina: **64.598**

Pattern classici:

- Doppio minimo: **Possibile**
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248.
- Triplo minimo: **Possibile**
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248.
- Adam/Eve Bottom: **Adam and Eve Bottom**
  - Possibile pattern Adam and Eve Bottom vicino a 62.201 dal 2026-03-29 al 2026-06-18. Nel modello Adam/Eve un minimo è più appuntito e violento, l'altro è più arrotondato. Neckline stimata: 82.792.
- Doppio massimo: **Possibile**
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-07-06. Neckline ribassista stimata: 57.748.
- Triplo massimo: **Confermato**
  - Tre massimi simili vicino a 79.488 dal 2026-04-22 al 2026-05-26. Neckline ribassista stimata: 74.959.
- Adam/Eve Top: **Adam and Eve Top**
  - Possibile pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-06. Nel modello Adam/Eve un massimo è più appuntito e violento, l'altro è più arrotondato. Neckline ribassista stimata: 57.748.

### SOL

- Prezzo: **79,21**
- Punteggio tecnico: **2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 67.92 -> 64.42. Ultimi massimi: 74.89 -> 83.81.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 49,65%. Fase non abbastanza chiara.
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

- Prezzo: **0.07414**
- Punteggio tecnico: **-10 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07809 -> 0.06961. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 37.8.
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

Generato: 2026-07-10 12:09 UTC

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
| BTC | 64.345 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | SPRING / TEST POSSIBILE | MEDIO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 79,21 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | RANGE / FASE NON CHIARA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07414 $ | -9 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | -2 | +1 | +2 | 0 | 0 | +1 | -2 |
| SOL | -4 | 0 | 0 | +2 | 0 | 0 | 0 | -2 |
| DOGE | -4 | -2 | -2 | +1 | 0 | 0 | -2 | -9 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.062 $ | 64.598 $ | 82.430 $ | 57.748 $ | 3,04% | 4,71% | -11,92% |
| SOL | 78,43 $ | 83,22 $ | 98,27 $ | 60,41 $ | 4,20% | 25,41% | -6,76% |
| DOGE | 0.07206 $ | 0.07923 $ | 0.11825 $ | 0.06961 $ | 3,87% | -10,63% | -20,38% |

## Lettura dettagliata

### BTC

- Prezzo: **64.345 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 3,04%; distanza supporto 2,03%; distanza resistenza 0,39%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+1** — RSI sano 54.6; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.13; volume ratio 0.92
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 54.57 |
| MACD histogram | 630.43968 |
| CMF20 | 0.130 |
| Volume ratio 20 | 0.92 |
| MA20 | 61.826 $ |
| MA50 | 65.373 $ |
| MA100 | 70.792 $ |
| MA200 | 74.104 $ |
| Pendenza MA50 20g | -9,72% |
| Pendenza MA200 60g | -10,27% |
| Bollinger width | 11,21% |
| Bollinger position | 0.85 |

### SOL

- Prezzo: **79,21 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 4,20%; distanza supporto 0,99%; distanza resistenza 5,06%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 56.8; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.09; volume ratio 0.66
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 56.80 |
| MACD histogram | 0.39481 |
| CMF20 | 0.087 |
| Volume ratio 20 | 0.66 |
| MA20 | 75,63 $ |
| MA50 | 74,71 $ |
| MA100 | 80,42 $ |
| MA200 | 92,21 $ |
| Pendenza MA50 20g | -6,59% |
| Pendenza MA200 60g | -18,73% |
| Bollinger width | 25,35% |
| Bollinger position | 0.68 |

### DOGE

- Prezzo: **0.07414 $**
- Score classico: **-9 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,87%; distanza supporto 2,89%; distanza resistenza 6,87%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-2** — RSI debole 37.8; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.00; volume ratio 0.78
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 37.85 |
| MACD histogram | 0.00049 |
| CMF20 | 0.003 |
| Volume ratio 20 | 0.78 |
| MA20 | 0.07559 $ |
| MA50 | 0.08518 $ |
| MA100 | 0.09329 $ |
| MA200 | 0.10156 $ |
| Pendenza MA50 20g | -13,74% |
| Pendenza MA200 60g | -16,68% |
| Bollinger width | 16,44% |
| Bollinger position | 0.38 |

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

Generato: 2026-07-10 12:09 UTC

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
| BTC | 64.345 $ | Doppio massimo | CONFERMATO | ribassista | NEL RANGE | 62.553 $ | 64.598 $ |
| SOL | 79,21 $ | Testa e spalle | CONFERMATO | ribassista | NEL RANGE | 78,43 $ | 83,81 $ |
| DOGE | 0.07414 $ | Doppio massimo | CONFERMATO | ribassista | NEL RANGE | 0.06961 $ | 0.07923 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CONFERMATO**
- Famiglia: **ribassista**
- Dettaglio: Due massimi simili a 78.321 $ e 77.991 $. Neckline circa 74.959 $.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **64.598 $**
- Breakout 60g: **82.430 $**
- Breakdown 60g: **57.748 $**
- RSI14: **54.57**
- ATR14: **3,04%**
- Volume ratio 20g: **0.92**
- Rendimento 30g: **+4,71%**
- Rendimento 90g: **-11,92%**

### Pattern trovati

| Pattern | Stato | Famiglia | Neckline | Dettaglio |
| --- | --- | --- | --- | --- |
| Doppio massimo | CONFERMATO | ribassista | 74.959 $ | Due massimi simili a 78.321 $ e 77.991 $. Neckline circa 74.959 $. |
| Triangolo discendente possibile | CANDIDATO | ribassista | n/a | Massimi decrescenti e supporto quasi piatto. |
| Doppio minimo | CANDIDATO | rialzista | 67.248 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Testa e spalle**
- Stato pattern: **CONFERMATO**
- Famiglia: **ribassista**
- Dettaglio: Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **78,43 $**
- Resistenza: **83,81 $**
- Breakout 60g: **98,27 $**
- Breakdown 60g: **60,41 $**
- RSI14: **56.80**
- ATR14: **4,20%**
- Volume ratio 20g: **0.66**
- Rendimento 30g: **+25,41%**
- Rendimento 90g: **-6,76%**

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
- RSI14: **37.85**
- ATR14: **3,87%**
- Volume ratio 20g: **0.78**
- Rendimento 30g: **-10,63%**
- Rendimento 90g: **-20,38%**

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

Generato: 2026-07-10 12:09 UTC

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
- Prezzo SOL corrente: **79,21 $**
- Verdetto: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza: **+65,04%**
- Tracking: **STORICO INIZIALE**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Confronto dal bottom a oggi

- Giorni controllati dal bottom: **35**
- Giorni controllati da inizio programma/scanner: **8**
- Errore medio assoluto dal bottom: **9,59%**
- Errore medio assoluto ultimi 7 giorni: **21,17%**
- Errore medio assoluto da inizio programma/scanner: **21,60%**
- Errore ultimo giorno: **+19,39%**
- Stato: **DEVIAZIONE MODERATA**

## Grafico completo: bottom, inizio programma e proiezione giornaliera

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato - ultimi 60 giorni

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap: **+19,39%**
- Media mobile 7g gap: **+21,17%**
- Variazione recente gap: **-2,25%**
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
|       33 | 2026-07-09 | 2022-12-24     | 78,05 $     | 66,37 $       | +17,60%  | da inizio programma |
|       34 | 2026-07-10 | 2022-12-25     | 79,21 $     | 66,34 $       | +19,39%  | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Base frattale   | Min percorso   | Max percorso   | Controllato   | Prezzo reale   | Errore   | Dentro banda   |
|:------------|:--------------|:----------------|:---------------|:---------------|:--------------|:---------------|:---------|:---------------|
| 7g          | 2026-07-17    | 78,19 $         | 77,82 $        | 79,58 $        | no            | n/a            | n/a      | n/a            |
| 14g         | 2026-07-24    | 80,38 $         | 77,82 $        | 80,38 $        | no            | n/a            | n/a      | n/a            |
| 21g         | 2026-07-31    | 98,21 $         | 77,82 $        | 98,65 $        | no            | n/a            | n/a      | n/a            |
| 28g         | 2026-08-07    | 106,86 $        | 77,82 $        | 107,13 $       | no            | n/a            | n/a      | n/a            |
| 35g         | 2026-08-14    | 111,81 $        | 77,82 $        | 111,81 $       | no            | n/a            | n/a      | n/a            |
| 42g         | 2026-08-21    | 107,96 $        | 77,82 $        | 111,81 $       | no            | n/a            | n/a      | n/a            |
| 49g         | 2026-08-28    | 102,47 $        | 77,82 $        | 111,81 $       | no            | n/a            | n/a      | n/a            |
| 56g         | 2026-09-04    | 114,42 $        | 77,82 $        | 115,89 $       | no            | n/a            | n/a      | n/a            |
| 63g         | 2026-09-11    | 110,81 $        | 77,82 $        | 116,77 $       | no            | n/a            | n/a      | n/a            |
| 70g         | 2026-09-18    | 105,52 $        | 77,82 $        | 116,77 $       | no            | n/a            | n/a      | n/a            |
| 77g         | 2026-09-25    | 104,24 $        | 77,82 $        | 116,77 $       | no            | n/a            | n/a      | n/a            |
| 84g         | 2026-10-02    | 131,87 $        | 77,82 $        | 131,87 $       | no            | n/a            | n/a      | n/a            |
| 91g         | 2026-10-09    | 131,66 $        | 77,82 $        | 133,26 $       | no            | n/a            | n/a      | n/a            |
| 98g         | 2026-10-16    | 132,62 $        | 77,82 $        | 133,94 $       | no            | n/a            | n/a      | n/a            |
| 105g        | 2026-10-23    | 133,25 $        | 77,82 $        | 133,94 $       | no            | n/a            | n/a      | n/a            |
| 112g        | 2026-10-30    | 142,58 $        | 77,82 $        | 143,38 $       | no            | n/a            | n/a      | n/a            |
| 119g        | 2026-11-06    | 129,77 $        | 77,82 $        | 143,38 $       | no            | n/a            | n/a      | n/a            |
| 126g        | 2026-11-13    | 137,65 $        | 77,82 $        | 143,38 $       | no            | n/a            | n/a      | n/a            |

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

**BTC** — BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $64,380 | +0.0057% | -0.38% | 1.94 | Misto | 1/5 |
| SOL | $79.23 | +0.0015% | -21.95% | 2.67 | Misto | 1/5 |
| DOGE | $0.07420 | +0.0100% | -1.57% | 3.08 | Rischio sotto | 2/5 |

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

<!-- DATA_QUALITY_COHERENCE_START -->
# Data quality / coherence check

Generato: 2026-07-10 12:10 UTC

Questo controllo non modifica punteggi o decisioni. Segnala soltanto problemi tecnici, dati mancanti e ambiguità di lettura.

## Stato finale: **OK**

## Coerenza prezzi snapshot

| Asset   | Stato   | Snapshot   | Scanner   | Differenza   |
|:--------|:--------|:-----------|:----------|:-------------|
| BTC     | OK      | 64.335 $   | 64.335 $  | +0,000%      |
| SOL     | OK      | 79,14 $    | 79,14 $   | +0,000%      |
| DOGE    | OK      | 0.07414 $  | 0.07414 $ | -0,000%      |

## Controllo codifica UTF-8

Nessun indicatore comune di mojibake trovato.

## File strutturati

- Snapshot condiviso: **OK**
- Scanner summary: **OK**

Il workflow è tecnicamente coerente nei controlli disponibili.
<!-- DATA_QUALITY_COHERENCE_END -->
