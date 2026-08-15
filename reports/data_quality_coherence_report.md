# Data quality / coherence check

Generato: 2026-08-15 05:34 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 63.051 $          | 63.051 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07014 $         | 0.07014 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 63.051 $          | 63.103 $        | +0,0833%     |
| Exchange Microstructure | SOL     | price             | OK      | 75,39 $           | 75,48 $         | +0,1154%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.07014 $         | 0.07029 $       | +0,2139%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 75,39 $           | 75,39 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 75,39 $           | 75,39 $         | +0,0000%     |

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

Il workflow può continuare, ma gli avvisi sopra vanno verificati.
