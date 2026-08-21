# Block 3 — Shadow Exit Engine

Generato: 2026-08-21T05:05:56+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **913**
- Scenari virtuali ancora attivi: **15266**
- Gruppi in attesa dell'uscita originale: **321**
- Gruppi con originale chiuso ma Shadow ancora attive: **592**
- Confronti completati: **294496**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 6801 | 6874 | +€3,27 | 49,7% | 1543 | 791 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 6792 | 6865 | +€9,84 | 52,6% | 1999 | 15 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 6792 | 6865 | +€9,22 | 52,3% | 1955 | 68 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 6792 | 6865 | +€5,68 | 49,6% | 2212 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 6784 | 6857 | +€6,37 | 43,9% | 1848 | 106 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 6782 | 6855 | +€9,78 | 47,0% | 1616 | 121 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 6782 | 6855 | +€9,00 | 47,5% | 1502 | 202 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 6777 | 6850 | +€5,05 | 46,8% | 974 | 1130 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 6769 | 6842 | +€6,36 | 36,6% | 1180 | 568 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 6765 | 6838 | +€7,82 | 51,2% | 1931 | 149 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 6747 | 6820 | +€5,59 | 42,8% | 865 | 995 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 6726 | 6799 | +€5,16 | 40,7% | 677 | 1301 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 6711 | 6784 | +€6,30 | 40,5% | 590 | 894 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 6695 | 6768 | +€7,40 | 46,9% | 1333 | 337 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 6695 | 6768 | +€6,46 | 51,1% | 1820 | 227 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 6666 | 6739 | +€4,01 | 39,4% | 569 | 1610 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 6660 | 6733 | +€1,62 | 37,4% | 574 | 1524 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 6613 | 6686 | +€5,36 | 45,3% | 1160 | 587 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 6492 | 6565 | €-1,55 | 38,1% | 1183 | 1197 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 6385 | 6458 | €-6,05 | 30,5% | 543 | 1791 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
