# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-27 07:13:56 CEST**  
UTC: **2026-07-27 05:13:56 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.039 $ | 71.834 $ | +39,13% | +15,79% | rimbalzo debole | 71.834 $ | 62.039 $ | 0,00% | -13,64% | spike storicamente più resistente |
| SOL | 72,50 $ | 83,95 $ | +26,92% | +15,79% | rimbalzo poco frequente | 83,95 $ | 72,50 $ | +9,52% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06925 $ | 0,08018 $ | +36,00% | +15,79% | rimbalzo debole | 0,08018 $ | 0,06925 $ | +43,33% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 23 prima sono scesi a -5,00%. Tra quei 23, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +39,13% (9/23). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 62.039 $ | 23/40 | +57,50% | +5,00% | 68.569 $ | 10/23 | +43,48% | +10,53% | BASSA | 6,1 | 14,5 |
| -5,00% | 62.039 $ | 23/40 | +57,50% | +10,00% | 71.834 $ | 9/23 | +39,13% | +15,79% | BASSA | 6,1 | 19,9 |
| -5,00% | 62.039 $ | 23/40 | +57,50% | +15,00% | 75.099 $ | 9/23 | +39,13% | +21,05% | BASSA | 6,1 | 21,6 |
| -5,00% | 62.039 $ | 23/40 | +57,50% | +20,00% | 78.365 $ | 8/23 | +34,78% | +26,32% | DEBOLE | 6,1 | 23,5 |
| -8,00% | 60.079 $ | 18/40 | +45,00% | +5,00% | 68.569 $ | 6/18 | +33,33% | +14,13% | DEBOLE | 8,1 | 15,2 |
| -8,00% | 60.079 $ | 18/40 | +45,00% | +10,00% | 71.834 $ | 5/18 | +27,78% | +19,57% | DEBOLE | 8,1 | 21,8 |
| -8,00% | 60.079 $ | 18/40 | +45,00% | +15,00% | 75.099 $ | 5/18 | +27,78% | +25,00% | DEBOLE | 8,1 | 23,6 |
| -8,00% | 60.079 $ | 18/40 | +45,00% | +20,00% | 78.365 $ | 5/18 | +27,78% | +30,43% | DEBOLE | 8,1 | 27,2 |
| -10,00% | 58.773 $ | 15/40 | +37,50% | +5,00% | 68.569 $ | 3/15 | +20,00% | +16,67% | DEBOLE | 10,8 | 15,7 |
| -10,00% | 58.773 $ | 15/40 | +37,50% | +10,00% | 71.834 $ | 2/15 | +13,33% | +22,22% | DEBOLE | 10,8 | 26,5 |
| -10,00% | 58.773 $ | 15/40 | +37,50% | +15,00% | 75.099 $ | 2/15 | +13,33% | +27,78% | DEBOLE | 10,8 | 26,5 |
| -10,00% | 58.773 $ | 15/40 | +37,50% | +20,00% | 78.365 $ | 2/15 | +13,33% | +33,33% | DEBOLE | 10,8 | 29,5 |
| -15,00% | 55.508 $ | 11/40 | +27,50% | +5,00% | 68.569 $ | 1/11 | +9,09% | +23,53% | DEBOLE | 12,0 | 7,0 |
| -15,00% | 55.508 $ | 11/40 | +27,50% | +10,00% | 71.834 $ | 0/11 | 0,00% | +29,41% | DEBOLE | 12,0 | n/d |
| -15,00% | 55.508 $ | 11/40 | +27,50% | +15,00% | 75.099 $ | 0/11 | 0,00% | +35,29% | DEBOLE | 12,0 | n/d |
| -15,00% | 55.508 $ | 11/40 | +27,50% | +20,00% | 78.365 $ | 0/11 | 0,00% | +41,18% | DEBOLE | 12,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 68.569 $ | 30/40 | +75,00% | prezzo iniziale | 65.304 $ | 8/30 | +26,67% | -4,76% | DEBOLE | 10,2 | 11,1 |
| +5,00% | 68.569 $ | 30/40 | +75,00% | -5,00% | 62.039 $ | 5/30 | +16,67% | -9,52% | DEBOLE | 10,2 | 12,0 |
| +5,00% | 68.569 $ | 30/40 | +75,00% | -8,00% | 60.079 $ | 5/30 | +16,67% | -12,38% | DEBOLE | 10,2 | 16,2 |
| +5,00% | 68.569 $ | 30/40 | +75,00% | -10,00% | 58.773 $ | 4/30 | +13,33% | -14,29% | DEBOLE | 10,2 | 19,8 |
| +5,00% | 68.569 $ | 30/40 | +75,00% | -15,00% | 55.508 $ | 2/30 | +6,67% | -19,05% | DEBOLE | 10,2 | 20,5 |
| +10,00% | 71.834 $ | 23/40 | +57,50% | prezzo iniziale | 65.304 $ | 0/23 | 0,00% | -9,09% | DEBOLE | 16,0 | n/d |
| +10,00% | 71.834 $ | 23/40 | +57,50% | -5,00% | 62.039 $ | 0/23 | 0,00% | -13,64% | DEBOLE | 16,0 | n/d |
| +10,00% | 71.834 $ | 23/40 | +57,50% | -8,00% | 60.079 $ | 0/23 | 0,00% | -16,36% | DEBOLE | 16,0 | n/d |
| +10,00% | 71.834 $ | 23/40 | +57,50% | -10,00% | 58.773 $ | 0/23 | 0,00% | -18,18% | DEBOLE | 16,0 | n/d |
| +10,00% | 71.834 $ | 23/40 | +57,50% | -15,00% | 55.508 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 16,0 | n/d |
| +15,00% | 75.099 $ | 20/40 | +50,00% | prezzo iniziale | 65.304 $ | 0/20 | 0,00% | -13,04% | DEBOLE | 18,3 | n/d |
| +15,00% | 75.099 $ | 20/40 | +50,00% | -5,00% | 62.039 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 18,3 | n/d |
| +15,00% | 75.099 $ | 20/40 | +50,00% | -8,00% | 60.079 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 18,3 | n/d |
| +15,00% | 75.099 $ | 20/40 | +50,00% | -10,00% | 58.773 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 18,3 | n/d |
| +15,00% | 75.099 $ | 20/40 | +50,00% | -15,00% | 55.508 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 18,3 | n/d |
| +20,00% | 78.365 $ | 17/40 | +42,50% | prezzo iniziale | 65.304 $ | 0/17 | 0,00% | -16,67% | DEBOLE | 20,5 | n/d |
| +20,00% | 78.365 $ | 17/40 | +42,50% | -5,00% | 62.039 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 20,5 | n/d |
| +20,00% | 78.365 $ | 17/40 | +42,50% | -8,00% | 60.079 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 20,5 | n/d |
| +20,00% | 78.365 $ | 17/40 | +42,50% | -10,00% | 58.773 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 20,5 | n/d |
| +20,00% | 78.365 $ | 17/40 | +42,50% | -15,00% | 55.508 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 20,5 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +26,92% (7/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 2 poi sono scaricati a -5,00%. Percentuale: +9,52% (2/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,50 $ | 26/40 | +65,00% | +5,00% | 80,14 $ | 12/26 | +46,15% | +10,53% | BASSA | 8,5 | 18,8 |
| -5,00% | 72,50 $ | 26/40 | +65,00% | +10,00% | 83,95 $ | 7/26 | +26,92% | +15,79% | DEBOLE | 8,5 | 18,7 |
| -5,00% | 72,50 $ | 26/40 | +65,00% | +15,00% | 87,77 $ | 5/26 | +19,23% | +21,05% | DEBOLE | 8,5 | 19,2 |
| -5,00% | 72,50 $ | 26/40 | +65,00% | +20,00% | 91,58 $ | 5/26 | +19,23% | +26,32% | DEBOLE | 8,5 | 20,4 |
| -8,00% | 70,21 $ | 21/40 | +52,50% | +5,00% | 80,14 $ | 6/21 | +28,57% | +14,13% | DEBOLE | 12,0 | 22,3 |
| -8,00% | 70,21 $ | 21/40 | +52,50% | +10,00% | 83,95 $ | 4/21 | +19,05% | +19,57% | DEBOLE | 12,0 | 22,5 |
| -8,00% | 70,21 $ | 21/40 | +52,50% | +15,00% | 87,77 $ | 3/21 | +14,29% | +25,00% | DEBOLE | 12,0 | 25,3 |
| -8,00% | 70,21 $ | 21/40 | +52,50% | +20,00% | 91,58 $ | 3/21 | +14,29% | +30,43% | DEBOLE | 12,0 | 26,7 |
| -10,00% | 68,69 $ | 16/40 | +40,00% | +5,00% | 80,14 $ | 2/16 | +12,50% | +16,67% | DEBOLE | 15,2 | 22,5 |
| -10,00% | 68,69 $ | 16/40 | +40,00% | +10,00% | 83,95 $ | 1/16 | +6,25% | +22,22% | DEBOLE | 15,2 | 27,0 |
| -10,00% | 68,69 $ | 16/40 | +40,00% | +15,00% | 87,77 $ | 1/16 | +6,25% | +27,78% | DEBOLE | 15,2 | 28,0 |
| -10,00% | 68,69 $ | 16/40 | +40,00% | +20,00% | 91,58 $ | 1/16 | +6,25% | +33,33% | DEBOLE | 15,2 | 28,0 |
| -15,00% | 64,87 $ | 7/40 | +17,50% | +5,00% | 80,14 $ | 0/7 | 0,00% | +23,53% | DEBOLE | 19,3 | n/d |
| -15,00% | 64,87 $ | 7/40 | +17,50% | +10,00% | 83,95 $ | 0/7 | 0,00% | +29,41% | DEBOLE | 19,3 | n/d |
| -15,00% | 64,87 $ | 7/40 | +17,50% | +15,00% | 87,77 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 19,3 | n/d |
| -15,00% | 64,87 $ | 7/40 | +17,50% | +20,00% | 91,58 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 19,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 80,14 $ | 29/40 | +72,50% | prezzo iniziale | 76,32 $ | 9/29 | +31,03% | -4,76% | DEBOLE | 9,8 | 10,9 |
| +5,00% | 80,14 $ | 29/40 | +72,50% | -5,00% | 72,50 $ | 7/29 | +24,14% | -9,52% | DEBOLE | 9,8 | 13,1 |
| +5,00% | 80,14 $ | 29/40 | +72,50% | -8,00% | 70,21 $ | 6/29 | +20,69% | -12,38% | DEBOLE | 9,8 | 14,5 |
| +5,00% | 80,14 $ | 29/40 | +72,50% | -10,00% | 68,69 $ | 3/29 | +10,34% | -14,29% | DEBOLE | 9,8 | 19,3 |
| +5,00% | 80,14 $ | 29/40 | +72,50% | -15,00% | 64,87 $ | 2/29 | +6,90% | -19,05% | DEBOLE | 9,8 | 19,5 |
| +10,00% | 83,95 $ | 21/40 | +52,50% | prezzo iniziale | 76,32 $ | 2/21 | +9,52% | -9,09% | DEBOLE | 12,9 | 14,5 |
| +10,00% | 83,95 $ | 21/40 | +52,50% | -5,00% | 72,50 $ | 2/21 | +9,52% | -13,64% | DEBOLE | 12,9 | 17,0 |
| +10,00% | 83,95 $ | 21/40 | +52,50% | -8,00% | 70,21 $ | 1/21 | +4,76% | -16,36% | DEBOLE | 12,9 | 24,0 |
| +10,00% | 83,95 $ | 21/40 | +52,50% | -10,00% | 68,69 $ | 1/21 | +4,76% | -18,18% | DEBOLE | 12,9 | 24,0 |
| +10,00% | 83,95 $ | 21/40 | +52,50% | -15,00% | 64,87 $ | 0/21 | 0,00% | -22,73% | DEBOLE | 12,9 | n/d |
| +15,00% | 87,77 $ | 16/40 | +40,00% | prezzo iniziale | 76,32 $ | 1/16 | +6,25% | -13,04% | DEBOLE | 13,9 | 19,0 |
| +15,00% | 87,77 $ | 16/40 | +40,00% | -5,00% | 72,50 $ | 1/16 | +6,25% | -17,39% | DEBOLE | 13,9 | 23,0 |
| +15,00% | 87,77 $ | 16/40 | +40,00% | -8,00% | 70,21 $ | 1/16 | +6,25% | -20,00% | DEBOLE | 13,9 | 24,0 |
| +15,00% | 87,77 $ | 16/40 | +40,00% | -10,00% | 68,69 $ | 1/16 | +6,25% | -21,74% | DEBOLE | 13,9 | 24,0 |
| +15,00% | 87,77 $ | 16/40 | +40,00% | -15,00% | 64,87 $ | 0/16 | 0,00% | -26,09% | DEBOLE | 13,9 | n/d |
| +20,00% | 91,58 $ | 12/40 | +30,00% | prezzo iniziale | 76,32 $ | 1/12 | +8,33% | -16,67% | DEBOLE | 14,8 | 19,0 |
| +20,00% | 91,58 $ | 12/40 | +30,00% | -5,00% | 72,50 $ | 1/12 | +8,33% | -20,83% | DEBOLE | 14,8 | 23,0 |
| +20,00% | 91,58 $ | 12/40 | +30,00% | -8,00% | 70,21 $ | 1/12 | +8,33% | -23,33% | DEBOLE | 14,8 | 24,0 |
| +20,00% | 91,58 $ | 12/40 | +30,00% | -10,00% | 68,69 $ | 1/12 | +8,33% | -25,00% | DEBOLE | 14,8 | 24,0 |
| +20,00% | 91,58 $ | 12/40 | +30,00% | -15,00% | 64,87 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 14,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +36,00% (9/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 13 poi sono scaricati a -5,00%. Percentuale: +43,33% (13/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06925 $ | 25/40 | +62,50% | +5,00% | 0,07653 $ | 13/25 | +52,00% | +10,53% | MEDIA | 9,2 | 16,2 |
| -5,00% | 0,06925 $ | 25/40 | +62,50% | +10,00% | 0,08018 $ | 9/25 | +36,00% | +15,79% | BASSA | 9,2 | 16,2 |
| -5,00% | 0,06925 $ | 25/40 | +62,50% | +15,00% | 0,08382 $ | 5/25 | +20,00% | +21,05% | DEBOLE | 9,2 | 13,0 |
| -5,00% | 0,06925 $ | 25/40 | +62,50% | +20,00% | 0,08747 $ | 5/25 | +20,00% | +26,32% | DEBOLE | 9,2 | 16,2 |
| -8,00% | 0,06706 $ | 19/40 | +47,50% | +5,00% | 0,07653 $ | 7/19 | +36,84% | +14,13% | BASSA | 11,8 | 17,1 |
| -8,00% | 0,06706 $ | 19/40 | +47,50% | +10,00% | 0,08018 $ | 3/19 | +15,79% | +19,57% | DEBOLE | 11,8 | 14,7 |
| -8,00% | 0,06706 $ | 19/40 | +47,50% | +15,00% | 0,08382 $ | 2/19 | +10,53% | +25,00% | DEBOLE | 11,8 | 8,5 |
| -8,00% | 0,06706 $ | 19/40 | +47,50% | +20,00% | 0,08747 $ | 2/19 | +10,53% | +30,43% | DEBOLE | 11,8 | 15,5 |
| -10,00% | 0,06560 $ | 17/40 | +42,50% | +5,00% | 0,07653 $ | 6/17 | +35,29% | +16,67% | BASSA | 11,5 | 18,0 |
| -10,00% | 0,06560 $ | 17/40 | +42,50% | +10,00% | 0,08018 $ | 2/17 | +11,76% | +22,22% | DEBOLE | 11,5 | 8,0 |
| -10,00% | 0,06560 $ | 17/40 | +42,50% | +15,00% | 0,08382 $ | 2/17 | +11,76% | +27,78% | DEBOLE | 11,5 | 8,5 |
| -10,00% | 0,06560 $ | 17/40 | +42,50% | +20,00% | 0,08747 $ | 2/17 | +11,76% | +33,33% | DEBOLE | 11,5 | 15,5 |
| -15,00% | 0,06196 $ | 12/40 | +30,00% | +5,00% | 0,07653 $ | 1/12 | +8,33% | +23,53% | DEBOLE | 14,7 | 8,0 |
| -15,00% | 0,06196 $ | 12/40 | +30,00% | +10,00% | 0,08018 $ | 1/12 | +8,33% | +29,41% | DEBOLE | 14,7 | 9,0 |
| -15,00% | 0,06196 $ | 12/40 | +30,00% | +15,00% | 0,08382 $ | 1/12 | +8,33% | +35,29% | DEBOLE | 14,7 | 10,0 |
| -15,00% | 0,06196 $ | 12/40 | +30,00% | +20,00% | 0,08747 $ | 1/12 | +8,33% | +41,18% | DEBOLE | 14,7 | 24,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07653 $ | 36/40 | +90,00% | prezzo iniziale | 0,07289 $ | 27/36 | +75,00% | -4,76% | ALTA | 5,4 | 11,2 |
| +5,00% | 0,07653 $ | 36/40 | +90,00% | -5,00% | 0,06925 $ | 19/36 | +52,78% | -9,52% | MEDIA | 5,4 | 13,9 |
| +5,00% | 0,07653 $ | 36/40 | +90,00% | -8,00% | 0,06706 $ | 14/36 | +38,89% | -12,38% | BASSA | 5,4 | 15,4 |
| +5,00% | 0,07653 $ | 36/40 | +90,00% | -10,00% | 0,06560 $ | 12/36 | +33,33% | -14,29% | DEBOLE | 5,4 | 14,1 |
| +5,00% | 0,07653 $ | 36/40 | +90,00% | -15,00% | 0,06196 $ | 7/36 | +19,44% | -19,05% | DEBOLE | 5,4 | 16,0 |
| +10,00% | 0,08018 $ | 30/40 | +75,00% | prezzo iniziale | 0,07289 $ | 19/30 | +63,33% | -9,09% | MEDIA | 8,2 | 16,0 |
| +10,00% | 0,08018 $ | 30/40 | +75,00% | -5,00% | 0,06925 $ | 13/30 | +43,33% | -13,64% | BASSA | 8,2 | 17,3 |
| +10,00% | 0,08018 $ | 30/40 | +75,00% | -8,00% | 0,06706 $ | 8/30 | +26,67% | -16,36% | DEBOLE | 8,2 | 16,9 |
| +10,00% | 0,08018 $ | 30/40 | +75,00% | -10,00% | 0,06560 $ | 6/30 | +20,00% | -18,18% | DEBOLE | 8,2 | 14,5 |
| +10,00% | 0,08018 $ | 30/40 | +75,00% | -15,00% | 0,06196 $ | 5/30 | +16,67% | -22,73% | DEBOLE | 8,2 | 14,2 |
| +15,00% | 0,08382 $ | 22/40 | +55,00% | prezzo iniziale | 0,07289 $ | 11/22 | +50,00% | -13,04% | MEDIA | 9,0 | 18,3 |
| +15,00% | 0,08382 $ | 22/40 | +55,00% | -5,00% | 0,06925 $ | 6/22 | +27,27% | -17,39% | DEBOLE | 9,0 | 19,3 |
| +15,00% | 0,08382 $ | 22/40 | +55,00% | -8,00% | 0,06706 $ | 3/22 | +13,64% | -20,00% | DEBOLE | 9,0 | 18,0 |
| +15,00% | 0,08382 $ | 22/40 | +55,00% | -10,00% | 0,06560 $ | 2/22 | +9,09% | -21,74% | DEBOLE | 9,0 | 13,5 |
| +15,00% | 0,08382 $ | 22/40 | +55,00% | -15,00% | 0,06196 $ | 1/22 | +4,55% | -26,09% | DEBOLE | 9,0 | 11,0 |
| +20,00% | 0,08747 $ | 20/40 | +50,00% | prezzo iniziale | 0,07289 $ | 9/20 | +45,00% | -16,67% | BASSA | 11,5 | 20,9 |
| +20,00% | 0,08747 $ | 20/40 | +50,00% | -5,00% | 0,06925 $ | 3/20 | +15,00% | -20,83% | DEBOLE | 11,5 | 21,0 |
| +20,00% | 0,08747 $ | 20/40 | +50,00% | -8,00% | 0,06706 $ | 0/20 | 0,00% | -23,33% | DEBOLE | 11,5 | n/d |
| +20,00% | 0,08747 $ | 20/40 | +50,00% | -10,00% | 0,06560 $ | 0/20 | 0,00% | -25,00% | DEBOLE | 11,5 | n/d |
| +20,00% | 0,08747 $ | 20/40 | +50,00% | -15,00% | 0,06196 $ | 0/20 | 0,00% | -29,17% | DEBOLE | 11,5 | n/d |

---
