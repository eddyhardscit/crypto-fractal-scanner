# Block 3 — Shadow Exit Engine

Generato: 2026-08-19T05:05:56+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **651**
- Scenari virtuali ancora attivi: **13640**
- Gruppi in attesa dell'uscita originale: **335**
- Gruppi con originale chiuso ma Shadow ancora attive: **316**
- Confronti completati: **253445**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_12H | 5920 | 5993 | +€1,06 | 43,7% | 845 | 1061 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 5920 | 5993 | +€0,96 | 48,2% | 1328 | 711 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 5906 | 5975 | +€9,05 | 52,4% | 1664 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5906 | 5975 | +€8,16 | 51,8% | 1647 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5906 | 5975 | +€6,91 | 50,3% | 1657 | 129 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5906 | 5975 | +€5,68 | 49,8% | 1821 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5900 | 5969 | +€8,03 | 45,5% | 1351 | 111 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5900 | 5969 | +€6,82 | 45,5% | 1286 | 177 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5900 | 5969 | +€6,22 | 43,8% | 1470 | 98 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5898 | 5967 | +€5,81 | 44,9% | 1166 | 307 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5896 | 5965 | +€2,74 | 39,1% | 762 | 946 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5895 | 5964 | +€5,54 | 50,5% | 1572 | 193 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 5890 | 5963 | €-3,49 | 35,7% | 514 | 1502 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5882 | 5951 | +€3,98 | 43,3% | 1040 | 530 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 5881 | 5950 | +€1,92 | 36,7% | 620 | 1210 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 5864 | 5933 | +€5,27 | 35,7% | 899 | 533 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5844 | 5910 | +€4,96 | 39,2% | 483 | 842 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5826 | 5895 | €-1,88 | 33,8% | 528 | 1401 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5797 | 5866 | €-2,52 | 36,9% | 1049 | 1087 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 5708 | 5777 | €-6,48 | 28,8% | 492 | 1612 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
