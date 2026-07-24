# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-24T05:08:42+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **15063**
- Valutazioni prodotte: **4335**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 94 | 0,434 | 0,374 | 0,287 | 87,2% | 97,1 | VALIDATING |
| GB30_R050 | 94 | 0,383 | 0,301 | 0,246 | 87,2% | 97,0 | VALIDATING |
| GB20_R100 | 92 | 0,468 | 0,412 | 0,335 | 85,9% | 96,9 | VALIDATING |
| TP_R100 | 92 | 0,430 | 0,408 | 0,296 | 84,8% | 96,8 | VALIDATING |
| GB40_R100 | 92 | 0,375 | 0,369 | 0,245 | 84,8% | 96,8 | VALIDATING |
| GB30_R100 | 92 | 0,436 | 0,372 | 0,315 | 89,1% | 96,6 | VALIDATING |
| GB50_R100 | 92 | 0,324 | 0,408 | 0,214 | 82,6% | 96,5 | VALIDATING |
| GB40_R050 | 94 | 0,324 | 0,287 | 0,187 | 84,0% | 93,5 | VALIDATING |
| GB50_R050 | 94 | 0,330 | 0,287 | 0,211 | 83,0% | 93,3 | VALIDATING |
| TP_R050 | 94 | 0,247 | 0,290 | 0,105 | 84,0% | 91,3 | VALIDATING |
| BE_R050 | 85 | 0,091 | 0,129 | -0,043 | 61,2% | 77,3 | VALIDATING |
| TIME_6H | 86 | 0,048 | 0,159 | -0,098 | 66,3% | 76,4 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 621 | 0,102 | 0,000 | 0,038 | 45,1% | 70,0 | VALIDATING |
| TP_R200 | 67 | 0,037 | 0,217 | -0,111 | 73,1% | 69,8 | VALIDATING |
| GB20_R100 | 609 | 0,061 | 0,000 | 0,013 | 36,5% | 69,7 | VALIDATING |
| TP_R150 | 599 | 0,058 | 0,000 | 0,009 | 27,4% | 69,7 | VALIDATING |
| GB30_R050 | 621 | 0,061 | 0,000 | -0,003 | 43,5% | 69,5 | VALIDATING |
| ATR15_R100 | 92 | 0,020 | 0,104 | -0,098 | 64,1% | 64,3 | VALIDATING |
| ATR30_R100 | 85 | 0,018 | 0,104 | -0,092 | 60,0% | 63,4 | VALIDATING |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.
