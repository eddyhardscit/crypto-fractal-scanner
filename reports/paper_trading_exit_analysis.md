# Analisi uscite paper trading a leva

Generato: 2026-09-15T05:19:49+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **13403**
- Trade con percorso cronologico utilizzabile: **13349**
- Trade che hanno raggiunto almeno +€50: **4602**
- Di questi, chiusi poi in perdita: **875**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€18.963,55 | +€47.507,45 |
| 2 | Protegge +€30 dopo +€50 | -€14.565,17 | +€13.978,73 |
| 3 | Protegge +€20 dopo +€50 | -€21.397,53 | +€7.146,37 |
| 4 | TP +€50 / SL -€50 | -€24.654,81 | +€3.889,09 |
| 5 | Chiude 50% a +€50 | -€24.735,34 | +€3.808,56 |
| 6 | Strategia attuale | -€28.543,90 | €0,00 |
| 7 | Take profit fisso +€200 | -€28.543,90 | €0,00 |
| 8 | Take profit fisso +€150 | -€28.554,08 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€30.081,13 | -€1.537,23 |
| 10 | Take profit fisso +€100 | -€31.469,35 | -€2.925,46 |
| 11 | Pareggio dopo +€50 | -€31.649,48 | -€3.105,59 |
| 12 | Take profit fisso +€75 | -€47.150,10 | -€18.606,20 |
| 13 | Take profit fisso +€50 | -€71.002,85 | -€42.458,96 |
| 14 | Take profit fisso +€25 | -€85.834,63 | -€57.290,73 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
