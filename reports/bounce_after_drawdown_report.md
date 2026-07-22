# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-22 07:13:52 CEST**  
UTC: **2026-07-22 05:13:52 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.909 $ | 72.842 $ | +48,57% | +15,79% | rimbalzo debole | 72.842 $ | 62.909 $ | +16,00% | -13,64% | spike storicamente più resistente |
| SOL | 73,95 $ | 85,62 $ | +20,00% | +15,79% | rimbalzo poco frequente | 85,62 $ | 73,95 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06951 $ | 0,08049 $ | +32,43% | +15,79% | rimbalzo poco frequente | 0,08049 $ | 0,06951 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 17 poi sono rimbalzati fino a +10,00%. Percentuale: +48,57% (17/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 4 poi sono scaricati a -5,00%. Percentuale: +16,00% (4/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 62.909 $ | 35/40 | +87,50% | +5,00% | 69.531 $ | 21/35 | +60,00% | +10,53% | MEDIA | 6,8 | 19,7 |
| -5,00% | 62.909 $ | 35/40 | +87,50% | +10,00% | 72.842 $ | 17/35 | +48,57% | +15,79% | BASSA | 6,8 | 22,0 |
| -5,00% | 62.909 $ | 35/40 | +87,50% | +15,00% | 76.153 $ | 15/35 | +42,86% | +21,05% | BASSA | 6,8 | 25,3 |
| -5,00% | 62.909 $ | 35/40 | +87,50% | +20,00% | 79.464 $ | 14/35 | +40,00% | +26,32% | BASSA | 6,8 | 27,0 |
| -8,00% | 60.923 $ | 28/40 | +70,00% | +5,00% | 69.531 $ | 15/28 | +53,57% | +14,13% | MEDIA | 9,0 | 20,9 |
| -8,00% | 60.923 $ | 28/40 | +70,00% | +10,00% | 72.842 $ | 12/28 | +42,86% | +19,57% | BASSA | 9,0 | 22,2 |
| -8,00% | 60.923 $ | 28/40 | +70,00% | +15,00% | 76.153 $ | 10/28 | +35,71% | +25,00% | BASSA | 9,0 | 24,4 |
| -8,00% | 60.923 $ | 28/40 | +70,00% | +20,00% | 79.464 $ | 10/28 | +35,71% | +30,43% | BASSA | 9,0 | 26,1 |
| -10,00% | 59.598 $ | 22/40 | +55,00% | +5,00% | 69.531 $ | 10/22 | +45,45% | +16,67% | BASSA | 11,4 | 21,5 |
| -10,00% | 59.598 $ | 22/40 | +55,00% | +10,00% | 72.842 $ | 8/22 | +36,36% | +22,22% | BASSA | 11,4 | 22,9 |
| -10,00% | 59.598 $ | 22/40 | +55,00% | +15,00% | 76.153 $ | 7/22 | +31,82% | +27,78% | DEBOLE | 11,4 | 25,0 |
| -10,00% | 59.598 $ | 22/40 | +55,00% | +20,00% | 79.464 $ | 7/22 | +31,82% | +33,33% | DEBOLE | 11,4 | 25,7 |
| -15,00% | 56.287 $ | 11/40 | +27,50% | +5,00% | 69.531 $ | 1/11 | +9,09% | +23,53% | DEBOLE | 15,0 | 21,0 |
| -15,00% | 56.287 $ | 11/40 | +27,50% | +10,00% | 72.842 $ | 0/11 | 0,00% | +29,41% | DEBOLE | 15,0 | n/d |
| -15,00% | 56.287 $ | 11/40 | +27,50% | +15,00% | 76.153 $ | 0/11 | 0,00% | +35,29% | DEBOLE | 15,0 | n/d |
| -15,00% | 56.287 $ | 11/40 | +27,50% | +20,00% | 79.464 $ | 0/11 | 0,00% | +41,18% | DEBOLE | 15,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 69.531 $ | 32/40 | +80,00% | prezzo iniziale | 66.220 $ | 11/32 | +34,38% | -4,76% | DEBOLE | 14,9 | 15,4 |
| +5,00% | 69.531 $ | 32/40 | +80,00% | -5,00% | 62.909 $ | 9/32 | +28,12% | -9,52% | DEBOLE | 14,9 | 14,7 |
| +5,00% | 69.531 $ | 32/40 | +80,00% | -8,00% | 60.923 $ | 7/32 | +21,88% | -12,38% | DEBOLE | 14,9 | 15,4 |
| +5,00% | 69.531 $ | 32/40 | +80,00% | -10,00% | 59.598 $ | 7/32 | +21,88% | -14,29% | DEBOLE | 14,9 | 16,3 |
| +5,00% | 69.531 $ | 32/40 | +80,00% | -15,00% | 56.287 $ | 5/32 | +15,62% | -19,05% | DEBOLE | 14,9 | 19,8 |
| +10,00% | 72.842 $ | 25/40 | +62,50% | prezzo iniziale | 66.220 $ | 5/25 | +20,00% | -9,09% | DEBOLE | 17,6 | 19,8 |
| +10,00% | 72.842 $ | 25/40 | +62,50% | -5,00% | 62.909 $ | 4/25 | +16,00% | -13,64% | DEBOLE | 17,6 | 20,5 |
| +10,00% | 72.842 $ | 25/40 | +62,50% | -8,00% | 60.923 $ | 3/25 | +12,00% | -16,36% | DEBOLE | 17,6 | 22,3 |
| +10,00% | 72.842 $ | 25/40 | +62,50% | -10,00% | 59.598 $ | 3/25 | +12,00% | -18,18% | DEBOLE | 17,6 | 22,7 |
| +10,00% | 72.842 $ | 25/40 | +62,50% | -15,00% | 56.287 $ | 2/25 | +8,00% | -22,73% | DEBOLE | 17,6 | 26,0 |
| +15,00% | 76.153 $ | 21/40 | +52,50% | prezzo iniziale | 66.220 $ | 2/21 | +9,52% | -13,04% | DEBOLE | 21,6 | 25,5 |
| +15,00% | 76.153 $ | 21/40 | +52,50% | -5,00% | 62.909 $ | 2/21 | +9,52% | -17,39% | DEBOLE | 21,6 | 26,0 |
| +15,00% | 76.153 $ | 21/40 | +52,50% | -8,00% | 60.923 $ | 2/21 | +9,52% | -20,00% | DEBOLE | 21,6 | 26,0 |
| +15,00% | 76.153 $ | 21/40 | +52,50% | -10,00% | 59.598 $ | 2/21 | +9,52% | -21,74% | DEBOLE | 21,6 | 26,0 |
| +15,00% | 76.153 $ | 21/40 | +52,50% | -15,00% | 56.287 $ | 2/21 | +9,52% | -26,09% | DEBOLE | 21,6 | 26,0 |
| +20,00% | 79.464 $ | 17/40 | +42,50% | prezzo iniziale | 66.220 $ | 0/17 | 0,00% | -16,67% | DEBOLE | 25,6 | n/d |
| +20,00% | 79.464 $ | 17/40 | +42,50% | -5,00% | 62.909 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 25,6 | n/d |
| +20,00% | 79.464 $ | 17/40 | +42,50% | -8,00% | 60.923 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 25,6 | n/d |
| +20,00% | 79.464 $ | 17/40 | +42,50% | -10,00% | 59.598 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 25,6 | n/d |
| +20,00% | 79.464 $ | 17/40 | +42,50% | -15,00% | 56.287 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 25,6 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +20,00% (6/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 3 poi sono scaricati a -5,00%. Percentuale: +20,00% (3/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,95 $ | 30/40 | +75,00% | +5,00% | 81,73 $ | 17/30 | +56,67% | +10,53% | MEDIA | 5,7 | 18,2 |
| -5,00% | 73,95 $ | 30/40 | +75,00% | +10,00% | 85,62 $ | 6/30 | +20,00% | +15,79% | DEBOLE | 5,7 | 18,7 |
| -5,00% | 73,95 $ | 30/40 | +75,00% | +15,00% | 89,52 $ | 4/30 | +13,33% | +21,05% | DEBOLE | 5,7 | 18,8 |
| -5,00% | 73,95 $ | 30/40 | +75,00% | +20,00% | 93,41 $ | 3/30 | +10,00% | +26,32% | DEBOLE | 5,7 | 19,3 |
| -8,00% | 71,61 $ | 21/40 | +52,50% | +5,00% | 81,73 $ | 8/21 | +38,10% | +14,13% | BASSA | 7,7 | 18,5 |
| -8,00% | 71,61 $ | 21/40 | +52,50% | +10,00% | 85,62 $ | 3/21 | +14,29% | +19,57% | DEBOLE | 7,7 | 16,7 |
| -8,00% | 71,61 $ | 21/40 | +52,50% | +15,00% | 89,52 $ | 2/21 | +9,52% | +25,00% | DEBOLE | 7,7 | 15,5 |
| -8,00% | 71,61 $ | 21/40 | +52,50% | +20,00% | 93,41 $ | 1/21 | +4,76% | +30,43% | DEBOLE | 7,7 | 11,0 |
| -10,00% | 70,06 $ | 19/40 | +47,50% | +5,00% | 81,73 $ | 7/19 | +36,84% | +16,67% | BASSA | 8,4 | 19,4 |
| -10,00% | 70,06 $ | 19/40 | +47,50% | +10,00% | 85,62 $ | 2/19 | +10,53% | +22,22% | DEBOLE | 8,4 | 14,5 |
| -10,00% | 70,06 $ | 19/40 | +47,50% | +15,00% | 89,52 $ | 2/19 | +10,53% | +27,78% | DEBOLE | 8,4 | 15,5 |
| -10,00% | 70,06 $ | 19/40 | +47,50% | +20,00% | 93,41 $ | 1/19 | +5,26% | +33,33% | DEBOLE | 8,4 | 11,0 |
| -15,00% | 66,16 $ | 13/40 | +32,50% | +5,00% | 81,73 $ | 2/13 | +15,38% | +23,53% | DEBOLE | 13,2 | 21,5 |
| -15,00% | 66,16 $ | 13/40 | +32,50% | +10,00% | 85,62 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 13,2 | n/d |
| -15,00% | 66,16 $ | 13/40 | +32,50% | +15,00% | 89,52 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 13,2 | n/d |
| -15,00% | 66,16 $ | 13/40 | +32,50% | +20,00% | 93,41 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 13,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 81,73 $ | 28/40 | +70,00% | prezzo iniziale | 77,84 $ | 17/28 | +60,71% | -4,76% | MEDIA | 12,6 | 16,8 |
| +5,00% | 81,73 $ | 28/40 | +70,00% | -5,00% | 73,95 $ | 13/28 | +46,43% | -9,52% | BASSA | 12,6 | 20,5 |
| +5,00% | 81,73 $ | 28/40 | +70,00% | -8,00% | 71,61 $ | 6/28 | +21,43% | -12,38% | DEBOLE | 12,6 | 24,3 |
| +5,00% | 81,73 $ | 28/40 | +70,00% | -10,00% | 70,06 $ | 4/28 | +14,29% | -14,29% | DEBOLE | 12,6 | 21,8 |
| +5,00% | 81,73 $ | 28/40 | +70,00% | -15,00% | 66,16 $ | 2/28 | +7,14% | -19,05% | DEBOLE | 12,6 | 27,5 |
| +10,00% | 85,62 $ | 15/40 | +37,50% | prezzo iniziale | 77,84 $ | 5/15 | +33,33% | -9,09% | DEBOLE | 12,8 | 18,0 |
| +10,00% | 85,62 $ | 15/40 | +37,50% | -5,00% | 73,95 $ | 3/15 | +20,00% | -13,64% | DEBOLE | 12,8 | 22,0 |
| +10,00% | 85,62 $ | 15/40 | +37,50% | -8,00% | 71,61 $ | 0/15 | 0,00% | -16,36% | DEBOLE | 12,8 | n/d |
| +10,00% | 85,62 $ | 15/40 | +37,50% | -10,00% | 70,06 $ | 0/15 | 0,00% | -18,18% | DEBOLE | 12,8 | n/d |
| +10,00% | 85,62 $ | 15/40 | +37,50% | -15,00% | 66,16 $ | 0/15 | 0,00% | -22,73% | DEBOLE | 12,8 | n/d |
| +15,00% | 89,52 $ | 13/40 | +32,50% | prezzo iniziale | 77,84 $ | 3/13 | +23,08% | -13,04% | DEBOLE | 13,6 | 17,3 |
| +15,00% | 89,52 $ | 13/40 | +32,50% | -5,00% | 73,95 $ | 2/13 | +15,38% | -17,39% | DEBOLE | 13,6 | 18,0 |
| +15,00% | 89,52 $ | 13/40 | +32,50% | -8,00% | 71,61 $ | 0/13 | 0,00% | -20,00% | DEBOLE | 13,6 | n/d |
| +15,00% | 89,52 $ | 13/40 | +32,50% | -10,00% | 70,06 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 13,6 | n/d |
| +15,00% | 89,52 $ | 13/40 | +32,50% | -15,00% | 66,16 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 13,6 | n/d |
| +20,00% | 93,41 $ | 8/40 | +20,00% | prezzo iniziale | 77,84 $ | 1/8 | +12,50% | -16,67% | DEBOLE | 13,1 | 7,0 |
| +20,00% | 93,41 $ | 8/40 | +20,00% | -5,00% | 73,95 $ | 1/8 | +12,50% | -20,83% | DEBOLE | 13,1 | 7,0 |
| +20,00% | 93,41 $ | 8/40 | +20,00% | -8,00% | 71,61 $ | 0/8 | 0,00% | -23,33% | DEBOLE | 13,1 | n/d |
| +20,00% | 93,41 $ | 8/40 | +20,00% | -10,00% | 70,06 $ | 0/8 | 0,00% | -25,00% | DEBOLE | 13,1 | n/d |
| +20,00% | 93,41 $ | 8/40 | +20,00% | -15,00% | 66,16 $ | 0/8 | 0,00% | -29,17% | DEBOLE | 13,1 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 37 prima sono scesi a -5,00%. Tra quei 37, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +32,43% (12/37). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 11 poi sono scaricati a -5,00%. Percentuale: +50,00% (11/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06951 $ | 37/40 | +92,50% | +5,00% | 0,07683 $ | 16/37 | +43,24% | +10,53% | BASSA | 6,4 | 13,9 |
| -5,00% | 0,06951 $ | 37/40 | +92,50% | +10,00% | 0,08049 $ | 12/37 | +32,43% | +15,79% | DEBOLE | 6,4 | 17,9 |
| -5,00% | 0,06951 $ | 37/40 | +92,50% | +15,00% | 0,08415 $ | 9/37 | +24,32% | +21,05% | DEBOLE | 6,4 | 19,0 |
| -5,00% | 0,06951 $ | 37/40 | +92,50% | +20,00% | 0,08780 $ | 7/37 | +18,92% | +26,32% | DEBOLE | 6,4 | 21,6 |
| -8,00% | 0,06732 $ | 29/40 | +72,50% | +5,00% | 0,07683 $ | 9/29 | +31,03% | +14,13% | DEBOLE | 6,3 | 13,7 |
| -8,00% | 0,06732 $ | 29/40 | +72,50% | +10,00% | 0,08049 $ | 7/29 | +24,14% | +19,57% | DEBOLE | 6,3 | 15,7 |
| -8,00% | 0,06732 $ | 29/40 | +72,50% | +15,00% | 0,08415 $ | 4/29 | +13,79% | +25,00% | DEBOLE | 6,3 | 13,5 |
| -8,00% | 0,06732 $ | 29/40 | +72,50% | +20,00% | 0,08780 $ | 3/29 | +10,34% | +30,43% | DEBOLE | 6,3 | 15,0 |
| -10,00% | 0,06585 $ | 27/40 | +67,50% | +5,00% | 0,07683 $ | 7/27 | +25,93% | +16,67% | DEBOLE | 6,9 | 14,6 |
| -10,00% | 0,06585 $ | 27/40 | +67,50% | +10,00% | 0,08049 $ | 5/27 | +18,52% | +22,22% | DEBOLE | 6,9 | 17,6 |
| -10,00% | 0,06585 $ | 27/40 | +67,50% | +15,00% | 0,08415 $ | 2/27 | +7,41% | +27,78% | DEBOLE | 6,9 | 9,5 |
| -10,00% | 0,06585 $ | 27/40 | +67,50% | +20,00% | 0,08780 $ | 1/27 | +3,70% | +33,33% | DEBOLE | 6,9 | 9,0 |
| -15,00% | 0,06219 $ | 24/40 | +60,00% | +5,00% | 0,07683 $ | 5/24 | +20,83% | +23,53% | DEBOLE | 7,7 | 14,0 |
| -15,00% | 0,06219 $ | 24/40 | +60,00% | +10,00% | 0,08049 $ | 4/24 | +16,67% | +29,41% | DEBOLE | 7,7 | 14,5 |
| -15,00% | 0,06219 $ | 24/40 | +60,00% | +15,00% | 0,08415 $ | 2/24 | +8,33% | +35,29% | DEBOLE | 7,7 | 9,5 |
| -15,00% | 0,06219 $ | 24/40 | +60,00% | +20,00% | 0,08780 $ | 1/24 | +4,17% | +41,18% | DEBOLE | 7,7 | 9,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07683 $ | 27/40 | +67,50% | prezzo iniziale | 0,07317 $ | 23/27 | +85,19% | -4,76% | ALTA | 8,2 | 12,8 |
| +5,00% | 0,07683 $ | 27/40 | +67,50% | -5,00% | 0,06951 $ | 19/27 | +70,37% | -9,52% | ALTA | 8,2 | 16,1 |
| +5,00% | 0,07683 $ | 27/40 | +67,50% | -8,00% | 0,06732 $ | 13/27 | +48,15% | -12,38% | BASSA | 8,2 | 16,5 |
| +5,00% | 0,07683 $ | 27/40 | +67,50% | -10,00% | 0,06585 $ | 11/27 | +40,74% | -14,29% | BASSA | 8,2 | 18,6 |
| +5,00% | 0,07683 $ | 27/40 | +67,50% | -15,00% | 0,06219 $ | 7/27 | +25,93% | -19,05% | DEBOLE | 8,2 | 18,4 |
| +10,00% | 0,08049 $ | 22/40 | +55,00% | prezzo iniziale | 0,07317 $ | 13/22 | +59,09% | -9,09% | MEDIA | 11,1 | 14,3 |
| +10,00% | 0,08049 $ | 22/40 | +55,00% | -5,00% | 0,06951 $ | 11/22 | +50,00% | -13,64% | MEDIA | 11,1 | 19,5 |
| +10,00% | 0,08049 $ | 22/40 | +55,00% | -8,00% | 0,06732 $ | 6/22 | +27,27% | -16,36% | DEBOLE | 11,1 | 17,3 |
| +10,00% | 0,08049 $ | 22/40 | +55,00% | -10,00% | 0,06585 $ | 5/22 | +22,73% | -18,18% | DEBOLE | 11,1 | 18,0 |
| +10,00% | 0,08049 $ | 22/40 | +55,00% | -15,00% | 0,06219 $ | 3/22 | +13,64% | -22,73% | DEBOLE | 11,1 | 21,3 |
| +15,00% | 0,08415 $ | 18/40 | +45,00% | prezzo iniziale | 0,07317 $ | 9/18 | +50,00% | -13,04% | MEDIA | 12,7 | 15,9 |
| +15,00% | 0,08415 $ | 18/40 | +45,00% | -5,00% | 0,06951 $ | 7/18 | +38,89% | -17,39% | BASSA | 12,7 | 20,4 |
| +15,00% | 0,08415 $ | 18/40 | +45,00% | -8,00% | 0,06732 $ | 4/18 | +22,22% | -20,00% | DEBOLE | 12,7 | 15,5 |
| +15,00% | 0,08415 $ | 18/40 | +45,00% | -10,00% | 0,06585 $ | 4/18 | +22,22% | -21,74% | DEBOLE | 12,7 | 16,8 |
| +15,00% | 0,08415 $ | 18/40 | +45,00% | -15,00% | 0,06219 $ | 2/18 | +11,11% | -26,09% | DEBOLE | 12,7 | 20,0 |
| +20,00% | 0,08780 $ | 11/40 | +27,50% | prezzo iniziale | 0,07317 $ | 3/11 | +27,27% | -16,67% | DEBOLE | 16,5 | 18,0 |
| +20,00% | 0,08780 $ | 11/40 | +27,50% | -5,00% | 0,06951 $ | 2/11 | +18,18% | -20,83% | DEBOLE | 16,5 | 28,5 |
| +20,00% | 0,08780 $ | 11/40 | +27,50% | -8,00% | 0,06732 $ | 0/11 | 0,00% | -23,33% | DEBOLE | 16,5 | n/d |
| +20,00% | 0,08780 $ | 11/40 | +27,50% | -10,00% | 0,06585 $ | 0/11 | 0,00% | -25,00% | DEBOLE | 16,5 | n/d |
| +20,00% | 0,08780 $ | 11/40 | +27,50% | -15,00% | 0,06219 $ | 0/11 | 0,00% | -29,17% | DEBOLE | 16,5 | n/d |

---
