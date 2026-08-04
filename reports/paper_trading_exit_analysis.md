# Analisi uscite paper trading a leva

Generato: 2026-08-04T05:12:56+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3581**
- Trade con percorso cronologico utilizzabile: **3527**
- Trade che hanno raggiunto almeno +€50: **1406**
- Di questi, chiusi poi in perdita: **288**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.392,66 | +€11.995,61 |
| 2 | Chiude 50% a +€50 | -€3.436,90 | +€3.166,06 |
| 3 | Protegge +€30 dopo +€50 | -€4.894,61 | +€1.708,35 |
| 4 | TP +€50 / SL -€50 | -€5.328,35 | +€1.274,61 |
| 5 | Protegge +€20 dopo +€50 | -€5.810,90 | +€792,06 |
| 6 | Trailing 20% dopo +€50 | -€6.530,84 | +€72,11 |
| 7 | Strategia attuale | -€6.602,95 | €0,00 |
| 8 | Take profit fisso +€200 | -€6.602,95 | €0,00 |
| 9 | Take profit fisso +€150 | -€6.607,27 | -€4,32 |
| 10 | Take profit fisso +€100 | -€6.818,19 | -€215,24 |
| 11 | Pareggio dopo +€50 | -€7.727,41 | -€1.124,45 |
| 12 | Take profit fisso +€75 | -€10.013,09 | -€3.410,13 |
| 13 | Take profit fisso +€25 | -€17.136,68 | -€10.533,73 |
| 14 | Take profit fisso +€50 | -€17.184,91 | -€10.581,95 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
