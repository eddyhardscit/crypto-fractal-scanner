# Analisi uscite paper trading a leva

Generato: 2026-09-14T05:18:53+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **13221**
- Trade con percorso cronologico utilizzabile: **13167**
- Trade che hanno raggiunto almeno +€50: **4559**
- Di questi, chiusi poi in perdita: **867**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€18.992,16 | +€47.458,11 |
| 2 | Protegge +€30 dopo +€50 | -€14.557,58 | +€13.908,37 |
| 3 | Protegge +€20 dopo +€50 | -€21.359,95 | +€7.106,01 |
| 4 | TP +€50 / SL -€50 | -€24.204,38 | +€4.261,57 |
| 5 | Chiude 50% a +€50 | -€24.869,49 | +€3.596,46 |
| 6 | Strategia attuale | -€28.465,95 | €0,00 |
| 7 | Take profit fisso +€200 | -€28.465,95 | €0,00 |
| 8 | Take profit fisso +€150 | -€28.476,14 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€30.062,58 | -€1.596,63 |
| 10 | Take profit fisso +€100 | -€31.338,07 | -€2.872,12 |
| 11 | Pareggio dopo +€50 | -€31.551,90 | -€3.085,95 |
| 12 | Take profit fisso +€75 | -€46.957,88 | -€18.491,93 |
| 13 | Take profit fisso +€50 | -€70.503,09 | -€42.037,14 |
| 14 | Take profit fisso +€25 | -€85.219,56 | -€56.753,61 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
