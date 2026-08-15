# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-15 07:32:56 CEST**  
UTC: **2026-08-15 05:32:56 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.898 $ | 69.356 $ | +40,00% | +15,79% | rimbalzo debole | 69.356 $ | 59.898 $ | +10,71% | -13,64% | spike storicamente più resistente |
| SOL | 71,62 $ | 82,93 $ | +26,67% | +15,79% | rimbalzo poco frequente | 82,93 $ | 71,62 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06663 $ | 0,07715 $ | +62,50% | +15,79% | rimbalzo possibile | 0,07715 $ | 0,06663 $ | +22,58% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (6/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 3 poi sono scaricati a -5,00%. Percentuale: +10,71% (3/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.898 $ | 15/40 | +37,50% | +5,00% | 66.203 $ | 10/15 | +66,67% | +10,53% | ALTA | 7,5 | 18,5 |
| -5,00% | 59.898 $ | 15/40 | +37,50% | +10,00% | 69.356 $ | 6/15 | +40,00% | +15,79% | BASSA | 7,5 | 18,3 |
| -5,00% | 59.898 $ | 15/40 | +37,50% | +15,00% | 72.508 $ | 5/15 | +33,33% | +21,05% | DEBOLE | 7,5 | 19,0 |
| -5,00% | 59.898 $ | 15/40 | +37,50% | +20,00% | 75.661 $ | 3/15 | +20,00% | +26,32% | DEBOLE | 7,5 | 17,3 |
| -8,00% | 58.007 $ | 9/40 | +22,50% | +5,00% | 66.203 $ | 5/9 | +55,56% | +14,13% | MEDIA | 9,8 | 20,8 |
| -8,00% | 58.007 $ | 9/40 | +22,50% | +10,00% | 69.356 $ | 4/9 | +44,44% | +19,57% | BASSA | 9,8 | 19,8 |
| -8,00% | 58.007 $ | 9/40 | +22,50% | +15,00% | 72.508 $ | 3/9 | +33,33% | +25,00% | DEBOLE | 9,8 | 20,7 |
| -8,00% | 58.007 $ | 9/40 | +22,50% | +20,00% | 75.661 $ | 2/9 | +22,22% | +30,43% | DEBOLE | 9,8 | 17,0 |
| -10,00% | 56.746 $ | 9/40 | +22,50% | +5,00% | 66.203 $ | 5/9 | +55,56% | +16,67% | MEDIA | 12,3 | 20,8 |
| -10,00% | 56.746 $ | 9/40 | +22,50% | +10,00% | 69.356 $ | 4/9 | +44,44% | +22,22% | BASSA | 12,3 | 19,8 |
| -10,00% | 56.746 $ | 9/40 | +22,50% | +15,00% | 72.508 $ | 3/9 | +33,33% | +27,78% | DEBOLE | 12,3 | 20,7 |
| -10,00% | 56.746 $ | 9/40 | +22,50% | +20,00% | 75.661 $ | 2/9 | +22,22% | +33,33% | DEBOLE | 12,3 | 17,0 |
| -15,00% | 53.593 $ | 6/40 | +15,00% | +5,00% | 66.203 $ | 2/6 | +33,33% | +23,53% | DEBOLE | 16,0 | 24,5 |
| -15,00% | 53.593 $ | 6/40 | +15,00% | +10,00% | 69.356 $ | 2/6 | +33,33% | +29,41% | DEBOLE | 16,0 | 25,0 |
| -15,00% | 53.593 $ | 6/40 | +15,00% | +15,00% | 72.508 $ | 1/6 | +16,67% | +35,29% | DEBOLE | 16,0 | 29,0 |
| -15,00% | 53.593 $ | 6/40 | +15,00% | +20,00% | 75.661 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 16,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.203 $ | 36/40 | +90,00% | prezzo iniziale | 63.051 $ | 12/36 | +33,33% | -4,76% | DEBOLE | 8,1 | 19,4 |
| +5,00% | 66.203 $ | 36/40 | +90,00% | -5,00% | 59.898 $ | 5/36 | +13,89% | -9,52% | DEBOLE | 8,1 | 20,2 |
| +5,00% | 66.203 $ | 36/40 | +90,00% | -8,00% | 58.007 $ | 4/36 | +11,11% | -12,38% | DEBOLE | 8,1 | 18,2 |
| +5,00% | 66.203 $ | 36/40 | +90,00% | -10,00% | 56.746 $ | 3/36 | +8,33% | -14,29% | DEBOLE | 8,1 | 19,0 |
| +5,00% | 66.203 $ | 36/40 | +90,00% | -15,00% | 53.593 $ | 2/36 | +5,56% | -19,05% | DEBOLE | 8,1 | 22,5 |
| +10,00% | 69.356 $ | 28/40 | +70,00% | prezzo iniziale | 63.051 $ | 4/28 | +14,29% | -9,09% | DEBOLE | 12,9 | 27,8 |
| +10,00% | 69.356 $ | 28/40 | +70,00% | -5,00% | 59.898 $ | 3/28 | +10,71% | -13,64% | DEBOLE | 12,9 | 28,0 |
| +10,00% | 69.356 $ | 28/40 | +70,00% | -8,00% | 58.007 $ | 2/28 | +7,14% | -16,36% | DEBOLE | 12,9 | 28,0 |
| +10,00% | 69.356 $ | 28/40 | +70,00% | -10,00% | 56.746 $ | 1/28 | +3,57% | -18,18% | DEBOLE | 12,9 | 28,0 |
| +10,00% | 69.356 $ | 28/40 | +70,00% | -15,00% | 53.593 $ | 1/28 | +3,57% | -22,73% | DEBOLE | 12,9 | 28,0 |
| +15,00% | 72.508 $ | 24/40 | +60,00% | prezzo iniziale | 63.051 $ | 3/24 | +12,50% | -13,04% | DEBOLE | 12,6 | 27,7 |
| +15,00% | 72.508 $ | 24/40 | +60,00% | -5,00% | 59.898 $ | 2/24 | +8,33% | -17,39% | DEBOLE | 12,6 | 27,0 |
| +15,00% | 72.508 $ | 24/40 | +60,00% | -8,00% | 58.007 $ | 2/24 | +8,33% | -20,00% | DEBOLE | 12,6 | 28,0 |
| +15,00% | 72.508 $ | 24/40 | +60,00% | -10,00% | 56.746 $ | 1/24 | +4,17% | -21,74% | DEBOLE | 12,6 | 28,0 |
| +15,00% | 72.508 $ | 24/40 | +60,00% | -15,00% | 53.593 $ | 1/24 | +4,17% | -26,09% | DEBOLE | 12,6 | 28,0 |
| +20,00% | 75.661 $ | 19/40 | +47,50% | prezzo iniziale | 63.051 $ | 2/19 | +10,53% | -16,67% | DEBOLE | 11,4 | 27,0 |
| +20,00% | 75.661 $ | 19/40 | +47,50% | -5,00% | 59.898 $ | 2/19 | +10,53% | -20,83% | DEBOLE | 11,4 | 27,0 |
| +20,00% | 75.661 $ | 19/40 | +47,50% | -8,00% | 58.007 $ | 2/19 | +10,53% | -23,33% | DEBOLE | 11,4 | 28,0 |
| +20,00% | 75.661 $ | 19/40 | +47,50% | -10,00% | 56.746 $ | 1/19 | +5,26% | -25,00% | DEBOLE | 11,4 | 28,0 |
| +20,00% | 75.661 $ | 19/40 | +47,50% | -15,00% | 53.593 $ | 1/19 | +5,26% | -29,17% | DEBOLE | 11,4 | 28,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +26,67% (4/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,62 $ | 15/40 | +37,50% | +5,00% | 79,16 $ | 8/15 | +53,33% | +10,53% | MEDIA | 10,3 | 17,1 |
| -5,00% | 71,62 $ | 15/40 | +37,50% | +10,00% | 82,93 $ | 4/15 | +26,67% | +15,79% | DEBOLE | 10,3 | 17,2 |
| -5,00% | 71,62 $ | 15/40 | +37,50% | +15,00% | 86,70 $ | 3/15 | +20,00% | +21,05% | DEBOLE | 10,3 | 20,3 |
| -5,00% | 71,62 $ | 15/40 | +37,50% | +20,00% | 90,47 $ | 2/15 | +13,33% | +26,32% | DEBOLE | 10,3 | 20,5 |
| -8,00% | 69,36 $ | 6/40 | +15,00% | +5,00% | 79,16 $ | 2/6 | +33,33% | +14,13% | DEBOLE | 14,5 | 18,0 |
| -8,00% | 69,36 $ | 6/40 | +15,00% | +10,00% | 82,93 $ | 1/6 | +16,67% | +19,57% | DEBOLE | 14,5 | 17,0 |
| -8,00% | 69,36 $ | 6/40 | +15,00% | +15,00% | 86,70 $ | 1/6 | +16,67% | +25,00% | DEBOLE | 14,5 | 18,0 |
| -8,00% | 69,36 $ | 6/40 | +15,00% | +20,00% | 90,47 $ | 1/6 | +16,67% | +30,43% | DEBOLE | 14,5 | 18,0 |
| -10,00% | 67,85 $ | 5/40 | +12,50% | +5,00% | 79,16 $ | 2/5 | +40,00% | +16,67% | BASSA | 14,6 | 18,0 |
| -10,00% | 67,85 $ | 5/40 | +12,50% | +10,00% | 82,93 $ | 1/5 | +20,00% | +22,22% | DEBOLE | 14,6 | 17,0 |
| -10,00% | 67,85 $ | 5/40 | +12,50% | +15,00% | 86,70 $ | 1/5 | +20,00% | +27,78% | DEBOLE | 14,6 | 18,0 |
| -10,00% | 67,85 $ | 5/40 | +12,50% | +20,00% | 90,47 $ | 1/5 | +20,00% | +33,33% | DEBOLE | 14,6 | 18,0 |
| -15,00% | 64,08 $ | 2/40 | +5,00% | +5,00% | 79,16 $ | 0/2 | 0,00% | +23,53% | DEBOLE | 15,0 | n/d |
| -15,00% | 64,08 $ | 2/40 | +5,00% | +10,00% | 82,93 $ | 0/2 | 0,00% | +29,41% | DEBOLE | 15,0 | n/d |
| -15,00% | 64,08 $ | 2/40 | +5,00% | +15,00% | 86,70 $ | 0/2 | 0,00% | +35,29% | DEBOLE | 15,0 | n/d |
| -15,00% | 64,08 $ | 2/40 | +5,00% | +20,00% | 90,47 $ | 0/2 | 0,00% | +41,18% | DEBOLE | 15,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,16 $ | 34/40 | +85,00% | prezzo iniziale | 75,39 $ | 8/34 | +23,53% | -4,76% | DEBOLE | 8,4 | 19,9 |
| +5,00% | 79,16 $ | 34/40 | +85,00% | -5,00% | 71,62 $ | 2/34 | +5,88% | -9,52% | DEBOLE | 8,4 | 23,5 |
| +5,00% | 79,16 $ | 34/40 | +85,00% | -8,00% | 69,36 $ | 0/34 | 0,00% | -12,38% | DEBOLE | 8,4 | n/d |
| +5,00% | 79,16 $ | 34/40 | +85,00% | -10,00% | 67,85 $ | 0/34 | 0,00% | -14,29% | DEBOLE | 8,4 | n/d |
| +5,00% | 79,16 $ | 34/40 | +85,00% | -15,00% | 64,08 $ | 0/34 | 0,00% | -19,05% | DEBOLE | 8,4 | n/d |
| +10,00% | 82,93 $ | 25/40 | +62,50% | prezzo iniziale | 75,39 $ | 3/25 | +12,00% | -9,09% | DEBOLE | 8,3 | 20,0 |
| +10,00% | 82,93 $ | 25/40 | +62,50% | -5,00% | 71,62 $ | 0/25 | 0,00% | -13,64% | DEBOLE | 8,3 | n/d |
| +10,00% | 82,93 $ | 25/40 | +62,50% | -8,00% | 69,36 $ | 0/25 | 0,00% | -16,36% | DEBOLE | 8,3 | n/d |
| +10,00% | 82,93 $ | 25/40 | +62,50% | -10,00% | 67,85 $ | 0/25 | 0,00% | -18,18% | DEBOLE | 8,3 | n/d |
| +10,00% | 82,93 $ | 25/40 | +62,50% | -15,00% | 64,08 $ | 0/25 | 0,00% | -22,73% | DEBOLE | 8,3 | n/d |
| +15,00% | 86,70 $ | 20/40 | +50,00% | prezzo iniziale | 75,39 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 10,2 | 25,0 |
| +15,00% | 86,70 $ | 20/40 | +50,00% | -5,00% | 71,62 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 10,2 | n/d |
| +15,00% | 86,70 $ | 20/40 | +50,00% | -8,00% | 69,36 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 10,2 | n/d |
| +15,00% | 86,70 $ | 20/40 | +50,00% | -10,00% | 67,85 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 10,2 | n/d |
| +15,00% | 86,70 $ | 20/40 | +50,00% | -15,00% | 64,08 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 10,2 | n/d |
| +20,00% | 90,47 $ | 17/40 | +42,50% | prezzo iniziale | 75,39 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 10,4 | 25,0 |
| +20,00% | 90,47 $ | 17/40 | +42,50% | -5,00% | 71,62 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,47 $ | 17/40 | +42,50% | -8,00% | 69,36 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,47 $ | 17/40 | +42,50% | -10,00% | 67,85 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,47 $ | 17/40 | +42,50% | -15,00% | 64,08 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 10,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 20 poi sono rimbalzati fino a +10,00%. Percentuale: +62,50% (20/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 7 poi sono scaricati a -5,00%. Percentuale: +22,58% (7/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06663 $ | 32/40 | +80,00% | +5,00% | 0,07365 $ | 20/32 | +62,50% | +10,53% | MEDIA | 7,2 | 12,5 |
| -5,00% | 0,06663 $ | 32/40 | +80,00% | +10,00% | 0,07715 $ | 20/32 | +62,50% | +15,79% | MEDIA | 7,2 | 15,1 |
| -5,00% | 0,06663 $ | 32/40 | +80,00% | +15,00% | 0,08066 $ | 16/32 | +50,00% | +21,05% | MEDIA | 7,2 | 17,6 |
| -5,00% | 0,06663 $ | 32/40 | +80,00% | +20,00% | 0,08417 $ | 14/32 | +43,75% | +26,32% | BASSA | 7,2 | 19,1 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +5,00% | 0,07365 $ | 13/24 | +54,17% | +14,13% | MEDIA | 8,0 | 13,6 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +10,00% | 0,07715 $ | 13/24 | +54,17% | +19,57% | MEDIA | 8,0 | 16,3 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +15,00% | 0,08066 $ | 9/24 | +37,50% | +25,00% | BASSA | 8,0 | 18,4 |
| -8,00% | 0,06453 $ | 24/40 | +60,00% | +20,00% | 0,08417 $ | 8/24 | +33,33% | +30,43% | DEBOLE | 8,0 | 20,8 |
| -10,00% | 0,06313 $ | 20/40 | +50,00% | +5,00% | 0,07365 $ | 9/20 | +45,00% | +16,67% | BASSA | 8,6 | 14,0 |
| -10,00% | 0,06313 $ | 20/40 | +50,00% | +10,00% | 0,07715 $ | 9/20 | +45,00% | +22,22% | BASSA | 8,6 | 17,8 |
| -10,00% | 0,06313 $ | 20/40 | +50,00% | +15,00% | 0,08066 $ | 6/20 | +30,00% | +27,78% | DEBOLE | 8,6 | 17,5 |
| -10,00% | 0,06313 $ | 20/40 | +50,00% | +20,00% | 0,08417 $ | 6/20 | +30,00% | +33,33% | DEBOLE | 8,6 | 20,8 |
| -15,00% | 0,05962 $ | 11/40 | +27,50% | +5,00% | 0,07365 $ | 1/11 | +9,09% | +23,53% | DEBOLE | 10,6 | 9,0 |
| -15,00% | 0,05962 $ | 11/40 | +27,50% | +10,00% | 0,07715 $ | 1/11 | +9,09% | +29,41% | DEBOLE | 10,6 | 10,0 |
| -15,00% | 0,05962 $ | 11/40 | +27,50% | +15,00% | 0,08066 $ | 1/11 | +9,09% | +35,29% | DEBOLE | 10,6 | 10,0 |
| -15,00% | 0,05962 $ | 11/40 | +27,50% | +20,00% | 0,08417 $ | 1/11 | +9,09% | +41,18% | DEBOLE | 10,6 | 27,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07365 $ | 33/40 | +82,50% | prezzo iniziale | 0,07014 $ | 24/33 | +72,73% | -4,76% | ALTA | 7,0 | 14,5 |
| +5,00% | 0,07365 $ | 33/40 | +82,50% | -5,00% | 0,06663 $ | 15/33 | +45,45% | -9,52% | BASSA | 7,0 | 15,1 |
| +5,00% | 0,07365 $ | 33/40 | +82,50% | -8,00% | 0,06453 $ | 10/33 | +30,30% | -12,38% | DEBOLE | 7,0 | 14,4 |
| +5,00% | 0,07365 $ | 33/40 | +82,50% | -10,00% | 0,06313 $ | 8/33 | +24,24% | -14,29% | DEBOLE | 7,0 | 14,6 |
| +5,00% | 0,07365 $ | 33/40 | +82,50% | -15,00% | 0,05962 $ | 3/33 | +9,09% | -19,05% | DEBOLE | 7,0 | 24,0 |
| +10,00% | 0,07715 $ | 31/40 | +77,50% | prezzo iniziale | 0,07014 $ | 15/31 | +48,39% | -9,09% | BASSA | 11,9 | 18,7 |
| +10,00% | 0,07715 $ | 31/40 | +77,50% | -5,00% | 0,06663 $ | 7/31 | +22,58% | -13,64% | DEBOLE | 11,9 | 19,9 |
| +10,00% | 0,07715 $ | 31/40 | +77,50% | -8,00% | 0,06453 $ | 3/31 | +9,68% | -16,36% | DEBOLE | 11,9 | 19,7 |
| +10,00% | 0,07715 $ | 31/40 | +77,50% | -10,00% | 0,06313 $ | 2/31 | +6,45% | -18,18% | DEBOLE | 11,9 | 19,5 |
| +10,00% | 0,07715 $ | 31/40 | +77,50% | -15,00% | 0,05962 $ | 1/31 | +3,23% | -22,73% | DEBOLE | 11,9 | 25,0 |
| +15,00% | 0,08066 $ | 24/40 | +60,00% | prezzo iniziale | 0,07014 $ | 4/24 | +16,67% | -13,04% | DEBOLE | 14,9 | 19,2 |
| +15,00% | 0,08066 $ | 24/40 | +60,00% | -5,00% | 0,06663 $ | 2/24 | +8,33% | -17,39% | DEBOLE | 14,9 | 17,0 |
| +15,00% | 0,08066 $ | 24/40 | +60,00% | -8,00% | 0,06453 $ | 1/24 | +4,17% | -20,00% | DEBOLE | 14,9 | 27,0 |
| +15,00% | 0,08066 $ | 24/40 | +60,00% | -10,00% | 0,06313 $ | 1/24 | +4,17% | -21,74% | DEBOLE | 14,9 | 28,0 |
| +15,00% | 0,08066 $ | 24/40 | +60,00% | -15,00% | 0,05962 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 14,9 | n/d |
| +20,00% | 0,08417 $ | 22/40 | +55,00% | prezzo iniziale | 0,07014 $ | 1/22 | +4,55% | -16,67% | DEBOLE | 17,8 | 30,0 |
| +20,00% | 0,08417 $ | 22/40 | +55,00% | -5,00% | 0,06663 $ | 0/22 | 0,00% | -20,83% | DEBOLE | 17,8 | n/d |
| +20,00% | 0,08417 $ | 22/40 | +55,00% | -8,00% | 0,06453 $ | 0/22 | 0,00% | -23,33% | DEBOLE | 17,8 | n/d |
| +20,00% | 0,08417 $ | 22/40 | +55,00% | -10,00% | 0,06313 $ | 0/22 | 0,00% | -25,00% | DEBOLE | 17,8 | n/d |
| +20,00% | 0,08417 $ | 22/40 | +55,00% | -15,00% | 0,05962 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 17,8 | n/d |

---
