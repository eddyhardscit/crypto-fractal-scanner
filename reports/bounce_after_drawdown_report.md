# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-13 08:27:42 CEST**  
UTC: **2026-07-13 06:27:42 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.548 $ | 68.950 $ | +23,53% | +15,79% | rimbalzo poco frequente | 68.950 $ | 59.548 $ | +8,00% | -13,64% | spike storicamente più resistente |
| SOL | 72,48 $ | 83,92 $ | +12,90% | +15,79% | rimbalzo poco frequente | 83,92 $ | 72,48 $ | +43,75% | -13,64% | scarico possibile |
| DOGE | 0,06853 $ | 0,07935 $ | +13,89% | +15,79% | rimbalzo poco frequente | 0,07935 $ | 0,06853 $ | +56,25% | -13,64% | attenzione a prendere profitto |

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
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 2 poi sono scaricati a -5,00%. Percentuale: +8,00% (2/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.548 $ | 17/40 | +42,50% | +5,00% | 65.816 $ | 6/17 | +35,29% | +10,53% | BASSA | 12,4 | 23,5 |
| -5,00% | 59.548 $ | 17/40 | +42,50% | +10,00% | 68.950 $ | 4/17 | +23,53% | +15,79% | DEBOLE | 12,4 | 23,8 |
| -5,00% | 59.548 $ | 17/40 | +42,50% | +15,00% | 72.084 $ | 1/17 | +5,88% | +21,05% | DEBOLE | 12,4 | 29,0 |
| -5,00% | 59.548 $ | 17/40 | +42,50% | +20,00% | 75.218 $ | 0/17 | 0,00% | +26,32% | DEBOLE | 12,4 | n/d |
| -8,00% | 57.667 $ | 14/40 | +35,00% | +5,00% | 65.816 $ | 3/14 | +21,43% | +14,13% | DEBOLE | 14,6 | 23,0 |
| -8,00% | 57.667 $ | 14/40 | +35,00% | +10,00% | 68.950 $ | 1/14 | +7,14% | +19,57% | DEBOLE | 14,6 | 18,0 |
| -8,00% | 57.667 $ | 14/40 | +35,00% | +15,00% | 72.084 $ | 0/14 | 0,00% | +25,00% | DEBOLE | 14,6 | n/d |
| -8,00% | 57.667 $ | 14/40 | +35,00% | +20,00% | 75.218 $ | 0/14 | 0,00% | +30,43% | DEBOLE | 14,6 | n/d |
| -10,00% | 56.414 $ | 12/40 | +30,00% | +5,00% | 65.816 $ | 2/12 | +16,67% | +16,67% | DEBOLE | 16,0 | 21,5 |
| -10,00% | 56.414 $ | 12/40 | +30,00% | +10,00% | 68.950 $ | 1/12 | +8,33% | +22,22% | DEBOLE | 16,0 | 18,0 |
| -10,00% | 56.414 $ | 12/40 | +30,00% | +15,00% | 72.084 $ | 0/12 | 0,00% | +27,78% | DEBOLE | 16,0 | n/d |
| -10,00% | 56.414 $ | 12/40 | +30,00% | +20,00% | 75.218 $ | 0/12 | 0,00% | +33,33% | DEBOLE | 16,0 | n/d |
| -15,00% | 53.280 $ | 8/40 | +20,00% | +5,00% | 65.816 $ | 0/8 | 0,00% | +23,53% | DEBOLE | 17,9 | n/d |
| -15,00% | 53.280 $ | 8/40 | +20,00% | +10,00% | 68.950 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 17,9 | n/d |
| -15,00% | 53.280 $ | 8/40 | +20,00% | +15,00% | 72.084 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 17,9 | n/d |
| -15,00% | 53.280 $ | 8/40 | +20,00% | +20,00% | 75.218 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 17,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.816 $ | 36/40 | +90,00% | prezzo iniziale | 62.682 $ | 22/36 | +61,11% | -4,76% | MEDIA | 4,2 | 13,0 |
| +5,00% | 65.816 $ | 36/40 | +90,00% | -5,00% | 59.548 $ | 13/36 | +36,11% | -9,52% | BASSA | 4,2 | 18,5 |
| +5,00% | 65.816 $ | 36/40 | +90,00% | -8,00% | 57.667 $ | 9/36 | +25,00% | -12,38% | DEBOLE | 4,2 | 18,8 |
| +5,00% | 65.816 $ | 36/40 | +90,00% | -10,00% | 56.414 $ | 8/36 | +22,22% | -14,29% | DEBOLE | 4,2 | 20,9 |
| +5,00% | 65.816 $ | 36/40 | +90,00% | -15,00% | 53.280 $ | 5/36 | +13,89% | -19,05% | DEBOLE | 4,2 | 23,6 |
| +10,00% | 68.950 $ | 25/40 | +62,50% | prezzo iniziale | 62.682 $ | 6/25 | +24,00% | -9,09% | DEBOLE | 10,5 | 15,7 |
| +10,00% | 68.950 $ | 25/40 | +62,50% | -5,00% | 59.548 $ | 2/25 | +8,00% | -13,64% | DEBOLE | 10,5 | 13,0 |
| +10,00% | 68.950 $ | 25/40 | +62,50% | -8,00% | 57.667 $ | 2/25 | +8,00% | -16,36% | DEBOLE | 10,5 | 13,0 |
| +10,00% | 68.950 $ | 25/40 | +62,50% | -10,00% | 56.414 $ | 2/25 | +8,00% | -18,18% | DEBOLE | 10,5 | 13,0 |
| +10,00% | 68.950 $ | 25/40 | +62,50% | -15,00% | 53.280 $ | 1/25 | +4,00% | -22,73% | DEBOLE | 10,5 | 11,0 |
| +15,00% | 72.084 $ | 20/40 | +50,00% | prezzo iniziale | 62.682 $ | 5/20 | +25,00% | -13,04% | DEBOLE | 10,1 | 16,4 |
| +15,00% | 72.084 $ | 20/40 | +50,00% | -5,00% | 59.548 $ | 1/20 | +5,00% | -17,39% | DEBOLE | 10,1 | 11,0 |
| +15,00% | 72.084 $ | 20/40 | +50,00% | -8,00% | 57.667 $ | 1/20 | +5,00% | -20,00% | DEBOLE | 10,1 | 11,0 |
| +15,00% | 72.084 $ | 20/40 | +50,00% | -10,00% | 56.414 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 10,1 | 11,0 |
| +15,00% | 72.084 $ | 20/40 | +50,00% | -15,00% | 53.280 $ | 1/20 | +5,00% | -26,09% | DEBOLE | 10,1 | 11,0 |
| +20,00% | 75.218 $ | 14/40 | +35,00% | prezzo iniziale | 62.682 $ | 1/14 | +7,14% | -16,67% | DEBOLE | 11,1 | 22,0 |
| +20,00% | 75.218 $ | 14/40 | +35,00% | -5,00% | 59.548 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 11,1 | n/d |
| +20,00% | 75.218 $ | 14/40 | +35,00% | -8,00% | 57.667 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 11,1 | n/d |
| +20,00% | 75.218 $ | 14/40 | +35,00% | -10,00% | 56.414 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 11,1 | n/d |
| +20,00% | 75.218 $ | 14/40 | +35,00% | -15,00% | 53.280 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 11,1 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +12,90% (4/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 7 poi sono scaricati a -5,00%. Percentuale: +43,75% (7/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,48 $ | 31/40 | +77,50% | +5,00% | 80,10 $ | 6/31 | +19,35% | +10,53% | DEBOLE | 7,3 | 18,7 |
| -5,00% | 72,48 $ | 31/40 | +77,50% | +10,00% | 83,92 $ | 4/31 | +12,90% | +15,79% | DEBOLE | 7,3 | 17,0 |
| -5,00% | 72,48 $ | 31/40 | +77,50% | +15,00% | 87,73 $ | 2/31 | +6,45% | +21,05% | DEBOLE | 7,3 | 22,0 |
| -5,00% | 72,48 $ | 31/40 | +77,50% | +20,00% | 91,55 $ | 1/31 | +3,23% | +26,32% | DEBOLE | 7,3 | 16,0 |
| -8,00% | 70,19 $ | 30/40 | +75,00% | +5,00% | 80,10 $ | 5/30 | +16,67% | +14,13% | DEBOLE | 10,3 | 18,6 |
| -8,00% | 70,19 $ | 30/40 | +75,00% | +10,00% | 83,92 $ | 3/30 | +10,00% | +19,57% | DEBOLE | 10,3 | 16,0 |
| -8,00% | 70,19 $ | 30/40 | +75,00% | +15,00% | 87,73 $ | 1/30 | +3,33% | +25,00% | DEBOLE | 10,3 | 15,0 |
| -8,00% | 70,19 $ | 30/40 | +75,00% | +20,00% | 91,55 $ | 1/30 | +3,33% | +30,43% | DEBOLE | 10,3 | 16,0 |
| -10,00% | 68,66 $ | 25/40 | +62,50% | +5,00% | 80,10 $ | 4/25 | +16,00% | +16,67% | DEBOLE | 11,8 | 19,5 |
| -10,00% | 68,66 $ | 25/40 | +62,50% | +10,00% | 83,92 $ | 2/25 | +8,00% | +22,22% | DEBOLE | 11,8 | 16,5 |
| -10,00% | 68,66 $ | 25/40 | +62,50% | +15,00% | 87,73 $ | 0/25 | 0,00% | +27,78% | DEBOLE | 11,8 | n/d |
| -10,00% | 68,66 $ | 25/40 | +62,50% | +20,00% | 91,55 $ | 0/25 | 0,00% | +33,33% | DEBOLE | 11,8 | n/d |
| -15,00% | 64,85 $ | 17/40 | +42,50% | +5,00% | 80,10 $ | 2/17 | +11,76% | +23,53% | DEBOLE | 13,1 | 15,5 |
| -15,00% | 64,85 $ | 17/40 | +42,50% | +10,00% | 83,92 $ | 1/17 | +5,88% | +29,41% | DEBOLE | 13,1 | 15,0 |
| -15,00% | 64,85 $ | 17/40 | +42,50% | +15,00% | 87,73 $ | 0/17 | 0,00% | +35,29% | DEBOLE | 13,1 | n/d |
| -15,00% | 64,85 $ | 17/40 | +42,50% | +20,00% | 91,55 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 13,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 80,10 $ | 24/40 | +60,00% | prezzo iniziale | 76,29 $ | 16/24 | +66,67% | -4,76% | ALTA | 5,6 | 10,2 |
| +5,00% | 80,10 $ | 24/40 | +60,00% | -5,00% | 72,48 $ | 14/24 | +58,33% | -9,52% | MEDIA | 5,6 | 11,2 |
| +5,00% | 80,10 $ | 24/40 | +60,00% | -8,00% | 70,19 $ | 14/24 | +58,33% | -12,38% | MEDIA | 5,6 | 14,1 |
| +5,00% | 80,10 $ | 24/40 | +60,00% | -10,00% | 68,66 $ | 12/24 | +50,00% | -14,29% | MEDIA | 5,6 | 16,3 |
| +5,00% | 80,10 $ | 24/40 | +60,00% | -15,00% | 64,85 $ | 7/24 | +29,17% | -19,05% | DEBOLE | 5,6 | 17,1 |
| +10,00% | 83,92 $ | 16/40 | +40,00% | prezzo iniziale | 76,29 $ | 7/16 | +43,75% | -9,09% | BASSA | 9,8 | 10,0 |
| +10,00% | 83,92 $ | 16/40 | +40,00% | -5,00% | 72,48 $ | 7/16 | +43,75% | -13,64% | BASSA | 9,8 | 11,0 |
| +10,00% | 83,92 $ | 16/40 | +40,00% | -8,00% | 70,19 $ | 7/16 | +43,75% | -16,36% | BASSA | 9,8 | 12,6 |
| +10,00% | 83,92 $ | 16/40 | +40,00% | -10,00% | 68,66 $ | 6/16 | +37,50% | -18,18% | BASSA | 9,8 | 13,0 |
| +10,00% | 83,92 $ | 16/40 | +40,00% | -15,00% | 64,85 $ | 4/16 | +25,00% | -22,73% | DEBOLE | 9,8 | 14,2 |
| +15,00% | 87,73 $ | 10/40 | +25,00% | prezzo iniziale | 76,29 $ | 1/10 | +10,00% | -13,04% | DEBOLE | 12,0 | 11,0 |
| +15,00% | 87,73 $ | 10/40 | +25,00% | -5,00% | 72,48 $ | 1/10 | +10,00% | -17,39% | DEBOLE | 12,0 | 12,0 |
| +15,00% | 87,73 $ | 10/40 | +25,00% | -8,00% | 70,19 $ | 1/10 | +10,00% | -20,00% | DEBOLE | 12,0 | 12,0 |
| +15,00% | 87,73 $ | 10/40 | +25,00% | -10,00% | 68,66 $ | 1/10 | +10,00% | -21,74% | DEBOLE | 12,0 | 12,0 |
| +15,00% | 87,73 $ | 10/40 | +25,00% | -15,00% | 64,85 $ | 1/10 | +10,00% | -26,09% | DEBOLE | 12,0 | 13,0 |
| +20,00% | 91,55 $ | 8/40 | +20,00% | prezzo iniziale | 76,29 $ | 1/8 | +12,50% | -16,67% | DEBOLE | 11,8 | 11,0 |
| +20,00% | 91,55 $ | 8/40 | +20,00% | -5,00% | 72,48 $ | 1/8 | +12,50% | -20,83% | DEBOLE | 11,8 | 12,0 |
| +20,00% | 91,55 $ | 8/40 | +20,00% | -8,00% | 70,19 $ | 1/8 | +12,50% | -23,33% | DEBOLE | 11,8 | 12,0 |
| +20,00% | 91,55 $ | 8/40 | +20,00% | -10,00% | 68,66 $ | 1/8 | +12,50% | -25,00% | DEBOLE | 11,8 | 12,0 |
| +20,00% | 91,55 $ | 8/40 | +20,00% | -15,00% | 64,85 $ | 1/8 | +12,50% | -29,17% | DEBOLE | 11,8 | 13,0 |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +13,89% (5/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 9 poi sono scaricati a -5,00%. Percentuale: +56,25% (9/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06853 $ | 36/40 | +90,00% | +5,00% | 0,07575 $ | 5/36 | +13,89% | +10,53% | DEBOLE | 6,1 | 13,0 |
| -5,00% | 0,06853 $ | 36/40 | +90,00% | +10,00% | 0,07935 $ | 5/36 | +13,89% | +15,79% | DEBOLE | 6,1 | 13,6 |
| -5,00% | 0,06853 $ | 36/40 | +90,00% | +15,00% | 0,08296 $ | 3/36 | +8,33% | +21,05% | DEBOLE | 6,1 | 12,7 |
| -5,00% | 0,06853 $ | 36/40 | +90,00% | +20,00% | 0,08657 $ | 3/36 | +8,33% | +26,32% | DEBOLE | 6,1 | 14,7 |
| -8,00% | 0,06637 $ | 35/40 | +87,50% | +5,00% | 0,07575 $ | 5/35 | +14,29% | +14,13% | DEBOLE | 7,7 | 13,0 |
| -8,00% | 0,06637 $ | 35/40 | +87,50% | +10,00% | 0,07935 $ | 5/35 | +14,29% | +19,57% | DEBOLE | 7,7 | 13,6 |
| -8,00% | 0,06637 $ | 35/40 | +87,50% | +15,00% | 0,08296 $ | 3/35 | +8,57% | +25,00% | DEBOLE | 7,7 | 12,7 |
| -8,00% | 0,06637 $ | 35/40 | +87,50% | +20,00% | 0,08657 $ | 3/35 | +8,57% | +30,43% | DEBOLE | 7,7 | 14,7 |
| -10,00% | 0,06493 $ | 32/40 | +80,00% | +5,00% | 0,07575 $ | 2/32 | +6,25% | +16,67% | DEBOLE | 9,0 | 18,0 |
| -10,00% | 0,06493 $ | 32/40 | +80,00% | +10,00% | 0,07935 $ | 2/32 | +6,25% | +22,22% | DEBOLE | 9,0 | 18,5 |
| -10,00% | 0,06493 $ | 32/40 | +80,00% | +15,00% | 0,08296 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 9,0 | n/d |
| -10,00% | 0,06493 $ | 32/40 | +80,00% | +20,00% | 0,08657 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 9,0 | n/d |
| -15,00% | 0,06132 $ | 29/40 | +72,50% | +5,00% | 0,07575 $ | 2/29 | +6,90% | +23,53% | DEBOLE | 8,8 | 18,0 |
| -15,00% | 0,06132 $ | 29/40 | +72,50% | +10,00% | 0,07935 $ | 2/29 | +6,90% | +29,41% | DEBOLE | 8,8 | 18,5 |
| -15,00% | 0,06132 $ | 29/40 | +72,50% | +15,00% | 0,08296 $ | 0/29 | 0,00% | +35,29% | DEBOLE | 8,8 | n/d |
| -15,00% | 0,06132 $ | 29/40 | +72,50% | +20,00% | 0,08657 $ | 0/29 | 0,00% | +41,18% | DEBOLE | 8,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07575 $ | 20/40 | +50,00% | prezzo iniziale | 0,07214 $ | 16/20 | +80,00% | -4,76% | ALTA | 3,7 | 7,9 |
| +5,00% | 0,07575 $ | 20/40 | +50,00% | -5,00% | 0,06853 $ | 14/20 | +70,00% | -9,52% | ALTA | 3,7 | 9,3 |
| +5,00% | 0,07575 $ | 20/40 | +50,00% | -8,00% | 0,06637 $ | 14/20 | +70,00% | -12,38% | ALTA | 3,7 | 9,9 |
| +5,00% | 0,07575 $ | 20/40 | +50,00% | -10,00% | 0,06493 $ | 13/20 | +65,00% | -14,29% | ALTA | 3,7 | 11,8 |
| +5,00% | 0,07575 $ | 20/40 | +50,00% | -15,00% | 0,06132 $ | 11/20 | +55,00% | -19,05% | MEDIA | 3,7 | 9,7 |
| +10,00% | 0,07935 $ | 16/40 | +40,00% | prezzo iniziale | 0,07214 $ | 12/16 | +75,00% | -9,09% | ALTA | 7,8 | 12,6 |
| +10,00% | 0,07935 $ | 16/40 | +40,00% | -5,00% | 0,06853 $ | 9/16 | +56,25% | -13,64% | MEDIA | 7,8 | 12,3 |
| +10,00% | 0,07935 $ | 16/40 | +40,00% | -8,00% | 0,06637 $ | 9/16 | +56,25% | -16,36% | MEDIA | 7,8 | 13,2 |
| +10,00% | 0,07935 $ | 16/40 | +40,00% | -10,00% | 0,06493 $ | 8/16 | +50,00% | -18,18% | MEDIA | 7,8 | 14,5 |
| +10,00% | 0,07935 $ | 16/40 | +40,00% | -15,00% | 0,06132 $ | 6/16 | +37,50% | -22,73% | BASSA | 7,8 | 12,0 |
| +15,00% | 0,08296 $ | 10/40 | +25,00% | prezzo iniziale | 0,07214 $ | 5/10 | +50,00% | -13,04% | MEDIA | 10,0 | 17,8 |
| +15,00% | 0,08296 $ | 10/40 | +25,00% | -5,00% | 0,06853 $ | 4/10 | +40,00% | -17,39% | BASSA | 10,0 | 18,0 |
| +15,00% | 0,08296 $ | 10/40 | +25,00% | -8,00% | 0,06637 $ | 3/10 | +30,00% | -20,00% | DEBOLE | 10,0 | 15,0 |
| +15,00% | 0,08296 $ | 10/40 | +25,00% | -10,00% | 0,06493 $ | 3/10 | +30,00% | -21,74% | DEBOLE | 10,0 | 15,3 |
| +15,00% | 0,08296 $ | 10/40 | +25,00% | -15,00% | 0,06132 $ | 3/10 | +30,00% | -26,09% | DEBOLE | 10,0 | 15,7 |
| +20,00% | 0,08657 $ | 7/40 | +17,50% | prezzo iniziale | 0,07214 $ | 3/7 | +42,86% | -16,67% | BASSA | 10,0 | 11,3 |
| +20,00% | 0,08657 $ | 7/40 | +17,50% | -5,00% | 0,06853 $ | 3/7 | +42,86% | -20,83% | BASSA | 10,0 | 15,3 |
| +20,00% | 0,08657 $ | 7/40 | +17,50% | -8,00% | 0,06637 $ | 2/7 | +28,57% | -23,33% | DEBOLE | 10,0 | 9,5 |
| +20,00% | 0,08657 $ | 7/40 | +17,50% | -10,00% | 0,06493 $ | 2/7 | +28,57% | -25,00% | DEBOLE | 10,0 | 10,0 |
| +20,00% | 0,08657 $ | 7/40 | +17,50% | -15,00% | 0,06132 $ | 2/7 | +28,57% | -29,17% | DEBOLE | 10,0 | 10,5 |

---
