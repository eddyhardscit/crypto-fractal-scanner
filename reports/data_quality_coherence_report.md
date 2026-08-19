# Data quality / coherence check

Generato: 2026-08-19 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 64.306 $          | 64.306 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 64.306 $          | 64.306 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 64.306 $          | 64.306 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 64.306 $          | 64.306 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 64.306 $          | 64.306 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 64.306 $          | 64.334 $        | +0,0433%     |
| Exchange Microstructure | SOL     | price             | OK      | 76,92 $           | 76,86 $         | -0,0767%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07000 $         | 0.06998 $       | -0,0286%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 76,92 $           | 76,92 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 76,92 $           | 76,92 $         | +0,0000%     |

## Integrità Technical / Classic Visual

- Fibonacci strutturato: **OK**
- Candidati senza falso progresso target: **OK**
- Classic Visual allineato al lifecycle Technical: **OK**

## Controllo codifica UTF-8

Nessun indicatore comune di mojibake trovato.

## File strutturati

- Snapshot condiviso completo: **OK**
- Scanner summary: **OK**
- Price coherence sync: **OK**
- Dati exchange / microstruttura: **OK**

Il workflow è tecnicamente coerente nei controlli disponibili.
