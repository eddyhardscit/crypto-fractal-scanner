# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-18 07:13:52 CEST**  
UTC: **2026-07-18 05:13:52 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.695 $ | 70.278 $ | +38,71% | +15,79% | rimbalzo debole | 70.278 $ | 60.695 $ | +19,05% | -13,64% | spike storicamente più resistente |
| SOL | 71,18 $ | 82,42 $ | +16,67% | +15,79% | rimbalzo poco frequente | 82,42 $ | 71,18 $ | +18,75% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06875 $ | 0,07961 $ | +15,15% | +15,79% | rimbalzo poco frequente | 0,07961 $ | 0,06875 $ | +33,33% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +38,71% (12/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 4 poi sono scaricati a -5,00%. Percentuale: +19,05% (4/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.695 $ | 31/40 | +77,50% | +5,00% | 67.084 $ | 15/31 | +48,39% | +10,53% | BASSA | 7,9 | 21,8 |
| -5,00% | 60.695 $ | 31/40 | +77,50% | +10,00% | 70.278 $ | 12/31 | +38,71% | +15,79% | BASSA | 7,9 | 23,7 |
| -5,00% | 60.695 $ | 31/40 | +77,50% | +15,00% | 73.472 $ | 6/31 | +19,35% | +21,05% | DEBOLE | 7,9 | 21,2 |
| -5,00% | 60.695 $ | 31/40 | +77,50% | +20,00% | 76.667 $ | 3/31 | +9,68% | +26,32% | DEBOLE | 7,9 | 24,0 |
| -8,00% | 58.778 $ | 26/40 | +65,00% | +5,00% | 67.084 $ | 9/26 | +34,62% | +14,13% | DEBOLE | 11,0 | 23,3 |
| -8,00% | 58.778 $ | 26/40 | +65,00% | +10,00% | 70.278 $ | 6/26 | +23,08% | +19,57% | DEBOLE | 11,0 | 24,8 |
| -8,00% | 58.778 $ | 26/40 | +65,00% | +15,00% | 73.472 $ | 2/26 | +7,69% | +25,00% | DEBOLE | 11,0 | 20,0 |
| -8,00% | 58.778 $ | 26/40 | +65,00% | +20,00% | 76.667 $ | 1/26 | +3,85% | +30,43% | DEBOLE | 11,0 | 16,0 |
| -10,00% | 57.500 $ | 19/40 | +47,50% | +5,00% | 67.084 $ | 5/19 | +26,32% | +16,67% | DEBOLE | 11,9 | 26,2 |
| -10,00% | 57.500 $ | 19/40 | +47,50% | +10,00% | 70.278 $ | 2/19 | +10,53% | +22,22% | DEBOLE | 11,9 | 29,0 |
| -10,00% | 57.500 $ | 19/40 | +47,50% | +15,00% | 73.472 $ | 0/19 | 0,00% | +27,78% | DEBOLE | 11,9 | n/d |
| -10,00% | 57.500 $ | 19/40 | +47,50% | +20,00% | 76.667 $ | 0/19 | 0,00% | +33,33% | DEBOLE | 11,9 | n/d |
| -15,00% | 54.306 $ | 13/40 | +32,50% | +5,00% | 67.084 $ | 1/13 | +7,69% | +23,53% | DEBOLE | 14,7 | 30,0 |
| -15,00% | 54.306 $ | 13/40 | +32,50% | +10,00% | 70.278 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 14,7 | n/d |
| -15,00% | 54.306 $ | 13/40 | +32,50% | +15,00% | 73.472 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 14,7 | n/d |
| -15,00% | 54.306 $ | 13/40 | +32,50% | +20,00% | 76.667 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 14,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.084 $ | 28/40 | +70,00% | prezzo iniziale | 63.889 $ | 11/28 | +39,29% | -4,76% | BASSA | 13,1 | 13,1 |
| +5,00% | 67.084 $ | 28/40 | +70,00% | -5,00% | 60.695 $ | 8/28 | +28,57% | -9,52% | DEBOLE | 13,1 | 13,2 |
| +5,00% | 67.084 $ | 28/40 | +70,00% | -8,00% | 58.778 $ | 7/28 | +25,00% | -12,38% | DEBOLE | 13,1 | 17,3 |
| +5,00% | 67.084 $ | 28/40 | +70,00% | -10,00% | 57.500 $ | 3/28 | +10,71% | -14,29% | DEBOLE | 13,1 | 17,7 |
| +5,00% | 67.084 $ | 28/40 | +70,00% | -15,00% | 54.306 $ | 2/28 | +7,14% | -19,05% | DEBOLE | 13,1 | 28,0 |
| +10,00% | 70.278 $ | 21/40 | +52,50% | prezzo iniziale | 63.889 $ | 5/21 | +23,81% | -9,09% | DEBOLE | 16,9 | 14,6 |
| +10,00% | 70.278 $ | 21/40 | +52,50% | -5,00% | 60.695 $ | 4/21 | +19,05% | -13,64% | DEBOLE | 16,9 | 15,0 |
| +10,00% | 70.278 $ | 21/40 | +52,50% | -8,00% | 58.778 $ | 3/21 | +14,29% | -16,36% | DEBOLE | 16,9 | 22,7 |
| +10,00% | 70.278 $ | 21/40 | +52,50% | -10,00% | 57.500 $ | 1/21 | +4,76% | -18,18% | DEBOLE | 16,9 | 26,0 |
| +10,00% | 70.278 $ | 21/40 | +52,50% | -15,00% | 54.306 $ | 1/21 | +4,76% | -22,73% | DEBOLE | 16,9 | 26,0 |
| +15,00% | 73.472 $ | 13/40 | +32,50% | prezzo iniziale | 63.889 $ | 3/13 | +23,08% | -13,04% | DEBOLE | 14,9 | 18,7 |
| +15,00% | 73.472 $ | 13/40 | +32,50% | -5,00% | 60.695 $ | 2/13 | +15,38% | -17,39% | DEBOLE | 14,9 | 18,0 |
| +15,00% | 73.472 $ | 13/40 | +32,50% | -8,00% | 58.778 $ | 2/13 | +15,38% | -20,00% | DEBOLE | 14,9 | 28,0 |
| +15,00% | 73.472 $ | 13/40 | +32,50% | -10,00% | 57.500 $ | 1/13 | +7,69% | -21,74% | DEBOLE | 14,9 | 26,0 |
| +15,00% | 73.472 $ | 13/40 | +32,50% | -15,00% | 54.306 $ | 1/13 | +7,69% | -26,09% | DEBOLE | 14,9 | 26,0 |
| +20,00% | 76.667 $ | 9/40 | +22,50% | prezzo iniziale | 63.889 $ | 1/9 | +11,11% | -16,67% | DEBOLE | 16,3 | 10,0 |
| +20,00% | 76.667 $ | 9/40 | +22,50% | -5,00% | 60.695 $ | 1/9 | +11,11% | -20,83% | DEBOLE | 16,3 | 10,0 |
| +20,00% | 76.667 $ | 9/40 | +22,50% | -8,00% | 58.778 $ | 1/9 | +11,11% | -23,33% | DEBOLE | 16,3 | 30,0 |
| +20,00% | 76.667 $ | 9/40 | +22,50% | -10,00% | 57.500 $ | 0/9 | 0,00% | -25,00% | DEBOLE | 16,3 | n/d |
| +20,00% | 76.667 $ | 9/40 | +22,50% | -15,00% | 54.306 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 16,3 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +16,67% (5/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 3 poi sono scaricati a -5,00%. Percentuale: +18,75% (3/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,18 $ | 30/40 | +75,00% | +5,00% | 78,68 $ | 13/30 | +43,33% | +10,53% | BASSA | 6,4 | 22,2 |
| -5,00% | 71,18 $ | 30/40 | +75,00% | +10,00% | 82,42 $ | 5/30 | +16,67% | +15,79% | DEBOLE | 6,4 | 18,0 |
| -5,00% | 71,18 $ | 30/40 | +75,00% | +15,00% | 86,17 $ | 3/30 | +10,00% | +21,05% | DEBOLE | 6,4 | 16,3 |
| -5,00% | 71,18 $ | 30/40 | +75,00% | +20,00% | 89,92 $ | 2/30 | +6,67% | +26,32% | DEBOLE | 6,4 | 19,0 |
| -8,00% | 68,94 $ | 26/40 | +65,00% | +5,00% | 78,68 $ | 8/26 | +30,77% | +14,13% | DEBOLE | 7,7 | 21,4 |
| -8,00% | 68,94 $ | 26/40 | +65,00% | +10,00% | 82,42 $ | 4/26 | +15,38% | +19,57% | DEBOLE | 7,7 | 19,2 |
| -8,00% | 68,94 $ | 26/40 | +65,00% | +15,00% | 86,17 $ | 2/26 | +7,69% | +25,00% | DEBOLE | 7,7 | 18,0 |
| -8,00% | 68,94 $ | 26/40 | +65,00% | +20,00% | 89,92 $ | 2/26 | +7,69% | +30,43% | DEBOLE | 7,7 | 19,0 |
| -10,00% | 67,44 $ | 20/40 | +50,00% | +5,00% | 78,68 $ | 6/20 | +30,00% | +16,67% | DEBOLE | 7,0 | 21,0 |
| -10,00% | 67,44 $ | 20/40 | +50,00% | +10,00% | 82,42 $ | 2/20 | +10,00% | +22,22% | DEBOLE | 7,0 | 16,0 |
| -10,00% | 67,44 $ | 20/40 | +50,00% | +15,00% | 86,17 $ | 1/20 | +5,00% | +27,78% | DEBOLE | 7,0 | 11,0 |
| -10,00% | 67,44 $ | 20/40 | +50,00% | +20,00% | 89,92 $ | 1/20 | +5,00% | +33,33% | DEBOLE | 7,0 | 11,0 |
| -15,00% | 63,69 $ | 13/40 | +32,50% | +5,00% | 78,68 $ | 2/13 | +15,38% | +23,53% | DEBOLE | 11,9 | 26,0 |
| -15,00% | 63,69 $ | 13/40 | +32,50% | +10,00% | 82,42 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 11,9 | n/d |
| -15,00% | 63,69 $ | 13/40 | +32,50% | +15,00% | 86,17 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 11,9 | n/d |
| -15,00% | 63,69 $ | 13/40 | +32,50% | +20,00% | 89,92 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 11,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 78,68 $ | 25/40 | +62,50% | prezzo iniziale | 74,93 $ | 11/25 | +44,00% | -4,76% | BASSA | 13,2 | 14,5 |
| +5,00% | 78,68 $ | 25/40 | +62,50% | -5,00% | 71,18 $ | 8/25 | +32,00% | -9,52% | DEBOLE | 13,2 | 15,8 |
| +5,00% | 78,68 $ | 25/40 | +62,50% | -8,00% | 68,94 $ | 7/25 | +28,00% | -12,38% | DEBOLE | 13,2 | 21,4 |
| +5,00% | 78,68 $ | 25/40 | +62,50% | -10,00% | 67,44 $ | 4/25 | +16,00% | -14,29% | DEBOLE | 13,2 | 19,0 |
| +5,00% | 78,68 $ | 25/40 | +62,50% | -15,00% | 63,69 $ | 1/25 | +4,00% | -19,05% | DEBOLE | 13,2 | 28,0 |
| +10,00% | 82,42 $ | 16/40 | +40,00% | prezzo iniziale | 74,93 $ | 3/16 | +18,75% | -9,09% | DEBOLE | 12,8 | 14,0 |
| +10,00% | 82,42 $ | 16/40 | +40,00% | -5,00% | 71,18 $ | 3/16 | +18,75% | -13,64% | DEBOLE | 12,8 | 15,7 |
| +10,00% | 82,42 $ | 16/40 | +40,00% | -8,00% | 68,94 $ | 3/16 | +18,75% | -16,36% | DEBOLE | 12,8 | 23,7 |
| +10,00% | 82,42 $ | 16/40 | +40,00% | -10,00% | 67,44 $ | 2/16 | +12,50% | -18,18% | DEBOLE | 12,8 | 21,0 |
| +10,00% | 82,42 $ | 16/40 | +40,00% | -15,00% | 63,69 $ | 1/16 | +6,25% | -22,73% | DEBOLE | 12,8 | 28,0 |
| +15,00% | 86,17 $ | 10/40 | +25,00% | prezzo iniziale | 74,93 $ | 1/10 | +10,00% | -13,04% | DEBOLE | 9,7 | 10,0 |
| +15,00% | 86,17 $ | 10/40 | +25,00% | -5,00% | 71,18 $ | 1/10 | +10,00% | -17,39% | DEBOLE | 9,7 | 10,0 |
| +15,00% | 86,17 $ | 10/40 | +25,00% | -8,00% | 68,94 $ | 1/10 | +10,00% | -20,00% | DEBOLE | 9,7 | 30,0 |
| +15,00% | 86,17 $ | 10/40 | +25,00% | -10,00% | 67,44 $ | 0/10 | 0,00% | -21,74% | DEBOLE | 9,7 | n/d |
| +15,00% | 86,17 $ | 10/40 | +25,00% | -15,00% | 63,69 $ | 0/10 | 0,00% | -26,09% | DEBOLE | 9,7 | n/d |
| +20,00% | 89,92 $ | 10/40 | +25,00% | prezzo iniziale | 74,93 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 10,3 | 10,0 |
| +20,00% | 89,92 $ | 10/40 | +25,00% | -5,00% | 71,18 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 10,3 | 10,0 |
| +20,00% | 89,92 $ | 10/40 | +25,00% | -8,00% | 68,94 $ | 1/10 | +10,00% | -23,33% | DEBOLE | 10,3 | 30,0 |
| +20,00% | 89,92 $ | 10/40 | +25,00% | -10,00% | 67,44 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 10,3 | n/d |
| +20,00% | 89,92 $ | 10/40 | +25,00% | -15,00% | 63,69 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 10,3 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +15,15% (5/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 5 poi sono scaricati a -5,00%. Percentuale: +33,33% (5/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06875 $ | 33/40 | +82,50% | +5,00% | 0,07599 $ | 6/33 | +18,18% | +10,53% | DEBOLE | 5,7 | 15,3 |
| -5,00% | 0,06875 $ | 33/40 | +82,50% | +10,00% | 0,07961 $ | 5/33 | +15,15% | +15,79% | DEBOLE | 5,7 | 16,8 |
| -5,00% | 0,06875 $ | 33/40 | +82,50% | +15,00% | 0,08323 $ | 3/33 | +9,09% | +21,05% | DEBOLE | 5,7 | 17,0 |
| -5,00% | 0,06875 $ | 33/40 | +82,50% | +20,00% | 0,08684 $ | 3/33 | +9,09% | +26,32% | DEBOLE | 5,7 | 18,7 |
| -8,00% | 0,06658 $ | 30/40 | +75,00% | +5,00% | 0,07599 $ | 4/30 | +13,33% | +14,13% | DEBOLE | 5,8 | 18,0 |
| -8,00% | 0,06658 $ | 30/40 | +75,00% | +10,00% | 0,07961 $ | 3/30 | +10,00% | +19,57% | DEBOLE | 5,8 | 14,7 |
| -8,00% | 0,06658 $ | 30/40 | +75,00% | +15,00% | 0,08323 $ | 1/30 | +3,33% | +25,00% | DEBOLE | 5,8 | 8,0 |
| -8,00% | 0,06658 $ | 30/40 | +75,00% | +20,00% | 0,08684 $ | 1/30 | +3,33% | +30,43% | DEBOLE | 5,8 | 11,0 |
| -10,00% | 0,06513 $ | 29/40 | +72,50% | +5,00% | 0,07599 $ | 3/29 | +10,34% | +16,67% | DEBOLE | 6,4 | 23,0 |
| -10,00% | 0,06513 $ | 29/40 | +72,50% | +10,00% | 0,07961 $ | 2/29 | +6,90% | +22,22% | DEBOLE | 6,4 | 20,5 |
| -10,00% | 0,06513 $ | 29/40 | +72,50% | +15,00% | 0,08323 $ | 0/29 | 0,00% | +27,78% | DEBOLE | 6,4 | n/d |
| -10,00% | 0,06513 $ | 29/40 | +72,50% | +20,00% | 0,08684 $ | 0/29 | 0,00% | +33,33% | DEBOLE | 6,4 | n/d |
| -15,00% | 0,06151 $ | 26/40 | +65,00% | +5,00% | 0,07599 $ | 1/26 | +3,85% | +23,53% | DEBOLE | 7,3 | 15,0 |
| -15,00% | 0,06151 $ | 26/40 | +65,00% | +10,00% | 0,07961 $ | 1/26 | +3,85% | +29,41% | DEBOLE | 7,3 | 15,0 |
| -15,00% | 0,06151 $ | 26/40 | +65,00% | +15,00% | 0,08323 $ | 0/26 | 0,00% | +35,29% | DEBOLE | 7,3 | n/d |
| -15,00% | 0,06151 $ | 26/40 | +65,00% | +20,00% | 0,08684 $ | 0/26 | 0,00% | +41,18% | DEBOLE | 7,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07599 $ | 18/40 | +45,00% | prezzo iniziale | 0,07237 $ | 14/18 | +77,78% | -4,76% | ALTA | 5,7 | 12,6 |
| +5,00% | 0,07599 $ | 18/40 | +45,00% | -5,00% | 0,06875 $ | 7/18 | +38,89% | -9,52% | BASSA | 5,7 | 20,4 |
| +5,00% | 0,07599 $ | 18/40 | +45,00% | -8,00% | 0,06658 $ | 5/18 | +27,78% | -12,38% | DEBOLE | 5,7 | 20,2 |
| +5,00% | 0,07599 $ | 18/40 | +45,00% | -10,00% | 0,06513 $ | 5/18 | +27,78% | -14,29% | DEBOLE | 5,7 | 20,8 |
| +5,00% | 0,07599 $ | 18/40 | +45,00% | -15,00% | 0,06151 $ | 3/18 | +16,67% | -19,05% | DEBOLE | 5,7 | 20,3 |
| +10,00% | 0,07961 $ | 15/40 | +37,50% | prezzo iniziale | 0,07237 $ | 10/15 | +66,67% | -9,09% | ALTA | 9,2 | 17,2 |
| +10,00% | 0,07961 $ | 15/40 | +37,50% | -5,00% | 0,06875 $ | 5/15 | +33,33% | -13,64% | DEBOLE | 9,2 | 22,4 |
| +10,00% | 0,07961 $ | 15/40 | +37,50% | -8,00% | 0,06658 $ | 3/15 | +20,00% | -16,36% | DEBOLE | 9,2 | 22,3 |
| +10,00% | 0,07961 $ | 15/40 | +37,50% | -10,00% | 0,06513 $ | 3/15 | +20,00% | -18,18% | DEBOLE | 9,2 | 22,3 |
| +10,00% | 0,07961 $ | 15/40 | +37,50% | -15,00% | 0,06151 $ | 2/15 | +13,33% | -22,73% | DEBOLE | 9,2 | 24,5 |
| +15,00% | 0,08323 $ | 12/40 | +30,00% | prezzo iniziale | 0,07237 $ | 7/12 | +58,33% | -13,04% | MEDIA | 9,3 | 20,7 |
| +15,00% | 0,08323 $ | 12/40 | +30,00% | -5,00% | 0,06875 $ | 3/12 | +25,00% | -17,39% | DEBOLE | 9,3 | 23,0 |
| +15,00% | 0,08323 $ | 12/40 | +30,00% | -8,00% | 0,06658 $ | 2/12 | +16,67% | -20,00% | DEBOLE | 9,3 | 20,0 |
| +15,00% | 0,08323 $ | 12/40 | +30,00% | -10,00% | 0,06513 $ | 2/12 | +16,67% | -21,74% | DEBOLE | 9,3 | 20,0 |
| +15,00% | 0,08323 $ | 12/40 | +30,00% | -15,00% | 0,06151 $ | 1/12 | +8,33% | -26,09% | DEBOLE | 9,3 | 21,0 |
| +20,00% | 0,08684 $ | 9/40 | +22,50% | prezzo iniziale | 0,07237 $ | 4/9 | +44,44% | -16,67% | BASSA | 11,4 | 23,2 |
| +20,00% | 0,08684 $ | 9/40 | +22,50% | -5,00% | 0,06875 $ | 2/9 | +22,22% | -20,83% | DEBOLE | 11,4 | 24,0 |
| +20,00% | 0,08684 $ | 9/40 | +22,50% | -8,00% | 0,06658 $ | 1/9 | +11,11% | -23,33% | DEBOLE | 11,4 | 19,0 |
| +20,00% | 0,08684 $ | 9/40 | +22,50% | -10,00% | 0,06513 $ | 1/9 | +11,11% | -25,00% | DEBOLE | 11,4 | 19,0 |
| +20,00% | 0,08684 $ | 9/40 | +22,50% | -15,00% | 0,06151 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 11,4 | n/d |

---
