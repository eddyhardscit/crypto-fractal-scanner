# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-15 09:26:04 CEST**  
UTC: **2026-07-15 07:26:04 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.366 $ | 71.055 $ | +46,43% | +15,79% | rimbalzo debole | 71.055 $ | 61.366 $ | +25,00% | -13,64% | spike storicamente più resistente |
| SOL | 73,80 $ | 85,45 $ | +17,86% | +15,79% | rimbalzo poco frequente | 85,45 $ | 73,80 $ | +21,05% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07039 $ | 0,08150 $ | +13,89% | +15,79% | rimbalzo poco frequente | 0,08150 $ | 0,07039 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 13 poi sono rimbalzati fino a +10,00%. Percentuale: +46,43% (13/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 6 poi sono scaricati a -5,00%. Percentuale: +25,00% (6/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.366 $ | 28/40 | +70,00% | +5,00% | 67.826 $ | 16/28 | +57,14% | +10,53% | MEDIA | 8,5 | 22,5 |
| -5,00% | 61.366 $ | 28/40 | +70,00% | +10,00% | 71.055 $ | 13/28 | +46,43% | +15,79% | BASSA | 8,5 | 25,0 |
| -5,00% | 61.366 $ | 28/40 | +70,00% | +15,00% | 74.285 $ | 7/28 | +25,00% | +21,05% | DEBOLE | 8,5 | 24,7 |
| -5,00% | 61.366 $ | 28/40 | +70,00% | +20,00% | 77.515 $ | 5/28 | +17,86% | +26,32% | DEBOLE | 8,5 | 26,0 |
| -8,00% | 59.428 $ | 21/40 | +52,50% | +5,00% | 67.826 $ | 9/21 | +42,86% | +14,13% | BASSA | 9,9 | 22,4 |
| -8,00% | 59.428 $ | 21/40 | +52,50% | +10,00% | 71.055 $ | 6/21 | +28,57% | +19,57% | DEBOLE | 9,9 | 23,2 |
| -8,00% | 59.428 $ | 21/40 | +52,50% | +15,00% | 74.285 $ | 3/21 | +14,29% | +25,00% | DEBOLE | 9,9 | 22,0 |
| -8,00% | 59.428 $ | 21/40 | +52,50% | +20,00% | 77.515 $ | 2/21 | +9,52% | +30,43% | DEBOLE | 9,9 | 21,0 |
| -10,00% | 58.136 $ | 16/40 | +40,00% | +5,00% | 67.826 $ | 5/16 | +31,25% | +16,67% | DEBOLE | 11,1 | 24,0 |
| -10,00% | 58.136 $ | 16/40 | +40,00% | +10,00% | 71.055 $ | 3/16 | +18,75% | +22,22% | DEBOLE | 11,1 | 26,0 |
| -10,00% | 58.136 $ | 16/40 | +40,00% | +15,00% | 74.285 $ | 1/16 | +6,25% | +27,78% | DEBOLE | 11,1 | 26,0 |
| -10,00% | 58.136 $ | 16/40 | +40,00% | +20,00% | 77.515 $ | 1/16 | +6,25% | +33,33% | DEBOLE | 11,1 | 26,0 |
| -15,00% | 54.906 $ | 10/40 | +25,00% | +5,00% | 67.826 $ | 1/10 | +10,00% | +23,53% | DEBOLE | 15,5 | 30,0 |
| -15,00% | 54.906 $ | 10/40 | +25,00% | +10,00% | 71.055 $ | 0/10 | 0,00% | +29,41% | DEBOLE | 15,5 | n/d |
| -15,00% | 54.906 $ | 10/40 | +25,00% | +15,00% | 74.285 $ | 0/10 | 0,00% | +35,29% | DEBOLE | 15,5 | n/d |
| -15,00% | 54.906 $ | 10/40 | +25,00% | +20,00% | 77.515 $ | 0/10 | 0,00% | +41,18% | DEBOLE | 15,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.826 $ | 32/40 | +80,00% | prezzo iniziale | 64.596 $ | 21/32 | +65,62% | -4,76% | ALTA | 9,1 | 13,6 |
| +5,00% | 67.826 $ | 32/40 | +80,00% | -5,00% | 61.366 $ | 14/32 | +43,75% | -9,52% | BASSA | 9,1 | 14,3 |
| +5,00% | 67.826 $ | 32/40 | +80,00% | -8,00% | 59.428 $ | 9/32 | +28,12% | -12,38% | DEBOLE | 9,1 | 14,3 |
| +5,00% | 67.826 $ | 32/40 | +80,00% | -10,00% | 58.136 $ | 6/32 | +18,75% | -14,29% | DEBOLE | 9,1 | 18,5 |
| +5,00% | 67.826 $ | 32/40 | +80,00% | -15,00% | 54.906 $ | 3/32 | +9,38% | -19,05% | DEBOLE | 9,1 | 23,0 |
| +10,00% | 71.055 $ | 24/40 | +60,00% | prezzo iniziale | 64.596 $ | 8/24 | +33,33% | -9,09% | DEBOLE | 15,6 | 13,8 |
| +10,00% | 71.055 $ | 24/40 | +60,00% | -5,00% | 61.366 $ | 6/24 | +25,00% | -13,64% | DEBOLE | 15,6 | 13,8 |
| +10,00% | 71.055 $ | 24/40 | +60,00% | -8,00% | 59.428 $ | 4/24 | +16,67% | -16,36% | DEBOLE | 15,6 | 16,2 |
| +10,00% | 71.055 $ | 24/40 | +60,00% | -10,00% | 58.136 $ | 3/24 | +12,50% | -18,18% | DEBOLE | 15,6 | 18,3 |
| +10,00% | 71.055 $ | 24/40 | +60,00% | -15,00% | 54.906 $ | 2/24 | +8,33% | -22,73% | DEBOLE | 15,6 | 19,5 |
| +15,00% | 74.285 $ | 14/40 | +35,00% | prezzo iniziale | 64.596 $ | 2/14 | +14,29% | -13,04% | DEBOLE | 15,1 | 17,0 |
| +15,00% | 74.285 $ | 14/40 | +35,00% | -5,00% | 61.366 $ | 0/14 | 0,00% | -17,39% | DEBOLE | 15,1 | n/d |
| +15,00% | 74.285 $ | 14/40 | +35,00% | -8,00% | 59.428 $ | 0/14 | 0,00% | -20,00% | DEBOLE | 15,1 | n/d |
| +15,00% | 74.285 $ | 14/40 | +35,00% | -10,00% | 58.136 $ | 0/14 | 0,00% | -21,74% | DEBOLE | 15,1 | n/d |
| +15,00% | 74.285 $ | 14/40 | +35,00% | -15,00% | 54.906 $ | 0/14 | 0,00% | -26,09% | DEBOLE | 15,1 | n/d |
| +20,00% | 77.515 $ | 10/40 | +25,00% | prezzo iniziale | 64.596 $ | 0/10 | 0,00% | -16,67% | DEBOLE | 16,0 | n/d |
| +20,00% | 77.515 $ | 10/40 | +25,00% | -5,00% | 61.366 $ | 0/10 | 0,00% | -20,83% | DEBOLE | 16,0 | n/d |
| +20,00% | 77.515 $ | 10/40 | +25,00% | -8,00% | 59.428 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 16,0 | n/d |
| +20,00% | 77.515 $ | 10/40 | +25,00% | -10,00% | 58.136 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 16,0 | n/d |
| +20,00% | 77.515 $ | 10/40 | +25,00% | -15,00% | 54.906 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 16,0 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +17,86% (5/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 4 poi sono scaricati a -5,00%. Percentuale: +21,05% (4/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,80 $ | 28/40 | +70,00% | +5,00% | 81,56 $ | 11/28 | +39,29% | +10,53% | BASSA | 7,7 | 24,7 |
| -5,00% | 73,80 $ | 28/40 | +70,00% | +10,00% | 85,45 $ | 5/28 | +17,86% | +15,79% | DEBOLE | 7,7 | 21,4 |
| -5,00% | 73,80 $ | 28/40 | +70,00% | +15,00% | 89,33 $ | 4/28 | +14,29% | +21,05% | DEBOLE | 7,7 | 21,5 |
| -5,00% | 73,80 $ | 28/40 | +70,00% | +20,00% | 93,22 $ | 2/28 | +7,14% | +26,32% | DEBOLE | 7,7 | 23,0 |
| -8,00% | 71,47 $ | 22/40 | +55,00% | +5,00% | 81,56 $ | 4/22 | +18,18% | +14,13% | DEBOLE | 10,0 | 23,0 |
| -8,00% | 71,47 $ | 22/40 | +55,00% | +10,00% | 85,45 $ | 3/22 | +13,64% | +19,57% | DEBOLE | 10,0 | 22,0 |
| -8,00% | 71,47 $ | 22/40 | +55,00% | +15,00% | 89,33 $ | 2/22 | +9,09% | +25,00% | DEBOLE | 10,0 | 22,0 |
| -8,00% | 71,47 $ | 22/40 | +55,00% | +20,00% | 93,22 $ | 2/22 | +9,09% | +30,43% | DEBOLE | 10,0 | 23,0 |
| -10,00% | 69,91 $ | 17/40 | +42,50% | +5,00% | 81,56 $ | 1/17 | +5,88% | +16,67% | DEBOLE | 10,5 | 29,0 |
| -10,00% | 69,91 $ | 17/40 | +42,50% | +10,00% | 85,45 $ | 0/17 | 0,00% | +22,22% | DEBOLE | 10,5 | n/d |
| -10,00% | 69,91 $ | 17/40 | +42,50% | +15,00% | 89,33 $ | 0/17 | 0,00% | +27,78% | DEBOLE | 10,5 | n/d |
| -10,00% | 69,91 $ | 17/40 | +42,50% | +20,00% | 93,22 $ | 0/17 | 0,00% | +33,33% | DEBOLE | 10,5 | n/d |
| -15,00% | 66,03 $ | 11/40 | +27,50% | +5,00% | 81,56 $ | 0/11 | 0,00% | +23,53% | DEBOLE | 12,1 | n/d |
| -15,00% | 66,03 $ | 11/40 | +27,50% | +10,00% | 85,45 $ | 0/11 | 0,00% | +29,41% | DEBOLE | 12,1 | n/d |
| -15,00% | 66,03 $ | 11/40 | +27,50% | +15,00% | 89,33 $ | 0/11 | 0,00% | +35,29% | DEBOLE | 12,1 | n/d |
| -15,00% | 66,03 $ | 11/40 | +27,50% | +20,00% | 93,22 $ | 0/11 | 0,00% | +41,18% | DEBOLE | 12,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 81,56 $ | 26/40 | +65,00% | prezzo iniziale | 77,68 $ | 9/26 | +34,62% | -4,76% | DEBOLE | 10,4 | 10,9 |
| +5,00% | 81,56 $ | 26/40 | +65,00% | -5,00% | 73,80 $ | 8/26 | +30,77% | -9,52% | DEBOLE | 10,4 | 11,6 |
| +5,00% | 81,56 $ | 26/40 | +65,00% | -8,00% | 71,47 $ | 7/26 | +26,92% | -12,38% | DEBOLE | 10,4 | 17,1 |
| +5,00% | 81,56 $ | 26/40 | +65,00% | -10,00% | 69,91 $ | 4/26 | +15,38% | -14,29% | DEBOLE | 10,4 | 18,0 |
| +5,00% | 81,56 $ | 26/40 | +65,00% | -15,00% | 66,03 $ | 3/26 | +11,54% | -19,05% | DEBOLE | 10,4 | 25,7 |
| +10,00% | 85,45 $ | 19/40 | +47,50% | prezzo iniziale | 77,68 $ | 4/19 | +21,05% | -9,09% | DEBOLE | 10,3 | 7,5 |
| +10,00% | 85,45 $ | 19/40 | +47,50% | -5,00% | 73,80 $ | 4/19 | +21,05% | -13,64% | DEBOLE | 10,3 | 8,8 |
| +10,00% | 85,45 $ | 19/40 | +47,50% | -8,00% | 71,47 $ | 4/19 | +21,05% | -16,36% | DEBOLE | 10,3 | 16,0 |
| +10,00% | 85,45 $ | 19/40 | +47,50% | -10,00% | 69,91 $ | 2/19 | +10,53% | -18,18% | DEBOLE | 10,3 | 12,0 |
| +10,00% | 85,45 $ | 19/40 | +47,50% | -15,00% | 66,03 $ | 1/19 | +5,26% | -22,73% | DEBOLE | 10,3 | 28,0 |
| +15,00% | 89,33 $ | 14/40 | +35,00% | prezzo iniziale | 77,68 $ | 1/14 | +7,14% | -13,04% | DEBOLE | 9,8 | 10,0 |
| +15,00% | 89,33 $ | 14/40 | +35,00% | -5,00% | 73,80 $ | 1/14 | +7,14% | -17,39% | DEBOLE | 9,8 | 10,0 |
| +15,00% | 89,33 $ | 14/40 | +35,00% | -8,00% | 71,47 $ | 1/14 | +7,14% | -20,00% | DEBOLE | 9,8 | 30,0 |
| +15,00% | 89,33 $ | 14/40 | +35,00% | -10,00% | 69,91 $ | 0/14 | 0,00% | -21,74% | DEBOLE | 9,8 | n/d |
| +15,00% | 89,33 $ | 14/40 | +35,00% | -15,00% | 66,03 $ | 0/14 | 0,00% | -26,09% | DEBOLE | 9,8 | n/d |
| +20,00% | 93,22 $ | 12/40 | +30,00% | prezzo iniziale | 77,68 $ | 1/12 | +8,33% | -16,67% | DEBOLE | 9,7 | 10,0 |
| +20,00% | 93,22 $ | 12/40 | +30,00% | -5,00% | 73,80 $ | 1/12 | +8,33% | -20,83% | DEBOLE | 9,7 | 10,0 |
| +20,00% | 93,22 $ | 12/40 | +30,00% | -8,00% | 71,47 $ | 1/12 | +8,33% | -23,33% | DEBOLE | 9,7 | 30,0 |
| +20,00% | 93,22 $ | 12/40 | +30,00% | -10,00% | 69,91 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 9,7 | n/d |
| +20,00% | 93,22 $ | 12/40 | +30,00% | -15,00% | 66,03 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 9,7 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +13,89% (5/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 14 prima sono saliti a +10,00%. Tra quei 14, 7 poi sono scaricati a -5,00%. Percentuale: +50,00% (7/14). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07039 $ | 36/40 | +90,00% | +5,00% | 0,07779 $ | 7/36 | +19,44% | +10,53% | DEBOLE | 5,0 | 13,0 |
| -5,00% | 0,07039 $ | 36/40 | +90,00% | +10,00% | 0,08150 $ | 5/36 | +13,89% | +15,79% | DEBOLE | 5,0 | 15,4 |
| -5,00% | 0,07039 $ | 36/40 | +90,00% | +15,00% | 0,08520 $ | 3/36 | +8,33% | +21,05% | DEBOLE | 5,0 | 15,7 |
| -5,00% | 0,07039 $ | 36/40 | +90,00% | +20,00% | 0,08891 $ | 3/36 | +8,33% | +26,32% | DEBOLE | 5,0 | 17,0 |
| -8,00% | 0,06816 $ | 35/40 | +87,50% | +5,00% | 0,07779 $ | 5/35 | +14,29% | +14,13% | DEBOLE | 6,6 | 14,8 |
| -8,00% | 0,06816 $ | 35/40 | +87,50% | +10,00% | 0,08150 $ | 4/35 | +11,43% | +19,57% | DEBOLE | 6,6 | 12,5 |
| -8,00% | 0,06816 $ | 35/40 | +87,50% | +15,00% | 0,08520 $ | 2/35 | +5,71% | +25,00% | DEBOLE | 6,6 | 9,0 |
| -8,00% | 0,06816 $ | 35/40 | +87,50% | +20,00% | 0,08891 $ | 2/35 | +5,71% | +30,43% | DEBOLE | 6,6 | 11,0 |
| -10,00% | 0,06668 $ | 32/40 | +80,00% | +5,00% | 0,07779 $ | 2/32 | +6,25% | +16,67% | DEBOLE | 7,2 | 18,0 |
| -10,00% | 0,06668 $ | 32/40 | +80,00% | +10,00% | 0,08150 $ | 2/32 | +6,25% | +22,22% | DEBOLE | 7,2 | 18,5 |
| -10,00% | 0,06668 $ | 32/40 | +80,00% | +15,00% | 0,08520 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 7,2 | n/d |
| -10,00% | 0,06668 $ | 32/40 | +80,00% | +20,00% | 0,08891 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 7,2 | n/d |
| -15,00% | 0,06298 $ | 31/40 | +77,50% | +5,00% | 0,07779 $ | 2/31 | +6,45% | +23,53% | DEBOLE | 8,5 | 18,0 |
| -15,00% | 0,06298 $ | 31/40 | +77,50% | +10,00% | 0,08150 $ | 2/31 | +6,45% | +29,41% | DEBOLE | 8,5 | 18,5 |
| -15,00% | 0,06298 $ | 31/40 | +77,50% | +15,00% | 0,08520 $ | 0/31 | 0,00% | +35,29% | DEBOLE | 8,5 | n/d |
| -15,00% | 0,06298 $ | 31/40 | +77,50% | +20,00% | 0,08891 $ | 0/31 | 0,00% | +41,18% | DEBOLE | 8,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07779 $ | 18/40 | +45,00% | prezzo iniziale | 0,07409 $ | 16/18 | +88,89% | -4,76% | ALTA | 3,4 | 10,4 |
| +5,00% | 0,07779 $ | 18/40 | +45,00% | -5,00% | 0,07039 $ | 12/18 | +66,67% | -9,52% | ALTA | 3,4 | 10,3 |
| +5,00% | 0,07779 $ | 18/40 | +45,00% | -8,00% | 0,06816 $ | 12/18 | +66,67% | -12,38% | ALTA | 3,4 | 11,6 |
| +5,00% | 0,07779 $ | 18/40 | +45,00% | -10,00% | 0,06668 $ | 10/18 | +55,56% | -14,29% | MEDIA | 3,4 | 13,0 |
| +5,00% | 0,07779 $ | 18/40 | +45,00% | -15,00% | 0,06298 $ | 9/18 | +50,00% | -19,05% | MEDIA | 3,4 | 12,7 |
| +10,00% | 0,08150 $ | 14/40 | +35,00% | prezzo iniziale | 0,07409 $ | 11/14 | +78,57% | -9,09% | ALTA | 8,9 | 13,1 |
| +10,00% | 0,08150 $ | 14/40 | +35,00% | -5,00% | 0,07039 $ | 7/14 | +50,00% | -13,64% | MEDIA | 8,9 | 10,9 |
| +10,00% | 0,08150 $ | 14/40 | +35,00% | -8,00% | 0,06816 $ | 7/14 | +50,00% | -16,36% | MEDIA | 8,9 | 11,7 |
| +10,00% | 0,08150 $ | 14/40 | +35,00% | -10,00% | 0,06668 $ | 6/14 | +42,86% | -18,18% | BASSA | 8,9 | 13,0 |
| +10,00% | 0,08150 $ | 14/40 | +35,00% | -15,00% | 0,06298 $ | 5/14 | +35,71% | -22,73% | BASSA | 8,9 | 12,0 |
| +15,00% | 0,08520 $ | 9/40 | +22,50% | prezzo iniziale | 0,07409 $ | 5/9 | +55,56% | -13,04% | MEDIA | 12,8 | 18,4 |
| +15,00% | 0,08520 $ | 9/40 | +22,50% | -5,00% | 0,07039 $ | 3/9 | +33,33% | -17,39% | DEBOLE | 12,8 | 20,3 |
| +15,00% | 0,08520 $ | 9/40 | +22,50% | -8,00% | 0,06816 $ | 2/9 | +22,22% | -20,00% | DEBOLE | 12,8 | 17,0 |
| +15,00% | 0,08520 $ | 9/40 | +22,50% | -10,00% | 0,06668 $ | 2/9 | +22,22% | -21,74% | DEBOLE | 12,8 | 17,0 |
| +15,00% | 0,08520 $ | 9/40 | +22,50% | -15,00% | 0,06298 $ | 2/9 | +22,22% | -26,09% | DEBOLE | 12,8 | 17,5 |
| +20,00% | 0,08891 $ | 6/40 | +15,00% | prezzo iniziale | 0,07409 $ | 2/6 | +33,33% | -16,67% | DEBOLE | 14,5 | 11,5 |
| +20,00% | 0,08891 $ | 6/40 | +15,00% | -5,00% | 0,07039 $ | 2/6 | +33,33% | -20,83% | DEBOLE | 14,5 | 17,5 |
| +20,00% | 0,08891 $ | 6/40 | +15,00% | -8,00% | 0,06816 $ | 1/6 | +16,67% | -23,33% | DEBOLE | 14,5 | 8,0 |
| +20,00% | 0,08891 $ | 6/40 | +15,00% | -10,00% | 0,06668 $ | 1/6 | +16,67% | -25,00% | DEBOLE | 14,5 | 8,0 |
| +20,00% | 0,08891 $ | 6/40 | +15,00% | -15,00% | 0,06298 $ | 1/6 | +16,67% | -29,17% | DEBOLE | 14,5 | 9,0 |

---
