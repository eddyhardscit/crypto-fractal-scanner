# Analisi uscite paper trading a leva

Generato: 2026-08-17T05:08:44+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **5606**
- Trade con percorso cronologico utilizzabile: **5552**
- Trade che hanno raggiunto almeno +€50: **2127**
- Di questi, chiusi poi in perdita: **446**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€3.455,15 | +€26.061,85 |
| 2 | TP +€50 / SL -€50 | -€16.176,83 | +€13.340,17 |
| 3 | Protegge +€30 dopo +€50 | -€21.362,85 | +€8.154,15 |
| 4 | Chiude 50% a +€50 | -€23.908,22 | +€5.608,79 |
| 5 | Protegge +€20 dopo +€50 | -€24.440,93 | +€5.076,08 |
| 6 | Trailing 20% dopo +€50 | -€28.684,46 | +€832,54 |
| 7 | Strategia attuale | -€29.517,00 | €0,00 |
| 8 | Take profit fisso +€200 | -€29.517,00 | €0,00 |
| 9 | Take profit fisso +€150 | -€29.521,32 | -€4,32 |
| 10 | Pareggio dopo +€50 | -€29.751,94 | -€234,94 |
| 11 | Take profit fisso +€100 | -€29.980,49 | -€463,48 |
| 12 | Take profit fisso +€75 | -€34.930,93 | -€5.413,93 |
| 13 | Take profit fisso +€50 | -€41.278,73 | -€11.761,72 |
| 14 | Take profit fisso +€25 | -€46.081,11 | -€16.564,10 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
