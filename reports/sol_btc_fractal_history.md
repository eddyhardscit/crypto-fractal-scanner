# Storico frattale SOL/BTC

Generato: **2026-07-08 20:20:38 CEST**  
UTC: **2026-07-08 18:20:38 UTC**

Questo file salva giorno per giorno la lettura del frattale **BTC novembre 2022 vs SOL giugno 2026**.

Serve per vedere se SOL sta seguendo il percorso BTC-scalato, se si sta avvicinando, se si sta staccando sopra, oppure se sta perdendo aderenza.

Il CSV completo è: `sol_btc_fractal_history.csv`.

## Stato archivio

| Voce | Valore |
| --- | --- |
| Prima rilevazione salvata | 2026-07-08 |
| Ultima rilevazione salvata | 2026-07-08 |
| Righe salvate | 1 |

## Ultima lettura

| Voce | Valore |
| --- | --- |
| Data lettura | 2026-07-08 |
| Prezzo SOL | 77,16 $ |
| BTC scalato | 66,17 $ |
| Gap SOL vs BTC-scalato | +16,61% |
| Somiglianza totale | +73,98% |
| Fase | FASE ANTICIPATA |
| Tracking | FRATTALE STABILE |
| Errore medio da inizio programma | +22,48% |
| Errore ultimo giorno | +16,61% |
| Conferma 1 | 104,61 $ |
| Conferma 2 | 114,03 $ |
| Invalidazione soft | 73,28 $ |
| Invalidazione forte | 62,19 $ |
| Target ciclo base da oggi | 572,93 $ |

## Storico compatto giorno per giorno

| Data | SOL | BTC scalato | Gap | Somiglianza | Fase | Tracking | Errore live medio | Errore ultimo | Base 30g | Base 60g | Soft invalid. | Conferma 1 | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 77,16 $ | 66,17 $ | +16,61% | +73,98% | FASE ANTICIPATA | FRATTALE STABILE | +22,48% | +16,61% | 104,34 $ | 112,22 $ | 73,28 $ | 104,61 $ | 572,93 $ |

## Aderenza prima e dopo inizio programma

| Data | Aderenza pre | Errore pre | Stato pre | Aderenza live | Errore live | Stato live | Aderenza totale | Errore totale | Stato totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +55,05% | +22,48% | STACCATO / MOLTO IN ANTICIPO | +81,97% | +9,02% | ABBASTANZA ALLINEATO |

## Storico proiezioni frattali

| Data | Base 7g | Base 14g | Base 30g | Base 60g | Base 90g | Base 120g | Min 30g | Max 30g | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 76,25 $ | 77,85 $ | 104,34 $ | 112,22 $ | 130,12 $ | 127,75 $ | 75,99 $ | 104,61 $ | 572,93 $ |

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
