# Analisi uscite paper trading a leva

Generato: 2026-09-12T05:18:17+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **13012**
- Trade con percorso cronologico utilizzabile: **12958**
- Trade che hanno raggiunto almeno +€50: **4530**
- Di questi, chiusi poi in perdita: **862**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€21.305,32 | +€47.280,36 |
| 2 | Protegge +€30 dopo +€50 | -€12.130,77 | +€13.844,27 |
| 3 | Protegge +€20 dopo +€50 | -€18.913,13 | +€7.061,91 |
| 4 | TP +€50 / SL -€50 | -€21.757,00 | +€4.218,03 |
| 5 | Chiude 50% a +€50 | -€22.495,99 | +€3.479,04 |
| 6 | Strategia attuale | -€25.975,03 | €0,00 |
| 7 | Take profit fisso +€200 | -€25.975,03 | €0,00 |
| 8 | Take profit fisso +€150 | -€25.985,22 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€27.562,67 | -€1.587,63 |
| 10 | Take profit fisso +€100 | -€28.847,15 | -€2.872,12 |
| 11 | Pareggio dopo +€50 | -€29.065,08 | -€3.090,05 |
| 12 | Take profit fisso +€75 | -€44.466,97 | -€18.491,93 |
| 13 | Take profit fisso +€50 | -€67.877,96 | -€41.902,92 |
| 14 | Take profit fisso +€25 | -€82.263,39 | -€56.288,36 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
