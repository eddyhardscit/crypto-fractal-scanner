# Data quality / coherence check

Generato: 2026-07-11 03:03 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 3 campi prezzo non coincidono con lo snapshot entro 0.00%.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 64.115 $          | 64.115 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07418 $         | 0.07418 $       | +0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 64.115 $          | 64.115 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07418 $         | 0.07418 $       | +0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 64.115 $          | 64.115 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07418 $         | 0.07418 $       | +0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 64.115 $          | 64.115 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07418 $         | 0.07418 $       | +0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 64.115 $          | 64.115 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07418 $         | 0.07418 $       | +0,0000%     |
| Exchange Microstructure | BTC     | price             | WARN    | 64.115 $          | 64.152 $        | +0,0573%     |
| Exchange Microstructure | SOL     | price             | WARN    | 77,72 $           | 77,77 $         | +0,0605%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.07418 $         | 0.07422 $       | +0,0607%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 77,72 $           | 77,72 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 77,72 $           | 77,72 $         | +0,0000%     |

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
