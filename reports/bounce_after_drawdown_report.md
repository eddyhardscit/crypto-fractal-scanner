# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-25 07:32:47 CET**  
UTC: **2026-10-25 06:32:47 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.495 $ | 88.573 $ | +40,00% | +15,79% | rimbalzo debole | 88.573 $ | 76.495 $ | +12,00% | -13,64% | spike storicamente più resistente |
| SOL | 96,67 $ | 111,94 $ | +46,88% | +15,79% | rimbalzo debole | 111,94 $ | 96,67 $ | +12,50% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07312 $ | 0,08467 $ | +50,00% | +15,79% | rimbalzo possibile | 0,08467 $ | 0,07312 $ | +11,54% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (10/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 3 poi sono scaricati a -5,00%. Percentuale: +12,00% (3/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 76.495 $ | 25/40 | +62,50% | +5,00% | 84.547 $ | 11/25 | +44,00% | +10,53% | BASSA | 6,8 | 16,7 |
| -5,00% | 76.495 $ | 25/40 | +62,50% | +10,00% | 88.573 $ | 10/25 | +40,00% | +15,79% | BASSA | 6,8 | 18,9 |
| -5,00% | 76.495 $ | 25/40 | +62,50% | +15,00% | 92.599 $ | 6/25 | +24,00% | +21,05% | DEBOLE | 6,8 | 20,2 |
| -5,00% | 76.495 $ | 25/40 | +62,50% | +20,00% | 96.626 $ | 1/25 | +4,00% | +26,32% | DEBOLE | 6,8 | 25,0 |
| -8,00% | 74.080 $ | 20/40 | +50,00% | +5,00% | 84.547 $ | 7/20 | +35,00% | +14,13% | BASSA | 7,0 | 18,4 |
| -8,00% | 74.080 $ | 20/40 | +50,00% | +10,00% | 88.573 $ | 5/20 | +25,00% | +19,57% | DEBOLE | 7,0 | 19,8 |
| -8,00% | 74.080 $ | 20/40 | +50,00% | +15,00% | 92.599 $ | 4/20 | +20,00% | +25,00% | DEBOLE | 7,0 | 21,2 |
| -8,00% | 74.080 $ | 20/40 | +50,00% | +20,00% | 96.626 $ | 1/20 | +5,00% | +30,43% | DEBOLE | 7,0 | 25,0 |
| -10,00% | 72.469 $ | 19/40 | +47,50% | +5,00% | 84.547 $ | 5/19 | +26,32% | +16,67% | DEBOLE | 9,3 | 21,8 |
| -10,00% | 72.469 $ | 19/40 | +47,50% | +10,00% | 88.573 $ | 4/19 | +21,05% | +22,22% | DEBOLE | 9,3 | 21,2 |
| -10,00% | 72.469 $ | 19/40 | +47,50% | +15,00% | 92.599 $ | 4/19 | +21,05% | +27,78% | DEBOLE | 9,3 | 21,2 |
| -10,00% | 72.469 $ | 19/40 | +47,50% | +20,00% | 96.626 $ | 1/19 | +5,26% | +33,33% | DEBOLE | 9,3 | 25,0 |
| -15,00% | 68.443 $ | 12/40 | +30,00% | +5,00% | 84.547 $ | 2/12 | +16,67% | +23,53% | DEBOLE | 15,6 | 24,0 |
| -15,00% | 68.443 $ | 12/40 | +30,00% | +10,00% | 88.573 $ | 1/12 | +8,33% | +29,41% | DEBOLE | 15,6 | 23,0 |
| -15,00% | 68.443 $ | 12/40 | +30,00% | +15,00% | 92.599 $ | 1/12 | +8,33% | +35,29% | DEBOLE | 15,6 | 23,0 |
| -15,00% | 68.443 $ | 12/40 | +30,00% | +20,00% | 96.626 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 15,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 84.547 $ | 29/40 | +72,50% | prezzo iniziale | 80.521 $ | 14/29 | +48,28% | -4,76% | BASSA | 8,6 | 14,3 |
| +5,00% | 84.547 $ | 29/40 | +72,50% | -5,00% | 76.495 $ | 8/29 | +27,59% | -9,52% | DEBOLE | 8,6 | 13,5 |
| +5,00% | 84.547 $ | 29/40 | +72,50% | -8,00% | 74.080 $ | 6/29 | +20,69% | -12,38% | DEBOLE | 8,6 | 13,2 |
| +5,00% | 84.547 $ | 29/40 | +72,50% | -10,00% | 72.469 $ | 6/29 | +20,69% | -14,29% | DEBOLE | 8,6 | 14,2 |
| +5,00% | 84.547 $ | 29/40 | +72,50% | -15,00% | 68.443 $ | 5/29 | +17,24% | -19,05% | DEBOLE | 8,6 | 20,4 |
| +10,00% | 88.573 $ | 25/40 | +62,50% | prezzo iniziale | 80.521 $ | 8/25 | +32,00% | -9,09% | DEBOLE | 13,4 | 20,2 |
| +10,00% | 88.573 $ | 25/40 | +62,50% | -5,00% | 76.495 $ | 3/25 | +12,00% | -13,64% | DEBOLE | 13,4 | 15,7 |
| +10,00% | 88.573 $ | 25/40 | +62,50% | -8,00% | 74.080 $ | 2/25 | +8,00% | -16,36% | DEBOLE | 13,4 | 16,5 |
| +10,00% | 88.573 $ | 25/40 | +62,50% | -10,00% | 72.469 $ | 2/25 | +8,00% | -18,18% | DEBOLE | 13,4 | 16,5 |
| +10,00% | 88.573 $ | 25/40 | +62,50% | -15,00% | 68.443 $ | 2/25 | +8,00% | -22,73% | DEBOLE | 13,4 | 17,5 |
| +15,00% | 92.599 $ | 19/40 | +47,50% | prezzo iniziale | 80.521 $ | 4/19 | +21,05% | -13,04% | DEBOLE | 15,5 | 24,2 |
| +15,00% | 92.599 $ | 19/40 | +47,50% | -5,00% | 76.495 $ | 1/19 | +5,26% | -17,39% | DEBOLE | 15,5 | 14,0 |
| +15,00% | 92.599 $ | 19/40 | +47,50% | -8,00% | 74.080 $ | 1/19 | +5,26% | -20,00% | DEBOLE | 15,5 | 20,0 |
| +15,00% | 92.599 $ | 19/40 | +47,50% | -10,00% | 72.469 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 15,5 | 20,0 |
| +15,00% | 92.599 $ | 19/40 | +47,50% | -15,00% | 68.443 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 15,5 | 22,0 |
| +20,00% | 96.626 $ | 13/40 | +32,50% | prezzo iniziale | 80.521 $ | 1/13 | +7,69% | -16,67% | DEBOLE | 17,1 | 28,0 |
| +20,00% | 96.626 $ | 13/40 | +32,50% | -5,00% | 76.495 $ | 0/13 | 0,00% | -20,83% | DEBOLE | 17,1 | n/d |
| +20,00% | 96.626 $ | 13/40 | +32,50% | -8,00% | 74.080 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 17,1 | n/d |
| +20,00% | 96.626 $ | 13/40 | +32,50% | -10,00% | 72.469 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 17,1 | n/d |
| +20,00% | 96.626 $ | 13/40 | +32,50% | -15,00% | 68.443 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 17,1 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +46,88% (15/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 3 poi sono scaricati a -5,00%. Percentuale: +12,50% (3/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 96,67 $ | 32/40 | +80,00% | +5,00% | 106,85 $ | 17/32 | +53,12% | +10,53% | MEDIA | 5,2 | 18,1 |
| -5,00% | 96,67 $ | 32/40 | +80,00% | +10,00% | 111,94 $ | 15/32 | +46,88% | +15,79% | BASSA | 5,2 | 18,7 |
| -5,00% | 96,67 $ | 32/40 | +80,00% | +15,00% | 117,02 $ | 10/32 | +31,25% | +21,05% | DEBOLE | 5,2 | 21,2 |
| -5,00% | 96,67 $ | 32/40 | +80,00% | +20,00% | 122,11 $ | 3/32 | +9,38% | +26,32% | DEBOLE | 5,2 | 27,0 |
| -8,00% | 93,62 $ | 25/40 | +62,50% | +5,00% | 106,85 $ | 10/25 | +40,00% | +14,13% | BASSA | 7,8 | 19,9 |
| -8,00% | 93,62 $ | 25/40 | +62,50% | +10,00% | 111,94 $ | 9/25 | +36,00% | +19,57% | BASSA | 7,8 | 19,9 |
| -8,00% | 93,62 $ | 25/40 | +62,50% | +15,00% | 117,02 $ | 8/25 | +32,00% | +25,00% | DEBOLE | 7,8 | 23,0 |
| -8,00% | 93,62 $ | 25/40 | +62,50% | +20,00% | 122,11 $ | 3/25 | +12,00% | +30,43% | DEBOLE | 7,8 | 27,0 |
| -10,00% | 91,58 $ | 22/40 | +55,00% | +5,00% | 106,85 $ | 8/22 | +36,36% | +16,67% | BASSA | 8,2 | 22,5 |
| -10,00% | 91,58 $ | 22/40 | +55,00% | +10,00% | 111,94 $ | 7/22 | +31,82% | +22,22% | DEBOLE | 8,2 | 22,9 |
| -10,00% | 91,58 $ | 22/40 | +55,00% | +15,00% | 117,02 $ | 7/22 | +31,82% | +27,78% | DEBOLE | 8,2 | 23,3 |
| -10,00% | 91,58 $ | 22/40 | +55,00% | +20,00% | 122,11 $ | 2/22 | +9,09% | +33,33% | DEBOLE | 8,2 | 27,5 |
| -15,00% | 86,50 $ | 12/40 | +30,00% | +5,00% | 106,85 $ | 3/12 | +25,00% | +23,53% | DEBOLE | 12,8 | 24,0 |
| -15,00% | 86,50 $ | 12/40 | +30,00% | +10,00% | 111,94 $ | 2/12 | +16,67% | +29,41% | DEBOLE | 12,8 | 24,0 |
| -15,00% | 86,50 $ | 12/40 | +30,00% | +15,00% | 117,02 $ | 2/12 | +16,67% | +35,29% | DEBOLE | 12,8 | 25,0 |
| -15,00% | 86,50 $ | 12/40 | +30,00% | +20,00% | 122,11 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 12,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 106,85 $ | 29/40 | +72,50% | prezzo iniziale | 101,76 $ | 18/29 | +62,07% | -4,76% | MEDIA | 11,1 | 18,5 |
| +5,00% | 106,85 $ | 29/40 | +72,50% | -5,00% | 96,67 $ | 9/29 | +31,03% | -9,52% | DEBOLE | 11,1 | 14,1 |
| +5,00% | 106,85 $ | 29/40 | +72,50% | -8,00% | 93,62 $ | 7/29 | +24,14% | -12,38% | DEBOLE | 11,1 | 11,0 |
| +5,00% | 106,85 $ | 29/40 | +72,50% | -10,00% | 91,58 $ | 7/29 | +24,14% | -14,29% | DEBOLE | 11,1 | 13,0 |
| +5,00% | 106,85 $ | 29/40 | +72,50% | -15,00% | 86,50 $ | 4/29 | +13,79% | -19,05% | DEBOLE | 11,1 | 20,0 |
| +10,00% | 111,94 $ | 24/40 | +60,00% | prezzo iniziale | 101,76 $ | 11/24 | +45,83% | -9,09% | BASSA | 15,2 | 21,9 |
| +10,00% | 111,94 $ | 24/40 | +60,00% | -5,00% | 96,67 $ | 3/24 | +12,50% | -13,64% | DEBOLE | 15,2 | 16,7 |
| +10,00% | 111,94 $ | 24/40 | +60,00% | -8,00% | 93,62 $ | 2/24 | +8,33% | -16,36% | DEBOLE | 15,2 | 11,5 |
| +10,00% | 111,94 $ | 24/40 | +60,00% | -10,00% | 91,58 $ | 2/24 | +8,33% | -18,18% | DEBOLE | 15,2 | 11,5 |
| +10,00% | 111,94 $ | 24/40 | +60,00% | -15,00% | 86,50 $ | 2/24 | +8,33% | -22,73% | DEBOLE | 15,2 | 19,5 |
| +15,00% | 117,02 $ | 18/40 | +45,00% | prezzo iniziale | 101,76 $ | 5/18 | +27,78% | -13,04% | DEBOLE | 17,4 | 25,4 |
| +15,00% | 117,02 $ | 18/40 | +45,00% | -5,00% | 96,67 $ | 0/18 | 0,00% | -17,39% | DEBOLE | 17,4 | n/d |
| +15,00% | 117,02 $ | 18/40 | +45,00% | -8,00% | 93,62 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 17,4 | n/d |
| +15,00% | 117,02 $ | 18/40 | +45,00% | -10,00% | 91,58 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 17,4 | n/d |
| +15,00% | 117,02 $ | 18/40 | +45,00% | -15,00% | 86,50 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 17,4 | n/d |
| +20,00% | 122,11 $ | 10/40 | +25,00% | prezzo iniziale | 101,76 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 19,1 | 28,0 |
| +20,00% | 122,11 $ | 10/40 | +25,00% | -5,00% | 96,67 $ | 0/10 | 0,00% | -20,83% | DEBOLE | 19,1 | n/d |
| +20,00% | 122,11 $ | 10/40 | +25,00% | -8,00% | 93,62 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 19,1 | n/d |
| +20,00% | 122,11 $ | 10/40 | +25,00% | -10,00% | 91,58 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 19,1 | n/d |
| +20,00% | 122,11 $ | 10/40 | +25,00% | -15,00% | 86,50 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 19,1 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (15/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 3 poi sono scaricati a -5,00%. Percentuale: +11,54% (3/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07312 $ | 30/40 | +75,00% | +5,00% | 0,08082 $ | 18/30 | +60,00% | +10,53% | MEDIA | 4,3 | 18,7 |
| -5,00% | 0,07312 $ | 30/40 | +75,00% | +10,00% | 0,08467 $ | 15/30 | +50,00% | +15,79% | MEDIA | 4,3 | 19,5 |
| -5,00% | 0,07312 $ | 30/40 | +75,00% | +15,00% | 0,08852 $ | 8/30 | +26,67% | +21,05% | DEBOLE | 4,3 | 19,1 |
| -5,00% | 0,07312 $ | 30/40 | +75,00% | +20,00% | 0,09236 $ | 4/30 | +13,33% | +26,32% | DEBOLE | 4,3 | 21,2 |
| -8,00% | 0,07081 $ | 23/40 | +57,50% | +5,00% | 0,08082 $ | 11/23 | +47,83% | +14,13% | BASSA | 7,6 | 22,8 |
| -8,00% | 0,07081 $ | 23/40 | +57,50% | +10,00% | 0,08467 $ | 8/23 | +34,78% | +19,57% | DEBOLE | 7,6 | 22,0 |
| -8,00% | 0,07081 $ | 23/40 | +57,50% | +15,00% | 0,08852 $ | 5/23 | +21,74% | +25,00% | DEBOLE | 7,6 | 22,8 |
| -8,00% | 0,07081 $ | 23/40 | +57,50% | +20,00% | 0,09236 $ | 3/23 | +13,04% | +30,43% | DEBOLE | 7,6 | 24,3 |
| -10,00% | 0,06927 $ | 17/40 | +42,50% | +5,00% | 0,08082 $ | 6/17 | +35,29% | +16,67% | BASSA | 7,8 | 24,2 |
| -10,00% | 0,06927 $ | 17/40 | +42,50% | +10,00% | 0,08467 $ | 4/17 | +23,53% | +22,22% | DEBOLE | 7,8 | 23,5 |
| -10,00% | 0,06927 $ | 17/40 | +42,50% | +15,00% | 0,08852 $ | 3/17 | +17,65% | +27,78% | DEBOLE | 7,8 | 23,3 |
| -10,00% | 0,06927 $ | 17/40 | +42,50% | +20,00% | 0,09236 $ | 2/17 | +11,76% | +33,33% | DEBOLE | 7,8 | 27,5 |
| -15,00% | 0,06542 $ | 8/40 | +20,00% | +5,00% | 0,08082 $ | 2/8 | +25,00% | +23,53% | DEBOLE | 6,4 | 27,5 |
| -15,00% | 0,06542 $ | 8/40 | +20,00% | +10,00% | 0,08467 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 6,4 | n/d |
| -15,00% | 0,06542 $ | 8/40 | +20,00% | +15,00% | 0,08852 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 6,4 | n/d |
| -15,00% | 0,06542 $ | 8/40 | +20,00% | +20,00% | 0,09236 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 6,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08082 $ | 29/40 | +72,50% | prezzo iniziale | 0,07697 $ | 15/29 | +51,72% | -4,76% | MEDIA | 12,8 | 21,7 |
| +5,00% | 0,08082 $ | 29/40 | +72,50% | -5,00% | 0,07312 $ | 6/29 | +20,69% | -9,52% | DEBOLE | 12,8 | 15,8 |
| +5,00% | 0,08082 $ | 29/40 | +72,50% | -8,00% | 0,07081 $ | 3/29 | +10,34% | -12,38% | DEBOLE | 12,8 | 18,7 |
| +5,00% | 0,08082 $ | 29/40 | +72,50% | -10,00% | 0,06927 $ | 3/29 | +10,34% | -14,29% | DEBOLE | 12,8 | 19,0 |
| +5,00% | 0,08082 $ | 29/40 | +72,50% | -15,00% | 0,06542 $ | 1/29 | +3,45% | -19,05% | DEBOLE | 12,8 | 13,0 |
| +10,00% | 0,08467 $ | 26/40 | +65,00% | prezzo iniziale | 0,07697 $ | 9/26 | +34,62% | -9,09% | DEBOLE | 16,3 | 26,8 |
| +10,00% | 0,08467 $ | 26/40 | +65,00% | -5,00% | 0,07312 $ | 3/26 | +11,54% | -13,64% | DEBOLE | 16,3 | 22,3 |
| +10,00% | 0,08467 $ | 26/40 | +65,00% | -8,00% | 0,07081 $ | 2/26 | +7,69% | -16,36% | DEBOLE | 16,3 | 20,5 |
| +10,00% | 0,08467 $ | 26/40 | +65,00% | -10,00% | 0,06927 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 16,3 | 20,5 |
| +10,00% | 0,08467 $ | 26/40 | +65,00% | -15,00% | 0,06542 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 16,3 | 13,0 |
| +15,00% | 0,08852 $ | 18/40 | +45,00% | prezzo iniziale | 0,07697 $ | 3/18 | +16,67% | -13,04% | DEBOLE | 16,9 | 29,0 |
| +15,00% | 0,08852 $ | 18/40 | +45,00% | -5,00% | 0,07312 $ | 0/18 | 0,00% | -17,39% | DEBOLE | 16,9 | n/d |
| +15,00% | 0,08852 $ | 18/40 | +45,00% | -8,00% | 0,07081 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 16,9 | n/d |
| +15,00% | 0,08852 $ | 18/40 | +45,00% | -10,00% | 0,06927 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 16,9 | n/d |
| +15,00% | 0,08852 $ | 18/40 | +45,00% | -15,00% | 0,06542 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 16,9 | n/d |
| +20,00% | 0,09236 $ | 14/40 | +35,00% | prezzo iniziale | 0,07697 $ | 1/14 | +7,14% | -16,67% | DEBOLE | 17,9 | 28,0 |
| +20,00% | 0,09236 $ | 14/40 | +35,00% | -5,00% | 0,07312 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 17,9 | n/d |
| +20,00% | 0,09236 $ | 14/40 | +35,00% | -8,00% | 0,07081 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 17,9 | n/d |
| +20,00% | 0,09236 $ | 14/40 | +35,00% | -10,00% | 0,06927 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 17,9 | n/d |
| +20,00% | 0,09236 $ | 14/40 | +35,00% | -15,00% | 0,06542 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 17,9 | n/d |

---
