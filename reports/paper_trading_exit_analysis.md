# Analisi uscite paper trading a leva

Generato: 2026-09-17T05:18:43+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **13724**
- Trade con percorso cronologico utilizzabile: **13670**
- Trade che hanno raggiunto almeno +€50: **4682**
- Di questi, chiusi poi in perdita: **884**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€18.528,95 | +€47.895,58 |
| 2 | Protegge +€30 dopo +€50 | -€15.069,11 | +€14.297,51 |
| 3 | Protegge +€20 dopo +€50 | -€22.171,48 | +€7.195,15 |
| 4 | Chiude 50% a +€50 | -€25.290,56 | +€4.076,06 |
| 5 | TP +€50 / SL -€50 | -€25.293,15 | +€4.073,48 |
| 6 | Strategia attuale | -€29.366,63 | €0,00 |
| 7 | Take profit fisso +€200 | -€29.366,63 | €0,00 |
| 8 | Take profit fisso +€150 | -€29.376,81 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€30.607,31 | -€1.240,68 |
| 10 | Take profit fisso +€100 | -€32.338,82 | -€2.972,19 |
| 11 | Pareggio dopo +€50 | -€32.872,10 | -€3.505,48 |
| 12 | Take profit fisso +€75 | -€48.267,08 | -€18.900,45 |
| 13 | Take profit fisso +€50 | -€71.961,17 | -€42.594,55 |
| 14 | Take profit fisso +€25 | -€88.141,47 | -€58.774,84 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
