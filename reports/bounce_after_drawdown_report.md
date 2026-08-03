# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-03 07:14:27 CEST**  
UTC: **2026-08-03 05:14:27 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.622 $ | 69.036 $ | +6,25% | +15,79% | rimbalzo poco frequente | 69.036 $ | 59.622 $ | +4,35% | -13,64% | spike storicamente più resistente |
| SOL | 69,28 $ | 80,22 $ | +31,25% | +15,79% | rimbalzo poco frequente | 80,22 $ | 69,28 $ | +3,85% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06636 $ | 0,07683 $ | +32,26% | +15,79% | rimbalzo poco frequente | 0,07683 $ | 0,06636 $ | +22,73% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 1 poi sono rimbalzati fino a +10,00%. Percentuale: +6,25% (1/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 1 poi sono scaricati a -5,00%. Percentuale: +4,35% (1/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.622 $ | 16/40 | +40,00% | +5,00% | 65.898 $ | 2/16 | +12,50% | +10,53% | DEBOLE | 7,4 | 16,5 |
| -5,00% | 59.622 $ | 16/40 | +40,00% | +10,00% | 69.036 $ | 1/16 | +6,25% | +15,79% | DEBOLE | 7,4 | 8,0 |
| -5,00% | 59.622 $ | 16/40 | +40,00% | +15,00% | 72.174 $ | 1/16 | +6,25% | +21,05% | DEBOLE | 7,4 | 15,0 |
| -5,00% | 59.622 $ | 16/40 | +40,00% | +20,00% | 75.312 $ | 1/16 | +6,25% | +26,32% | DEBOLE | 7,4 | 17,0 |
| -8,00% | 57.740 $ | 14/40 | +35,00% | +5,00% | 65.898 $ | 2/14 | +14,29% | +14,13% | DEBOLE | 8,4 | 16,5 |
| -8,00% | 57.740 $ | 14/40 | +35,00% | +10,00% | 69.036 $ | 1/14 | +7,14% | +19,57% | DEBOLE | 8,4 | 8,0 |
| -8,00% | 57.740 $ | 14/40 | +35,00% | +15,00% | 72.174 $ | 1/14 | +7,14% | +25,00% | DEBOLE | 8,4 | 15,0 |
| -8,00% | 57.740 $ | 14/40 | +35,00% | +20,00% | 75.312 $ | 1/14 | +7,14% | +30,43% | DEBOLE | 8,4 | 17,0 |
| -10,00% | 56.484 $ | 13/40 | +32,50% | +5,00% | 65.898 $ | 2/13 | +15,38% | +16,67% | DEBOLE | 10,2 | 16,5 |
| -10,00% | 56.484 $ | 13/40 | +32,50% | +10,00% | 69.036 $ | 1/13 | +7,69% | +22,22% | DEBOLE | 10,2 | 8,0 |
| -10,00% | 56.484 $ | 13/40 | +32,50% | +15,00% | 72.174 $ | 1/13 | +7,69% | +27,78% | DEBOLE | 10,2 | 15,0 |
| -10,00% | 56.484 $ | 13/40 | +32,50% | +20,00% | 75.312 $ | 1/13 | +7,69% | +33,33% | DEBOLE | 10,2 | 17,0 |
| -15,00% | 53.346 $ | 8/40 | +20,00% | +5,00% | 65.898 $ | 1/8 | +12,50% | +23,53% | DEBOLE | 9,8 | 8,0 |
| -15,00% | 53.346 $ | 8/40 | +20,00% | +10,00% | 69.036 $ | 1/8 | +12,50% | +29,41% | DEBOLE | 9,8 | 8,0 |
| -15,00% | 53.346 $ | 8/40 | +20,00% | +15,00% | 72.174 $ | 1/8 | +12,50% | +35,29% | DEBOLE | 9,8 | 15,0 |
| -15,00% | 53.346 $ | 8/40 | +20,00% | +20,00% | 75.312 $ | 1/8 | +12,50% | +41,18% | DEBOLE | 9,8 | 17,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.898 $ | 28/40 | +70,00% | prezzo iniziale | 62.760 $ | 5/28 | +17,86% | -4,76% | DEBOLE | 6,3 | 12,8 |
| +5,00% | 65.898 $ | 28/40 | +70,00% | -5,00% | 59.622 $ | 3/28 | +10,71% | -9,52% | DEBOLE | 6,3 | 17,0 |
| +5,00% | 65.898 $ | 28/40 | +70,00% | -8,00% | 57.740 $ | 3/28 | +10,71% | -12,38% | DEBOLE | 6,3 | 17,3 |
| +5,00% | 65.898 $ | 28/40 | +70,00% | -10,00% | 56.484 $ | 3/28 | +10,71% | -14,29% | DEBOLE | 6,3 | 18,7 |
| +5,00% | 65.898 $ | 28/40 | +70,00% | -15,00% | 53.346 $ | 1/28 | +3,57% | -19,05% | DEBOLE | 6,3 | 12,0 |
| +10,00% | 69.036 $ | 23/40 | +57,50% | prezzo iniziale | 62.760 $ | 2/23 | +8,70% | -9,09% | DEBOLE | 10,6 | 15,0 |
| +10,00% | 69.036 $ | 23/40 | +57,50% | -5,00% | 59.622 $ | 1/23 | +4,35% | -13,64% | DEBOLE | 10,6 | 25,0 |
| +10,00% | 69.036 $ | 23/40 | +57,50% | -8,00% | 57.740 $ | 1/23 | +4,35% | -16,36% | DEBOLE | 10,6 | 26,0 |
| +10,00% | 69.036 $ | 23/40 | +57,50% | -10,00% | 56.484 $ | 1/23 | +4,35% | -18,18% | DEBOLE | 10,6 | 27,0 |
| +10,00% | 69.036 $ | 23/40 | +57,50% | -15,00% | 53.346 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 10,6 | n/d |
| +15,00% | 72.174 $ | 20/40 | +50,00% | prezzo iniziale | 62.760 $ | 0/20 | 0,00% | -13,04% | DEBOLE | 13,9 | n/d |
| +15,00% | 72.174 $ | 20/40 | +50,00% | -5,00% | 59.622 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 13,9 | n/d |
| +15,00% | 72.174 $ | 20/40 | +50,00% | -8,00% | 57.740 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 13,9 | n/d |
| +15,00% | 72.174 $ | 20/40 | +50,00% | -10,00% | 56.484 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 13,9 | n/d |
| +15,00% | 72.174 $ | 20/40 | +50,00% | -15,00% | 53.346 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 13,9 | n/d |
| +20,00% | 75.312 $ | 17/40 | +42,50% | prezzo iniziale | 62.760 $ | 0/17 | 0,00% | -16,67% | DEBOLE | 15,7 | n/d |
| +20,00% | 75.312 $ | 17/40 | +42,50% | -5,00% | 59.622 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 15,7 | n/d |
| +20,00% | 75.312 $ | 17/40 | +42,50% | -8,00% | 57.740 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 15,7 | n/d |
| +20,00% | 75.312 $ | 17/40 | +42,50% | -10,00% | 56.484 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 15,7 | n/d |
| +20,00% | 75.312 $ | 17/40 | +42,50% | -15,00% | 53.346 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 15,7 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +31,25% (5/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 1 poi sono scaricati a -5,00%. Percentuale: +3,85% (1/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 69,28 $ | 16/40 | +40,00% | +5,00% | 76,58 $ | 7/16 | +43,75% | +10,53% | BASSA | 6,9 | 16,9 |
| -5,00% | 69,28 $ | 16/40 | +40,00% | +10,00% | 80,22 $ | 5/16 | +31,25% | +15,79% | DEBOLE | 6,9 | 19,2 |
| -5,00% | 69,28 $ | 16/40 | +40,00% | +15,00% | 83,87 $ | 3/16 | +18,75% | +21,05% | DEBOLE | 6,9 | 19,3 |
| -5,00% | 69,28 $ | 16/40 | +40,00% | +20,00% | 87,52 $ | 3/16 | +18,75% | +26,32% | DEBOLE | 6,9 | 19,7 |
| -8,00% | 67,10 $ | 13/40 | +32,50% | +5,00% | 76,58 $ | 4/13 | +30,77% | +14,13% | DEBOLE | 7,7 | 21,5 |
| -8,00% | 67,10 $ | 13/40 | +32,50% | +10,00% | 80,22 $ | 3/13 | +23,08% | +19,57% | DEBOLE | 7,7 | 20,3 |
| -8,00% | 67,10 $ | 13/40 | +32,50% | +15,00% | 83,87 $ | 1/13 | +7,69% | +25,00% | DEBOLE | 7,7 | 18,0 |
| -8,00% | 67,10 $ | 13/40 | +32,50% | +20,00% | 87,52 $ | 1/13 | +7,69% | +30,43% | DEBOLE | 7,7 | 18,0 |
| -10,00% | 65,64 $ | 12/40 | +30,00% | +5,00% | 76,58 $ | 4/12 | +33,33% | +16,67% | DEBOLE | 8,8 | 21,5 |
| -10,00% | 65,64 $ | 12/40 | +30,00% | +10,00% | 80,22 $ | 3/12 | +25,00% | +22,22% | DEBOLE | 8,8 | 20,3 |
| -10,00% | 65,64 $ | 12/40 | +30,00% | +15,00% | 83,87 $ | 1/12 | +8,33% | +27,78% | DEBOLE | 8,8 | 18,0 |
| -10,00% | 65,64 $ | 12/40 | +30,00% | +20,00% | 87,52 $ | 1/12 | +8,33% | +33,33% | DEBOLE | 8,8 | 18,0 |
| -15,00% | 61,99 $ | 7/40 | +17,50% | +5,00% | 76,58 $ | 1/7 | +14,29% | +23,53% | DEBOLE | 13,9 | 28,0 |
| -15,00% | 61,99 $ | 7/40 | +17,50% | +10,00% | 80,22 $ | 1/7 | +14,29% | +29,41% | DEBOLE | 13,9 | 30,0 |
| -15,00% | 61,99 $ | 7/40 | +17,50% | +15,00% | 83,87 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 13,9 | n/d |
| -15,00% | 61,99 $ | 7/40 | +17,50% | +20,00% | 87,52 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 13,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 76,58 $ | 32/40 | +80,00% | prezzo iniziale | 72,93 $ | 8/32 | +25,00% | -4,76% | DEBOLE | 8,0 | 10,6 |
| +5,00% | 76,58 $ | 32/40 | +80,00% | -5,00% | 69,28 $ | 4/32 | +12,50% | -9,52% | DEBOLE | 8,0 | 13,2 |
| +5,00% | 76,58 $ | 32/40 | +80,00% | -8,00% | 67,10 $ | 2/32 | +6,25% | -12,38% | DEBOLE | 8,0 | 18,0 |
| +5,00% | 76,58 $ | 32/40 | +80,00% | -10,00% | 65,64 $ | 1/32 | +3,12% | -14,29% | DEBOLE | 8,0 | 23,0 |
| +5,00% | 76,58 $ | 32/40 | +80,00% | -15,00% | 61,99 $ | 0/32 | 0,00% | -19,05% | DEBOLE | 8,0 | n/d |
| +10,00% | 80,22 $ | 26/40 | +65,00% | prezzo iniziale | 72,93 $ | 1/26 | +3,85% | -9,09% | DEBOLE | 11,3 | 14,0 |
| +10,00% | 80,22 $ | 26/40 | +65,00% | -5,00% | 69,28 $ | 1/26 | +3,85% | -13,64% | DEBOLE | 11,3 | 18,0 |
| +10,00% | 80,22 $ | 26/40 | +65,00% | -8,00% | 67,10 $ | 1/26 | +3,85% | -16,36% | DEBOLE | 11,3 | 18,0 |
| +10,00% | 80,22 $ | 26/40 | +65,00% | -10,00% | 65,64 $ | 1/26 | +3,85% | -18,18% | DEBOLE | 11,3 | 23,0 |
| +10,00% | 80,22 $ | 26/40 | +65,00% | -15,00% | 61,99 $ | 0/26 | 0,00% | -22,73% | DEBOLE | 11,3 | n/d |
| +15,00% | 83,87 $ | 20/40 | +50,00% | prezzo iniziale | 72,93 $ | 0/20 | 0,00% | -13,04% | DEBOLE | 14,8 | n/d |
| +15,00% | 83,87 $ | 20/40 | +50,00% | -5,00% | 69,28 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 14,8 | n/d |
| +15,00% | 83,87 $ | 20/40 | +50,00% | -8,00% | 67,10 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 14,8 | n/d |
| +15,00% | 83,87 $ | 20/40 | +50,00% | -10,00% | 65,64 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 14,8 | n/d |
| +15,00% | 83,87 $ | 20/40 | +50,00% | -15,00% | 61,99 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 14,8 | n/d |
| +20,00% | 87,52 $ | 16/40 | +40,00% | prezzo iniziale | 72,93 $ | 0/16 | 0,00% | -16,67% | DEBOLE | 17,7 | n/d |
| +20,00% | 87,52 $ | 16/40 | +40,00% | -5,00% | 69,28 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 17,7 | n/d |
| +20,00% | 87,52 $ | 16/40 | +40,00% | -8,00% | 67,10 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 17,7 | n/d |
| +20,00% | 87,52 $ | 16/40 | +40,00% | -10,00% | 65,64 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 17,7 | n/d |
| +20,00% | 87,52 $ | 16/40 | +40,00% | -15,00% | 61,99 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 17,7 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +32,26% (10/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 5 poi sono scaricati a -5,00%. Percentuale: +22,73% (5/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06636 $ | 31/40 | +77,50% | +5,00% | 0,07334 $ | 16/31 | +51,61% | +10,53% | MEDIA | 5,4 | 19,6 |
| -5,00% | 0,06636 $ | 31/40 | +77,50% | +10,00% | 0,07683 $ | 10/31 | +32,26% | +15,79% | DEBOLE | 5,4 | 19,5 |
| -5,00% | 0,06636 $ | 31/40 | +77,50% | +15,00% | 0,08033 $ | 9/31 | +29,03% | +21,05% | DEBOLE | 5,4 | 21,4 |
| -5,00% | 0,06636 $ | 31/40 | +77,50% | +20,00% | 0,08382 $ | 4/31 | +12,90% | +26,32% | DEBOLE | 5,4 | 20,5 |
| -8,00% | 0,06426 $ | 27/40 | +67,50% | +5,00% | 0,07334 $ | 12/27 | +44,44% | +14,13% | BASSA | 6,6 | 19,8 |
| -8,00% | 0,06426 $ | 27/40 | +67,50% | +10,00% | 0,07683 $ | 7/27 | +25,93% | +19,57% | DEBOLE | 6,6 | 19,7 |
| -8,00% | 0,06426 $ | 27/40 | +67,50% | +15,00% | 0,08033 $ | 6/27 | +22,22% | +25,00% | DEBOLE | 6,6 | 21,7 |
| -8,00% | 0,06426 $ | 27/40 | +67,50% | +20,00% | 0,08382 $ | 3/27 | +11,11% | +30,43% | DEBOLE | 6,6 | 22,0 |
| -10,00% | 0,06286 $ | 25/40 | +62,50% | +5,00% | 0,07334 $ | 10/25 | +40,00% | +16,67% | BASSA | 8,1 | 21,5 |
| -10,00% | 0,06286 $ | 25/40 | +62,50% | +10,00% | 0,07683 $ | 5/25 | +20,00% | +22,22% | DEBOLE | 8,1 | 20,6 |
| -10,00% | 0,06286 $ | 25/40 | +62,50% | +15,00% | 0,08033 $ | 4/25 | +16,00% | +27,78% | DEBOLE | 8,1 | 23,8 |
| -10,00% | 0,06286 $ | 25/40 | +62,50% | +20,00% | 0,08382 $ | 1/25 | +4,00% | +33,33% | DEBOLE | 8,1 | 24,0 |
| -15,00% | 0,05937 $ | 18/40 | +45,00% | +5,00% | 0,07334 $ | 4/18 | +22,22% | +23,53% | DEBOLE | 12,1 | 23,8 |
| -15,00% | 0,05937 $ | 18/40 | +45,00% | +10,00% | 0,07683 $ | 2/18 | +11,11% | +29,41% | DEBOLE | 12,1 | 23,0 |
| -15,00% | 0,05937 $ | 18/40 | +45,00% | +15,00% | 0,08033 $ | 2/18 | +11,11% | +35,29% | DEBOLE | 12,1 | 23,5 |
| -15,00% | 0,05937 $ | 18/40 | +45,00% | +20,00% | 0,08382 $ | 1/18 | +5,56% | +41,18% | DEBOLE | 12,1 | 24,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07334 $ | 31/40 | +77,50% | prezzo iniziale | 0,06985 $ | 20/31 | +64,52% | -4,76% | MEDIA | 9,6 | 15,2 |
| +5,00% | 0,07334 $ | 31/40 | +77,50% | -5,00% | 0,06636 $ | 13/31 | +41,94% | -9,52% | BASSA | 9,6 | 13,7 |
| +5,00% | 0,07334 $ | 31/40 | +77,50% | -8,00% | 0,06426 $ | 10/31 | +32,26% | -12,38% | DEBOLE | 9,6 | 12,8 |
| +5,00% | 0,07334 $ | 31/40 | +77,50% | -10,00% | 0,06286 $ | 8/31 | +25,81% | -14,29% | DEBOLE | 9,6 | 12,4 |
| +5,00% | 0,07334 $ | 31/40 | +77,50% | -15,00% | 0,05937 $ | 6/31 | +19,35% | -19,05% | DEBOLE | 9,6 | 14,0 |
| +10,00% | 0,07683 $ | 22/40 | +55,00% | prezzo iniziale | 0,06985 $ | 8/22 | +36,36% | -9,09% | BASSA | 11,3 | 16,4 |
| +10,00% | 0,07683 $ | 22/40 | +55,00% | -5,00% | 0,06636 $ | 5/22 | +22,73% | -13,64% | DEBOLE | 11,3 | 17,0 |
| +10,00% | 0,07683 $ | 22/40 | +55,00% | -8,00% | 0,06426 $ | 3/22 | +13,64% | -16,36% | DEBOLE | 11,3 | 13,7 |
| +10,00% | 0,07683 $ | 22/40 | +55,00% | -10,00% | 0,06286 $ | 3/22 | +13,64% | -18,18% | DEBOLE | 11,3 | 13,7 |
| +10,00% | 0,07683 $ | 22/40 | +55,00% | -15,00% | 0,05937 $ | 3/22 | +13,64% | -22,73% | DEBOLE | 11,3 | 16,7 |
| +15,00% | 0,08033 $ | 19/40 | +47,50% | prezzo iniziale | 0,06985 $ | 6/19 | +31,58% | -13,04% | DEBOLE | 11,5 | 16,5 |
| +15,00% | 0,08033 $ | 19/40 | +47,50% | -5,00% | 0,06636 $ | 3/19 | +15,79% | -17,39% | DEBOLE | 11,5 | 14,3 |
| +15,00% | 0,08033 $ | 19/40 | +47,50% | -8,00% | 0,06426 $ | 2/19 | +10,53% | -20,00% | DEBOLE | 11,5 | 13,5 |
| +15,00% | 0,08033 $ | 19/40 | +47,50% | -10,00% | 0,06286 $ | 2/19 | +10,53% | -21,74% | DEBOLE | 11,5 | 13,5 |
| +15,00% | 0,08033 $ | 19/40 | +47,50% | -15,00% | 0,05937 $ | 2/19 | +10,53% | -26,09% | DEBOLE | 11,5 | 18,0 |
| +20,00% | 0,08382 $ | 13/40 | +32,50% | prezzo iniziale | 0,06985 $ | 3/13 | +23,08% | -16,67% | DEBOLE | 11,8 | 16,7 |
| +20,00% | 0,08382 $ | 13/40 | +32,50% | -5,00% | 0,06636 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 11,8 | 17,0 |
| +20,00% | 0,08382 $ | 13/40 | +32,50% | -8,00% | 0,06426 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 11,8 | n/d |
| +20,00% | 0,08382 $ | 13/40 | +32,50% | -10,00% | 0,06286 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 11,8 | n/d |
| +20,00% | 0,08382 $ | 13/40 | +32,50% | -15,00% | 0,05937 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 11,8 | n/d |

---
