# Block 3 — Shadow Exit Engine

Generato: 2026-08-18T05:06:06+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **629**
- Scenari virtuali ancora attivi: **10201**
- Gruppi in attesa dell'uscita originale: **252**
- Gruppi con originale chiuso ma Shadow ancora attive: **377**
- Confronti completati: **244280**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 5743 | 5816 | +€0,08 | 47,7% | 1280 | 711 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 5742 | 5811 | +€8,12 | 51,8% | 1626 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5742 | 5811 | +€7,26 | 51,2% | 1609 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5742 | 5811 | +€5,97 | 49,6% | 1624 | 128 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5742 | 5811 | +€4,88 | 49,2% | 1783 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5742 | 5811 | +€4,60 | 49,7% | 1545 | 193 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 5735 | 5808 | +€0,03 | 43,0% | 814 | 1046 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5725 | 5794 | +€7,27 | 45,0% | 1315 | 111 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5725 | 5794 | +€6,08 | 45,0% | 1250 | 177 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5725 | 5794 | +€5,41 | 43,1% | 1437 | 98 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5722 | 5791 | +€5,05 | 44,3% | 1134 | 305 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5721 | 5790 | +€2,18 | 38,4% | 740 | 930 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 5721 | 5790 | +€1,40 | 36,0% | 600 | 1195 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5717 | 5786 | +€3,21 | 42,7% | 1015 | 529 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 5700 | 5773 | €-4,27 | 35,0% | 507 | 1464 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5656 | 5725 | €-2,52 | 33,3% | 502 | 1375 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 5644 | 5713 | +€4,77 | 34,9% | 876 | 507 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5621 | 5687 | +€4,87 | 38,8% | 472 | 795 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5613 | 5682 | €-3,25 | 36,4% | 1023 | 1048 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 5497 | 5566 | €-7,00 | 28,3% | 466 | 1555 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
