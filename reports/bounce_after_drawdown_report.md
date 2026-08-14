# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-14 12:51:56 CEST**  
UTC: **2026-08-14 10:51:56 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.622 $ | 69.036 $ | +42,86% | +15,79% | rimbalzo debole | 69.036 $ | 59.622 $ | +10,71% | -13,64% | spike storicamente più resistente |
| SOL | 71,60 $ | 82,91 $ | +26,67% | +15,79% | rimbalzo poco frequente | 82,91 $ | 71,60 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06586 $ | 0,07626 $ | +67,74% | +15,79% | buona zona storica di rimbalzo | 0,07626 $ | 0,06586 $ | +24,24% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +42,86% (6/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 3 poi sono scaricati a -5,00%. Percentuale: +10,71% (3/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.622 $ | 14/40 | +35,00% | +5,00% | 65.898 $ | 9/14 | +64,29% | +10,53% | MEDIA | 7,9 | 19,1 |
| -5,00% | 59.622 $ | 14/40 | +35,00% | +10,00% | 69.036 $ | 6/14 | +42,86% | +15,79% | BASSA | 7,9 | 18,3 |
| -5,00% | 59.622 $ | 14/40 | +35,00% | +15,00% | 72.174 $ | 5/14 | +35,71% | +21,05% | BASSA | 7,9 | 19,0 |
| -5,00% | 59.622 $ | 14/40 | +35,00% | +20,00% | 75.312 $ | 3/14 | +21,43% | +26,32% | DEBOLE | 7,9 | 17,3 |
| -8,00% | 57.739 $ | 9/40 | +22,50% | +5,00% | 65.898 $ | 5/9 | +55,56% | +14,13% | MEDIA | 9,8 | 20,8 |
| -8,00% | 57.739 $ | 9/40 | +22,50% | +10,00% | 69.036 $ | 4/9 | +44,44% | +19,57% | BASSA | 9,8 | 19,8 |
| -8,00% | 57.739 $ | 9/40 | +22,50% | +15,00% | 72.174 $ | 3/9 | +33,33% | +25,00% | DEBOLE | 9,8 | 20,7 |
| -8,00% | 57.739 $ | 9/40 | +22,50% | +20,00% | 75.312 $ | 2/9 | +22,22% | +30,43% | DEBOLE | 9,8 | 17,0 |
| -10,00% | 56.484 $ | 9/40 | +22,50% | +5,00% | 65.898 $ | 5/9 | +55,56% | +16,67% | MEDIA | 12,3 | 20,8 |
| -10,00% | 56.484 $ | 9/40 | +22,50% | +10,00% | 69.036 $ | 4/9 | +44,44% | +22,22% | BASSA | 12,3 | 19,8 |
| -10,00% | 56.484 $ | 9/40 | +22,50% | +15,00% | 72.174 $ | 3/9 | +33,33% | +27,78% | DEBOLE | 12,3 | 20,7 |
| -10,00% | 56.484 $ | 9/40 | +22,50% | +20,00% | 75.312 $ | 2/9 | +22,22% | +33,33% | DEBOLE | 12,3 | 17,0 |
| -15,00% | 53.346 $ | 6/40 | +15,00% | +5,00% | 65.898 $ | 2/6 | +33,33% | +23,53% | DEBOLE | 16,0 | 24,5 |
| -15,00% | 53.346 $ | 6/40 | +15,00% | +10,00% | 69.036 $ | 2/6 | +33,33% | +29,41% | DEBOLE | 16,0 | 25,0 |
| -15,00% | 53.346 $ | 6/40 | +15,00% | +15,00% | 72.174 $ | 1/6 | +16,67% | +35,29% | DEBOLE | 16,0 | 29,0 |
| -15,00% | 53.346 $ | 6/40 | +15,00% | +20,00% | 75.312 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 16,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.898 $ | 36/40 | +90,00% | prezzo iniziale | 62.760 $ | 11/36 | +30,56% | -4,76% | DEBOLE | 7,4 | 18,7 |
| +5,00% | 65.898 $ | 36/40 | +90,00% | -5,00% | 59.622 $ | 5/36 | +13,89% | -9,52% | DEBOLE | 7,4 | 20,2 |
| +5,00% | 65.898 $ | 36/40 | +90,00% | -8,00% | 57.739 $ | 4/36 | +11,11% | -12,38% | DEBOLE | 7,4 | 18,2 |
| +5,00% | 65.898 $ | 36/40 | +90,00% | -10,00% | 56.484 $ | 3/36 | +8,33% | -14,29% | DEBOLE | 7,4 | 19,0 |
| +5,00% | 65.898 $ | 36/40 | +90,00% | -15,00% | 53.346 $ | 2/36 | +5,56% | -19,05% | DEBOLE | 7,4 | 22,5 |
| +10,00% | 69.036 $ | 28/40 | +70,00% | prezzo iniziale | 62.760 $ | 4/28 | +14,29% | -9,09% | DEBOLE | 11,9 | 27,8 |
| +10,00% | 69.036 $ | 28/40 | +70,00% | -5,00% | 59.622 $ | 3/28 | +10,71% | -13,64% | DEBOLE | 11,9 | 28,0 |
| +10,00% | 69.036 $ | 28/40 | +70,00% | -8,00% | 57.739 $ | 2/28 | +7,14% | -16,36% | DEBOLE | 11,9 | 28,0 |
| +10,00% | 69.036 $ | 28/40 | +70,00% | -10,00% | 56.484 $ | 1/28 | +3,57% | -18,18% | DEBOLE | 11,9 | 28,0 |
| +10,00% | 69.036 $ | 28/40 | +70,00% | -15,00% | 53.346 $ | 1/28 | +3,57% | -22,73% | DEBOLE | 11,9 | 28,0 |
| +15,00% | 72.174 $ | 25/40 | +62,50% | prezzo iniziale | 62.760 $ | 3/25 | +12,00% | -13,04% | DEBOLE | 12,6 | 27,7 |
| +15,00% | 72.174 $ | 25/40 | +62,50% | -5,00% | 59.622 $ | 2/25 | +8,00% | -17,39% | DEBOLE | 12,6 | 27,0 |
| +15,00% | 72.174 $ | 25/40 | +62,50% | -8,00% | 57.739 $ | 2/25 | +8,00% | -20,00% | DEBOLE | 12,6 | 28,0 |
| +15,00% | 72.174 $ | 25/40 | +62,50% | -10,00% | 56.484 $ | 1/25 | +4,00% | -21,74% | DEBOLE | 12,6 | 28,0 |
| +15,00% | 72.174 $ | 25/40 | +62,50% | -15,00% | 53.346 $ | 1/25 | +4,00% | -26,09% | DEBOLE | 12,6 | 28,0 |
| +20,00% | 75.312 $ | 20/40 | +50,00% | prezzo iniziale | 62.760 $ | 2/20 | +10,00% | -16,67% | DEBOLE | 12,2 | 27,0 |
| +20,00% | 75.312 $ | 20/40 | +50,00% | -5,00% | 59.622 $ | 2/20 | +10,00% | -20,83% | DEBOLE | 12,2 | 27,0 |
| +20,00% | 75.312 $ | 20/40 | +50,00% | -8,00% | 57.739 $ | 2/20 | +10,00% | -23,33% | DEBOLE | 12,2 | 28,0 |
| +20,00% | 75.312 $ | 20/40 | +50,00% | -10,00% | 56.484 $ | 1/20 | +5,00% | -25,00% | DEBOLE | 12,2 | 28,0 |
| +20,00% | 75.312 $ | 20/40 | +50,00% | -15,00% | 53.346 $ | 1/20 | +5,00% | -29,17% | DEBOLE | 12,2 | 28,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +26,67% (4/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,60 $ | 15/40 | +37,50% | +5,00% | 79,14 $ | 8/15 | +53,33% | +10,53% | MEDIA | 10,3 | 17,1 |
| -5,00% | 71,60 $ | 15/40 | +37,50% | +10,00% | 82,91 $ | 4/15 | +26,67% | +15,79% | DEBOLE | 10,3 | 17,2 |
| -5,00% | 71,60 $ | 15/40 | +37,50% | +15,00% | 86,68 $ | 3/15 | +20,00% | +21,05% | DEBOLE | 10,3 | 20,3 |
| -5,00% | 71,60 $ | 15/40 | +37,50% | +20,00% | 90,44 $ | 2/15 | +13,33% | +26,32% | DEBOLE | 10,3 | 20,5 |
| -8,00% | 69,34 $ | 6/40 | +15,00% | +5,00% | 79,14 $ | 2/6 | +33,33% | +14,13% | DEBOLE | 14,5 | 18,0 |
| -8,00% | 69,34 $ | 6/40 | +15,00% | +10,00% | 82,91 $ | 1/6 | +16,67% | +19,57% | DEBOLE | 14,5 | 17,0 |
| -8,00% | 69,34 $ | 6/40 | +15,00% | +15,00% | 86,68 $ | 1/6 | +16,67% | +25,00% | DEBOLE | 14,5 | 18,0 |
| -8,00% | 69,34 $ | 6/40 | +15,00% | +20,00% | 90,44 $ | 1/6 | +16,67% | +30,43% | DEBOLE | 14,5 | 18,0 |
| -10,00% | 67,83 $ | 5/40 | +12,50% | +5,00% | 79,14 $ | 2/5 | +40,00% | +16,67% | BASSA | 14,6 | 18,0 |
| -10,00% | 67,83 $ | 5/40 | +12,50% | +10,00% | 82,91 $ | 1/5 | +20,00% | +22,22% | DEBOLE | 14,6 | 17,0 |
| -10,00% | 67,83 $ | 5/40 | +12,50% | +15,00% | 86,68 $ | 1/5 | +20,00% | +27,78% | DEBOLE | 14,6 | 18,0 |
| -10,00% | 67,83 $ | 5/40 | +12,50% | +20,00% | 90,44 $ | 1/5 | +20,00% | +33,33% | DEBOLE | 14,6 | 18,0 |
| -15,00% | 64,06 $ | 2/40 | +5,00% | +5,00% | 79,14 $ | 0/2 | 0,00% | +23,53% | DEBOLE | 15,0 | n/d |
| -15,00% | 64,06 $ | 2/40 | +5,00% | +10,00% | 82,91 $ | 0/2 | 0,00% | +29,41% | DEBOLE | 15,0 | n/d |
| -15,00% | 64,06 $ | 2/40 | +5,00% | +15,00% | 86,68 $ | 0/2 | 0,00% | +35,29% | DEBOLE | 15,0 | n/d |
| -15,00% | 64,06 $ | 2/40 | +5,00% | +20,00% | 90,44 $ | 0/2 | 0,00% | +41,18% | DEBOLE | 15,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,14 $ | 34/40 | +85,00% | prezzo iniziale | 75,37 $ | 9/34 | +26,47% | -4,76% | DEBOLE | 8,6 | 19,8 |
| +5,00% | 79,14 $ | 34/40 | +85,00% | -5,00% | 71,60 $ | 2/34 | +5,88% | -9,52% | DEBOLE | 8,6 | 23,5 |
| +5,00% | 79,14 $ | 34/40 | +85,00% | -8,00% | 69,34 $ | 0/34 | 0,00% | -12,38% | DEBOLE | 8,6 | n/d |
| +5,00% | 79,14 $ | 34/40 | +85,00% | -10,00% | 67,83 $ | 0/34 | 0,00% | -14,29% | DEBOLE | 8,6 | n/d |
| +5,00% | 79,14 $ | 34/40 | +85,00% | -15,00% | 64,06 $ | 0/34 | 0,00% | -19,05% | DEBOLE | 8,6 | n/d |
| +10,00% | 82,91 $ | 24/40 | +60,00% | prezzo iniziale | 75,37 $ | 3/24 | +12,50% | -9,09% | DEBOLE | 8,4 | 20,0 |
| +10,00% | 82,91 $ | 24/40 | +60,00% | -5,00% | 71,60 $ | 0/24 | 0,00% | -13,64% | DEBOLE | 8,4 | n/d |
| +10,00% | 82,91 $ | 24/40 | +60,00% | -8,00% | 69,34 $ | 0/24 | 0,00% | -16,36% | DEBOLE | 8,4 | n/d |
| +10,00% | 82,91 $ | 24/40 | +60,00% | -10,00% | 67,83 $ | 0/24 | 0,00% | -18,18% | DEBOLE | 8,4 | n/d |
| +10,00% | 82,91 $ | 24/40 | +60,00% | -15,00% | 64,06 $ | 0/24 | 0,00% | -22,73% | DEBOLE | 8,4 | n/d |
| +15,00% | 86,68 $ | 20/40 | +50,00% | prezzo iniziale | 75,37 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 10,2 | 25,0 |
| +15,00% | 86,68 $ | 20/40 | +50,00% | -5,00% | 71,60 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 10,2 | n/d |
| +15,00% | 86,68 $ | 20/40 | +50,00% | -8,00% | 69,34 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 10,2 | n/d |
| +15,00% | 86,68 $ | 20/40 | +50,00% | -10,00% | 67,83 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 10,2 | n/d |
| +15,00% | 86,68 $ | 20/40 | +50,00% | -15,00% | 64,06 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 10,2 | n/d |
| +20,00% | 90,44 $ | 17/40 | +42,50% | prezzo iniziale | 75,37 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 10,4 | 25,0 |
| +20,00% | 90,44 $ | 17/40 | +42,50% | -5,00% | 71,60 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,44 $ | 17/40 | +42,50% | -8,00% | 69,34 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,44 $ | 17/40 | +42,50% | -10,00% | 67,83 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,44 $ | 17/40 | +42,50% | -15,00% | 64,06 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 10,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 21 poi sono rimbalzati fino a +10,00%. Percentuale: +67,74% (21/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.
- DOGE: su 40 casi simili, 33 prima sono saliti a +10,00%. Tra quei 33, 8 poi sono scaricati a -5,00%. Percentuale: +24,24% (8/33). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06586 $ | 31/40 | +77,50% | +5,00% | 0,07280 $ | 21/31 | +67,74% | +10,53% | ALTA | 7,1 | 12,5 |
| -5,00% | 0,06586 $ | 31/40 | +77,50% | +10,00% | 0,07626 $ | 21/31 | +67,74% | +15,79% | ALTA | 7,1 | 15,4 |
| -5,00% | 0,06586 $ | 31/40 | +77,50% | +15,00% | 0,07973 $ | 17/31 | +54,84% | +21,05% | MEDIA | 7,1 | 18,3 |
| -5,00% | 0,06586 $ | 31/40 | +77,50% | +20,00% | 0,08320 $ | 15/31 | +48,39% | +26,32% | BASSA | 7,1 | 19,8 |
| -8,00% | 0,06378 $ | 23/40 | +57,50% | +5,00% | 0,07280 $ | 14/23 | +60,87% | +14,13% | MEDIA | 7,6 | 13,5 |
| -8,00% | 0,06378 $ | 23/40 | +57,50% | +10,00% | 0,07626 $ | 14/23 | +60,87% | +19,57% | MEDIA | 7,6 | 16,7 |
| -8,00% | 0,06378 $ | 23/40 | +57,50% | +15,00% | 0,07973 $ | 10/23 | +43,48% | +25,00% | BASSA | 7,6 | 19,5 |
| -8,00% | 0,06378 $ | 23/40 | +57,50% | +20,00% | 0,08320 $ | 9/23 | +39,13% | +30,43% | BASSA | 7,6 | 21,7 |
| -10,00% | 0,06240 $ | 18/40 | +45,00% | +5,00% | 0,07280 $ | 9/18 | +50,00% | +16,67% | MEDIA | 8,2 | 14,0 |
| -10,00% | 0,06240 $ | 18/40 | +45,00% | +10,00% | 0,07626 $ | 9/18 | +50,00% | +22,22% | MEDIA | 8,2 | 17,8 |
| -10,00% | 0,06240 $ | 18/40 | +45,00% | +15,00% | 0,07973 $ | 6/18 | +33,33% | +27,78% | DEBOLE | 8,2 | 17,5 |
| -10,00% | 0,06240 $ | 18/40 | +45,00% | +20,00% | 0,08320 $ | 6/18 | +33,33% | +33,33% | DEBOLE | 8,2 | 20,8 |
| -15,00% | 0,05893 $ | 9/40 | +22,50% | +5,00% | 0,07280 $ | 1/9 | +11,11% | +23,53% | DEBOLE | 10,2 | 9,0 |
| -15,00% | 0,05893 $ | 9/40 | +22,50% | +10,00% | 0,07626 $ | 1/9 | +11,11% | +29,41% | DEBOLE | 10,2 | 10,0 |
| -15,00% | 0,05893 $ | 9/40 | +22,50% | +15,00% | 0,07973 $ | 1/9 | +11,11% | +35,29% | DEBOLE | 10,2 | 10,0 |
| -15,00% | 0,05893 $ | 9/40 | +22,50% | +20,00% | 0,08320 $ | 1/9 | +11,11% | +41,18% | DEBOLE | 10,2 | 27,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07280 $ | 34/40 | +85,00% | prezzo iniziale | 0,06933 $ | 25/34 | +73,53% | -4,76% | ALTA | 6,9 | 13,9 |
| +5,00% | 0,07280 $ | 34/40 | +85,00% | -5,00% | 0,06586 $ | 15/34 | +44,12% | -9,52% | BASSA | 6,9 | 14,1 |
| +5,00% | 0,07280 $ | 34/40 | +85,00% | -8,00% | 0,06378 $ | 10/34 | +29,41% | -12,38% | DEBOLE | 6,9 | 12,7 |
| +5,00% | 0,07280 $ | 34/40 | +85,00% | -10,00% | 0,06240 $ | 7/34 | +20,59% | -14,29% | DEBOLE | 6,9 | 13,4 |
| +5,00% | 0,07280 $ | 34/40 | +85,00% | -15,00% | 0,05893 $ | 2/34 | +5,88% | -19,05% | DEBOLE | 6,9 | 24,0 |
| +10,00% | 0,07626 $ | 33/40 | +82,50% | prezzo iniziale | 0,06933 $ | 17/33 | +51,52% | -9,09% | MEDIA | 11,7 | 18,1 |
| +10,00% | 0,07626 $ | 33/40 | +82,50% | -5,00% | 0,06586 $ | 8/33 | +24,24% | -13,64% | DEBOLE | 11,7 | 18,1 |
| +10,00% | 0,07626 $ | 33/40 | +82,50% | -8,00% | 0,06378 $ | 4/33 | +12,12% | -16,36% | DEBOLE | 11,7 | 16,2 |
| +10,00% | 0,07626 $ | 33/40 | +82,50% | -10,00% | 0,06240 $ | 2/33 | +6,06% | -18,18% | DEBOLE | 11,7 | 19,5 |
| +10,00% | 0,07626 $ | 33/40 | +82,50% | -15,00% | 0,05893 $ | 1/33 | +3,03% | -22,73% | DEBOLE | 11,7 | 25,0 |
| +15,00% | 0,07973 $ | 26/40 | +65,00% | prezzo iniziale | 0,06933 $ | 4/26 | +15,38% | -13,04% | DEBOLE | 15,9 | 19,2 |
| +15,00% | 0,07973 $ | 26/40 | +65,00% | -5,00% | 0,06586 $ | 2/26 | +7,69% | -17,39% | DEBOLE | 15,9 | 17,0 |
| +15,00% | 0,07973 $ | 26/40 | +65,00% | -8,00% | 0,06378 $ | 1/26 | +3,85% | -20,00% | DEBOLE | 15,9 | 27,0 |
| +15,00% | 0,07973 $ | 26/40 | +65,00% | -10,00% | 0,06240 $ | 1/26 | +3,85% | -21,74% | DEBOLE | 15,9 | 28,0 |
| +15,00% | 0,07973 $ | 26/40 | +65,00% | -15,00% | 0,05893 $ | 0/26 | 0,00% | -26,09% | DEBOLE | 15,9 | n/d |
| +20,00% | 0,08320 $ | 24/40 | +60,00% | prezzo iniziale | 0,06933 $ | 1/24 | +4,17% | -16,67% | DEBOLE | 18,6 | 30,0 |
| +20,00% | 0,08320 $ | 24/40 | +60,00% | -5,00% | 0,06586 $ | 0/24 | 0,00% | -20,83% | DEBOLE | 18,6 | n/d |
| +20,00% | 0,08320 $ | 24/40 | +60,00% | -8,00% | 0,06378 $ | 0/24 | 0,00% | -23,33% | DEBOLE | 18,6 | n/d |
| +20,00% | 0,08320 $ | 24/40 | +60,00% | -10,00% | 0,06240 $ | 0/24 | 0,00% | -25,00% | DEBOLE | 18,6 | n/d |
| +20,00% | 0,08320 $ | 24/40 | +60,00% | -15,00% | 0,05893 $ | 0/24 | 0,00% | -29,17% | DEBOLE | 18,6 | n/d |

---
