# Storico frattale SOL/BTC

Generato: **2026-07-08 20:39:13 CEST**  
UTC: **2026-07-08 18:39:13 UTC**

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
| Prezzo SOL | 76,86 $ |
| BTC scalato | 66,17 $ |
| Gap SOL vs BTC-scalato | +16,16% |
| Somiglianza totale | +74,01% |
| Fase | FASE ANTICIPATA |
| Tracking | FRATTALE STABILE |
| Errore medio da inizio programma | +22,41% |
| Errore ultimo giorno | +16,16% |
| Conferma 1 | 104,24 $ |
| Conferma 2 | 113,63 $ |
| Invalidazione soft | 73,03 $ |
| Invalidazione forte | 62,19 $ |
| Target ciclo base da oggi | 570,92 $ |

## Storico compatto giorno per giorno

| Data | SOL | BTC scalato | Gap | Somiglianza | Fase | Tracking | Errore live medio | Errore ultimo | Base 30g | Base 60g | Soft invalid. | Conferma 1 | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 76,86 $ | 66,17 $ | +16,16% | +74,01% | FASE ANTICIPATA | FRATTALE STABILE | +22,41% | +16,16% | 103,98 $ | 111,83 $ | 73,03 $ | 104,24 $ | 570,92 $ |

## Aderenza prima e dopo inizio programma

| Data | Aderenza pre | Errore pre | Stato pre | Aderenza live | Errore live | Stato live | Aderenza totale | Errore totale | Stato totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +55,18% | +22,41% | STACCATO / MOLTO IN ANTICIPO | +81,99% | +9,00% | ABBASTANZA ALLINEATO |

## Storico proiezioni frattali

| Data | Base 7g | Base 14g | Base 30g | Base 60g | Base 90g | Base 120g | Min 30g | Max 30g | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 75,98 $ | 77,58 $ | 103,98 $ | 111,83 $ | 129,67 $ | 127,30 $ | 75,73 $ | 104,24 $ | 570,92 $ |

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
