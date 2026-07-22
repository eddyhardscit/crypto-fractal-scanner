# Block 3 — Shadow Exit Engine

Generato: 2026-07-22T05:08:40+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **271**
- Scenari virtuali ancora attivi: **2951**
- Gruppi in attesa dell'uscita originale: **162**
- Gruppi con originale chiuso ma Shadow ancora attive: **109**
- Confronti completati: **6484**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 297 | 347 | +€6,85 | 49,3% | 82 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 297 | 347 | +€4,84 | 47,6% | 81 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 297 | 347 | +€2,92 | 46,7% | 82 | 9 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 297 | 347 | +€2,53 | 46,7% | 91 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 297 | 347 | +€0,81 | 45,5% | 77 | 18 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 297 | 352 | €-4,62 | 44,9% | 72 | 48 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 284 | 334 | +€2,52 | 41,3% | 66 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 284 | 334 | +€0,67 | 39,2% | 73 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 284 | 334 | +€0,63 | 38,6% | 66 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 284 | 334 | €-1,32 | 39,2% | 51 | 33 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 281 | 336 | +€0,24 | 39,6% | 34 | 60 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 281 | 331 | €-6,74 | 27,8% | 26 | 86 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 279 | 329 | €-1,83 | 35,9% | 27 | 66 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 272 | 322 | €-9,70 | 24,8% | 21 | 93 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 257 | 307 | €-7,55 | 29,0% | 61 | 31 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 256 | 306 | €-1,10 | 31,4% | 32 | 30 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 238 | 288 | +€2,77 | 37,2% | 15 | 33 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 235 | 285 | €-14,96 | 22,8% | 18 | 73 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 229 | 284 | €-3,76 | 32,4% | 17 | 61 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 224 | 273 | €-13,50 | 23,4% | 17 | 63 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
