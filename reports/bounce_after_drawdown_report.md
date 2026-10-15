# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-15 07:32:46 CEST**  
UTC: **2026-10-15 05:32:46 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.945 $ | 89.094 $ | +32,14% | +15,79% | rimbalzo poco frequente | 89.094 $ | 76.945 $ | +24,00% | -13,64% | spike storicamente più resistente |
| SOL | 97,10 $ | 112,43 $ | +33,33% | +15,79% | rimbalzo poco frequente | 112,43 $ | 97,10 $ | +25,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07581 $ | 0,08778 $ | +31,25% | +15,79% | rimbalzo poco frequente | 0,08778 $ | 0,07581 $ | +14,71% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +32,14% (9/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 6 poi sono scaricati a -5,00%. Percentuale: +24,00% (6/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 76.945 $ | 28/40 | +70,00% | +5,00% | 85.045 $ | 13/28 | +46,43% | +10,53% | BASSA | 7,5 | 16,2 |
| -5,00% | 76.945 $ | 28/40 | +70,00% | +10,00% | 89.094 $ | 9/28 | +32,14% | +15,79% | DEBOLE | 7,5 | 16,6 |
| -5,00% | 76.945 $ | 28/40 | +70,00% | +15,00% | 93.144 $ | 8/28 | +28,57% | +21,05% | DEBOLE | 7,5 | 17,4 |
| -5,00% | 76.945 $ | 28/40 | +70,00% | +20,00% | 97.194 $ | 6/28 | +21,43% | +26,32% | DEBOLE | 7,5 | 17,8 |
| -8,00% | 74.515 $ | 22/40 | +55,00% | +5,00% | 85.045 $ | 8/22 | +36,36% | +14,13% | BASSA | 8,8 | 19,0 |
| -8,00% | 74.515 $ | 22/40 | +55,00% | +10,00% | 89.094 $ | 5/22 | +22,73% | +19,57% | DEBOLE | 8,8 | 17,4 |
| -8,00% | 74.515 $ | 22/40 | +55,00% | +15,00% | 93.144 $ | 4/22 | +18,18% | +25,00% | DEBOLE | 8,8 | 18,2 |
| -8,00% | 74.515 $ | 22/40 | +55,00% | +20,00% | 97.194 $ | 3/22 | +13,64% | +30,43% | DEBOLE | 8,8 | 19,3 |
| -10,00% | 72.895 $ | 20/40 | +50,00% | +5,00% | 85.045 $ | 6/20 | +30,00% | +16,67% | DEBOLE | 9,7 | 18,3 |
| -10,00% | 72.895 $ | 20/40 | +50,00% | +10,00% | 89.094 $ | 4/20 | +20,00% | +22,22% | DEBOLE | 9,7 | 17,0 |
| -10,00% | 72.895 $ | 20/40 | +50,00% | +15,00% | 93.144 $ | 3/20 | +15,00% | +27,78% | DEBOLE | 9,7 | 18,0 |
| -10,00% | 72.895 $ | 20/40 | +50,00% | +20,00% | 97.194 $ | 2/20 | +10,00% | +33,33% | DEBOLE | 9,7 | 14,5 |
| -15,00% | 68.846 $ | 17/40 | +42,50% | +5,00% | 85.045 $ | 3/17 | +17,65% | +23,53% | DEBOLE | 13,0 | 23,7 |
| -15,00% | 68.846 $ | 17/40 | +42,50% | +10,00% | 89.094 $ | 2/17 | +11,76% | +29,41% | DEBOLE | 13,0 | 21,0 |
| -15,00% | 68.846 $ | 17/40 | +42,50% | +15,00% | 93.144 $ | 1/17 | +5,88% | +35,29% | DEBOLE | 13,0 | 26,0 |
| -15,00% | 68.846 $ | 17/40 | +42,50% | +20,00% | 97.194 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 13,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 85.045 $ | 30/40 | +75,00% | prezzo iniziale | 80.995 $ | 16/30 | +53,33% | -4,76% | MEDIA | 6,6 | 13,7 |
| +5,00% | 85.045 $ | 30/40 | +75,00% | -5,00% | 76.945 $ | 12/30 | +40,00% | -9,52% | BASSA | 6,6 | 14,8 |
| +5,00% | 85.045 $ | 30/40 | +75,00% | -8,00% | 74.515 $ | 8/30 | +26,67% | -12,38% | DEBOLE | 6,6 | 14,2 |
| +5,00% | 85.045 $ | 30/40 | +75,00% | -10,00% | 72.895 $ | 7/30 | +23,33% | -14,29% | DEBOLE | 6,6 | 13,9 |
| +5,00% | 85.045 $ | 30/40 | +75,00% | -15,00% | 68.846 $ | 6/30 | +20,00% | -19,05% | DEBOLE | 6,6 | 15,0 |
| +10,00% | 89.094 $ | 25/40 | +62,50% | prezzo iniziale | 80.995 $ | 10/25 | +40,00% | -9,09% | BASSA | 8,6 | 18,5 |
| +10,00% | 89.094 $ | 25/40 | +62,50% | -5,00% | 76.945 $ | 6/25 | +24,00% | -13,64% | DEBOLE | 8,6 | 16,5 |
| +10,00% | 89.094 $ | 25/40 | +62,50% | -8,00% | 74.515 $ | 5/25 | +20,00% | -16,36% | DEBOLE | 8,6 | 17,0 |
| +10,00% | 89.094 $ | 25/40 | +62,50% | -10,00% | 72.895 $ | 4/25 | +16,00% | -18,18% | DEBOLE | 8,6 | 17,0 |
| +10,00% | 89.094 $ | 25/40 | +62,50% | -15,00% | 68.846 $ | 2/25 | +8,00% | -22,73% | DEBOLE | 8,6 | 12,5 |
| +15,00% | 93.144 $ | 18/40 | +45,00% | prezzo iniziale | 80.995 $ | 3/18 | +16,67% | -13,04% | DEBOLE | 10,7 | 24,3 |
| +15,00% | 93.144 $ | 18/40 | +45,00% | -5,00% | 76.945 $ | 0/18 | 0,00% | -17,39% | DEBOLE | 10,7 | n/d |
| +15,00% | 93.144 $ | 18/40 | +45,00% | -8,00% | 74.515 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 10,7 | n/d |
| +15,00% | 93.144 $ | 18/40 | +45,00% | -10,00% | 72.895 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 10,7 | n/d |
| +15,00% | 93.144 $ | 18/40 | +45,00% | -15,00% | 68.846 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 10,7 | n/d |
| +20,00% | 97.194 $ | 13/40 | +32,50% | prezzo iniziale | 80.995 $ | 1/13 | +7,69% | -16,67% | DEBOLE | 11,8 | 30,0 |
| +20,00% | 97.194 $ | 13/40 | +32,50% | -5,00% | 76.945 $ | 0/13 | 0,00% | -20,83% | DEBOLE | 11,8 | n/d |
| +20,00% | 97.194 $ | 13/40 | +32,50% | -8,00% | 74.515 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 11,8 | n/d |
| +20,00% | 97.194 $ | 13/40 | +32,50% | -10,00% | 72.895 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 11,8 | n/d |
| +20,00% | 97.194 $ | 13/40 | +32,50% | -15,00% | 68.846 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 11,8 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (7/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 8 poi sono scaricati a -5,00%. Percentuale: +25,00% (8/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 97,10 $ | 21/40 | +52,50% | +5,00% | 107,32 $ | 13/21 | +61,90% | +10,53% | MEDIA | 8,5 | 18,5 |
| -5,00% | 97,10 $ | 21/40 | +52,50% | +10,00% | 112,43 $ | 7/21 | +33,33% | +15,79% | DEBOLE | 8,5 | 15,6 |
| -5,00% | 97,10 $ | 21/40 | +52,50% | +15,00% | 117,54 $ | 7/21 | +33,33% | +21,05% | DEBOLE | 8,5 | 16,1 |
| -5,00% | 97,10 $ | 21/40 | +52,50% | +20,00% | 122,65 $ | 6/21 | +28,57% | +26,32% | DEBOLE | 8,5 | 16,8 |
| -8,00% | 94,03 $ | 13/40 | +32,50% | +5,00% | 107,32 $ | 7/13 | +53,85% | +14,13% | MEDIA | 11,8 | 22,6 |
| -8,00% | 94,03 $ | 13/40 | +32,50% | +10,00% | 112,43 $ | 3/13 | +23,08% | +19,57% | DEBOLE | 11,8 | 20,3 |
| -8,00% | 94,03 $ | 13/40 | +32,50% | +15,00% | 117,54 $ | 3/13 | +23,08% | +25,00% | DEBOLE | 11,8 | 20,3 |
| -8,00% | 94,03 $ | 13/40 | +32,50% | +20,00% | 122,65 $ | 2/13 | +15,38% | +30,43% | DEBOLE | 11,8 | 22,0 |
| -10,00% | 91,99 $ | 10/40 | +25,00% | +5,00% | 107,32 $ | 4/10 | +40,00% | +16,67% | BASSA | 14,4 | 21,5 |
| -10,00% | 91,99 $ | 10/40 | +25,00% | +10,00% | 112,43 $ | 2/10 | +20,00% | +22,22% | DEBOLE | 14,4 | 21,0 |
| -10,00% | 91,99 $ | 10/40 | +25,00% | +15,00% | 117,54 $ | 2/10 | +20,00% | +27,78% | DEBOLE | 14,4 | 21,0 |
| -10,00% | 91,99 $ | 10/40 | +25,00% | +20,00% | 122,65 $ | 1/10 | +10,00% | +33,33% | DEBOLE | 14,4 | 15,0 |
| -15,00% | 86,88 $ | 6/40 | +15,00% | +5,00% | 107,32 $ | 1/6 | +16,67% | +23,53% | DEBOLE | 18,5 | 30,0 |
| -15,00% | 86,88 $ | 6/40 | +15,00% | +10,00% | 112,43 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 18,5 | n/d |
| -15,00% | 86,88 $ | 6/40 | +15,00% | +15,00% | 117,54 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 18,5 | n/d |
| -15,00% | 86,88 $ | 6/40 | +15,00% | +20,00% | 122,65 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 18,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 107,32 $ | 39/40 | +97,50% | prezzo iniziale | 102,21 $ | 19/39 | +48,72% | -4,76% | BASSA | 5,2 | 13,6 |
| +5,00% | 107,32 $ | 39/40 | +97,50% | -5,00% | 97,10 $ | 14/39 | +35,90% | -9,52% | BASSA | 5,2 | 14,7 |
| +5,00% | 107,32 $ | 39/40 | +97,50% | -8,00% | 94,03 $ | 10/39 | +25,64% | -12,38% | DEBOLE | 5,2 | 14,1 |
| +5,00% | 107,32 $ | 39/40 | +97,50% | -10,00% | 91,99 $ | 8/39 | +20,51% | -14,29% | DEBOLE | 5,2 | 15,4 |
| +5,00% | 107,32 $ | 39/40 | +97,50% | -15,00% | 86,88 $ | 5/39 | +12,82% | -19,05% | DEBOLE | 5,2 | 17,8 |
| +10,00% | 112,43 $ | 32/40 | +80,00% | prezzo iniziale | 102,21 $ | 12/32 | +37,50% | -9,09% | BASSA | 6,7 | 18,4 |
| +10,00% | 112,43 $ | 32/40 | +80,00% | -5,00% | 97,10 $ | 8/32 | +25,00% | -13,64% | DEBOLE | 6,7 | 18,2 |
| +10,00% | 112,43 $ | 32/40 | +80,00% | -8,00% | 94,03 $ | 5/32 | +15,62% | -16,36% | DEBOLE | 6,7 | 16,0 |
| +10,00% | 112,43 $ | 32/40 | +80,00% | -10,00% | 91,99 $ | 3/32 | +9,38% | -18,18% | DEBOLE | 6,7 | 14,0 |
| +10,00% | 112,43 $ | 32/40 | +80,00% | -15,00% | 86,88 $ | 1/32 | +3,12% | -22,73% | DEBOLE | 6,7 | 11,0 |
| +15,00% | 117,54 $ | 24/40 | +60,00% | prezzo iniziale | 102,21 $ | 4/24 | +16,67% | -13,04% | DEBOLE | 9,5 | 24,5 |
| +15,00% | 117,54 $ | 24/40 | +60,00% | -5,00% | 97,10 $ | 1/24 | +4,17% | -17,39% | DEBOLE | 9,5 | 27,0 |
| +15,00% | 117,54 $ | 24/40 | +60,00% | -8,00% | 94,03 $ | 0/24 | 0,00% | -20,00% | DEBOLE | 9,5 | n/d |
| +15,00% | 117,54 $ | 24/40 | +60,00% | -10,00% | 91,99 $ | 0/24 | 0,00% | -21,74% | DEBOLE | 9,5 | n/d |
| +15,00% | 117,54 $ | 24/40 | +60,00% | -15,00% | 86,88 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 9,5 | n/d |
| +20,00% | 122,65 $ | 17/40 | +42,50% | prezzo iniziale | 102,21 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 11,5 | 25,0 |
| +20,00% | 122,65 $ | 17/40 | +42,50% | -5,00% | 97,10 $ | 1/17 | +5,88% | -20,83% | DEBOLE | 11,5 | 27,0 |
| +20,00% | 122,65 $ | 17/40 | +42,50% | -8,00% | 94,03 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 11,5 | n/d |
| +20,00% | 122,65 $ | 17/40 | +42,50% | -10,00% | 91,99 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 11,5 | n/d |
| +20,00% | 122,65 $ | 17/40 | +42,50% | -15,00% | 86,88 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 11,5 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +31,25% (5/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 34 prima sono saliti a +10,00%. Tra quei 34, 5 poi sono scaricati a -5,00%. Percentuale: +14,71% (5/34). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07581 $ | 16/40 | +40,00% | +5,00% | 0,08379 $ | 10/16 | +62,50% | +10,53% | MEDIA | 6,2 | 17,5 |
| -5,00% | 0,07581 $ | 16/40 | +40,00% | +10,00% | 0,08778 $ | 5/16 | +31,25% | +15,79% | DEBOLE | 6,2 | 17,8 |
| -5,00% | 0,07581 $ | 16/40 | +40,00% | +15,00% | 0,09177 $ | 4/16 | +25,00% | +21,05% | DEBOLE | 6,2 | 15,8 |
| -5,00% | 0,07581 $ | 16/40 | +40,00% | +20,00% | 0,09576 $ | 4/16 | +25,00% | +26,32% | DEBOLE | 6,2 | 19,5 |
| -8,00% | 0,07342 $ | 12/40 | +30,00% | +5,00% | 0,08379 $ | 6/12 | +50,00% | +14,13% | MEDIA | 9,2 | 18,5 |
| -8,00% | 0,07342 $ | 12/40 | +30,00% | +10,00% | 0,08778 $ | 3/12 | +25,00% | +19,57% | DEBOLE | 9,2 | 20,7 |
| -8,00% | 0,07342 $ | 12/40 | +30,00% | +15,00% | 0,09177 $ | 2/12 | +16,67% | +25,00% | DEBOLE | 9,2 | 17,0 |
| -8,00% | 0,07342 $ | 12/40 | +30,00% | +20,00% | 0,09576 $ | 2/12 | +16,67% | +30,43% | DEBOLE | 9,2 | 22,0 |
| -10,00% | 0,07182 $ | 9/40 | +22,50% | +5,00% | 0,08379 $ | 4/9 | +44,44% | +16,67% | BASSA | 11,8 | 22,0 |
| -10,00% | 0,07182 $ | 9/40 | +22,50% | +10,00% | 0,08778 $ | 2/9 | +22,22% | +22,22% | DEBOLE | 11,8 | 21,5 |
| -10,00% | 0,07182 $ | 9/40 | +22,50% | +15,00% | 0,09177 $ | 1/9 | +11,11% | +27,78% | DEBOLE | 11,8 | 15,0 |
| -10,00% | 0,07182 $ | 9/40 | +22,50% | +20,00% | 0,09576 $ | 1/9 | +11,11% | +33,33% | DEBOLE | 11,8 | 15,0 |
| -15,00% | 0,06783 $ | 6/40 | +15,00% | +5,00% | 0,08379 $ | 2/6 | +33,33% | +23,53% | DEBOLE | 14,5 | 29,0 |
| -15,00% | 0,06783 $ | 6/40 | +15,00% | +10,00% | 0,08778 $ | 1/6 | +16,67% | +29,41% | DEBOLE | 14,5 | 28,0 |
| -15,00% | 0,06783 $ | 6/40 | +15,00% | +15,00% | 0,09177 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 14,5 | n/d |
| -15,00% | 0,06783 $ | 6/40 | +15,00% | +20,00% | 0,09576 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 14,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08379 $ | 39/40 | +97,50% | prezzo iniziale | 0,07980 $ | 13/39 | +33,33% | -4,76% | DEBOLE | 6,0 | 15,6 |
| +5,00% | 0,08379 $ | 39/40 | +97,50% | -5,00% | 0,07581 $ | 8/39 | +20,51% | -9,52% | DEBOLE | 6,0 | 14,6 |
| +5,00% | 0,08379 $ | 39/40 | +97,50% | -8,00% | 0,07342 $ | 7/39 | +17,95% | -12,38% | DEBOLE | 6,0 | 15,4 |
| +5,00% | 0,08379 $ | 39/40 | +97,50% | -10,00% | 0,07182 $ | 5/39 | +12,82% | -14,29% | DEBOLE | 6,0 | 13,4 |
| +5,00% | 0,08379 $ | 39/40 | +97,50% | -15,00% | 0,06783 $ | 4/39 | +10,26% | -19,05% | DEBOLE | 6,0 | 14,2 |
| +10,00% | 0,08778 $ | 34/40 | +85,00% | prezzo iniziale | 0,07980 $ | 9/34 | +26,47% | -9,09% | DEBOLE | 6,4 | 16,9 |
| +10,00% | 0,08778 $ | 34/40 | +85,00% | -5,00% | 0,07581 $ | 5/34 | +14,71% | -13,64% | DEBOLE | 6,4 | 13,4 |
| +10,00% | 0,08778 $ | 34/40 | +85,00% | -8,00% | 0,07342 $ | 4/34 | +11,76% | -16,36% | DEBOLE | 6,4 | 12,8 |
| +10,00% | 0,08778 $ | 34/40 | +85,00% | -10,00% | 0,07182 $ | 3/34 | +8,82% | -18,18% | DEBOLE | 6,4 | 10,3 |
| +10,00% | 0,08778 $ | 34/40 | +85,00% | -15,00% | 0,06783 $ | 2/34 | +5,88% | -22,73% | DEBOLE | 6,4 | 9,5 |
| +15,00% | 0,09177 $ | 26/40 | +65,00% | prezzo iniziale | 0,07980 $ | 2/26 | +7,69% | -13,04% | DEBOLE | 7,5 | 21,5 |
| +15,00% | 0,09177 $ | 26/40 | +65,00% | -5,00% | 0,07581 $ | 0/26 | 0,00% | -17,39% | DEBOLE | 7,5 | n/d |
| +15,00% | 0,09177 $ | 26/40 | +65,00% | -8,00% | 0,07342 $ | 0/26 | 0,00% | -20,00% | DEBOLE | 7,5 | n/d |
| +15,00% | 0,09177 $ | 26/40 | +65,00% | -10,00% | 0,07182 $ | 0/26 | 0,00% | -21,74% | DEBOLE | 7,5 | n/d |
| +15,00% | 0,09177 $ | 26/40 | +65,00% | -15,00% | 0,06783 $ | 0/26 | 0,00% | -26,09% | DEBOLE | 7,5 | n/d |
| +20,00% | 0,09576 $ | 20/40 | +50,00% | prezzo iniziale | 0,07980 $ | 0/20 | 0,00% | -16,67% | DEBOLE | 11,6 | n/d |
| +20,00% | 0,09576 $ | 20/40 | +50,00% | -5,00% | 0,07581 $ | 0/20 | 0,00% | -20,83% | DEBOLE | 11,6 | n/d |
| +20,00% | 0,09576 $ | 20/40 | +50,00% | -8,00% | 0,07342 $ | 0/20 | 0,00% | -23,33% | DEBOLE | 11,6 | n/d |
| +20,00% | 0,09576 $ | 20/40 | +50,00% | -10,00% | 0,07182 $ | 0/20 | 0,00% | -25,00% | DEBOLE | 11,6 | n/d |
| +20,00% | 0,09576 $ | 20/40 | +50,00% | -15,00% | 0,06783 $ | 0/20 | 0,00% | -29,17% | DEBOLE | 11,6 | n/d |

---
