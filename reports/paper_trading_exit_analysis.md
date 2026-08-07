# Analisi uscite paper trading a leva

Generato: 2026-08-07T05:12:08+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3615**
- Trade con percorso cronologico utilizzabile: **3561**
- Trade che hanno raggiunto almeno +€50: **1407**
- Di questi, chiusi poi in perdita: **289**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.337,02 | +€11.995,61 |
| 2 | Chiude 50% a +€50 | -€3.466,86 | +€3.191,73 |
| 3 | Protegge +€30 dopo +€50 | -€4.918,89 | +€1.739,70 |
| 4 | TP +€50 / SL -€50 | -€5.332,64 | +€1.325,96 |
| 5 | Protegge +€20 dopo +€50 | -€5.845,19 | +€813,41 |
| 6 | Trailing 20% dopo +€50 | -€6.549,80 | +€108,79 |
| 7 | Strategia attuale | -€6.658,59 | €0,00 |
| 8 | Take profit fisso +€200 | -€6.658,59 | €0,00 |
| 9 | Take profit fisso +€150 | -€6.662,91 | -€4,32 |
| 10 | Take profit fisso +€100 | -€6.873,83 | -€215,24 |
| 11 | Pareggio dopo +€50 | -€7.781,70 | -€1.123,10 |
| 12 | Take profit fisso +€75 | -€10.068,73 | -€3.410,13 |
| 13 | Take profit fisso +€25 | -€17.165,97 | -€10.507,38 |
| 14 | Take profit fisso +€50 | -€17.189,19 | -€10.530,60 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
