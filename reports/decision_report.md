# Decisione operativa sintetica

Generato: **2026-07-09 19:56:21 CEST**  
UTC: **2026-07-09 17:56:21 UTC**

Questo report prende tutti i dati dello scanner e li trasforma in una lettura pratica.

Scopo:

- capire se conviene spot, long, short o aspettare;
- separare long e short, invece di mettere tutto dentro una sola voce;
- usare parole semplici per zone alte, zone basse e rischio leva;
- leggere anche Global Confluence e Lifecycle EMA200, così il report decisionale non resta scollegato dalla sintesi principale.

## Dashboard veloce

| Asset | Prezzo | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.024 $ | BULLISH | COMPRA / ACCUMULA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | 78,01 $ | LEGGERMENTE BEARISH | TAKE PROFIT SU SPIKE / NON INSEGUIRE | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0,07291 $ | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

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

### Global Confluence e Lifecycle EMA200

Il Decision Report ora legge anche il Global Confluence.

Per SOL legge anche il modulo **Major alt lifecycle squeeze / EMA200 weekly**.

Questo serve a evitare che lo scanner 30 giorni, da solo, faccia sembrare SOL più bearish di quanto sia nella lettura globale.

Nota importante:

> il Lifecycle EMA200 migliora il bias spot, ma non autorizza leva da solo.

### Long e short

Il report separa le due cose:

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

Prezzo usato: **63.024 $**

- **Direzione:** BULLISH
- **Spot:** COMPRA / ACCUMULA
- **Long a leva:** LONG PRUDENTE
- **Short a leva:** NO SHORT
- **Max long:** max 2x isolated
- **Max short:** nessuna
- **Rischio:** MEDIO

### Perché

- molti casi storici chiudevano positivi (+70,00%); rendimento mediano positivo (+6,89%); media 30 giorni positiva (+11,61%); zona alta storica abbastanza lontana (+32,64%); rimbalzo dopo discesa debole (+17,65%); dump dopo spike poco frequente (+16,00%); troppi long aperti (2,13)

### Rischi principali

- zona bassa storica moderata (-9,39%); rimbalzo dopo discesa debole (+17,65%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +70,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | +6,89% | risultato centrale dei casi storici |
| Zona bassa storica | -9,39% | discesa pesante da rispettare |
| Zona alta storica | +32,64% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +17,65% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +16,00% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 2,13 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 59.873 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 69.327 $ | zona obiettivo dopo pullback |
| Spike +10% | 69.327 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 59.873 $ | zona di scarico dopo spike |
| Zona bassa storica | 57.107 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 83.594 $ | zona alta; se ci arriva, pensare a profitto |
| EMA200 weekly SOL | n/d | target tecnico del modulo lifecycle squeeze, solo se applicabile |

### Piano sintetico

> spot: valutare accumulo solo verso 59.873 $; long: long prudente, max 2x isolated; short: evitato; zona bassa storica/rischio: 57.107 $; zona alta storica/take profit: 83.594 $

---

## Solana — SOL

Prezzo usato: **78,01 $**

- **Direzione:** LEGGERMENTE BEARISH
- **Spot:** TAKE PROFIT SU SPIKE / NON INSEGUIRE
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** MOLTO ALTO

### Perché

- casi positivi sotto la media (+42,50%); zona alta storica abbastanza lontana (+22,56%); rimbalzo dopo discesa debole (+11,11%); troppi long aperti (2,73)

### Rischi principali

- zona bassa storica molto profonda (-23,56%); rimbalzo dopo discesa debole (+11,11%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +42,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -1,54% | risultato centrale dei casi storici |
| Zona bassa storica | -23,56% | discesa pesante da rispettare |
| Zona alta storica | +22,56% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +11,11% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +26,32% | se fa spike prima, quante volte poi scarica |
| Funding | +0,01% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 2,73 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 74,11 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 85,81 $ | zona obiettivo dopo pullback |
| Spike +10% | 85,81 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 74,11 $ | zona di scarico dopo spike |
| Zona bassa storica | 59,63 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 95,61 $ | zona alta; se ci arriva, pensare a profitto |
| EMA200 weekly SOL | n/d | target tecnico del modulo lifecycle squeeze, solo se applicabile |

### Piano sintetico

> spot: prendere profitto su spike verso 85,81 $; long: evitato; short: evitato; zona bassa storica/rischio: 59,63 $; zona alta storica/take profit: 95,61 $

---

## Dogecoin — DOGE

Prezzo usato: **0,07291 $**

- **Direzione:** BEARISH
- **Spot:** VENDI PARZIALE / STAI FUORI
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** SHORT SOLO DOPO SPIKE
- **Max long:** nessuna
- **Max short:** max 1x-2x isolated
- **Rischio:** MOLTO ALTO

### Perché

- pochi casi storici positivi (+12,50%); rendimento mediano negativo (-20,25%); media 30 giorni negativa (-16,99%); rimbalzo dopo discesa debole (+8,33%); dump dopo spike frequente (+66,67%); troppi long aperti (3,34)

### Rischi principali

- zona bassa storica molto profonda (-37,60%); gli spike venivano spesso scaricati (+66,67%); rimbalzo dopo discesa debole (+8,33%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +12,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -20,25% | risultato centrale dei casi storici |
| Zona bassa storica | -37,60% | discesa pesante da rispettare |
| Zona alta storica | +12,34% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +8,33% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +66,67% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 3,34 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 0,06926 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 0,08020 $ | zona obiettivo dopo pullback |
| Spike +10% | 0,08020 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 0,06926 $ | zona di scarico dopo spike |
| Zona bassa storica | 0,04550 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 0,08191 $ | zona alta; se ci arriva, pensare a profitto |
| EMA200 weekly SOL | n/d | target tecnico del modulo lifecycle squeeze, solo se applicabile |

### Piano sintetico

> spot: ridurre esposizione o stare fuori; long: evitato; short: solo dopo spike verso 0,08020 $, possibile target scarico 0,06926 $; zona bassa storica/rischio: 0,04550 $; zona alta storica/take profit: 0,08191 $

---
