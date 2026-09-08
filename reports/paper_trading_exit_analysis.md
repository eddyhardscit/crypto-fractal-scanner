# Analisi uscite paper trading a leva

Generato: 2026-09-08T05:16:57+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **12296**
- Trade con percorso cronologico utilizzabile: **12242**
- Trade che hanno raggiunto almeno +€50: **4375**
- Di questi, chiusi poi in perdita: **842**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€23.877,12 | +€46.565,47 |
| 2 | Protegge +€30 dopo +€50 | -€9.223,87 | +€13.464,48 |
| 3 | Protegge +€20 dopo +€50 | -€15.845,43 | +€6.842,92 |
| 4 | TP +€50 / SL -€50 | -€18.210,40 | +€4.477,95 |
| 5 | Chiude 50% a +€50 | -€19.637,32 | +€3.051,03 |
| 6 | Strategia attuale | -€22.688,35 | €0,00 |
| 7 | Take profit fisso +€200 | -€22.688,35 | €0,00 |
| 8 | Take profit fisso +€150 | -€22.698,53 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€24.576,19 | -€1.887,84 |
| 10 | Take profit fisso +€100 | -€25.461,52 | -€2.773,17 |
| 11 | Pareggio dopo +€50 | -€25.932,36 | -€3.244,01 |
| 12 | Take profit fisso +€75 | -€40.943,14 | -€18.254,80 |
| 13 | Take profit fisso +€50 | -€63.618,95 | -€40.930,60 |
| 14 | Take profit fisso +€25 | -€76.316,38 | -€53.628,03 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
