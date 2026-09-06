# Analisi uscite paper trading a leva

Generato: 2026-09-06T05:18:22+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **11732**
- Trade con percorso cronologico utilizzabile: **11678**
- Trade che hanno raggiunto almeno +€50: **4310**
- Di questi, chiusi poi in perdita: **829**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€28.372,00 | +€46.293,56 |
| 2 | Protegge +€30 dopo +€50 | -€4.881,11 | +€13.040,46 |
| 3 | Protegge +€20 dopo +€50 | -€11.379,76 | +€6.541,81 |
| 4 | TP +€50 / SL -€50 | -€13.776,94 | +€4.144,63 |
| 5 | Chiude 50% a +€50 | -€15.353,83 | +€2.567,74 |
| 6 | Strategia attuale | -€17.921,57 | €0,00 |
| 7 | Take profit fisso +€200 | -€17.921,57 | €0,00 |
| 8 | Take profit fisso +€150 | -€17.931,76 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€20.195,29 | -€2.273,72 |
| 10 | Take profit fisso +€100 | -€20.713,92 | -€2.792,35 |
| 11 | Pareggio dopo +€50 | -€21.342,05 | -€3.420,49 |
| 12 | Take profit fisso +€75 | -€36.072,36 | -€18.150,79 |
| 13 | Take profit fisso +€50 | -€58.916,72 | -€40.995,15 |
| 14 | Take profit fisso +€25 | -€71.285,55 | -€53.363,98 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
