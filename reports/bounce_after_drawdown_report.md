# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-19 07:31:47 CEST**  
UTC: **2026-08-19 05:31:47 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.091 $ | 70.736 $ | +35,29% | +15,79% | rimbalzo debole | 70.736 $ | 61.091 $ | +11,54% | -13,64% | spike storicamente più resistente |
| SOL | 73,07 $ | 84,61 $ | +37,50% | +15,79% | rimbalzo debole | 84,61 $ | 73,07 $ | +7,41% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06650 $ | 0,07700 $ | +57,14% | +15,79% | rimbalzo possibile | 0,07700 $ | 0,06650 $ | +20,00% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +35,29% (6/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 3 poi sono scaricati a -5,00%. Percentuale: +11,54% (3/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.091 $ | 17/40 | +42,50% | +5,00% | 67.521 $ | 9/17 | +52,94% | +10,53% | MEDIA | 10,3 | 16,9 |
| -5,00% | 61.091 $ | 17/40 | +42,50% | +10,00% | 70.736 $ | 6/17 | +35,29% | +15,79% | BASSA | 10,3 | 16,3 |
| -5,00% | 61.091 $ | 17/40 | +42,50% | +15,00% | 73.952 $ | 6/17 | +35,29% | +21,05% | BASSA | 10,3 | 18,8 |
| -5,00% | 61.091 $ | 17/40 | +42,50% | +20,00% | 77.167 $ | 5/17 | +29,41% | +26,32% | DEBOLE | 10,3 | 17,2 |
| -8,00% | 59.161 $ | 14/40 | +35,00% | +5,00% | 67.521 $ | 6/14 | +42,86% | +14,13% | BASSA | 13,2 | 19,0 |
| -8,00% | 59.161 $ | 14/40 | +35,00% | +10,00% | 70.736 $ | 4/14 | +28,57% | +19,57% | DEBOLE | 13,2 | 20,5 |
| -8,00% | 59.161 $ | 14/40 | +35,00% | +15,00% | 73.952 $ | 4/14 | +28,57% | +25,00% | DEBOLE | 13,2 | 21,8 |
| -8,00% | 59.161 $ | 14/40 | +35,00% | +20,00% | 77.167 $ | 3/14 | +21,43% | +30,43% | DEBOLE | 13,2 | 20,0 |
| -10,00% | 57.875 $ | 13/40 | +32,50% | +5,00% | 67.521 $ | 5/13 | +38,46% | +16,67% | BASSA | 17,3 | 20,4 |
| -10,00% | 57.875 $ | 13/40 | +32,50% | +10,00% | 70.736 $ | 3/13 | +23,08% | +22,22% | DEBOLE | 17,3 | 21,7 |
| -10,00% | 57.875 $ | 13/40 | +32,50% | +15,00% | 73.952 $ | 3/13 | +23,08% | +27,78% | DEBOLE | 17,3 | 23,3 |
| -10,00% | 57.875 $ | 13/40 | +32,50% | +20,00% | 77.167 $ | 2/13 | +15,38% | +33,33% | DEBOLE | 17,3 | 21,0 |
| -15,00% | 54.660 $ | 4/40 | +10,00% | +5,00% | 67.521 $ | 1/4 | +25,00% | +23,53% | DEBOLE | 23,2 | 23,0 |
| -15,00% | 54.660 $ | 4/40 | +10,00% | +10,00% | 70.736 $ | 1/4 | +25,00% | +29,41% | DEBOLE | 23,2 | 24,0 |
| -15,00% | 54.660 $ | 4/40 | +10,00% | +15,00% | 73.952 $ | 1/4 | +25,00% | +35,29% | DEBOLE | 23,2 | 29,0 |
| -15,00% | 54.660 $ | 4/40 | +10,00% | +20,00% | 77.167 $ | 0/4 | 0,00% | +41,18% | DEBOLE | 23,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.521 $ | 38/40 | +95,00% | prezzo iniziale | 64.306 $ | 18/38 | +47,37% | -4,76% | BASSA | 9,5 | 18,9 |
| +5,00% | 67.521 $ | 38/40 | +95,00% | -5,00% | 61.091 $ | 9/38 | +23,68% | -9,52% | DEBOLE | 9,5 | 17,6 |
| +5,00% | 67.521 $ | 38/40 | +95,00% | -8,00% | 59.161 $ | 9/38 | +23,68% | -12,38% | DEBOLE | 9,5 | 19,6 |
| +5,00% | 67.521 $ | 38/40 | +95,00% | -10,00% | 57.875 $ | 9/38 | +23,68% | -14,29% | DEBOLE | 9,5 | 21,4 |
| +5,00% | 67.521 $ | 38/40 | +95,00% | -15,00% | 54.660 $ | 4/38 | +10,53% | -19,05% | DEBOLE | 9,5 | 23,2 |
| +10,00% | 70.736 $ | 26/40 | +65,00% | prezzo iniziale | 64.306 $ | 8/26 | +30,77% | -9,09% | DEBOLE | 10,5 | 19,9 |
| +10,00% | 70.736 $ | 26/40 | +65,00% | -5,00% | 61.091 $ | 3/26 | +11,54% | -13,64% | DEBOLE | 10,5 | 15,3 |
| +10,00% | 70.736 $ | 26/40 | +65,00% | -8,00% | 59.161 $ | 3/26 | +11,54% | -16,36% | DEBOLE | 10,5 | 15,3 |
| +10,00% | 70.736 $ | 26/40 | +65,00% | -10,00% | 57.875 $ | 3/26 | +11,54% | -18,18% | DEBOLE | 10,5 | 15,3 |
| +10,00% | 70.736 $ | 26/40 | +65,00% | -15,00% | 54.660 $ | 2/26 | +7,69% | -22,73% | DEBOLE | 10,5 | 26,5 |
| +15,00% | 73.952 $ | 23/40 | +57,50% | prezzo iniziale | 64.306 $ | 6/23 | +26,09% | -13,04% | DEBOLE | 11,9 | 19,7 |
| +15,00% | 73.952 $ | 23/40 | +57,50% | -5,00% | 61.091 $ | 3/23 | +13,04% | -17,39% | DEBOLE | 11,9 | 15,3 |
| +15,00% | 73.952 $ | 23/40 | +57,50% | -8,00% | 59.161 $ | 3/23 | +13,04% | -20,00% | DEBOLE | 11,9 | 15,3 |
| +15,00% | 73.952 $ | 23/40 | +57,50% | -10,00% | 57.875 $ | 3/23 | +13,04% | -21,74% | DEBOLE | 11,9 | 15,3 |
| +15,00% | 73.952 $ | 23/40 | +57,50% | -15,00% | 54.660 $ | 2/23 | +8,70% | -26,09% | DEBOLE | 11,9 | 26,5 |
| +20,00% | 77.167 $ | 18/40 | +45,00% | prezzo iniziale | 64.306 $ | 4/18 | +22,22% | -16,67% | DEBOLE | 11,4 | 17,5 |
| +20,00% | 77.167 $ | 18/40 | +45,00% | -5,00% | 61.091 $ | 3/18 | +16,67% | -20,83% | DEBOLE | 11,4 | 15,3 |
| +20,00% | 77.167 $ | 18/40 | +45,00% | -8,00% | 59.161 $ | 3/18 | +16,67% | -23,33% | DEBOLE | 11,4 | 15,3 |
| +20,00% | 77.167 $ | 18/40 | +45,00% | -10,00% | 57.875 $ | 3/18 | +16,67% | -25,00% | DEBOLE | 11,4 | 15,3 |
| +20,00% | 77.167 $ | 18/40 | +45,00% | -15,00% | 54.660 $ | 2/18 | +11,11% | -29,17% | DEBOLE | 11,4 | 26,5 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +37,50% (6/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 2 poi sono scaricati a -5,00%. Percentuale: +7,41% (2/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,07 $ | 16/40 | +40,00% | +5,00% | 80,77 $ | 7/16 | +43,75% | +10,53% | BASSA | 12,4 | 14,7 |
| -5,00% | 73,07 $ | 16/40 | +40,00% | +10,00% | 84,61 $ | 6/16 | +37,50% | +15,79% | BASSA | 12,4 | 16,3 |
| -5,00% | 73,07 $ | 16/40 | +40,00% | +15,00% | 88,46 $ | 4/16 | +25,00% | +21,05% | DEBOLE | 12,4 | 15,0 |
| -5,00% | 73,07 $ | 16/40 | +40,00% | +20,00% | 92,30 $ | 4/16 | +25,00% | +26,32% | DEBOLE | 12,4 | 20,5 |
| -8,00% | 70,77 $ | 10/40 | +25,00% | +5,00% | 80,77 $ | 4/10 | +40,00% | +14,13% | BASSA | 10,2 | 14,0 |
| -8,00% | 70,77 $ | 10/40 | +25,00% | +10,00% | 84,61 $ | 4/10 | +40,00% | +19,57% | BASSA | 10,2 | 17,0 |
| -8,00% | 70,77 $ | 10/40 | +25,00% | +15,00% | 88,46 $ | 2/10 | +20,00% | +25,00% | DEBOLE | 10,2 | 14,5 |
| -8,00% | 70,77 $ | 10/40 | +25,00% | +20,00% | 92,30 $ | 2/10 | +20,00% | +30,43% | DEBOLE | 10,2 | 15,5 |
| -10,00% | 69,23 $ | 5/40 | +12,50% | +5,00% | 80,77 $ | 0/5 | 0,00% | +16,67% | DEBOLE | 12,4 | n/d |
| -10,00% | 69,23 $ | 5/40 | +12,50% | +10,00% | 84,61 $ | 0/5 | 0,00% | +22,22% | DEBOLE | 12,4 | n/d |
| -10,00% | 69,23 $ | 5/40 | +12,50% | +15,00% | 88,46 $ | 0/5 | 0,00% | +27,78% | DEBOLE | 12,4 | n/d |
| -10,00% | 69,23 $ | 5/40 | +12,50% | +20,00% | 92,30 $ | 0/5 | 0,00% | +33,33% | DEBOLE | 12,4 | n/d |
| -15,00% | 65,38 $ | 3/40 | +7,50% | +5,00% | 80,77 $ | 0/3 | 0,00% | +23,53% | DEBOLE | 17,7 | n/d |
| -15,00% | 65,38 $ | 3/40 | +7,50% | +10,00% | 84,61 $ | 0/3 | 0,00% | +29,41% | DEBOLE | 17,7 | n/d |
| -15,00% | 65,38 $ | 3/40 | +7,50% | +15,00% | 88,46 $ | 0/3 | 0,00% | +35,29% | DEBOLE | 17,7 | n/d |
| -15,00% | 65,38 $ | 3/40 | +7,50% | +20,00% | 92,30 $ | 0/3 | 0,00% | +41,18% | DEBOLE | 17,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 80,77 $ | 36/40 | +90,00% | prezzo iniziale | 76,92 $ | 15/36 | +41,67% | -4,76% | BASSA | 7,1 | 18,0 |
| +5,00% | 80,77 $ | 36/40 | +90,00% | -5,00% | 73,07 $ | 7/36 | +19,44% | -9,52% | DEBOLE | 7,1 | 21,0 |
| +5,00% | 80,77 $ | 36/40 | +90,00% | -8,00% | 70,77 $ | 3/36 | +8,33% | -12,38% | DEBOLE | 7,1 | 16,7 |
| +5,00% | 80,77 $ | 36/40 | +90,00% | -10,00% | 69,23 $ | 3/36 | +8,33% | -14,29% | DEBOLE | 7,1 | 17,0 |
| +5,00% | 80,77 $ | 36/40 | +90,00% | -15,00% | 65,38 $ | 1/36 | +2,78% | -19,05% | DEBOLE | 7,1 | 23,0 |
| +10,00% | 84,61 $ | 27/40 | +67,50% | prezzo iniziale | 76,92 $ | 6/27 | +22,22% | -9,09% | DEBOLE | 9,6 | 19,3 |
| +10,00% | 84,61 $ | 27/40 | +67,50% | -5,00% | 73,07 $ | 2/27 | +7,41% | -13,64% | DEBOLE | 9,6 | 12,5 |
| +10,00% | 84,61 $ | 27/40 | +67,50% | -8,00% | 70,77 $ | 1/27 | +3,70% | -16,36% | DEBOLE | 9,6 | 2,0 |
| +10,00% | 84,61 $ | 27/40 | +67,50% | -10,00% | 69,23 $ | 1/27 | +3,70% | -18,18% | DEBOLE | 9,6 | 2,0 |
| +10,00% | 84,61 $ | 27/40 | +67,50% | -15,00% | 65,38 $ | 0/27 | 0,00% | -22,73% | DEBOLE | 9,6 | n/d |
| +15,00% | 88,46 $ | 20/40 | +50,00% | prezzo iniziale | 76,92 $ | 2/20 | +10,00% | -13,04% | DEBOLE | 8,8 | 13,5 |
| +15,00% | 88,46 $ | 20/40 | +50,00% | -5,00% | 73,07 $ | 1/20 | +5,00% | -17,39% | DEBOLE | 8,8 | 2,0 |
| +15,00% | 88,46 $ | 20/40 | +50,00% | -8,00% | 70,77 $ | 1/20 | +5,00% | -20,00% | DEBOLE | 8,8 | 2,0 |
| +15,00% | 88,46 $ | 20/40 | +50,00% | -10,00% | 69,23 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 8,8 | 2,0 |
| +15,00% | 88,46 $ | 20/40 | +50,00% | -15,00% | 65,38 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 8,8 | n/d |
| +20,00% | 92,30 $ | 19/40 | +47,50% | prezzo iniziale | 76,92 $ | 2/19 | +10,53% | -16,67% | DEBOLE | 11,9 | 13,5 |
| +20,00% | 92,30 $ | 19/40 | +47,50% | -5,00% | 73,07 $ | 1/19 | +5,26% | -20,83% | DEBOLE | 11,9 | 2,0 |
| +20,00% | 92,30 $ | 19/40 | +47,50% | -8,00% | 70,77 $ | 1/19 | +5,26% | -23,33% | DEBOLE | 11,9 | 2,0 |
| +20,00% | 92,30 $ | 19/40 | +47,50% | -10,00% | 69,23 $ | 1/19 | +5,26% | -25,00% | DEBOLE | 11,9 | 2,0 |
| +20,00% | 92,30 $ | 19/40 | +47,50% | -15,00% | 65,38 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 11,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +57,14% (16/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 6 poi sono scaricati a -5,00%. Percentuale: +20,00% (6/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06650 $ | 28/40 | +70,00% | +5,00% | 0,07350 $ | 17/28 | +60,71% | +10,53% | MEDIA | 7,4 | 13,4 |
| -5,00% | 0,06650 $ | 28/40 | +70,00% | +10,00% | 0,07700 $ | 16/28 | +57,14% | +15,79% | MEDIA | 7,4 | 17,1 |
| -5,00% | 0,06650 $ | 28/40 | +70,00% | +15,00% | 0,08050 $ | 13/28 | +46,43% | +21,05% | BASSA | 7,4 | 21,2 |
| -5,00% | 0,06650 $ | 28/40 | +70,00% | +20,00% | 0,08400 $ | 10/28 | +35,71% | +26,32% | BASSA | 7,4 | 21,9 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +5,00% | 0,07350 $ | 12/22 | +54,55% | +14,13% | MEDIA | 7,9 | 13,5 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +10,00% | 0,07700 $ | 12/22 | +54,55% | +19,57% | MEDIA | 7,9 | 17,1 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +15,00% | 0,08050 $ | 9/22 | +40,91% | +25,00% | BASSA | 7,9 | 20,9 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +20,00% | 0,08400 $ | 8/22 | +36,36% | +30,43% | BASSA | 7,9 | 22,2 |
| -10,00% | 0,06300 $ | 19/40 | +47,50% | +5,00% | 0,07350 $ | 8/19 | +42,11% | +16,67% | BASSA | 10,5 | 11,8 |
| -10,00% | 0,06300 $ | 19/40 | +47,50% | +10,00% | 0,07700 $ | 8/19 | +42,11% | +22,22% | BASSA | 10,5 | 16,9 |
| -10,00% | 0,06300 $ | 19/40 | +47,50% | +15,00% | 0,08050 $ | 6/19 | +31,58% | +27,78% | DEBOLE | 10,5 | 19,5 |
| -10,00% | 0,06300 $ | 19/40 | +47,50% | +20,00% | 0,08400 $ | 6/19 | +31,58% | +33,33% | DEBOLE | 10,5 | 20,8 |
| -15,00% | 0,05950 $ | 10/40 | +25,00% | +5,00% | 0,07350 $ | 2/10 | +20,00% | +23,53% | DEBOLE | 14,5 | 9,5 |
| -15,00% | 0,05950 $ | 10/40 | +25,00% | +10,00% | 0,07700 $ | 2/10 | +20,00% | +29,41% | DEBOLE | 14,5 | 10,0 |
| -15,00% | 0,05950 $ | 10/40 | +25,00% | +15,00% | 0,08050 $ | 2/10 | +20,00% | +35,29% | DEBOLE | 14,5 | 16,5 |
| -15,00% | 0,05950 $ | 10/40 | +25,00% | +20,00% | 0,08400 $ | 2/10 | +20,00% | +41,18% | DEBOLE | 14,5 | 18,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | prezzo iniziale | 0,07000 $ | 16/33 | +48,48% | -4,76% | BASSA | 8,4 | 17,3 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -5,00% | 0,06650 $ | 11/33 | +33,33% | -9,52% | DEBOLE | 8,4 | 20,0 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -8,00% | 0,06440 $ | 6/33 | +18,18% | -12,38% | DEBOLE | 8,4 | 19,7 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -10,00% | 0,06300 $ | 4/33 | +12,12% | -14,29% | DEBOLE | 8,4 | 23,0 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -15,00% | 0,05950 $ | 2/33 | +6,06% | -19,05% | DEBOLE | 8,4 | 20,0 |
| +10,00% | 0,07700 $ | 30/40 | +75,00% | prezzo iniziale | 0,07000 $ | 10/30 | +33,33% | -9,09% | DEBOLE | 12,0 | 21,5 |
| +10,00% | 0,07700 $ | 30/40 | +75,00% | -5,00% | 0,06650 $ | 6/30 | +20,00% | -13,64% | DEBOLE | 12,0 | 25,3 |
| +10,00% | 0,07700 $ | 30/40 | +75,00% | -8,00% | 0,06440 $ | 3/30 | +10,00% | -16,36% | DEBOLE | 12,0 | 24,7 |
| +10,00% | 0,07700 $ | 30/40 | +75,00% | -10,00% | 0,06300 $ | 2/30 | +6,67% | -18,18% | DEBOLE | 12,0 | 28,0 |
| +10,00% | 0,07700 $ | 30/40 | +75,00% | -15,00% | 0,05950 $ | 0/30 | 0,00% | -22,73% | DEBOLE | 12,0 | n/d |
| +15,00% | 0,08050 $ | 26/40 | +65,00% | prezzo iniziale | 0,07000 $ | 3/26 | +11,54% | -13,04% | DEBOLE | 14,0 | 25,0 |
| +15,00% | 0,08050 $ | 26/40 | +65,00% | -5,00% | 0,06650 $ | 3/26 | +11,54% | -17,39% | DEBOLE | 14,0 | 27,3 |
| +15,00% | 0,08050 $ | 26/40 | +65,00% | -8,00% | 0,06440 $ | 2/26 | +7,69% | -20,00% | DEBOLE | 14,0 | 26,5 |
| +15,00% | 0,08050 $ | 26/40 | +65,00% | -10,00% | 0,06300 $ | 2/26 | +7,69% | -21,74% | DEBOLE | 14,0 | 28,0 |
| +15,00% | 0,08050 $ | 26/40 | +65,00% | -15,00% | 0,05950 $ | 0/26 | 0,00% | -26,09% | DEBOLE | 14,0 | n/d |
| +20,00% | 0,08400 $ | 22/40 | +55,00% | prezzo iniziale | 0,07000 $ | 0/22 | 0,00% | -16,67% | DEBOLE | 16,6 | n/d |
| +20,00% | 0,08400 $ | 22/40 | +55,00% | -5,00% | 0,06650 $ | 0/22 | 0,00% | -20,83% | DEBOLE | 16,6 | n/d |
| +20,00% | 0,08400 $ | 22/40 | +55,00% | -8,00% | 0,06440 $ | 0/22 | 0,00% | -23,33% | DEBOLE | 16,6 | n/d |
| +20,00% | 0,08400 $ | 22/40 | +55,00% | -10,00% | 0,06300 $ | 0/22 | 0,00% | -25,00% | DEBOLE | 16,6 | n/d |
| +20,00% | 0,08400 $ | 22/40 | +55,00% | -15,00% | 0,05950 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 16,6 | n/d |

---
