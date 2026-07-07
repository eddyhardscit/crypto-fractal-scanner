# Decisione operativa sintetica

Generato: **2026-07-07 17:22:45 CEST**  
UTC: **2026-07-07 15:22:45 UTC**

Questo report prende tutti i dati dello scanner e li trasforma in una lettura pratica.

Scopo:

- capire se conviene spot, long, short o aspettare;
- separare long e short, invece di mettere tutto dentro una sola voce;
- usare parole semplici per zone alte, zone basse e rischio leva.

## Dashboard veloce

| Asset | Prezzo | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.551 $ | LEGGERMENTE BULLISH | ACCUMULA SOLO SU PULLBACK | LONG SOLO SU PULLBACK | NO SHORT | max 2x isolated | nessuna | BASSO |
| SOL | 81,63 $ | NEUTRALE / INCERTO | ASPETTA / HOLD | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0,07458 $ | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

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

Prezzo usato: **63.551 $**

- **Direzione:** LEGGERMENTE BULLISH
- **Spot:** ACCUMULA SOLO SU PULLBACK
- **Long a leva:** LONG SOLO SU PULLBACK
- **Short a leva:** NO SHORT
- **Max long:** max 2x isolated
- **Max short:** nessuna
- **Rischio:** BASSO

### Perché

- casi positivi sopra la media (+62,50%); zona alta storica abbastanza lontana (+24,17%); dump dopo spike poco frequente (+20,83%); troppi long aperti (1,88)

### Rischi principali

- zona bassa storica moderata (-9,26%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +62,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | +2,91% | risultato centrale dei casi storici |
| Zona bassa storica | -9,26% | discesa pesante da rispettare |
| Zona alta storica | +24,17% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +33,33% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +20,83% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 1,88 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 60.373 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 69.906 $ | zona obiettivo dopo pullback |
| Spike +10% | 69.906 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 60.373 $ | zona di scarico dopo spike |
| Zona bassa storica | 57.665 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 78.912 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: valutare accumulo solo verso 60.373 $; long: long solo su pullback, max 2x isolated; short: evitato; zona bassa storica/rischio: 57.665 $; zona alta storica/take profit: 78.912 $

---

## Solana — SOL

Prezzo usato: **81,63 $**

- **Direzione:** NEUTRALE / INCERTO
- **Spot:** ASPETTA / HOLD
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** MOLTO ALTO

### Perché

- rimbalzo dopo discesa debole (+17,24%); dump dopo spike poco frequente (+23,53%); troppi long aperti (2,80)

### Rischi principali

- zona bassa storica molto profonda (-23,14%); rimbalzo dopo discesa debole (+17,24%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +47,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -2,37% | risultato centrale dei casi storici |
| Zona bassa storica | -23,14% | discesa pesante da rispettare |
| Zona alta storica | +16,63% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +17,24% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +23,53% | se fa spike prima, quante volte poi scarica |
| Funding | -0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 2,80 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 77,55 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 89,79 $ | zona obiettivo dopo pullback |
| Spike +10% | 89,79 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 77,55 $ | zona di scarico dopo spike |
| Zona bassa storica | 62,74 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 95,20 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: aspettare, non forzare entrate; long: evitato; short: evitato; zona bassa storica/rischio: 62,74 $; zona alta storica/take profit: 95,20 $

---

## Dogecoin — DOGE

Prezzo usato: **0,07458 $**

- **Direzione:** BEARISH
- **Spot:** VENDI PARZIALE / STAI FUORI
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** SHORT SOLO DOPO SPIKE
- **Max long:** nessuna
- **Max short:** max 1x-2x isolated
- **Rischio:** MOLTO ALTO

### Perché

- pochi casi storici positivi (+17,50%); rendimento mediano negativo (-18,49%); media 30 giorni negativa (-14,22%); rimbalzo dopo discesa debole (+14,29%); dump dopo spike da monitorare (+60,00%); troppi long aperti (3,24)

### Rischi principali

- zona bassa storica molto profonda (-37,60%); gli spike venivano spesso scaricati (+60,00%); rimbalzo dopo discesa debole (+14,29%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +17,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -18,49% | risultato centrale dei casi storici |
| Zona bassa storica | -37,60% | discesa pesante da rispettare |
| Zona alta storica | +14,78% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +14,29% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +60,00% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 3,24 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 0,07085 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 0,08204 $ | zona obiettivo dopo pullback |
| Spike +10% | 0,08204 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 0,07085 $ | zona di scarico dopo spike |
| Zona bassa storica | 0,04654 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 0,08560 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: ridurre esposizione o stare fuori; long: evitato; short: solo dopo spike verso 0,08204 $, possibile target scarico 0,07085 $; zona bassa storica/rischio: 0,04654 $; zona alta storica/take profit: 0,08560 $

---
