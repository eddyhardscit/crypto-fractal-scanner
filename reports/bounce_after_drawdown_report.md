# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-14 13:43:56 CEST**  
UTC: **2026-07-14 11:43:56 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.630 $ | 69.045 $ | +35,00% | +15,79% | rimbalzo debole | 69.045 $ | 59.630 $ | +20,83% | -13,64% | spike storicamente più resistente |
| SOL | 71,57 $ | 82,87 $ | +13,79% | +15,79% | rimbalzo poco frequente | 82,87 $ | 71,57 $ | +29,41% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06859 $ | 0,07942 $ | +11,76% | +15,79% | rimbalzo poco frequente | 0,07942 $ | 0,06859 $ | +42,86% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 20 prima sono scesi a -5,00%. Tra quei 20, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +35,00% (7/20). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 5 poi sono scaricati a -5,00%. Percentuale: +20,83% (5/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.630 $ | 20/40 | +50,00% | +5,00% | 65.907 $ | 9/20 | +45,00% | +10,53% | BASSA | 8,7 | 20,8 |
| -5,00% | 59.630 $ | 20/40 | +50,00% | +10,00% | 69.045 $ | 7/20 | +35,00% | +15,79% | BASSA | 8,7 | 23,0 |
| -5,00% | 59.630 $ | 20/40 | +50,00% | +15,00% | 72.183 $ | 4/20 | +20,00% | +21,05% | DEBOLE | 8,7 | 24,2 |
| -5,00% | 59.630 $ | 20/40 | +50,00% | +20,00% | 75.322 $ | 4/20 | +20,00% | +26,32% | DEBOLE | 8,7 | 25,0 |
| -8,00% | 57.747 $ | 16/40 | +40,00% | +5,00% | 65.907 $ | 5/16 | +31,25% | +14,13% | DEBOLE | 11,1 | 21,6 |
| -8,00% | 57.747 $ | 16/40 | +40,00% | +10,00% | 69.045 $ | 3/16 | +18,75% | +19,57% | DEBOLE | 11,1 | 19,7 |
| -8,00% | 57.747 $ | 16/40 | +40,00% | +15,00% | 72.183 $ | 2/16 | +12,50% | +25,00% | DEBOLE | 11,1 | 20,5 |
| -8,00% | 57.747 $ | 16/40 | +40,00% | +20,00% | 75.322 $ | 2/16 | +12,50% | +30,43% | DEBOLE | 11,1 | 21,0 |
| -10,00% | 56.491 $ | 13/40 | +32,50% | +5,00% | 65.907 $ | 3/13 | +23,08% | +16,67% | DEBOLE | 10,7 | 22,3 |
| -10,00% | 56.491 $ | 13/40 | +32,50% | +10,00% | 69.045 $ | 2/13 | +15,38% | +22,22% | DEBOLE | 10,7 | 22,0 |
| -10,00% | 56.491 $ | 13/40 | +32,50% | +15,00% | 72.183 $ | 1/13 | +7,69% | +27,78% | DEBOLE | 10,7 | 26,0 |
| -10,00% | 56.491 $ | 13/40 | +32,50% | +20,00% | 75.322 $ | 1/13 | +7,69% | +33,33% | DEBOLE | 10,7 | 26,0 |
| -15,00% | 53.353 $ | 9/40 | +22,50% | +5,00% | 65.907 $ | 0/9 | 0,00% | +23,53% | DEBOLE | 14,8 | n/d |
| -15,00% | 53.353 $ | 9/40 | +22,50% | +10,00% | 69.045 $ | 0/9 | 0,00% | +29,41% | DEBOLE | 14,8 | n/d |
| -15,00% | 53.353 $ | 9/40 | +22,50% | +15,00% | 72.183 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 14,8 | n/d |
| -15,00% | 53.353 $ | 9/40 | +22,50% | +20,00% | 75.322 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 14,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.907 $ | 33/40 | +82,50% | prezzo iniziale | 62.768 $ | 23/33 | +69,70% | -4,76% | ALTA | 4,9 | 12,8 |
| +5,00% | 65.907 $ | 33/40 | +82,50% | -5,00% | 59.630 $ | 12/33 | +36,36% | -9,52% | BASSA | 4,9 | 13,4 |
| +5,00% | 65.907 $ | 33/40 | +82,50% | -8,00% | 57.747 $ | 8/33 | +24,24% | -12,38% | DEBOLE | 4,9 | 13,2 |
| +5,00% | 65.907 $ | 33/40 | +82,50% | -10,00% | 56.491 $ | 6/33 | +18,18% | -14,29% | DEBOLE | 4,9 | 13,0 |
| +5,00% | 65.907 $ | 33/40 | +82,50% | -15,00% | 53.353 $ | 4/33 | +12,12% | -19,05% | DEBOLE | 4,9 | 18,8 |
| +10,00% | 69.045 $ | 24/40 | +60,00% | prezzo iniziale | 62.768 $ | 9/24 | +37,50% | -9,09% | BASSA | 10,3 | 10,8 |
| +10,00% | 69.045 $ | 24/40 | +60,00% | -5,00% | 59.630 $ | 5/24 | +20,83% | -13,64% | DEBOLE | 10,3 | 10,6 |
| +10,00% | 69.045 $ | 24/40 | +60,00% | -8,00% | 57.747 $ | 4/24 | +16,67% | -16,36% | DEBOLE | 10,3 | 13,8 |
| +10,00% | 69.045 $ | 24/40 | +60,00% | -10,00% | 56.491 $ | 3/24 | +12,50% | -18,18% | DEBOLE | 10,3 | 14,3 |
| +10,00% | 69.045 $ | 24/40 | +60,00% | -15,00% | 53.353 $ | 1/24 | +4,17% | -22,73% | DEBOLE | 10,3 | 12,0 |
| +15,00% | 72.183 $ | 18/40 | +45,00% | prezzo iniziale | 62.768 $ | 3/18 | +16,67% | -13,04% | DEBOLE | 13,0 | 13,7 |
| +15,00% | 72.183 $ | 18/40 | +45,00% | -5,00% | 59.630 $ | 0/18 | 0,00% | -17,39% | DEBOLE | 13,0 | n/d |
| +15,00% | 72.183 $ | 18/40 | +45,00% | -8,00% | 57.747 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 13,0 | n/d |
| +15,00% | 72.183 $ | 18/40 | +45,00% | -10,00% | 56.491 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 13,0 | n/d |
| +15,00% | 72.183 $ | 18/40 | +45,00% | -15,00% | 53.353 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 13,0 | n/d |
| +20,00% | 75.322 $ | 16/40 | +40,00% | prezzo iniziale | 62.768 $ | 1/16 | +6,25% | -16,67% | DEBOLE | 14,7 | 7,0 |
| +20,00% | 75.322 $ | 16/40 | +40,00% | -5,00% | 59.630 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 14,7 | n/d |
| +20,00% | 75.322 $ | 16/40 | +40,00% | -8,00% | 57.747 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 14,7 | n/d |
| +20,00% | 75.322 $ | 16/40 | +40,00% | -10,00% | 56.491 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 14,7 | n/d |
| +20,00% | 75.322 $ | 16/40 | +40,00% | -15,00% | 53.353 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 14,7 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +13,79% (4/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 5 poi sono scaricati a -5,00%. Percentuale: +29,41% (5/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,57 $ | 29/40 | +72,50% | +5,00% | 79,11 $ | 8/29 | +27,59% | +10,53% | DEBOLE | 7,2 | 23,5 |
| -5,00% | 71,57 $ | 29/40 | +72,50% | +10,00% | 82,87 $ | 4/29 | +13,79% | +15,79% | DEBOLE | 7,2 | 21,2 |
| -5,00% | 71,57 $ | 29/40 | +72,50% | +15,00% | 86,64 $ | 4/29 | +13,79% | +21,05% | DEBOLE | 7,2 | 21,5 |
| -5,00% | 71,57 $ | 29/40 | +72,50% | +20,00% | 90,41 $ | 2/29 | +6,90% | +26,32% | DEBOLE | 7,2 | 23,0 |
| -8,00% | 69,31 $ | 25/40 | +62,50% | +5,00% | 79,11 $ | 3/25 | +12,00% | +14,13% | DEBOLE | 9,7 | 23,3 |
| -8,00% | 69,31 $ | 25/40 | +62,50% | +10,00% | 82,87 $ | 2/25 | +8,00% | +19,57% | DEBOLE | 9,7 | 22,0 |
| -8,00% | 69,31 $ | 25/40 | +62,50% | +15,00% | 86,64 $ | 2/25 | +8,00% | +25,00% | DEBOLE | 9,7 | 22,0 |
| -8,00% | 69,31 $ | 25/40 | +62,50% | +20,00% | 90,41 $ | 2/25 | +8,00% | +30,43% | DEBOLE | 9,7 | 23,0 |
| -10,00% | 67,81 $ | 20/40 | +50,00% | +5,00% | 79,11 $ | 1/20 | +5,00% | +16,67% | DEBOLE | 9,7 | 29,0 |
| -10,00% | 67,81 $ | 20/40 | +50,00% | +10,00% | 82,87 $ | 0/20 | 0,00% | +22,22% | DEBOLE | 9,7 | n/d |
| -10,00% | 67,81 $ | 20/40 | +50,00% | +15,00% | 86,64 $ | 0/20 | 0,00% | +27,78% | DEBOLE | 9,7 | n/d |
| -10,00% | 67,81 $ | 20/40 | +50,00% | +20,00% | 90,41 $ | 0/20 | 0,00% | +33,33% | DEBOLE | 9,7 | n/d |
| -15,00% | 64,04 $ | 14/40 | +35,00% | +5,00% | 79,11 $ | 0/14 | 0,00% | +23,53% | DEBOLE | 11,1 | n/d |
| -15,00% | 64,04 $ | 14/40 | +35,00% | +10,00% | 82,87 $ | 0/14 | 0,00% | +29,41% | DEBOLE | 11,1 | n/d |
| -15,00% | 64,04 $ | 14/40 | +35,00% | +15,00% | 86,64 $ | 0/14 | 0,00% | +35,29% | DEBOLE | 11,1 | n/d |
| -15,00% | 64,04 $ | 14/40 | +35,00% | +20,00% | 90,41 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 11,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,11 $ | 24/40 | +60,00% | prezzo iniziale | 75,34 $ | 13/24 | +54,17% | -4,76% | MEDIA | 5,9 | 10,2 |
| +5,00% | 79,11 $ | 24/40 | +60,00% | -5,00% | 71,57 $ | 11/24 | +45,83% | -9,52% | BASSA | 5,9 | 11,3 |
| +5,00% | 79,11 $ | 24/40 | +60,00% | -8,00% | 69,31 $ | 9/24 | +37,50% | -12,38% | BASSA | 5,9 | 15,8 |
| +5,00% | 79,11 $ | 24/40 | +60,00% | -10,00% | 67,81 $ | 6/24 | +25,00% | -14,29% | DEBOLE | 5,9 | 15,7 |
| +5,00% | 79,11 $ | 24/40 | +60,00% | -15,00% | 64,04 $ | 4/24 | +16,67% | -19,05% | DEBOLE | 5,9 | 22,2 |
| +10,00% | 82,87 $ | 17/40 | +42,50% | prezzo iniziale | 75,34 $ | 5/17 | +29,41% | -9,09% | DEBOLE | 8,7 | 7,8 |
| +10,00% | 82,87 $ | 17/40 | +42,50% | -5,00% | 71,57 $ | 5/17 | +29,41% | -13,64% | DEBOLE | 8,7 | 8,8 |
| +10,00% | 82,87 $ | 17/40 | +42,50% | -8,00% | 69,31 $ | 5/17 | +29,41% | -16,36% | DEBOLE | 8,7 | 14,6 |
| +10,00% | 82,87 $ | 17/40 | +42,50% | -10,00% | 67,81 $ | 3/17 | +17,65% | -18,18% | DEBOLE | 8,7 | 11,0 |
| +10,00% | 82,87 $ | 17/40 | +42,50% | -15,00% | 64,04 $ | 2/17 | +11,76% | -22,73% | DEBOLE | 8,7 | 20,0 |
| +15,00% | 86,64 $ | 13/40 | +32,50% | prezzo iniziale | 75,34 $ | 1/13 | +7,69% | -13,04% | DEBOLE | 10,4 | 10,0 |
| +15,00% | 86,64 $ | 13/40 | +32,50% | -5,00% | 71,57 $ | 1/13 | +7,69% | -17,39% | DEBOLE | 10,4 | 10,0 |
| +15,00% | 86,64 $ | 13/40 | +32,50% | -8,00% | 69,31 $ | 1/13 | +7,69% | -20,00% | DEBOLE | 10,4 | 30,0 |
| +15,00% | 86,64 $ | 13/40 | +32,50% | -10,00% | 67,81 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 10,4 | n/d |
| +15,00% | 86,64 $ | 13/40 | +32,50% | -15,00% | 64,04 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,41 $ | 10/40 | +25,00% | prezzo iniziale | 75,34 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 9,9 | 10,0 |
| +20,00% | 90,41 $ | 10/40 | +25,00% | -5,00% | 71,57 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 9,9 | 10,0 |
| +20,00% | 90,41 $ | 10/40 | +25,00% | -8,00% | 69,31 $ | 1/10 | +10,00% | -23,33% | DEBOLE | 9,9 | 30,0 |
| +20,00% | 90,41 $ | 10/40 | +25,00% | -10,00% | 67,81 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 9,9 | n/d |
| +20,00% | 90,41 $ | 10/40 | +25,00% | -15,00% | 64,04 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 9,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +11,76% (4/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 14 prima sono saliti a +10,00%. Tra quei 14, 6 poi sono scaricati a -5,00%. Percentuale: +42,86% (6/14). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06859 $ | 34/40 | +85,00% | +5,00% | 0,07581 $ | 5/34 | +14,71% | +10,53% | DEBOLE | 5,3 | 14,8 |
| -5,00% | 0,06859 $ | 34/40 | +85,00% | +10,00% | 0,07942 $ | 4/34 | +11,76% | +15,79% | DEBOLE | 5,3 | 12,5 |
| -5,00% | 0,06859 $ | 34/40 | +85,00% | +15,00% | 0,08303 $ | 2/34 | +5,88% | +21,05% | DEBOLE | 5,3 | 9,0 |
| -5,00% | 0,06859 $ | 34/40 | +85,00% | +20,00% | 0,08664 $ | 2/34 | +5,88% | +26,32% | DEBOLE | 5,3 | 11,0 |
| -8,00% | 0,06642 $ | 34/40 | +85,00% | +5,00% | 0,07581 $ | 5/34 | +14,71% | +14,13% | DEBOLE | 6,2 | 14,8 |
| -8,00% | 0,06642 $ | 34/40 | +85,00% | +10,00% | 0,07942 $ | 4/34 | +11,76% | +19,57% | DEBOLE | 6,2 | 12,5 |
| -8,00% | 0,06642 $ | 34/40 | +85,00% | +15,00% | 0,08303 $ | 2/34 | +5,88% | +25,00% | DEBOLE | 6,2 | 9,0 |
| -8,00% | 0,06642 $ | 34/40 | +85,00% | +20,00% | 0,08664 $ | 2/34 | +5,88% | +30,43% | DEBOLE | 6,2 | 11,0 |
| -10,00% | 0,06498 $ | 31/40 | +77,50% | +5,00% | 0,07581 $ | 2/31 | +6,45% | +16,67% | DEBOLE | 6,8 | 18,0 |
| -10,00% | 0,06498 $ | 31/40 | +77,50% | +10,00% | 0,07942 $ | 2/31 | +6,45% | +22,22% | DEBOLE | 6,8 | 18,5 |
| -10,00% | 0,06498 $ | 31/40 | +77,50% | +15,00% | 0,08303 $ | 0/31 | 0,00% | +27,78% | DEBOLE | 6,8 | n/d |
| -10,00% | 0,06498 $ | 31/40 | +77,50% | +20,00% | 0,08664 $ | 0/31 | 0,00% | +33,33% | DEBOLE | 6,8 | n/d |
| -15,00% | 0,06137 $ | 30/40 | +75,00% | +5,00% | 0,07581 $ | 2/30 | +6,67% | +23,53% | DEBOLE | 8,1 | 18,0 |
| -15,00% | 0,06137 $ | 30/40 | +75,00% | +10,00% | 0,07942 $ | 2/30 | +6,67% | +29,41% | DEBOLE | 8,1 | 18,5 |
| -15,00% | 0,06137 $ | 30/40 | +75,00% | +15,00% | 0,08303 $ | 0/30 | 0,00% | +35,29% | DEBOLE | 8,1 | n/d |
| -15,00% | 0,06137 $ | 30/40 | +75,00% | +20,00% | 0,08664 $ | 0/30 | 0,00% | +41,18% | DEBOLE | 8,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07581 $ | 18/40 | +45,00% | prezzo iniziale | 0,07220 $ | 15/18 | +83,33% | -4,76% | ALTA | 3,0 | 9,7 |
| +5,00% | 0,07581 $ | 18/40 | +45,00% | -5,00% | 0,06859 $ | 11/18 | +61,11% | -9,52% | MEDIA | 3,0 | 9,1 |
| +5,00% | 0,07581 $ | 18/40 | +45,00% | -8,00% | 0,06642 $ | 11/18 | +61,11% | -12,38% | MEDIA | 3,0 | 10,1 |
| +5,00% | 0,07581 $ | 18/40 | +45,00% | -10,00% | 0,06498 $ | 9/18 | +50,00% | -14,29% | MEDIA | 3,0 | 11,4 |
| +5,00% | 0,07581 $ | 18/40 | +45,00% | -15,00% | 0,06137 $ | 8/18 | +44,44% | -19,05% | BASSA | 3,0 | 10,4 |
| +10,00% | 0,07942 $ | 14/40 | +35,00% | prezzo iniziale | 0,07220 $ | 10/14 | +71,43% | -9,09% | ALTA | 9,1 | 14,0 |
| +10,00% | 0,07942 $ | 14/40 | +35,00% | -5,00% | 0,06859 $ | 6/14 | +42,86% | -13,64% | BASSA | 9,1 | 11,8 |
| +10,00% | 0,07942 $ | 14/40 | +35,00% | -8,00% | 0,06642 $ | 6/14 | +42,86% | -16,36% | BASSA | 9,1 | 12,7 |
| +10,00% | 0,07942 $ | 14/40 | +35,00% | -10,00% | 0,06498 $ | 5/14 | +35,71% | -18,18% | BASSA | 9,1 | 14,4 |
| +10,00% | 0,07942 $ | 14/40 | +35,00% | -15,00% | 0,06137 $ | 4/14 | +28,57% | -22,73% | DEBOLE | 9,1 | 13,2 |
| +15,00% | 0,08303 $ | 10/40 | +25,00% | prezzo iniziale | 0,07220 $ | 5/10 | +50,00% | -13,04% | MEDIA | 12,8 | 18,4 |
| +15,00% | 0,08303 $ | 10/40 | +25,00% | -5,00% | 0,06859 $ | 3/10 | +30,00% | -17,39% | DEBOLE | 12,8 | 20,3 |
| +15,00% | 0,08303 $ | 10/40 | +25,00% | -8,00% | 0,06642 $ | 2/10 | +20,00% | -20,00% | DEBOLE | 12,8 | 17,0 |
| +15,00% | 0,08303 $ | 10/40 | +25,00% | -10,00% | 0,06498 $ | 2/10 | +20,00% | -21,74% | DEBOLE | 12,8 | 17,0 |
| +15,00% | 0,08303 $ | 10/40 | +25,00% | -15,00% | 0,06137 $ | 2/10 | +20,00% | -26,09% | DEBOLE | 12,8 | 17,5 |
| +20,00% | 0,08664 $ | 6/40 | +15,00% | prezzo iniziale | 0,07220 $ | 2/6 | +33,33% | -16,67% | DEBOLE | 11,8 | 11,5 |
| +20,00% | 0,08664 $ | 6/40 | +15,00% | -5,00% | 0,06859 $ | 2/6 | +33,33% | -20,83% | DEBOLE | 11,8 | 17,5 |
| +20,00% | 0,08664 $ | 6/40 | +15,00% | -8,00% | 0,06642 $ | 1/6 | +16,67% | -23,33% | DEBOLE | 11,8 | 8,0 |
| +20,00% | 0,08664 $ | 6/40 | +15,00% | -10,00% | 0,06498 $ | 1/6 | +16,67% | -25,00% | DEBOLE | 11,8 | 8,0 |
| +20,00% | 0,08664 $ | 6/40 | +15,00% | -15,00% | 0,06137 $ | 1/6 | +16,67% | -29,17% | DEBOLE | 11,8 | 9,0 |

---
