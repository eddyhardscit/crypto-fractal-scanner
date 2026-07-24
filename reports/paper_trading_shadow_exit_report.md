# Block 3 — Shadow Exit Engine

Generato: 2026-07-24T05:08:40+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **368**
- Scenari virtuali ancora attivi: **3339**
- Gruppi in attesa dell'uscita originale: **184**
- Gruppi con originale chiuso ma Shadow ancora attive: **184**
- Confronti completati: **15063**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 721 | 784 | +€6,25 | 49,6% | 200 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 721 | 784 | +€4,14 | 48,3% | 205 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 721 | 784 | +€1,88 | 46,9% | 211 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 721 | 784 | +€0,94 | 47,1% | 223 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 718 | 781 | +€0,59 | 45,2% | 206 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 716 | 779 | €-0,64 | 50,6% | 165 | 105 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 707 | 770 | +€5,03 | 42,5% | 169 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 707 | 770 | +€3,09 | 42,3% | 158 | 34 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 707 | 770 | +€2,91 | 40,5% | 184 | 22 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 707 | 770 | +€1,94 | 41,9% | 135 | 58 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 704 | 767 | +€1,62 | 38,6% | 99 | 115 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 703 | 766 | €-1,49 | 33,4% | 61 | 171 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 696 | 759 | +€0,53 | 44,4% | 84 | 165 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 678 | 741 | +€1,61 | 30,9% | 78 | 84 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 678 | 741 | €-4,32 | 29,7% | 44 | 196 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 656 | 719 | €-10,45 | 27,8% | 125 | 128 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 653 | 716 | €-9,26 | 25,6% | 40 | 198 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 646 | 709 | +€0,44 | 36,1% | 36 | 125 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 638 | 701 | €-5,45 | 32,8% | 46 | 194 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 605 | 668 | €-16,63 | 20,1% | 39 | 196 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
