# Analisi uscite paper trading a leva

Generato: 2026-09-10T05:17:11+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **12677**
- Trade con percorso cronologico utilizzabile: **12623**
- Trade che hanno raggiunto almeno +€50: **4475**
- Di questi, chiusi poi in perdita: **856**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€22.909,10 | +€46.964,02 |
| 2 | Protegge +€30 dopo +€50 | -€10.345,54 | +€13.709,38 |
| 3 | Protegge +€20 dopo +€50 | -€17.078,87 | +€6.976,06 |
| 4 | TP +€50 / SL -€50 | -€19.622,89 | +€4.432,04 |
| 5 | Chiude 50% a +€50 | -€20.611,23 | +€3.443,69 |
| 6 | Strategia attuale | -€24.054,93 | €0,00 |
| 7 | Take profit fisso +€200 | -€24.054,93 | €0,00 |
| 8 | Take profit fisso +€150 | -€24.065,11 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€25.744,57 | -€1.689,65 |
| 10 | Take profit fisso +€100 | -€26.866,91 | -€2.811,99 |
| 11 | Pareggio dopo +€50 | -€27.170,82 | -€3.115,89 |
| 12 | Take profit fisso +€75 | -€42.468,34 | -€18.413,41 |
| 13 | Take profit fisso +€50 | -€65.427,51 | -€41.372,59 |
| 14 | Take profit fisso +€25 | -€78.935,77 | -€54.880,84 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
