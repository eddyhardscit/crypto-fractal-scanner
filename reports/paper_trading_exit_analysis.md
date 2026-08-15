# Analisi uscite paper trading a leva

Generato: 2026-08-15T05:10:26+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **5207**
- Trade con percorso cronologico utilizzabile: **5153**
- Trade che hanno raggiunto almeno +€50: **2007**
- Di questi, chiusi poi in perdita: **400**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€1.728,24 | +€21.544,12 |
| 2 | TP +€50 / SL -€50 | -€13.308,68 | +€9.963,68 |
| 3 | Protegge +€30 dopo +€50 | -€15.176,79 | +€8.095,57 |
| 4 | Protegge +€20 dopo +€50 | -€17.984,87 | +€5.287,50 |
| 5 | Chiude 50% a +€50 | -€18.226,38 | +€5.045,99 |
| 6 | Pareggio dopo +€50 | -€22.644,17 | +€628,19 |
| 7 | Trailing 20% dopo +€50 | -€22.727,10 | +€545,27 |
| 8 | Strategia attuale | -€23.272,37 | €0,00 |
| 9 | Take profit fisso +€200 | -€23.272,37 | €0,00 |
| 10 | Take profit fisso +€150 | -€23.276,68 | -€4,32 |
| 11 | Take profit fisso +€100 | -€23.991,99 | -€719,62 |
| 12 | Take profit fisso +€75 | -€28.171,56 | -€4.899,19 |
| 13 | Take profit fisso +€50 | -€33.930,95 | -€10.658,58 |
| 14 | Take profit fisso +€25 | -€40.998,05 | -€17.725,68 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
