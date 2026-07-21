# Block 3 — Shadow Exit Engine

Generato: 2026-07-21T05:08:39+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **169**
- Scenari virtuali ancora attivi: **2259**
- Gruppi in attesa dell'uscita originale: **128**
- Gruppi con originale chiuso ma Shadow ancora attive: **41**
- Confronti completati: **2473**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 93 | 130 | +€11,63 | 47,7% | 25 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 93 | 130 | +€9,32 | 46,9% | 25 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 93 | 130 | +€6,97 | 45,4% | 26 | 2 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 93 | 130 | +€6,13 | 47,7% | 25 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 93 | 130 | +€5,95 | 44,6% | 22 | 7 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 93 | 137 | +€4,65 | 40,1% | 18 | 16 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 93 | 137 | €-0,97 | 41,6% | 26 | 11 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 92 | 129 | +€8,97 | 42,6% | 23 | 2 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 92 | 129 | +€6,57 | 43,4% | 22 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 90 | 127 | +€5,30 | 40,9% | 23 | 3 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 89 | 126 | +€2,07 | 40,5% | 20 | 5 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 89 | 126 | +€0,67 | 38,1% | 13 | 16 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 87 | 124 | €-7,16 | 33,1% | 7 | 24 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 85 | 122 | €-3,89 | 27,9% | 26 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 84 | 121 | +€2,35 | 29,8% | 15 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 80 | 116 | +€7,14 | 32,8% | 9 | 14 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 72 | 106 | €-4,79 | 32,1% | 4 | 15 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 71 | 115 | +€2,70 | 33,0% | 11 | 17 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 71 | 104 | €-6,72 | 25,0% | 3 | 21 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 71 | 104 | €-7,11 | 25,0% | 2 | 22 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
