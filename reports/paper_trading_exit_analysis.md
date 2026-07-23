# Analisi uscite paper trading a leva

Generato: 2026-07-23T07:35:12+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **828**
- Trade con percorso cronologico utilizzabile: **774**
- Trade che hanno raggiunto almeno +€50: **323**
- Di questi, chiusi poi in perdita: **77**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€3.050,60 | +€1.600,00 |
| 2 | Protegge +€30 dopo +€50 | -€4.072,53 | +€578,07 |
| 3 | Chiude 50% a +€50 | -€4.260,03 | +€390,56 |
| 4 | Protegge +€20 dopo +€50 | -€4.315,96 | +€334,63 |
| 5 | Take profit fisso +€100 | -€4.456,64 | +€193,95 |
| 6 | Pareggio dopo +€50 | -€4.571,46 | +€79,13 |
| 7 | Strategia attuale | -€4.650,59 | €0,00 |
| 8 | Take profit fisso +€150 | -€4.650,59 | €0,00 |
| 9 | Take profit fisso +€200 | -€4.650,59 | €0,00 |
| 10 | Trailing 20% dopo +€50 | -€5.035,54 | -€384,95 |
| 11 | Take profit fisso +€75 | -€5.305,81 | -€655,22 |
| 12 | TP +€50 / SL -€50 | -€6.637,90 | -€1.987,31 |
| 13 | Take profit fisso +€25 | -€7.243,68 | -€2.593,09 |
| 14 | Take profit fisso +€50 | -€8.253,89 | -€3.603,30 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
