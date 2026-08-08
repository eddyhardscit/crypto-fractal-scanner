# Block 3 — Shadow Exit Engine

Generato: 2026-08-08T05:09:03+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **11**
- Scenari virtuali ancora attivi: **150**
- Gruppi in attesa dell'uscita originale: **11**
- Gruppi con originale chiuso ma Shadow ancora attive: **0**
- Confronti completati: **123147**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3274 | 3340 | +€9,07 | 51,6% | 923 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3274 | 3340 | +€7,43 | 50,7% | 923 | 30 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3274 | 3340 | +€6,64 | 43,1% | 711 | 88 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3274 | 3340 | +€6,20 | 49,1% | 923 | 78 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3274 | 3340 | +€5,08 | 33,1% | 412 | 381 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3274 | 3340 | +€4,83 | 48,6% | 1026 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3274 | 3340 | +€4,80 | 42,7% | 687 | 126 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3274 | 3340 | +€4,58 | 49,0% | 865 | 138 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3274 | 3340 | +€4,48 | 41,1% | 779 | 86 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3274 | 3340 | +€4,15 | 41,7% | 602 | 215 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3274 | 3340 | +€3,78 | 35,7% | 199 | 622 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3274 | 3340 | +€2,27 | 39,9% | 520 | 375 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3274 | 3340 | €-0,32 | 31,5% | 369 | 694 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3274 | 3340 | €-1,01 | 28,7% | 312 | 833 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3274 | 3340 | €-1,05 | 39,6% | 401 | 735 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3274 | 3340 | €-1,43 | 45,5% | 671 | 496 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3274 | 3340 | €-3,74 | 32,9% | 554 | 713 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3274 | 3340 | €-4,49 | 31,9% | 188 | 1001 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3274 | 3340 | €-5,32 | 27,3% | 261 | 910 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3274 | 3340 | €-8,62 | 22,6% | 261 | 1043 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
