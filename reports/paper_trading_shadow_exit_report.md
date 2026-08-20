# Block 3 — Shadow Exit Engine

Generato: 2026-08-20T05:05:55+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **678**
- Scenari virtuali ancora attivi: **13353**
- Gruppi in attesa dell'uscita originale: **224**
- Gruppi con originale chiuso ma Shadow ancora attive: **454**
- Confronti completati: **279692**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 6493 | 6566 | +€3,44 | 49,9% | 1445 | 747 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 6473 | 6542 | +€9,96 | 53,0% | 1856 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 6473 | 6542 | +€9,38 | 52,8% | 1813 | 60 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 6473 | 6542 | +€5,83 | 50,0% | 2057 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 6467 | 6536 | +€6,37 | 44,2% | 1698 | 106 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 6466 | 6535 | +€9,66 | 47,0% | 1501 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 6466 | 6535 | +€8,92 | 47,6% | 1394 | 189 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 6463 | 6532 | +€5,29 | 42,5% | 812 | 967 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 6454 | 6523 | +€4,78 | 40,3% | 646 | 1258 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 6447 | 6516 | +€7,93 | 51,4% | 1806 | 139 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 6442 | 6511 | +€5,70 | 36,5% | 1093 | 568 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 6438 | 6511 | +€4,03 | 45,6% | 937 | 1099 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 6422 | 6491 | +€1,25 | 36,9% | 556 | 1488 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 6413 | 6482 | +€5,43 | 39,9% | 553 | 891 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 6391 | 6460 | +€7,29 | 46,9% | 1238 | 325 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 6384 | 6453 | +€6,53 | 51,4% | 1695 | 213 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 6314 | 6383 | +€5,07 | 45,1% | 1089 | 562 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 6310 | 6383 | €-2,19 | 37,7% | 551 | 1558 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 6244 | 6313 | €-1,68 | 38,0% | 1121 | 1155 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 6144 | 6213 | €-6,05 | 30,3% | 525 | 1711 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
