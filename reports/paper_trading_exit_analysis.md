# Analisi uscite paper trading a leva

Generato: 2026-08-31T05:15:59+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **10120**
- Trade con percorso cronologico utilizzabile: **10066**
- Trade che hanno raggiunto almeno +€50: **3782**
- Di questi, chiusi poi in perdita: **785**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€18.959,80 | +€44.428,88 |
| 2 | Protegge +€30 dopo +€50 | -€10.361,78 | +€15.107,29 |
| 3 | TP +€50 / SL -€50 | -€12.535,73 | +€12.933,35 |
| 4 | Protegge +€20 dopo +€50 | -€16.063,33 | +€9.405,74 |
| 5 | Chiude 50% a +€50 | -€20.249,49 | +€5.219,58 |
| 6 | Trailing 20% dopo +€50 | -€23.941,60 | +€1.527,47 |
| 7 | Pareggio dopo +€50 | -€25.258,41 | +€210,66 |
| 8 | Strategia attuale | -€25.469,07 | €0,00 |
| 9 | Take profit fisso +€200 | -€25.469,07 | €0,00 |
| 10 | Take profit fisso +€150 | -€25.479,26 | -€10,19 |
| 11 | Take profit fisso +€100 | -€27.472,46 | -€2.003,39 |
| 12 | Take profit fisso +€75 | -€39.755,04 | -€14.285,97 |
| 13 | Take profit fisso +€50 | -€55.810,82 | -€30.341,74 |
| 14 | Take profit fisso +€25 | -€62.470,02 | -€37.000,95 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
