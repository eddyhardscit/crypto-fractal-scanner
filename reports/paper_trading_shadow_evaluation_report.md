# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-26T05:08:49+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **28648**
- Valutazioni prodotte: **10767**
- Candidature al Blocco 5: **1**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R100 | 116 | 0,292 | 0,298 | 0,153 | 60,3% | 90,2 | VALIDATING |
| GB40_R100 | 89 | 0,228 | 0,095 | 0,076 | 59,6% | 87,3 | VALIDATING |
| GB20_R075 | 116 | 0,235 | 0,057 | 0,098 | 55,2% | 84,9 | VALIDATING |
| GB50_R100 | 78 | 0,238 | 0,168 | 0,088 | 59,0% | 84,4 | VALIDATING |
| GB50_R075 | 78 | 0,233 | 0,189 | 0,083 | 59,0% | 84,2 | VALIDATING |
| BE_R075 | 57 | 0,140 | 0,286 | -0,008 | 70,2% | 83,8 | VALIDATING |
| BE_A075 | 57 | 0,140 | 0,286 | -0,008 | 70,2% | 83,7 | VALIDATING |
| GB30_R100 | 116 | 0,183 | 0,169 | 0,041 | 56,0% | 82,0 | VALIDATING |
| BE_A060 | 57 | 0,140 | 0,286 | -0,020 | 70,2% | 81,9 | VALIDATING |
| TP_R250 | 84 | 0,231 | 0,199 | 0,060 | 54,8% | 80,6 | VALIDATING |
| ATR15_R100 | 63 | 0,095 | 0,252 | -0,035 | 63,5% | 79,9 | VALIDATING |
| ATR20_R100 | 57 | 0,105 | 0,286 | -0,043 | 70,2% | 79,1 | VALIDATING |
| BE_R100 | 57 | 0,105 | 0,286 | -0,050 | 70,2% | 78,0 | VALIDATING |
| ATR30_R100 | 57 | 0,105 | 0,286 | -0,053 | 70,2% | 77,7 | VALIDATING |
| BE_A100 | 57 | 0,105 | 0,286 | -0,055 | 70,2% | 77,2 | VALIDATING |
| TP_R300 | 75 | 0,381 | 0,063 | 0,153 | 52,0% | 76,8 | VALIDATING |
| TIME_24H | 6 | 0,997 | 1,104 | 0,180 | 66,7% | 74,1 | INSUFFICIENT_DATA |
| GB20_R050 | 665 | 0,107 | 0,000 | 0,043 | 46,2% | 69,6 | VALIDATING |
| GB30_R050 | 665 | 0,067 | 0,000 | -0,001 | 44,7% | 69,5 | VALIDATING |
| GB40_R075 | 89 | 0,190 | 0,000 | 0,040 | 48,3% | 67,5 | VALIDATING |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.
