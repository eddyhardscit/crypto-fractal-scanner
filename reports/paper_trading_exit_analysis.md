# Analisi uscite paper trading a leva

Generato: 2026-08-19T05:08:53+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **6280**
- Trade con percorso cronologico utilizzabile: **6226**
- Trade che hanno raggiunto almeno +€50: **2345**
- Di questi, chiusi poi in perdita: **509**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€4.228,64 | +€32.420,69 |
| 2 | TP +€50 / SL -€50 | -€17.978,59 | +€18.670,73 |
| 3 | Protegge +€30 dopo +€50 | -€26.840,84 | +€9.808,48 |
| 4 | Chiude 50% a +€50 | -€29.714,35 | +€6.934,97 |
| 5 | Protegge +€20 dopo +€50 | -€30.389,31 | +€6.260,02 |
| 6 | Trailing 20% dopo +€50 | -€35.750,68 | +€898,64 |
| 7 | Strategia attuale | -€36.649,33 | €0,00 |
| 8 | Take profit fisso +€200 | -€36.649,33 | €0,00 |
| 9 | Take profit fisso +€150 | -€36.653,64 | -€4,32 |
| 10 | Pareggio dopo +€50 | -€36.760,32 | -€111,00 |
| 11 | Take profit fisso +€100 | -€37.026,02 | -€376,70 |
| 12 | Take profit fisso +€75 | -€42.739,29 | -€6.089,96 |
| 13 | Take profit fisso +€50 | -€49.073,00 | -€12.423,68 |
| 14 | Take profit fisso +€25 | -€52.785,98 | -€16.136,66 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
