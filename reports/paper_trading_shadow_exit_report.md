# Block 3 — Shadow Exit Engine

Generato: 2026-08-22T05:07:56+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **1436**
- Scenari virtuali ancora attivi: **23822**
- Gruppi in attesa dell'uscita originale: **268**
- Gruppi con originale chiuso ma Shadow ancora attive: **1168**
- Confronti completati: **325794**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 7554 | 7627 | +€6,10 | 49,2% | 2595 | 15 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 7554 | 7627 | +€2,22 | 46,3% | 2821 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 7551 | 7624 | +€5,63 | 49,1% | 2535 | 74 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 7544 | 7617 | +€3,98 | 41,5% | 2427 | 106 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 7541 | 7614 | +€5,25 | 35,2% | 1586 | 568 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 7539 | 7612 | +€7,40 | 45,2% | 2123 | 124 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 7525 | 7598 | +€6,81 | 45,8% | 1976 | 224 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 7523 | 7596 | +€6,82 | 41,2% | 755 | 896 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 7511 | 7584 | +€1,59 | 48,2% | 1920 | 855 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 7503 | 7576 | +€4,44 | 48,2% | 2482 | 163 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 7397 | 7470 | +€5,55 | 45,6% | 1739 | 380 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 7387 | 7460 | +€5,16 | 47,5% | 1153 | 1197 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 7363 | 7436 | +€3,45 | 48,2% | 2321 | 247 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 7356 | 7429 | +€5,30 | 43,4% | 1073 | 1057 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 7338 | 7411 | +€5,44 | 41,4% | 861 | 1394 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 7174 | 7247 | +€3,83 | 44,0% | 1481 | 641 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 7163 | 7236 | +€2,97 | 38,4% | 675 | 1636 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 7120 | 7193 | +€5,00 | 41,1% | 646 | 1653 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 6887 | 6960 | €-3,47 | 36,9% | 1458 | 1218 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 6629 | 6702 | €-6,71 | 30,4% | 633 | 1843 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
