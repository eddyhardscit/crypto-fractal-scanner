# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-06 07:14:34 CEST**  
UTC: **2026-08-06 05:14:34 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.606 $ | 71.333 $ | +23,53% | +15,79% | rimbalzo poco frequente | 71.333 $ | 61.606 $ | +8,33% | -13,64% | spike storicamente più resistente |
| SOL | 70,42 $ | 81,54 $ | +18,75% | +15,79% | rimbalzo poco frequente | 81,54 $ | 70,42 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06648 $ | 0,07698 $ | +35,48% | +15,79% | rimbalzo debole | 0,07698 $ | 0,06648 $ | +16,67% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +23,53% (4/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 2 poi sono scaricati a -5,00%. Percentuale: +8,33% (2/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.606 $ | 17/40 | +42,50% | +5,00% | 68.090 $ | 7/17 | +41,18% | +10,53% | BASSA | 10,5 | 20,0 |
| -5,00% | 61.606 $ | 17/40 | +42,50% | +10,00% | 71.333 $ | 4/17 | +23,53% | +15,79% | DEBOLE | 10,5 | 17,2 |
| -5,00% | 61.606 $ | 17/40 | +42,50% | +15,00% | 74.575 $ | 4/17 | +23,53% | +21,05% | DEBOLE | 10,5 | 18,2 |
| -5,00% | 61.606 $ | 17/40 | +42,50% | +20,00% | 77.817 $ | 4/17 | +23,53% | +26,32% | DEBOLE | 10,5 | 19,0 |
| -8,00% | 59.660 $ | 13/40 | +32,50% | +5,00% | 68.090 $ | 3/13 | +23,08% | +14,13% | DEBOLE | 13,5 | 24,7 |
| -8,00% | 59.660 $ | 13/40 | +32,50% | +10,00% | 71.333 $ | 1/13 | +7,69% | +19,57% | DEBOLE | 13,5 | 27,0 |
| -8,00% | 59.660 $ | 13/40 | +32,50% | +15,00% | 74.575 $ | 1/13 | +7,69% | +25,00% | DEBOLE | 13,5 | 28,0 |
| -8,00% | 59.660 $ | 13/40 | +32,50% | +20,00% | 77.817 $ | 1/13 | +7,69% | +30,43% | DEBOLE | 13,5 | 30,0 |
| -10,00% | 58.363 $ | 12/40 | +30,00% | +5,00% | 68.090 $ | 2/12 | +16,67% | +16,67% | DEBOLE | 14,8 | 27,0 |
| -10,00% | 58.363 $ | 12/40 | +30,00% | +10,00% | 71.333 $ | 0/12 | 0,00% | +22,22% | DEBOLE | 14,8 | n/d |
| -10,00% | 58.363 $ | 12/40 | +30,00% | +15,00% | 74.575 $ | 0/12 | 0,00% | +27,78% | DEBOLE | 14,8 | n/d |
| -10,00% | 58.363 $ | 12/40 | +30,00% | +20,00% | 77.817 $ | 0/12 | 0,00% | +33,33% | DEBOLE | 14,8 | n/d |
| -15,00% | 55.121 $ | 7/40 | +17,50% | +5,00% | 68.090 $ | 0/7 | 0,00% | +23,53% | DEBOLE | 14,4 | n/d |
| -15,00% | 55.121 $ | 7/40 | +17,50% | +10,00% | 71.333 $ | 0/7 | 0,00% | +29,41% | DEBOLE | 14,4 | n/d |
| -15,00% | 55.121 $ | 7/40 | +17,50% | +15,00% | 74.575 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 14,4 | n/d |
| -15,00% | 55.121 $ | 7/40 | +17,50% | +20,00% | 77.817 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 14,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 68.090 $ | 33/40 | +82,50% | prezzo iniziale | 64.848 $ | 7/33 | +21,21% | -4,76% | DEBOLE | 9,9 | 11,7 |
| +5,00% | 68.090 $ | 33/40 | +82,50% | -5,00% | 61.606 $ | 6/33 | +18,18% | -9,52% | DEBOLE | 9,9 | 15,3 |
| +5,00% | 68.090 $ | 33/40 | +82,50% | -8,00% | 59.660 $ | 5/33 | +15,15% | -12,38% | DEBOLE | 9,9 | 17,2 |
| +5,00% | 68.090 $ | 33/40 | +82,50% | -10,00% | 58.363 $ | 5/33 | +15,15% | -14,29% | DEBOLE | 9,9 | 18,0 |
| +5,00% | 68.090 $ | 33/40 | +82,50% | -15,00% | 55.121 $ | 2/33 | +6,06% | -19,05% | DEBOLE | 9,9 | 11,0 |
| +10,00% | 71.333 $ | 24/40 | +60,00% | prezzo iniziale | 64.848 $ | 2/24 | +8,33% | -9,09% | DEBOLE | 14,1 | 11,5 |
| +10,00% | 71.333 $ | 24/40 | +60,00% | -5,00% | 61.606 $ | 2/24 | +8,33% | -13,64% | DEBOLE | 14,1 | 16,0 |
| +10,00% | 71.333 $ | 24/40 | +60,00% | -8,00% | 59.660 $ | 2/24 | +8,33% | -16,36% | DEBOLE | 14,1 | 16,5 |
| +10,00% | 71.333 $ | 24/40 | +60,00% | -10,00% | 58.363 $ | 2/24 | +8,33% | -18,18% | DEBOLE | 14,1 | 17,0 |
| +10,00% | 71.333 $ | 24/40 | +60,00% | -15,00% | 55.121 $ | 1/24 | +4,17% | -22,73% | DEBOLE | 14,1 | 10,0 |
| +15,00% | 74.575 $ | 17/40 | +42,50% | prezzo iniziale | 64.848 $ | 1/17 | +5,88% | -13,04% | DEBOLE | 13,4 | 6,0 |
| +15,00% | 74.575 $ | 17/40 | +42,50% | -5,00% | 61.606 $ | 1/17 | +5,88% | -17,39% | DEBOLE | 13,4 | 7,0 |
| +15,00% | 74.575 $ | 17/40 | +42,50% | -8,00% | 59.660 $ | 1/17 | +5,88% | -20,00% | DEBOLE | 13,4 | 7,0 |
| +15,00% | 74.575 $ | 17/40 | +42,50% | -10,00% | 58.363 $ | 1/17 | +5,88% | -21,74% | DEBOLE | 13,4 | 7,0 |
| +15,00% | 74.575 $ | 17/40 | +42,50% | -15,00% | 55.121 $ | 1/17 | +5,88% | -26,09% | DEBOLE | 13,4 | 10,0 |
| +20,00% | 77.817 $ | 16/40 | +40,00% | prezzo iniziale | 64.848 $ | 1/16 | +6,25% | -16,67% | DEBOLE | 15,5 | 6,0 |
| +20,00% | 77.817 $ | 16/40 | +40,00% | -5,00% | 61.606 $ | 1/16 | +6,25% | -20,83% | DEBOLE | 15,5 | 7,0 |
| +20,00% | 77.817 $ | 16/40 | +40,00% | -8,00% | 59.660 $ | 1/16 | +6,25% | -23,33% | DEBOLE | 15,5 | 7,0 |
| +20,00% | 77.817 $ | 16/40 | +40,00% | -10,00% | 58.363 $ | 1/16 | +6,25% | -25,00% | DEBOLE | 15,5 | 7,0 |
| +20,00% | 77.817 $ | 16/40 | +40,00% | -15,00% | 55.121 $ | 1/16 | +6,25% | -29,17% | DEBOLE | 15,5 | 10,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +18,75% (3/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 70,42 $ | 16/40 | +40,00% | +5,00% | 77,84 $ | 5/16 | +31,25% | +10,53% | DEBOLE | 6,8 | 23,8 |
| -5,00% | 70,42 $ | 16/40 | +40,00% | +10,00% | 81,54 $ | 3/16 | +18,75% | +15,79% | DEBOLE | 6,8 | 29,3 |
| -5,00% | 70,42 $ | 16/40 | +40,00% | +15,00% | 85,25 $ | 1/16 | +6,25% | +21,05% | DEBOLE | 6,8 | 28,0 |
| -5,00% | 70,42 $ | 16/40 | +40,00% | +20,00% | 88,96 $ | 0/16 | 0,00% | +26,32% | DEBOLE | 6,8 | n/d |
| -8,00% | 68,20 $ | 15/40 | +37,50% | +5,00% | 77,84 $ | 4/15 | +26,67% | +14,13% | DEBOLE | 9,7 | 26,8 |
| -8,00% | 68,20 $ | 15/40 | +37,50% | +10,00% | 81,54 $ | 3/15 | +20,00% | +19,57% | DEBOLE | 9,7 | 29,3 |
| -8,00% | 68,20 $ | 15/40 | +37,50% | +15,00% | 85,25 $ | 1/15 | +6,67% | +25,00% | DEBOLE | 9,7 | 28,0 |
| -8,00% | 68,20 $ | 15/40 | +37,50% | +20,00% | 88,96 $ | 0/15 | 0,00% | +30,43% | DEBOLE | 9,7 | n/d |
| -10,00% | 66,72 $ | 15/40 | +37,50% | +5,00% | 77,84 $ | 4/15 | +26,67% | +16,67% | DEBOLE | 10,1 | 26,8 |
| -10,00% | 66,72 $ | 15/40 | +37,50% | +10,00% | 81,54 $ | 3/15 | +20,00% | +22,22% | DEBOLE | 10,1 | 29,3 |
| -10,00% | 66,72 $ | 15/40 | +37,50% | +15,00% | 85,25 $ | 1/15 | +6,67% | +27,78% | DEBOLE | 10,1 | 28,0 |
| -10,00% | 66,72 $ | 15/40 | +37,50% | +20,00% | 88,96 $ | 0/15 | 0,00% | +33,33% | DEBOLE | 10,1 | n/d |
| -15,00% | 63,01 $ | 10/40 | +25,00% | +5,00% | 77,84 $ | 3/10 | +30,00% | +23,53% | DEBOLE | 12,7 | 26,3 |
| -15,00% | 63,01 $ | 10/40 | +25,00% | +10,00% | 81,54 $ | 2/10 | +20,00% | +29,41% | DEBOLE | 12,7 | 29,0 |
| -15,00% | 63,01 $ | 10/40 | +25,00% | +15,00% | 85,25 $ | 1/10 | +10,00% | +35,29% | DEBOLE | 12,7 | 28,0 |
| -15,00% | 63,01 $ | 10/40 | +25,00% | +20,00% | 88,96 $ | 0/10 | 0,00% | +41,18% | DEBOLE | 12,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,84 $ | 28/40 | +70,00% | prezzo iniziale | 74,13 $ | 6/28 | +21,43% | -4,76% | DEBOLE | 9,3 | 12,3 |
| +5,00% | 77,84 $ | 28/40 | +70,00% | -5,00% | 70,42 $ | 2/28 | +7,14% | -9,52% | DEBOLE | 9,3 | 12,5 |
| +5,00% | 77,84 $ | 28/40 | +70,00% | -8,00% | 68,20 $ | 1/28 | +3,57% | -12,38% | DEBOLE | 9,3 | 15,0 |
| +5,00% | 77,84 $ | 28/40 | +70,00% | -10,00% | 66,72 $ | 1/28 | +3,57% | -14,29% | DEBOLE | 9,3 | 17,0 |
| +5,00% | 77,84 $ | 28/40 | +70,00% | -15,00% | 63,01 $ | 0/28 | 0,00% | -19,05% | DEBOLE | 9,3 | n/d |
| +10,00% | 81,54 $ | 23/40 | +57,50% | prezzo iniziale | 74,13 $ | 2/23 | +8,70% | -9,09% | DEBOLE | 15,3 | 20,5 |
| +10,00% | 81,54 $ | 23/40 | +57,50% | -5,00% | 70,42 $ | 0/23 | 0,00% | -13,64% | DEBOLE | 15,3 | n/d |
| +10,00% | 81,54 $ | 23/40 | +57,50% | -8,00% | 68,20 $ | 0/23 | 0,00% | -16,36% | DEBOLE | 15,3 | n/d |
| +10,00% | 81,54 $ | 23/40 | +57,50% | -10,00% | 66,72 $ | 0/23 | 0,00% | -18,18% | DEBOLE | 15,3 | n/d |
| +10,00% | 81,54 $ | 23/40 | +57,50% | -15,00% | 63,01 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 15,3 | n/d |
| +15,00% | 85,25 $ | 16/40 | +40,00% | prezzo iniziale | 74,13 $ | 2/16 | +12,50% | -13,04% | DEBOLE | 15,1 | 20,5 |
| +15,00% | 85,25 $ | 16/40 | +40,00% | -5,00% | 70,42 $ | 0/16 | 0,00% | -17,39% | DEBOLE | 15,1 | n/d |
| +15,00% | 85,25 $ | 16/40 | +40,00% | -8,00% | 68,20 $ | 0/16 | 0,00% | -20,00% | DEBOLE | 15,1 | n/d |
| +15,00% | 85,25 $ | 16/40 | +40,00% | -10,00% | 66,72 $ | 0/16 | 0,00% | -21,74% | DEBOLE | 15,1 | n/d |
| +15,00% | 85,25 $ | 16/40 | +40,00% | -15,00% | 63,01 $ | 0/16 | 0,00% | -26,09% | DEBOLE | 15,1 | n/d |
| +20,00% | 88,96 $ | 12/40 | +30,00% | prezzo iniziale | 74,13 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 16,8 | n/d |
| +20,00% | 88,96 $ | 12/40 | +30,00% | -5,00% | 70,42 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 16,8 | n/d |
| +20,00% | 88,96 $ | 12/40 | +30,00% | -8,00% | 68,20 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 16,8 | n/d |
| +20,00% | 88,96 $ | 12/40 | +30,00% | -10,00% | 66,72 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 16,8 | n/d |
| +20,00% | 88,96 $ | 12/40 | +30,00% | -15,00% | 63,01 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 16,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +35,48% (11/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 4 poi sono scaricati a -5,00%. Percentuale: +16,67% (4/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06648 $ | 31/40 | +77,50% | +5,00% | 0,07348 $ | 14/31 | +45,16% | +10,53% | BASSA | 4,9 | 18,0 |
| -5,00% | 0,06648 $ | 31/40 | +77,50% | +10,00% | 0,07698 $ | 11/31 | +35,48% | +15,79% | BASSA | 4,9 | 18,7 |
| -5,00% | 0,06648 $ | 31/40 | +77,50% | +15,00% | 0,08048 $ | 10/31 | +32,26% | +21,05% | DEBOLE | 4,9 | 20,2 |
| -5,00% | 0,06648 $ | 31/40 | +77,50% | +20,00% | 0,08398 $ | 5/31 | +16,13% | +26,32% | DEBOLE | 4,9 | 26,0 |
| -8,00% | 0,06438 $ | 28/40 | +70,00% | +5,00% | 0,07348 $ | 11/28 | +39,29% | +14,13% | BASSA | 6,9 | 19,3 |
| -8,00% | 0,06438 $ | 28/40 | +70,00% | +10,00% | 0,07698 $ | 8/28 | +28,57% | +19,57% | DEBOLE | 6,9 | 20,4 |
| -8,00% | 0,06438 $ | 28/40 | +70,00% | +15,00% | 0,08048 $ | 7/28 | +25,00% | +25,00% | DEBOLE | 6,9 | 20,9 |
| -8,00% | 0,06438 $ | 28/40 | +70,00% | +20,00% | 0,08398 $ | 4/28 | +14,29% | +30,43% | DEBOLE | 6,9 | 26,0 |
| -10,00% | 0,06298 $ | 26/40 | +65,00% | +5,00% | 0,07348 $ | 9/26 | +34,62% | +16,67% | DEBOLE | 8,0 | 20,6 |
| -10,00% | 0,06298 $ | 26/40 | +65,00% | +10,00% | 0,07698 $ | 6/26 | +23,08% | +22,22% | DEBOLE | 8,0 | 20,5 |
| -10,00% | 0,06298 $ | 26/40 | +65,00% | +15,00% | 0,08048 $ | 5/26 | +19,23% | +27,78% | DEBOLE | 8,0 | 21,0 |
| -10,00% | 0,06298 $ | 26/40 | +65,00% | +20,00% | 0,08398 $ | 3/26 | +11,54% | +33,33% | DEBOLE | 8,0 | 25,7 |
| -15,00% | 0,05948 $ | 19/40 | +47,50% | +5,00% | 0,07348 $ | 4/19 | +21,05% | +23,53% | DEBOLE | 9,3 | 19,5 |
| -15,00% | 0,05948 $ | 19/40 | +47,50% | +10,00% | 0,07698 $ | 3/19 | +15,79% | +29,41% | DEBOLE | 9,3 | 19,0 |
| -15,00% | 0,05948 $ | 19/40 | +47,50% | +15,00% | 0,08048 $ | 3/19 | +15,79% | +35,29% | DEBOLE | 9,3 | 19,0 |
| -15,00% | 0,05948 $ | 19/40 | +47,50% | +20,00% | 0,08398 $ | 3/19 | +15,79% | +41,18% | DEBOLE | 9,3 | 25,7 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07348 $ | 28/40 | +70,00% | prezzo iniziale | 0,06998 $ | 15/28 | +53,57% | -4,76% | MEDIA | 10,8 | 15,8 |
| +5,00% | 0,07348 $ | 28/40 | +70,00% | -5,00% | 0,06648 $ | 8/28 | +28,57% | -9,52% | DEBOLE | 10,8 | 14,6 |
| +5,00% | 0,07348 $ | 28/40 | +70,00% | -8,00% | 0,06438 $ | 8/28 | +28,57% | -12,38% | DEBOLE | 10,8 | 15,4 |
| +5,00% | 0,07348 $ | 28/40 | +70,00% | -10,00% | 0,06298 $ | 7/28 | +25,00% | -14,29% | DEBOLE | 10,8 | 14,6 |
| +5,00% | 0,07348 $ | 28/40 | +70,00% | -15,00% | 0,05948 $ | 4/28 | +14,29% | -19,05% | DEBOLE | 10,8 | 14,0 |
| +10,00% | 0,07698 $ | 24/40 | +60,00% | prezzo iniziale | 0,06998 $ | 10/24 | +41,67% | -9,09% | BASSA | 13,0 | 16,1 |
| +10,00% | 0,07698 $ | 24/40 | +60,00% | -5,00% | 0,06648 $ | 4/24 | +16,67% | -13,64% | DEBOLE | 13,0 | 15,8 |
| +10,00% | 0,07698 $ | 24/40 | +60,00% | -8,00% | 0,06438 $ | 4/24 | +16,67% | -16,36% | DEBOLE | 13,0 | 16,0 |
| +10,00% | 0,07698 $ | 24/40 | +60,00% | -10,00% | 0,06298 $ | 4/24 | +16,67% | -18,18% | DEBOLE | 13,0 | 16,5 |
| +10,00% | 0,07698 $ | 24/40 | +60,00% | -15,00% | 0,05948 $ | 3/24 | +12,50% | -22,73% | DEBOLE | 13,0 | 15,7 |
| +15,00% | 0,08048 $ | 20/40 | +50,00% | prezzo iniziale | 0,06998 $ | 5/20 | +25,00% | -13,04% | DEBOLE | 16,2 | 15,4 |
| +15,00% | 0,08048 $ | 20/40 | +50,00% | -5,00% | 0,06648 $ | 2/20 | +10,00% | -17,39% | DEBOLE | 16,2 | 13,0 |
| +15,00% | 0,08048 $ | 20/40 | +50,00% | -8,00% | 0,06438 $ | 2/20 | +10,00% | -20,00% | DEBOLE | 16,2 | 13,5 |
| +15,00% | 0,08048 $ | 20/40 | +50,00% | -10,00% | 0,06298 $ | 2/20 | +10,00% | -21,74% | DEBOLE | 16,2 | 13,5 |
| +15,00% | 0,08048 $ | 20/40 | +50,00% | -15,00% | 0,05948 $ | 2/20 | +10,00% | -26,09% | DEBOLE | 16,2 | 18,0 |
| +20,00% | 0,08398 $ | 13/40 | +32,50% | prezzo iniziale | 0,06998 $ | 1/13 | +7,69% | -16,67% | DEBOLE | 22,2 | 30,0 |
| +20,00% | 0,08398 $ | 13/40 | +32,50% | -5,00% | 0,06648 $ | 0/13 | 0,00% | -20,83% | DEBOLE | 22,2 | n/d |
| +20,00% | 0,08398 $ | 13/40 | +32,50% | -8,00% | 0,06438 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 22,2 | n/d |
| +20,00% | 0,08398 $ | 13/40 | +32,50% | -10,00% | 0,06298 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 22,2 | n/d |
| +20,00% | 0,08398 $ | 13/40 | +32,50% | -15,00% | 0,05948 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 22,2 | n/d |

---
