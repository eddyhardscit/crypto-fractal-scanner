# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-11 09:20:57 CEST**  
UTC: **2026-07-11 07:20:57 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.935 $ | 70.556 $ | +5,88% | +15,79% | rimbalzo poco frequente | 70.556 $ | 60.935 $ | +9,52% | -13,64% | spike storicamente più resistente |
| SOL | 74,03 $ | 85,72 $ | +9,68% | +15,79% | rimbalzo poco frequente | 85,72 $ | 74,03 $ | +37,50% | -13,64% | scarico possibile |
| DOGE | 0,07059 $ | 0,08174 $ | +13,16% | +15,79% | rimbalzo poco frequente | 0,08174 $ | 0,07059 $ | +64,29% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 1 poi sono rimbalzati fino a +10,00%. Percentuale: +5,88% (1/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 2 poi sono scaricati a -5,00%. Percentuale: +9,52% (2/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.935 $ | 17/40 | +42,50% | +5,00% | 67.349 $ | 6/17 | +35,29% | +10,53% | BASSA | 11,2 | 25,0 |
| -5,00% | 60.935 $ | 17/40 | +42,50% | +10,00% | 70.556 $ | 1/17 | +5,88% | +15,79% | DEBOLE | 11,2 | 30,0 |
| -5,00% | 60.935 $ | 17/40 | +42,50% | +15,00% | 73.763 $ | 0/17 | 0,00% | +21,05% | DEBOLE | 11,2 | n/d |
| -5,00% | 60.935 $ | 17/40 | +42,50% | +20,00% | 76.970 $ | 0/17 | 0,00% | +26,32% | DEBOLE | 11,2 | n/d |
| -8,00% | 59.011 $ | 15/40 | +37,50% | +5,00% | 67.349 $ | 3/15 | +20,00% | +14,13% | DEBOLE | 15,5 | 28,7 |
| -8,00% | 59.011 $ | 15/40 | +37,50% | +10,00% | 70.556 $ | 0/15 | 0,00% | +19,57% | DEBOLE | 15,5 | n/d |
| -8,00% | 59.011 $ | 15/40 | +37,50% | +15,00% | 73.763 $ | 0/15 | 0,00% | +25,00% | DEBOLE | 15,5 | n/d |
| -8,00% | 59.011 $ | 15/40 | +37,50% | +20,00% | 76.970 $ | 0/15 | 0,00% | +30,43% | DEBOLE | 15,5 | n/d |
| -10,00% | 57.728 $ | 13/40 | +32,50% | +5,00% | 67.349 $ | 2/13 | +15,38% | +16,67% | DEBOLE | 17,2 | 30,0 |
| -10,00% | 57.728 $ | 13/40 | +32,50% | +10,00% | 70.556 $ | 0/13 | 0,00% | +22,22% | DEBOLE | 17,2 | n/d |
| -10,00% | 57.728 $ | 13/40 | +32,50% | +15,00% | 73.763 $ | 0/13 | 0,00% | +27,78% | DEBOLE | 17,2 | n/d |
| -10,00% | 57.728 $ | 13/40 | +32,50% | +20,00% | 76.970 $ | 0/13 | 0,00% | +33,33% | DEBOLE | 17,2 | n/d |
| -15,00% | 54.521 $ | 8/40 | +20,00% | +5,00% | 67.349 $ | 0/8 | 0,00% | +23,53% | DEBOLE | 18,6 | n/d |
| -15,00% | 54.521 $ | 8/40 | +20,00% | +10,00% | 70.556 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 18,6 | n/d |
| -15,00% | 54.521 $ | 8/40 | +20,00% | +15,00% | 73.763 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 18,6 | n/d |
| -15,00% | 54.521 $ | 8/40 | +20,00% | +20,00% | 76.970 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 18,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.349 $ | 36/40 | +90,00% | prezzo iniziale | 64.142 $ | 19/36 | +52,78% | -4,76% | MEDIA | 4,9 | 11,8 |
| +5,00% | 67.349 $ | 36/40 | +90,00% | -5,00% | 60.935 $ | 11/36 | +30,56% | -9,52% | DEBOLE | 4,9 | 16,7 |
| +5,00% | 67.349 $ | 36/40 | +90,00% | -8,00% | 59.011 $ | 9/36 | +25,00% | -12,38% | DEBOLE | 4,9 | 19,4 |
| +5,00% | 67.349 $ | 36/40 | +90,00% | -10,00% | 57.728 $ | 8/36 | +22,22% | -14,29% | DEBOLE | 4,9 | 21,9 |
| +5,00% | 67.349 $ | 36/40 | +90,00% | -15,00% | 54.521 $ | 5/36 | +13,89% | -19,05% | DEBOLE | 4,9 | 24,8 |
| +10,00% | 70.556 $ | 21/40 | +52,50% | prezzo iniziale | 64.142 $ | 4/21 | +19,05% | -9,09% | DEBOLE | 6,9 | 16,0 |
| +10,00% | 70.556 $ | 21/40 | +52,50% | -5,00% | 60.935 $ | 2/21 | +9,52% | -13,64% | DEBOLE | 6,9 | 16,0 |
| +10,00% | 70.556 $ | 21/40 | +52,50% | -8,00% | 59.011 $ | 2/21 | +9,52% | -16,36% | DEBOLE | 6,9 | 17,0 |
| +10,00% | 70.556 $ | 21/40 | +52,50% | -10,00% | 57.728 $ | 2/21 | +9,52% | -18,18% | DEBOLE | 6,9 | 17,0 |
| +10,00% | 70.556 $ | 21/40 | +52,50% | -15,00% | 54.521 $ | 2/21 | +9,52% | -22,73% | DEBOLE | 6,9 | 17,5 |
| +15,00% | 73.763 $ | 18/40 | +45,00% | prezzo iniziale | 64.142 $ | 3/18 | +16,67% | -13,04% | DEBOLE | 9,1 | 14,7 |
| +15,00% | 73.763 $ | 18/40 | +45,00% | -5,00% | 60.935 $ | 1/18 | +5,56% | -17,39% | DEBOLE | 9,1 | 11,0 |
| +15,00% | 73.763 $ | 18/40 | +45,00% | -8,00% | 59.011 $ | 1/18 | +5,56% | -20,00% | DEBOLE | 9,1 | 11,0 |
| +15,00% | 73.763 $ | 18/40 | +45,00% | -10,00% | 57.728 $ | 1/18 | +5,56% | -21,74% | DEBOLE | 9,1 | 11,0 |
| +15,00% | 73.763 $ | 18/40 | +45,00% | -15,00% | 54.521 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 9,1 | 11,0 |
| +20,00% | 76.970 $ | 15/40 | +37,50% | prezzo iniziale | 64.142 $ | 1/15 | +6,67% | -16,67% | DEBOLE | 11,2 | 22,0 |
| +20,00% | 76.970 $ | 15/40 | +37,50% | -5,00% | 60.935 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 11,2 | n/d |
| +20,00% | 76.970 $ | 15/40 | +37,50% | -8,00% | 59.011 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 11,2 | n/d |
| +20,00% | 76.970 $ | 15/40 | +37,50% | -10,00% | 57.728 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 11,2 | n/d |
| +20,00% | 76.970 $ | 15/40 | +37,50% | -15,00% | 54.521 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 11,2 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +9,68% (3/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 6 poi sono scaricati a -5,00%. Percentuale: +37,50% (6/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 74,03 $ | 31/40 | +77,50% | +5,00% | 81,83 $ | 6/31 | +19,35% | +10,53% | DEBOLE | 8,4 | 20,3 |
| -5,00% | 74,03 $ | 31/40 | +77,50% | +10,00% | 85,72 $ | 3/31 | +9,68% | +15,79% | DEBOLE | 8,4 | 16,3 |
| -5,00% | 74,03 $ | 31/40 | +77,50% | +15,00% | 89,62 $ | 0/31 | 0,00% | +21,05% | DEBOLE | 8,4 | n/d |
| -5,00% | 74,03 $ | 31/40 | +77,50% | +20,00% | 93,52 $ | 0/31 | 0,00% | +26,32% | DEBOLE | 8,4 | n/d |
| -8,00% | 71,70 $ | 27/40 | +67,50% | +5,00% | 81,83 $ | 4/27 | +14,81% | +14,13% | DEBOLE | 10,6 | 19,8 |
| -8,00% | 71,70 $ | 27/40 | +67,50% | +10,00% | 85,72 $ | 2/27 | +7,41% | +19,57% | DEBOLE | 10,6 | 16,5 |
| -8,00% | 71,70 $ | 27/40 | +67,50% | +15,00% | 89,62 $ | 0/27 | 0,00% | +25,00% | DEBOLE | 10,6 | n/d |
| -8,00% | 71,70 $ | 27/40 | +67,50% | +20,00% | 93,52 $ | 0/27 | 0,00% | +30,43% | DEBOLE | 10,6 | n/d |
| -10,00% | 70,14 $ | 24/40 | +60,00% | +5,00% | 81,83 $ | 3/24 | +12,50% | +16,67% | DEBOLE | 10,8 | 16,3 |
| -10,00% | 70,14 $ | 24/40 | +60,00% | +10,00% | 85,72 $ | 2/24 | +8,33% | +22,22% | DEBOLE | 10,8 | 16,5 |
| -10,00% | 70,14 $ | 24/40 | +60,00% | +15,00% | 89,62 $ | 0/24 | 0,00% | +27,78% | DEBOLE | 10,8 | n/d |
| -10,00% | 70,14 $ | 24/40 | +60,00% | +20,00% | 93,52 $ | 0/24 | 0,00% | +33,33% | DEBOLE | 10,8 | n/d |
| -15,00% | 66,24 $ | 17/40 | +42,50% | +5,00% | 81,83 $ | 2/17 | +11,76% | +23,53% | DEBOLE | 12,8 | 15,5 |
| -15,00% | 66,24 $ | 17/40 | +42,50% | +10,00% | 85,72 $ | 1/17 | +5,88% | +29,41% | DEBOLE | 12,8 | 15,0 |
| -15,00% | 66,24 $ | 17/40 | +42,50% | +15,00% | 89,62 $ | 0/17 | 0,00% | +35,29% | DEBOLE | 12,8 | n/d |
| -15,00% | 66,24 $ | 17/40 | +42,50% | +20,00% | 93,52 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 12,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 81,83 $ | 23/40 | +57,50% | prezzo iniziale | 77,93 $ | 14/23 | +60,87% | -4,76% | MEDIA | 4,6 | 9,5 |
| +5,00% | 81,83 $ | 23/40 | +57,50% | -5,00% | 74,03 $ | 13/23 | +56,52% | -9,52% | MEDIA | 4,6 | 12,8 |
| +5,00% | 81,83 $ | 23/40 | +57,50% | -8,00% | 71,70 $ | 10/23 | +43,48% | -12,38% | BASSA | 4,6 | 14,8 |
| +5,00% | 81,83 $ | 23/40 | +57,50% | -10,00% | 70,14 $ | 8/23 | +34,78% | -14,29% | DEBOLE | 4,6 | 15,9 |
| +5,00% | 81,83 $ | 23/40 | +57,50% | -15,00% | 66,24 $ | 4/23 | +17,39% | -19,05% | DEBOLE | 4,6 | 14,8 |
| +10,00% | 85,72 $ | 16/40 | +40,00% | prezzo iniziale | 77,93 $ | 7/16 | +43,75% | -9,09% | BASSA | 8,5 | 12,4 |
| +10,00% | 85,72 $ | 16/40 | +40,00% | -5,00% | 74,03 $ | 6/16 | +37,50% | -13,64% | BASSA | 8,5 | 14,7 |
| +10,00% | 85,72 $ | 16/40 | +40,00% | -8,00% | 71,70 $ | 5/16 | +31,25% | -16,36% | DEBOLE | 8,5 | 14,6 |
| +10,00% | 85,72 $ | 16/40 | +40,00% | -10,00% | 70,14 $ | 4/16 | +25,00% | -18,18% | DEBOLE | 8,5 | 14,2 |
| +10,00% | 85,72 $ | 16/40 | +40,00% | -15,00% | 66,24 $ | 3/16 | +18,75% | -22,73% | DEBOLE | 8,5 | 15,0 |
| +15,00% | 89,62 $ | 11/40 | +27,50% | prezzo iniziale | 77,93 $ | 3/11 | +27,27% | -13,04% | DEBOLE | 9,6 | 13,0 |
| +15,00% | 89,62 $ | 11/40 | +27,50% | -5,00% | 74,03 $ | 2/11 | +18,18% | -17,39% | DEBOLE | 9,6 | 14,5 |
| +15,00% | 89,62 $ | 11/40 | +27,50% | -8,00% | 71,70 $ | 2/11 | +18,18% | -20,00% | DEBOLE | 9,6 | 14,5 |
| +15,00% | 89,62 $ | 11/40 | +27,50% | -10,00% | 70,14 $ | 1/11 | +9,09% | -21,74% | DEBOLE | 9,6 | 12,0 |
| +15,00% | 89,62 $ | 11/40 | +27,50% | -15,00% | 66,24 $ | 1/11 | +9,09% | -26,09% | DEBOLE | 9,6 | 13,0 |
| +20,00% | 93,52 $ | 9/40 | +22,50% | prezzo iniziale | 77,93 $ | 1/9 | +11,11% | -16,67% | DEBOLE | 11,9 | 11,0 |
| +20,00% | 93,52 $ | 9/40 | +22,50% | -5,00% | 74,03 $ | 1/9 | +11,11% | -20,83% | DEBOLE | 11,9 | 12,0 |
| +20,00% | 93,52 $ | 9/40 | +22,50% | -8,00% | 71,70 $ | 1/9 | +11,11% | -23,33% | DEBOLE | 11,9 | 12,0 |
| +20,00% | 93,52 $ | 9/40 | +22,50% | -10,00% | 70,14 $ | 1/9 | +11,11% | -25,00% | DEBOLE | 11,9 | 12,0 |
| +20,00% | 93,52 $ | 9/40 | +22,50% | -15,00% | 66,24 $ | 1/9 | +11,11% | -29,17% | DEBOLE | 11,9 | 13,0 |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 38 prima sono scesi a -5,00%. Tra quei 38, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +13,16% (5/38). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 14 prima sono saliti a +10,00%. Tra quei 14, 9 poi sono scaricati a -5,00%. Percentuale: +64,29% (9/14). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07059 $ | 38/40 | +95,00% | +5,00% | 0,07803 $ | 7/38 | +18,42% | +10,53% | DEBOLE | 7,0 | 14,3 |
| -5,00% | 0,07059 $ | 38/40 | +95,00% | +10,00% | 0,08174 $ | 5/38 | +13,16% | +15,79% | DEBOLE | 7,0 | 10,0 |
| -5,00% | 0,07059 $ | 38/40 | +95,00% | +15,00% | 0,08546 $ | 5/38 | +13,16% | +21,05% | DEBOLE | 7,0 | 13,6 |
| -5,00% | 0,07059 $ | 38/40 | +95,00% | +20,00% | 0,08917 $ | 5/38 | +13,16% | +26,32% | DEBOLE | 7,0 | 15,2 |
| -8,00% | 0,06837 $ | 37/40 | +92,50% | +5,00% | 0,07803 $ | 5/37 | +13,51% | +14,13% | DEBOLE | 9,0 | 17,0 |
| -8,00% | 0,06837 $ | 37/40 | +92,50% | +10,00% | 0,08174 $ | 3/37 | +8,11% | +19,57% | DEBOLE | 9,0 | 11,0 |
| -8,00% | 0,06837 $ | 37/40 | +92,50% | +15,00% | 0,08546 $ | 3/37 | +8,11% | +25,00% | DEBOLE | 9,0 | 16,3 |
| -8,00% | 0,06837 $ | 37/40 | +92,50% | +20,00% | 0,08917 $ | 3/37 | +8,11% | +30,43% | DEBOLE | 9,0 | 18,3 |
| -10,00% | 0,06688 $ | 34/40 | +85,00% | +5,00% | 0,07803 $ | 2/34 | +5,88% | +16,67% | DEBOLE | 10,1 | 26,5 |
| -10,00% | 0,06688 $ | 34/40 | +85,00% | +10,00% | 0,08174 $ | 0/34 | 0,00% | +22,22% | DEBOLE | 10,1 | n/d |
| -10,00% | 0,06688 $ | 34/40 | +85,00% | +15,00% | 0,08546 $ | 0/34 | 0,00% | +27,78% | DEBOLE | 10,1 | n/d |
| -10,00% | 0,06688 $ | 34/40 | +85,00% | +20,00% | 0,08917 $ | 0/34 | 0,00% | +33,33% | DEBOLE | 10,1 | n/d |
| -15,00% | 0,06316 $ | 29/40 | +72,50% | +5,00% | 0,07803 $ | 1/29 | +3,45% | +23,53% | DEBOLE | 9,6 | 25,0 |
| -15,00% | 0,06316 $ | 29/40 | +72,50% | +10,00% | 0,08174 $ | 0/29 | 0,00% | +29,41% | DEBOLE | 9,6 | n/d |
| -15,00% | 0,06316 $ | 29/40 | +72,50% | +15,00% | 0,08546 $ | 0/29 | 0,00% | +35,29% | DEBOLE | 9,6 | n/d |
| -15,00% | 0,06316 $ | 29/40 | +72,50% | +20,00% | 0,08917 $ | 0/29 | 0,00% | +41,18% | DEBOLE | 9,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07803 $ | 21/40 | +52,50% | prezzo iniziale | 0,07431 $ | 17/21 | +80,95% | -4,76% | ALTA | 5,3 | 8,8 |
| +5,00% | 0,07803 $ | 21/40 | +52,50% | -5,00% | 0,07059 $ | 16/21 | +76,19% | -9,52% | ALTA | 5,3 | 13,0 |
| +5,00% | 0,07803 $ | 21/40 | +52,50% | -8,00% | 0,06837 $ | 15/21 | +71,43% | -12,38% | ALTA | 5,3 | 12,5 |
| +5,00% | 0,07803 $ | 21/40 | +52,50% | -10,00% | 0,06688 $ | 14/21 | +66,67% | -14,29% | ALTA | 5,3 | 14,0 |
| +5,00% | 0,07803 $ | 21/40 | +52,50% | -15,00% | 0,06316 $ | 10/21 | +47,62% | -19,05% | BASSA | 5,3 | 11,6 |
| +10,00% | 0,08174 $ | 14/40 | +35,00% | prezzo iniziale | 0,07431 $ | 10/14 | +71,43% | -9,09% | ALTA | 7,7 | 10,8 |
| +10,00% | 0,08174 $ | 14/40 | +35,00% | -5,00% | 0,07059 $ | 9/14 | +64,29% | -13,64% | MEDIA | 7,7 | 14,3 |
| +10,00% | 0,08174 $ | 14/40 | +35,00% | -8,00% | 0,06837 $ | 9/14 | +64,29% | -16,36% | MEDIA | 7,7 | 14,9 |
| +10,00% | 0,08174 $ | 14/40 | +35,00% | -10,00% | 0,06688 $ | 8/14 | +57,14% | -18,18% | MEDIA | 7,7 | 15,8 |
| +10,00% | 0,08174 $ | 14/40 | +35,00% | -15,00% | 0,06316 $ | 5/14 | +35,71% | -22,73% | BASSA | 7,7 | 14,0 |
| +15,00% | 0,08546 $ | 10/40 | +25,00% | prezzo iniziale | 0,07431 $ | 5/10 | +50,00% | -13,04% | MEDIA | 10,8 | 13,8 |
| +15,00% | 0,08546 $ | 10/40 | +25,00% | -5,00% | 0,07059 $ | 5/10 | +50,00% | -17,39% | MEDIA | 10,8 | 15,6 |
| +15,00% | 0,08546 $ | 10/40 | +25,00% | -8,00% | 0,06837 $ | 5/10 | +50,00% | -20,00% | MEDIA | 10,8 | 16,0 |
| +15,00% | 0,08546 $ | 10/40 | +25,00% | -10,00% | 0,06688 $ | 4/10 | +40,00% | -21,74% | BASSA | 10,8 | 18,0 |
| +15,00% | 0,08546 $ | 10/40 | +25,00% | -15,00% | 0,06316 $ | 3/10 | +30,00% | -26,09% | DEBOLE | 10,8 | 17,3 |
| +20,00% | 0,08917 $ | 7/40 | +17,50% | prezzo iniziale | 0,07431 $ | 3/7 | +42,86% | -16,67% | BASSA | 13,0 | 16,7 |
| +20,00% | 0,08917 $ | 7/40 | +17,50% | -5,00% | 0,07059 $ | 2/7 | +28,57% | -20,83% | DEBOLE | 13,0 | 11,5 |
| +20,00% | 0,08917 $ | 7/40 | +17,50% | -8,00% | 0,06837 $ | 2/7 | +28,57% | -23,33% | DEBOLE | 13,0 | 12,0 |
| +20,00% | 0,08917 $ | 7/40 | +17,50% | -10,00% | 0,06688 $ | 2/7 | +28,57% | -25,00% | DEBOLE | 13,0 | 12,5 |
| +20,00% | 0,08917 $ | 7/40 | +17,50% | -15,00% | 0,06316 $ | 2/7 | +28,57% | -29,17% | DEBOLE | 13,0 | 13,0 |

---
