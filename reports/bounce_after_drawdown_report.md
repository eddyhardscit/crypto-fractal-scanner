# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-31 07:13:58 CEST**  
UTC: **2026-07-31 05:13:58 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.113 $ | 70.763 $ | +23,53% | +15,79% | rimbalzo poco frequente | 70.763 $ | 61.113 $ | +3,85% | -13,64% | spike storicamente più resistente |
| SOL | 70,30 $ | 81,40 $ | +23,81% | +15,79% | rimbalzo poco frequente | 81,40 $ | 70,30 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06655 $ | 0,07706 $ | +32,14% | +15,79% | rimbalzo poco frequente | 0,07706 $ | 0,06655 $ | +46,67% | -13,64% | scarico possibile |

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
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 1 poi sono scaricati a -5,00%. Percentuale: +3,85% (1/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.113 $ | 17/40 | +42,50% | +5,00% | 67.546 $ | 6/17 | +35,29% | +10,53% | BASSA | 8,5 | 18,8 |
| -5,00% | 61.113 $ | 17/40 | +42,50% | +10,00% | 70.763 $ | 4/17 | +23,53% | +15,79% | DEBOLE | 8,5 | 15,2 |
| -5,00% | 61.113 $ | 17/40 | +42,50% | +15,00% | 73.979 $ | 4/17 | +23,53% | +21,05% | DEBOLE | 8,5 | 20,5 |
| -5,00% | 61.113 $ | 17/40 | +42,50% | +20,00% | 77.196 $ | 4/17 | +23,53% | +26,32% | DEBOLE | 8,5 | 23,5 |
| -8,00% | 59.183 $ | 14/40 | +35,00% | +5,00% | 67.546 $ | 4/14 | +28,57% | +14,13% | DEBOLE | 10,6 | 21,2 |
| -8,00% | 59.183 $ | 14/40 | +35,00% | +10,00% | 70.763 $ | 2/14 | +14,29% | +19,57% | DEBOLE | 10,6 | 15,5 |
| -8,00% | 59.183 $ | 14/40 | +35,00% | +15,00% | 73.979 $ | 2/14 | +14,29% | +25,00% | DEBOLE | 10,6 | 25,0 |
| -8,00% | 59.183 $ | 14/40 | +35,00% | +20,00% | 77.196 $ | 2/14 | +14,29% | +30,43% | DEBOLE | 10,6 | 26,0 |
| -10,00% | 57.897 $ | 12/40 | +30,00% | +5,00% | 67.546 $ | 2/12 | +16,67% | +16,67% | DEBOLE | 12,1 | 28,0 |
| -10,00% | 57.897 $ | 12/40 | +30,00% | +10,00% | 70.763 $ | 0/12 | 0,00% | +22,22% | DEBOLE | 12,1 | n/d |
| -10,00% | 57.897 $ | 12/40 | +30,00% | +15,00% | 73.979 $ | 0/12 | 0,00% | +27,78% | DEBOLE | 12,1 | n/d |
| -10,00% | 57.897 $ | 12/40 | +30,00% | +20,00% | 77.196 $ | 0/12 | 0,00% | +33,33% | DEBOLE | 12,1 | n/d |
| -15,00% | 54.680 $ | 7/40 | +17,50% | +5,00% | 67.546 $ | 0/7 | 0,00% | +23,53% | DEBOLE | 13,1 | n/d |
| -15,00% | 54.680 $ | 7/40 | +17,50% | +10,00% | 70.763 $ | 0/7 | 0,00% | +29,41% | DEBOLE | 13,1 | n/d |
| -15,00% | 54.680 $ | 7/40 | +17,50% | +15,00% | 73.979 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 13,1 | n/d |
| -15,00% | 54.680 $ | 7/40 | +17,50% | +20,00% | 77.196 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 13,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.546 $ | 31/40 | +77,50% | prezzo iniziale | 64.330 $ | 7/31 | +22,58% | -4,76% | DEBOLE | 8,1 | 12,0 |
| +5,00% | 67.546 $ | 31/40 | +77,50% | -5,00% | 61.113 $ | 4/31 | +12,90% | -9,52% | DEBOLE | 8,1 | 11,2 |
| +5,00% | 67.546 $ | 31/40 | +77,50% | -8,00% | 59.183 $ | 4/31 | +12,90% | -12,38% | DEBOLE | 8,1 | 13,0 |
| +5,00% | 67.546 $ | 31/40 | +77,50% | -10,00% | 57.897 $ | 2/31 | +6,45% | -14,29% | DEBOLE | 8,1 | 20,5 |
| +5,00% | 67.546 $ | 31/40 | +77,50% | -15,00% | 54.680 $ | 1/31 | +3,23% | -19,05% | DEBOLE | 8,1 | 12,0 |
| +10,00% | 70.763 $ | 26/40 | +65,00% | prezzo iniziale | 64.330 $ | 3/26 | +11,54% | -9,09% | DEBOLE | 12,4 | 16,7 |
| +10,00% | 70.763 $ | 26/40 | +65,00% | -5,00% | 61.113 $ | 1/26 | +3,85% | -13,64% | DEBOLE | 12,4 | 10,0 |
| +10,00% | 70.763 $ | 26/40 | +65,00% | -8,00% | 59.183 $ | 1/26 | +3,85% | -16,36% | DEBOLE | 12,4 | 12,0 |
| +10,00% | 70.763 $ | 26/40 | +65,00% | -10,00% | 57.897 $ | 1/26 | +3,85% | -18,18% | DEBOLE | 12,4 | 12,0 |
| +10,00% | 70.763 $ | 26/40 | +65,00% | -15,00% | 54.680 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 12,4 | 12,0 |
| +15,00% | 73.979 $ | 21/40 | +52,50% | prezzo iniziale | 64.330 $ | 2/21 | +9,52% | -13,04% | DEBOLE | 14,8 | 18,5 |
| +15,00% | 73.979 $ | 21/40 | +52,50% | -5,00% | 61.113 $ | 1/21 | +4,76% | -17,39% | DEBOLE | 14,8 | 10,0 |
| +15,00% | 73.979 $ | 21/40 | +52,50% | -8,00% | 59.183 $ | 1/21 | +4,76% | -20,00% | DEBOLE | 14,8 | 12,0 |
| +15,00% | 73.979 $ | 21/40 | +52,50% | -10,00% | 57.897 $ | 1/21 | +4,76% | -21,74% | DEBOLE | 14,8 | 12,0 |
| +15,00% | 73.979 $ | 21/40 | +52,50% | -15,00% | 54.680 $ | 1/21 | +4,76% | -26,09% | DEBOLE | 14,8 | 12,0 |
| +20,00% | 77.196 $ | 17/40 | +42,50% | prezzo iniziale | 64.330 $ | 0/17 | 0,00% | -16,67% | DEBOLE | 17,3 | n/d |
| +20,00% | 77.196 $ | 17/40 | +42,50% | -5,00% | 61.113 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 17,3 | n/d |
| +20,00% | 77.196 $ | 17/40 | +42,50% | -8,00% | 59.183 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 17,3 | n/d |
| +20,00% | 77.196 $ | 17/40 | +42,50% | -10,00% | 57.897 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 17,3 | n/d |
| +20,00% | 77.196 $ | 17/40 | +42,50% | -15,00% | 54.680 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 17,3 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +23,81% (5/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 70,30 $ | 21/40 | +52,50% | +5,00% | 77,70 $ | 8/21 | +38,10% | +10,53% | BASSA | 7,3 | 20,5 |
| -5,00% | 70,30 $ | 21/40 | +52,50% | +10,00% | 81,40 $ | 5/21 | +23,81% | +15,79% | DEBOLE | 7,3 | 21,2 |
| -5,00% | 70,30 $ | 21/40 | +52,50% | +15,00% | 85,10 $ | 3/21 | +14,29% | +21,05% | DEBOLE | 7,3 | 19,7 |
| -5,00% | 70,30 $ | 21/40 | +52,50% | +20,00% | 88,80 $ | 3/21 | +14,29% | +26,32% | DEBOLE | 7,3 | 20,3 |
| -8,00% | 68,08 $ | 18/40 | +45,00% | +5,00% | 77,70 $ | 5/18 | +27,78% | +14,13% | DEBOLE | 8,2 | 23,2 |
| -8,00% | 68,08 $ | 18/40 | +45,00% | +10,00% | 81,40 $ | 3/18 | +16,67% | +19,57% | DEBOLE | 8,2 | 25,0 |
| -8,00% | 68,08 $ | 18/40 | +45,00% | +15,00% | 85,10 $ | 1/18 | +5,56% | +25,00% | DEBOLE | 8,2 | 23,0 |
| -8,00% | 68,08 $ | 18/40 | +45,00% | +20,00% | 88,80 $ | 1/18 | +5,56% | +30,43% | DEBOLE | 8,2 | 23,0 |
| -10,00% | 66,60 $ | 18/40 | +45,00% | +5,00% | 77,70 $ | 5/18 | +27,78% | +16,67% | DEBOLE | 9,7 | 23,2 |
| -10,00% | 66,60 $ | 18/40 | +45,00% | +10,00% | 81,40 $ | 3/18 | +16,67% | +22,22% | DEBOLE | 9,7 | 25,0 |
| -10,00% | 66,60 $ | 18/40 | +45,00% | +15,00% | 85,10 $ | 1/18 | +5,56% | +27,78% | DEBOLE | 9,7 | 23,0 |
| -10,00% | 66,60 $ | 18/40 | +45,00% | +20,00% | 88,80 $ | 1/18 | +5,56% | +33,33% | DEBOLE | 9,7 | 23,0 |
| -15,00% | 62,90 $ | 7/40 | +17,50% | +5,00% | 77,70 $ | 0/7 | 0,00% | +23,53% | DEBOLE | 14,7 | n/d |
| -15,00% | 62,90 $ | 7/40 | +17,50% | +10,00% | 81,40 $ | 0/7 | 0,00% | +29,41% | DEBOLE | 14,7 | n/d |
| -15,00% | 62,90 $ | 7/40 | +17,50% | +15,00% | 85,10 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 14,7 | n/d |
| -15,00% | 62,90 $ | 7/40 | +17,50% | +20,00% | 88,80 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 14,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,70 $ | 28/40 | +70,00% | prezzo iniziale | 74,00 $ | 6/28 | +21,43% | -4,76% | DEBOLE | 9,1 | 8,0 |
| +5,00% | 77,70 $ | 28/40 | +70,00% | -5,00% | 70,30 $ | 4/28 | +14,29% | -9,52% | DEBOLE | 9,1 | 10,5 |
| +5,00% | 77,70 $ | 28/40 | +70,00% | -8,00% | 68,08 $ | 2/28 | +7,14% | -12,38% | DEBOLE | 9,1 | 14,5 |
| +5,00% | 77,70 $ | 28/40 | +70,00% | -10,00% | 66,60 $ | 2/28 | +7,14% | -14,29% | DEBOLE | 9,1 | 16,5 |
| +5,00% | 77,70 $ | 28/40 | +70,00% | -15,00% | 62,90 $ | 0/28 | 0,00% | -19,05% | DEBOLE | 9,1 | n/d |
| +10,00% | 81,40 $ | 21/40 | +52,50% | prezzo iniziale | 74,00 $ | 0/21 | 0,00% | -9,09% | DEBOLE | 11,9 | n/d |
| +10,00% | 81,40 $ | 21/40 | +52,50% | -5,00% | 70,30 $ | 0/21 | 0,00% | -13,64% | DEBOLE | 11,9 | n/d |
| +10,00% | 81,40 $ | 21/40 | +52,50% | -8,00% | 68,08 $ | 0/21 | 0,00% | -16,36% | DEBOLE | 11,9 | n/d |
| +10,00% | 81,40 $ | 21/40 | +52,50% | -10,00% | 66,60 $ | 0/21 | 0,00% | -18,18% | DEBOLE | 11,9 | n/d |
| +10,00% | 81,40 $ | 21/40 | +52,50% | -15,00% | 62,90 $ | 0/21 | 0,00% | -22,73% | DEBOLE | 11,9 | n/d |
| +15,00% | 85,10 $ | 16/40 | +40,00% | prezzo iniziale | 74,00 $ | 0/16 | 0,00% | -13,04% | DEBOLE | 12,6 | n/d |
| +15,00% | 85,10 $ | 16/40 | +40,00% | -5,00% | 70,30 $ | 0/16 | 0,00% | -17,39% | DEBOLE | 12,6 | n/d |
| +15,00% | 85,10 $ | 16/40 | +40,00% | -8,00% | 68,08 $ | 0/16 | 0,00% | -20,00% | DEBOLE | 12,6 | n/d |
| +15,00% | 85,10 $ | 16/40 | +40,00% | -10,00% | 66,60 $ | 0/16 | 0,00% | -21,74% | DEBOLE | 12,6 | n/d |
| +15,00% | 85,10 $ | 16/40 | +40,00% | -15,00% | 62,90 $ | 0/16 | 0,00% | -26,09% | DEBOLE | 12,6 | n/d |
| +20,00% | 88,80 $ | 14/40 | +35,00% | prezzo iniziale | 74,00 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 16,0 | n/d |
| +20,00% | 88,80 $ | 14/40 | +35,00% | -5,00% | 70,30 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 16,0 | n/d |
| +20,00% | 88,80 $ | 14/40 | +35,00% | -8,00% | 68,08 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 16,0 | n/d |
| +20,00% | 88,80 $ | 14/40 | +35,00% | -10,00% | 66,60 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 16,0 | n/d |
| +20,00% | 88,80 $ | 14/40 | +35,00% | -15,00% | 62,90 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 16,0 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +32,14% (9/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 14 poi sono scaricati a -5,00%. Percentuale: +46,67% (14/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06655 $ | 28/40 | +70,00% | +5,00% | 0,07355 $ | 14/28 | +50,00% | +10,53% | MEDIA | 10,7 | 24,8 |
| -5,00% | 0,06655 $ | 28/40 | +70,00% | +10,00% | 0,07706 $ | 9/28 | +32,14% | +15,79% | DEBOLE | 10,7 | 26,6 |
| -5,00% | 0,06655 $ | 28/40 | +70,00% | +15,00% | 0,08056 $ | 5/28 | +17,86% | +21,05% | DEBOLE | 10,7 | 25,8 |
| -5,00% | 0,06655 $ | 28/40 | +70,00% | +20,00% | 0,08406 $ | 2/28 | +7,14% | +26,32% | DEBOLE | 10,7 | 24,0 |
| -8,00% | 0,06445 $ | 25/40 | +62,50% | +5,00% | 0,07355 $ | 12/25 | +48,00% | +14,13% | BASSA | 12,4 | 26,0 |
| -8,00% | 0,06445 $ | 25/40 | +62,50% | +10,00% | 0,07706 $ | 7/25 | +28,00% | +19,57% | DEBOLE | 12,4 | 27,3 |
| -8,00% | 0,06445 $ | 25/40 | +62,50% | +15,00% | 0,08056 $ | 3/25 | +12,00% | +25,00% | DEBOLE | 12,4 | 27,0 |
| -8,00% | 0,06445 $ | 25/40 | +62,50% | +20,00% | 0,08406 $ | 1/25 | +4,00% | +30,43% | DEBOLE | 12,4 | 28,0 |
| -10,00% | 0,06305 $ | 20/40 | +50,00% | +5,00% | 0,07355 $ | 7/20 | +35,00% | +16,67% | BASSA | 12,0 | 24,4 |
| -10,00% | 0,06305 $ | 20/40 | +50,00% | +10,00% | 0,07706 $ | 3/20 | +15,00% | +22,22% | DEBOLE | 12,0 | 25,7 |
| -10,00% | 0,06305 $ | 20/40 | +50,00% | +15,00% | 0,08056 $ | 2/20 | +10,00% | +27,78% | DEBOLE | 12,0 | 26,5 |
| -10,00% | 0,06305 $ | 20/40 | +50,00% | +20,00% | 0,08406 $ | 0/20 | 0,00% | +33,33% | DEBOLE | 12,0 | n/d |
| -15,00% | 0,05954 $ | 12/40 | +30,00% | +5,00% | 0,07355 $ | 1/12 | +8,33% | +23,53% | DEBOLE | 13,2 | 23,0 |
| -15,00% | 0,05954 $ | 12/40 | +30,00% | +10,00% | 0,07706 $ | 1/12 | +8,33% | +29,41% | DEBOLE | 13,2 | 23,0 |
| -15,00% | 0,05954 $ | 12/40 | +30,00% | +15,00% | 0,08056 $ | 1/12 | +8,33% | +35,29% | DEBOLE | 13,2 | 24,0 |
| -15,00% | 0,05954 $ | 12/40 | +30,00% | +20,00% | 0,08406 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 13,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07355 $ | 35/40 | +87,50% | prezzo iniziale | 0,07005 $ | 28/35 | +80,00% | -4,76% | ALTA | 6,3 | 11,8 |
| +5,00% | 0,07355 $ | 35/40 | +87,50% | -5,00% | 0,06655 $ | 19/35 | +54,29% | -9,52% | MEDIA | 6,3 | 13,2 |
| +5,00% | 0,07355 $ | 35/40 | +87,50% | -8,00% | 0,06445 $ | 16/35 | +45,71% | -12,38% | BASSA | 6,3 | 14,8 |
| +5,00% | 0,07355 $ | 35/40 | +87,50% | -10,00% | 0,06305 $ | 11/35 | +31,43% | -14,29% | DEBOLE | 6,3 | 14,3 |
| +5,00% | 0,07355 $ | 35/40 | +87,50% | -15,00% | 0,05954 $ | 6/35 | +17,14% | -19,05% | DEBOLE | 6,3 | 15,5 |
| +10,00% | 0,07706 $ | 30/40 | +75,00% | prezzo iniziale | 0,07005 $ | 20/30 | +66,67% | -9,09% | ALTA | 9,5 | 12,9 |
| +10,00% | 0,07706 $ | 30/40 | +75,00% | -5,00% | 0,06655 $ | 14/30 | +46,67% | -13,64% | BASSA | 9,5 | 15,0 |
| +10,00% | 0,07706 $ | 30/40 | +75,00% | -8,00% | 0,06445 $ | 11/30 | +36,67% | -16,36% | BASSA | 9,5 | 16,1 |
| +10,00% | 0,07706 $ | 30/40 | +75,00% | -10,00% | 0,06305 $ | 7/30 | +23,33% | -18,18% | DEBOLE | 9,5 | 14,1 |
| +10,00% | 0,07706 $ | 30/40 | +75,00% | -15,00% | 0,05954 $ | 6/30 | +20,00% | -22,73% | DEBOLE | 9,5 | 15,5 |
| +15,00% | 0,08056 $ | 19/40 | +47,50% | prezzo iniziale | 0,07005 $ | 8/19 | +42,11% | -13,04% | BASSA | 13,7 | 15,8 |
| +15,00% | 0,08056 $ | 19/40 | +47,50% | -5,00% | 0,06655 $ | 4/19 | +21,05% | -17,39% | DEBOLE | 13,7 | 16,5 |
| +15,00% | 0,08056 $ | 19/40 | +47,50% | -8,00% | 0,06445 $ | 3/19 | +15,79% | -20,00% | DEBOLE | 13,7 | 17,0 |
| +15,00% | 0,08056 $ | 19/40 | +47,50% | -10,00% | 0,06305 $ | 2/19 | +10,53% | -21,74% | DEBOLE | 13,7 | 14,0 |
| +15,00% | 0,08056 $ | 19/40 | +47,50% | -15,00% | 0,05954 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 13,7 | 11,0 |
| +20,00% | 0,08406 $ | 13/40 | +32,50% | prezzo iniziale | 0,07005 $ | 4/13 | +30,77% | -16,67% | DEBOLE | 13,3 | 17,0 |
| +20,00% | 0,08406 $ | 13/40 | +32,50% | -5,00% | 0,06655 $ | 2/13 | +15,38% | -20,83% | DEBOLE | 13,3 | 21,5 |
| +20,00% | 0,08406 $ | 13/40 | +32,50% | -8,00% | 0,06445 $ | 1/13 | +7,69% | -23,33% | DEBOLE | 13,3 | 17,0 |
| +20,00% | 0,08406 $ | 13/40 | +32,50% | -10,00% | 0,06305 $ | 1/13 | +7,69% | -25,00% | DEBOLE | 13,3 | 17,0 |
| +20,00% | 0,08406 $ | 13/40 | +32,50% | -15,00% | 0,05954 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 13,3 | n/d |

---
