# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-22T05:08:41+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **6484**
- Valutazioni prodotte: **3139**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 291 | 0,217 | 0,043 | 0,117 | 51,5% | 81,5 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| TP_R200 | 232 | 0,141 | 0,000 | 0,056 | 39,7% | 72,6 | VALIDATING |
| GB30_R050 | 291 | 0,177 | 0,000 | 0,084 | 49,5% | 69,9 | VALIDATING |
| TP_R050 | 291 | 0,128 | 0,000 | 0,028 | 48,5% | 69,9 | VALIDATING |
| GB40_R050 | 291 | 0,136 | 0,000 | 0,051 | 49,1% | 69,8 | VALIDATING |
| GB50_R050 | 291 | 0,093 | 0,000 | 0,008 | 48,1% | 69,7 | VALIDATING |
| GB20_R100 | 278 | 0,100 | 0,000 | 0,030 | 42,4% | 69,5 | VALIDATING |
| TP_R150 | 250 | 0,050 | 0,000 | -0,019 | 32,8% | 62,1 | VALIDATING |
| GB30_R100 | 278 | 0,066 | 0,000 | 0,002 | 39,6% | 61,9 | VALIDATING |
| TP_R100 | 278 | 0,068 | 0,000 | -0,005 | 39,6% | 61,1 | VALIDATING |
| TIME_12H | 275 | 0,034 | 0,000 | -0,032 | 41,1% | 60,4 | VALIDATING |
| TP_R200 | 6 | 0,472 | 0,250 | -0,017 | 50,0% | 58,7 | INSUFFICIENT_DATA |
| GB50_R100 | 273 | 0,027 | 0,000 | -0,031 | 37,0% | 54,8 | VALIDATING |
| GB40_R100 | 278 | 0,028 | 0,000 | -0,040 | 40,3% | 50,3 | VALIDATING |
| BE_R050 | 251 | -0,050 | 0,000 | -0,150 | 33,5% | 35,5 | VALIDATING |
| TIME_6H | 291 | -0,051 | 0,000 | -0,135 | 48,8% | 35,4 | VALIDATING |
| BE_R100 | 218 | -0,151 | 0,000 | -0,248 | 27,5% | 33,9 | UNDERPERFORMING |
| ATR20_R100 | 266 | -0,155 | 0,000 | -0,221 | 24,4% | 31,7 | UNDERPERFORMING |
| ATR15_R100 | 275 | -0,075 | 0,000 | -0,123 | 28,0% | 31,2 | UNDERPERFORMING |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.
