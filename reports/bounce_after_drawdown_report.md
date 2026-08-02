# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-02 07:14:19 CEST**  
UTC: **2026-08-02 05:14:19 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.236 $ | 69.747 $ | +17,65% | +15,79% | rimbalzo poco frequente | 69.747 $ | 60.236 $ | 0,00% | -13,64% | spike storicamente più resistente |
| SOL | 69,75 $ | 80,76 $ | +25,00% | +15,79% | rimbalzo poco frequente | 80,76 $ | 69,75 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06663 $ | 0,07715 $ | +37,93% | +15,79% | rimbalzo debole | 0,07715 $ | 0,06663 $ | +29,63% | -13,64% | spike storicamente più resistente |

## Spiegazione semplice delle percentuali

Queste percentuali sono **condizionate**.

Vuol dire che il report controlla sempre due passaggi, in ordine:

1. Prima deve succedere la prima cosa.
2. Solo dopo si controlla se succede la seconda cosa.

### Esempio rimbalzo

`Se scende a -5% → poi +10% = 24%`

Vuol dire:

- Lo scanner prende i 40 casi storici più simili.
- Prima guarda quanti sono scesi almeno a -5% dal prezzo iniziale.
- Poi, solo tra quelli che sono scesi, guarda quanti sono arrivati a +10% dal prezzo iniziale.
- Se il risultato è 24%, vuol dire circa 1 caso su 4.

Esempio con prezzo iniziale 100 $:

- -5% = 95 $
- +10% = 110 $
- il movimento reale da 95 $ a 110 $ non è +10%, ma circa +15,79%.

Quindi `poi +10%` non significa +10% dal minimo. Significa +10% dal prezzo iniziale.

### Esempio dump dopo spike

`Se sale a +10% → poi dump -5% = 62%`

Vuol dire:

- Prima il prezzo deve salire almeno a +10% dal prezzo iniziale.
- Poi si controlla se, dopo quello spike, scende fino a -5% dal prezzo iniziale.
- Se il risultato è 62%, vuol dire che questo scarico è successo più di metà delle volte.

Esempio con prezzo iniziale 100 $:

- +10% = 110 $
- -5% = 95 $
- il movimento reale da 110 $ a 95 $ non è -5%, ma circa -13,64%.

Quindi `dump -5%` non significa -5% dallo spike. Significa che torna fino a 5% sotto il prezzo iniziale.

### Soglie controllate

Nel report principale vedi solo la lettura più semplice:

- discesa -5% → rimbalzo +10%
- spike +10% → dump -5%

Nel report dettagliato invece lo scanner controlla anche soglie intermedie:

- discese: -5%, -8%, -10%, -15%
- rimbalzi: +5%, +10%, +15%, +20%
- spike: +5%, +10%, +15%, +20%
- dump: 0%, -5%, -8%, -10%, -15%

---

# Bitcoin — BTC

## Lettura semplice

- BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +17,65% (3/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.236 $ | 17/40 | +42,50% | +5,00% | 66.576 $ | 4/17 | +23,53% | +10,53% | DEBOLE | 7,4 | 15,2 |
| -5,00% | 60.236 $ | 17/40 | +42,50% | +10,00% | 69.747 $ | 3/17 | +17,65% | +15,79% | DEBOLE | 7,4 | 12,7 |
| -5,00% | 60.236 $ | 17/40 | +42,50% | +15,00% | 72.917 $ | 3/17 | +17,65% | +21,05% | DEBOLE | 7,4 | 15,7 |
| -5,00% | 60.236 $ | 17/40 | +42,50% | +20,00% | 76.087 $ | 3/17 | +17,65% | +26,32% | DEBOLE | 7,4 | 19,7 |
| -8,00% | 58.334 $ | 13/40 | +32,50% | +5,00% | 66.576 $ | 2/13 | +15,38% | +14,13% | DEBOLE | 9,2 | 16,5 |
| -8,00% | 58.334 $ | 13/40 | +32,50% | +10,00% | 69.747 $ | 1/13 | +7,69% | +19,57% | DEBOLE | 9,2 | 8,0 |
| -8,00% | 58.334 $ | 13/40 | +32,50% | +15,00% | 72.917 $ | 1/13 | +7,69% | +25,00% | DEBOLE | 9,2 | 15,0 |
| -8,00% | 58.334 $ | 13/40 | +32,50% | +20,00% | 76.087 $ | 1/13 | +7,69% | +30,43% | DEBOLE | 9,2 | 17,0 |
| -10,00% | 57.065 $ | 11/40 | +27,50% | +5,00% | 66.576 $ | 2/11 | +18,18% | +16,67% | DEBOLE | 11,8 | 16,5 |
| -10,00% | 57.065 $ | 11/40 | +27,50% | +10,00% | 69.747 $ | 1/11 | +9,09% | +22,22% | DEBOLE | 11,8 | 8,0 |
| -10,00% | 57.065 $ | 11/40 | +27,50% | +15,00% | 72.917 $ | 1/11 | +9,09% | +27,78% | DEBOLE | 11,8 | 15,0 |
| -10,00% | 57.065 $ | 11/40 | +27,50% | +20,00% | 76.087 $ | 1/11 | +9,09% | +33,33% | DEBOLE | 11,8 | 17,0 |
| -15,00% | 53.895 $ | 6/40 | +15,00% | +5,00% | 66.576 $ | 1/6 | +16,67% | +23,53% | DEBOLE | 10,3 | 8,0 |
| -15,00% | 53.895 $ | 6/40 | +15,00% | +10,00% | 69.747 $ | 1/6 | +16,67% | +29,41% | DEBOLE | 10,3 | 8,0 |
| -15,00% | 53.895 $ | 6/40 | +15,00% | +15,00% | 72.917 $ | 1/6 | +16,67% | +35,29% | DEBOLE | 10,3 | 15,0 |
| -15,00% | 53.895 $ | 6/40 | +15,00% | +20,00% | 76.087 $ | 1/6 | +16,67% | +41,18% | DEBOLE | 10,3 | 17,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.576 $ | 30/40 | +75,00% | prezzo iniziale | 63.406 $ | 6/30 | +20,00% | -4,76% | DEBOLE | 6,6 | 15,7 |
| +5,00% | 66.576 $ | 30/40 | +75,00% | -5,00% | 60.236 $ | 3/30 | +10,00% | -9,52% | DEBOLE | 6,6 | 17,0 |
| +5,00% | 66.576 $ | 30/40 | +75,00% | -8,00% | 58.334 $ | 3/30 | +10,00% | -12,38% | DEBOLE | 6,6 | 18,0 |
| +5,00% | 66.576 $ | 30/40 | +75,00% | -10,00% | 57.065 $ | 3/30 | +10,00% | -14,29% | DEBOLE | 6,6 | 19,3 |
| +5,00% | 66.576 $ | 30/40 | +75,00% | -15,00% | 53.895 $ | 1/30 | +3,33% | -19,05% | DEBOLE | 6,6 | 12,0 |
| +10,00% | 69.747 $ | 23/40 | +57,50% | prezzo iniziale | 63.406 $ | 2/23 | +8,70% | -9,09% | DEBOLE | 11,0 | 20,5 |
| +10,00% | 69.747 $ | 23/40 | +57,50% | -5,00% | 60.236 $ | 0/23 | 0,00% | -13,64% | DEBOLE | 11,0 | n/d |
| +10,00% | 69.747 $ | 23/40 | +57,50% | -8,00% | 58.334 $ | 0/23 | 0,00% | -16,36% | DEBOLE | 11,0 | n/d |
| +10,00% | 69.747 $ | 23/40 | +57,50% | -10,00% | 57.065 $ | 0/23 | 0,00% | -18,18% | DEBOLE | 11,0 | n/d |
| +10,00% | 69.747 $ | 23/40 | +57,50% | -15,00% | 53.895 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 11,0 | n/d |
| +15,00% | 72.917 $ | 20/40 | +50,00% | prezzo iniziale | 63.406 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 14,7 | 28,0 |
| +15,00% | 72.917 $ | 20/40 | +50,00% | -5,00% | 60.236 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 14,7 | n/d |
| +15,00% | 72.917 $ | 20/40 | +50,00% | -8,00% | 58.334 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 14,7 | n/d |
| +15,00% | 72.917 $ | 20/40 | +50,00% | -10,00% | 57.065 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 14,7 | n/d |
| +15,00% | 72.917 $ | 20/40 | +50,00% | -15,00% | 53.895 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 14,7 | n/d |
| +20,00% | 76.087 $ | 16/40 | +40,00% | prezzo iniziale | 63.406 $ | 0/16 | 0,00% | -16,67% | DEBOLE | 16,5 | n/d |
| +20,00% | 76.087 $ | 16/40 | +40,00% | -5,00% | 60.236 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 16,5 | n/d |
| +20,00% | 76.087 $ | 16/40 | +40,00% | -8,00% | 58.334 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 16,5 | n/d |
| +20,00% | 76.087 $ | 16/40 | +40,00% | -10,00% | 57.065 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 16,5 | n/d |
| +20,00% | 76.087 $ | 16/40 | +40,00% | -15,00% | 53.895 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 16,5 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 20 prima sono scesi a -5,00%. Tra quei 20, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +25,00% (5/20). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 69,75 $ | 20/40 | +50,00% | +5,00% | 77,09 $ | 7/20 | +35,00% | +10,53% | BASSA | 8,4 | 16,1 |
| -5,00% | 69,75 $ | 20/40 | +50,00% | +10,00% | 80,76 $ | 5/20 | +25,00% | +15,79% | DEBOLE | 8,4 | 14,8 |
| -5,00% | 69,75 $ | 20/40 | +50,00% | +15,00% | 84,43 $ | 4/20 | +20,00% | +21,05% | DEBOLE | 8,4 | 18,0 |
| -5,00% | 69,75 $ | 20/40 | +50,00% | +20,00% | 88,10 $ | 4/20 | +20,00% | +26,32% | DEBOLE | 8,4 | 18,5 |
| -8,00% | 67,55 $ | 16/40 | +40,00% | +5,00% | 77,09 $ | 3/16 | +18,75% | +14,13% | DEBOLE | 9,4 | 19,3 |
| -8,00% | 67,55 $ | 16/40 | +40,00% | +10,00% | 80,76 $ | 2/16 | +12,50% | +19,57% | DEBOLE | 9,4 | 15,5 |
| -8,00% | 67,55 $ | 16/40 | +40,00% | +15,00% | 84,43 $ | 1/16 | +6,25% | +25,00% | DEBOLE | 9,4 | 18,0 |
| -8,00% | 67,55 $ | 16/40 | +40,00% | +20,00% | 88,10 $ | 1/16 | +6,25% | +30,43% | DEBOLE | 9,4 | 18,0 |
| -10,00% | 66,08 $ | 15/40 | +37,50% | +5,00% | 77,09 $ | 3/15 | +20,00% | +16,67% | DEBOLE | 10,4 | 19,3 |
| -10,00% | 66,08 $ | 15/40 | +37,50% | +10,00% | 80,76 $ | 2/15 | +13,33% | +22,22% | DEBOLE | 10,4 | 15,5 |
| -10,00% | 66,08 $ | 15/40 | +37,50% | +15,00% | 84,43 $ | 1/15 | +6,67% | +27,78% | DEBOLE | 10,4 | 18,0 |
| -10,00% | 66,08 $ | 15/40 | +37,50% | +20,00% | 88,10 $ | 1/15 | +6,67% | +33,33% | DEBOLE | 10,4 | 18,0 |
| -15,00% | 62,41 $ | 6/40 | +15,00% | +5,00% | 77,09 $ | 0/6 | 0,00% | +23,53% | DEBOLE | 13,2 | n/d |
| -15,00% | 62,41 $ | 6/40 | +15,00% | +10,00% | 80,76 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 13,2 | n/d |
| -15,00% | 62,41 $ | 6/40 | +15,00% | +15,00% | 84,43 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 13,2 | n/d |
| -15,00% | 62,41 $ | 6/40 | +15,00% | +20,00% | 88,10 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 13,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,09 $ | 31/40 | +77,50% | prezzo iniziale | 73,42 $ | 9/31 | +29,03% | -4,76% | DEBOLE | 7,4 | 9,8 |
| +5,00% | 77,09 $ | 31/40 | +77,50% | -5,00% | 69,75 $ | 7/31 | +22,58% | -9,52% | DEBOLE | 7,4 | 12,4 |
| +5,00% | 77,09 $ | 31/40 | +77,50% | -8,00% | 67,55 $ | 4/31 | +12,90% | -12,38% | DEBOLE | 7,4 | 16,8 |
| +5,00% | 77,09 $ | 31/40 | +77,50% | -10,00% | 66,08 $ | 3/31 | +9,68% | -14,29% | DEBOLE | 7,4 | 18,3 |
| +5,00% | 77,09 $ | 31/40 | +77,50% | -15,00% | 62,41 $ | 0/31 | 0,00% | -19,05% | DEBOLE | 7,4 | n/d |
| +10,00% | 80,76 $ | 24/40 | +60,00% | prezzo iniziale | 73,42 $ | 0/24 | 0,00% | -9,09% | DEBOLE | 10,5 | n/d |
| +10,00% | 80,76 $ | 24/40 | +60,00% | -5,00% | 69,75 $ | 0/24 | 0,00% | -13,64% | DEBOLE | 10,5 | n/d |
| +10,00% | 80,76 $ | 24/40 | +60,00% | -8,00% | 67,55 $ | 0/24 | 0,00% | -16,36% | DEBOLE | 10,5 | n/d |
| +10,00% | 80,76 $ | 24/40 | +60,00% | -10,00% | 66,08 $ | 0/24 | 0,00% | -18,18% | DEBOLE | 10,5 | n/d |
| +10,00% | 80,76 $ | 24/40 | +60,00% | -15,00% | 62,41 $ | 0/24 | 0,00% | -22,73% | DEBOLE | 10,5 | n/d |
| +15,00% | 84,43 $ | 19/40 | +47,50% | prezzo iniziale | 73,42 $ | 0/19 | 0,00% | -13,04% | DEBOLE | 14,4 | n/d |
| +15,00% | 84,43 $ | 19/40 | +47,50% | -5,00% | 69,75 $ | 0/19 | 0,00% | -17,39% | DEBOLE | 14,4 | n/d |
| +15,00% | 84,43 $ | 19/40 | +47,50% | -8,00% | 67,55 $ | 0/19 | 0,00% | -20,00% | DEBOLE | 14,4 | n/d |
| +15,00% | 84,43 $ | 19/40 | +47,50% | -10,00% | 66,08 $ | 0/19 | 0,00% | -21,74% | DEBOLE | 14,4 | n/d |
| +15,00% | 84,43 $ | 19/40 | +47,50% | -15,00% | 62,41 $ | 0/19 | 0,00% | -26,09% | DEBOLE | 14,4 | n/d |
| +20,00% | 88,10 $ | 14/40 | +35,00% | prezzo iniziale | 73,42 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 17,4 | n/d |
| +20,00% | 88,10 $ | 14/40 | +35,00% | -5,00% | 69,75 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 17,4 | n/d |
| +20,00% | 88,10 $ | 14/40 | +35,00% | -8,00% | 67,55 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 17,4 | n/d |
| +20,00% | 88,10 $ | 14/40 | +35,00% | -10,00% | 66,08 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 17,4 | n/d |
| +20,00% | 88,10 $ | 14/40 | +35,00% | -15,00% | 62,41 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 17,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +37,93% (11/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 8 poi sono scaricati a -5,00%. Percentuale: +29,63% (8/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06663 $ | 29/40 | +72,50% | +5,00% | 0,07365 $ | 16/29 | +55,17% | +10,53% | MEDIA | 6,8 | 21,1 |
| -5,00% | 0,06663 $ | 29/40 | +72,50% | +10,00% | 0,07715 $ | 11/29 | +37,93% | +15,79% | BASSA | 6,8 | 21,5 |
| -5,00% | 0,06663 $ | 29/40 | +72,50% | +15,00% | 0,08066 $ | 9/29 | +31,03% | +21,05% | DEBOLE | 6,8 | 21,4 |
| -5,00% | 0,06663 $ | 29/40 | +72,50% | +20,00% | 0,08417 $ | 3/29 | +10,34% | +26,32% | DEBOLE | 6,8 | 19,3 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +5,00% | 0,07365 $ | 12/24 | +50,00% | +14,13% | MEDIA | 7,4 | 22,6 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +10,00% | 0,07715 $ | 8/24 | +33,33% | +19,57% | DEBOLE | 7,4 | 22,4 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +15,00% | 0,08066 $ | 6/24 | +25,00% | +25,00% | DEBOLE | 7,4 | 21,7 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +20,00% | 0,08417 $ | 2/24 | +8,33% | +30,43% | DEBOLE | 7,4 | 21,0 |
| -10,00% | 0,06313 $ | 21/40 | +52,50% | +5,00% | 0,07365 $ | 9/21 | +42,86% | +16,67% | BASSA | 7,9 | 23,1 |
| -10,00% | 0,06313 $ | 21/40 | +52,50% | +10,00% | 0,07715 $ | 5/21 | +23,81% | +22,22% | DEBOLE | 7,9 | 23,0 |
| -10,00% | 0,06313 $ | 21/40 | +52,50% | +15,00% | 0,08066 $ | 4/21 | +19,05% | +27,78% | DEBOLE | 7,9 | 23,8 |
| -10,00% | 0,06313 $ | 21/40 | +52,50% | +20,00% | 0,08417 $ | 0/21 | 0,00% | +33,33% | DEBOLE | 7,9 | n/d |
| -15,00% | 0,05962 $ | 14/40 | +35,00% | +5,00% | 0,07365 $ | 3/14 | +21,43% | +23,53% | DEBOLE | 12,0 | 24,3 |
| -15,00% | 0,05962 $ | 14/40 | +35,00% | +10,00% | 0,07715 $ | 1/14 | +7,14% | +29,41% | DEBOLE | 12,0 | 23,0 |
| -15,00% | 0,05962 $ | 14/40 | +35,00% | +15,00% | 0,08066 $ | 1/14 | +7,14% | +35,29% | DEBOLE | 12,0 | 24,0 |
| -15,00% | 0,05962 $ | 14/40 | +35,00% | +20,00% | 0,08417 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 12,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07365 $ | 35/40 | +87,50% | prezzo iniziale | 0,07014 $ | 23/35 | +65,71% | -4,76% | ALTA | 8,5 | 14,4 |
| +5,00% | 0,07365 $ | 35/40 | +87,50% | -5,00% | 0,06663 $ | 15/35 | +42,86% | -9,52% | BASSA | 8,5 | 12,4 |
| +5,00% | 0,07365 $ | 35/40 | +87,50% | -8,00% | 0,06453 $ | 11/35 | +31,43% | -12,38% | DEBOLE | 8,5 | 11,1 |
| +5,00% | 0,07365 $ | 35/40 | +87,50% | -10,00% | 0,06313 $ | 9/35 | +25,71% | -14,29% | DEBOLE | 8,5 | 10,9 |
| +5,00% | 0,07365 $ | 35/40 | +87,50% | -15,00% | 0,05962 $ | 7/35 | +20,00% | -19,05% | DEBOLE | 8,5 | 13,0 |
| +10,00% | 0,07715 $ | 27/40 | +67,50% | prezzo iniziale | 0,07014 $ | 12/27 | +44,44% | -9,09% | BASSA | 10,9 | 15,9 |
| +10,00% | 0,07715 $ | 27/40 | +67,50% | -5,00% | 0,06663 $ | 8/27 | +29,63% | -13,64% | DEBOLE | 10,9 | 15,8 |
| +10,00% | 0,07715 $ | 27/40 | +67,50% | -8,00% | 0,06453 $ | 5/27 | +18,52% | -16,36% | DEBOLE | 10,9 | 13,4 |
| +10,00% | 0,07715 $ | 27/40 | +67,50% | -10,00% | 0,06313 $ | 4/27 | +14,81% | -18,18% | DEBOLE | 10,9 | 11,2 |
| +10,00% | 0,07715 $ | 27/40 | +67,50% | -15,00% | 0,05962 $ | 4/27 | +14,81% | -22,73% | DEBOLE | 10,9 | 14,0 |
| +15,00% | 0,08066 $ | 21/40 | +52,50% | prezzo iniziale | 0,07014 $ | 8/21 | +38,10% | -13,04% | BASSA | 11,8 | 18,9 |
| +15,00% | 0,08066 $ | 21/40 | +52,50% | -5,00% | 0,06663 $ | 5/21 | +23,81% | -17,39% | DEBOLE | 11,8 | 19,0 |
| +15,00% | 0,08066 $ | 21/40 | +52,50% | -8,00% | 0,06453 $ | 2/21 | +9,52% | -20,00% | DEBOLE | 11,8 | 17,0 |
| +15,00% | 0,08066 $ | 21/40 | +52,50% | -10,00% | 0,06313 $ | 1/21 | +4,76% | -21,74% | DEBOLE | 11,8 | 11,0 |
| +15,00% | 0,08066 $ | 21/40 | +52,50% | -15,00% | 0,05962 $ | 1/21 | +4,76% | -26,09% | DEBOLE | 11,8 | 11,0 |
| +20,00% | 0,08417 $ | 14/40 | +35,00% | prezzo iniziale | 0,07014 $ | 4/14 | +28,57% | -16,67% | DEBOLE | 10,5 | 17,8 |
| +20,00% | 0,08417 $ | 14/40 | +35,00% | -5,00% | 0,06663 $ | 2/14 | +14,29% | -20,83% | DEBOLE | 10,5 | 21,5 |
| +20,00% | 0,08417 $ | 14/40 | +35,00% | -8,00% | 0,06453 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 10,5 | n/d |
| +20,00% | 0,08417 $ | 14/40 | +35,00% | -10,00% | 0,06313 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 10,5 | n/d |
| +20,00% | 0,08417 $ | 14/40 | +35,00% | -15,00% | 0,05962 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 10,5 | n/d |

---
