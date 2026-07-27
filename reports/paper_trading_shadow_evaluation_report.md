# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-27T05:08:51+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **50073**
- Valutazioni prodotte: **15566**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 38 | 3,902 | 4,831 | 3,381 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB20_R075 | 38 | 3,902 | 4,831 | 3,408 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB30_R050 | 38 | 3,879 | 4,818 | 3,340 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB30_R075 | 38 | 3,879 | 4,818 | 3,335 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB40_R050 | 38 | 3,769 | 4,678 | 3,263 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB40_R075 | 38 | 3,769 | 4,678 | 3,258 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB50_R050 | 38 | 3,651 | 4,538 | 3,100 | 92,1% | 87,0 | EARLY_SIGNAL |
| GB50_R075 | 38 | 3,651 | 4,538 | 3,108 | 92,1% | 87,0 | EARLY_SIGNAL |
| ATR15_R050 | 38 | 3,266 | 4,115 | 2,800 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB30_R100 | 38 | 3,766 | 4,818 | 3,156 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R075 | 38 | 3,732 | 4,587 | 3,212 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB40_R100 | 38 | 3,654 | 4,678 | 3,048 | 92,1% | 86,9 | EARLY_SIGNAL |
| ATR10_R050 | 38 | 3,653 | 4,641 | 3,141 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R060 | 38 | 3,598 | 4,437 | 3,093 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB50_R100 | 38 | 3,542 | 4,538 | 2,989 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R050 | 38 | 3,508 | 4,337 | 3,040 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R040 | 38 | 3,419 | 4,238 | 2,952 | 92,1% | 86,9 | EARLY_SIGNAL |
| TP_R035 | 38 | 3,374 | 4,188 | 2,922 | 92,1% | 86,9 | EARLY_SIGNAL |
| GB20_R100 | 38 | 3,783 | 4,831 | 3,210 | 92,1% | 86,9 | EARLY_SIGNAL |
| ATR15_R100 | 38 | 3,187 | 4,115 | 2,696 | 92,1% | 86,9 | EARLY_SIGNAL |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.
