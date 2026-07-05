# Decisione operativa sintetica

Generato: **2026-07-05 14:10:10 CEST**  
UTC: **2026-07-05 12:10:10 UTC**

Questo report prende tutti i dati dello scanner e li trasforma in una lettura pratica.

Scopo:

- capire se conviene spot, long, short o aspettare;
- separare long e short, invece di mettere tutto dentro una sola voce;
- usare parole semplici per zone alte, zone basse e rischio leva.

## Dashboard veloce

| Asset | Prezzo | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.568 $ | NEUTRALE / INCERTO | ASPETTA / HOLD | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | 80,43 $ | NEUTRALE / INCERTO | ASPETTA / HOLD | NO LONG A LEVA | NO SHORT | nessuna | nessuna | ALTO |
| DOGE | 0,07579 $ | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

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

Prezzo usato: **62.568 $**

- **Direzione:** NEUTRALE / INCERTO
- **Spot:** ASPETTA / HOLD
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** MEDIO

### Perché

- casi positivi sotto la media (+40,00%); zona alta storica abbastanza lontana (+25,03%); rimbalzo dopo discesa debole (+22,73%); dump dopo spike poco frequente (+18,18%); troppi long aperti (1,76)

### Rischi principali

- zona bassa storica importante (-14,75%); rimbalzo dopo discesa debole (+22,73%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +40,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -2,14% | risultato centrale dei casi storici |
| Zona bassa storica | -14,75% | discesa pesante da rispettare |
| Zona alta storica | +25,03% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +22,73% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +18,18% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 1,76 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 59.440 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 68.825 $ | zona obiettivo dopo pullback |
| Spike +10% | 68.825 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 59.440 $ | zona di scarico dopo spike |
| Zona bassa storica | 53.340 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 78.229 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: aspettare, non forzare entrate; long: evitato; short: evitato; zona bassa storica/rischio: 53.340 $; zona alta storica/take profit: 78.229 $

---

## Solana — SOL

Prezzo usato: **80,43 $**

- **Direzione:** NEUTRALE / INCERTO
- **Spot:** ASPETTA / HOLD
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** ALTO

### Perché

- casi positivi sotto la media (+45,00%); zona alta storica abbastanza lontana (+25,17%); rimbalzo dopo discesa debole (+20,83%); dump dopo spike poco frequente (+21,74%); troppi long aperti (3,20)

### Rischi principali

- zona bassa storica profonda (-16,09%); rimbalzo dopo discesa debole (+20,83%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +45,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -0,89% | risultato centrale dei casi storici |
| Zona bassa storica | -16,09% | discesa pesante da rispettare |
| Zona alta storica | +25,17% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +20,83% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +21,74% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 3,20 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 76,41 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 88,47 $ | zona obiettivo dopo pullback |
| Spike +10% | 88,47 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 76,41 $ | zona di scarico dopo spike |
| Zona bassa storica | 67,49 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 100,68 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: aspettare, non forzare entrate; long: evitato; short: evitato; zona bassa storica/rischio: 67,49 $; zona alta storica/take profit: 100,68 $

---

## Dogecoin — DOGE

Prezzo usato: **0,07579 $**

- **Direzione:** BEARISH
- **Spot:** VENDI PARZIALE / STAI FUORI
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** SHORT SOLO DOPO SPIKE
- **Max long:** nessuna
- **Max short:** max 1x-2x isolated
- **Rischio:** MOLTO ALTO

### Perché

- pochi casi storici positivi (+25,00%); rendimento mediano negativo (-16,29%); media 30 giorni negativa (-11,96%); rimbalzo dopo discesa debole (+11,76%); dump dopo spike da monitorare (+64,71%); troppi long aperti (3,84)

### Rischi principali

- zona bassa storica molto profonda (-34,60%); gli spike venivano spesso scaricati (+64,71%); rimbalzo dopo discesa debole (+11,76%)

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +25,00% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -16,29% | risultato centrale dei casi storici |
| Zona bassa storica | -34,60% | discesa pesante da rispettare |
| Zona alta storica | +13,90% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +11,76% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +64,71% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 3,84 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 0,07200 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 0,08337 $ | zona obiettivo dopo pullback |
| Spike +10% | 0,08337 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 0,07200 $ | zona di scarico dopo spike |
| Zona bassa storica | 0,04956 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 0,08632 $ | zona alta; se ci arriva, pensare a profitto |

### Piano sintetico

> spot: ridurre esposizione o stare fuori; long: evitato; short: solo dopo spike verso 0,08337 $, possibile target scarico 0,07200 $; zona bassa storica/rischio: 0,04956 $; zona alta storica/take profit: 0,08632 $

---
