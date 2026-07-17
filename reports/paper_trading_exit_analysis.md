# Analisi uscite paper trading a leva

Generato: 2026-07-17T00:23:59+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **103**
- Trade con percorso cronologico utilizzabile: **49**
- Trade che hanno raggiunto almeno +€50: **36**
- Di questi, chiusi poi in perdita: **6**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Protegge +€30 dopo +€50 | +€978,89 | +€103,59 |
| 2 | Stop loss fisso -€50 | +€960,89 | +€85,60 |
| 3 | Protegge +€20 dopo +€50 | +€953,18 | +€77,88 |
| 4 | Pareggio dopo +€50 | +€928,30 | +€53,00 |
| 5 | Take profit fisso +€100 | +€914,24 | +€38,95 |
| 6 | Trailing 20% dopo +€50 | +€908,29 | +€32,99 |
| 7 | Strategia attuale | +€875,30 | €0,00 |
| 8 | Take profit fisso +€150 | +€875,30 | €0,00 |
| 9 | Take profit fisso +€200 | +€875,30 | €0,00 |
| 10 | Take profit fisso +€75 | +€832,91 | -€42,39 |
| 11 | Chiude 50% a +€50 | +€813,52 | -€61,77 |
| 12 | TP +€50 / SL -€50 | +€632,55 | -€242,74 |
| 13 | Take profit fisso +€50 | +€549,96 | -€325,34 |
| 14 | Take profit fisso +€25 | +€260,04 | -€615,26 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
