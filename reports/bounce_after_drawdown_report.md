# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-07 07:15:34 CEST**  
UTC: **2026-08-07 05:15:34 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.985 $ | 70.615 $ | +41,18% | +15,79% | rimbalzo debole | 70.615 $ | 60.985 $ | +7,41% | -13,64% | spike storicamente più resistente |
| SOL | 69,02 $ | 79,92 $ | +29,41% | +15,79% | rimbalzo poco frequente | 79,92 $ | 69,02 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06553 $ | 0,07588 $ | +37,93% | +15,79% | rimbalzo debole | 0,07588 $ | 0,06553 $ | +12,00% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +41,18% (7/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 2 poi sono scaricati a -5,00%. Percentuale: +7,41% (2/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.985 $ | 17/40 | +42,50% | +5,00% | 67.405 $ | 9/17 | +52,94% | +10,53% | MEDIA | 8,8 | 20,1 |
| -5,00% | 60.985 $ | 17/40 | +42,50% | +10,00% | 70.615 $ | 7/17 | +41,18% | +15,79% | BASSA | 8,8 | 21,0 |
| -5,00% | 60.985 $ | 17/40 | +42,50% | +15,00% | 73.824 $ | 4/17 | +23,53% | +21,05% | DEBOLE | 8,8 | 18,2 |
| -5,00% | 60.985 $ | 17/40 | +42,50% | +20,00% | 77.034 $ | 4/17 | +23,53% | +26,32% | DEBOLE | 8,8 | 19,0 |
| -8,00% | 59.059 $ | 12/40 | +30,00% | +5,00% | 67.405 $ | 4/12 | +33,33% | +14,13% | DEBOLE | 11,2 | 22,0 |
| -8,00% | 59.059 $ | 12/40 | +30,00% | +10,00% | 70.615 $ | 3/12 | +25,00% | +19,57% | DEBOLE | 11,2 | 25,3 |
| -8,00% | 59.059 $ | 12/40 | +30,00% | +15,00% | 73.824 $ | 1/12 | +8,33% | +25,00% | DEBOLE | 11,2 | 28,0 |
| -8,00% | 59.059 $ | 12/40 | +30,00% | +20,00% | 77.034 $ | 1/12 | +8,33% | +30,43% | DEBOLE | 11,2 | 30,0 |
| -10,00% | 57.776 $ | 11/40 | +27,50% | +5,00% | 67.405 $ | 3/11 | +27,27% | +16,67% | DEBOLE | 12,4 | 22,7 |
| -10,00% | 57.776 $ | 11/40 | +27,50% | +10,00% | 70.615 $ | 2/11 | +18,18% | +22,22% | DEBOLE | 12,4 | 24,5 |
| -10,00% | 57.776 $ | 11/40 | +27,50% | +15,00% | 73.824 $ | 0/11 | 0,00% | +27,78% | DEBOLE | 12,4 | n/d |
| -10,00% | 57.776 $ | 11/40 | +27,50% | +20,00% | 77.034 $ | 0/11 | 0,00% | +33,33% | DEBOLE | 12,4 | n/d |
| -15,00% | 54.566 $ | 6/40 | +15,00% | +5,00% | 67.405 $ | 1/6 | +16,67% | +23,53% | DEBOLE | 13,8 | 23,0 |
| -15,00% | 54.566 $ | 6/40 | +15,00% | +10,00% | 70.615 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 13,8 | n/d |
| -15,00% | 54.566 $ | 6/40 | +15,00% | +15,00% | 73.824 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 13,8 | n/d |
| -15,00% | 54.566 $ | 6/40 | +15,00% | +20,00% | 77.034 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 13,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.405 $ | 33/40 | +82,50% | prezzo iniziale | 64.195 $ | 5/33 | +15,15% | -4,76% | DEBOLE | 10,1 | 13,4 |
| +5,00% | 67.405 $ | 33/40 | +82,50% | -5,00% | 60.985 $ | 5/33 | +15,15% | -9,52% | DEBOLE | 10,1 | 16,2 |
| +5,00% | 67.405 $ | 33/40 | +82,50% | -8,00% | 59.059 $ | 4/33 | +12,12% | -12,38% | DEBOLE | 10,1 | 18,8 |
| +5,00% | 67.405 $ | 33/40 | +82,50% | -10,00% | 57.776 $ | 4/33 | +12,12% | -14,29% | DEBOLE | 10,1 | 19,5 |
| +5,00% | 67.405 $ | 33/40 | +82,50% | -15,00% | 54.566 $ | 1/33 | +3,03% | -19,05% | DEBOLE | 10,1 | 10,0 |
| +10,00% | 70.615 $ | 27/40 | +67,50% | prezzo iniziale | 64.195 $ | 2/27 | +7,41% | -9,09% | DEBOLE | 14,4 | 11,5 |
| +10,00% | 70.615 $ | 27/40 | +67,50% | -5,00% | 60.985 $ | 2/27 | +7,41% | -13,64% | DEBOLE | 14,4 | 16,0 |
| +10,00% | 70.615 $ | 27/40 | +67,50% | -8,00% | 59.059 $ | 2/27 | +7,41% | -16,36% | DEBOLE | 14,4 | 16,5 |
| +10,00% | 70.615 $ | 27/40 | +67,50% | -10,00% | 57.776 $ | 2/27 | +7,41% | -18,18% | DEBOLE | 14,4 | 17,0 |
| +10,00% | 70.615 $ | 27/40 | +67,50% | -15,00% | 54.566 $ | 1/27 | +3,70% | -22,73% | DEBOLE | 14,4 | 10,0 |
| +15,00% | 73.824 $ | 20/40 | +50,00% | prezzo iniziale | 64.195 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 13,9 | 6,0 |
| +15,00% | 73.824 $ | 20/40 | +50,00% | -5,00% | 60.985 $ | 1/20 | +5,00% | -17,39% | DEBOLE | 13,9 | 7,0 |
| +15,00% | 73.824 $ | 20/40 | +50,00% | -8,00% | 59.059 $ | 1/20 | +5,00% | -20,00% | DEBOLE | 13,9 | 7,0 |
| +15,00% | 73.824 $ | 20/40 | +50,00% | -10,00% | 57.776 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 13,9 | 7,0 |
| +15,00% | 73.824 $ | 20/40 | +50,00% | -15,00% | 54.566 $ | 1/20 | +5,00% | -26,09% | DEBOLE | 13,9 | 10,0 |
| +20,00% | 77.034 $ | 17/40 | +42,50% | prezzo iniziale | 64.195 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 15,0 | 6,0 |
| +20,00% | 77.034 $ | 17/40 | +42,50% | -5,00% | 60.985 $ | 1/17 | +5,88% | -20,83% | DEBOLE | 15,0 | 7,0 |
| +20,00% | 77.034 $ | 17/40 | +42,50% | -8,00% | 59.059 $ | 1/17 | +5,88% | -23,33% | DEBOLE | 15,0 | 7,0 |
| +20,00% | 77.034 $ | 17/40 | +42,50% | -10,00% | 57.776 $ | 1/17 | +5,88% | -25,00% | DEBOLE | 15,0 | 7,0 |
| +20,00% | 77.034 $ | 17/40 | +42,50% | -15,00% | 54.566 $ | 1/17 | +5,88% | -29,17% | DEBOLE | 15,0 | 10,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +29,41% (5/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 69,02 $ | 17/40 | +42,50% | +5,00% | 76,28 $ | 7/17 | +41,18% | +10,53% | BASSA | 6,0 | 21,9 |
| -5,00% | 69,02 $ | 17/40 | +42,50% | +10,00% | 79,92 $ | 5/17 | +29,41% | +15,79% | DEBOLE | 6,0 | 25,2 |
| -5,00% | 69,02 $ | 17/40 | +42,50% | +15,00% | 83,55 $ | 2/17 | +11,76% | +21,05% | DEBOLE | 6,0 | 19,5 |
| -5,00% | 69,02 $ | 17/40 | +42,50% | +20,00% | 87,18 $ | 1/17 | +5,88% | +26,32% | DEBOLE | 6,0 | 13,0 |
| -8,00% | 66,84 $ | 16/40 | +40,00% | +5,00% | 76,28 $ | 6/16 | +37,50% | +14,13% | BASSA | 8,6 | 23,5 |
| -8,00% | 66,84 $ | 16/40 | +40,00% | +10,00% | 79,92 $ | 5/16 | +31,25% | +19,57% | DEBOLE | 8,6 | 25,2 |
| -8,00% | 66,84 $ | 16/40 | +40,00% | +15,00% | 83,55 $ | 2/16 | +12,50% | +25,00% | DEBOLE | 8,6 | 19,5 |
| -8,00% | 66,84 $ | 16/40 | +40,00% | +20,00% | 87,18 $ | 1/16 | +6,25% | +30,43% | DEBOLE | 8,6 | 13,0 |
| -10,00% | 65,39 $ | 16/40 | +40,00% | +5,00% | 76,28 $ | 6/16 | +37,50% | +16,67% | BASSA | 9,4 | 23,5 |
| -10,00% | 65,39 $ | 16/40 | +40,00% | +10,00% | 79,92 $ | 5/16 | +31,25% | +22,22% | DEBOLE | 9,4 | 25,2 |
| -10,00% | 65,39 $ | 16/40 | +40,00% | +15,00% | 83,55 $ | 2/16 | +12,50% | +27,78% | DEBOLE | 9,4 | 19,5 |
| -10,00% | 65,39 $ | 16/40 | +40,00% | +20,00% | 87,18 $ | 1/16 | +6,25% | +33,33% | DEBOLE | 9,4 | 13,0 |
| -15,00% | 61,75 $ | 9/40 | +22,50% | +5,00% | 76,28 $ | 3/9 | +33,33% | +23,53% | DEBOLE | 12,7 | 26,3 |
| -15,00% | 61,75 $ | 9/40 | +22,50% | +10,00% | 79,92 $ | 2/9 | +22,22% | +29,41% | DEBOLE | 12,7 | 29,0 |
| -15,00% | 61,75 $ | 9/40 | +22,50% | +15,00% | 83,55 $ | 1/9 | +11,11% | +35,29% | DEBOLE | 12,7 | 28,0 |
| -15,00% | 61,75 $ | 9/40 | +22,50% | +20,00% | 87,18 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 12,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 76,28 $ | 30/40 | +75,00% | prezzo iniziale | 72,65 $ | 7/30 | +23,33% | -4,76% | DEBOLE | 8,9 | 14,7 |
| +5,00% | 76,28 $ | 30/40 | +75,00% | -5,00% | 69,02 $ | 2/30 | +6,67% | -9,52% | DEBOLE | 8,9 | 12,5 |
| +5,00% | 76,28 $ | 30/40 | +75,00% | -8,00% | 66,84 $ | 1/30 | +3,33% | -12,38% | DEBOLE | 8,9 | 15,0 |
| +5,00% | 76,28 $ | 30/40 | +75,00% | -10,00% | 65,39 $ | 1/30 | +3,33% | -14,29% | DEBOLE | 8,9 | 17,0 |
| +5,00% | 76,28 $ | 30/40 | +75,00% | -15,00% | 61,75 $ | 0/30 | 0,00% | -19,05% | DEBOLE | 8,9 | n/d |
| +10,00% | 79,92 $ | 26/40 | +65,00% | prezzo iniziale | 72,65 $ | 3/26 | +11,54% | -9,09% | DEBOLE | 15,0 | 23,3 |
| +10,00% | 79,92 $ | 26/40 | +65,00% | -5,00% | 69,02 $ | 0/26 | 0,00% | -13,64% | DEBOLE | 15,0 | n/d |
| +10,00% | 79,92 $ | 26/40 | +65,00% | -8,00% | 66,84 $ | 0/26 | 0,00% | -16,36% | DEBOLE | 15,0 | n/d |
| +10,00% | 79,92 $ | 26/40 | +65,00% | -10,00% | 65,39 $ | 0/26 | 0,00% | -18,18% | DEBOLE | 15,0 | n/d |
| +10,00% | 79,92 $ | 26/40 | +65,00% | -15,00% | 61,75 $ | 0/26 | 0,00% | -22,73% | DEBOLE | 15,0 | n/d |
| +15,00% | 83,55 $ | 17/40 | +42,50% | prezzo iniziale | 72,65 $ | 2/17 | +11,76% | -13,04% | DEBOLE | 13,4 | 20,5 |
| +15,00% | 83,55 $ | 17/40 | +42,50% | -5,00% | 69,02 $ | 0/17 | 0,00% | -17,39% | DEBOLE | 13,4 | n/d |
| +15,00% | 83,55 $ | 17/40 | +42,50% | -8,00% | 66,84 $ | 0/17 | 0,00% | -20,00% | DEBOLE | 13,4 | n/d |
| +15,00% | 83,55 $ | 17/40 | +42,50% | -10,00% | 65,39 $ | 0/17 | 0,00% | -21,74% | DEBOLE | 13,4 | n/d |
| +15,00% | 83,55 $ | 17/40 | +42,50% | -15,00% | 61,75 $ | 0/17 | 0,00% | -26,09% | DEBOLE | 13,4 | n/d |
| +20,00% | 87,18 $ | 14/40 | +35,00% | prezzo iniziale | 72,65 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 15,4 | n/d |
| +20,00% | 87,18 $ | 14/40 | +35,00% | -5,00% | 69,02 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 15,4 | n/d |
| +20,00% | 87,18 $ | 14/40 | +35,00% | -8,00% | 66,84 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 15,4 | n/d |
| +20,00% | 87,18 $ | 14/40 | +35,00% | -10,00% | 65,39 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 15,4 | n/d |
| +20,00% | 87,18 $ | 14/40 | +35,00% | -15,00% | 61,75 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 15,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +37,93% (11/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 3 poi sono scaricati a -5,00%. Percentuale: +12,00% (3/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06553 $ | 29/40 | +72,50% | +5,00% | 0,07243 $ | 13/29 | +44,83% | +10,53% | BASSA | 5,2 | 17,5 |
| -5,00% | 0,06553 $ | 29/40 | +72,50% | +10,00% | 0,07588 $ | 11/29 | +37,93% | +15,79% | BASSA | 5,2 | 18,7 |
| -5,00% | 0,06553 $ | 29/40 | +72,50% | +15,00% | 0,07933 $ | 10/29 | +34,48% | +21,05% | DEBOLE | 5,2 | 20,3 |
| -5,00% | 0,06553 $ | 29/40 | +72,50% | +20,00% | 0,08278 $ | 6/29 | +20,69% | +26,32% | DEBOLE | 5,2 | 26,5 |
| -8,00% | 0,06346 $ | 27/40 | +67,50% | +5,00% | 0,07243 $ | 11/27 | +40,74% | +14,13% | BASSA | 7,1 | 18,7 |
| -8,00% | 0,06346 $ | 27/40 | +67,50% | +10,00% | 0,07588 $ | 9/27 | +33,33% | +19,57% | DEBOLE | 7,1 | 20,3 |
| -8,00% | 0,06346 $ | 27/40 | +67,50% | +15,00% | 0,07933 $ | 8/27 | +29,63% | +25,00% | DEBOLE | 7,1 | 22,1 |
| -8,00% | 0,06346 $ | 27/40 | +67,50% | +20,00% | 0,08278 $ | 5/27 | +18,52% | +30,43% | DEBOLE | 7,1 | 26,6 |
| -10,00% | 0,06208 $ | 25/40 | +62,50% | +5,00% | 0,07243 $ | 9/25 | +36,00% | +16,67% | BASSA | 7,7 | 19,9 |
| -10,00% | 0,06208 $ | 25/40 | +62,50% | +10,00% | 0,07588 $ | 7/25 | +28,00% | +22,22% | DEBOLE | 7,7 | 20,4 |
| -10,00% | 0,06208 $ | 25/40 | +62,50% | +15,00% | 0,07933 $ | 6/25 | +24,00% | +27,78% | DEBOLE | 7,7 | 22,7 |
| -10,00% | 0,06208 $ | 25/40 | +62,50% | +20,00% | 0,08278 $ | 4/25 | +16,00% | +33,33% | DEBOLE | 7,7 | 26,5 |
| -15,00% | 0,05863 $ | 20/40 | +50,00% | +5,00% | 0,07243 $ | 5/20 | +25,00% | +23,53% | DEBOLE | 9,0 | 20,0 |
| -15,00% | 0,05863 $ | 20/40 | +50,00% | +10,00% | 0,07588 $ | 4/20 | +20,00% | +29,41% | DEBOLE | 9,0 | 20,0 |
| -15,00% | 0,05863 $ | 20/40 | +50,00% | +15,00% | 0,07933 $ | 4/20 | +20,00% | +35,29% | DEBOLE | 9,0 | 21,8 |
| -15,00% | 0,05863 $ | 20/40 | +50,00% | +20,00% | 0,08278 $ | 3/20 | +15,00% | +41,18% | DEBOLE | 9,0 | 25,7 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07243 $ | 29/40 | +72,50% | prezzo iniziale | 0,06898 $ | 16/29 | +55,17% | -4,76% | MEDIA | 10,5 | 14,0 |
| +5,00% | 0,07243 $ | 29/40 | +72,50% | -5,00% | 0,06553 $ | 7/29 | +24,14% | -9,52% | DEBOLE | 10,5 | 14,9 |
| +5,00% | 0,07243 $ | 29/40 | +72,50% | -8,00% | 0,06346 $ | 7/29 | +24,14% | -12,38% | DEBOLE | 10,5 | 15,3 |
| +5,00% | 0,07243 $ | 29/40 | +72,50% | -10,00% | 0,06208 $ | 6/29 | +20,69% | -14,29% | DEBOLE | 10,5 | 13,8 |
| +5,00% | 0,07243 $ | 29/40 | +72,50% | -15,00% | 0,05863 $ | 4/29 | +13,79% | -19,05% | DEBOLE | 10,5 | 13,0 |
| +10,00% | 0,07588 $ | 25/40 | +62,50% | prezzo iniziale | 0,06898 $ | 11/25 | +44,00% | -9,09% | BASSA | 13,6 | 16,5 |
| +10,00% | 0,07588 $ | 25/40 | +62,50% | -5,00% | 0,06553 $ | 3/25 | +12,00% | -13,64% | DEBOLE | 13,6 | 16,7 |
| +10,00% | 0,07588 $ | 25/40 | +62,50% | -8,00% | 0,06346 $ | 3/25 | +12,00% | -16,36% | DEBOLE | 13,6 | 17,3 |
| +10,00% | 0,07588 $ | 25/40 | +62,50% | -10,00% | 0,06208 $ | 3/25 | +12,00% | -18,18% | DEBOLE | 13,6 | 18,0 |
| +10,00% | 0,07588 $ | 25/40 | +62,50% | -15,00% | 0,05863 $ | 2/25 | +8,00% | -22,73% | DEBOLE | 13,6 | 17,5 |
| +15,00% | 0,07933 $ | 21/40 | +52,50% | prezzo iniziale | 0,06898 $ | 5/21 | +23,81% | -13,04% | DEBOLE | 17,5 | 15,4 |
| +15,00% | 0,07933 $ | 21/40 | +52,50% | -5,00% | 0,06553 $ | 1/21 | +4,76% | -17,39% | DEBOLE | 17,5 | 15,0 |
| +15,00% | 0,07933 $ | 21/40 | +52,50% | -8,00% | 0,06346 $ | 1/21 | +4,76% | -20,00% | DEBOLE | 17,5 | 16,0 |
| +15,00% | 0,07933 $ | 21/40 | +52,50% | -10,00% | 0,06208 $ | 1/21 | +4,76% | -21,74% | DEBOLE | 17,5 | 16,0 |
| +15,00% | 0,07933 $ | 21/40 | +52,50% | -15,00% | 0,05863 $ | 1/21 | +4,76% | -26,09% | DEBOLE | 17,5 | 25,0 |
| +20,00% | 0,08278 $ | 16/40 | +40,00% | prezzo iniziale | 0,06898 $ | 2/16 | +12,50% | -16,67% | DEBOLE | 23,0 | 20,5 |
| +20,00% | 0,08278 $ | 16/40 | +40,00% | -5,00% | 0,06553 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 23,0 | n/d |
| +20,00% | 0,08278 $ | 16/40 | +40,00% | -8,00% | 0,06346 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 23,0 | n/d |
| +20,00% | 0,08278 $ | 16/40 | +40,00% | -10,00% | 0,06208 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 23,0 | n/d |
| +20,00% | 0,08278 $ | 16/40 | +40,00% | -15,00% | 0,05863 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 23,0 | n/d |

---
