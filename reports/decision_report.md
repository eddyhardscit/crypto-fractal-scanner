# Decisione operativa sintetica

Generato: **2026-07-08 15:18:36 CEST**  
UTC: **2026-07-08 13:18:36 UTC**

Questo report prende tutti i dati dello scanner e li trasforma in una lettura pratica.

Scopo:

- capire se conviene spot, long, short o aspettare;
- separare long e short, invece di mettere tutto dentro una sola voce;
- usare parole semplici per zone alte, zone basse e rischio leva.

## Dashboard veloce

| Asset | Prezzo | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.846 $ | LEGGERMENTE BULLISH | ACCUMULA SOLO SU PULLBACK | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | BASSO |
| SOL | 76,80 $ | LEGGERMENTE BEARISH | TAKE PROFIT SU SPIKE / NON INSEGUIRE | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0,07189 $ | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Spiegazione semplice

### Zona alta storica

Prima si chiamava `target rialzo storico P75`.

Nome più chiaro: **zona alta storica**.

Vuol dire:

> nei casi storici simili, quella era una zona alta raggiunta nei movimenti migliori.

Non vuol dire che il prezzo ci deve arrivare.

Uso pratico:

> se il prezzo arriva lì, non inseguire alla cieca; pensa a prendere profitto o alleggerire.

### Zona bassa storica

Prima si chiamava `drawdown P25`.

Nome più chiaro: **zona bassa storica**.

Vuol dire:

> nei casi storici simili, quella era una discesa pesante ma non impossibile.

Uso pratico:

> se fai leva, la liquidazione non dovrebbe stare vicino a quella zona.

### Long e short

Il report ora separa le due cose:

- **Long leva**: comprare con leva sperando che salga.
- **Short leva**: vendere con leva sperando che scenda.

Nota importante:

> `NO LONG` non significa automaticamente `SHORT`.

A volte la scelta migliore è semplicemente non fare niente.

Lo short viene indicato solo se:

- il quadro è bearish;
- oppure gli spike vengono spesso scaricati;
- e il report prova a indicare la zona dove avrebbe più senso, di solito **dopo uno spike**, non dopo che è già crollato.


## Dettaglio per asset

## Bitcoin — BTC

Prezzo usato: **61.846 $**

- **Direzione:** LEGGERMENTE BULLISH
- **Spot:** ACCUMULA SOLO SU PULLBACK
- **Long a leva:** LONG PRUDENTE
- **Short a leva:** NO SHORT
- **Max long:** max 2x isolated
- **Max short:** nessuna
- **Rischio:** BASSO

### Perché

- casi positivi sopra la media (+65,00%); rendimento mediano positivo (+3,39%); zona alta storica abbastanza lontana (+28,81%); troppi long aperti (1,57)

### Rischi principali

- zona bassa storica moderata (-9,52%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +65,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | +3,39% | risultato centrale dei casi storici |
| Zona bassa storica | -9,52% | discesa pesante da rispettare |
| Zona alta storica | +28,81% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +33,33% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +26,92% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 1,57 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 58.754 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 68.031 $ | zona obiettivo dopo pullback |
| Spike +10% | 68.031 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 58.754 $ | zona di scarico dopo spike |
| Zona bassa storica | 55.959 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 79.662 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: valutare accumulo solo verso 58.754 $; long: long prudente, max 2x isolated; short: evitato; zona bassa storica/rischio: 55.959 $; zona alta storica/take profit: 79.662 $

---

## Solana — SOL

Prezzo usato: **76,80 $**

- **Direzione:** LEGGERMENTE BEARISH
- **Spot:** TAKE PROFIT SU SPIKE / NON INSEGUIRE
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** MOLTO ALTO

### Perché

- casi positivi sotto la media (+45,00%); rimbalzo dopo discesa debole (+11,11%); dump dopo spike poco frequente (+18,75%); troppi long aperti (2,69)

### Rischi principali

- zona bassa storica molto profonda (-23,33%); rimbalzo dopo discesa debole (+11,11%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +45,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -2,05% | risultato centrale dei casi storici |
| Zona bassa storica | -23,33% | discesa pesante da rispettare |
| Zona alta storica | +16,73% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +11,11% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +18,75% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 2,69 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 72,96 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 84,48 $ | zona obiettivo dopo pullback |
| Spike +10% | 84,48 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 72,96 $ | zona di scarico dopo spike |
| Zona bassa storica | 58,88 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 89,65 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: prendere profitto su spike verso 84,48 $; long: evitato; short: evitato; zona bassa storica/rischio: 58,88 $; zona alta storica/take profit: 89,65 $

---

## Dogecoin — DOGE

Prezzo usato: **0,07189 $**

- **Direzione:** BEARISH
- **Spot:** VENDI PARZIALE / STAI FUORI
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** SHORT SOLO DOPO SPIKE
- **Max long:** nessuna
- **Max short:** max 1x-2x isolated
- **Rischio:** MOLTO ALTO

### Perché

- pochi casi storici positivi (+20,00%); rendimento mediano negativo (-18,45%); media 30 giorni negativa (-13,72%); rimbalzo dopo discesa debole (+16,67%); dump dopo spike da monitorare (+53,85%); troppi long aperti (3,20)

### Rischi principali

- zona bassa storica molto profonda (-37,60%); rimbalzo dopo discesa debole (+16,67%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +20,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -18,45% | risultato centrale dei casi storici |
| Zona bassa storica | -37,60% | discesa pesante da rispettare |
| Zona alta storica | +13,96% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +16,67% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +53,85% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 3,20 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 0,06830 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 0,07908 $ | zona obiettivo dopo pullback |
| Spike +10% | 0,07908 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 0,06830 $ | zona di scarico dopo spike |
| Zona bassa storica | 0,04486 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 0,08192 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: ridurre esposizione o stare fuori; long: evitato; short: solo dopo spike verso 0,07908 $, possibile target scarico 0,06830 $; zona bassa storica/rischio: 0,04486 $; zona alta storica/take profit: 0,08192 $

---
