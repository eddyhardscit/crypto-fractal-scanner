# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-14 07:32:09 CEST**  
UTC: **2026-10-14 05:32:09 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.348 $ | 91.877 $ | +33,33% | +15,79% | rimbalzo poco frequente | 91.877 $ | 79.348 $ | +28,00% | -13,64% | spike storicamente più resistente |
| SOL | 102,01 $ | 118,12 $ | +44,00% | +15,79% | rimbalzo debole | 118,12 $ | 102,01 $ | +19,35% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08056 $ | 0,09328 $ | +50,00% | +15,79% | rimbalzo possibile | 0,09328 $ | 0,08056 $ | +13,89% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (10/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 7 poi sono scaricati a -5,00%. Percentuale: +28,00% (7/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 79.348 $ | 30/40 | +75,00% | +5,00% | 87.701 $ | 14/30 | +46,67% | +10,53% | BASSA | 9,0 | 16,1 |
| -5,00% | 79.348 $ | 30/40 | +75,00% | +10,00% | 91.877 $ | 10/30 | +33,33% | +15,79% | DEBOLE | 9,0 | 17,1 |
| -5,00% | 79.348 $ | 30/40 | +75,00% | +15,00% | 96.053 $ | 9/30 | +30,00% | +21,05% | DEBOLE | 9,0 | 18,3 |
| -5,00% | 79.348 $ | 30/40 | +75,00% | +20,00% | 100.229 $ | 7/30 | +23,33% | +26,32% | DEBOLE | 9,0 | 21,7 |
| -8,00% | 76.842 $ | 24/40 | +60,00% | +5,00% | 87.701 $ | 10/24 | +41,67% | +14,13% | BASSA | 10,1 | 17,3 |
| -8,00% | 76.842 $ | 24/40 | +60,00% | +10,00% | 91.877 $ | 7/24 | +29,17% | +19,57% | DEBOLE | 10,1 | 16,4 |
| -8,00% | 76.842 $ | 24/40 | +60,00% | +15,00% | 96.053 $ | 6/24 | +25,00% | +25,00% | DEBOLE | 10,1 | 17,5 |
| -8,00% | 76.842 $ | 24/40 | +60,00% | +20,00% | 100.229 $ | 5/24 | +20,83% | +30,43% | DEBOLE | 10,1 | 22,8 |
| -10,00% | 75.172 $ | 20/40 | +50,00% | +5,00% | 87.701 $ | 7/20 | +35,00% | +16,67% | BASSA | 10,5 | 17,7 |
| -10,00% | 75.172 $ | 20/40 | +50,00% | +10,00% | 91.877 $ | 5/20 | +25,00% | +22,22% | DEBOLE | 10,5 | 17,0 |
| -10,00% | 75.172 $ | 20/40 | +50,00% | +15,00% | 96.053 $ | 4/20 | +20,00% | +27,78% | DEBOLE | 10,5 | 17,8 |
| -10,00% | 75.172 $ | 20/40 | +50,00% | +20,00% | 100.229 $ | 3/20 | +15,00% | +33,33% | DEBOLE | 10,5 | 18,3 |
| -15,00% | 70.996 $ | 16/40 | +40,00% | +5,00% | 87.701 $ | 3/16 | +18,75% | +23,53% | DEBOLE | 14,8 | 23,7 |
| -15,00% | 70.996 $ | 16/40 | +40,00% | +10,00% | 91.877 $ | 2/16 | +12,50% | +29,41% | DEBOLE | 14,8 | 21,0 |
| -15,00% | 70.996 $ | 16/40 | +40,00% | +15,00% | 96.053 $ | 1/16 | +6,25% | +35,29% | DEBOLE | 14,8 | 26,0 |
| -15,00% | 70.996 $ | 16/40 | +40,00% | +20,00% | 100.229 $ | 0/16 | 0,00% | +41,18% | DEBOLE | 14,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 87.701 $ | 32/40 | +80,00% | prezzo iniziale | 83.524 $ | 20/32 | +62,50% | -4,76% | MEDIA | 7,0 | 13,8 |
| +5,00% | 87.701 $ | 32/40 | +80,00% | -5,00% | 79.348 $ | 15/32 | +46,88% | -9,52% | BASSA | 7,0 | 16,1 |
| +5,00% | 87.701 $ | 32/40 | +80,00% | -8,00% | 76.842 $ | 10/32 | +31,25% | -12,38% | DEBOLE | 7,0 | 15,7 |
| +5,00% | 87.701 $ | 32/40 | +80,00% | -10,00% | 75.172 $ | 8/32 | +25,00% | -14,29% | DEBOLE | 7,0 | 14,0 |
| +5,00% | 87.701 $ | 32/40 | +80,00% | -15,00% | 70.996 $ | 7/32 | +21,88% | -19,05% | DEBOLE | 7,0 | 15,6 |
| +10,00% | 91.877 $ | 25/40 | +62,50% | prezzo iniziale | 83.524 $ | 12/25 | +48,00% | -9,09% | BASSA | 10,0 | 19,9 |
| +10,00% | 91.877 $ | 25/40 | +62,50% | -5,00% | 79.348 $ | 7/25 | +28,00% | -13,64% | DEBOLE | 10,0 | 20,7 |
| +10,00% | 91.877 $ | 25/40 | +62,50% | -8,00% | 76.842 $ | 5/25 | +20,00% | -16,36% | DEBOLE | 10,0 | 21,6 |
| +10,00% | 91.877 $ | 25/40 | +62,50% | -10,00% | 75.172 $ | 3/25 | +12,00% | -18,18% | DEBOLE | 10,0 | 20,3 |
| +10,00% | 91.877 $ | 25/40 | +62,50% | -15,00% | 70.996 $ | 1/25 | +4,00% | -22,73% | DEBOLE | 10,0 | 17,0 |
| +15,00% | 96.053 $ | 17/40 | +42,50% | prezzo iniziale | 83.524 $ | 4/17 | +23,53% | -13,04% | DEBOLE | 12,4 | 22,0 |
| +15,00% | 96.053 $ | 17/40 | +42,50% | -5,00% | 79.348 $ | 1/17 | +5,88% | -17,39% | DEBOLE | 12,4 | 30,0 |
| +15,00% | 96.053 $ | 17/40 | +42,50% | -8,00% | 76.842 $ | 1/17 | +5,88% | -20,00% | DEBOLE | 12,4 | 30,0 |
| +15,00% | 96.053 $ | 17/40 | +42,50% | -10,00% | 75.172 $ | 0/17 | 0,00% | -21,74% | DEBOLE | 12,4 | n/d |
| +15,00% | 96.053 $ | 17/40 | +42,50% | -15,00% | 70.996 $ | 0/17 | 0,00% | -26,09% | DEBOLE | 12,4 | n/d |
| +20,00% | 100.229 $ | 12/40 | +30,00% | prezzo iniziale | 83.524 $ | 2/12 | +16,67% | -16,67% | DEBOLE | 16,0 | 28,5 |
| +20,00% | 100.229 $ | 12/40 | +30,00% | -5,00% | 79.348 $ | 1/12 | +8,33% | -20,83% | DEBOLE | 16,0 | 30,0 |
| +20,00% | 100.229 $ | 12/40 | +30,00% | -8,00% | 76.842 $ | 1/12 | +8,33% | -23,33% | DEBOLE | 16,0 | 30,0 |
| +20,00% | 100.229 $ | 12/40 | +30,00% | -10,00% | 75.172 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 16,0 | n/d |
| +20,00% | 100.229 $ | 12/40 | +30,00% | -15,00% | 70.996 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 16,0 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +44,00% (11/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 6 poi sono scaricati a -5,00%. Percentuale: +19,35% (6/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 102,01 $ | 25/40 | +62,50% | +5,00% | 112,75 $ | 16/25 | +64,00% | +10,53% | MEDIA | 6,5 | 14,1 |
| -5,00% | 102,01 $ | 25/40 | +62,50% | +10,00% | 118,12 $ | 11/25 | +44,00% | +15,79% | BASSA | 6,5 | 12,0 |
| -5,00% | 102,01 $ | 25/40 | +62,50% | +15,00% | 123,49 $ | 10/25 | +40,00% | +21,05% | BASSA | 6,5 | 13,3 |
| -5,00% | 102,01 $ | 25/40 | +62,50% | +20,00% | 128,86 $ | 9/25 | +36,00% | +26,32% | BASSA | 6,5 | 19,3 |
| -8,00% | 98,79 $ | 18/40 | +45,00% | +5,00% | 112,75 $ | 10/18 | +55,56% | +14,13% | MEDIA | 9,3 | 16,7 |
| -8,00% | 98,79 $ | 18/40 | +45,00% | +10,00% | 118,12 $ | 6/18 | +33,33% | +19,57% | DEBOLE | 9,3 | 13,5 |
| -8,00% | 98,79 $ | 18/40 | +45,00% | +15,00% | 123,49 $ | 5/18 | +27,78% | +25,00% | DEBOLE | 9,3 | 16,0 |
| -8,00% | 98,79 $ | 18/40 | +45,00% | +20,00% | 128,86 $ | 5/18 | +27,78% | +30,43% | DEBOLE | 9,3 | 24,4 |
| -10,00% | 96,64 $ | 12/40 | +30,00% | +5,00% | 112,75 $ | 4/12 | +33,33% | +16,67% | DEBOLE | 11,9 | 18,5 |
| -10,00% | 96,64 $ | 12/40 | +30,00% | +10,00% | 118,12 $ | 2/12 | +16,67% | +22,22% | DEBOLE | 11,9 | 16,0 |
| -10,00% | 96,64 $ | 12/40 | +30,00% | +15,00% | 123,49 $ | 2/12 | +16,67% | +27,78% | DEBOLE | 11,9 | 16,0 |
| -10,00% | 96,64 $ | 12/40 | +30,00% | +20,00% | 128,86 $ | 2/12 | +16,67% | +33,33% | DEBOLE | 11,9 | 20,5 |
| -15,00% | 91,27 $ | 9/40 | +22,50% | +5,00% | 112,75 $ | 1/9 | +11,11% | +23,53% | DEBOLE | 16,2 | 30,0 |
| -15,00% | 91,27 $ | 9/40 | +22,50% | +10,00% | 118,12 $ | 0/9 | 0,00% | +29,41% | DEBOLE | 16,2 | n/d |
| -15,00% | 91,27 $ | 9/40 | +22,50% | +15,00% | 123,49 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 16,2 | n/d |
| -15,00% | 91,27 $ | 9/40 | +22,50% | +20,00% | 128,86 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 16,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 112,75 $ | 36/40 | +90,00% | prezzo iniziale | 107,38 $ | 17/36 | +47,22% | -4,76% | BASSA | 5,5 | 13,3 |
| +5,00% | 112,75 $ | 36/40 | +90,00% | -5,00% | 102,01 $ | 11/36 | +30,56% | -9,52% | DEBOLE | 5,5 | 14,6 |
| +5,00% | 112,75 $ | 36/40 | +90,00% | -8,00% | 98,79 $ | 8/36 | +22,22% | -12,38% | DEBOLE | 5,5 | 14,9 |
| +5,00% | 112,75 $ | 36/40 | +90,00% | -10,00% | 96,64 $ | 6/36 | +16,67% | -14,29% | DEBOLE | 5,5 | 15,8 |
| +5,00% | 112,75 $ | 36/40 | +90,00% | -15,00% | 91,27 $ | 5/36 | +13,89% | -19,05% | DEBOLE | 5,5 | 19,0 |
| +10,00% | 118,12 $ | 31/40 | +77,50% | prezzo iniziale | 107,38 $ | 11/31 | +35,48% | -9,09% | BASSA | 7,8 | 19,3 |
| +10,00% | 118,12 $ | 31/40 | +77,50% | -5,00% | 102,01 $ | 6/31 | +19,35% | -13,64% | DEBOLE | 7,8 | 18,7 |
| +10,00% | 118,12 $ | 31/40 | +77,50% | -8,00% | 98,79 $ | 4/31 | +12,90% | -16,36% | DEBOLE | 7,8 | 18,0 |
| +10,00% | 118,12 $ | 31/40 | +77,50% | -10,00% | 96,64 $ | 2/31 | +6,45% | -18,18% | DEBOLE | 7,8 | 17,5 |
| +10,00% | 118,12 $ | 31/40 | +77,50% | -15,00% | 91,27 $ | 2/31 | +6,45% | -22,73% | DEBOLE | 7,8 | 19,5 |
| +15,00% | 123,49 $ | 24/40 | +60,00% | prezzo iniziale | 107,38 $ | 4/24 | +16,67% | -13,04% | DEBOLE | 9,5 | 23,0 |
| +15,00% | 123,49 $ | 24/40 | +60,00% | -5,00% | 102,01 $ | 1/24 | +4,17% | -17,39% | DEBOLE | 9,5 | 26,0 |
| +15,00% | 123,49 $ | 24/40 | +60,00% | -8,00% | 98,79 $ | 1/24 | +4,17% | -20,00% | DEBOLE | 9,5 | 27,0 |
| +15,00% | 123,49 $ | 24/40 | +60,00% | -10,00% | 96,64 $ | 1/24 | +4,17% | -21,74% | DEBOLE | 9,5 | 28,0 |
| +15,00% | 123,49 $ | 24/40 | +60,00% | -15,00% | 91,27 $ | 1/24 | +4,17% | -26,09% | DEBOLE | 9,5 | 28,0 |
| +20,00% | 128,86 $ | 17/40 | +42,50% | prezzo iniziale | 107,38 $ | 0/17 | 0,00% | -16,67% | DEBOLE | 14,3 | n/d |
| +20,00% | 128,86 $ | 17/40 | +42,50% | -5,00% | 102,01 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 14,3 | n/d |
| +20,00% | 128,86 $ | 17/40 | +42,50% | -8,00% | 98,79 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 14,3 | n/d |
| +20,00% | 128,86 $ | 17/40 | +42,50% | -10,00% | 96,64 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 14,3 | n/d |
| +20,00% | 128,86 $ | 17/40 | +42,50% | -15,00% | 91,27 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 14,3 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (9/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 36 prima sono saliti a +10,00%. Tra quei 36, 5 poi sono scaricati a -5,00%. Percentuale: +13,89% (5/36). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,08056 $ | 18/40 | +45,00% | +5,00% | 0,08904 $ | 12/18 | +66,67% | +10,53% | ALTA | 6,4 | 11,5 |
| -5,00% | 0,08056 $ | 18/40 | +45,00% | +10,00% | 0,09328 $ | 9/18 | +50,00% | +15,79% | MEDIA | 6,4 | 11,9 |
| -5,00% | 0,08056 $ | 18/40 | +45,00% | +15,00% | 0,09752 $ | 8/18 | +44,44% | +21,05% | BASSA | 6,4 | 13,2 |
| -5,00% | 0,08056 $ | 18/40 | +45,00% | +20,00% | 0,10176 $ | 7/18 | +38,89% | +26,32% | BASSA | 6,4 | 16,1 |
| -8,00% | 0,07802 $ | 11/40 | +27,50% | +5,00% | 0,08904 $ | 6/11 | +54,55% | +14,13% | MEDIA | 9,0 | 14,8 |
| -8,00% | 0,07802 $ | 11/40 | +27,50% | +10,00% | 0,09328 $ | 4/11 | +36,36% | +19,57% | BASSA | 9,0 | 13,2 |
| -8,00% | 0,07802 $ | 11/40 | +27,50% | +15,00% | 0,09752 $ | 3/11 | +27,27% | +25,00% | DEBOLE | 9,0 | 16,0 |
| -8,00% | 0,07802 $ | 11/40 | +27,50% | +20,00% | 0,10176 $ | 3/11 | +27,27% | +30,43% | DEBOLE | 9,0 | 22,0 |
| -10,00% | 0,07632 $ | 8/40 | +20,00% | +5,00% | 0,08904 $ | 3/8 | +37,50% | +16,67% | BASSA | 12,6 | 20,0 |
| -10,00% | 0,07632 $ | 8/40 | +20,00% | +10,00% | 0,09328 $ | 1/8 | +12,50% | +22,22% | DEBOLE | 12,6 | 15,0 |
| -10,00% | 0,07632 $ | 8/40 | +20,00% | +15,00% | 0,09752 $ | 1/8 | +12,50% | +27,78% | DEBOLE | 12,6 | 15,0 |
| -10,00% | 0,07632 $ | 8/40 | +20,00% | +20,00% | 0,10176 $ | 1/8 | +12,50% | +33,33% | DEBOLE | 12,6 | 15,0 |
| -15,00% | 0,07208 $ | 6/40 | +15,00% | +5,00% | 0,08904 $ | 1/6 | +16,67% | +23,53% | DEBOLE | 15,3 | 30,0 |
| -15,00% | 0,07208 $ | 6/40 | +15,00% | +10,00% | 0,09328 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 15,3 | n/d |
| -15,00% | 0,07208 $ | 6/40 | +15,00% | +15,00% | 0,09752 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 15,3 | n/d |
| -15,00% | 0,07208 $ | 6/40 | +15,00% | +20,00% | 0,10176 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 15,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08904 $ | 40/40 | +100,00% | prezzo iniziale | 0,08480 $ | 15/40 | +37,50% | -4,76% | BASSA | 5,1 | 12,7 |
| +5,00% | 0,08904 $ | 40/40 | +100,00% | -5,00% | 0,08056 $ | 9/40 | +22,50% | -9,52% | DEBOLE | 5,1 | 14,2 |
| +5,00% | 0,08904 $ | 40/40 | +100,00% | -8,00% | 0,07802 $ | 6/40 | +15,00% | -12,38% | DEBOLE | 5,1 | 13,2 |
| +5,00% | 0,08904 $ | 40/40 | +100,00% | -10,00% | 0,07632 $ | 6/40 | +15,00% | -14,29% | DEBOLE | 5,1 | 13,3 |
| +5,00% | 0,08904 $ | 40/40 | +100,00% | -15,00% | 0,07208 $ | 5/40 | +12,50% | -19,05% | DEBOLE | 5,1 | 14,0 |
| +10,00% | 0,09328 $ | 36/40 | +90,00% | prezzo iniziale | 0,08480 $ | 10/36 | +27,78% | -9,09% | DEBOLE | 6,5 | 17,4 |
| +10,00% | 0,09328 $ | 36/40 | +90,00% | -5,00% | 0,08056 $ | 5/36 | +13,89% | -13,64% | DEBOLE | 6,5 | 13,8 |
| +10,00% | 0,09328 $ | 36/40 | +90,00% | -8,00% | 0,07802 $ | 3/36 | +8,33% | -16,36% | DEBOLE | 6,5 | 10,3 |
| +10,00% | 0,09328 $ | 36/40 | +90,00% | -10,00% | 0,07632 $ | 3/36 | +8,33% | -18,18% | DEBOLE | 6,5 | 10,3 |
| +10,00% | 0,09328 $ | 36/40 | +90,00% | -15,00% | 0,07208 $ | 2/36 | +5,56% | -22,73% | DEBOLE | 6,5 | 9,5 |
| +15,00% | 0,09752 $ | 28/40 | +70,00% | prezzo iniziale | 0,08480 $ | 3/28 | +10,71% | -13,04% | DEBOLE | 8,6 | 22,7 |
| +15,00% | 0,09752 $ | 28/40 | +70,00% | -5,00% | 0,08056 $ | 0/28 | 0,00% | -17,39% | DEBOLE | 8,6 | n/d |
| +15,00% | 0,09752 $ | 28/40 | +70,00% | -8,00% | 0,07802 $ | 0/28 | 0,00% | -20,00% | DEBOLE | 8,6 | n/d |
| +15,00% | 0,09752 $ | 28/40 | +70,00% | -10,00% | 0,07632 $ | 0/28 | 0,00% | -21,74% | DEBOLE | 8,6 | n/d |
| +15,00% | 0,09752 $ | 28/40 | +70,00% | -15,00% | 0,07208 $ | 0/28 | 0,00% | -26,09% | DEBOLE | 8,6 | n/d |
| +20,00% | 0,10176 $ | 22/40 | +55,00% | prezzo iniziale | 0,08480 $ | 0/22 | 0,00% | -16,67% | DEBOLE | 12,0 | n/d |
| +20,00% | 0,10176 $ | 22/40 | +55,00% | -5,00% | 0,08056 $ | 0/22 | 0,00% | -20,83% | DEBOLE | 12,0 | n/d |
| +20,00% | 0,10176 $ | 22/40 | +55,00% | -8,00% | 0,07802 $ | 0/22 | 0,00% | -23,33% | DEBOLE | 12,0 | n/d |
| +20,00% | 0,10176 $ | 22/40 | +55,00% | -10,00% | 0,07632 $ | 0/22 | 0,00% | -25,00% | DEBOLE | 12,0 | n/d |
| +20,00% | 0,10176 $ | 22/40 | +55,00% | -15,00% | 0,07208 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 12,0 | n/d |

---
