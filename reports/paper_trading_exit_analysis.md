# Analisi uscite paper trading a leva

Generato: 2026-09-09T05:17:38+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **12456**
- Trade con percorso cronologico utilizzabile: **12402**
- Trade che hanno raggiunto almeno +€50: **4422**
- Di questi, chiusi poi in perdita: **846**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€24.431,45 | +€46.718,17 |
| 2 | Protegge +€30 dopo +€50 | -€8.815,25 | +€13.471,46 |
| 3 | Protegge +€20 dopo +€50 | -€15.443,80 | +€6.842,92 |
| 4 | TP +€50 / SL -€50 | -€18.393,06 | +€3.893,66 |
| 5 | Chiude 50% a +€50 | -€19.343,05 | +€2.943,67 |
| 6 | Strategia attuale | -€22.286,71 | €0,00 |
| 7 | Take profit fisso +€200 | -€22.286,71 | €0,00 |
| 8 | Take profit fisso +€150 | -€22.296,90 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€24.275,00 | -€1.988,29 |
| 10 | Take profit fisso +€100 | -€25.072,77 | -€2.786,05 |
| 11 | Pareggio dopo +€50 | -€25.530,73 | -€3.244,01 |
| 12 | Take profit fisso +€75 | -€40.612,17 | -€18.325,46 |
| 13 | Take profit fisso +€50 | -€63.954,31 | -€41.667,59 |
| 14 | Take profit fisso +€25 | -€77.205,79 | -€54.919,07 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
