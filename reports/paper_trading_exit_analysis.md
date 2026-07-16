# Analisi uscite paper trading a leva

Generato: 2026-07-16T09:22:59+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **87**
- Trade con percorso cronologico utilizzabile: **33**
- Trade che hanno raggiunto almeno +€50: **29**
- Di questi, chiusi poi in perdita: **6**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Protegge +€30 dopo +€50 | +€968,99 | +€103,59 |
| 2 | Protegge +€20 dopo +€50 | +€943,28 | +€77,88 |
| 3 | Trailing 20% dopo +€50 | +€931,65 | +€66,25 |
| 4 | Pareggio dopo +€50 | +€918,40 | +€53,00 |
| 5 | Stop loss fisso -€50 | +€912,89 | +€47,49 |
| 6 | Take profit fisso +€100 | +€884,74 | +€19,35 |
| 7 | Chiude 50% a +€50 | +€877,63 | +€12,23 |
| 8 | Strategia attuale | +€865,40 | €0,00 |
| 9 | Take profit fisso +€150 | +€865,40 | €0,00 |
| 10 | Take profit fisso +€200 | +€865,40 | €0,00 |
| 11 | Take profit fisso +€75 | +€796,02 | -€69,38 |
| 12 | TP +€50 / SL -€50 | +€732,55 | -€132,84 |
| 13 | Take profit fisso +€50 | +€688,07 | -€177,33 |
| 14 | Take profit fisso +€25 | +€491,98 | -€373,42 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
