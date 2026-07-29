# Analisi uscite paper trading a leva

Generato: 2026-07-29T05:10:08+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3350**
- Trade con percorso cronologico utilizzabile: **3296**
- Trade che hanno raggiunto almeno +€50: **1374**
- Di questi, chiusi poi in perdita: **274**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.930,65 | +€11.953,10 |
| 2 | Chiude 50% a +€50 | -€3.434,55 | +€2.587,90 |
| 3 | Protegge +€30 dopo +€50 | -€4.804,95 | +€1.217,50 |
| 4 | Protegge +€20 dopo +€50 | -€5.553,36 | +€469,09 |
| 5 | TP +€50 / SL -€50 | -€5.800,73 | +€221,72 |
| 6 | Strategia attuale | -€6.022,45 | €0,00 |
| 7 | Take profit fisso +€200 | -€6.022,45 | €0,00 |
| 8 | Take profit fisso +€150 | -€6.026,77 | -€4,32 |
| 9 | Take profit fisso +€100 | -€6.237,69 | -€215,24 |
| 10 | Trailing 20% dopo +€50 | -€6.700,73 | -€678,28 |
| 11 | Pareggio dopo +€50 | -€7.202,47 | -€1.180,02 |
| 12 | Take profit fisso +€75 | -€10.360,32 | -€4.337,87 |
| 13 | Take profit fisso +€50 | -€17.615,70 | -€11.593,24 |
| 14 | Take profit fisso +€25 | -€18.270,00 | -€12.247,55 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
