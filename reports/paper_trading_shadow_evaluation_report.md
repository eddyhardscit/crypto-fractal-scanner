# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-21T05:08:39+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **2473**
- Valutazioni prodotte: **2152**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB30_R050 | 87 | 0,268 | 0,000 | 0,105 | 46,0% | 67,8 | VALIDATING |
| GB40_R050 | 87 | 0,226 | 0,000 | 0,070 | 46,0% | 67,8 | VALIDATING |
| GB50_R050 | 87 | 0,227 | 0,000 | 0,075 | 46,0% | 67,7 | VALIDATING |
| GB20_R050 | 87 | 0,304 | 0,000 | 0,145 | 47,1% | 67,4 | VALIDATING |
| TP_R050 | 87 | 0,217 | 0,000 | 0,028 | 47,1% | 67,3 | VALIDATING |
| GB20_R100 | 86 | 0,159 | 0,000 | 0,037 | 40,7% | 67,1 | VALIDATING |
| TP_R100 | 86 | 0,130 | 0,000 | -0,002 | 40,7% | 66,7 | VALIDATING |
| TIME_12H | 87 | 0,163 | 0,000 | 0,029 | 42,5% | 66,5 | VALIDATING |
| TIME_6H | 87 | 0,077 | 0,000 | -0,017 | 49,4% | 64,1 | VALIDATING |
| GB30_R100 | 84 | 0,093 | 0,000 | -0,027 | 39,3% | 62,5 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| BE_R050 | 80 | 0,098 | 0,000 | -0,045 | 36,2% | 55,6 | VALIDATING |
| GB50_R100 | 83 | 0,040 | 0,000 | -0,061 | 37,3% | 55,0 | VALIDATING |
| TP_R200 | 74 | 0,095 | 0,000 | -0,029 | 31,1% | 54,9 | VALIDATING |
| GB40_R100 | 83 | 0,038 | 0,000 | -0,072 | 38,6% | 53,0 | VALIDATING |
| TP_R150 | 78 | 0,038 | 0,000 | -0,089 | 28,2% | 44,9 | VALIDATING |
| TIME_24H | 65 | 0,017 | 0,000 | -0,152 | 27,7% | 34,0 | VALIDATING |
| TP_R150 | 6 | 0,056 | 0,000 | -0,433 | 16,7% | 28,7 | INSUFFICIENT_DATA |
| ATR20_R100 | 68 | -0,032 | 0,000 | -0,111 | 32,4% | 26,3 | VALIDATING |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.
