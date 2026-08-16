# Analisi uscite paper trading a leva

Generato: 2026-08-16T05:09:26+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **5385**
- Trade con percorso cronologico utilizzabile: **5331**
- Trade che hanno raggiunto almeno +€50: **2099**
- Di questi, chiusi poi in perdita: **438**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€52,88 | +€25.094,99 |
| 2 | TP +€50 / SL -€50 | -€12.680,69 | +€12.467,18 |
| 3 | Protegge +€30 dopo +€50 | -€17.133,51 | +€8.014,36 |
| 4 | Chiude 50% a +€50 | -€19.773,70 | +€5.374,17 |
| 5 | Protegge +€20 dopo +€50 | -€20.171,59 | +€4.976,28 |
| 6 | Trailing 20% dopo +€50 | -€24.439,92 | +€707,95 |
| 7 | Strategia attuale | -€25.147,87 | €0,00 |
| 8 | Take profit fisso +€200 | -€25.147,87 | €0,00 |
| 9 | Take profit fisso +€150 | -€25.152,19 | -€4,32 |
| 10 | Pareggio dopo +€50 | -€25.408,74 | -€260,87 |
| 11 | Take profit fisso +€100 | -€25.611,35 | -€463,48 |
| 12 | Take profit fisso +€75 | -€30.477,24 | -€5.329,36 |
| 13 | Take profit fisso +€50 | -€36.815,73 | -€11.667,86 |
| 14 | Take profit fisso +€25 | -€42.431,25 | -€17.283,38 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
