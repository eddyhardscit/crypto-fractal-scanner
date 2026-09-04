# Analisi uscite paper trading a leva

Generato: 2026-09-04T05:17:05+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **11130**
- Trade con percorso cronologico utilizzabile: **11076**
- Trade che hanno raggiunto almeno +€50: **4156**
- Di questi, chiusi poi in perdita: **817**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€26.177,30 | +€45.426,07 |
| 2 | Protegge +€30 dopo +€50 | -€6.165,04 | +€13.083,73 |
| 3 | Protegge +€20 dopo +€50 | -€12.413,79 | +€6.834,98 |
| 4 | TP +€50 / SL -€50 | -€13.258,46 | +€5.990,31 |
| 5 | Chiude 50% a +€50 | -€15.923,98 | +€3.324,80 |
| 6 | Strategia attuale | -€19.248,77 | €0,00 |
| 7 | Take profit fisso +€200 | -€19.248,77 | €0,00 |
| 8 | Take profit fisso +€150 | -€19.258,96 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€21.250,44 | -€2.001,66 |
| 10 | Take profit fisso +€100 | -€21.873,76 | -€2.624,99 |
| 11 | Pareggio dopo +€50 | -€22.475,63 | -€3.226,85 |
| 12 | Take profit fisso +€75 | -€36.367,94 | -€17.119,17 |
| 13 | Take profit fisso +€50 | -€57.530,74 | -€38.281,97 |
| 14 | Take profit fisso +€25 | -€69.426,32 | -€50.177,55 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
