# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-09-24 07:31:42 CEST**  
UTC: **2026-09-24 05:31:42 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.974 $ | 92.602 $ | +40,00% | +15,79% | rimbalzo debole | 92.602 $ | 79.974 $ | +7,14% | -13,64% | spike storicamente più resistente |
| SOL | 109,68 $ | 126,99 $ | +30,77% | +15,79% | rimbalzo poco frequente | 126,99 $ | 109,68 $ | +24,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08976 $ | 0,10393 $ | +18,18% | +15,79% | rimbalzo poco frequente | 0,10393 $ | 0,08976 $ | +33,33% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 20 prima sono scesi a -5,00%. Tra quei 20, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (8/20). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 2 poi sono scaricati a -5,00%. Percentuale: +7,14% (2/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 79.974 $ | 20/40 | +50,00% | +5,00% | 88.393 $ | 10/20 | +50,00% | +10,53% | MEDIA | 5,9 | 14,8 |
| -5,00% | 79.974 $ | 20/40 | +50,00% | +10,00% | 92.602 $ | 8/20 | +40,00% | +15,79% | BASSA | 5,9 | 14,4 |
| -5,00% | 79.974 $ | 20/40 | +50,00% | +15,00% | 96.811 $ | 5/20 | +25,00% | +21,05% | DEBOLE | 5,9 | 14,0 |
| -5,00% | 79.974 $ | 20/40 | +50,00% | +20,00% | 101.020 $ | 5/20 | +25,00% | +26,32% | DEBOLE | 5,9 | 14,4 |
| -8,00% | 77.449 $ | 19/40 | +47,50% | +5,00% | 88.393 $ | 9/19 | +47,37% | +14,13% | BASSA | 9,0 | 15,1 |
| -8,00% | 77.449 $ | 19/40 | +47,50% | +10,00% | 92.602 $ | 8/19 | +42,11% | +19,57% | BASSA | 9,0 | 14,4 |
| -8,00% | 77.449 $ | 19/40 | +47,50% | +15,00% | 96.811 $ | 5/19 | +26,32% | +25,00% | DEBOLE | 9,0 | 14,0 |
| -8,00% | 77.449 $ | 19/40 | +47,50% | +20,00% | 101.020 $ | 5/19 | +26,32% | +30,43% | DEBOLE | 9,0 | 14,4 |
| -10,00% | 75.765 $ | 15/40 | +37,50% | +5,00% | 88.393 $ | 6/15 | +40,00% | +16,67% | BASSA | 8,5 | 11,8 |
| -10,00% | 75.765 $ | 15/40 | +37,50% | +10,00% | 92.602 $ | 6/15 | +40,00% | +22,22% | BASSA | 8,5 | 12,2 |
| -10,00% | 75.765 $ | 15/40 | +37,50% | +15,00% | 96.811 $ | 4/15 | +26,67% | +27,78% | DEBOLE | 8,5 | 12,5 |
| -10,00% | 75.765 $ | 15/40 | +37,50% | +20,00% | 101.020 $ | 4/15 | +26,67% | +33,33% | DEBOLE | 8,5 | 13,0 |
| -15,00% | 71.556 $ | 11/40 | +27,50% | +5,00% | 88.393 $ | 3/11 | +27,27% | +23,53% | DEBOLE | 11,7 | 16,7 |
| -15,00% | 71.556 $ | 11/40 | +27,50% | +10,00% | 92.602 $ | 3/11 | +27,27% | +29,41% | DEBOLE | 11,7 | 17,3 |
| -15,00% | 71.556 $ | 11/40 | +27,50% | +15,00% | 96.811 $ | 1/11 | +9,09% | +35,29% | DEBOLE | 11,7 | 20,0 |
| -15,00% | 71.556 $ | 11/40 | +27,50% | +20,00% | 101.020 $ | 1/11 | +9,09% | +41,18% | DEBOLE | 11,7 | 20,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 88.393 $ | 33/40 | +82,50% | prezzo iniziale | 84.184 $ | 10/33 | +30,30% | -4,76% | DEBOLE | 4,9 | 10,8 |
| +5,00% | 88.393 $ | 33/40 | +82,50% | -5,00% | 79.974 $ | 7/33 | +21,21% | -9,52% | DEBOLE | 4,9 | 16,1 |
| +5,00% | 88.393 $ | 33/40 | +82,50% | -8,00% | 77.449 $ | 6/33 | +18,18% | -12,38% | DEBOLE | 4,9 | 18,3 |
| +5,00% | 88.393 $ | 33/40 | +82,50% | -10,00% | 75.765 $ | 3/33 | +9,09% | -14,29% | DEBOLE | 4,9 | 14,7 |
| +5,00% | 88.393 $ | 33/40 | +82,50% | -15,00% | 71.556 $ | 2/33 | +6,06% | -19,05% | DEBOLE | 4,9 | 20,5 |
| +10,00% | 92.602 $ | 28/40 | +70,00% | prezzo iniziale | 84.184 $ | 5/28 | +17,86% | -9,09% | DEBOLE | 6,9 | 13,2 |
| +10,00% | 92.602 $ | 28/40 | +70,00% | -5,00% | 79.974 $ | 2/28 | +7,14% | -13,64% | DEBOLE | 6,9 | 12,0 |
| +10,00% | 92.602 $ | 28/40 | +70,00% | -8,00% | 77.449 $ | 2/28 | +7,14% | -16,36% | DEBOLE | 6,9 | 12,0 |
| +10,00% | 92.602 $ | 28/40 | +70,00% | -10,00% | 75.765 $ | 1/28 | +3,57% | -18,18% | DEBOLE | 6,9 | 10,0 |
| +10,00% | 92.602 $ | 28/40 | +70,00% | -15,00% | 71.556 $ | 1/28 | +3,57% | -22,73% | DEBOLE | 6,9 | 22,0 |
| +15,00% | 96.811 $ | 24/40 | +60,00% | prezzo iniziale | 84.184 $ | 1/24 | +4,17% | -13,04% | DEBOLE | 8,7 | 13,0 |
| +15,00% | 96.811 $ | 24/40 | +60,00% | -5,00% | 79.974 $ | 0/24 | 0,00% | -17,39% | DEBOLE | 8,7 | n/d |
| +15,00% | 96.811 $ | 24/40 | +60,00% | -8,00% | 77.449 $ | 0/24 | 0,00% | -20,00% | DEBOLE | 8,7 | n/d |
| +15,00% | 96.811 $ | 24/40 | +60,00% | -10,00% | 75.765 $ | 0/24 | 0,00% | -21,74% | DEBOLE | 8,7 | n/d |
| +15,00% | 96.811 $ | 24/40 | +60,00% | -15,00% | 71.556 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 8,7 | n/d |
| +20,00% | 101.020 $ | 22/40 | +55,00% | prezzo iniziale | 84.184 $ | 0/22 | 0,00% | -16,67% | DEBOLE | 11,2 | n/d |
| +20,00% | 101.020 $ | 22/40 | +55,00% | -5,00% | 79.974 $ | 0/22 | 0,00% | -20,83% | DEBOLE | 11,2 | n/d |
| +20,00% | 101.020 $ | 22/40 | +55,00% | -8,00% | 77.449 $ | 0/22 | 0,00% | -23,33% | DEBOLE | 11,2 | n/d |
| +20,00% | 101.020 $ | 22/40 | +55,00% | -10,00% | 75.765 $ | 0/22 | 0,00% | -25,00% | DEBOLE | 11,2 | n/d |
| +20,00% | 101.020 $ | 22/40 | +55,00% | -15,00% | 71.556 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 11,2 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +30,77% (8/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 6 poi sono scaricati a -5,00%. Percentuale: +24,00% (6/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 109,68 $ | 26/40 | +65,00% | +5,00% | 121,22 $ | 9/26 | +34,62% | +10,53% | DEBOLE | 6,3 | 14,0 |
| -5,00% | 109,68 $ | 26/40 | +65,00% | +10,00% | 126,99 $ | 8/26 | +30,77% | +15,79% | DEBOLE | 6,3 | 13,9 |
| -5,00% | 109,68 $ | 26/40 | +65,00% | +15,00% | 132,77 $ | 5/26 | +19,23% | +21,05% | DEBOLE | 6,3 | 14,8 |
| -5,00% | 109,68 $ | 26/40 | +65,00% | +20,00% | 138,54 $ | 4/26 | +15,38% | +26,32% | DEBOLE | 6,3 | 14,5 |
| -8,00% | 106,21 $ | 24/40 | +60,00% | +5,00% | 121,22 $ | 7/24 | +29,17% | +14,13% | DEBOLE | 7,4 | 14,0 |
| -8,00% | 106,21 $ | 24/40 | +60,00% | +10,00% | 126,99 $ | 7/24 | +29,17% | +19,57% | DEBOLE | 7,4 | 15,4 |
| -8,00% | 106,21 $ | 24/40 | +60,00% | +15,00% | 132,77 $ | 4/24 | +16,67% | +25,00% | DEBOLE | 7,4 | 17,5 |
| -8,00% | 106,21 $ | 24/40 | +60,00% | +20,00% | 138,54 $ | 3/24 | +12,50% | +30,43% | DEBOLE | 7,4 | 16,7 |
| -10,00% | 103,90 $ | 23/40 | +57,50% | +5,00% | 121,22 $ | 6/23 | +26,09% | +16,67% | DEBOLE | 7,8 | 13,7 |
| -10,00% | 103,90 $ | 23/40 | +57,50% | +10,00% | 126,99 $ | 6/23 | +26,09% | +22,22% | DEBOLE | 7,8 | 14,8 |
| -10,00% | 103,90 $ | 23/40 | +57,50% | +15,00% | 132,77 $ | 3/23 | +13,04% | +27,78% | DEBOLE | 7,8 | 16,7 |
| -10,00% | 103,90 $ | 23/40 | +57,50% | +20,00% | 138,54 $ | 2/23 | +8,70% | +33,33% | DEBOLE | 7,8 | 15,0 |
| -15,00% | 98,13 $ | 20/40 | +50,00% | +5,00% | 121,22 $ | 3/20 | +15,00% | +23,53% | DEBOLE | 11,8 | 15,7 |
| -15,00% | 98,13 $ | 20/40 | +50,00% | +10,00% | 126,99 $ | 3/20 | +15,00% | +29,41% | DEBOLE | 11,8 | 16,0 |
| -15,00% | 98,13 $ | 20/40 | +50,00% | +15,00% | 132,77 $ | 1/20 | +5,00% | +35,29% | DEBOLE | 11,8 | 16,0 |
| -15,00% | 98,13 $ | 20/40 | +50,00% | +20,00% | 138,54 $ | 1/20 | +5,00% | +41,18% | DEBOLE | 11,8 | 20,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 121,22 $ | 28/40 | +70,00% | prezzo iniziale | 115,45 $ | 12/28 | +42,86% | -4,76% | BASSA | 4,3 | 9,5 |
| +5,00% | 121,22 $ | 28/40 | +70,00% | -5,00% | 109,68 $ | 10/28 | +35,71% | -9,52% | BASSA | 4,3 | 13,2 |
| +5,00% | 121,22 $ | 28/40 | +70,00% | -8,00% | 106,21 $ | 9/28 | +32,14% | -12,38% | DEBOLE | 4,3 | 13,1 |
| +5,00% | 121,22 $ | 28/40 | +70,00% | -10,00% | 103,90 $ | 9/28 | +32,14% | -14,29% | DEBOLE | 4,3 | 13,2 |
| +5,00% | 121,22 $ | 28/40 | +70,00% | -15,00% | 98,13 $ | 7/28 | +25,00% | -19,05% | DEBOLE | 4,3 | 20,1 |
| +10,00% | 126,99 $ | 25/40 | +62,50% | prezzo iniziale | 115,45 $ | 9/25 | +36,00% | -9,09% | BASSA | 6,8 | 14,0 |
| +10,00% | 126,99 $ | 25/40 | +62,50% | -5,00% | 109,68 $ | 6/25 | +24,00% | -13,64% | DEBOLE | 6,8 | 15,2 |
| +10,00% | 126,99 $ | 25/40 | +62,50% | -8,00% | 106,21 $ | 5/25 | +20,00% | -16,36% | DEBOLE | 6,8 | 14,4 |
| +10,00% | 126,99 $ | 25/40 | +62,50% | -10,00% | 103,90 $ | 5/25 | +20,00% | -18,18% | DEBOLE | 6,8 | 14,6 |
| +10,00% | 126,99 $ | 25/40 | +62,50% | -15,00% | 98,13 $ | 4/25 | +16,00% | -22,73% | DEBOLE | 6,8 | 20,0 |
| +15,00% | 132,77 $ | 19/40 | +47,50% | prezzo iniziale | 115,45 $ | 2/19 | +10,53% | -13,04% | DEBOLE | 7,0 | 19,0 |
| +15,00% | 132,77 $ | 19/40 | +47,50% | -5,00% | 109,68 $ | 1/19 | +5,26% | -17,39% | DEBOLE | 7,0 | 22,0 |
| +15,00% | 132,77 $ | 19/40 | +47,50% | -8,00% | 106,21 $ | 0/19 | 0,00% | -20,00% | DEBOLE | 7,0 | n/d |
| +15,00% | 132,77 $ | 19/40 | +47,50% | -10,00% | 103,90 $ | 0/19 | 0,00% | -21,74% | DEBOLE | 7,0 | n/d |
| +15,00% | 132,77 $ | 19/40 | +47,50% | -15,00% | 98,13 $ | 0/19 | 0,00% | -26,09% | DEBOLE | 7,0 | n/d |
| +20,00% | 138,54 $ | 18/40 | +45,00% | prezzo iniziale | 115,45 $ | 2/18 | +11,11% | -16,67% | DEBOLE | 8,6 | 19,0 |
| +20,00% | 138,54 $ | 18/40 | +45,00% | -5,00% | 109,68 $ | 1/18 | +5,56% | -20,83% | DEBOLE | 8,6 | 22,0 |
| +20,00% | 138,54 $ | 18/40 | +45,00% | -8,00% | 106,21 $ | 0/18 | 0,00% | -23,33% | DEBOLE | 8,6 | n/d |
| +20,00% | 138,54 $ | 18/40 | +45,00% | -10,00% | 103,90 $ | 0/18 | 0,00% | -25,00% | DEBOLE | 8,6 | n/d |
| +20,00% | 138,54 $ | 18/40 | +45,00% | -15,00% | 98,13 $ | 0/18 | 0,00% | -29,17% | DEBOLE | 8,6 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +18,18% (6/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 18 prima sono saliti a +10,00%. Tra quei 18, 6 poi sono scaricati a -5,00%. Percentuale: +33,33% (6/18). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,08976 $ | 33/40 | +82,50% | +5,00% | 0,09920 $ | 9/33 | +27,27% | +10,53% | DEBOLE | 6,8 | 13,1 |
| -5,00% | 0,08976 $ | 33/40 | +82,50% | +10,00% | 0,10393 $ | 6/33 | +18,18% | +15,79% | DEBOLE | 6,8 | 17,2 |
| -5,00% | 0,08976 $ | 33/40 | +82,50% | +15,00% | 0,10865 $ | 4/33 | +12,12% | +21,05% | DEBOLE | 6,8 | 19,0 |
| -5,00% | 0,08976 $ | 33/40 | +82,50% | +20,00% | 0,11338 $ | 2/33 | +6,06% | +26,32% | DEBOLE | 6,8 | 14,5 |
| -8,00% | 0,08692 $ | 31/40 | +77,50% | +5,00% | 0,09920 $ | 5/31 | +16,13% | +14,13% | DEBOLE | 9,6 | 15,6 |
| -8,00% | 0,08692 $ | 31/40 | +77,50% | +10,00% | 0,10393 $ | 5/31 | +16,13% | +19,57% | DEBOLE | 9,6 | 16,6 |
| -8,00% | 0,08692 $ | 31/40 | +77,50% | +15,00% | 0,10865 $ | 3/31 | +9,68% | +25,00% | DEBOLE | 9,6 | 18,3 |
| -8,00% | 0,08692 $ | 31/40 | +77,50% | +20,00% | 0,11338 $ | 2/31 | +6,45% | +30,43% | DEBOLE | 9,6 | 14,5 |
| -10,00% | 0,08503 $ | 30/40 | +75,00% | +5,00% | 0,09920 $ | 4/30 | +13,33% | +16,67% | DEBOLE | 10,6 | 16,8 |
| -10,00% | 0,08503 $ | 30/40 | +75,00% | +10,00% | 0,10393 $ | 4/30 | +13,33% | +22,22% | DEBOLE | 10,6 | 17,5 |
| -10,00% | 0,08503 $ | 30/40 | +75,00% | +15,00% | 0,10865 $ | 2/30 | +6,67% | +27,78% | DEBOLE | 10,6 | 21,0 |
| -10,00% | 0,08503 $ | 30/40 | +75,00% | +20,00% | 0,11338 $ | 1/30 | +3,33% | +33,33% | DEBOLE | 10,6 | 12,0 |
| -15,00% | 0,08031 $ | 28/40 | +70,00% | +5,00% | 0,09920 $ | 2/28 | +7,14% | +23,53% | DEBOLE | 13,6 | 14,5 |
| -15,00% | 0,08031 $ | 28/40 | +70,00% | +10,00% | 0,10393 $ | 2/28 | +7,14% | +29,41% | DEBOLE | 13,6 | 15,5 |
| -15,00% | 0,08031 $ | 28/40 | +70,00% | +15,00% | 0,10865 $ | 0/28 | 0,00% | +35,29% | DEBOLE | 13,6 | n/d |
| -15,00% | 0,08031 $ | 28/40 | +70,00% | +20,00% | 0,11338 $ | 0/28 | 0,00% | +41,18% | DEBOLE | 13,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,09920 $ | 27/40 | +67,50% | prezzo iniziale | 0,09448 $ | 21/27 | +77,78% | -4,76% | ALTA | 3,6 | 9,2 |
| +5,00% | 0,09920 $ | 27/40 | +67,50% | -5,00% | 0,08976 $ | 18/27 | +66,67% | -9,52% | ALTA | 3,6 | 10,8 |
| +5,00% | 0,09920 $ | 27/40 | +67,50% | -8,00% | 0,08692 $ | 17/27 | +62,96% | -12,38% | MEDIA | 3,6 | 12,8 |
| +5,00% | 0,09920 $ | 27/40 | +67,50% | -10,00% | 0,08503 $ | 17/27 | +62,96% | -14,29% | MEDIA | 3,6 | 13,8 |
| +5,00% | 0,09920 $ | 27/40 | +67,50% | -15,00% | 0,08031 $ | 16/27 | +59,26% | -19,05% | MEDIA | 3,6 | 17,8 |
| +10,00% | 0,10393 $ | 18/40 | +45,00% | prezzo iniziale | 0,09448 $ | 9/18 | +50,00% | -9,09% | MEDIA | 7,7 | 13,1 |
| +10,00% | 0,10393 $ | 18/40 | +45,00% | -5,00% | 0,08976 $ | 6/18 | +33,33% | -13,64% | DEBOLE | 7,7 | 13,5 |
| +10,00% | 0,10393 $ | 18/40 | +45,00% | -8,00% | 0,08692 $ | 6/18 | +33,33% | -16,36% | DEBOLE | 7,7 | 15,5 |
| +10,00% | 0,10393 $ | 18/40 | +45,00% | -10,00% | 0,08503 $ | 6/18 | +33,33% | -18,18% | DEBOLE | 7,7 | 16,5 |
| +10,00% | 0,10393 $ | 18/40 | +45,00% | -15,00% | 0,08031 $ | 6/18 | +33,33% | -22,73% | DEBOLE | 7,7 | 20,7 |
| +15,00% | 0,10865 $ | 14/40 | +35,00% | prezzo iniziale | 0,09448 $ | 5/14 | +35,71% | -13,04% | BASSA | 9,2 | 18,6 |
| +15,00% | 0,10865 $ | 14/40 | +35,00% | -5,00% | 0,08976 $ | 3/14 | +21,43% | -17,39% | DEBOLE | 9,2 | 16,0 |
| +15,00% | 0,10865 $ | 14/40 | +35,00% | -8,00% | 0,08692 $ | 3/14 | +21,43% | -20,00% | DEBOLE | 9,2 | 18,7 |
| +15,00% | 0,10865 $ | 14/40 | +35,00% | -10,00% | 0,08503 $ | 3/14 | +21,43% | -21,74% | DEBOLE | 9,2 | 20,0 |
| +15,00% | 0,10865 $ | 14/40 | +35,00% | -15,00% | 0,08031 $ | 3/14 | +21,43% | -26,09% | DEBOLE | 9,2 | 22,0 |
| +20,00% | 0,11338 $ | 12/40 | +30,00% | prezzo iniziale | 0,09448 $ | 4/12 | +33,33% | -16,67% | DEBOLE | 9,1 | 15,8 |
| +20,00% | 0,11338 $ | 12/40 | +30,00% | -5,00% | 0,08976 $ | 3/12 | +25,00% | -20,83% | DEBOLE | 9,1 | 16,0 |
| +20,00% | 0,11338 $ | 12/40 | +30,00% | -8,00% | 0,08692 $ | 3/12 | +25,00% | -23,33% | DEBOLE | 9,1 | 18,7 |
| +20,00% | 0,11338 $ | 12/40 | +30,00% | -10,00% | 0,08503 $ | 3/12 | +25,00% | -25,00% | DEBOLE | 9,1 | 20,0 |
| +20,00% | 0,11338 $ | 12/40 | +30,00% | -15,00% | 0,08031 $ | 3/12 | +25,00% | -29,17% | DEBOLE | 9,1 | 22,0 |

---
