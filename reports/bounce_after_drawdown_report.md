# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-20 07:13:53 CEST**  
UTC: **2026-07-20 05:13:53 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.942 $ | 70.565 $ | +51,43% | +15,79% | rimbalzo possibile | 70.565 $ | 60.942 $ | +26,92% | -13,64% | spike storicamente più resistente |
| SOL | 72,12 $ | 83,51 $ | +36,36% | +15,79% | rimbalzo debole | 83,51 $ | 72,12 $ | +21,05% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06815 $ | 0,07891 $ | +25,00% | +15,79% | rimbalzo poco frequente | 0,07891 $ | 0,06815 $ | +47,37% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 18 poi sono rimbalzati fino a +10,00%. Percentuale: +51,43% (18/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 7 poi sono scaricati a -5,00%. Percentuale: +26,92% (7/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.942 $ | 35/40 | +87,50% | +5,00% | 67.357 $ | 21/35 | +60,00% | +10,53% | MEDIA | 8,0 | 22,0 |
| -5,00% | 60.942 $ | 35/40 | +87,50% | +10,00% | 70.565 $ | 18/35 | +51,43% | +15,79% | MEDIA | 8,0 | 23,6 |
| -5,00% | 60.942 $ | 35/40 | +87,50% | +15,00% | 73.772 $ | 12/35 | +34,29% | +21,05% | DEBOLE | 8,0 | 23,2 |
| -5,00% | 60.942 $ | 35/40 | +87,50% | +20,00% | 76.980 $ | 9/35 | +25,71% | +26,32% | DEBOLE | 8,0 | 24,6 |
| -8,00% | 59.018 $ | 27/40 | +67,50% | +5,00% | 67.357 $ | 12/27 | +44,44% | +14,13% | BASSA | 10,9 | 23,2 |
| -8,00% | 59.018 $ | 27/40 | +67,50% | +10,00% | 70.565 $ | 9/27 | +33,33% | +19,57% | DEBOLE | 10,9 | 23,7 |
| -8,00% | 59.018 $ | 27/40 | +67,50% | +15,00% | 73.772 $ | 5/27 | +18,52% | +25,00% | DEBOLE | 10,9 | 22,0 |
| -8,00% | 59.018 $ | 27/40 | +67,50% | +20,00% | 76.980 $ | 5/27 | +18,52% | +30,43% | DEBOLE | 10,9 | 22,0 |
| -10,00% | 57.735 $ | 23/40 | +57,50% | +5,00% | 67.357 $ | 9/23 | +39,13% | +16,67% | BASSA | 12,1 | 22,4 |
| -10,00% | 57.735 $ | 23/40 | +57,50% | +10,00% | 70.565 $ | 7/23 | +30,43% | +22,22% | DEBOLE | 12,1 | 23,0 |
| -10,00% | 57.735 $ | 23/40 | +57,50% | +15,00% | 73.772 $ | 5/23 | +21,74% | +27,78% | DEBOLE | 12,1 | 22,0 |
| -10,00% | 57.735 $ | 23/40 | +57,50% | +20,00% | 76.980 $ | 5/23 | +21,74% | +33,33% | DEBOLE | 12,1 | 22,0 |
| -15,00% | 54.527 $ | 12/40 | +30,00% | +5,00% | 67.357 $ | 0/12 | 0,00% | +23,53% | DEBOLE | 13,8 | n/d |
| -15,00% | 54.527 $ | 12/40 | +30,00% | +10,00% | 70.565 $ | 0/12 | 0,00% | +29,41% | DEBOLE | 13,8 | n/d |
| -15,00% | 54.527 $ | 12/40 | +30,00% | +15,00% | 73.772 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 13,8 | n/d |
| -15,00% | 54.527 $ | 12/40 | +30,00% | +20,00% | 76.980 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 13,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.357 $ | 32/40 | +80,00% | prezzo iniziale | 64.150 $ | 13/32 | +40,62% | -4,76% | BASSA | 14,7 | 13,1 |
| +5,00% | 67.357 $ | 32/40 | +80,00% | -5,00% | 60.942 $ | 10/32 | +31,25% | -9,52% | DEBOLE | 14,7 | 15,4 |
| +5,00% | 67.357 $ | 32/40 | +80,00% | -8,00% | 59.018 $ | 8/32 | +25,00% | -12,38% | DEBOLE | 14,7 | 20,0 |
| +5,00% | 67.357 $ | 32/40 | +80,00% | -10,00% | 57.735 $ | 7/32 | +21,88% | -14,29% | DEBOLE | 14,7 | 18,7 |
| +5,00% | 67.357 $ | 32/40 | +80,00% | -15,00% | 54.527 $ | 4/32 | +12,50% | -19,05% | DEBOLE | 14,7 | 22,5 |
| +10,00% | 70.565 $ | 26/40 | +65,00% | prezzo iniziale | 64.150 $ | 8/26 | +30,77% | -9,09% | DEBOLE | 17,7 | 16,8 |
| +10,00% | 70.565 $ | 26/40 | +65,00% | -5,00% | 60.942 $ | 7/26 | +26,92% | -13,64% | DEBOLE | 17,7 | 18,6 |
| +10,00% | 70.565 $ | 26/40 | +65,00% | -8,00% | 59.018 $ | 5/26 | +19,23% | -16,36% | DEBOLE | 17,7 | 23,8 |
| +10,00% | 70.565 $ | 26/40 | +65,00% | -10,00% | 57.735 $ | 4/26 | +15,38% | -18,18% | DEBOLE | 17,7 | 22,5 |
| +10,00% | 70.565 $ | 26/40 | +65,00% | -15,00% | 54.527 $ | 3/26 | +11,54% | -22,73% | DEBOLE | 17,7 | 25,0 |
| +15,00% | 73.772 $ | 18/40 | +45,00% | prezzo iniziale | 64.150 $ | 5/18 | +27,78% | -13,04% | DEBOLE | 19,6 | 20,0 |
| +15,00% | 73.772 $ | 18/40 | +45,00% | -5,00% | 60.942 $ | 4/18 | +22,22% | -17,39% | DEBOLE | 19,6 | 21,0 |
| +15,00% | 73.772 $ | 18/40 | +45,00% | -8,00% | 59.018 $ | 4/18 | +22,22% | -20,00% | DEBOLE | 19,6 | 26,0 |
| +15,00% | 73.772 $ | 18/40 | +45,00% | -10,00% | 57.735 $ | 3/18 | +16,67% | -21,74% | DEBOLE | 19,6 | 24,7 |
| +15,00% | 73.772 $ | 18/40 | +45,00% | -15,00% | 54.527 $ | 3/18 | +16,67% | -26,09% | DEBOLE | 19,6 | 25,0 |
| +20,00% | 76.980 $ | 13/40 | +32,50% | prezzo iniziale | 64.150 $ | 2/13 | +15,38% | -16,67% | DEBOLE | 21,5 | 16,0 |
| +20,00% | 76.980 $ | 13/40 | +32,50% | -5,00% | 60.942 $ | 2/13 | +15,38% | -20,83% | DEBOLE | 21,5 | 16,0 |
| +20,00% | 76.980 $ | 13/40 | +32,50% | -8,00% | 59.018 $ | 2/13 | +15,38% | -23,33% | DEBOLE | 21,5 | 26,0 |
| +20,00% | 76.980 $ | 13/40 | +32,50% | -10,00% | 57.735 $ | 1/13 | +7,69% | -25,00% | DEBOLE | 21,5 | 22,0 |
| +20,00% | 76.980 $ | 13/40 | +32,50% | -15,00% | 54.527 $ | 1/13 | +7,69% | -29,17% | DEBOLE | 21,5 | 23,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +36,36% (12/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 4 poi sono scaricati a -5,00%. Percentuale: +21,05% (4/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,12 $ | 33/40 | +82,50% | +5,00% | 79,72 $ | 19/33 | +57,58% | +10,53% | MEDIA | 5,5 | 20,8 |
| -5,00% | 72,12 $ | 33/40 | +82,50% | +10,00% | 83,51 $ | 12/33 | +36,36% | +15,79% | BASSA | 5,5 | 22,5 |
| -5,00% | 72,12 $ | 33/40 | +82,50% | +15,00% | 87,31 $ | 6/33 | +18,18% | +21,05% | DEBOLE | 5,5 | 20,8 |
| -5,00% | 72,12 $ | 33/40 | +82,50% | +20,00% | 91,10 $ | 5/33 | +15,15% | +26,32% | DEBOLE | 5,5 | 22,0 |
| -8,00% | 69,85 $ | 26/40 | +65,00% | +5,00% | 79,72 $ | 12/26 | +46,15% | +14,13% | BASSA | 6,4 | 20,7 |
| -8,00% | 69,85 $ | 26/40 | +65,00% | +10,00% | 83,51 $ | 8/26 | +30,77% | +19,57% | DEBOLE | 6,4 | 22,2 |
| -8,00% | 69,85 $ | 26/40 | +65,00% | +15,00% | 87,31 $ | 4/26 | +15,38% | +25,00% | DEBOLE | 6,4 | 20,2 |
| -8,00% | 69,85 $ | 26/40 | +65,00% | +20,00% | 91,10 $ | 3/26 | +11,54% | +30,43% | DEBOLE | 6,4 | 21,0 |
| -10,00% | 68,33 $ | 21/40 | +52,50% | +5,00% | 79,72 $ | 9/21 | +42,86% | +16,67% | BASSA | 6,7 | 20,8 |
| -10,00% | 68,33 $ | 21/40 | +52,50% | +10,00% | 83,51 $ | 5/21 | +23,81% | +22,22% | DEBOLE | 6,7 | 20,8 |
| -10,00% | 68,33 $ | 21/40 | +52,50% | +15,00% | 87,31 $ | 3/21 | +14,29% | +27,78% | DEBOLE | 6,7 | 18,7 |
| -10,00% | 68,33 $ | 21/40 | +52,50% | +20,00% | 91,10 $ | 2/21 | +9,52% | +33,33% | DEBOLE | 6,7 | 18,0 |
| -15,00% | 64,53 $ | 11/40 | +27,50% | +5,00% | 79,72 $ | 2/11 | +18,18% | +23,53% | DEBOLE | 12,7 | 21,5 |
| -15,00% | 64,53 $ | 11/40 | +27,50% | +10,00% | 83,51 $ | 0/11 | 0,00% | +29,41% | DEBOLE | 12,7 | n/d |
| -15,00% | 64,53 $ | 11/40 | +27,50% | +15,00% | 87,31 $ | 0/11 | 0,00% | +35,29% | DEBOLE | 12,7 | n/d |
| -15,00% | 64,53 $ | 11/40 | +27,50% | +20,00% | 91,10 $ | 0/11 | 0,00% | +41,18% | DEBOLE | 12,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,72 $ | 27/40 | +67,50% | prezzo iniziale | 75,92 $ | 16/27 | +59,26% | -4,76% | MEDIA | 13,8 | 16,6 |
| +5,00% | 79,72 $ | 27/40 | +67,50% | -5,00% | 72,12 $ | 11/27 | +40,74% | -9,52% | BASSA | 13,8 | 19,4 |
| +5,00% | 79,72 $ | 27/40 | +67,50% | -8,00% | 69,85 $ | 6/27 | +22,22% | -12,38% | DEBOLE | 13,8 | 22,7 |
| +5,00% | 79,72 $ | 27/40 | +67,50% | -10,00% | 68,33 $ | 4/27 | +14,81% | -14,29% | DEBOLE | 13,8 | 23,0 |
| +5,00% | 79,72 $ | 27/40 | +67,50% | -15,00% | 64,53 $ | 1/27 | +3,70% | -19,05% | DEBOLE | 13,8 | 30,0 |
| +10,00% | 83,51 $ | 19/40 | +47,50% | prezzo iniziale | 75,92 $ | 6/19 | +31,58% | -9,09% | DEBOLE | 17,6 | 19,2 |
| +10,00% | 83,51 $ | 19/40 | +47,50% | -5,00% | 72,12 $ | 4/19 | +21,05% | -13,64% | DEBOLE | 17,6 | 23,2 |
| +10,00% | 83,51 $ | 19/40 | +47,50% | -8,00% | 69,85 $ | 1/19 | +5,26% | -16,36% | DEBOLE | 17,6 | 30,0 |
| +10,00% | 83,51 $ | 19/40 | +47,50% | -10,00% | 68,33 $ | 1/19 | +5,26% | -18,18% | DEBOLE | 17,6 | 30,0 |
| +10,00% | 83,51 $ | 19/40 | +47,50% | -15,00% | 64,53 $ | 0/19 | 0,00% | -22,73% | DEBOLE | 17,6 | n/d |
| +15,00% | 87,31 $ | 12/40 | +30,00% | prezzo iniziale | 75,92 $ | 3/12 | +25,00% | -13,04% | DEBOLE | 14,8 | 17,3 |
| +15,00% | 87,31 $ | 12/40 | +30,00% | -5,00% | 72,12 $ | 2/12 | +16,67% | -17,39% | DEBOLE | 14,8 | 18,0 |
| +15,00% | 87,31 $ | 12/40 | +30,00% | -8,00% | 69,85 $ | 0/12 | 0,00% | -20,00% | DEBOLE | 14,8 | n/d |
| +15,00% | 87,31 $ | 12/40 | +30,00% | -10,00% | 68,33 $ | 0/12 | 0,00% | -21,74% | DEBOLE | 14,8 | n/d |
| +15,00% | 87,31 $ | 12/40 | +30,00% | -15,00% | 64,53 $ | 0/12 | 0,00% | -26,09% | DEBOLE | 14,8 | n/d |
| +20,00% | 91,10 $ | 9/40 | +22,50% | prezzo iniziale | 75,92 $ | 1/9 | +11,11% | -16,67% | DEBOLE | 15,0 | 7,0 |
| +20,00% | 91,10 $ | 9/40 | +22,50% | -5,00% | 72,12 $ | 1/9 | +11,11% | -20,83% | DEBOLE | 15,0 | 7,0 |
| +20,00% | 91,10 $ | 9/40 | +22,50% | -8,00% | 69,85 $ | 0/9 | 0,00% | -23,33% | DEBOLE | 15,0 | n/d |
| +20,00% | 91,10 $ | 9/40 | +22,50% | -10,00% | 68,33 $ | 0/9 | 0,00% | -25,00% | DEBOLE | 15,0 | n/d |
| +20,00% | 91,10 $ | 9/40 | +22,50% | -15,00% | 64,53 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 15,0 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +25,00% (9/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 9 poi sono scaricati a -5,00%. Percentuale: +47,37% (9/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06815 $ | 36/40 | +90,00% | +5,00% | 0,07533 $ | 10/36 | +27,78% | +10,53% | DEBOLE | 6,6 | 14,6 |
| -5,00% | 0,06815 $ | 36/40 | +90,00% | +10,00% | 0,07891 $ | 9/36 | +25,00% | +15,79% | DEBOLE | 6,6 | 18,3 |
| -5,00% | 0,06815 $ | 36/40 | +90,00% | +15,00% | 0,08250 $ | 6/36 | +16,67% | +21,05% | DEBOLE | 6,6 | 19,2 |
| -5,00% | 0,06815 $ | 36/40 | +90,00% | +20,00% | 0,08609 $ | 5/36 | +13,89% | +26,32% | DEBOLE | 6,6 | 21,4 |
| -8,00% | 0,06600 $ | 31/40 | +77,50% | +5,00% | 0,07533 $ | 6/31 | +19,35% | +14,13% | DEBOLE | 7,0 | 16,0 |
| -8,00% | 0,06600 $ | 31/40 | +77,50% | +10,00% | 0,07891 $ | 5/31 | +16,13% | +19,57% | DEBOLE | 7,0 | 18,6 |
| -8,00% | 0,06600 $ | 31/40 | +77,50% | +15,00% | 0,08250 $ | 2/31 | +6,45% | +25,00% | DEBOLE | 7,0 | 17,5 |
| -8,00% | 0,06600 $ | 31/40 | +77,50% | +20,00% | 0,08609 $ | 2/31 | +6,45% | +30,43% | DEBOLE | 7,0 | 18,0 |
| -10,00% | 0,06457 $ | 29/40 | +72,50% | +5,00% | 0,07533 $ | 4/29 | +13,79% | +16,67% | DEBOLE | 7,4 | 18,8 |
| -10,00% | 0,06457 $ | 29/40 | +72,50% | +10,00% | 0,07891 $ | 3/29 | +10,34% | +22,22% | DEBOLE | 7,4 | 23,7 |
| -10,00% | 0,06457 $ | 29/40 | +72,50% | +15,00% | 0,08250 $ | 0/29 | 0,00% | +27,78% | DEBOLE | 7,4 | n/d |
| -10,00% | 0,06457 $ | 29/40 | +72,50% | +20,00% | 0,08609 $ | 0/29 | 0,00% | +33,33% | DEBOLE | 7,4 | n/d |
| -15,00% | 0,06098 $ | 24/40 | +60,00% | +5,00% | 0,07533 $ | 2/24 | +8,33% | +23,53% | DEBOLE | 7,4 | 14,0 |
| -15,00% | 0,06098 $ | 24/40 | +60,00% | +10,00% | 0,07891 $ | 1/24 | +4,17% | +29,41% | DEBOLE | 7,4 | 15,0 |
| -15,00% | 0,06098 $ | 24/40 | +60,00% | +15,00% | 0,08250 $ | 0/24 | 0,00% | +35,29% | DEBOLE | 7,4 | n/d |
| -15,00% | 0,06098 $ | 24/40 | +60,00% | +20,00% | 0,08609 $ | 0/24 | 0,00% | +41,18% | DEBOLE | 7,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07533 $ | 22/40 | +55,00% | prezzo iniziale | 0,07174 $ | 18/22 | +81,82% | -4,76% | ALTA | 7,2 | 12,3 |
| +5,00% | 0,07533 $ | 22/40 | +55,00% | -5,00% | 0,06815 $ | 14/22 | +63,64% | -9,52% | MEDIA | 7,2 | 17,4 |
| +5,00% | 0,07533 $ | 22/40 | +55,00% | -8,00% | 0,06600 $ | 10/22 | +45,45% | -12,38% | BASSA | 7,2 | 19,8 |
| +5,00% | 0,07533 $ | 22/40 | +55,00% | -10,00% | 0,06457 $ | 8/22 | +36,36% | -14,29% | BASSA | 7,2 | 22,8 |
| +5,00% | 0,07533 $ | 22/40 | +55,00% | -15,00% | 0,06098 $ | 4/22 | +18,18% | -19,05% | DEBOLE | 7,2 | 23,5 |
| +10,00% | 0,07891 $ | 19/40 | +47,50% | prezzo iniziale | 0,07174 $ | 12/19 | +63,16% | -9,09% | MEDIA | 11,2 | 17,5 |
| +10,00% | 0,07891 $ | 19/40 | +47,50% | -5,00% | 0,06815 $ | 9/19 | +47,37% | -13,64% | BASSA | 11,2 | 20,9 |
| +10,00% | 0,07891 $ | 19/40 | +47,50% | -8,00% | 0,06600 $ | 6/19 | +31,58% | -16,36% | DEBOLE | 11,2 | 21,5 |
| +10,00% | 0,07891 $ | 19/40 | +47,50% | -10,00% | 0,06457 $ | 5/19 | +26,32% | -18,18% | DEBOLE | 11,2 | 22,0 |
| +10,00% | 0,07891 $ | 19/40 | +47,50% | -15,00% | 0,06098 $ | 3/19 | +15,79% | -22,73% | DEBOLE | 11,2 | 24,3 |
| +15,00% | 0,08250 $ | 16/40 | +40,00% | prezzo iniziale | 0,07174 $ | 9/16 | +56,25% | -13,04% | MEDIA | 12,1 | 20,4 |
| +15,00% | 0,08250 $ | 16/40 | +40,00% | -5,00% | 0,06815 $ | 6/16 | +37,50% | -17,39% | BASSA | 12,1 | 22,8 |
| +15,00% | 0,08250 $ | 16/40 | +40,00% | -8,00% | 0,06600 $ | 5/16 | +31,25% | -20,00% | DEBOLE | 12,1 | 22,0 |
| +15,00% | 0,08250 $ | 16/40 | +40,00% | -10,00% | 0,06457 $ | 5/16 | +31,25% | -21,74% | DEBOLE | 12,1 | 22,0 |
| +15,00% | 0,08250 $ | 16/40 | +40,00% | -15,00% | 0,06098 $ | 3/16 | +18,75% | -26,09% | DEBOLE | 12,1 | 24,3 |
| +20,00% | 0,08609 $ | 9/40 | +22,50% | prezzo iniziale | 0,07174 $ | 3/9 | +33,33% | -16,67% | DEBOLE | 16,0 | 24,7 |
| +20,00% | 0,08609 $ | 9/40 | +22,50% | -5,00% | 0,06815 $ | 1/9 | +11,11% | -20,83% | DEBOLE | 16,0 | 29,0 |
| +20,00% | 0,08609 $ | 9/40 | +22,50% | -8,00% | 0,06600 $ | 0/9 | 0,00% | -23,33% | DEBOLE | 16,0 | n/d |
| +20,00% | 0,08609 $ | 9/40 | +22,50% | -10,00% | 0,06457 $ | 0/9 | 0,00% | -25,00% | DEBOLE | 16,0 | n/d |
| +20,00% | 0,08609 $ | 9/40 | +22,50% | -15,00% | 0,06098 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 16,0 | n/d |

---
