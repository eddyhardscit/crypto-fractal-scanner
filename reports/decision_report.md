# Decisione operativa sintetica

Generato: **2026-07-06 13:00:12 CEST**  
UTC: **2026-07-06 11:00:12 UTC**

Questo report prende tutti i dati dello scanner e li trasforma in una lettura pratica.

Scopo:

- capire se conviene spot, long, short o aspettare;
- separare long e short, invece di mettere tutto dentro una sola voce;
- usare parole semplici per zone alte, zone basse e rischio leva.

## Dashboard veloce

| Asset | Prezzo | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.751 $ | NEUTRALE / INCERTO | ASPETTA / HOLD | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | 80,58 $ | NEUTRALE / INCERTO | ASPETTA / HOLD | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0,07706 $ | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

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

Prezzo usato: **62.751 $**

- **Direzione:** NEUTRALE / INCERTO
- **Spot:** ASPETTA / HOLD
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** MEDIO

### Perché

- leggera maggioranza positiva (+52,50%); zona alta storica abbastanza lontana (+23,62%); rimbalzo dopo discesa debole (+29,17%); dump dopo spike poco frequente (+22,73%); troppi long aperti (1,78)

### Rischi principali

- zona bassa storica importante (-12,55%); rimbalzo dopo discesa debole (+29,17%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +52,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | +1,25% | risultato centrale dei casi storici |
| Zona bassa storica | -12,55% | discesa pesante da rispettare |
| Zona alta storica | +23,62% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +29,17% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +22,73% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 1,78 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 59.613 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 69.026 $ | zona obiettivo dopo pullback |
| Spike +10% | 69.026 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 59.613 $ | zona di scarico dopo spike |
| Zona bassa storica | 54.873 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 77.575 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: aspettare, non forzare entrate; long: evitato; short: evitato; zona bassa storica/rischio: 54.873 $; zona alta storica/take profit: 77.575 $

---

## Solana — SOL

Prezzo usato: **80,58 $**

- **Direzione:** NEUTRALE / INCERTO
- **Spot:** ASPETTA / HOLD
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** MOLTO ALTO

### Perché

- zona alta storica abbastanza lontana (+23,82%); rimbalzo dopo discesa debole (+15,38%); troppi long aperti (2,73)

### Rischi principali

- zona bassa storica molto profonda (-23,45%); rimbalzo dopo discesa debole (+15,38%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +47,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -2,01% | risultato centrale dei casi storici |
| Zona bassa storica | -23,45% | discesa pesante da rispettare |
| Zona alta storica | +23,82% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +15,38% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +33,33% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 2,73 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 76,55 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 88,64 $ | zona obiettivo dopo pullback |
| Spike +10% | 88,64 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 76,55 $ | zona di scarico dopo spike |
| Zona bassa storica | 61,68 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 99,77 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: aspettare, non forzare entrate; long: evitato; short: evitato; zona bassa storica/rischio: 61,68 $; zona alta storica/take profit: 99,77 $

---

## Dogecoin — DOGE

Prezzo usato: **0,07706 $**

- **Direzione:** BEARISH
- **Spot:** VENDI PARZIALE / STAI FUORI
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** SHORT SOLO DOPO SPIKE
- **Max long:** nessuna
- **Max short:** max 1x-2x isolated
- **Rischio:** MOLTO ALTO

### Perché

- pochi casi storici positivi (+15,00%); rendimento mediano negativo (-18,49%); media 30 giorni negativa (-14,61%); rimbalzo dopo discesa debole (+13,89%); dump dopo spike frequente (+66,67%); troppi long aperti (3,11)

### Rischi principali

- zona bassa storica molto profonda (-37,24%); gli spike venivano spesso scaricati (+66,67%); rimbalzo dopo discesa debole (+13,89%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +15,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -18,49% | risultato centrale dei casi storici |
| Zona bassa storica | -37,24% | discesa pesante da rispettare |
| Zona alta storica | +13,96% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +13,89% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +66,67% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 3,11 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 0,07321 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 0,08477 $ | zona obiettivo dopo pullback |
| Spike +10% | 0,08477 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 0,07321 $ | zona di scarico dopo spike |
| Zona bassa storica | 0,04836 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 0,08781 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: ridurre esposizione o stare fuori; long: evitato; short: solo dopo spike verso 0,08477 $, possibile target scarico 0,07321 $; zona bassa storica/rischio: 0,04836 $; zona alta storica/take profit: 0,08781 $

---
