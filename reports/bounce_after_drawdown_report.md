# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-20 07:32:48 CEST**  
UTC: **2026-10-20 05:32:48 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.787 $ | 90.069 $ | +36,00% | +15,79% | rimbalzo debole | 90.069 $ | 77.787 $ | +19,23% | -13,64% | spike storicamente più resistente |
| SOL | 99,38 $ | 115,07 $ | +33,33% | +15,79% | rimbalzo poco frequente | 115,07 $ | 99,38 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07542 $ | 0,08733 $ | +42,86% | +15,79% | rimbalzo debole | 0,08733 $ | 0,07542 $ | +3,57% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +36,00% (9/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 5 poi sono scaricati a -5,00%. Percentuale: +19,23% (5/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 77.787 $ | 25/40 | +62,50% | +5,00% | 85.975 $ | 12/25 | +48,00% | +10,53% | BASSA | 7,6 | 14,5 |
| -5,00% | 77.787 $ | 25/40 | +62,50% | +10,00% | 90.069 $ | 9/25 | +36,00% | +15,79% | BASSA | 7,6 | 18,6 |
| -5,00% | 77.787 $ | 25/40 | +62,50% | +15,00% | 94.163 $ | 6/25 | +24,00% | +21,05% | DEBOLE | 7,6 | 17,0 |
| -5,00% | 77.787 $ | 25/40 | +62,50% | +20,00% | 98.257 $ | 4/25 | +16,00% | +26,32% | DEBOLE | 7,6 | 14,5 |
| -8,00% | 75.331 $ | 20/40 | +50,00% | +5,00% | 85.975 $ | 8/20 | +40,00% | +14,13% | BASSA | 9,3 | 16,6 |
| -8,00% | 75.331 $ | 20/40 | +50,00% | +10,00% | 90.069 $ | 5/20 | +25,00% | +19,57% | DEBOLE | 9,3 | 19,0 |
| -8,00% | 75.331 $ | 20/40 | +50,00% | +15,00% | 94.163 $ | 2/20 | +10,00% | +25,00% | DEBOLE | 9,3 | 12,5 |
| -8,00% | 75.331 $ | 20/40 | +50,00% | +20,00% | 98.257 $ | 1/20 | +5,00% | +30,43% | DEBOLE | 9,3 | 10,0 |
| -10,00% | 73.693 $ | 15/40 | +37,50% | +5,00% | 85.975 $ | 4/15 | +26,67% | +16,67% | DEBOLE | 10,5 | 22,5 |
| -10,00% | 73.693 $ | 15/40 | +37,50% | +10,00% | 90.069 $ | 3/15 | +20,00% | +22,22% | DEBOLE | 10,5 | 22,7 |
| -10,00% | 73.693 $ | 15/40 | +37,50% | +15,00% | 94.163 $ | 1/15 | +6,67% | +27,78% | DEBOLE | 10,5 | 15,0 |
| -10,00% | 73.693 $ | 15/40 | +37,50% | +20,00% | 98.257 $ | 0/15 | 0,00% | +33,33% | DEBOLE | 10,5 | n/d |
| -15,00% | 69.599 $ | 11/40 | +27,50% | +5,00% | 85.975 $ | 2/11 | +18,18% | +23,53% | DEBOLE | 19,2 | 27,0 |
| -15,00% | 69.599 $ | 11/40 | +27,50% | +10,00% | 90.069 $ | 2/11 | +18,18% | +29,41% | DEBOLE | 19,2 | 27,0 |
| -15,00% | 69.599 $ | 11/40 | +27,50% | +15,00% | 94.163 $ | 0/11 | 0,00% | +35,29% | DEBOLE | 19,2 | n/d |
| -15,00% | 69.599 $ | 11/40 | +27,50% | +20,00% | 98.257 $ | 0/11 | 0,00% | +41,18% | DEBOLE | 19,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 85.975 $ | 31/40 | +77,50% | prezzo iniziale | 81.881 $ | 19/31 | +61,29% | -4,76% | MEDIA | 6,1 | 13,7 |
| +5,00% | 85.975 $ | 31/40 | +77,50% | -5,00% | 77.787 $ | 12/31 | +38,71% | -9,52% | BASSA | 6,1 | 14,4 |
| +5,00% | 85.975 $ | 31/40 | +77,50% | -8,00% | 75.331 $ | 8/31 | +25,81% | -12,38% | DEBOLE | 6,1 | 14,0 |
| +5,00% | 85.975 $ | 31/40 | +77,50% | -10,00% | 73.693 $ | 6/31 | +19,35% | -14,29% | DEBOLE | 6,1 | 14,7 |
| +5,00% | 85.975 $ | 31/40 | +77,50% | -15,00% | 69.599 $ | 3/31 | +9,68% | -19,05% | DEBOLE | 6,1 | 25,0 |
| +10,00% | 90.069 $ | 26/40 | +65,00% | prezzo iniziale | 81.881 $ | 11/26 | +42,31% | -9,09% | BASSA | 11,4 | 19,6 |
| +10,00% | 90.069 $ | 26/40 | +65,00% | -5,00% | 77.787 $ | 5/26 | +19,23% | -13,64% | DEBOLE | 11,4 | 23,0 |
| +10,00% | 90.069 $ | 26/40 | +65,00% | -8,00% | 75.331 $ | 2/26 | +7,69% | -16,36% | DEBOLE | 11,4 | 20,5 |
| +10,00% | 90.069 $ | 26/40 | +65,00% | -10,00% | 73.693 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 11,4 | 21,0 |
| +10,00% | 90.069 $ | 26/40 | +65,00% | -15,00% | 69.599 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 11,4 | 27,0 |
| +15,00% | 94.163 $ | 20/40 | +50,00% | prezzo iniziale | 81.881 $ | 4/20 | +20,00% | -13,04% | DEBOLE | 15,2 | 19,5 |
| +15,00% | 94.163 $ | 20/40 | +50,00% | -5,00% | 77.787 $ | 3/20 | +15,00% | -17,39% | DEBOLE | 15,2 | 26,0 |
| +15,00% | 94.163 $ | 20/40 | +50,00% | -8,00% | 75.331 $ | 1/20 | +5,00% | -20,00% | DEBOLE | 15,2 | 29,0 |
| +15,00% | 94.163 $ | 20/40 | +50,00% | -10,00% | 73.693 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 15,2 | 30,0 |
| +15,00% | 94.163 $ | 20/40 | +50,00% | -15,00% | 69.599 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 15,2 | n/d |
| +20,00% | 98.257 $ | 16/40 | +40,00% | prezzo iniziale | 81.881 $ | 1/16 | +6,25% | -16,67% | DEBOLE | 18,2 | 25,0 |
| +20,00% | 98.257 $ | 16/40 | +40,00% | -5,00% | 77.787 $ | 1/16 | +6,25% | -20,83% | DEBOLE | 18,2 | 27,0 |
| +20,00% | 98.257 $ | 16/40 | +40,00% | -8,00% | 75.331 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 18,2 | n/d |
| +20,00% | 98.257 $ | 16/40 | +40,00% | -10,00% | 73.693 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 18,2 | n/d |
| +20,00% | 98.257 $ | 16/40 | +40,00% | -15,00% | 69.599 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 18,2 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 24 prima sono scesi a -5,00%. Tra quei 24, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (8/24). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 99,38 $ | 24/40 | +60,00% | +5,00% | 109,84 $ | 11/24 | +45,83% | +10,53% | BASSA | 6,9 | 18,2 |
| -5,00% | 99,38 $ | 24/40 | +60,00% | +10,00% | 115,07 $ | 8/24 | +33,33% | +15,79% | DEBOLE | 6,9 | 23,1 |
| -5,00% | 99,38 $ | 24/40 | +60,00% | +15,00% | 120,30 $ | 3/24 | +12,50% | +21,05% | DEBOLE | 6,9 | 20,7 |
| -5,00% | 99,38 $ | 24/40 | +60,00% | +20,00% | 125,53 $ | 3/24 | +12,50% | +26,32% | DEBOLE | 6,9 | 20,7 |
| -8,00% | 96,24 $ | 22/40 | +55,00% | +5,00% | 109,84 $ | 9/22 | +40,91% | +14,13% | BASSA | 8,1 | 17,9 |
| -8,00% | 96,24 $ | 22/40 | +55,00% | +10,00% | 115,07 $ | 6/22 | +27,27% | +19,57% | DEBOLE | 8,1 | 22,8 |
| -8,00% | 96,24 $ | 22/40 | +55,00% | +15,00% | 120,30 $ | 2/22 | +9,09% | +25,00% | DEBOLE | 8,1 | 20,0 |
| -8,00% | 96,24 $ | 22/40 | +55,00% | +20,00% | 125,53 $ | 2/22 | +9,09% | +30,43% | DEBOLE | 8,1 | 20,0 |
| -10,00% | 94,15 $ | 17/40 | +42,50% | +5,00% | 109,84 $ | 5/17 | +29,41% | +16,67% | DEBOLE | 9,9 | 23,6 |
| -10,00% | 94,15 $ | 17/40 | +42,50% | +10,00% | 115,07 $ | 4/17 | +23,53% | +22,22% | DEBOLE | 9,9 | 27,5 |
| -10,00% | 94,15 $ | 17/40 | +42,50% | +15,00% | 120,30 $ | 1/17 | +5,88% | +27,78% | DEBOLE | 9,9 | 30,0 |
| -10,00% | 94,15 $ | 17/40 | +42,50% | +20,00% | 125,53 $ | 1/17 | +5,88% | +33,33% | DEBOLE | 9,9 | 30,0 |
| -15,00% | 88,92 $ | 12/40 | +30,00% | +5,00% | 109,84 $ | 2/12 | +16,67% | +23,53% | DEBOLE | 13,8 | 27,0 |
| -15,00% | 88,92 $ | 12/40 | +30,00% | +10,00% | 115,07 $ | 2/12 | +16,67% | +29,41% | DEBOLE | 13,8 | 27,0 |
| -15,00% | 88,92 $ | 12/40 | +30,00% | +15,00% | 120,30 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 13,8 | n/d |
| -15,00% | 88,92 $ | 12/40 | +30,00% | +20,00% | 125,53 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 13,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 109,84 $ | 30/40 | +75,00% | prezzo iniziale | 104,61 $ | 19/30 | +63,33% | -4,76% | MEDIA | 5,4 | 11,6 |
| +5,00% | 109,84 $ | 30/40 | +75,00% | -5,00% | 99,38 $ | 10/30 | +33,33% | -9,52% | DEBOLE | 5,4 | 13,4 |
| +5,00% | 109,84 $ | 30/40 | +75,00% | -8,00% | 96,24 $ | 7/30 | +23,33% | -12,38% | DEBOLE | 5,4 | 14,1 |
| +5,00% | 109,84 $ | 30/40 | +75,00% | -10,00% | 94,15 $ | 5/30 | +16,67% | -14,29% | DEBOLE | 5,4 | 15,2 |
| +5,00% | 109,84 $ | 30/40 | +75,00% | -15,00% | 88,92 $ | 4/30 | +13,33% | -19,05% | DEBOLE | 5,4 | 20,0 |
| +10,00% | 115,07 $ | 24/40 | +60,00% | prezzo iniziale | 104,61 $ | 5/24 | +20,83% | -9,09% | DEBOLE | 14,2 | 21,0 |
| +10,00% | 115,07 $ | 24/40 | +60,00% | -5,00% | 99,38 $ | 0/24 | 0,00% | -13,64% | DEBOLE | 14,2 | n/d |
| +10,00% | 115,07 $ | 24/40 | +60,00% | -8,00% | 96,24 $ | 0/24 | 0,00% | -16,36% | DEBOLE | 14,2 | n/d |
| +10,00% | 115,07 $ | 24/40 | +60,00% | -10,00% | 94,15 $ | 0/24 | 0,00% | -18,18% | DEBOLE | 14,2 | n/d |
| +10,00% | 115,07 $ | 24/40 | +60,00% | -15,00% | 88,92 $ | 0/24 | 0,00% | -22,73% | DEBOLE | 14,2 | n/d |
| +15,00% | 120,30 $ | 15/40 | +37,50% | prezzo iniziale | 104,61 $ | 1/15 | +6,67% | -13,04% | DEBOLE | 14,8 | 19,0 |
| +15,00% | 120,30 $ | 15/40 | +37,50% | -5,00% | 99,38 $ | 0/15 | 0,00% | -17,39% | DEBOLE | 14,8 | n/d |
| +15,00% | 120,30 $ | 15/40 | +37,50% | -8,00% | 96,24 $ | 0/15 | 0,00% | -20,00% | DEBOLE | 14,8 | n/d |
| +15,00% | 120,30 $ | 15/40 | +37,50% | -10,00% | 94,15 $ | 0/15 | 0,00% | -21,74% | DEBOLE | 14,8 | n/d |
| +15,00% | 120,30 $ | 15/40 | +37,50% | -15,00% | 88,92 $ | 0/15 | 0,00% | -26,09% | DEBOLE | 14,8 | n/d |
| +20,00% | 125,53 $ | 13/40 | +32,50% | prezzo iniziale | 104,61 $ | 0/13 | 0,00% | -16,67% | DEBOLE | 17,1 | n/d |
| +20,00% | 125,53 $ | 13/40 | +32,50% | -5,00% | 99,38 $ | 0/13 | 0,00% | -20,83% | DEBOLE | 17,1 | n/d |
| +20,00% | 125,53 $ | 13/40 | +32,50% | -8,00% | 96,24 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 17,1 | n/d |
| +20,00% | 125,53 $ | 13/40 | +32,50% | -10,00% | 94,15 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 17,1 | n/d |
| +20,00% | 125,53 $ | 13/40 | +32,50% | -15,00% | 88,92 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 17,1 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +42,86% (9/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 1 poi sono scaricati a -5,00%. Percentuale: +3,57% (1/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07542 $ | 21/40 | +52,50% | +5,00% | 0,08336 $ | 11/21 | +52,38% | +10,53% | MEDIA | 5,9 | 19,2 |
| -5,00% | 0,07542 $ | 21/40 | +52,50% | +10,00% | 0,08733 $ | 9/21 | +42,86% | +15,79% | BASSA | 5,9 | 22,7 |
| -5,00% | 0,07542 $ | 21/40 | +52,50% | +15,00% | 0,09130 $ | 7/21 | +33,33% | +21,05% | DEBOLE | 5,9 | 23,7 |
| -5,00% | 0,07542 $ | 21/40 | +52,50% | +20,00% | 0,09527 $ | 4/21 | +19,05% | +26,32% | DEBOLE | 5,9 | 21,2 |
| -8,00% | 0,07304 $ | 17/40 | +42,50% | +5,00% | 0,08336 $ | 7/17 | +41,18% | +14,13% | BASSA | 7,6 | 19,0 |
| -8,00% | 0,07304 $ | 17/40 | +42,50% | +10,00% | 0,08733 $ | 6/17 | +35,29% | +19,57% | BASSA | 7,6 | 21,0 |
| -8,00% | 0,07304 $ | 17/40 | +42,50% | +15,00% | 0,09130 $ | 4/17 | +23,53% | +25,00% | DEBOLE | 7,6 | 21,0 |
| -8,00% | 0,07304 $ | 17/40 | +42,50% | +20,00% | 0,09527 $ | 3/17 | +17,65% | +30,43% | DEBOLE | 7,6 | 21,0 |
| -10,00% | 0,07145 $ | 13/40 | +32,50% | +5,00% | 0,08336 $ | 3/13 | +23,08% | +16,67% | DEBOLE | 9,2 | 26,0 |
| -10,00% | 0,07145 $ | 13/40 | +32,50% | +10,00% | 0,08733 $ | 3/13 | +23,08% | +22,22% | DEBOLE | 9,2 | 26,0 |
| -10,00% | 0,07145 $ | 13/40 | +32,50% | +15,00% | 0,09130 $ | 2/13 | +15,38% | +27,78% | DEBOLE | 9,2 | 26,5 |
| -10,00% | 0,07145 $ | 13/40 | +32,50% | +20,00% | 0,09527 $ | 1/13 | +7,69% | +33,33% | DEBOLE | 9,2 | 30,0 |
| -15,00% | 0,06748 $ | 9/40 | +22,50% | +5,00% | 0,08336 $ | 2/9 | +22,22% | +23,53% | DEBOLE | 12,6 | 24,5 |
| -15,00% | 0,06748 $ | 9/40 | +22,50% | +10,00% | 0,08733 $ | 2/9 | +22,22% | +29,41% | DEBOLE | 12,6 | 24,5 |
| -15,00% | 0,06748 $ | 9/40 | +22,50% | +15,00% | 0,09130 $ | 1/9 | +11,11% | +35,29% | DEBOLE | 12,6 | 23,0 |
| -15,00% | 0,06748 $ | 9/40 | +22,50% | +20,00% | 0,09527 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 12,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08336 $ | 31/40 | +77,50% | prezzo iniziale | 0,07939 $ | 17/31 | +54,84% | -4,76% | MEDIA | 4,9 | 9,6 |
| +5,00% | 0,08336 $ | 31/40 | +77,50% | -5,00% | 0,07542 $ | 6/31 | +19,35% | -9,52% | DEBOLE | 4,9 | 11,3 |
| +5,00% | 0,08336 $ | 31/40 | +77,50% | -8,00% | 0,07304 $ | 3/31 | +9,68% | -12,38% | DEBOLE | 4,9 | 12,0 |
| +5,00% | 0,08336 $ | 31/40 | +77,50% | -10,00% | 0,07145 $ | 3/31 | +9,68% | -14,29% | DEBOLE | 4,9 | 16,0 |
| +5,00% | 0,08336 $ | 31/40 | +77,50% | -15,00% | 0,06748 $ | 2/31 | +6,45% | -19,05% | DEBOLE | 4,9 | 22,0 |
| +10,00% | 0,08733 $ | 28/40 | +70,00% | prezzo iniziale | 0,07939 $ | 6/28 | +21,43% | -9,09% | DEBOLE | 13,4 | 14,7 |
| +10,00% | 0,08733 $ | 28/40 | +70,00% | -5,00% | 0,07542 $ | 1/28 | +3,57% | -13,64% | DEBOLE | 13,4 | 10,0 |
| +10,00% | 0,08733 $ | 28/40 | +70,00% | -8,00% | 0,07304 $ | 1/28 | +3,57% | -16,36% | DEBOLE | 13,4 | 10,0 |
| +10,00% | 0,08733 $ | 28/40 | +70,00% | -10,00% | 0,07145 $ | 1/28 | +3,57% | -18,18% | DEBOLE | 13,4 | 10,0 |
| +10,00% | 0,08733 $ | 28/40 | +70,00% | -15,00% | 0,06748 $ | 1/28 | +3,57% | -22,73% | DEBOLE | 13,4 | 26,0 |
| +15,00% | 0,09130 $ | 21/40 | +52,50% | prezzo iniziale | 0,07939 $ | 1/21 | +4,76% | -13,04% | DEBOLE | 16,9 | 14,0 |
| +15,00% | 0,09130 $ | 21/40 | +52,50% | -5,00% | 0,07542 $ | 0/21 | 0,00% | -17,39% | DEBOLE | 16,9 | n/d |
| +15,00% | 0,09130 $ | 21/40 | +52,50% | -8,00% | 0,07304 $ | 0/21 | 0,00% | -20,00% | DEBOLE | 16,9 | n/d |
| +15,00% | 0,09130 $ | 21/40 | +52,50% | -10,00% | 0,07145 $ | 0/21 | 0,00% | -21,74% | DEBOLE | 16,9 | n/d |
| +15,00% | 0,09130 $ | 21/40 | +52,50% | -15,00% | 0,06748 $ | 0/21 | 0,00% | -26,09% | DEBOLE | 16,9 | n/d |
| +20,00% | 0,09527 $ | 15/40 | +37,50% | prezzo iniziale | 0,07939 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09527 $ | 15/40 | +37,50% | -5,00% | 0,07542 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09527 $ | 15/40 | +37,50% | -8,00% | 0,07304 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09527 $ | 15/40 | +37,50% | -10,00% | 0,07145 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09527 $ | 15/40 | +37,50% | -15,00% | 0,06748 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 17,2 | n/d |

---
