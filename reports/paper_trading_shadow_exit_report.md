# Block 3 — Shadow Exit Engine

Generato: 2026-08-10T05:09:11+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **4**
- Scenari virtuali ancora attivi: **0**
- Gruppi in attesa dell'uscita originale: **4**
- Gruppi con originale chiuso ma Shadow ancora attive: **0**
- Confronti completati: **124215**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3296 | 3362 | +€9,08 | 51,5% | 925 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3296 | 3362 | +€7,45 | 50,5% | 925 | 35 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3296 | 3362 | +€6,68 | 43,1% | 711 | 93 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3296 | 3362 | +€6,23 | 48,9% | 926 | 83 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3296 | 3362 | +€5,09 | 33,2% | 412 | 386 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3296 | 3362 | +€4,87 | 48,5% | 1028 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3296 | 3362 | +€4,84 | 42,7% | 687 | 131 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3296 | 3362 | +€4,62 | 48,9% | 868 | 143 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3296 | 3362 | +€4,53 | 41,1% | 779 | 91 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3296 | 3362 | +€4,19 | 41,7% | 604 | 220 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3296 | 3362 | +€3,81 | 35,7% | 199 | 627 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3296 | 3362 | +€2,32 | 39,9% | 520 | 380 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3296 | 3362 | €-0,27 | 31,4% | 369 | 702 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3296 | 3362 | €-0,95 | 28,7% | 312 | 840 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3296 | 3362 | €-0,98 | 39,6% | 402 | 740 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3296 | 3362 | €-1,37 | 45,4% | 673 | 502 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3296 | 3362 | €-3,67 | 32,8% | 557 | 718 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3296 | 3362 | €-4,42 | 31,8% | 189 | 1009 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3296 | 3362 | €-5,24 | 27,2% | 261 | 918 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3296 | 3362 | €-8,52 | 22,6% | 261 | 1051 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
