# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-25 07:14:06 CEST**  
UTC: **2026-07-25 05:14:06 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.887 $ | 70.500 $ | +51,52% | +15,79% | rimbalzo possibile | 70.500 $ | 60.887 $ | +8,33% | -13,64% | spike storicamente più resistente |
| SOL | 70,49 $ | 81,62 $ | +36,67% | +15,79% | rimbalzo debole | 81,62 $ | 70,49 $ | +5,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06610 $ | 0,07654 $ | +40,62% | +15,79% | rimbalzo debole | 0,07654 $ | 0,06610 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 17 poi sono rimbalzati fino a +10,00%. Percentuale: +51,52% (17/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 2 poi sono scaricati a -5,00%. Percentuale: +8,33% (2/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.887 $ | 33/40 | +82,50% | +5,00% | 67.296 $ | 19/33 | +57,58% | +10,53% | MEDIA | 4,9 | 15,6 |
| -5,00% | 60.887 $ | 33/40 | +82,50% | +10,00% | 70.500 $ | 17/33 | +51,52% | +15,79% | MEDIA | 4,9 | 19,1 |
| -5,00% | 60.887 $ | 33/40 | +82,50% | +15,00% | 73.705 $ | 15/33 | +45,45% | +21,05% | BASSA | 4,9 | 22,4 |
| -5,00% | 60.887 $ | 33/40 | +82,50% | +20,00% | 76.909 $ | 12/33 | +36,36% | +26,32% | BASSA | 4,9 | 24,6 |
| -8,00% | 58.964 $ | 21/40 | +52,50% | +5,00% | 67.296 $ | 7/21 | +33,33% | +14,13% | DEBOLE | 8,4 | 16,9 |
| -8,00% | 58.964 $ | 21/40 | +52,50% | +10,00% | 70.500 $ | 6/21 | +28,57% | +19,57% | DEBOLE | 8,4 | 20,5 |
| -8,00% | 58.964 $ | 21/40 | +52,50% | +15,00% | 73.705 $ | 5/21 | +23,81% | +25,00% | DEBOLE | 8,4 | 23,6 |
| -8,00% | 58.964 $ | 21/40 | +52,50% | +20,00% | 76.909 $ | 4/21 | +19,05% | +30,43% | DEBOLE | 8,4 | 27,0 |
| -10,00% | 57.682 $ | 15/40 | +37,50% | +5,00% | 67.296 $ | 2/15 | +13,33% | +16,67% | DEBOLE | 11,0 | 18,5 |
| -10,00% | 57.682 $ | 15/40 | +37,50% | +10,00% | 70.500 $ | 1/15 | +6,67% | +22,22% | DEBOLE | 11,0 | 23,0 |
| -10,00% | 57.682 $ | 15/40 | +37,50% | +15,00% | 73.705 $ | 1/15 | +6,67% | +27,78% | DEBOLE | 11,0 | 25,0 |
| -10,00% | 57.682 $ | 15/40 | +37,50% | +20,00% | 76.909 $ | 1/15 | +6,67% | +33,33% | DEBOLE | 11,0 | 30,0 |
| -15,00% | 54.477 $ | 12/40 | +30,00% | +5,00% | 67.296 $ | 1/12 | +8,33% | +23,53% | DEBOLE | 14,8 | 21,0 |
| -15,00% | 54.477 $ | 12/40 | +30,00% | +10,00% | 70.500 $ | 0/12 | 0,00% | +29,41% | DEBOLE | 14,8 | n/d |
| -15,00% | 54.477 $ | 12/40 | +30,00% | +15,00% | 73.705 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 14,8 | n/d |
| -15,00% | 54.477 $ | 12/40 | +30,00% | +20,00% | 76.909 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 14,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.296 $ | 30/40 | +75,00% | prezzo iniziale | 64.091 $ | 9/30 | +30,00% | -4,76% | DEBOLE | 11,5 | 11,4 |
| +5,00% | 67.296 $ | 30/40 | +75,00% | -5,00% | 60.887 $ | 8/30 | +26,67% | -9,52% | DEBOLE | 11,5 | 13,6 |
| +5,00% | 67.296 $ | 30/40 | +75,00% | -8,00% | 58.964 $ | 7/30 | +23,33% | -12,38% | DEBOLE | 11,5 | 14,9 |
| +5,00% | 67.296 $ | 30/40 | +75,00% | -10,00% | 57.682 $ | 5/30 | +16,67% | -14,29% | DEBOLE | 11,5 | 17,4 |
| +5,00% | 67.296 $ | 30/40 | +75,00% | -15,00% | 54.477 $ | 5/30 | +16,67% | -19,05% | DEBOLE | 11,5 | 19,0 |
| +10,00% | 70.500 $ | 24/40 | +60,00% | prezzo iniziale | 64.091 $ | 2/24 | +8,33% | -9,09% | DEBOLE | 17,0 | 18,5 |
| +10,00% | 70.500 $ | 24/40 | +60,00% | -5,00% | 60.887 $ | 2/24 | +8,33% | -13,64% | DEBOLE | 17,0 | 19,0 |
| +10,00% | 70.500 $ | 24/40 | +60,00% | -8,00% | 58.964 $ | 2/24 | +8,33% | -16,36% | DEBOLE | 17,0 | 19,0 |
| +10,00% | 70.500 $ | 24/40 | +60,00% | -10,00% | 57.682 $ | 2/24 | +8,33% | -18,18% | DEBOLE | 17,0 | 19,0 |
| +10,00% | 70.500 $ | 24/40 | +60,00% | -15,00% | 54.477 $ | 2/24 | +8,33% | -22,73% | DEBOLE | 17,0 | 19,5 |
| +15,00% | 73.705 $ | 22/40 | +55,00% | prezzo iniziale | 64.091 $ | 1/22 | +4,55% | -13,04% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 73.705 $ | 22/40 | +55,00% | -5,00% | 60.887 $ | 1/22 | +4,55% | -17,39% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 73.705 $ | 22/40 | +55,00% | -8,00% | 58.964 $ | 1/22 | +4,55% | -20,00% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 73.705 $ | 22/40 | +55,00% | -10,00% | 57.682 $ | 1/22 | +4,55% | -21,74% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 73.705 $ | 22/40 | +55,00% | -15,00% | 54.477 $ | 1/22 | +4,55% | -26,09% | DEBOLE | 20,4 | 18,0 |
| +20,00% | 76.909 $ | 18/40 | +45,00% | prezzo iniziale | 64.091 $ | 1/18 | +5,56% | -16,67% | DEBOLE | 22,4 | 17,0 |
| +20,00% | 76.909 $ | 18/40 | +45,00% | -5,00% | 60.887 $ | 1/18 | +5,56% | -20,83% | DEBOLE | 22,4 | 17,0 |
| +20,00% | 76.909 $ | 18/40 | +45,00% | -8,00% | 58.964 $ | 1/18 | +5,56% | -23,33% | DEBOLE | 22,4 | 17,0 |
| +20,00% | 76.909 $ | 18/40 | +45,00% | -10,00% | 57.682 $ | 1/18 | +5,56% | -25,00% | DEBOLE | 22,4 | 17,0 |
| +20,00% | 76.909 $ | 18/40 | +45,00% | -15,00% | 54.477 $ | 1/18 | +5,56% | -29,17% | DEBOLE | 22,4 | 18,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +36,67% (11/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 1 poi sono scaricati a -5,00%. Percentuale: +5,00% (1/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 70,49 $ | 30/40 | +75,00% | +5,00% | 77,91 $ | 15/30 | +50,00% | +10,53% | MEDIA | 7,2 | 18,6 |
| -5,00% | 70,49 $ | 30/40 | +75,00% | +10,00% | 81,62 $ | 11/30 | +36,67% | +15,79% | BASSA | 7,2 | 21,2 |
| -5,00% | 70,49 $ | 30/40 | +75,00% | +15,00% | 85,33 $ | 8/30 | +26,67% | +21,05% | DEBOLE | 7,2 | 21,5 |
| -5,00% | 70,49 $ | 30/40 | +75,00% | +20,00% | 89,04 $ | 7/30 | +23,33% | +26,32% | DEBOLE | 7,2 | 22,6 |
| -8,00% | 68,26 $ | 26/40 | +65,00% | +5,00% | 77,91 $ | 11/26 | +42,31% | +14,13% | BASSA | 10,7 | 20,9 |
| -8,00% | 68,26 $ | 26/40 | +65,00% | +10,00% | 81,62 $ | 9/26 | +34,62% | +19,57% | DEBOLE | 10,7 | 22,8 |
| -8,00% | 68,26 $ | 26/40 | +65,00% | +15,00% | 85,33 $ | 7/26 | +26,92% | +25,00% | DEBOLE | 10,7 | 23,9 |
| -8,00% | 68,26 $ | 26/40 | +65,00% | +20,00% | 89,04 $ | 6/26 | +23,08% | +30,43% | DEBOLE | 10,7 | 25,5 |
| -10,00% | 66,78 $ | 16/40 | +40,00% | +5,00% | 77,91 $ | 2/16 | +12,50% | +16,67% | DEBOLE | 14,9 | 24,0 |
| -10,00% | 66,78 $ | 16/40 | +40,00% | +10,00% | 81,62 $ | 2/16 | +12,50% | +22,22% | DEBOLE | 14,9 | 27,5 |
| -10,00% | 66,78 $ | 16/40 | +40,00% | +15,00% | 85,33 $ | 2/16 | +12,50% | +27,78% | DEBOLE | 14,9 | 28,0 |
| -10,00% | 66,78 $ | 16/40 | +40,00% | +20,00% | 89,04 $ | 2/16 | +12,50% | +33,33% | DEBOLE | 14,9 | 28,0 |
| -15,00% | 63,07 $ | 6/40 | +15,00% | +5,00% | 77,91 $ | 0/6 | 0,00% | +23,53% | DEBOLE | 20,7 | n/d |
| -15,00% | 63,07 $ | 6/40 | +15,00% | +10,00% | 81,62 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 20,7 | n/d |
| -15,00% | 63,07 $ | 6/40 | +15,00% | +15,00% | 85,33 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 20,7 | n/d |
| -15,00% | 63,07 $ | 6/40 | +15,00% | +20,00% | 89,04 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 20,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,91 $ | 29/40 | +72,50% | prezzo iniziale | 74,20 $ | 10/29 | +34,48% | -4,76% | DEBOLE | 11,8 | 13,6 |
| +5,00% | 77,91 $ | 29/40 | +72,50% | -5,00% | 70,49 $ | 7/29 | +24,14% | -9,52% | DEBOLE | 11,8 | 14,7 |
| +5,00% | 77,91 $ | 29/40 | +72,50% | -8,00% | 68,26 $ | 6/29 | +20,69% | -12,38% | DEBOLE | 11,8 | 16,2 |
| +5,00% | 77,91 $ | 29/40 | +72,50% | -10,00% | 66,78 $ | 3/29 | +10,34% | -14,29% | DEBOLE | 11,8 | 22,0 |
| +5,00% | 77,91 $ | 29/40 | +72,50% | -15,00% | 63,07 $ | 2/29 | +6,90% | -19,05% | DEBOLE | 11,8 | 22,5 |
| +10,00% | 81,62 $ | 20/40 | +50,00% | prezzo iniziale | 74,20 $ | 1/20 | +5,00% | -9,09% | DEBOLE | 15,6 | 19,0 |
| +10,00% | 81,62 $ | 20/40 | +50,00% | -5,00% | 70,49 $ | 1/20 | +5,00% | -13,64% | DEBOLE | 15,6 | 23,0 |
| +10,00% | 81,62 $ | 20/40 | +50,00% | -8,00% | 68,26 $ | 1/20 | +5,00% | -16,36% | DEBOLE | 15,6 | 24,0 |
| +10,00% | 81,62 $ | 20/40 | +50,00% | -10,00% | 66,78 $ | 1/20 | +5,00% | -18,18% | DEBOLE | 15,6 | 24,0 |
| +10,00% | 81,62 $ | 20/40 | +50,00% | -15,00% | 63,07 $ | 0/20 | 0,00% | -22,73% | DEBOLE | 15,6 | n/d |
| +15,00% | 85,33 $ | 17/40 | +42,50% | prezzo iniziale | 74,20 $ | 1/17 | +5,88% | -13,04% | DEBOLE | 15,8 | 19,0 |
| +15,00% | 85,33 $ | 17/40 | +42,50% | -5,00% | 70,49 $ | 1/17 | +5,88% | -17,39% | DEBOLE | 15,8 | 23,0 |
| +15,00% | 85,33 $ | 17/40 | +42,50% | -8,00% | 68,26 $ | 1/17 | +5,88% | -20,00% | DEBOLE | 15,8 | 24,0 |
| +15,00% | 85,33 $ | 17/40 | +42,50% | -10,00% | 66,78 $ | 1/17 | +5,88% | -21,74% | DEBOLE | 15,8 | 24,0 |
| +15,00% | 85,33 $ | 17/40 | +42,50% | -15,00% | 63,07 $ | 0/17 | 0,00% | -26,09% | DEBOLE | 15,8 | n/d |
| +20,00% | 89,04 $ | 15/40 | +37,50% | prezzo iniziale | 74,20 $ | 1/15 | +6,67% | -16,67% | DEBOLE | 16,8 | 19,0 |
| +20,00% | 89,04 $ | 15/40 | +37,50% | -5,00% | 70,49 $ | 1/15 | +6,67% | -20,83% | DEBOLE | 16,8 | 23,0 |
| +20,00% | 89,04 $ | 15/40 | +37,50% | -8,00% | 68,26 $ | 1/15 | +6,67% | -23,33% | DEBOLE | 16,8 | 24,0 |
| +20,00% | 89,04 $ | 15/40 | +37,50% | -10,00% | 66,78 $ | 1/15 | +6,67% | -25,00% | DEBOLE | 16,8 | 24,0 |
| +20,00% | 89,04 $ | 15/40 | +37,50% | -15,00% | 63,07 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 16,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 13 poi sono rimbalzati fino a +10,00%. Percentuale: +40,62% (13/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 14 poi sono scaricati a -5,00%. Percentuale: +50,00% (14/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06610 $ | 32/40 | +80,00% | +5,00% | 0,07306 $ | 19/32 | +59,38% | +10,53% | MEDIA | 7,1 | 14,4 |
| -5,00% | 0,06610 $ | 32/40 | +80,00% | +10,00% | 0,07654 $ | 13/32 | +40,62% | +15,79% | BASSA | 7,1 | 15,2 |
| -5,00% | 0,06610 $ | 32/40 | +80,00% | +15,00% | 0,08002 $ | 7/32 | +21,88% | +21,05% | DEBOLE | 7,1 | 14,1 |
| -5,00% | 0,06610 $ | 32/40 | +80,00% | +20,00% | 0,08350 $ | 5/32 | +15,62% | +26,32% | DEBOLE | 7,1 | 21,8 |
| -8,00% | 0,06401 $ | 24/40 | +60,00% | +5,00% | 0,07306 $ | 9/24 | +37,50% | +14,13% | BASSA | 10,8 | 15,2 |
| -8,00% | 0,06401 $ | 24/40 | +60,00% | +10,00% | 0,07654 $ | 6/24 | +25,00% | +19,57% | DEBOLE | 10,8 | 16,3 |
| -8,00% | 0,06401 $ | 24/40 | +60,00% | +15,00% | 0,08002 $ | 4/24 | +16,67% | +25,00% | DEBOLE | 10,8 | 14,0 |
| -8,00% | 0,06401 $ | 24/40 | +60,00% | +20,00% | 0,08350 $ | 3/24 | +12,50% | +30,43% | DEBOLE | 10,8 | 22,3 |
| -10,00% | 0,06262 $ | 22/40 | +55,00% | +5,00% | 0,07306 $ | 9/22 | +40,91% | +16,67% | BASSA | 10,9 | 16,9 |
| -10,00% | 0,06262 $ | 22/40 | +55,00% | +10,00% | 0,07654 $ | 6/22 | +27,27% | +22,22% | DEBOLE | 10,9 | 16,3 |
| -10,00% | 0,06262 $ | 22/40 | +55,00% | +15,00% | 0,08002 $ | 4/22 | +18,18% | +27,78% | DEBOLE | 10,9 | 14,0 |
| -10,00% | 0,06262 $ | 22/40 | +55,00% | +20,00% | 0,08350 $ | 3/22 | +13,64% | +33,33% | DEBOLE | 10,9 | 22,3 |
| -15,00% | 0,05914 $ | 15/40 | +37,50% | +5,00% | 0,07306 $ | 4/15 | +26,67% | +23,53% | DEBOLE | 12,3 | 16,5 |
| -15,00% | 0,05914 $ | 15/40 | +37,50% | +10,00% | 0,07654 $ | 4/15 | +26,67% | +29,41% | DEBOLE | 12,3 | 17,0 |
| -15,00% | 0,05914 $ | 15/40 | +37,50% | +15,00% | 0,08002 $ | 2/15 | +13,33% | +35,29% | DEBOLE | 12,3 | 10,0 |
| -15,00% | 0,05914 $ | 15/40 | +37,50% | +20,00% | 0,08350 $ | 1/15 | +6,67% | +41,18% | DEBOLE | 12,3 | 24,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07306 $ | 33/40 | +82,50% | prezzo iniziale | 0,06958 $ | 27/33 | +81,82% | -4,76% | ALTA | 6,0 | 12,6 |
| +5,00% | 0,07306 $ | 33/40 | +82,50% | -5,00% | 0,06610 $ | 20/33 | +60,61% | -9,52% | MEDIA | 6,0 | 15,1 |
| +5,00% | 0,07306 $ | 33/40 | +82,50% | -8,00% | 0,06401 $ | 14/33 | +42,42% | -12,38% | BASSA | 6,0 | 18,7 |
| +5,00% | 0,07306 $ | 33/40 | +82,50% | -10,00% | 0,06262 $ | 12/33 | +36,36% | -14,29% | BASSA | 6,0 | 18,5 |
| +5,00% | 0,07306 $ | 33/40 | +82,50% | -15,00% | 0,05914 $ | 5/33 | +15,15% | -19,05% | DEBOLE | 6,0 | 16,6 |
| +10,00% | 0,07654 $ | 28/40 | +70,00% | prezzo iniziale | 0,06958 $ | 20/28 | +71,43% | -9,09% | ALTA | 7,7 | 15,3 |
| +10,00% | 0,07654 $ | 28/40 | +70,00% | -5,00% | 0,06610 $ | 14/28 | +50,00% | -13,64% | MEDIA | 7,7 | 19,3 |
| +10,00% | 0,07654 $ | 28/40 | +70,00% | -8,00% | 0,06401 $ | 9/28 | +32,14% | -16,36% | DEBOLE | 7,7 | 19,1 |
| +10,00% | 0,07654 $ | 28/40 | +70,00% | -10,00% | 0,06262 $ | 7/28 | +25,00% | -18,18% | DEBOLE | 7,7 | 18,4 |
| +10,00% | 0,07654 $ | 28/40 | +70,00% | -15,00% | 0,05914 $ | 3/28 | +10,71% | -22,73% | DEBOLE | 7,7 | 14,3 |
| +15,00% | 0,08002 $ | 20/40 | +50,00% | prezzo iniziale | 0,06958 $ | 13/20 | +65,00% | -13,04% | ALTA | 8,7 | 16,2 |
| +15,00% | 0,08002 $ | 20/40 | +50,00% | -5,00% | 0,06610 $ | 8/20 | +40,00% | -17,39% | BASSA | 8,7 | 20,4 |
| +15,00% | 0,08002 $ | 20/40 | +50,00% | -8,00% | 0,06401 $ | 5/20 | +25,00% | -20,00% | DEBOLE | 8,7 | 17,4 |
| +15,00% | 0,08002 $ | 20/40 | +50,00% | -10,00% | 0,06262 $ | 4/20 | +20,00% | -21,74% | DEBOLE | 8,7 | 17,5 |
| +15,00% | 0,08002 $ | 20/40 | +50,00% | -15,00% | 0,05914 $ | 1/20 | +5,00% | -26,09% | DEBOLE | 8,7 | 11,0 |
| +20,00% | 0,08350 $ | 13/40 | +32,50% | prezzo iniziale | 0,06958 $ | 6/13 | +46,15% | -16,67% | BASSA | 13,2 | 21,8 |
| +20,00% | 0,08350 $ | 13/40 | +32,50% | -5,00% | 0,06610 $ | 2/13 | +15,38% | -20,83% | DEBOLE | 13,2 | 26,0 |
| +20,00% | 0,08350 $ | 13/40 | +32,50% | -8,00% | 0,06401 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 13,2 | n/d |
| +20,00% | 0,08350 $ | 13/40 | +32,50% | -10,00% | 0,06262 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 13,2 | n/d |
| +20,00% | 0,08350 $ | 13/40 | +32,50% | -15,00% | 0,05914 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 13,2 | n/d |

---
