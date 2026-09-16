# Analisi uscite paper trading a leva

Generato: 2026-09-16T05:19:05+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **13562**
- Trade con percorso cronologico utilizzabile: **13508**
- Trade che hanno raggiunto almeno +€50: **4658**
- Di questi, chiusi poi in perdita: **884**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€19.075,47 | +€47.684,06 |
| 2 | Protegge +€30 dopo +€50 | -€14.237,50 | +€14.371,09 |
| 3 | Protegge +€20 dopo +€50 | -€21.319,87 | +€7.288,73 |
| 4 | TP +€50 / SL -€50 | -€24.112,46 | +€4.496,14 |
| 5 | Chiude 50% a +€50 | -€24.327,05 | +€4.281,55 |
| 6 | Strategia attuale | -€28.608,59 | €0,00 |
| 7 | Take profit fisso +€200 | -€28.608,59 | €0,00 |
| 8 | Take profit fisso +€150 | -€28.618,78 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€29.679,85 | -€1.071,26 |
| 10 | Take profit fisso +€100 | -€31.534,05 | -€2.925,46 |
| 11 | Pareggio dopo +€50 | -€31.980,49 | -€3.371,90 |
| 12 | Take profit fisso +€75 | -€47.271,93 | -€18.663,33 |
| 13 | Take profit fisso +€50 | -€70.568,96 | -€41.960,37 |
| 14 | Take profit fisso +€25 | -€86.373,86 | -€57.765,27 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
