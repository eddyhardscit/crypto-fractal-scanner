# Analisi uscite paper trading a leva

Generato: 2026-08-20T05:09:08+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **6852**
- Trade con percorso cronologico utilizzabile: **6798**
- Trade che hanno raggiunto almeno +€50: **2579**
- Di questi, chiusi poi in perdita: **555**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€1.017,05 | +€37.152,24 |
| 2 | TP +€50 / SL -€50 | -€18.596,22 | +€17.538,97 |
| 3 | Protegge +€30 dopo +€50 | -€25.672,51 | +€10.462,69 |
| 4 | Protegge +€20 dopo +€50 | -€29.334,34 | +€6.800,85 |
| 5 | Chiude 50% a +€50 | -€30.626,17 | +€5.509,02 |
| 6 | Trailing 20% dopo +€50 | -€35.012,18 | +€1.123,02 |
| 7 | Pareggio dopo +€50 | -€35.986,28 | +€148,91 |
| 8 | Strategia attuale | -€36.135,19 | €0,00 |
| 9 | Take profit fisso +€200 | -€36.135,19 | €0,00 |
| 10 | Take profit fisso +€150 | -€36.139,51 | -€4,32 |
| 11 | Take profit fisso +€100 | -€36.342,46 | -€207,27 |
| 12 | Take profit fisso +€75 | -€44.392,98 | -€8.257,79 |
| 13 | Take profit fisso +€25 | -€51.374,62 | -€15.239,43 |
| 14 | Take profit fisso +€50 | -€54.280,00 | -€18.144,81 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
