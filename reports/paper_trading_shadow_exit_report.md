# Block 3 — Shadow Exit Engine

Generato: 2026-08-07T05:09:05+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **15**
- Scenari virtuali ancora attivi: **108**
- Gruppi in attesa dell'uscita originale: **9**
- Gruppi con originale chiuso ma Shadow ancora attive: **6**
- Confronti completati: **122839**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3270 | 3336 | +€9,08 | 51,6% | 922 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3270 | 3336 | +€7,44 | 50,7% | 922 | 30 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3270 | 3336 | +€6,65 | 43,2% | 710 | 88 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3270 | 3336 | +€6,21 | 49,1% | 922 | 78 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3270 | 3336 | +€4,84 | 48,6% | 1025 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3270 | 3336 | +€4,81 | 42,7% | 686 | 126 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3270 | 3336 | +€4,59 | 49,1% | 864 | 138 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3270 | 3336 | +€4,49 | 41,2% | 778 | 86 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3270 | 3336 | +€4,15 | 41,8% | 601 | 215 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3270 | 3336 | €-1,05 | 39,7% | 400 | 735 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3270 | 3336 | €-1,43 | 45,6% | 670 | 496 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3270 | 3336 | €-3,74 | 32,9% | 553 | 713 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3264 | 3330 | +€5,07 | 33,1% | 411 | 381 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3264 | 3330 | +€3,79 | 35,6% | 198 | 622 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3264 | 3330 | +€2,28 | 40,0% | 519 | 371 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3264 | 3330 | €-0,33 | 31,4% | 368 | 694 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3264 | 3330 | €-1,01 | 28,8% | 311 | 827 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3264 | 3330 | €-4,51 | 31,8% | 187 | 1001 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3264 | 3330 | €-5,35 | 27,2% | 260 | 910 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3264 | 3330 | €-8,66 | 22,5% | 260 | 1043 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
