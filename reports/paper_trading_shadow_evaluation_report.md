# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-25T05:08:52+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **18933**
- Valutazioni prodotte: **5367**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TP_R100 | 251 | 0,251 | 0,343 | 0,149 | 67,3% | 95,0 | ELIGIBLE_FOR_MUTATION |
| GB20_R050 | 258 | 0,230 | 0,322 | 0,129 | 67,8% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB20_R100 | 251 | 0,256 | 0,351 | 0,147 | 67,7% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB30_R100 | 251 | 0,221 | 0,322 | 0,112 | 68,9% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB30_R050 | 258 | 0,174 | 0,279 | 0,073 | 66,7% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB40_R100 | 251 | 0,160 | 0,275 | 0,064 | 66,9% | 94,9 | ELIGIBLE_FOR_MUTATION |
| GB50_R100 | 246 | 0,113 | 0,276 | 0,021 | 67,5% | 94,7 | ELIGIBLE_FOR_MUTATION |
| GB50_R050 | 256 | 0,102 | 0,178 | 0,015 | 65,2% | 94,6 | ELIGIBLE_FOR_MUTATION |
| GB40_R050 | 258 | 0,116 | 0,229 | 0,012 | 64,7% | 94,5 | ELIGIBLE_FOR_MUTATION |
| TP_R050 | 258 | 0,082 | 0,268 | -0,012 | 66,7% | 92,0 | VALIDATING |
| TP_R150 | 217 | 0,137 | 0,053 | 0,002 | 52,5% | 82,2 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 655 | 0,092 | 0,000 | 0,031 | 45,8% | 70,0 | VALIDATING |
| TP_R150 | 632 | 0,065 | 0,000 | 0,013 | 28,2% | 69,8 | VALIDATING |
| GB20_R100 | 641 | 0,063 | 0,000 | 0,014 | 37,1% | 69,7 | VALIDATING |
| GB30_R050 | 655 | 0,052 | 0,000 | -0,014 | 44,3% | 67,9 | VALIDATING |
| TP_R200 | 209 | 0,052 | 0,053 | -0,111 | 54,1% | 65,0 | VALIDATING |
| TP_R200 | 622 | 0,051 | 0,000 | -0,014 | 35,2% | 63,8 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| TP_R100 | 641 | 0,031 | 0,000 | -0,022 | 34,9% | 58,0 | VALIDATING |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.
