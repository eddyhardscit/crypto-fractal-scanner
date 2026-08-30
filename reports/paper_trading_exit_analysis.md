# Analisi uscite paper trading a leva

Generato: 2026-08-30T05:15:30+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **9717**
- Trade con percorso cronologico utilizzabile: **9663**
- Trade che hanno raggiunto almeno +€50: **3675**
- Di questi, chiusi poi in perdita: **768**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€22.354,68 | +€44.037,71 |
| 2 | Protegge +€30 dopo +€50 | -€7.582,20 | +€14.100,83 |
| 3 | TP +€50 / SL -€50 | -€9.216,81 | +€12.466,22 |
| 4 | Protegge +€20 dopo +€50 | -€13.001,23 | +€8.681,80 |
| 5 | Chiude 50% a +€50 | -€16.905,54 | +€4.777,49 |
| 6 | Trailing 20% dopo +€50 | -€21.355,41 | +€327,62 |
| 7 | Strategia attuale | -€21.683,03 | €0,00 |
| 8 | Take profit fisso +€200 | -€21.683,03 | €0,00 |
| 9 | Take profit fisso +€150 | -€21.693,22 | -€10,19 |
| 10 | Pareggio dopo +€50 | -€21.967,31 | -€284,28 |
| 11 | Take profit fisso +€100 | -€23.587,00 | -€1.903,97 |
| 12 | Take profit fisso +€75 | -€35.475,50 | -€13.792,47 |
| 13 | Take profit fisso +€50 | -€52.109,08 | -€30.426,05 |
| 14 | Take profit fisso +€25 | -€58.098,97 | -€36.415,94 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
