# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-28 07:13:53 CEST**  
UTC: **2026-07-28 05:13:53 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.222 $ | 69.731 $ | +30,43% | +15,79% | rimbalzo poco frequente | 69.731 $ | 60.222 $ | +4,35% | -13,64% | spike storicamente più resistente |
| SOL | 69,62 $ | 80,61 $ | +27,78% | +15,79% | rimbalzo poco frequente | 80,61 $ | 69,62 $ | +4,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06646 $ | 0,07696 $ | +29,63% | +15,79% | rimbalzo poco frequente | 0,07696 $ | 0,06646 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 23 prima sono scesi a -5,00%. Tra quei 23, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +30,43% (7/23). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 1 poi sono scaricati a -5,00%. Percentuale: +4,35% (1/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.222 $ | 23/40 | +57,50% | +5,00% | 66.561 $ | 8/23 | +34,78% | +10,53% | DEBOLE | 6,7 | 16,8 |
| -5,00% | 60.222 $ | 23/40 | +57,50% | +10,00% | 69.731 $ | 7/23 | +30,43% | +15,79% | DEBOLE | 6,7 | 18,9 |
| -5,00% | 60.222 $ | 23/40 | +57,50% | +15,00% | 72.900 $ | 7/23 | +30,43% | +21,05% | DEBOLE | 6,7 | 21,0 |
| -5,00% | 60.222 $ | 23/40 | +57,50% | +20,00% | 76.070 $ | 6/23 | +26,09% | +26,32% | DEBOLE | 6,7 | 22,7 |
| -8,00% | 58.320 $ | 19/40 | +47,50% | +5,00% | 66.561 $ | 5/19 | +26,32% | +14,13% | DEBOLE | 8,7 | 19,2 |
| -8,00% | 58.320 $ | 19/40 | +47,50% | +10,00% | 69.731 $ | 4/19 | +21,05% | +19,57% | DEBOLE | 8,7 | 19,8 |
| -8,00% | 58.320 $ | 19/40 | +47,50% | +15,00% | 72.900 $ | 4/19 | +21,05% | +25,00% | DEBOLE | 8,7 | 22,0 |
| -8,00% | 58.320 $ | 19/40 | +47,50% | +20,00% | 76.070 $ | 4/19 | +21,05% | +30,43% | DEBOLE | 8,7 | 26,5 |
| -10,00% | 57.053 $ | 16/40 | +40,00% | +5,00% | 66.561 $ | 2/16 | +12,50% | +16,67% | DEBOLE | 9,9 | 26,0 |
| -10,00% | 57.053 $ | 16/40 | +40,00% | +10,00% | 69.731 $ | 1/16 | +6,25% | +22,22% | DEBOLE | 9,9 | 23,0 |
| -10,00% | 57.053 $ | 16/40 | +40,00% | +15,00% | 72.900 $ | 1/16 | +6,25% | +27,78% | DEBOLE | 9,9 | 23,0 |
| -10,00% | 57.053 $ | 16/40 | +40,00% | +20,00% | 76.070 $ | 1/16 | +6,25% | +33,33% | DEBOLE | 9,9 | 29,0 |
| -15,00% | 53.883 $ | 12/40 | +30,00% | +5,00% | 66.561 $ | 0/12 | 0,00% | +23,53% | DEBOLE | 10,2 | n/d |
| -15,00% | 53.883 $ | 12/40 | +30,00% | +10,00% | 69.731 $ | 0/12 | 0,00% | +29,41% | DEBOLE | 10,2 | n/d |
| -15,00% | 53.883 $ | 12/40 | +30,00% | +15,00% | 72.900 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 10,2 | n/d |
| -15,00% | 53.883 $ | 12/40 | +30,00% | +20,00% | 76.070 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 10,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.561 $ | 27/40 | +67,50% | prezzo iniziale | 63.392 $ | 5/27 | +18,52% | -4,76% | DEBOLE | 10,6 | 12,2 |
| +5,00% | 66.561 $ | 27/40 | +67,50% | -5,00% | 60.222 $ | 3/27 | +11,11% | -9,52% | DEBOLE | 10,6 | 17,7 |
| +5,00% | 66.561 $ | 27/40 | +67,50% | -8,00% | 58.320 $ | 3/27 | +11,11% | -12,38% | DEBOLE | 10,6 | 18,3 |
| +5,00% | 66.561 $ | 27/40 | +67,50% | -10,00% | 57.053 $ | 2/27 | +7,41% | -14,29% | DEBOLE | 10,6 | 24,5 |
| +5,00% | 66.561 $ | 27/40 | +67,50% | -15,00% | 53.883 $ | 1/27 | +3,70% | -19,05% | DEBOLE | 10,6 | 25,0 |
| +10,00% | 69.731 $ | 23/40 | +57,50% | prezzo iniziale | 63.392 $ | 1/23 | +4,35% | -9,09% | DEBOLE | 14,5 | 19,0 |
| +10,00% | 69.731 $ | 23/40 | +57,50% | -5,00% | 60.222 $ | 1/23 | +4,35% | -13,64% | DEBOLE | 14,5 | 23,0 |
| +10,00% | 69.731 $ | 23/40 | +57,50% | -8,00% | 58.320 $ | 1/23 | +4,35% | -16,36% | DEBOLE | 14,5 | 24,0 |
| +10,00% | 69.731 $ | 23/40 | +57,50% | -10,00% | 57.053 $ | 1/23 | +4,35% | -18,18% | DEBOLE | 14,5 | 24,0 |
| +10,00% | 69.731 $ | 23/40 | +57,50% | -15,00% | 53.883 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 14,5 | n/d |
| +15,00% | 72.900 $ | 20/40 | +50,00% | prezzo iniziale | 63.392 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 16,9 | 19,0 |
| +15,00% | 72.900 $ | 20/40 | +50,00% | -5,00% | 60.222 $ | 1/20 | +5,00% | -17,39% | DEBOLE | 16,9 | 23,0 |
| +15,00% | 72.900 $ | 20/40 | +50,00% | -8,00% | 58.320 $ | 1/20 | +5,00% | -20,00% | DEBOLE | 16,9 | 24,0 |
| +15,00% | 72.900 $ | 20/40 | +50,00% | -10,00% | 57.053 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 16,9 | 24,0 |
| +15,00% | 72.900 $ | 20/40 | +50,00% | -15,00% | 53.883 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 16,9 | n/d |
| +20,00% | 76.070 $ | 17/40 | +42,50% | prezzo iniziale | 63.392 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 18,4 | 19,0 |
| +20,00% | 76.070 $ | 17/40 | +42,50% | -5,00% | 60.222 $ | 1/17 | +5,88% | -20,83% | DEBOLE | 18,4 | 23,0 |
| +20,00% | 76.070 $ | 17/40 | +42,50% | -8,00% | 58.320 $ | 1/17 | +5,88% | -23,33% | DEBOLE | 18,4 | 24,0 |
| +20,00% | 76.070 $ | 17/40 | +42,50% | -10,00% | 57.053 $ | 1/17 | +5,88% | -25,00% | DEBOLE | 18,4 | 24,0 |
| +20,00% | 76.070 $ | 17/40 | +42,50% | -15,00% | 53.883 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 18,4 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +27,78% (5/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 1 poi sono scaricati a -5,00%. Percentuale: +4,00% (1/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 69,62 $ | 18/40 | +45,00% | +5,00% | 76,94 $ | 7/18 | +38,89% | +10,53% | BASSA | 8,1 | 17,0 |
| -5,00% | 69,62 $ | 18/40 | +45,00% | +10,00% | 80,61 $ | 5/18 | +27,78% | +15,79% | DEBOLE | 8,1 | 18,6 |
| -5,00% | 69,62 $ | 18/40 | +45,00% | +15,00% | 84,27 $ | 4/18 | +22,22% | +21,05% | DEBOLE | 8,1 | 19,0 |
| -5,00% | 69,62 $ | 18/40 | +45,00% | +20,00% | 87,94 $ | 3/18 | +16,67% | +26,32% | DEBOLE | 8,1 | 23,0 |
| -8,00% | 67,42 $ | 15/40 | +37,50% | +5,00% | 76,94 $ | 3/15 | +20,00% | +14,13% | DEBOLE | 11,8 | 23,0 |
| -8,00% | 67,42 $ | 15/40 | +37,50% | +10,00% | 80,61 $ | 2/15 | +13,33% | +19,57% | DEBOLE | 11,8 | 22,0 |
| -8,00% | 67,42 $ | 15/40 | +37,50% | +15,00% | 84,27 $ | 2/15 | +13,33% | +25,00% | DEBOLE | 11,8 | 24,0 |
| -8,00% | 67,42 $ | 15/40 | +37,50% | +20,00% | 87,94 $ | 2/15 | +13,33% | +30,43% | DEBOLE | 11,8 | 26,0 |
| -10,00% | 65,95 $ | 12/40 | +30,00% | +5,00% | 76,94 $ | 1/12 | +8,33% | +16,67% | DEBOLE | 14,2 | 25,0 |
| -10,00% | 65,95 $ | 12/40 | +30,00% | +10,00% | 80,61 $ | 0/12 | 0,00% | +22,22% | DEBOLE | 14,2 | n/d |
| -10,00% | 65,95 $ | 12/40 | +30,00% | +15,00% | 84,27 $ | 0/12 | 0,00% | +27,78% | DEBOLE | 14,2 | n/d |
| -10,00% | 65,95 $ | 12/40 | +30,00% | +20,00% | 87,94 $ | 0/12 | 0,00% | +33,33% | DEBOLE | 14,2 | n/d |
| -15,00% | 62,29 $ | 7/40 | +17,50% | +5,00% | 76,94 $ | 0/7 | 0,00% | +23,53% | DEBOLE | 17,9 | n/d |
| -15,00% | 62,29 $ | 7/40 | +17,50% | +10,00% | 80,61 $ | 0/7 | 0,00% | +29,41% | DEBOLE | 17,9 | n/d |
| -15,00% | 62,29 $ | 7/40 | +17,50% | +15,00% | 84,27 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 17,9 | n/d |
| -15,00% | 62,29 $ | 7/40 | +17,50% | +20,00% | 87,94 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 17,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 76,94 $ | 31/40 | +77,50% | prezzo iniziale | 73,28 $ | 7/31 | +22,58% | -4,76% | DEBOLE | 9,0 | 12,4 |
| +5,00% | 76,94 $ | 31/40 | +77,50% | -5,00% | 69,62 $ | 4/31 | +12,90% | -9,52% | DEBOLE | 9,0 | 13,8 |
| +5,00% | 76,94 $ | 31/40 | +77,50% | -8,00% | 67,42 $ | 4/31 | +12,90% | -12,38% | DEBOLE | 9,0 | 14,8 |
| +5,00% | 76,94 $ | 31/40 | +77,50% | -10,00% | 65,95 $ | 2/31 | +6,45% | -14,29% | DEBOLE | 9,0 | 20,5 |
| +5,00% | 76,94 $ | 31/40 | +77,50% | -15,00% | 62,29 $ | 1/31 | +3,23% | -19,05% | DEBOLE | 9,0 | 19,0 |
| +10,00% | 80,61 $ | 25/40 | +62,50% | prezzo iniziale | 73,28 $ | 3/25 | +12,00% | -9,09% | DEBOLE | 11,9 | 18,0 |
| +10,00% | 80,61 $ | 25/40 | +62,50% | -5,00% | 69,62 $ | 1/25 | +4,00% | -13,64% | DEBOLE | 11,9 | 23,0 |
| +10,00% | 80,61 $ | 25/40 | +62,50% | -8,00% | 67,42 $ | 1/25 | +4,00% | -16,36% | DEBOLE | 11,9 | 24,0 |
| +10,00% | 80,61 $ | 25/40 | +62,50% | -10,00% | 65,95 $ | 1/25 | +4,00% | -18,18% | DEBOLE | 11,9 | 24,0 |
| +10,00% | 80,61 $ | 25/40 | +62,50% | -15,00% | 62,29 $ | 0/25 | 0,00% | -22,73% | DEBOLE | 11,9 | n/d |
| +15,00% | 84,27 $ | 22/40 | +55,00% | prezzo iniziale | 73,28 $ | 2/22 | +9,09% | -13,04% | DEBOLE | 13,4 | 20,5 |
| +15,00% | 84,27 $ | 22/40 | +55,00% | -5,00% | 69,62 $ | 1/22 | +4,55% | -17,39% | DEBOLE | 13,4 | 23,0 |
| +15,00% | 84,27 $ | 22/40 | +55,00% | -8,00% | 67,42 $ | 1/22 | +4,55% | -20,00% | DEBOLE | 13,4 | 24,0 |
| +15,00% | 84,27 $ | 22/40 | +55,00% | -10,00% | 65,95 $ | 1/22 | +4,55% | -21,74% | DEBOLE | 13,4 | 24,0 |
| +15,00% | 84,27 $ | 22/40 | +55,00% | -15,00% | 62,29 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 13,4 | n/d |
| +20,00% | 87,94 $ | 16/40 | +40,00% | prezzo iniziale | 73,28 $ | 1/16 | +6,25% | -16,67% | DEBOLE | 14,4 | 19,0 |
| +20,00% | 87,94 $ | 16/40 | +40,00% | -5,00% | 69,62 $ | 1/16 | +6,25% | -20,83% | DEBOLE | 14,4 | 23,0 |
| +20,00% | 87,94 $ | 16/40 | +40,00% | -8,00% | 67,42 $ | 1/16 | +6,25% | -23,33% | DEBOLE | 14,4 | 24,0 |
| +20,00% | 87,94 $ | 16/40 | +40,00% | -10,00% | 65,95 $ | 1/16 | +6,25% | -25,00% | DEBOLE | 14,4 | 24,0 |
| +20,00% | 87,94 $ | 16/40 | +40,00% | -15,00% | 62,29 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 14,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +29,63% (8/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 15 poi sono scaricati a -5,00%. Percentuale: +50,00% (15/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06646 $ | 27/40 | +67,50% | +5,00% | 0,07346 $ | 12/27 | +44,44% | +10,53% | BASSA | 10,1 | 17,4 |
| -5,00% | 0,06646 $ | 27/40 | +67,50% | +10,00% | 0,07696 $ | 8/27 | +29,63% | +15,79% | DEBOLE | 10,1 | 16,1 |
| -5,00% | 0,06646 $ | 27/40 | +67,50% | +15,00% | 0,08045 $ | 6/27 | +22,22% | +21,05% | DEBOLE | 10,1 | 12,5 |
| -5,00% | 0,06646 $ | 27/40 | +67,50% | +20,00% | 0,08395 $ | 5/27 | +18,52% | +26,32% | DEBOLE | 10,1 | 16,2 |
| -8,00% | 0,06436 $ | 23/40 | +57,50% | +5,00% | 0,07346 $ | 9/23 | +39,13% | +14,13% | BASSA | 12,1 | 19,1 |
| -8,00% | 0,06436 $ | 23/40 | +57,50% | +10,00% | 0,07696 $ | 5/23 | +21,74% | +19,57% | DEBOLE | 12,1 | 16,4 |
| -8,00% | 0,06436 $ | 23/40 | +57,50% | +15,00% | 0,08045 $ | 3/23 | +13,04% | +25,00% | DEBOLE | 12,1 | 9,0 |
| -8,00% | 0,06436 $ | 23/40 | +57,50% | +20,00% | 0,08395 $ | 2/23 | +8,70% | +30,43% | DEBOLE | 12,1 | 15,5 |
| -10,00% | 0,06296 $ | 19/40 | +47,50% | +5,00% | 0,07346 $ | 7/19 | +36,84% | +16,67% | BASSA | 11,3 | 18,7 |
| -10,00% | 0,06296 $ | 19/40 | +47,50% | +10,00% | 0,07696 $ | 3/19 | +15,79% | +22,22% | DEBOLE | 11,3 | 8,0 |
| -10,00% | 0,06296 $ | 19/40 | +47,50% | +15,00% | 0,08045 $ | 3/19 | +15,79% | +27,78% | DEBOLE | 11,3 | 9,0 |
| -10,00% | 0,06296 $ | 19/40 | +47,50% | +20,00% | 0,08395 $ | 2/19 | +10,53% | +33,33% | DEBOLE | 11,3 | 15,5 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +5,00% | 0,07346 $ | 2/13 | +15,38% | +23,53% | DEBOLE | 13,9 | 19,0 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +10,00% | 0,07696 $ | 1/13 | +7,69% | +29,41% | DEBOLE | 13,9 | 9,0 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +15,00% | 0,08045 $ | 1/13 | +7,69% | +35,29% | DEBOLE | 13,9 | 10,0 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +20,00% | 0,08395 $ | 1/13 | +7,69% | +41,18% | DEBOLE | 13,9 | 24,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07346 $ | 36/40 | +90,00% | prezzo iniziale | 0,06996 $ | 26/36 | +72,22% | -4,76% | ALTA | 5,2 | 10,3 |
| +5,00% | 0,07346 $ | 36/40 | +90,00% | -5,00% | 0,06646 $ | 21/36 | +58,33% | -9,52% | MEDIA | 5,2 | 14,0 |
| +5,00% | 0,07346 $ | 36/40 | +90,00% | -8,00% | 0,06436 $ | 17/36 | +47,22% | -12,38% | BASSA | 5,2 | 14,4 |
| +5,00% | 0,07346 $ | 36/40 | +90,00% | -10,00% | 0,06296 $ | 13/36 | +36,11% | -14,29% | BASSA | 5,2 | 12,5 |
| +5,00% | 0,07346 $ | 36/40 | +90,00% | -15,00% | 0,05947 $ | 8/36 | +22,22% | -19,05% | DEBOLE | 5,2 | 16,0 |
| +10,00% | 0,07696 $ | 30/40 | +75,00% | prezzo iniziale | 0,06996 $ | 19/30 | +63,33% | -9,09% | MEDIA | 7,8 | 13,2 |
| +10,00% | 0,07696 $ | 30/40 | +75,00% | -5,00% | 0,06646 $ | 15/30 | +50,00% | -13,64% | MEDIA | 7,8 | 16,4 |
| +10,00% | 0,07696 $ | 30/40 | +75,00% | -8,00% | 0,06436 $ | 11/30 | +36,67% | -16,36% | BASSA | 7,8 | 16,8 |
| +10,00% | 0,07696 $ | 30/40 | +75,00% | -10,00% | 0,06296 $ | 7/30 | +23,33% | -18,18% | DEBOLE | 7,8 | 12,9 |
| +10,00% | 0,07696 $ | 30/40 | +75,00% | -15,00% | 0,05947 $ | 6/30 | +20,00% | -22,73% | DEBOLE | 7,8 | 14,2 |
| +15,00% | 0,08045 $ | 21/40 | +52,50% | prezzo iniziale | 0,06996 $ | 9/21 | +42,86% | -13,04% | BASSA | 10,0 | 15,8 |
| +15,00% | 0,08045 $ | 21/40 | +52,50% | -5,00% | 0,06646 $ | 7/21 | +33,33% | -17,39% | DEBOLE | 10,0 | 20,3 |
| +15,00% | 0,08045 $ | 21/40 | +52,50% | -8,00% | 0,06436 $ | 4/21 | +19,05% | -20,00% | DEBOLE | 10,0 | 19,8 |
| +15,00% | 0,08045 $ | 21/40 | +52,50% | -10,00% | 0,06296 $ | 2/21 | +9,52% | -21,74% | DEBOLE | 10,0 | 13,5 |
| +15,00% | 0,08045 $ | 21/40 | +52,50% | -15,00% | 0,05947 $ | 1/21 | +4,76% | -26,09% | DEBOLE | 10,0 | 11,0 |
| +20,00% | 0,08395 $ | 18/40 | +45,00% | prezzo iniziale | 0,06996 $ | 6/18 | +33,33% | -16,67% | DEBOLE | 12,5 | 18,7 |
| +20,00% | 0,08395 $ | 18/40 | +45,00% | -5,00% | 0,06646 $ | 3/18 | +16,67% | -20,83% | DEBOLE | 12,5 | 20,7 |
| +20,00% | 0,08395 $ | 18/40 | +45,00% | -8,00% | 0,06436 $ | 1/18 | +5,56% | -23,33% | DEBOLE | 12,5 | 25,0 |
| +20,00% | 0,08395 $ | 18/40 | +45,00% | -10,00% | 0,06296 $ | 0/18 | 0,00% | -25,00% | DEBOLE | 12,5 | n/d |
| +20,00% | 0,08395 $ | 18/40 | +45,00% | -15,00% | 0,05947 $ | 0/18 | 0,00% | -29,17% | DEBOLE | 12,5 | n/d |

---
