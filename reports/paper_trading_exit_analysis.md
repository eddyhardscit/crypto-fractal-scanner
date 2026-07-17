# Analisi uscite paper trading a leva

Generato: 2026-07-17T06:30:17+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **111**
- Trade con percorso cronologico utilizzabile: **57**
- Trade che hanno raggiunto almeno +€50: **40**
- Di questi, chiusi poi in perdita: **7**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Take profit fisso +€100 | +€1.040,72 | +€139,84 |
| 2 | Protegge +€30 dopo +€50 | +€1.035,36 | +€134,49 |
| 3 | Protegge +€20 dopo +€50 | +€999,65 | +€98,77 |
| 4 | Trailing 20% dopo +€50 | +€976,87 | +€75,99 |
| 5 | Pareggio dopo +€50 | +€954,77 | +€53,90 |
| 6 | Take profit fisso +€75 | +€910,82 | +€9,94 |
| 7 | Strategia attuale | +€900,88 | €0,00 |
| 8 | Take profit fisso +€150 | +€900,88 | €0,00 |
| 9 | Take profit fisso +€200 | +€900,88 | €0,00 |
| 10 | Stop loss fisso -€50 | +€880,85 | -€20,03 |
| 11 | Chiude 50% a +€50 | +€819,63 | -€81,25 |
| 12 | Take profit fisso +€50 | +€536,59 | -€364,29 |
| 13 | TP +€50 / SL -€50 | +€532,55 | -€368,32 |
| 14 | Take profit fisso +€25 | +€223,27 | -€677,61 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
