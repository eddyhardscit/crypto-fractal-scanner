# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-09 03:14:52 CEST**  
UTC: **2026-07-09 01:14:52 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.275 $ | 68.634 $ | +33,33% | +15,79% | rimbalzo poco frequente | 68.634 $ | 59.275 $ | +26,92% | -13,64% | spike storicamente più resistente |
| SOL | 74,47 $ | 86,23 $ | +10,71% | +15,79% | rimbalzo poco frequente | 86,23 $ | 74,47 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06905 $ | 0,07995 $ | +16,22% | +15,79% | rimbalzo poco frequente | 0,07995 $ | 0,06905 $ | +64,29% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (7/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 7 poi sono scaricati a -5,00%. Percentuale: +26,92% (7/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.275 $ | 21/40 | +52,50% | +5,00% | 65.514 $ | 8/21 | +38,10% | +10,53% | BASSA | 12,0 | 12,2 |
| -5,00% | 59.275 $ | 21/40 | +52,50% | +10,00% | 68.634 $ | 7/21 | +33,33% | +15,79% | DEBOLE | 12,0 | 14,9 |
| -5,00% | 59.275 $ | 21/40 | +52,50% | +15,00% | 71.754 $ | 5/21 | +23,81% | +21,05% | DEBOLE | 12,0 | 15,8 |
| -5,00% | 59.275 $ | 21/40 | +52,50% | +20,00% | 74.873 $ | 3/21 | +14,29% | +26,32% | DEBOLE | 12,0 | 16,0 |
| -8,00% | 57.403 $ | 13/40 | +32,50% | +5,00% | 65.514 $ | 4/13 | +30,77% | +14,13% | DEBOLE | 12,9 | 10,2 |
| -8,00% | 57.403 $ | 13/40 | +32,50% | +10,00% | 68.634 $ | 4/13 | +30,77% | +19,57% | DEBOLE | 12,9 | 13,2 |
| -8,00% | 57.403 $ | 13/40 | +32,50% | +15,00% | 71.754 $ | 3/13 | +23,08% | +25,00% | DEBOLE | 12,9 | 17,0 |
| -8,00% | 57.403 $ | 13/40 | +32,50% | +20,00% | 74.873 $ | 2/13 | +15,38% | +30,43% | DEBOLE | 12,9 | 18,5 |
| -10,00% | 56.155 $ | 9/40 | +22,50% | +5,00% | 65.514 $ | 2/9 | +22,22% | +16,67% | DEBOLE | 13,7 | 14,5 |
| -10,00% | 56.155 $ | 9/40 | +22,50% | +10,00% | 68.634 $ | 2/9 | +22,22% | +22,22% | DEBOLE | 13,7 | 20,0 |
| -10,00% | 56.155 $ | 9/40 | +22,50% | +15,00% | 71.754 $ | 2/9 | +22,22% | +27,78% | DEBOLE | 13,7 | 20,5 |
| -10,00% | 56.155 $ | 9/40 | +22,50% | +20,00% | 74.873 $ | 1/9 | +11,11% | +33,33% | DEBOLE | 13,7 | 26,0 |
| -15,00% | 53.035 $ | 7/40 | +17,50% | +5,00% | 65.514 $ | 2/7 | +28,57% | +23,53% | DEBOLE | 12,6 | 14,5 |
| -15,00% | 53.035 $ | 7/40 | +17,50% | +10,00% | 68.634 $ | 2/7 | +28,57% | +29,41% | DEBOLE | 12,6 | 20,0 |
| -15,00% | 53.035 $ | 7/40 | +17,50% | +15,00% | 71.754 $ | 2/7 | +28,57% | +35,29% | DEBOLE | 12,6 | 20,5 |
| -15,00% | 53.035 $ | 7/40 | +17,50% | +20,00% | 74.873 $ | 1/7 | +14,29% | +41,18% | DEBOLE | 12,6 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.514 $ | 36/40 | +90,00% | prezzo iniziale | 62.394 $ | 23/36 | +63,89% | -4,76% | MEDIA | 4,4 | 14,0 |
| +5,00% | 65.514 $ | 36/40 | +90,00% | -5,00% | 59.275 $ | 15/36 | +41,67% | -9,52% | BASSA | 4,4 | 16,2 |
| +5,00% | 65.514 $ | 36/40 | +90,00% | -8,00% | 57.403 $ | 10/36 | +27,78% | -12,38% | DEBOLE | 4,4 | 18,0 |
| +5,00% | 65.514 $ | 36/40 | +90,00% | -10,00% | 56.155 $ | 6/36 | +16,67% | -14,29% | DEBOLE | 4,4 | 17,8 |
| +5,00% | 65.514 $ | 36/40 | +90,00% | -15,00% | 53.035 $ | 4/36 | +11,11% | -19,05% | DEBOLE | 4,4 | 17,0 |
| +10,00% | 68.634 $ | 26/40 | +65,00% | prezzo iniziale | 62.394 $ | 11/26 | +42,31% | -9,09% | BASSA | 8,9 | 17,5 |
| +10,00% | 68.634 $ | 26/40 | +65,00% | -5,00% | 59.275 $ | 7/26 | +26,92% | -13,64% | DEBOLE | 8,9 | 17,1 |
| +10,00% | 68.634 $ | 26/40 | +65,00% | -8,00% | 57.403 $ | 5/26 | +19,23% | -16,36% | DEBOLE | 8,9 | 19,4 |
| +10,00% | 68.634 $ | 26/40 | +65,00% | -10,00% | 56.155 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 8,9 | 22,0 |
| +10,00% | 68.634 $ | 26/40 | +65,00% | -15,00% | 53.035 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 8,9 | 24,0 |
| +15,00% | 71.754 $ | 20/40 | +50,00% | prezzo iniziale | 62.394 $ | 6/20 | +30,00% | -13,04% | DEBOLE | 12,2 | 20,3 |
| +15,00% | 71.754 $ | 20/40 | +50,00% | -5,00% | 59.275 $ | 4/20 | +20,00% | -17,39% | DEBOLE | 12,2 | 22,2 |
| +15,00% | 71.754 $ | 20/40 | +50,00% | -8,00% | 57.403 $ | 2/20 | +10,00% | -20,00% | DEBOLE | 12,2 | 20,5 |
| +15,00% | 71.754 $ | 20/40 | +50,00% | -10,00% | 56.155 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 12,2 | 21,0 |
| +15,00% | 71.754 $ | 20/40 | +50,00% | -15,00% | 53.035 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 12,2 | n/d |
| +20,00% | 74.873 $ | 13/40 | +32,50% | prezzo iniziale | 62.394 $ | 1/13 | +7,69% | -16,67% | DEBOLE | 13,1 | 16,0 |
| +20,00% | 74.873 $ | 13/40 | +32,50% | -5,00% | 59.275 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 13,1 | 28,0 |
| +20,00% | 74.873 $ | 13/40 | +32,50% | -8,00% | 57.403 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 13,1 | n/d |
| +20,00% | 74.873 $ | 13/40 | +32,50% | -10,00% | 56.155 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 13,1 | n/d |
| +20,00% | 74.873 $ | 13/40 | +32,50% | -15,00% | 53.035 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 13,1 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +10,71% (3/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 3 poi sono scaricati a -5,00%. Percentuale: +20,00% (3/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 74,47 $ | 28/40 | +70,00% | +5,00% | 82,31 $ | 6/28 | +21,43% | +10,53% | DEBOLE | 7,2 | 13,7 |
| -5,00% | 74,47 $ | 28/40 | +70,00% | +10,00% | 86,23 $ | 3/28 | +10,71% | +15,79% | DEBOLE | 7,2 | 11,7 |
| -5,00% | 74,47 $ | 28/40 | +70,00% | +15,00% | 90,15 $ | 2/28 | +7,14% | +21,05% | DEBOLE | 7,2 | 11,5 |
| -5,00% | 74,47 $ | 28/40 | +70,00% | +20,00% | 94,07 $ | 1/28 | +3,57% | +26,32% | DEBOLE | 7,2 | 10,0 |
| -8,00% | 72,12 $ | 25/40 | +62,50% | +5,00% | 82,31 $ | 3/25 | +12,00% | +14,13% | DEBOLE | 10,6 | 19,3 |
| -8,00% | 72,12 $ | 25/40 | +62,50% | +10,00% | 86,23 $ | 2/25 | +8,00% | +19,57% | DEBOLE | 10,6 | 15,0 |
| -8,00% | 72,12 $ | 25/40 | +62,50% | +15,00% | 90,15 $ | 1/25 | +4,00% | +25,00% | DEBOLE | 10,6 | 15,0 |
| -8,00% | 72,12 $ | 25/40 | +62,50% | +20,00% | 94,07 $ | 0/25 | 0,00% | +30,43% | DEBOLE | 10,6 | n/d |
| -10,00% | 70,55 $ | 23/40 | +57,50% | +5,00% | 82,31 $ | 2/23 | +8,70% | +16,67% | DEBOLE | 11,1 | 14,0 |
| -10,00% | 70,55 $ | 23/40 | +57,50% | +10,00% | 86,23 $ | 2/23 | +8,70% | +22,22% | DEBOLE | 11,1 | 15,0 |
| -10,00% | 70,55 $ | 23/40 | +57,50% | +15,00% | 90,15 $ | 1/23 | +4,35% | +27,78% | DEBOLE | 11,1 | 15,0 |
| -10,00% | 70,55 $ | 23/40 | +57,50% | +20,00% | 94,07 $ | 0/23 | 0,00% | +33,33% | DEBOLE | 11,1 | n/d |
| -15,00% | 66,63 $ | 17/40 | +42,50% | +5,00% | 82,31 $ | 2/17 | +11,76% | +23,53% | DEBOLE | 12,9 | 14,0 |
| -15,00% | 66,63 $ | 17/40 | +42,50% | +10,00% | 86,23 $ | 2/17 | +11,76% | +29,41% | DEBOLE | 12,9 | 15,0 |
| -15,00% | 66,63 $ | 17/40 | +42,50% | +15,00% | 90,15 $ | 1/17 | +5,88% | +35,29% | DEBOLE | 12,9 | 15,0 |
| -15,00% | 66,63 $ | 17/40 | +42,50% | +20,00% | 94,07 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 12,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 82,31 $ | 25/40 | +62,50% | prezzo iniziale | 78,39 $ | 16/25 | +64,00% | -4,76% | MEDIA | 3,9 | 11,4 |
| +5,00% | 82,31 $ | 25/40 | +62,50% | -5,00% | 74,47 $ | 12/25 | +48,00% | -9,52% | BASSA | 3,9 | 12,7 |
| +5,00% | 82,31 $ | 25/40 | +62,50% | -8,00% | 72,12 $ | 12/25 | +48,00% | -12,38% | BASSA | 3,9 | 16,0 |
| +5,00% | 82,31 $ | 25/40 | +62,50% | -10,00% | 70,55 $ | 9/25 | +36,00% | -14,29% | BASSA | 3,9 | 14,9 |
| +5,00% | 82,31 $ | 25/40 | +62,50% | -15,00% | 66,63 $ | 5/25 | +20,00% | -19,05% | DEBOLE | 3,9 | 16,2 |
| +10,00% | 86,23 $ | 15/40 | +37,50% | prezzo iniziale | 78,39 $ | 5/15 | +33,33% | -9,09% | DEBOLE | 6,3 | 16,2 |
| +10,00% | 86,23 $ | 15/40 | +37,50% | -5,00% | 74,47 $ | 3/15 | +20,00% | -13,64% | DEBOLE | 6,3 | 17,0 |
| +10,00% | 86,23 $ | 15/40 | +37,50% | -8,00% | 72,12 $ | 3/15 | +20,00% | -16,36% | DEBOLE | 6,3 | 17,0 |
| +10,00% | 86,23 $ | 15/40 | +37,50% | -10,00% | 70,55 $ | 1/15 | +6,67% | -18,18% | DEBOLE | 6,3 | 14,0 |
| +10,00% | 86,23 $ | 15/40 | +37,50% | -15,00% | 66,63 $ | 1/15 | +6,67% | -22,73% | DEBOLE | 6,3 | 14,0 |
| +15,00% | 90,15 $ | 12/40 | +30,00% | prezzo iniziale | 78,39 $ | 3/12 | +25,00% | -13,04% | DEBOLE | 9,7 | 15,3 |
| +15,00% | 90,15 $ | 12/40 | +30,00% | -5,00% | 74,47 $ | 2/12 | +16,67% | -17,39% | DEBOLE | 9,7 | 18,5 |
| +15,00% | 90,15 $ | 12/40 | +30,00% | -8,00% | 72,12 $ | 2/12 | +16,67% | -20,00% | DEBOLE | 9,7 | 18,5 |
| +15,00% | 90,15 $ | 12/40 | +30,00% | -10,00% | 70,55 $ | 0/12 | 0,00% | -21,74% | DEBOLE | 9,7 | n/d |
| +15,00% | 90,15 $ | 12/40 | +30,00% | -15,00% | 66,63 $ | 0/12 | 0,00% | -26,09% | DEBOLE | 9,7 | n/d |
| +20,00% | 94,07 $ | 9/40 | +22,50% | prezzo iniziale | 78,39 $ | 0/9 | 0,00% | -16,67% | DEBOLE | 12,2 | n/d |
| +20,00% | 94,07 $ | 9/40 | +22,50% | -5,00% | 74,47 $ | 0/9 | 0,00% | -20,83% | DEBOLE | 12,2 | n/d |
| +20,00% | 94,07 $ | 9/40 | +22,50% | -8,00% | 72,12 $ | 0/9 | 0,00% | -23,33% | DEBOLE | 12,2 | n/d |
| +20,00% | 94,07 $ | 9/40 | +22,50% | -10,00% | 70,55 $ | 0/9 | 0,00% | -25,00% | DEBOLE | 12,2 | n/d |
| +20,00% | 94,07 $ | 9/40 | +22,50% | -15,00% | 66,63 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 12,2 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 37 prima sono scesi a -5,00%. Tra quei 37, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +16,22% (6/37). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 14 prima sono saliti a +10,00%. Tra quei 14, 9 poi sono scaricati a -5,00%. Percentuale: +64,29% (9/14). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06905 $ | 37/40 | +92,50% | +5,00% | 0,07631 $ | 9/37 | +24,32% | +10,53% | DEBOLE | 5,9 | 15,2 |
| -5,00% | 0,06905 $ | 37/40 | +92,50% | +10,00% | 0,07995 $ | 6/37 | +16,22% | +15,79% | DEBOLE | 5,9 | 13,7 |
| -5,00% | 0,06905 $ | 37/40 | +92,50% | +15,00% | 0,08358 $ | 6/37 | +16,22% | +21,05% | DEBOLE | 5,9 | 16,0 |
| -5,00% | 0,06905 $ | 37/40 | +92,50% | +20,00% | 0,08722 $ | 6/37 | +16,22% | +26,32% | DEBOLE | 5,9 | 16,8 |
| -8,00% | 0,06687 $ | 35/40 | +87,50% | +5,00% | 0,07631 $ | 7/35 | +20,00% | +14,13% | DEBOLE | 7,9 | 17,4 |
| -8,00% | 0,06687 $ | 35/40 | +87,50% | +10,00% | 0,07995 $ | 4/35 | +11,43% | +19,57% | DEBOLE | 7,9 | 16,2 |
| -8,00% | 0,06687 $ | 35/40 | +87,50% | +15,00% | 0,08358 $ | 4/35 | +11,43% | +25,00% | DEBOLE | 7,9 | 19,2 |
| -8,00% | 0,06687 $ | 35/40 | +87,50% | +20,00% | 0,08722 $ | 4/35 | +11,43% | +30,43% | DEBOLE | 7,9 | 20,0 |
| -10,00% | 0,06541 $ | 33/40 | +82,50% | +5,00% | 0,07631 $ | 5/33 | +15,15% | +16,67% | DEBOLE | 8,5 | 17,6 |
| -10,00% | 0,06541 $ | 33/40 | +82,50% | +10,00% | 0,07995 $ | 2/33 | +6,06% | +22,22% | DEBOLE | 8,5 | 15,0 |
| -10,00% | 0,06541 $ | 33/40 | +82,50% | +15,00% | 0,08358 $ | 2/33 | +6,06% | +27,78% | DEBOLE | 8,5 | 15,5 |
| -10,00% | 0,06541 $ | 33/40 | +82,50% | +20,00% | 0,08722 $ | 2/33 | +6,06% | +33,33% | DEBOLE | 8,5 | 15,5 |
| -15,00% | 0,06178 $ | 31/40 | +77,50% | +5,00% | 0,07631 $ | 4/31 | +12,90% | +23,53% | DEBOLE | 11,1 | 15,8 |
| -15,00% | 0,06178 $ | 31/40 | +77,50% | +10,00% | 0,07995 $ | 2/31 | +6,45% | +29,41% | DEBOLE | 11,1 | 15,0 |
| -15,00% | 0,06178 $ | 31/40 | +77,50% | +15,00% | 0,08358 $ | 2/31 | +6,45% | +35,29% | DEBOLE | 11,1 | 15,5 |
| -15,00% | 0,06178 $ | 31/40 | +77,50% | +20,00% | 0,08722 $ | 2/31 | +6,45% | +41,18% | DEBOLE | 11,1 | 15,5 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07631 $ | 19/40 | +47,50% | prezzo iniziale | 0,07268 $ | 16/19 | +84,21% | -4,76% | ALTA | 8,0 | 12,1 |
| +5,00% | 0,07631 $ | 19/40 | +47,50% | -5,00% | 0,06905 $ | 14/19 | +73,68% | -9,52% | ALTA | 8,0 | 15,2 |
| +5,00% | 0,07631 $ | 19/40 | +47,50% | -8,00% | 0,06687 $ | 12/19 | +63,16% | -12,38% | MEDIA | 8,0 | 14,8 |
| +5,00% | 0,07631 $ | 19/40 | +47,50% | -10,00% | 0,06541 $ | 11/19 | +57,89% | -14,29% | MEDIA | 8,0 | 15,5 |
| +5,00% | 0,07631 $ | 19/40 | +47,50% | -15,00% | 0,06178 $ | 10/19 | +52,63% | -19,05% | MEDIA | 8,0 | 15,2 |
| +10,00% | 0,07995 $ | 14/40 | +35,00% | prezzo iniziale | 0,07268 $ | 9/14 | +64,29% | -9,09% | MEDIA | 9,6 | 12,8 |
| +10,00% | 0,07995 $ | 14/40 | +35,00% | -5,00% | 0,06905 $ | 9/14 | +64,29% | -13,64% | MEDIA | 9,6 | 13,9 |
| +10,00% | 0,07995 $ | 14/40 | +35,00% | -8,00% | 0,06687 $ | 8/14 | +57,14% | -16,36% | MEDIA | 9,6 | 14,4 |
| +10,00% | 0,07995 $ | 14/40 | +35,00% | -10,00% | 0,06541 $ | 7/14 | +50,00% | -18,18% | MEDIA | 9,6 | 15,3 |
| +10,00% | 0,07995 $ | 14/40 | +35,00% | -15,00% | 0,06178 $ | 7/14 | +50,00% | -22,73% | MEDIA | 9,6 | 16,4 |
| +15,00% | 0,08358 $ | 8/40 | +20,00% | prezzo iniziale | 0,07268 $ | 3/8 | +37,50% | -13,04% | BASSA | 13,0 | 13,0 |
| +15,00% | 0,08358 $ | 8/40 | +20,00% | -5,00% | 0,06905 $ | 3/8 | +37,50% | -17,39% | BASSA | 13,0 | 13,3 |
| +15,00% | 0,08358 $ | 8/40 | +20,00% | -8,00% | 0,06687 $ | 3/8 | +37,50% | -20,00% | BASSA | 13,0 | 13,7 |
| +15,00% | 0,08358 $ | 8/40 | +20,00% | -10,00% | 0,06541 $ | 2/8 | +25,00% | -21,74% | DEBOLE | 13,0 | 16,0 |
| +15,00% | 0,08358 $ | 8/40 | +20,00% | -15,00% | 0,06178 $ | 2/8 | +25,00% | -26,09% | DEBOLE | 13,0 | 18,0 |
| +20,00% | 0,08722 $ | 7/40 | +17,50% | prezzo iniziale | 0,07268 $ | 3/7 | +42,86% | -16,67% | BASSA | 17,0 | 19,0 |
| +20,00% | 0,08722 $ | 7/40 | +17,50% | -5,00% | 0,06905 $ | 2/7 | +28,57% | -20,83% | DEBOLE | 17,0 | 15,5 |
| +20,00% | 0,08722 $ | 7/40 | +17,50% | -8,00% | 0,06687 $ | 2/7 | +28,57% | -23,33% | DEBOLE | 17,0 | 16,0 |
| +20,00% | 0,08722 $ | 7/40 | +17,50% | -10,00% | 0,06541 $ | 2/7 | +28,57% | -25,00% | DEBOLE | 17,0 | 16,0 |
| +20,00% | 0,08722 $ | 7/40 | +17,50% | -15,00% | 0,06178 $ | 2/7 | +28,57% | -29,17% | DEBOLE | 17,0 | 18,0 |

---
