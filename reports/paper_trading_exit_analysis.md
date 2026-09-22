# Analisi uscite paper trading a leva

Generato: 2026-09-17T17:41:16+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **14204**
- Trade con percorso cronologico utilizzabile: **14082**
- Trade che hanno raggiunto almeno +€50: **4911**
- Di questi, chiusi poi in perdita: **952**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€17.109,67 | +€47.396,95 |
| 2 | Protegge +€30 dopo +€50 | -€16.290,56 | +€13.996,73 |
| 3 | Trailing 20% dopo +€50 | -€23.648,35 | +€6.638,93 |
| 4 | Protegge +€20 dopo +€50 | -€24.322,92 | +€5.964,36 |
| 5 | Chiude 50% a +€50 | -€25.924,33 | +€4.362,95 |
| 6 | TP +€50 / SL -€50 | -€26.095,33 | +€4.191,95 |
| 7 | Take profit fisso +€150 | -€26.926,22 | +€3.361,06 |
| 8 | Take profit fisso +€200 | -€27.486,20 | +€2.801,08 |
| 9 | Take profit fisso +€100 | -€29.710,32 | +€576,96 |
| 10 | Strategia attuale | -€30.287,28 | €0,00 |
| 11 | Pareggio dopo +€50 | -€36.883,55 | -€6.596,26 |
| 12 | Take profit fisso +€75 | -€45.942,11 | -€15.654,83 |
| 13 | Take profit fisso +€50 | -€71.668,56 | -€41.381,28 |
| 14 | Take profit fisso +€25 | -€89.124,01 | -€58.836,73 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
