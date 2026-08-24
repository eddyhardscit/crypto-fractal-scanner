# Block 3 — Shadow Exit Engine

Generato: 2026-08-24T05:08:30+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **1063**
- Scenari virtuali ancora attivi: **16090**
- Gruppi in attesa dell'uscita originale: **257**
- Gruppi con originale chiuso ma Shadow ancora attive: **806**
- Confronti completati: **353923**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 8013 | 8086 | +€1,31 | 48,1% | 2045 | 890 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 8010 | 8083 | +€3,93 | 46,8% | 1299 | 1318 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 8006 | 8079 | +€6,45 | 49,7% | 2675 | 15 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 8006 | 8079 | +€5,86 | 49,5% | 2617 | 76 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 8006 | 8079 | +€2,74 | 46,9% | 2912 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 7999 | 8072 | +€5,28 | 48,7% | 2581 | 173 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 7996 | 8069 | +€4,51 | 42,7% | 2476 | 106 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 7994 | 8067 | +€7,81 | 46,2% | 2163 | 124 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 7994 | 8067 | +€6,91 | 46,5% | 2028 | 239 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 7987 | 8060 | +€4,39 | 43,2% | 1197 | 1175 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 7975 | 8048 | +€5,77 | 42,1% | 758 | 1838 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 7971 | 8044 | +€7,21 | 46,4% | 1818 | 424 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 7968 | 8041 | +€5,67 | 36,3% | 1622 | 568 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 7967 | 8040 | +€4,31 | 40,9% | 981 | 1555 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 7950 | 8023 | +€4,69 | 48,4% | 2449 | 291 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 7930 | 8003 | +€3,17 | 38,8% | 815 | 1806 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 7913 | 7986 | +€6,97 | 41,8% | 798 | 898 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 7885 | 7958 | +€5,70 | 44,9% | 1587 | 739 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 7516 | 7589 | €-3,50 | 36,3% | 1613 | 1390 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 7350 | 7423 | €-5,72 | 30,2% | 773 | 2097 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
