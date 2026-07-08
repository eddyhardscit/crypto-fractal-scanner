# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-08 10:40:05 CEST**  
UTC: **2026-07-08 08:40:05 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 58.805 $ | 68.090 $ | +35,00% | +15,79% | rimbalzo debole | 68.090 $ | 58.805 $ | +23,08% | -13,64% | spike storicamente più resistente |
| SOL | 73,13 $ | 84,68 $ | +12,00% | +15,79% | rimbalzo poco frequente | 84,68 $ | 73,13 $ | +16,67% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06773 $ | 0,07842 $ | +16,67% | +15,79% | rimbalzo poco frequente | 0,07842 $ | 0,06773 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 6 poi sono scaricati a -5,00%. Percentuale: +23,08% (6/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 58.805 $ | 20/40 | +50,00% | +5,00% | 64.995 $ | 8/20 | +40,00% | +10,53% | BASSA | 10,9 | 12,4 |
| -5,00% | 58.805 $ | 20/40 | +50,00% | +10,00% | 68.090 $ | 7/20 | +35,00% | +15,79% | BASSA | 10,9 | 15,0 |
| -5,00% | 58.805 $ | 20/40 | +50,00% | +15,00% | 71.185 $ | 5/20 | +25,00% | +21,05% | DEBOLE | 10,9 | 16,0 |
| -5,00% | 58.805 $ | 20/40 | +50,00% | +20,00% | 74.280 $ | 3/20 | +15,00% | +26,32% | DEBOLE | 10,9 | 16,0 |
| -8,00% | 56.948 $ | 14/40 | +35,00% | +5,00% | 64.995 $ | 4/14 | +28,57% | +14,13% | DEBOLE | 12,2 | 10,2 |
| -8,00% | 56.948 $ | 14/40 | +35,00% | +10,00% | 68.090 $ | 4/14 | +28,57% | +19,57% | DEBOLE | 12,2 | 13,2 |
| -8,00% | 56.948 $ | 14/40 | +35,00% | +15,00% | 71.185 $ | 3/14 | +21,43% | +25,00% | DEBOLE | 12,2 | 17,0 |
| -8,00% | 56.948 $ | 14/40 | +35,00% | +20,00% | 74.280 $ | 2/14 | +14,29% | +30,43% | DEBOLE | 12,2 | 18,5 |
| -10,00% | 55.710 $ | 10/40 | +25,00% | +5,00% | 64.995 $ | 2/10 | +20,00% | +16,67% | DEBOLE | 12,6 | 14,5 |
| -10,00% | 55.710 $ | 10/40 | +25,00% | +10,00% | 68.090 $ | 2/10 | +20,00% | +22,22% | DEBOLE | 12,6 | 20,0 |
| -10,00% | 55.710 $ | 10/40 | +25,00% | +15,00% | 71.185 $ | 2/10 | +20,00% | +27,78% | DEBOLE | 12,6 | 20,5 |
| -10,00% | 55.710 $ | 10/40 | +25,00% | +20,00% | 74.280 $ | 1/10 | +10,00% | +33,33% | DEBOLE | 12,6 | 26,0 |
| -15,00% | 52.615 $ | 8/40 | +20,00% | +5,00% | 64.995 $ | 2/8 | +25,00% | +23,53% | DEBOLE | 13,0 | 14,5 |
| -15,00% | 52.615 $ | 8/40 | +20,00% | +10,00% | 68.090 $ | 2/8 | +25,00% | +29,41% | DEBOLE | 13,0 | 20,0 |
| -15,00% | 52.615 $ | 8/40 | +20,00% | +15,00% | 71.185 $ | 2/8 | +25,00% | +35,29% | DEBOLE | 13,0 | 20,5 |
| -15,00% | 52.615 $ | 8/40 | +20,00% | +20,00% | 74.280 $ | 1/8 | +12,50% | +41,18% | DEBOLE | 13,0 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 64.995 $ | 35/40 | +87,50% | prezzo iniziale | 61.900 $ | 21/35 | +60,00% | -4,76% | MEDIA | 4,3 | 14,1 |
| +5,00% | 64.995 $ | 35/40 | +87,50% | -5,00% | 58.805 $ | 13/35 | +37,14% | -9,52% | BASSA | 4,3 | 15,9 |
| +5,00% | 64.995 $ | 35/40 | +87,50% | -8,00% | 56.948 $ | 10/35 | +28,57% | -12,38% | DEBOLE | 4,3 | 18,0 |
| +5,00% | 64.995 $ | 35/40 | +87,50% | -10,00% | 55.710 $ | 6/35 | +17,14% | -14,29% | DEBOLE | 4,3 | 17,8 |
| +5,00% | 64.995 $ | 35/40 | +87,50% | -15,00% | 52.615 $ | 4/35 | +11,43% | -19,05% | DEBOLE | 4,3 | 17,0 |
| +10,00% | 68.090 $ | 26/40 | +65,00% | prezzo iniziale | 61.900 $ | 10/26 | +38,46% | -9,09% | BASSA | 8,7 | 18,2 |
| +10,00% | 68.090 $ | 26/40 | +65,00% | -5,00% | 58.805 $ | 6/26 | +23,08% | -13,64% | DEBOLE | 8,7 | 17,0 |
| +10,00% | 68.090 $ | 26/40 | +65,00% | -8,00% | 56.948 $ | 5/26 | +19,23% | -16,36% | DEBOLE | 8,7 | 19,4 |
| +10,00% | 68.090 $ | 26/40 | +65,00% | -10,00% | 55.710 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 8,7 | 22,0 |
| +10,00% | 68.090 $ | 26/40 | +65,00% | -15,00% | 52.615 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 8,7 | 24,0 |
| +15,00% | 71.185 $ | 21/40 | +52,50% | prezzo iniziale | 61.900 $ | 6/21 | +28,57% | -13,04% | DEBOLE | 11,7 | 20,7 |
| +15,00% | 71.185 $ | 21/40 | +52,50% | -5,00% | 58.805 $ | 4/21 | +19,05% | -17,39% | DEBOLE | 11,7 | 22,2 |
| +15,00% | 71.185 $ | 21/40 | +52,50% | -8,00% | 56.948 $ | 2/21 | +9,52% | -20,00% | DEBOLE | 11,7 | 20,5 |
| +15,00% | 71.185 $ | 21/40 | +52,50% | -10,00% | 55.710 $ | 1/21 | +4,76% | -21,74% | DEBOLE | 11,7 | 21,0 |
| +15,00% | 71.185 $ | 21/40 | +52,50% | -15,00% | 52.615 $ | 0/21 | 0,00% | -26,09% | DEBOLE | 11,7 | n/d |
| +20,00% | 74.280 $ | 14/40 | +35,00% | prezzo iniziale | 61.900 $ | 1/14 | +7,14% | -16,67% | DEBOLE | 12,6 | 16,0 |
| +20,00% | 74.280 $ | 14/40 | +35,00% | -5,00% | 58.805 $ | 1/14 | +7,14% | -20,83% | DEBOLE | 12,6 | 28,0 |
| +20,00% | 74.280 $ | 14/40 | +35,00% | -8,00% | 56.948 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 12,6 | n/d |
| +20,00% | 74.280 $ | 14/40 | +35,00% | -10,00% | 55.710 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 12,6 | n/d |
| +20,00% | 74.280 $ | 14/40 | +35,00% | -15,00% | 52.615 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 12,6 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +12,00% (3/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 18 prima sono saliti a +10,00%. Tra quei 18, 3 poi sono scaricati a -5,00%. Percentuale: +16,67% (3/18). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,13 $ | 25/40 | +62,50% | +5,00% | 80,83 $ | 6/25 | +24,00% | +10,53% | DEBOLE | 7,2 | 13,7 |
| -5,00% | 73,13 $ | 25/40 | +62,50% | +10,00% | 84,68 $ | 3/25 | +12,00% | +15,79% | DEBOLE | 7,2 | 11,7 |
| -5,00% | 73,13 $ | 25/40 | +62,50% | +15,00% | 88,53 $ | 2/25 | +8,00% | +21,05% | DEBOLE | 7,2 | 11,5 |
| -5,00% | 73,13 $ | 25/40 | +62,50% | +20,00% | 92,38 $ | 1/25 | +4,00% | +26,32% | DEBOLE | 7,2 | 10,0 |
| -8,00% | 70,82 $ | 22/40 | +55,00% | +5,00% | 80,83 $ | 3/22 | +13,64% | +14,13% | DEBOLE | 10,8 | 19,3 |
| -8,00% | 70,82 $ | 22/40 | +55,00% | +10,00% | 84,68 $ | 2/22 | +9,09% | +19,57% | DEBOLE | 10,8 | 15,0 |
| -8,00% | 70,82 $ | 22/40 | +55,00% | +15,00% | 88,53 $ | 1/22 | +4,55% | +25,00% | DEBOLE | 10,8 | 15,0 |
| -8,00% | 70,82 $ | 22/40 | +55,00% | +20,00% | 92,38 $ | 0/22 | 0,00% | +30,43% | DEBOLE | 10,8 | n/d |
| -10,00% | 69,28 $ | 20/40 | +50,00% | +5,00% | 80,83 $ | 2/20 | +10,00% | +16,67% | DEBOLE | 11,4 | 14,0 |
| -10,00% | 69,28 $ | 20/40 | +50,00% | +10,00% | 84,68 $ | 2/20 | +10,00% | +22,22% | DEBOLE | 11,4 | 15,0 |
| -10,00% | 69,28 $ | 20/40 | +50,00% | +15,00% | 88,53 $ | 1/20 | +5,00% | +27,78% | DEBOLE | 11,4 | 15,0 |
| -10,00% | 69,28 $ | 20/40 | +50,00% | +20,00% | 92,38 $ | 0/20 | 0,00% | +33,33% | DEBOLE | 11,4 | n/d |
| -15,00% | 65,43 $ | 15/40 | +37,50% | +5,00% | 80,83 $ | 2/15 | +13,33% | +23,53% | DEBOLE | 13,3 | 14,0 |
| -15,00% | 65,43 $ | 15/40 | +37,50% | +10,00% | 84,68 $ | 2/15 | +13,33% | +29,41% | DEBOLE | 13,3 | 15,0 |
| -15,00% | 65,43 $ | 15/40 | +37,50% | +15,00% | 88,53 $ | 1/15 | +6,67% | +35,29% | DEBOLE | 13,3 | 15,0 |
| -15,00% | 65,43 $ | 15/40 | +37,50% | +20,00% | 92,38 $ | 0/15 | 0,00% | +41,18% | DEBOLE | 13,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 80,83 $ | 26/40 | +65,00% | prezzo iniziale | 76,98 $ | 16/26 | +61,54% | -4,76% | MEDIA | 3,7 | 12,2 |
| +5,00% | 80,83 $ | 26/40 | +65,00% | -5,00% | 73,13 $ | 10/26 | +38,46% | -9,52% | BASSA | 3,7 | 13,3 |
| +5,00% | 80,83 $ | 26/40 | +65,00% | -8,00% | 70,82 $ | 10/26 | +38,46% | -12,38% | BASSA | 3,7 | 16,9 |
| +5,00% | 80,83 $ | 26/40 | +65,00% | -10,00% | 69,28 $ | 7/26 | +26,92% | -14,29% | DEBOLE | 3,7 | 15,9 |
| +5,00% | 80,83 $ | 26/40 | +65,00% | -15,00% | 65,43 $ | 4/26 | +15,38% | -19,05% | DEBOLE | 3,7 | 17,5 |
| +10,00% | 84,68 $ | 18/40 | +45,00% | prezzo iniziale | 76,98 $ | 6/18 | +33,33% | -9,09% | DEBOLE | 7,3 | 16,2 |
| +10,00% | 84,68 $ | 18/40 | +45,00% | -5,00% | 73,13 $ | 3/18 | +16,67% | -13,64% | DEBOLE | 7,3 | 17,0 |
| +10,00% | 84,68 $ | 18/40 | +45,00% | -8,00% | 70,82 $ | 3/18 | +16,67% | -16,36% | DEBOLE | 7,3 | 17,0 |
| +10,00% | 84,68 $ | 18/40 | +45,00% | -10,00% | 69,28 $ | 1/18 | +5,56% | -18,18% | DEBOLE | 7,3 | 14,0 |
| +10,00% | 84,68 $ | 18/40 | +45,00% | -15,00% | 65,43 $ | 1/18 | +5,56% | -22,73% | DEBOLE | 7,3 | 14,0 |
| +15,00% | 88,53 $ | 15/40 | +37,50% | prezzo iniziale | 76,98 $ | 4/15 | +26,67% | -13,04% | DEBOLE | 11,1 | 15,5 |
| +15,00% | 88,53 $ | 15/40 | +37,50% | -5,00% | 73,13 $ | 2/15 | +13,33% | -17,39% | DEBOLE | 11,1 | 18,5 |
| +15,00% | 88,53 $ | 15/40 | +37,50% | -8,00% | 70,82 $ | 2/15 | +13,33% | -20,00% | DEBOLE | 11,1 | 18,5 |
| +15,00% | 88,53 $ | 15/40 | +37,50% | -10,00% | 69,28 $ | 0/15 | 0,00% | -21,74% | DEBOLE | 11,1 | n/d |
| +15,00% | 88,53 $ | 15/40 | +37,50% | -15,00% | 65,43 $ | 0/15 | 0,00% | -26,09% | DEBOLE | 11,1 | n/d |
| +20,00% | 92,38 $ | 11/40 | +27,50% | prezzo iniziale | 76,98 $ | 0/11 | 0,00% | -16,67% | DEBOLE | 14,0 | n/d |
| +20,00% | 92,38 $ | 11/40 | +27,50% | -5,00% | 73,13 $ | 0/11 | 0,00% | -20,83% | DEBOLE | 14,0 | n/d |
| +20,00% | 92,38 $ | 11/40 | +27,50% | -8,00% | 70,82 $ | 0/11 | 0,00% | -23,33% | DEBOLE | 14,0 | n/d |
| +20,00% | 92,38 $ | 11/40 | +27,50% | -10,00% | 69,28 $ | 0/11 | 0,00% | -25,00% | DEBOLE | 14,0 | n/d |
| +20,00% | 92,38 $ | 11/40 | +27,50% | -15,00% | 65,43 $ | 0/11 | 0,00% | -29,17% | DEBOLE | 14,0 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +16,67% (6/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 12 prima sono saliti a +10,00%. Tra quei 12, 6 poi sono scaricati a -5,00%. Percentuale: +50,00% (6/12). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06773 $ | 36/40 | +90,00% | +5,00% | 0,07485 $ | 9/36 | +25,00% | +10,53% | DEBOLE | 5,2 | 15,2 |
| -5,00% | 0,06773 $ | 36/40 | +90,00% | +10,00% | 0,07842 $ | 6/36 | +16,67% | +15,79% | DEBOLE | 5,2 | 13,7 |
| -5,00% | 0,06773 $ | 36/40 | +90,00% | +15,00% | 0,08198 $ | 6/36 | +16,67% | +21,05% | DEBOLE | 5,2 | 16,0 |
| -5,00% | 0,06773 $ | 36/40 | +90,00% | +20,00% | 0,08555 $ | 6/36 | +16,67% | +26,32% | DEBOLE | 5,2 | 16,8 |
| -8,00% | 0,06559 $ | 34/40 | +85,00% | +5,00% | 0,07485 $ | 7/34 | +20,59% | +14,13% | DEBOLE | 7,6 | 17,4 |
| -8,00% | 0,06559 $ | 34/40 | +85,00% | +10,00% | 0,07842 $ | 4/34 | +11,76% | +19,57% | DEBOLE | 7,6 | 16,2 |
| -8,00% | 0,06559 $ | 34/40 | +85,00% | +15,00% | 0,08198 $ | 4/34 | +11,76% | +25,00% | DEBOLE | 7,6 | 19,2 |
| -8,00% | 0,06559 $ | 34/40 | +85,00% | +20,00% | 0,08555 $ | 4/34 | +11,76% | +30,43% | DEBOLE | 7,6 | 20,0 |
| -10,00% | 0,06416 $ | 31/40 | +77,50% | +5,00% | 0,07485 $ | 5/31 | +16,13% | +16,67% | DEBOLE | 7,9 | 17,6 |
| -10,00% | 0,06416 $ | 31/40 | +77,50% | +10,00% | 0,07842 $ | 2/31 | +6,45% | +22,22% | DEBOLE | 7,9 | 15,0 |
| -10,00% | 0,06416 $ | 31/40 | +77,50% | +15,00% | 0,08198 $ | 2/31 | +6,45% | +27,78% | DEBOLE | 7,9 | 15,5 |
| -10,00% | 0,06416 $ | 31/40 | +77,50% | +20,00% | 0,08555 $ | 2/31 | +6,45% | +33,33% | DEBOLE | 7,9 | 15,5 |
| -15,00% | 0,06060 $ | 29/40 | +72,50% | +5,00% | 0,07485 $ | 4/29 | +13,79% | +23,53% | DEBOLE | 10,2 | 15,8 |
| -15,00% | 0,06060 $ | 29/40 | +72,50% | +10,00% | 0,07842 $ | 2/29 | +6,90% | +29,41% | DEBOLE | 10,2 | 15,0 |
| -15,00% | 0,06060 $ | 29/40 | +72,50% | +15,00% | 0,08198 $ | 2/29 | +6,90% | +35,29% | DEBOLE | 10,2 | 15,5 |
| -15,00% | 0,06060 $ | 29/40 | +72,50% | +20,00% | 0,08555 $ | 2/29 | +6,90% | +41,18% | DEBOLE | 10,2 | 15,5 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07485 $ | 18/40 | +45,00% | prezzo iniziale | 0,07129 $ | 14/18 | +77,78% | -4,76% | ALTA | 9,0 | 12,9 |
| +5,00% | 0,07485 $ | 18/40 | +45,00% | -5,00% | 0,06773 $ | 12/18 | +66,67% | -9,52% | ALTA | 9,0 | 15,7 |
| +5,00% | 0,07485 $ | 18/40 | +45,00% | -8,00% | 0,06559 $ | 10/18 | +55,56% | -12,38% | MEDIA | 9,0 | 15,3 |
| +5,00% | 0,07485 $ | 18/40 | +45,00% | -10,00% | 0,06416 $ | 8/18 | +44,44% | -14,29% | BASSA | 9,0 | 15,6 |
| +5,00% | 0,07485 $ | 18/40 | +45,00% | -15,00% | 0,06060 $ | 7/18 | +38,89% | -19,05% | BASSA | 9,0 | 15,1 |
| +10,00% | 0,07842 $ | 12/40 | +30,00% | prezzo iniziale | 0,07129 $ | 6/12 | +50,00% | -9,09% | MEDIA | 10,9 | 12,7 |
| +10,00% | 0,07842 $ | 12/40 | +30,00% | -5,00% | 0,06773 $ | 6/12 | +50,00% | -13,64% | MEDIA | 10,9 | 13,7 |
| +10,00% | 0,07842 $ | 12/40 | +30,00% | -8,00% | 0,06559 $ | 5/12 | +41,67% | -16,36% | BASSA | 10,9 | 14,0 |
| +10,00% | 0,07842 $ | 12/40 | +30,00% | -10,00% | 0,06416 $ | 4/12 | +33,33% | -18,18% | DEBOLE | 10,9 | 15,5 |
| +10,00% | 0,07842 $ | 12/40 | +30,00% | -15,00% | 0,06060 $ | 4/12 | +33,33% | -22,73% | DEBOLE | 10,9 | 17,2 |
| +15,00% | 0,08198 $ | 9/40 | +22,50% | prezzo iniziale | 0,07129 $ | 3/9 | +33,33% | -13,04% | DEBOLE | 13,0 | 13,0 |
| +15,00% | 0,08198 $ | 9/40 | +22,50% | -5,00% | 0,06773 $ | 3/9 | +33,33% | -17,39% | DEBOLE | 13,0 | 13,3 |
| +15,00% | 0,08198 $ | 9/40 | +22,50% | -8,00% | 0,06559 $ | 3/9 | +33,33% | -20,00% | DEBOLE | 13,0 | 13,7 |
| +15,00% | 0,08198 $ | 9/40 | +22,50% | -10,00% | 0,06416 $ | 2/9 | +22,22% | -21,74% | DEBOLE | 13,0 | 16,0 |
| +15,00% | 0,08198 $ | 9/40 | +22,50% | -15,00% | 0,06060 $ | 2/9 | +22,22% | -26,09% | DEBOLE | 13,0 | 18,0 |
| +20,00% | 0,08555 $ | 7/40 | +17,50% | prezzo iniziale | 0,07129 $ | 3/7 | +42,86% | -16,67% | BASSA | 17,0 | 19,0 |
| +20,00% | 0,08555 $ | 7/40 | +17,50% | -5,00% | 0,06773 $ | 2/7 | +28,57% | -20,83% | DEBOLE | 17,0 | 15,5 |
| +20,00% | 0,08555 $ | 7/40 | +17,50% | -8,00% | 0,06559 $ | 2/7 | +28,57% | -23,33% | DEBOLE | 17,0 | 16,0 |
| +20,00% | 0,08555 $ | 7/40 | +17,50% | -10,00% | 0,06416 $ | 2/7 | +28,57% | -25,00% | DEBOLE | 17,0 | 16,0 |
| +20,00% | 0,08555 $ | 7/40 | +17,50% | -15,00% | 0,06060 $ | 2/7 | +28,57% | -29,17% | DEBOLE | 17,0 | 18,0 |

---
