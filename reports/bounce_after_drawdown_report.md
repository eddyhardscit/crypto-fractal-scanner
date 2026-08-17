# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-17 07:31:41 CEST**  
UTC: **2026-08-17 05:31:41 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.258 $ | 69.772 $ | +43,75% | +15,79% | rimbalzo debole | 69.772 $ | 60.258 $ | +14,29% | -13,64% | spike storicamente più resistente |
| SOL | 71,65 $ | 82,96 $ | +21,43% | +15,79% | rimbalzo poco frequente | 82,96 $ | 71,65 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06660 $ | 0,07711 $ | +57,14% | +15,79% | rimbalzo possibile | 0,07711 $ | 0,06660 $ | +28,12% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +43,75% (7/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 4 poi sono scaricati a -5,00%. Percentuale: +14,29% (4/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.258 $ | 16/40 | +40,00% | +5,00% | 66.601 $ | 10/16 | +62,50% | +10,53% | MEDIA | 9,1 | 18,3 |
| -5,00% | 60.258 $ | 16/40 | +40,00% | +10,00% | 69.772 $ | 7/16 | +43,75% | +15,79% | BASSA | 9,1 | 16,9 |
| -5,00% | 60.258 $ | 16/40 | +40,00% | +15,00% | 72.944 $ | 7/16 | +43,75% | +21,05% | BASSA | 9,1 | 18,7 |
| -5,00% | 60.258 $ | 16/40 | +40,00% | +20,00% | 76.115 $ | 6/16 | +37,50% | +26,32% | BASSA | 9,1 | 17,3 |
| -8,00% | 58.355 $ | 11/40 | +27,50% | +5,00% | 66.601 $ | 6/11 | +54,55% | +14,13% | MEDIA | 9,1 | 19,3 |
| -8,00% | 58.355 $ | 11/40 | +27,50% | +10,00% | 69.772 $ | 5/11 | +45,45% | +19,57% | BASSA | 9,1 | 18,2 |
| -8,00% | 58.355 $ | 11/40 | +27,50% | +15,00% | 72.944 $ | 5/11 | +45,45% | +25,00% | BASSA | 9,1 | 20,0 |
| -8,00% | 58.355 $ | 11/40 | +27,50% | +20,00% | 76.115 $ | 4/11 | +36,36% | +30,43% | BASSA | 9,1 | 18,2 |
| -10,00% | 57.086 $ | 11/40 | +27,50% | +5,00% | 66.601 $ | 6/11 | +54,55% | +16,67% | MEDIA | 13,3 | 19,3 |
| -10,00% | 57.086 $ | 11/40 | +27,50% | +10,00% | 69.772 $ | 5/11 | +45,45% | +22,22% | BASSA | 13,3 | 18,2 |
| -10,00% | 57.086 $ | 11/40 | +27,50% | +15,00% | 72.944 $ | 5/11 | +45,45% | +27,78% | BASSA | 13,3 | 20,0 |
| -10,00% | 57.086 $ | 11/40 | +27,50% | +20,00% | 76.115 $ | 4/11 | +36,36% | +33,33% | BASSA | 13,3 | 18,2 |
| -15,00% | 53.915 $ | 6/40 | +15,00% | +5,00% | 66.601 $ | 2/6 | +33,33% | +23,53% | DEBOLE | 15,0 | 20,0 |
| -15,00% | 53.915 $ | 6/40 | +15,00% | +10,00% | 69.772 $ | 2/6 | +33,33% | +29,41% | DEBOLE | 15,0 | 20,5 |
| -15,00% | 53.915 $ | 6/40 | +15,00% | +15,00% | 72.944 $ | 2/6 | +33,33% | +35,29% | DEBOLE | 15,0 | 23,0 |
| -15,00% | 53.915 $ | 6/40 | +15,00% | +20,00% | 76.115 $ | 1/6 | +16,67% | +41,18% | DEBOLE | 15,0 | 18,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.601 $ | 37/40 | +92,50% | prezzo iniziale | 63.429 $ | 15/37 | +40,54% | -4,76% | BASSA | 9,5 | 22,5 |
| +5,00% | 66.601 $ | 37/40 | +92,50% | -5,00% | 60.258 $ | 8/37 | +21,62% | -9,52% | DEBOLE | 9,5 | 19,5 |
| +5,00% | 66.601 $ | 37/40 | +92,50% | -8,00% | 58.355 $ | 7/37 | +18,92% | -12,38% | DEBOLE | 9,5 | 18,4 |
| +5,00% | 66.601 $ | 37/40 | +92,50% | -10,00% | 57.086 $ | 5/37 | +13,51% | -14,29% | DEBOLE | 9,5 | 17,6 |
| +5,00% | 66.601 $ | 37/40 | +92,50% | -15,00% | 53.915 $ | 4/37 | +10,81% | -19,05% | DEBOLE | 9,5 | 20,8 |
| +10,00% | 69.772 $ | 28/40 | +70,00% | prezzo iniziale | 63.429 $ | 8/28 | +28,57% | -9,09% | DEBOLE | 11,3 | 25,9 |
| +10,00% | 69.772 $ | 28/40 | +70,00% | -5,00% | 60.258 $ | 4/28 | +14,29% | -13,64% | DEBOLE | 11,3 | 26,0 |
| +10,00% | 69.772 $ | 28/40 | +70,00% | -8,00% | 58.355 $ | 3/28 | +10,71% | -16,36% | DEBOLE | 11,3 | 25,3 |
| +10,00% | 69.772 $ | 28/40 | +70,00% | -10,00% | 57.086 $ | 1/28 | +3,57% | -18,18% | DEBOLE | 11,3 | 22,0 |
| +10,00% | 69.772 $ | 28/40 | +70,00% | -15,00% | 53.915 $ | 1/28 | +3,57% | -22,73% | DEBOLE | 11,3 | 23,0 |
| +15,00% | 72.944 $ | 24/40 | +60,00% | prezzo iniziale | 63.429 $ | 5/24 | +20,83% | -13,04% | DEBOLE | 12,6 | 25,2 |
| +15,00% | 72.944 $ | 24/40 | +60,00% | -5,00% | 60.258 $ | 3/24 | +12,50% | -17,39% | DEBOLE | 12,6 | 24,7 |
| +15,00% | 72.944 $ | 24/40 | +60,00% | -8,00% | 58.355 $ | 3/24 | +12,50% | -20,00% | DEBOLE | 12,6 | 25,3 |
| +15,00% | 72.944 $ | 24/40 | +60,00% | -10,00% | 57.086 $ | 1/24 | +4,17% | -21,74% | DEBOLE | 12,6 | 22,0 |
| +15,00% | 72.944 $ | 24/40 | +60,00% | -15,00% | 53.915 $ | 1/24 | +4,17% | -26,09% | DEBOLE | 12,6 | 23,0 |
| +20,00% | 76.115 $ | 21/40 | +52,50% | prezzo iniziale | 63.429 $ | 4/21 | +19,05% | -16,67% | DEBOLE | 12,7 | 24,5 |
| +20,00% | 76.115 $ | 21/40 | +52,50% | -5,00% | 60.258 $ | 3/21 | +14,29% | -20,83% | DEBOLE | 12,7 | 24,7 |
| +20,00% | 76.115 $ | 21/40 | +52,50% | -8,00% | 58.355 $ | 3/21 | +14,29% | -23,33% | DEBOLE | 12,7 | 25,3 |
| +20,00% | 76.115 $ | 21/40 | +52,50% | -10,00% | 57.086 $ | 1/21 | +4,76% | -25,00% | DEBOLE | 12,7 | 22,0 |
| +20,00% | 76.115 $ | 21/40 | +52,50% | -15,00% | 53.915 $ | 1/21 | +4,76% | -29,17% | DEBOLE | 12,7 | 23,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +21,43% (3/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,65 $ | 14/40 | +35,00% | +5,00% | 79,19 $ | 6/14 | +42,86% | +10,53% | BASSA | 10,8 | 18,5 |
| -5,00% | 71,65 $ | 14/40 | +35,00% | +10,00% | 82,96 $ | 3/14 | +21,43% | +15,79% | DEBOLE | 10,8 | 19,0 |
| -5,00% | 71,65 $ | 14/40 | +35,00% | +15,00% | 86,73 $ | 2/14 | +14,29% | +21,05% | DEBOLE | 10,8 | 14,5 |
| -5,00% | 71,65 $ | 14/40 | +35,00% | +20,00% | 90,50 $ | 2/14 | +14,29% | +26,32% | DEBOLE | 10,8 | 21,5 |
| -8,00% | 69,39 $ | 9/40 | +22,50% | +5,00% | 79,19 $ | 3/9 | +33,33% | +14,13% | DEBOLE | 14,3 | 21,7 |
| -8,00% | 69,39 $ | 9/40 | +22,50% | +10,00% | 82,96 $ | 2/9 | +22,22% | +19,57% | DEBOLE | 14,3 | 23,0 |
| -8,00% | 69,39 $ | 9/40 | +22,50% | +15,00% | 86,73 $ | 1/9 | +11,11% | +25,00% | DEBOLE | 14,3 | 18,0 |
| -8,00% | 69,39 $ | 9/40 | +22,50% | +20,00% | 90,50 $ | 1/9 | +11,11% | +30,43% | DEBOLE | 14,3 | 18,0 |
| -10,00% | 67,88 $ | 7/40 | +17,50% | +5,00% | 79,19 $ | 2/7 | +28,57% | +16,67% | DEBOLE | 15,0 | 18,0 |
| -10,00% | 67,88 $ | 7/40 | +17,50% | +10,00% | 82,96 $ | 1/7 | +14,29% | +22,22% | DEBOLE | 15,0 | 17,0 |
| -10,00% | 67,88 $ | 7/40 | +17,50% | +15,00% | 86,73 $ | 1/7 | +14,29% | +27,78% | DEBOLE | 15,0 | 18,0 |
| -10,00% | 67,88 $ | 7/40 | +17,50% | +20,00% | 90,50 $ | 1/7 | +14,29% | +33,33% | DEBOLE | 15,0 | 18,0 |
| -15,00% | 64,11 $ | 3/40 | +7,50% | +5,00% | 79,19 $ | 0/3 | 0,00% | +23,53% | DEBOLE | 17,7 | n/d |
| -15,00% | 64,11 $ | 3/40 | +7,50% | +10,00% | 82,96 $ | 0/3 | 0,00% | +29,41% | DEBOLE | 17,7 | n/d |
| -15,00% | 64,11 $ | 3/40 | +7,50% | +15,00% | 86,73 $ | 0/3 | 0,00% | +35,29% | DEBOLE | 17,7 | n/d |
| -15,00% | 64,11 $ | 3/40 | +7,50% | +20,00% | 90,50 $ | 0/3 | 0,00% | +41,18% | DEBOLE | 17,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,19 $ | 35/40 | +87,50% | prezzo iniziale | 75,42 $ | 10/35 | +28,57% | -4,76% | DEBOLE | 7,7 | 19,7 |
| +5,00% | 79,19 $ | 35/40 | +87,50% | -5,00% | 71,65 $ | 3/35 | +8,57% | -9,52% | DEBOLE | 7,7 | 24,0 |
| +5,00% | 79,19 $ | 35/40 | +87,50% | -8,00% | 69,39 $ | 2/35 | +5,71% | -12,38% | DEBOLE | 7,7 | 24,0 |
| +5,00% | 79,19 $ | 35/40 | +87,50% | -10,00% | 67,88 $ | 2/35 | +5,71% | -14,29% | DEBOLE | 7,7 | 24,5 |
| +5,00% | 79,19 $ | 35/40 | +87,50% | -15,00% | 64,11 $ | 1/35 | +2,86% | -19,05% | DEBOLE | 7,7 | 23,0 |
| +10,00% | 82,96 $ | 25/40 | +62,50% | prezzo iniziale | 75,42 $ | 3/25 | +12,00% | -9,09% | DEBOLE | 8,6 | 22,3 |
| +10,00% | 82,96 $ | 25/40 | +62,50% | -5,00% | 71,65 $ | 0/25 | 0,00% | -13,64% | DEBOLE | 8,6 | n/d |
| +10,00% | 82,96 $ | 25/40 | +62,50% | -8,00% | 69,39 $ | 0/25 | 0,00% | -16,36% | DEBOLE | 8,6 | n/d |
| +10,00% | 82,96 $ | 25/40 | +62,50% | -10,00% | 67,88 $ | 0/25 | 0,00% | -18,18% | DEBOLE | 8,6 | n/d |
| +10,00% | 82,96 $ | 25/40 | +62,50% | -15,00% | 64,11 $ | 0/25 | 0,00% | -22,73% | DEBOLE | 8,6 | n/d |
| +15,00% | 86,73 $ | 21/40 | +52,50% | prezzo iniziale | 75,42 $ | 2/21 | +9,52% | -13,04% | DEBOLE | 9,9 | 25,0 |
| +15,00% | 86,73 $ | 21/40 | +52,50% | -5,00% | 71,65 $ | 0/21 | 0,00% | -17,39% | DEBOLE | 9,9 | n/d |
| +15,00% | 86,73 $ | 21/40 | +52,50% | -8,00% | 69,39 $ | 0/21 | 0,00% | -20,00% | DEBOLE | 9,9 | n/d |
| +15,00% | 86,73 $ | 21/40 | +52,50% | -10,00% | 67,88 $ | 0/21 | 0,00% | -21,74% | DEBOLE | 9,9 | n/d |
| +15,00% | 86,73 $ | 21/40 | +52,50% | -15,00% | 64,11 $ | 0/21 | 0,00% | -26,09% | DEBOLE | 9,9 | n/d |
| +20,00% | 90,50 $ | 19/40 | +47,50% | prezzo iniziale | 75,42 $ | 2/19 | +10,53% | -16,67% | DEBOLE | 13,4 | 25,0 |
| +20,00% | 90,50 $ | 19/40 | +47,50% | -5,00% | 71,65 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 13,4 | n/d |
| +20,00% | 90,50 $ | 19/40 | +47,50% | -8,00% | 69,39 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 13,4 | n/d |
| +20,00% | 90,50 $ | 19/40 | +47,50% | -10,00% | 67,88 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 13,4 | n/d |
| +20,00% | 90,50 $ | 19/40 | +47,50% | -15,00% | 64,11 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 13,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +57,14% (16/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 9 poi sono scaricati a -5,00%. Percentuale: +28,12% (9/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06660 $ | 28/40 | +70,00% | +5,00% | 0,07361 $ | 16/28 | +57,14% | +10,53% | MEDIA | 8,5 | 12,8 |
| -5,00% | 0,06660 $ | 28/40 | +70,00% | +10,00% | 0,07711 $ | 16/28 | +57,14% | +15,79% | MEDIA | 8,5 | 15,4 |
| -5,00% | 0,06660 $ | 28/40 | +70,00% | +15,00% | 0,08062 $ | 13/28 | +46,43% | +21,05% | BASSA | 8,5 | 19,2 |
| -5,00% | 0,06660 $ | 28/40 | +70,00% | +20,00% | 0,08412 $ | 11/28 | +39,29% | +26,32% | BASSA | 8,5 | 19,6 |
| -8,00% | 0,06449 $ | 21/40 | +52,50% | +5,00% | 0,07361 $ | 11/21 | +52,38% | +14,13% | MEDIA | 8,4 | 13,5 |
| -8,00% | 0,06449 $ | 21/40 | +52,50% | +10,00% | 0,07711 $ | 11/21 | +52,38% | +19,57% | MEDIA | 8,4 | 16,1 |
| -8,00% | 0,06449 $ | 21/40 | +52,50% | +15,00% | 0,08062 $ | 8/21 | +38,10% | +25,00% | BASSA | 8,4 | 20,4 |
| -8,00% | 0,06449 $ | 21/40 | +52,50% | +20,00% | 0,08412 $ | 7/21 | +33,33% | +30,43% | DEBOLE | 8,4 | 21,0 |
| -10,00% | 0,06309 $ | 16/40 | +40,00% | +5,00% | 0,07361 $ | 6/16 | +37,50% | +16,67% | BASSA | 9,6 | 14,3 |
| -10,00% | 0,06309 $ | 16/40 | +40,00% | +10,00% | 0,07711 $ | 6/16 | +37,50% | +22,22% | BASSA | 9,6 | 17,2 |
| -10,00% | 0,06309 $ | 16/40 | +40,00% | +15,00% | 0,08062 $ | 4/16 | +25,00% | +27,78% | DEBOLE | 9,6 | 18,2 |
| -10,00% | 0,06309 $ | 16/40 | +40,00% | +20,00% | 0,08412 $ | 4/16 | +25,00% | +33,33% | DEBOLE | 9,6 | 19,2 |
| -15,00% | 0,05959 $ | 9/40 | +22,50% | +5,00% | 0,07361 $ | 0/9 | 0,00% | +23,53% | DEBOLE | 13,8 | n/d |
| -15,00% | 0,05959 $ | 9/40 | +22,50% | +10,00% | 0,07711 $ | 0/9 | 0,00% | +29,41% | DEBOLE | 13,8 | n/d |
| -15,00% | 0,05959 $ | 9/40 | +22,50% | +15,00% | 0,08062 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 13,8 | n/d |
| -15,00% | 0,05959 $ | 9/40 | +22,50% | +20,00% | 0,08412 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 13,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07361 $ | 34/40 | +85,00% | prezzo iniziale | 0,07010 $ | 21/34 | +61,76% | -4,76% | MEDIA | 6,6 | 13,8 |
| +5,00% | 0,07361 $ | 34/40 | +85,00% | -5,00% | 0,06660 $ | 16/34 | +47,06% | -9,52% | BASSA | 6,6 | 16,1 |
| +5,00% | 0,07361 $ | 34/40 | +85,00% | -8,00% | 0,06449 $ | 9/34 | +26,47% | -12,38% | DEBOLE | 6,6 | 14,0 |
| +5,00% | 0,07361 $ | 34/40 | +85,00% | -10,00% | 0,06309 $ | 6/34 | +17,65% | -14,29% | DEBOLE | 6,6 | 15,5 |
| +5,00% | 0,07361 $ | 34/40 | +85,00% | -15,00% | 0,05959 $ | 3/34 | +8,82% | -19,05% | DEBOLE | 6,6 | 23,0 |
| +10,00% | 0,07711 $ | 32/40 | +80,00% | prezzo iniziale | 0,07010 $ | 14/32 | +43,75% | -9,09% | BASSA | 10,1 | 17,4 |
| +10,00% | 0,07711 $ | 32/40 | +80,00% | -5,00% | 0,06660 $ | 9/32 | +28,12% | -13,64% | DEBOLE | 10,1 | 19,4 |
| +10,00% | 0,07711 $ | 32/40 | +80,00% | -8,00% | 0,06449 $ | 4/32 | +12,50% | -16,36% | DEBOLE | 10,1 | 16,2 |
| +10,00% | 0,07711 $ | 32/40 | +80,00% | -10,00% | 0,06309 $ | 2/32 | +6,25% | -18,18% | DEBOLE | 10,1 | 19,5 |
| +10,00% | 0,07711 $ | 32/40 | +80,00% | -15,00% | 0,05959 $ | 1/32 | +3,12% | -22,73% | DEBOLE | 10,1 | 25,0 |
| +15,00% | 0,08062 $ | 26/40 | +65,00% | prezzo iniziale | 0,07010 $ | 3/26 | +11,54% | -13,04% | DEBOLE | 14,7 | 18,7 |
| +15,00% | 0,08062 $ | 26/40 | +65,00% | -5,00% | 0,06660 $ | 3/26 | +11,54% | -17,39% | DEBOLE | 14,7 | 21,3 |
| +15,00% | 0,08062 $ | 26/40 | +65,00% | -8,00% | 0,06449 $ | 1/26 | +3,85% | -20,00% | DEBOLE | 14,7 | 27,0 |
| +15,00% | 0,08062 $ | 26/40 | +65,00% | -10,00% | 0,06309 $ | 1/26 | +3,85% | -21,74% | DEBOLE | 14,7 | 28,0 |
| +15,00% | 0,08062 $ | 26/40 | +65,00% | -15,00% | 0,05959 $ | 0/26 | 0,00% | -26,09% | DEBOLE | 14,7 | n/d |
| +20,00% | 0,08412 $ | 22/40 | +55,00% | prezzo iniziale | 0,07010 $ | 0/22 | 0,00% | -16,67% | DEBOLE | 18,3 | n/d |
| +20,00% | 0,08412 $ | 22/40 | +55,00% | -5,00% | 0,06660 $ | 0/22 | 0,00% | -20,83% | DEBOLE | 18,3 | n/d |
| +20,00% | 0,08412 $ | 22/40 | +55,00% | -8,00% | 0,06449 $ | 0/22 | 0,00% | -23,33% | DEBOLE | 18,3 | n/d |
| +20,00% | 0,08412 $ | 22/40 | +55,00% | -10,00% | 0,06309 $ | 0/22 | 0,00% | -25,00% | DEBOLE | 18,3 | n/d |
| +20,00% | 0,08412 $ | 22/40 | +55,00% | -15,00% | 0,05959 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 18,3 | n/d |

---
