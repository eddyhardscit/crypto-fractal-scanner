# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-10 20:23:21 CEST**  
UTC: **2026-07-10 18:23:21 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.660 $ | 70.238 $ | +7,14% | +15,79% | rimbalzo poco frequente | 70.238 $ | 60.660 $ | +8,33% | -13,64% | spike storicamente più resistente |
| SOL | 73,74 $ | 85,38 $ | +11,11% | +15,79% | rimbalzo poco frequente | 85,38 $ | 73,74 $ | +26,32% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07024 $ | 0,08133 $ | +10,81% | +15,79% | rimbalzo poco frequente | 0,08133 $ | 0,07024 $ | +61,54% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 1 poi sono rimbalzati fino a +10,00%. Percentuale: +7,14% (1/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 2 poi sono scaricati a -5,00%. Percentuale: +8,33% (2/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.660 $ | 14/40 | +35,00% | +5,00% | 67.045 $ | 2/14 | +14,29% | +10,53% | DEBOLE | 10,6 | 19,5 |
| -5,00% | 60.660 $ | 14/40 | +35,00% | +10,00% | 70.238 $ | 1/14 | +7,14% | +15,79% | DEBOLE | 10,6 | 9,0 |
| -5,00% | 60.660 $ | 14/40 | +35,00% | +15,00% | 73.430 $ | 1/14 | +7,14% | +21,05% | DEBOLE | 10,6 | 9,0 |
| -5,00% | 60.660 $ | 14/40 | +35,00% | +20,00% | 76.623 $ | 1/14 | +7,14% | +26,32% | DEBOLE | 10,6 | 10,0 |
| -8,00% | 58.744 $ | 12/40 | +30,00% | +5,00% | 67.045 $ | 2/12 | +16,67% | +14,13% | DEBOLE | 12,9 | 19,5 |
| -8,00% | 58.744 $ | 12/40 | +30,00% | +10,00% | 70.238 $ | 1/12 | +8,33% | +19,57% | DEBOLE | 12,9 | 9,0 |
| -8,00% | 58.744 $ | 12/40 | +30,00% | +15,00% | 73.430 $ | 1/12 | +8,33% | +25,00% | DEBOLE | 12,9 | 9,0 |
| -8,00% | 58.744 $ | 12/40 | +30,00% | +20,00% | 76.623 $ | 1/12 | +8,33% | +30,43% | DEBOLE | 12,9 | 10,0 |
| -10,00% | 57.467 $ | 9/40 | +22,50% | +5,00% | 67.045 $ | 1/9 | +11,11% | +16,67% | DEBOLE | 15,0 | 30,0 |
| -10,00% | 57.467 $ | 9/40 | +22,50% | +10,00% | 70.238 $ | 0/9 | 0,00% | +22,22% | DEBOLE | 15,0 | n/d |
| -10,00% | 57.467 $ | 9/40 | +22,50% | +15,00% | 73.430 $ | 0/9 | 0,00% | +27,78% | DEBOLE | 15,0 | n/d |
| -10,00% | 57.467 $ | 9/40 | +22,50% | +20,00% | 76.623 $ | 0/9 | 0,00% | +33,33% | DEBOLE | 15,0 | n/d |
| -15,00% | 54.275 $ | 6/40 | +15,00% | +5,00% | 67.045 $ | 0/6 | 0,00% | +23,53% | DEBOLE | 14,7 | n/d |
| -15,00% | 54.275 $ | 6/40 | +15,00% | +10,00% | 70.238 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 14,7 | n/d |
| -15,00% | 54.275 $ | 6/40 | +15,00% | +15,00% | 73.430 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 14,7 | n/d |
| -15,00% | 54.275 $ | 6/40 | +15,00% | +20,00% | 76.623 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 14,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.045 $ | 34/40 | +85,00% | prezzo iniziale | 63.852 $ | 15/34 | +44,12% | -4,76% | BASSA | 4,3 | 12,9 |
| +5,00% | 67.045 $ | 34/40 | +85,00% | -5,00% | 60.660 $ | 7/34 | +20,59% | -9,52% | DEBOLE | 4,3 | 16,1 |
| +5,00% | 67.045 $ | 34/40 | +85,00% | -8,00% | 58.744 $ | 6/34 | +17,65% | -12,38% | DEBOLE | 4,3 | 18,0 |
| +5,00% | 67.045 $ | 34/40 | +85,00% | -10,00% | 57.467 $ | 4/34 | +11,76% | -14,29% | DEBOLE | 4,3 | 24,2 |
| +5,00% | 67.045 $ | 34/40 | +85,00% | -15,00% | 54.275 $ | 2/34 | +5,88% | -19,05% | DEBOLE | 4,3 | 26,5 |
| +10,00% | 70.238 $ | 24/40 | +60,00% | prezzo iniziale | 63.852 $ | 4/24 | +16,67% | -9,09% | DEBOLE | 5,8 | 16,8 |
| +10,00% | 70.238 $ | 24/40 | +60,00% | -5,00% | 60.660 $ | 2/24 | +8,33% | -13,64% | DEBOLE | 5,8 | 19,5 |
| +10,00% | 70.238 $ | 24/40 | +60,00% | -8,00% | 58.744 $ | 1/24 | +4,17% | -16,36% | DEBOLE | 5,8 | 23,0 |
| +10,00% | 70.238 $ | 24/40 | +60,00% | -10,00% | 57.467 $ | 1/24 | +4,17% | -18,18% | DEBOLE | 5,8 | 23,0 |
| +10,00% | 70.238 $ | 24/40 | +60,00% | -15,00% | 54.275 $ | 1/24 | +4,17% | -22,73% | DEBOLE | 5,8 | 24,0 |
| +15,00% | 73.430 $ | 21/40 | +52,50% | prezzo iniziale | 63.852 $ | 2/21 | +9,52% | -13,04% | DEBOLE | 9,8 | 17,0 |
| +15,00% | 73.430 $ | 21/40 | +52,50% | -5,00% | 60.660 $ | 0/21 | 0,00% | -17,39% | DEBOLE | 9,8 | n/d |
| +15,00% | 73.430 $ | 21/40 | +52,50% | -8,00% | 58.744 $ | 0/21 | 0,00% | -20,00% | DEBOLE | 9,8 | n/d |
| +15,00% | 73.430 $ | 21/40 | +52,50% | -10,00% | 57.467 $ | 0/21 | 0,00% | -21,74% | DEBOLE | 9,8 | n/d |
| +15,00% | 73.430 $ | 21/40 | +52,50% | -15,00% | 54.275 $ | 0/21 | 0,00% | -26,09% | DEBOLE | 9,8 | n/d |
| +20,00% | 76.623 $ | 19/40 | +47,50% | prezzo iniziale | 63.852 $ | 1/19 | +5,26% | -16,67% | DEBOLE | 11,6 | 22,0 |
| +20,00% | 76.623 $ | 19/40 | +47,50% | -5,00% | 60.660 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 11,6 | n/d |
| +20,00% | 76.623 $ | 19/40 | +47,50% | -8,00% | 58.744 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 11,6 | n/d |
| +20,00% | 76.623 $ | 19/40 | +47,50% | -10,00% | 57.467 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 11,6 | n/d |
| +20,00% | 76.623 $ | 19/40 | +47,50% | -15,00% | 54.275 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 11,6 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +11,11% (3/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 5 poi sono scaricati a -5,00%. Percentuale: +26,32% (5/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,74 $ | 27/40 | +67,50% | +5,00% | 81,50 $ | 4/27 | +14,81% | +10,53% | DEBOLE | 6,7 | 14,5 |
| -5,00% | 73,74 $ | 27/40 | +67,50% | +10,00% | 85,38 $ | 3/27 | +11,11% | +15,79% | DEBOLE | 6,7 | 10,0 |
| -5,00% | 73,74 $ | 27/40 | +67,50% | +15,00% | 89,26 $ | 1/27 | +3,70% | +21,05% | DEBOLE | 6,7 | 8,0 |
| -5,00% | 73,74 $ | 27/40 | +67,50% | +20,00% | 93,14 $ | 1/27 | +3,70% | +26,32% | DEBOLE | 6,7 | 10,0 |
| -8,00% | 71,41 $ | 25/40 | +62,50% | +5,00% | 81,50 $ | 3/25 | +12,00% | +14,13% | DEBOLE | 9,8 | 21,0 |
| -8,00% | 71,41 $ | 25/40 | +62,50% | +10,00% | 85,38 $ | 2/25 | +8,00% | +19,57% | DEBOLE | 9,8 | 16,5 |
| -8,00% | 71,41 $ | 25/40 | +62,50% | +15,00% | 89,26 $ | 0/25 | 0,00% | +25,00% | DEBOLE | 9,8 | n/d |
| -8,00% | 71,41 $ | 25/40 | +62,50% | +20,00% | 93,14 $ | 0/25 | 0,00% | +30,43% | DEBOLE | 9,8 | n/d |
| -10,00% | 69,86 $ | 22/40 | +55,00% | +5,00% | 81,50 $ | 2/22 | +9,09% | +16,67% | DEBOLE | 10,4 | 16,5 |
| -10,00% | 69,86 $ | 22/40 | +55,00% | +10,00% | 85,38 $ | 2/22 | +9,09% | +22,22% | DEBOLE | 10,4 | 16,5 |
| -10,00% | 69,86 $ | 22/40 | +55,00% | +15,00% | 89,26 $ | 0/22 | 0,00% | +27,78% | DEBOLE | 10,4 | n/d |
| -10,00% | 69,86 $ | 22/40 | +55,00% | +20,00% | 93,14 $ | 0/22 | 0,00% | +33,33% | DEBOLE | 10,4 | n/d |
| -15,00% | 65,98 $ | 17/40 | +42,50% | +5,00% | 81,50 $ | 1/17 | +5,88% | +23,53% | DEBOLE | 12,8 | 15,0 |
| -15,00% | 65,98 $ | 17/40 | +42,50% | +10,00% | 85,38 $ | 1/17 | +5,88% | +29,41% | DEBOLE | 12,8 | 15,0 |
| -15,00% | 65,98 $ | 17/40 | +42,50% | +15,00% | 89,26 $ | 0/17 | 0,00% | +35,29% | DEBOLE | 12,8 | n/d |
| -15,00% | 65,98 $ | 17/40 | +42,50% | +20,00% | 93,14 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 12,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 81,50 $ | 23/40 | +57,50% | prezzo iniziale | 77,62 $ | 10/23 | +43,48% | -4,76% | BASSA | 2,8 | 10,3 |
| +5,00% | 81,50 $ | 23/40 | +57,50% | -5,00% | 73,74 $ | 9/23 | +39,13% | -9,52% | BASSA | 2,8 | 12,9 |
| +5,00% | 81,50 $ | 23/40 | +57,50% | -8,00% | 71,41 $ | 8/23 | +34,78% | -12,38% | DEBOLE | 2,8 | 15,0 |
| +5,00% | 81,50 $ | 23/40 | +57,50% | -10,00% | 69,86 $ | 6/23 | +26,09% | -14,29% | DEBOLE | 2,8 | 15,3 |
| +5,00% | 81,50 $ | 23/40 | +57,50% | -15,00% | 65,98 $ | 3/23 | +13,04% | -19,05% | DEBOLE | 2,8 | 15,3 |
| +10,00% | 85,38 $ | 19/40 | +47,50% | prezzo iniziale | 77,62 $ | 6/19 | +31,58% | -9,09% | DEBOLE | 6,3 | 12,7 |
| +10,00% | 85,38 $ | 19/40 | +47,50% | -5,00% | 73,74 $ | 5/19 | +26,32% | -13,64% | DEBOLE | 6,3 | 15,2 |
| +10,00% | 85,38 $ | 19/40 | +47,50% | -8,00% | 71,41 $ | 4/19 | +21,05% | -16,36% | DEBOLE | 6,3 | 15,2 |
| +10,00% | 85,38 $ | 19/40 | +47,50% | -10,00% | 69,86 $ | 3/19 | +15,79% | -18,18% | DEBOLE | 6,3 | 15,0 |
| +10,00% | 85,38 $ | 19/40 | +47,50% | -15,00% | 65,98 $ | 2/19 | +10,53% | -22,73% | DEBOLE | 6,3 | 16,0 |
| +15,00% | 89,26 $ | 14/40 | +35,00% | prezzo iniziale | 77,62 $ | 2/14 | +14,29% | -13,04% | DEBOLE | 10,3 | 14,0 |
| +15,00% | 89,26 $ | 14/40 | +35,00% | -5,00% | 73,74 $ | 1/14 | +7,14% | -17,39% | DEBOLE | 10,3 | 17,0 |
| +15,00% | 89,26 $ | 14/40 | +35,00% | -8,00% | 71,41 $ | 1/14 | +7,14% | -20,00% | DEBOLE | 10,3 | 17,0 |
| +15,00% | 89,26 $ | 14/40 | +35,00% | -10,00% | 69,86 $ | 0/14 | 0,00% | -21,74% | DEBOLE | 10,3 | n/d |
| +15,00% | 89,26 $ | 14/40 | +35,00% | -15,00% | 65,98 $ | 0/14 | 0,00% | -26,09% | DEBOLE | 10,3 | n/d |
| +20,00% | 93,14 $ | 12/40 | +30,00% | prezzo iniziale | 77,62 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,14 $ | 12/40 | +30,00% | -5,00% | 73,74 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,14 $ | 12/40 | +30,00% | -8,00% | 71,41 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,14 $ | 12/40 | +30,00% | -10,00% | 69,86 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,14 $ | 12/40 | +30,00% | -15,00% | 65,98 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 12,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 37 prima sono scesi a -5,00%. Tra quei 37, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +10,81% (4/37). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 13 prima sono saliti a +10,00%. Tra quei 13, 8 poi sono scaricati a -5,00%. Percentuale: +61,54% (8/13). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07024 $ | 37/40 | +92,50% | +5,00% | 0,07764 $ | 6/37 | +16,22% | +10,53% | DEBOLE | 6,6 | 13,3 |
| -5,00% | 0,07024 $ | 37/40 | +92,50% | +10,00% | 0,08133 $ | 4/37 | +10,81% | +15,79% | DEBOLE | 6,6 | 8,0 |
| -5,00% | 0,07024 $ | 37/40 | +92,50% | +15,00% | 0,08503 $ | 4/37 | +10,81% | +21,05% | DEBOLE | 6,6 | 12,0 |
| -5,00% | 0,07024 $ | 37/40 | +92,50% | +20,00% | 0,08873 $ | 4/37 | +10,81% | +26,32% | DEBOLE | 6,6 | 13,5 |
| -8,00% | 0,06802 $ | 35/40 | +87,50% | +5,00% | 0,07764 $ | 4/35 | +11,43% | +14,13% | DEBOLE | 8,4 | 16,2 |
| -8,00% | 0,06802 $ | 35/40 | +87,50% | +10,00% | 0,08133 $ | 2/35 | +5,71% | +19,57% | DEBOLE | 8,4 | 7,5 |
| -8,00% | 0,06802 $ | 35/40 | +87,50% | +15,00% | 0,08503 $ | 2/35 | +5,71% | +25,00% | DEBOLE | 8,4 | 14,5 |
| -8,00% | 0,06802 $ | 35/40 | +87,50% | +20,00% | 0,08873 $ | 2/35 | +5,71% | +30,43% | DEBOLE | 8,4 | 16,5 |
| -10,00% | 0,06655 $ | 32/40 | +80,00% | +5,00% | 0,07764 $ | 2/32 | +6,25% | +16,67% | DEBOLE | 9,2 | 25,0 |
| -10,00% | 0,06655 $ | 32/40 | +80,00% | +10,00% | 0,08133 $ | 0/32 | 0,00% | +22,22% | DEBOLE | 9,2 | n/d |
| -10,00% | 0,06655 $ | 32/40 | +80,00% | +15,00% | 0,08503 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 9,2 | n/d |
| -10,00% | 0,06655 $ | 32/40 | +80,00% | +20,00% | 0,08873 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 9,2 | n/d |
| -15,00% | 0,06285 $ | 29/40 | +72,50% | +5,00% | 0,07764 $ | 1/29 | +3,45% | +23,53% | DEBOLE | 10,8 | 25,0 |
| -15,00% | 0,06285 $ | 29/40 | +72,50% | +10,00% | 0,08133 $ | 0/29 | 0,00% | +29,41% | DEBOLE | 10,8 | n/d |
| -15,00% | 0,06285 $ | 29/40 | +72,50% | +15,00% | 0,08503 $ | 0/29 | 0,00% | +35,29% | DEBOLE | 10,8 | n/d |
| -15,00% | 0,06285 $ | 29/40 | +72,50% | +20,00% | 0,08873 $ | 0/29 | 0,00% | +41,18% | DEBOLE | 10,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07764 $ | 18/40 | +45,00% | prezzo iniziale | 0,07394 $ | 15/18 | +83,33% | -4,76% | ALTA | 6,3 | 10,4 |
| +5,00% | 0,07764 $ | 18/40 | +45,00% | -5,00% | 0,07024 $ | 13/18 | +72,22% | -9,52% | ALTA | 6,3 | 15,4 |
| +5,00% | 0,07764 $ | 18/40 | +45,00% | -8,00% | 0,06802 $ | 11/18 | +61,11% | -12,38% | MEDIA | 6,3 | 15,0 |
| +5,00% | 0,07764 $ | 18/40 | +45,00% | -10,00% | 0,06655 $ | 9/18 | +50,00% | -14,29% | MEDIA | 6,3 | 15,4 |
| +5,00% | 0,07764 $ | 18/40 | +45,00% | -15,00% | 0,06285 $ | 7/18 | +38,89% | -19,05% | BASSA | 6,3 | 12,7 |
| +10,00% | 0,08133 $ | 13/40 | +32,50% | prezzo iniziale | 0,07394 $ | 9/13 | +69,23% | -9,09% | ALTA | 6,8 | 10,3 |
| +10,00% | 0,08133 $ | 13/40 | +32,50% | -5,00% | 0,07024 $ | 8/13 | +61,54% | -13,64% | MEDIA | 6,8 | 13,9 |
| +10,00% | 0,08133 $ | 13/40 | +32,50% | -8,00% | 0,06802 $ | 7/13 | +53,85% | -16,36% | MEDIA | 6,8 | 14,3 |
| +10,00% | 0,08133 $ | 13/40 | +32,50% | -10,00% | 0,06655 $ | 6/13 | +46,15% | -18,18% | BASSA | 6,8 | 15,7 |
| +10,00% | 0,08133 $ | 13/40 | +32,50% | -15,00% | 0,06285 $ | 5/13 | +38,46% | -22,73% | BASSA | 6,8 | 14,4 |
| +15,00% | 0,08503 $ | 8/40 | +20,00% | prezzo iniziale | 0,07394 $ | 3/8 | +37,50% | -13,04% | BASSA | 9,1 | 10,7 |
| +15,00% | 0,08503 $ | 8/40 | +20,00% | -5,00% | 0,07024 $ | 3/8 | +37,50% | -17,39% | BASSA | 9,1 | 10,7 |
| +15,00% | 0,08503 $ | 8/40 | +20,00% | -8,00% | 0,06802 $ | 3/8 | +37,50% | -20,00% | BASSA | 9,1 | 11,0 |
| +15,00% | 0,08503 $ | 8/40 | +20,00% | -10,00% | 0,06655 $ | 2/8 | +25,00% | -21,74% | DEBOLE | 9,1 | 12,5 |
| +15,00% | 0,08503 $ | 8/40 | +20,00% | -15,00% | 0,06285 $ | 2/8 | +25,00% | -26,09% | DEBOLE | 9,1 | 13,0 |
| +20,00% | 0,08873 $ | 6/40 | +15,00% | prezzo iniziale | 0,07394 $ | 3/6 | +50,00% | -16,67% | MEDIA | 11,5 | 16,7 |
| +20,00% | 0,08873 $ | 6/40 | +15,00% | -5,00% | 0,07024 $ | 2/6 | +33,33% | -20,83% | DEBOLE | 11,5 | 11,5 |
| +20,00% | 0,08873 $ | 6/40 | +15,00% | -8,00% | 0,06802 $ | 2/6 | +33,33% | -23,33% | DEBOLE | 11,5 | 12,0 |
| +20,00% | 0,08873 $ | 6/40 | +15,00% | -10,00% | 0,06655 $ | 2/6 | +33,33% | -25,00% | DEBOLE | 11,5 | 12,5 |
| +20,00% | 0,08873 $ | 6/40 | +15,00% | -15,00% | 0,06285 $ | 2/6 | +33,33% | -29,17% | DEBOLE | 11,5 | 13,0 |

---
