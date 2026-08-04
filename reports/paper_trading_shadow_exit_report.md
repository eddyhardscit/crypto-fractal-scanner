# Block 3 — Shadow Exit Engine

Generato: 2026-08-04T05:09:11+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **30**
- Scenari virtuali ancora attivi: **146**
- Gruppi in attesa dell'uscita originale: **13**
- Gruppi con originale chiuso ma Shadow ancora attive: **17**
- Confronti completati: **121185**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3236 | 3302 | +€9,16 | 51,8% | 912 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3236 | 3302 | +€7,50 | 50,9% | 912 | 30 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3236 | 3302 | +€6,70 | 43,3% | 706 | 88 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3236 | 3302 | +€6,26 | 49,3% | 911 | 78 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3236 | 3302 | +€5,10 | 33,2% | 411 | 381 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3236 | 3302 | +€4,87 | 48,8% | 1015 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3236 | 3302 | +€4,84 | 42,8% | 682 | 126 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3236 | 3302 | +€4,63 | 49,2% | 854 | 138 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3236 | 3302 | +€4,50 | 41,2% | 774 | 86 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3236 | 3302 | +€4,18 | 41,9% | 597 | 215 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3236 | 3302 | +€2,29 | 40,1% | 515 | 371 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3236 | 3302 | €-0,33 | 31,5% | 368 | 690 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3236 | 3302 | €-1,02 | 29,0% | 311 | 822 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3236 | 3302 | €-1,09 | 39,7% | 400 | 732 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3236 | 3302 | €-1,45 | 45,9% | 669 | 488 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3234 | 3300 | +€3,83 | 35,7% | 198 | 620 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3230 | 3296 | €-5,76 | 27,2% | 260 | 905 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3227 | 3293 | €-4,15 | 33,1% | 547 | 702 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3227 | 3293 | €-4,57 | 31,9% | 187 | 992 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3227 | 3293 | €-9,12 | 22,6% | 260 | 1032 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
