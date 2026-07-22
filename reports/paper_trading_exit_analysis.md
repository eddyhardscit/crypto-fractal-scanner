# Analisi uscite paper trading a leva

Generato: 2026-07-22T05:08:45+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **631**
- Trade con percorso cronologico utilizzabile: **577**
- Trade che hanno raggiunto almeno +€50: **263**
- Di questi, chiusi poi in perdita: **65**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€112,34 | +€1.014,82 |
| 2 | Protegge +€30 dopo +€50 | -€536,35 | +€590,80 |
| 3 | Chiude 50% a +€50 | -€777,14 | +€350,02 |
| 4 | Protegge +€20 dopo +€50 | -€796,94 | +€330,22 |
| 5 | Take profit fisso +€100 | -€940,79 | +€186,37 |
| 6 | Pareggio dopo +€50 | -€1.059,55 | +€67,61 |
| 7 | Strategia attuale | -€1.127,16 | €0,00 |
| 8 | Take profit fisso +€150 | -€1.127,16 | €0,00 |
| 9 | Take profit fisso +€200 | -€1.127,16 | €0,00 |
| 10 | Take profit fisso +€75 | -€1.525,60 | -€398,44 |
| 11 | Trailing 20% dopo +€50 | -€1.532,98 | -€405,82 |
| 12 | TP +€50 / SL -€50 | -€2.865,23 | -€1.738,07 |
| 13 | Take profit fisso +€25 | -€3.813,02 | -€2.685,86 |
| 14 | Take profit fisso +€50 | -€3.896,04 | -€2.768,88 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
