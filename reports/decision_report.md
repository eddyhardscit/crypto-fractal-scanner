# Decisione operativa sintetica

Generato: **2026-07-09 03:16:02 CEST**  
UTC: **2026-07-09 01:16:02 UTC**

Questo report prende tutti i dati dello scanner e li trasforma in una lettura pratica.

Scopo:

- capire se conviene spot, long, short o aspettare;
- separare long e short, invece di mettere tutto dentro una sola voce;
- usare parole semplici per zone alte, zone basse e rischio leva;
- leggere anche Global Confluence e Lifecycle EMA200, così il report decisionale non resta scollegato dalla sintesi principale.

## Dashboard veloce

| Asset | Prezzo | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.394 $ | LEGGERMENTE BULLISH | ACCUMULA SOLO SU PULLBACK | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | BASSO |
| SOL | 78,39 $ | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0,07268 $ | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

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

Prezzo usato: **62.394 $**

- **Direzione:** LEGGERMENTE BULLISH
- **Spot:** ACCUMULA SOLO SU PULLBACK
- **Long a leva:** LONG PRUDENTE
- **Short a leva:** NO SHORT
- **Max long:** max 2x isolated
- **Max short:** nessuna
- **Rischio:** BASSO

### Perché

- casi positivi sopra la media (+65,00%); rendimento mediano positivo (+3,39%); zona alta storica abbastanza lontana (+28,81%); Global Confluence moderatamente positivo (+3); troppi long aperti (1,84)

### Rischi principali

- zona bassa storica moderata (-9,52%)

### Lettura Global Confluence

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Global score | +3 | MODERATAMENTE POSITIVA |
| Bias globale | Costruttivo prudente | lettura finale del report di confluenza |
| Azione globale | ACCUMULA SU PULLBACK / NO SHORT | azione coerente nel Global Confluence |
| Lifecycle EMA | 0 | nan |
| EMA200 weekly | n/d | target tecnico naturale del modulo squeeze |
| Upside EMA200 | n/d | spazio teorico verso EMA200 |

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
| Long/Short ratio | 1,84 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 59.275 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 68.634 $ | zona obiettivo dopo pullback |
| Spike +10% | 68.634 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 59.275 $ | zona di scarico dopo spike |
| Zona bassa storica | 56.455 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 80.367 $ | zona alta; se ci arriva, pensare a profitto |
| EMA200 weekly SOL | n/d | target tecnico del modulo lifecycle squeeze, solo se applicabile |

### Conferme e invalidazioni

- Conferme: Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### Piano sintetico

> spot: valutare accumulo solo verso 59.275 $; long: long prudente, max 2x isolated; short: evitato; zona bassa storica/rischio: 56.455 $; zona alta storica/take profit: 80.367 $

---

## Solana — SOL

Prezzo usato: **78,39 $**

- **Direzione:** NEUTRALE / COSTRUTTIVO
- **Spot:** HOLD / TRANCHE PICCOLE, NO LEVA
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** NO SHORT
- **Max long:** nessuna
- **Max short:** nessuna
- **Rischio:** MOLTO ALTO

### Perché

- casi positivi sotto la media (+42,50%); rimbalzo dopo discesa debole (+10,71%); dump dopo spike poco frequente (+20,00%); Global Confluence costruttivo (+6); Lifecycle EMA200 positivo: possibile squeeze verso EMA200 (+1); troppi long aperti (2,71)

### Rischi principali

- zona bassa storica molto profonda (-23,93%); rimbalzo dopo discesa debole (+10,71%)

### Lettura Global Confluence

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Global score | +6 | MODERATAMENTE POSITIVA |
| Bias globale | Costruttivo prudente | lettura finale del report di confluenza |
| Azione globale | HOLD / TRANCHE PICCOLE, NO LEVA | azione coerente nel Global Confluence |
| Lifecycle EMA | +1 | SQUEEZE SETUP FORTE |
| EMA200 weekly | 113,51 $ | target tecnico naturale del modulo squeeze |
| Upside EMA200 | +44,96% | spazio teorico verso EMA200 |

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +42,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -2,37% | risultato centrale dei casi storici |
| Zona bassa storica | -23,93% | discesa pesante da rispettare |
| Zona alta storica | +16,63% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +10,71% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +20,00% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 2,71 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 74,47 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 86,23 $ | zona obiettivo dopo pullback |
| Spike +10% | 86,23 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 74,47 $ | zona di scarico dopo spike |
| Zona bassa storica | 59,63 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 91,43 $ | zona alta; se ci arriva, pensare a profitto |
| EMA200 weekly SOL | 113,51 $ | target tecnico del modulo lifecycle squeeze, solo se applicabile |

### Conferme e invalidazioni

- Conferme: Conferme sopra 83,81 / 106,19 / 115,76.
- Invalidazioni: Allarmi sotto 74,39 / 64,42 / 62,19.

### Piano sintetico

> spot: hold o tranche piccole, senza inseguire e senza leva; long: evitato; short: evitato; EMA200 weekly / target squeeze: 113,51 $; zona bassa storica/rischio: 59,63 $; zona alta storica/take profit: 91,43 $

---

## Dogecoin — DOGE

Prezzo usato: **0,07268 $**

- **Direzione:** BEARISH
- **Spot:** VENDI PARZIALE / STAI FUORI
- **Long a leva:** NO LONG A LEVA
- **Short a leva:** SHORT SOLO DOPO SPIKE
- **Max long:** nessuna
- **Max short:** max 1x-2x isolated
- **Rischio:** MOLTO ALTO

### Perché

- pochi casi storici positivi (+17,50%); rendimento mediano negativo (-18,45%); media 30 giorni negativa (-14,09%); rimbalzo dopo discesa debole (+16,22%); dump dopo spike da monitorare (+64,29%); Global Confluence molto negativo (-9); troppi long aperti (3,27)

### Rischi principali

- zona bassa storica molto profonda (-34,84%); gli spike venivano spesso scaricati (+64,29%); rimbalzo dopo discesa debole (+16,22%)

### Lettura Global Confluence

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Global score | -9 | NEGATIVA |
| Bias globale | Ribassista | lettura finale del report di confluenza |
| Azione globale | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | azione coerente nel Global Confluence |
| Lifecycle EMA | 0 | nan |
| EMA200 weekly | n/d | target tecnico naturale del modulo squeeze |
| Upside EMA200 | n/d | spazio teorico verso EMA200 |

### Numeri semplici

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Casi positivi 30 giorni | +17,50% | quante volte i casi simili chiudevano verdi dopo 30 giorni |
| Rendimento mediano | -18,45% | risultato centrale dei casi storici |
| Zona bassa storica | -34,84% | discesa pesante da rispettare |
| Zona alta storica | +12,87% | zona alta dove non inseguire troppo |
| Rimbalzo dopo -5% → +10% | +16,22% | se scende prima, quante volte poi rimbalza forte |
| Dump dopo +10% → -5% | +64,29% | se fa spike prima, quante volte poi scarica |
| Funding | +0,00% | se è alto positivo, troppi long possono essere un rischio |
| Long/Short ratio | 3,27 | se è alto, ci sono molti long aperti |

### Aree operative

| Area | Prezzo | Uso pratico |
| --- | --- | --- |
| Pullback -5% | 0,06905 $ | zona dove valutare accumulo, non comprare a caso |
| Target rimbalzo +10% | 0,07995 $ | zona obiettivo dopo pullback |
| Spike +10% | 0,07995 $ | zona dove non inseguire; possibile take profit o short solo se il quadro è bearish |
| Dump -5% | 0,06905 $ | zona di scarico dopo spike |
| Zona bassa storica | 0,04736 $ | zona rischio; con leva bisogna rispettarla |
| Zona alta storica | 0,08204 $ | zona alta; se ci arriva, pensare a profitto |
| EMA200 weekly SOL | n/d | target tecnico del modulo lifecycle squeeze, solo se applicabile |

### Conferme e invalidazioni

- Conferme: Sopra 0.07923 migliora, ma resta asset debole finché scanner e struttura non girano.
- Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.

### Piano sintetico

> spot: ridurre esposizione o stare fuori; long: evitato; short: solo dopo spike verso 0,07995 $, possibile target scarico 0,06905 $; zona bassa storica/rischio: 0,04736 $; zona alta storica/take profit: 0,08204 $

---
