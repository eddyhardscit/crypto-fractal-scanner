# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-11 05:02:01 CEST**  
UTC: **2026-07-11 03:02:01 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.910 $ | 70.527 $ | +7,14% | +15,79% | rimbalzo poco frequente | 70.527 $ | 60.910 $ | +8,33% | -13,64% | spike storicamente più resistente |
| SOL | 73,83 $ | 85,49 $ | +10,71% | +15,79% | rimbalzo poco frequente | 85,49 $ | 73,83 $ | +27,78% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07047 $ | 0,08160 $ | +10,81% | +15,79% | rimbalzo poco frequente | 0,08160 $ | 0,07047 $ | +58,33% | -13,64% | attenzione a prendere profitto |

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
| -5,00% | 60.910 $ | 14/40 | +35,00% | +5,00% | 67.321 $ | 3/14 | +21,43% | +10,53% | DEBOLE | 9,6 | 23,0 |
| -5,00% | 60.910 $ | 14/40 | +35,00% | +10,00% | 70.527 $ | 1/14 | +7,14% | +15,79% | DEBOLE | 9,6 | 9,0 |
| -5,00% | 60.910 $ | 14/40 | +35,00% | +15,00% | 73.733 $ | 1/14 | +7,14% | +21,05% | DEBOLE | 9,6 | 9,0 |
| -5,00% | 60.910 $ | 14/40 | +35,00% | +20,00% | 76.938 $ | 1/14 | +7,14% | +26,32% | DEBOLE | 9,6 | 10,0 |
| -8,00% | 58.986 $ | 12/40 | +30,00% | +5,00% | 67.321 $ | 3/12 | +25,00% | +14,13% | DEBOLE | 12,7 | 23,0 |
| -8,00% | 58.986 $ | 12/40 | +30,00% | +10,00% | 70.527 $ | 1/12 | +8,33% | +19,57% | DEBOLE | 12,7 | 9,0 |
| -8,00% | 58.986 $ | 12/40 | +30,00% | +15,00% | 73.733 $ | 1/12 | +8,33% | +25,00% | DEBOLE | 12,7 | 9,0 |
| -8,00% | 58.986 $ | 12/40 | +30,00% | +20,00% | 76.938 $ | 1/12 | +8,33% | +30,43% | DEBOLE | 12,7 | 10,0 |
| -10,00% | 57.704 $ | 9/40 | +22,50% | +5,00% | 67.321 $ | 2/9 | +22,22% | +16,67% | DEBOLE | 14,6 | 30,0 |
| -10,00% | 57.704 $ | 9/40 | +22,50% | +10,00% | 70.527 $ | 0/9 | 0,00% | +22,22% | DEBOLE | 14,6 | n/d |
| -10,00% | 57.704 $ | 9/40 | +22,50% | +15,00% | 73.733 $ | 0/9 | 0,00% | +27,78% | DEBOLE | 14,6 | n/d |
| -10,00% | 57.704 $ | 9/40 | +22,50% | +20,00% | 76.938 $ | 0/9 | 0,00% | +33,33% | DEBOLE | 14,6 | n/d |
| -15,00% | 54.498 $ | 5/40 | +12,50% | +5,00% | 67.321 $ | 0/5 | 0,00% | +23,53% | DEBOLE | 11,8 | n/d |
| -15,00% | 54.498 $ | 5/40 | +12,50% | +10,00% | 70.527 $ | 0/5 | 0,00% | +29,41% | DEBOLE | 11,8 | n/d |
| -15,00% | 54.498 $ | 5/40 | +12,50% | +15,00% | 73.733 $ | 0/5 | 0,00% | +35,29% | DEBOLE | 11,8 | n/d |
| -15,00% | 54.498 $ | 5/40 | +12,50% | +20,00% | 76.938 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 11,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.321 $ | 34/40 | +85,00% | prezzo iniziale | 64.115 $ | 14/34 | +41,18% | -4,76% | BASSA | 5,1 | 12,4 |
| +5,00% | 67.321 $ | 34/40 | +85,00% | -5,00% | 60.910 $ | 6/34 | +17,65% | -9,52% | DEBOLE | 5,1 | 15,7 |
| +5,00% | 67.321 $ | 34/40 | +85,00% | -8,00% | 58.986 $ | 5/34 | +14,71% | -12,38% | DEBOLE | 5,1 | 17,6 |
| +5,00% | 67.321 $ | 34/40 | +85,00% | -10,00% | 57.704 $ | 3/34 | +8,82% | -14,29% | DEBOLE | 5,1 | 24,7 |
| +5,00% | 67.321 $ | 34/40 | +85,00% | -15,00% | 54.498 $ | 1/34 | +2,94% | -19,05% | DEBOLE | 5,1 | 24,0 |
| +10,00% | 70.527 $ | 24/40 | +60,00% | prezzo iniziale | 64.115 $ | 4/24 | +16,67% | -9,09% | DEBOLE | 5,7 | 16,8 |
| +10,00% | 70.527 $ | 24/40 | +60,00% | -5,00% | 60.910 $ | 2/24 | +8,33% | -13,64% | DEBOLE | 5,7 | 19,5 |
| +10,00% | 70.527 $ | 24/40 | +60,00% | -8,00% | 58.986 $ | 1/24 | +4,17% | -16,36% | DEBOLE | 5,7 | 23,0 |
| +10,00% | 70.527 $ | 24/40 | +60,00% | -10,00% | 57.704 $ | 1/24 | +4,17% | -18,18% | DEBOLE | 5,7 | 23,0 |
| +10,00% | 70.527 $ | 24/40 | +60,00% | -15,00% | 54.498 $ | 1/24 | +4,17% | -22,73% | DEBOLE | 5,7 | 24,0 |
| +15,00% | 73.733 $ | 21/40 | +52,50% | prezzo iniziale | 64.115 $ | 2/21 | +9,52% | -13,04% | DEBOLE | 9,8 | 17,0 |
| +15,00% | 73.733 $ | 21/40 | +52,50% | -5,00% | 60.910 $ | 0/21 | 0,00% | -17,39% | DEBOLE | 9,8 | n/d |
| +15,00% | 73.733 $ | 21/40 | +52,50% | -8,00% | 58.986 $ | 0/21 | 0,00% | -20,00% | DEBOLE | 9,8 | n/d |
| +15,00% | 73.733 $ | 21/40 | +52,50% | -10,00% | 57.704 $ | 0/21 | 0,00% | -21,74% | DEBOLE | 9,8 | n/d |
| +15,00% | 73.733 $ | 21/40 | +52,50% | -15,00% | 54.498 $ | 0/21 | 0,00% | -26,09% | DEBOLE | 9,8 | n/d |
| +20,00% | 76.938 $ | 19/40 | +47,50% | prezzo iniziale | 64.115 $ | 1/19 | +5,26% | -16,67% | DEBOLE | 11,6 | 22,0 |
| +20,00% | 76.938 $ | 19/40 | +47,50% | -5,00% | 60.910 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 11,6 | n/d |
| +20,00% | 76.938 $ | 19/40 | +47,50% | -8,00% | 58.986 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 11,6 | n/d |
| +20,00% | 76.938 $ | 19/40 | +47,50% | -10,00% | 57.704 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 11,6 | n/d |
| +20,00% | 76.938 $ | 19/40 | +47,50% | -15,00% | 54.498 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 11,6 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +10,71% (3/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 18 prima sono saliti a +10,00%. Tra quei 18, 5 poi sono scaricati a -5,00%. Percentuale: +27,78% (5/18). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,83 $ | 28/40 | +70,00% | +5,00% | 81,61 $ | 4/28 | +14,29% | +10,53% | DEBOLE | 6,9 | 14,5 |
| -5,00% | 73,83 $ | 28/40 | +70,00% | +10,00% | 85,49 $ | 3/28 | +10,71% | +15,79% | DEBOLE | 6,9 | 10,0 |
| -5,00% | 73,83 $ | 28/40 | +70,00% | +15,00% | 89,38 $ | 1/28 | +3,57% | +21,05% | DEBOLE | 6,9 | 8,0 |
| -5,00% | 73,83 $ | 28/40 | +70,00% | +20,00% | 93,26 $ | 1/28 | +3,57% | +26,32% | DEBOLE | 6,9 | 10,0 |
| -8,00% | 71,50 $ | 25/40 | +62,50% | +5,00% | 81,61 $ | 3/25 | +12,00% | +14,13% | DEBOLE | 9,8 | 21,0 |
| -8,00% | 71,50 $ | 25/40 | +62,50% | +10,00% | 85,49 $ | 2/25 | +8,00% | +19,57% | DEBOLE | 9,8 | 16,5 |
| -8,00% | 71,50 $ | 25/40 | +62,50% | +15,00% | 89,38 $ | 0/25 | 0,00% | +25,00% | DEBOLE | 9,8 | n/d |
| -8,00% | 71,50 $ | 25/40 | +62,50% | +20,00% | 93,26 $ | 0/25 | 0,00% | +30,43% | DEBOLE | 9,8 | n/d |
| -10,00% | 69,95 $ | 22/40 | +55,00% | +5,00% | 81,61 $ | 2/22 | +9,09% | +16,67% | DEBOLE | 10,4 | 16,5 |
| -10,00% | 69,95 $ | 22/40 | +55,00% | +10,00% | 85,49 $ | 2/22 | +9,09% | +22,22% | DEBOLE | 10,4 | 16,5 |
| -10,00% | 69,95 $ | 22/40 | +55,00% | +15,00% | 89,38 $ | 0/22 | 0,00% | +27,78% | DEBOLE | 10,4 | n/d |
| -10,00% | 69,95 $ | 22/40 | +55,00% | +20,00% | 93,26 $ | 0/22 | 0,00% | +33,33% | DEBOLE | 10,4 | n/d |
| -15,00% | 66,06 $ | 17/40 | +42,50% | +5,00% | 81,61 $ | 1/17 | +5,88% | +23,53% | DEBOLE | 12,8 | 15,0 |
| -15,00% | 66,06 $ | 17/40 | +42,50% | +10,00% | 85,49 $ | 1/17 | +5,88% | +29,41% | DEBOLE | 12,8 | 15,0 |
| -15,00% | 66,06 $ | 17/40 | +42,50% | +15,00% | 89,38 $ | 0/17 | 0,00% | +35,29% | DEBOLE | 12,8 | n/d |
| -15,00% | 66,06 $ | 17/40 | +42,50% | +20,00% | 93,26 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 12,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 81,61 $ | 23/40 | +57,50% | prezzo iniziale | 77,72 $ | 11/23 | +47,83% | -4,76% | BASSA | 2,9 | 9,8 |
| +5,00% | 81,61 $ | 23/40 | +57,50% | -5,00% | 73,83 $ | 10/23 | +43,48% | -9,52% | BASSA | 2,9 | 12,9 |
| +5,00% | 81,61 $ | 23/40 | +57,50% | -8,00% | 71,50 $ | 8/23 | +34,78% | -12,38% | DEBOLE | 2,9 | 15,0 |
| +5,00% | 81,61 $ | 23/40 | +57,50% | -10,00% | 69,95 $ | 6/23 | +26,09% | -14,29% | DEBOLE | 2,9 | 15,3 |
| +5,00% | 81,61 $ | 23/40 | +57,50% | -15,00% | 66,06 $ | 3/23 | +13,04% | -19,05% | DEBOLE | 2,9 | 15,3 |
| +10,00% | 85,49 $ | 18/40 | +45,00% | prezzo iniziale | 77,72 $ | 6/18 | +33,33% | -9,09% | DEBOLE | 6,5 | 12,7 |
| +10,00% | 85,49 $ | 18/40 | +45,00% | -5,00% | 73,83 $ | 5/18 | +27,78% | -13,64% | DEBOLE | 6,5 | 15,2 |
| +10,00% | 85,49 $ | 18/40 | +45,00% | -8,00% | 71,50 $ | 4/18 | +22,22% | -16,36% | DEBOLE | 6,5 | 15,2 |
| +10,00% | 85,49 $ | 18/40 | +45,00% | -10,00% | 69,95 $ | 3/18 | +16,67% | -18,18% | DEBOLE | 6,5 | 15,0 |
| +10,00% | 85,49 $ | 18/40 | +45,00% | -15,00% | 66,06 $ | 2/18 | +11,11% | -22,73% | DEBOLE | 6,5 | 16,0 |
| +15,00% | 89,38 $ | 14/40 | +35,00% | prezzo iniziale | 77,72 $ | 2/14 | +14,29% | -13,04% | DEBOLE | 10,3 | 14,0 |
| +15,00% | 89,38 $ | 14/40 | +35,00% | -5,00% | 73,83 $ | 1/14 | +7,14% | -17,39% | DEBOLE | 10,3 | 17,0 |
| +15,00% | 89,38 $ | 14/40 | +35,00% | -8,00% | 71,50 $ | 1/14 | +7,14% | -20,00% | DEBOLE | 10,3 | 17,0 |
| +15,00% | 89,38 $ | 14/40 | +35,00% | -10,00% | 69,95 $ | 0/14 | 0,00% | -21,74% | DEBOLE | 10,3 | n/d |
| +15,00% | 89,38 $ | 14/40 | +35,00% | -15,00% | 66,06 $ | 0/14 | 0,00% | -26,09% | DEBOLE | 10,3 | n/d |
| +20,00% | 93,26 $ | 12/40 | +30,00% | prezzo iniziale | 77,72 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,26 $ | 12/40 | +30,00% | -5,00% | 73,83 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,26 $ | 12/40 | +30,00% | -8,00% | 71,50 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,26 $ | 12/40 | +30,00% | -10,00% | 69,95 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 12,8 | n/d |
| +20,00% | 93,26 $ | 12/40 | +30,00% | -15,00% | 66,06 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 12,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 37 prima sono scesi a -5,00%. Tra quei 37, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +10,81% (4/37). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 12 prima sono saliti a +10,00%. Tra quei 12, 7 poi sono scaricati a -5,00%. Percentuale: +58,33% (7/12). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07047 $ | 37/40 | +92,50% | +5,00% | 0,07789 $ | 6/37 | +16,22% | +10,53% | DEBOLE | 6,6 | 13,3 |
| -5,00% | 0,07047 $ | 37/40 | +92,50% | +10,00% | 0,08160 $ | 4/37 | +10,81% | +15,79% | DEBOLE | 6,6 | 8,0 |
| -5,00% | 0,07047 $ | 37/40 | +92,50% | +15,00% | 0,08531 $ | 4/37 | +10,81% | +21,05% | DEBOLE | 6,6 | 12,0 |
| -5,00% | 0,07047 $ | 37/40 | +92,50% | +20,00% | 0,08902 $ | 4/37 | +10,81% | +26,32% | DEBOLE | 6,6 | 13,5 |
| -8,00% | 0,06825 $ | 35/40 | +87,50% | +5,00% | 0,07789 $ | 4/35 | +11,43% | +14,13% | DEBOLE | 8,5 | 16,2 |
| -8,00% | 0,06825 $ | 35/40 | +87,50% | +10,00% | 0,08160 $ | 2/35 | +5,71% | +19,57% | DEBOLE | 8,5 | 7,5 |
| -8,00% | 0,06825 $ | 35/40 | +87,50% | +15,00% | 0,08531 $ | 2/35 | +5,71% | +25,00% | DEBOLE | 8,5 | 14,5 |
| -8,00% | 0,06825 $ | 35/40 | +87,50% | +20,00% | 0,08902 $ | 2/35 | +5,71% | +30,43% | DEBOLE | 8,5 | 16,5 |
| -10,00% | 0,06676 $ | 32/40 | +80,00% | +5,00% | 0,07789 $ | 2/32 | +6,25% | +16,67% | DEBOLE | 9,3 | 25,0 |
| -10,00% | 0,06676 $ | 32/40 | +80,00% | +10,00% | 0,08160 $ | 0/32 | 0,00% | +22,22% | DEBOLE | 9,3 | n/d |
| -10,00% | 0,06676 $ | 32/40 | +80,00% | +15,00% | 0,08531 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 9,3 | n/d |
| -10,00% | 0,06676 $ | 32/40 | +80,00% | +20,00% | 0,08902 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 9,3 | n/d |
| -15,00% | 0,06305 $ | 29/40 | +72,50% | +5,00% | 0,07789 $ | 1/29 | +3,45% | +23,53% | DEBOLE | 10,9 | 25,0 |
| -15,00% | 0,06305 $ | 29/40 | +72,50% | +10,00% | 0,08160 $ | 0/29 | 0,00% | +29,41% | DEBOLE | 10,9 | n/d |
| -15,00% | 0,06305 $ | 29/40 | +72,50% | +15,00% | 0,08531 $ | 0/29 | 0,00% | +35,29% | DEBOLE | 10,9 | n/d |
| -15,00% | 0,06305 $ | 29/40 | +72,50% | +20,00% | 0,08902 $ | 0/29 | 0,00% | +41,18% | DEBOLE | 10,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07789 $ | 19/40 | +47,50% | prezzo iniziale | 0,07418 $ | 16/19 | +84,21% | -4,76% | ALTA | 5,9 | 10,0 |
| +5,00% | 0,07789 $ | 19/40 | +47,50% | -5,00% | 0,07047 $ | 14/19 | +73,68% | -9,52% | ALTA | 5,9 | 15,1 |
| +5,00% | 0,07789 $ | 19/40 | +47,50% | -8,00% | 0,06825 $ | 12/19 | +63,16% | -12,38% | MEDIA | 5,9 | 14,8 |
| +5,00% | 0,07789 $ | 19/40 | +47,50% | -10,00% | 0,06676 $ | 10/19 | +52,63% | -14,29% | MEDIA | 5,9 | 15,2 |
| +5,00% | 0,07789 $ | 19/40 | +47,50% | -15,00% | 0,06305 $ | 8/19 | +42,11% | -19,05% | BASSA | 5,9 | 12,9 |
| +10,00% | 0,08160 $ | 12/40 | +30,00% | prezzo iniziale | 0,07418 $ | 8/12 | +66,67% | -9,09% | ALTA | 7,2 | 10,2 |
| +10,00% | 0,08160 $ | 12/40 | +30,00% | -5,00% | 0,07047 $ | 7/12 | +58,33% | -13,64% | MEDIA | 7,2 | 14,0 |
| +10,00% | 0,08160 $ | 12/40 | +30,00% | -8,00% | 0,06825 $ | 6/12 | +50,00% | -16,36% | MEDIA | 7,2 | 14,5 |
| +10,00% | 0,08160 $ | 12/40 | +30,00% | -10,00% | 0,06676 $ | 5/12 | +41,67% | -18,18% | BASSA | 7,2 | 16,0 |
| +10,00% | 0,08160 $ | 12/40 | +30,00% | -15,00% | 0,06305 $ | 4/12 | +33,33% | -22,73% | DEBOLE | 7,2 | 14,5 |
| +15,00% | 0,08531 $ | 8/40 | +20,00% | prezzo iniziale | 0,07418 $ | 3/8 | +37,50% | -13,04% | BASSA | 9,1 | 10,7 |
| +15,00% | 0,08531 $ | 8/40 | +20,00% | -5,00% | 0,07047 $ | 3/8 | +37,50% | -17,39% | BASSA | 9,1 | 10,7 |
| +15,00% | 0,08531 $ | 8/40 | +20,00% | -8,00% | 0,06825 $ | 3/8 | +37,50% | -20,00% | BASSA | 9,1 | 11,0 |
| +15,00% | 0,08531 $ | 8/40 | +20,00% | -10,00% | 0,06676 $ | 2/8 | +25,00% | -21,74% | DEBOLE | 9,1 | 12,5 |
| +15,00% | 0,08531 $ | 8/40 | +20,00% | -15,00% | 0,06305 $ | 2/8 | +25,00% | -26,09% | DEBOLE | 9,1 | 13,0 |
| +20,00% | 0,08902 $ | 6/40 | +15,00% | prezzo iniziale | 0,07418 $ | 3/6 | +50,00% | -16,67% | MEDIA | 11,5 | 16,7 |
| +20,00% | 0,08902 $ | 6/40 | +15,00% | -5,00% | 0,07047 $ | 2/6 | +33,33% | -20,83% | DEBOLE | 11,5 | 11,5 |
| +20,00% | 0,08902 $ | 6/40 | +15,00% | -8,00% | 0,06825 $ | 2/6 | +33,33% | -23,33% | DEBOLE | 11,5 | 12,0 |
| +20,00% | 0,08902 $ | 6/40 | +15,00% | -10,00% | 0,06676 $ | 2/6 | +33,33% | -25,00% | DEBOLE | 11,5 | 12,5 |
| +20,00% | 0,08902 $ | 6/40 | +15,00% | -15,00% | 0,06305 $ | 2/6 | +33,33% | -29,17% | DEBOLE | 11,5 | 13,0 |

---
