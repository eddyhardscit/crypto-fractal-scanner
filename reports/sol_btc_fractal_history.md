# Storico frattale SOL/BTC

Generato: **2026-07-09 03:06:22 CEST**  
UTC: **2026-07-09 01:06:22 UTC**

Questo file salva giorno per giorno la lettura del frattale **BTC novembre 2022 vs SOL giugno 2026**.

Serve per vedere se SOL sta seguendo il percorso BTC-scalato, se si sta avvicinando, se si sta staccando sopra, oppure se sta perdendo aderenza.

Il CSV completo è: `sol_btc_fractal_history.csv`.

## Stato archivio

| Voce | Valore |
| --- | --- |
| Prima rilevazione salvata | 2026-07-08 |
| Ultima rilevazione salvata | 2026-07-09 |
| Righe salvate | 2 |

## Ultima lettura

| Voce | Valore |
| --- | --- |
| Data lettura | 2026-07-09 |
| Prezzo SOL | 77,77 $ |
| BTC scalato | 70,55 $ |
| Gap SOL vs BTC-scalato | +10,23% |
| Somiglianza totale | +73,91% |
| Fase | FASE ANTICIPATA |
| Tracking | FRATTALE STABILE |
| Errore medio da inizio programma | +22,63% |
| Errore ultimo giorno | +10,23% |
| Conferma 1 | 105,43 $ |
| Conferma 2 | 114,93 $ |
| Invalidazione soft | 73,86 $ |
| Invalidazione forte | 62,19 $ |
| Target ciclo base da oggi | 577,46 $ |

## Storico compatto giorno per giorno

| Data | SOL | BTC scalato | Gap | Somiglianza | Fase | Tracking | Errore live medio | Errore ultimo | Base 30g | Base 60g | Soft invalid. | Conferma 1 | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 77,45 $ | 66,17 $ | +17,05% | +73,94% | FASE ANTICIPATA | FRATTALE STABILE | +22,55% | +17,05% | 104,76 $ | 112,67 $ | 73,58 $ | 105,03 $ | 575,23 $ |
| 2026-07-09 | 77,77 $ | 70,55 $ | +10,23% | +73,91% | FASE ANTICIPATA | FRATTALE STABILE | +22,63% | +10,23% | 105,17 $ | 113,11 $ | 73,86 $ | 105,43 $ | 577,46 $ |

## Aderenza prima e dopo inizio programma

| Data | Aderenza pre | Errore pre | Stato pre | Aderenza live | Errore live | Stato live | Aderenza totale | Errore totale | Stato totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +54,89% | +22,55% | STACCATO / MOLTO IN ANTICIPO | +81,94% | +9,03% | ABBASTANZA ALLINEATO |
| 2026-07-09 | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +54,74% | +22,63% | STACCATO / MOLTO IN ANTICIPO | +81,91% | +9,04% | ABBASTANZA ALLINEATO |

## Storico proiezioni frattali

| Data | Base 7g | Base 14g | Base 30g | Base 60g | Base 90g | Base 120g | Min 30g | Max 30g | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 76,55 $ | 78,16 $ | 104,76 $ | 112,67 $ | 130,65 $ | 128,27 $ | 76,30 $ | 105,03 $ | 575,23 $ |
| 2026-07-09 | 76,85 $ | 78,47 $ | 105,17 $ | 113,11 $ | 131,15 $ | 128,76 $ | 76,60 $ | 105,43 $ | 577,46 $ |

## Come leggerlo

- **Gap**: quanto SOL è sopra o sotto la linea BTC-scalata.
- **Gap 0-5%**: frattale molto pulito.
- **Gap 5-10%**: frattale buono.
- **Gap 10-15%**: ancora accettabile, ma SOL è in anticipo.
- **Gap 15-25%**: frattale valido, ma meno preciso per prevedere ritracciamenti e date.
- **Gap oltre 25%**: SOL troppo accelerata rispetto al frattale.
- **Errore live medio**: la parte più importante, perché misura da quando abbiamo iniziato a monitorarlo davvero.
- **Base 30g / 60g**: dove dovrebbe andare SOL se segue il percorso BTC equivalente.
- **Soft invalidation**: primo livello dove il frattale si sporca.
- **Invalidazione forte**: sotto il bottom SOL usato, il frattale è quasi rotto.

Nota: se il workflow gira più volte nello stesso giorno, viene tenuta solo l'ultima lettura del giorno.
