# Analisi uscite paper trading a leva

Generato: 2026-07-16T13:30:30+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **88**
- Trade con percorso cronologico utilizzabile: **34**
- Trade che hanno raggiunto almeno +€50: **29**
- Di questi, chiusi poi in perdita: **6**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Protegge +€30 dopo +€50 | +€913,41 | +€103,59 |
| 2 | Protegge +€20 dopo +€50 | +€887,69 | +€77,88 |
| 3 | Trailing 20% dopo +€50 | +€876,06 | +€66,25 |
| 4 | Stop loss fisso -€50 | +€862,89 | +€53,07 |
| 5 | Pareggio dopo +€50 | +€862,81 | +€53,00 |
| 6 | Take profit fisso +€100 | +€829,16 | +€19,35 |
| 7 | Chiude 50% a +€50 | +€822,04 | +€12,23 |
| 8 | Strategia attuale | +€809,81 | €0,00 |
| 9 | Take profit fisso +€150 | +€809,81 | €0,00 |
| 10 | Take profit fisso +€200 | +€809,81 | €0,00 |
| 11 | Take profit fisso +€75 | +€740,43 | -€69,38 |
| 12 | TP +€50 / SL -€50 | +€682,55 | -€127,26 |
| 13 | Take profit fisso +€50 | +€632,48 | -€177,33 |
| 14 | Take profit fisso +€25 | +€436,39 | -€373,42 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
