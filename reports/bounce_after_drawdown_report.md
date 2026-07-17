# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-17 09:31:40 CEST**  
UTC: **2026-07-17 07:31:40 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.727 $ | 69.158 $ | +35,48% | +15,79% | rimbalzo debole | 69.158 $ | 59.727 $ | +20,00% | -13,64% | spike storicamente più resistente |
| SOL | 70,74 $ | 81,91 $ | +16,13% | +15,79% | rimbalzo poco frequente | 81,91 $ | 70,74 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06807 $ | 0,07881 $ | +15,15% | +15,79% | rimbalzo poco frequente | 0,07881 $ | 0,06807 $ | +33,33% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +35,48% (11/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 4 poi sono scaricati a -5,00%. Percentuale: +20,00% (4/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.727 $ | 31/40 | +77,50% | +5,00% | 66.014 $ | 14/31 | +45,16% | +10,53% | BASSA | 7,8 | 21,8 |
| -5,00% | 59.727 $ | 31/40 | +77,50% | +10,00% | 69.158 $ | 11/31 | +35,48% | +15,79% | BASSA | 7,8 | 23,6 |
| -5,00% | 59.727 $ | 31/40 | +77,50% | +15,00% | 72.301 $ | 6/31 | +19,35% | +21,05% | DEBOLE | 7,8 | 21,2 |
| -5,00% | 59.727 $ | 31/40 | +77,50% | +20,00% | 75.445 $ | 3/31 | +9,68% | +26,32% | DEBOLE | 7,8 | 24,0 |
| -8,00% | 57.841 $ | 27/40 | +67,50% | +5,00% | 66.014 $ | 9/27 | +33,33% | +14,13% | DEBOLE | 11,2 | 23,3 |
| -8,00% | 57.841 $ | 27/40 | +67,50% | +10,00% | 69.158 $ | 6/27 | +22,22% | +19,57% | DEBOLE | 11,2 | 24,8 |
| -8,00% | 57.841 $ | 27/40 | +67,50% | +15,00% | 72.301 $ | 2/27 | +7,41% | +25,00% | DEBOLE | 11,2 | 20,0 |
| -8,00% | 57.841 $ | 27/40 | +67,50% | +20,00% | 75.445 $ | 1/27 | +3,70% | +30,43% | DEBOLE | 11,2 | 16,0 |
| -10,00% | 56.584 $ | 20/40 | +50,00% | +5,00% | 66.014 $ | 5/20 | +25,00% | +16,67% | DEBOLE | 11,5 | 26,2 |
| -10,00% | 56.584 $ | 20/40 | +50,00% | +10,00% | 69.158 $ | 2/20 | +10,00% | +22,22% | DEBOLE | 11,5 | 29,0 |
| -10,00% | 56.584 $ | 20/40 | +50,00% | +15,00% | 72.301 $ | 0/20 | 0,00% | +27,78% | DEBOLE | 11,5 | n/d |
| -10,00% | 56.584 $ | 20/40 | +50,00% | +20,00% | 75.445 $ | 0/20 | 0,00% | +33,33% | DEBOLE | 11,5 | n/d |
| -15,00% | 53.440 $ | 14/40 | +35,00% | +5,00% | 66.014 $ | 1/14 | +7,14% | +23,53% | DEBOLE | 13,8 | 30,0 |
| -15,00% | 53.440 $ | 14/40 | +35,00% | +10,00% | 69.158 $ | 0/14 | 0,00% | +29,41% | DEBOLE | 13,8 | n/d |
| -15,00% | 53.440 $ | 14/40 | +35,00% | +15,00% | 72.301 $ | 0/14 | 0,00% | +35,29% | DEBOLE | 13,8 | n/d |
| -15,00% | 53.440 $ | 14/40 | +35,00% | +20,00% | 75.445 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 13,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.014 $ | 28/40 | +70,00% | prezzo iniziale | 62.871 $ | 12/28 | +42,86% | -4,76% | BASSA | 12,5 | 12,8 |
| +5,00% | 66.014 $ | 28/40 | +70,00% | -5,00% | 59.727 $ | 9/28 | +32,14% | -9,52% | DEBOLE | 12,5 | 13,1 |
| +5,00% | 66.014 $ | 28/40 | +70,00% | -8,00% | 57.841 $ | 8/28 | +28,57% | -12,38% | DEBOLE | 12,5 | 18,5 |
| +5,00% | 66.014 $ | 28/40 | +70,00% | -10,00% | 56.584 $ | 4/28 | +14,29% | -14,29% | DEBOLE | 12,5 | 20,2 |
| +5,00% | 66.014 $ | 28/40 | +70,00% | -15,00% | 53.440 $ | 2/28 | +7,14% | -19,05% | DEBOLE | 12,5 | 28,0 |
| +10,00% | 69.158 $ | 20/40 | +50,00% | prezzo iniziale | 62.871 $ | 5/20 | +25,00% | -9,09% | DEBOLE | 16,6 | 14,6 |
| +10,00% | 69.158 $ | 20/40 | +50,00% | -5,00% | 59.727 $ | 4/20 | +20,00% | -13,64% | DEBOLE | 16,6 | 15,0 |
| +10,00% | 69.158 $ | 20/40 | +50,00% | -8,00% | 57.841 $ | 3/20 | +15,00% | -16,36% | DEBOLE | 16,6 | 22,7 |
| +10,00% | 69.158 $ | 20/40 | +50,00% | -10,00% | 56.584 $ | 1/20 | +5,00% | -18,18% | DEBOLE | 16,6 | 26,0 |
| +10,00% | 69.158 $ | 20/40 | +50,00% | -15,00% | 53.440 $ | 1/20 | +5,00% | -22,73% | DEBOLE | 16,6 | 26,0 |
| +15,00% | 72.301 $ | 13/40 | +32,50% | prezzo iniziale | 62.871 $ | 3/13 | +23,08% | -13,04% | DEBOLE | 15,0 | 18,7 |
| +15,00% | 72.301 $ | 13/40 | +32,50% | -5,00% | 59.727 $ | 2/13 | +15,38% | -17,39% | DEBOLE | 15,0 | 18,0 |
| +15,00% | 72.301 $ | 13/40 | +32,50% | -8,00% | 57.841 $ | 2/13 | +15,38% | -20,00% | DEBOLE | 15,0 | 28,0 |
| +15,00% | 72.301 $ | 13/40 | +32,50% | -10,00% | 56.584 $ | 1/13 | +7,69% | -21,74% | DEBOLE | 15,0 | 26,0 |
| +15,00% | 72.301 $ | 13/40 | +32,50% | -15,00% | 53.440 $ | 1/13 | +7,69% | -26,09% | DEBOLE | 15,0 | 26,0 |
| +20,00% | 75.445 $ | 9/40 | +22,50% | prezzo iniziale | 62.871 $ | 1/9 | +11,11% | -16,67% | DEBOLE | 16,1 | 10,0 |
| +20,00% | 75.445 $ | 9/40 | +22,50% | -5,00% | 59.727 $ | 1/9 | +11,11% | -20,83% | DEBOLE | 16,1 | 10,0 |
| +20,00% | 75.445 $ | 9/40 | +22,50% | -8,00% | 57.841 $ | 1/9 | +11,11% | -23,33% | DEBOLE | 16,1 | 30,0 |
| +20,00% | 75.445 $ | 9/40 | +22,50% | -10,00% | 56.584 $ | 0/9 | 0,00% | -25,00% | DEBOLE | 16,1 | n/d |
| +20,00% | 75.445 $ | 9/40 | +22,50% | -15,00% | 53.440 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 16,1 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +16,13% (5/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 3 poi sono scaricati a -5,00%. Percentuale: +20,00% (3/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 70,74 $ | 31/40 | +77,50% | +5,00% | 78,18 $ | 14/31 | +45,16% | +10,53% | BASSA | 6,4 | 22,4 |
| -5,00% | 70,74 $ | 31/40 | +77,50% | +10,00% | 81,91 $ | 5/31 | +16,13% | +15,79% | DEBOLE | 6,4 | 18,0 |
| -5,00% | 70,74 $ | 31/40 | +77,50% | +15,00% | 85,63 $ | 3/31 | +9,68% | +21,05% | DEBOLE | 6,4 | 16,3 |
| -5,00% | 70,74 $ | 31/40 | +77,50% | +20,00% | 89,35 $ | 2/31 | +6,45% | +26,32% | DEBOLE | 6,4 | 19,0 |
| -8,00% | 68,50 $ | 26/40 | +65,00% | +5,00% | 78,18 $ | 8/26 | +30,77% | +14,13% | DEBOLE | 7,7 | 21,4 |
| -8,00% | 68,50 $ | 26/40 | +65,00% | +10,00% | 81,91 $ | 4/26 | +15,38% | +19,57% | DEBOLE | 7,7 | 19,2 |
| -8,00% | 68,50 $ | 26/40 | +65,00% | +15,00% | 85,63 $ | 2/26 | +7,69% | +25,00% | DEBOLE | 7,7 | 18,0 |
| -8,00% | 68,50 $ | 26/40 | +65,00% | +20,00% | 89,35 $ | 2/26 | +7,69% | +30,43% | DEBOLE | 7,7 | 19,0 |
| -10,00% | 67,01 $ | 20/40 | +50,00% | +5,00% | 78,18 $ | 6/20 | +30,00% | +16,67% | DEBOLE | 7,0 | 21,0 |
| -10,00% | 67,01 $ | 20/40 | +50,00% | +10,00% | 81,91 $ | 2/20 | +10,00% | +22,22% | DEBOLE | 7,0 | 16,0 |
| -10,00% | 67,01 $ | 20/40 | +50,00% | +15,00% | 85,63 $ | 1/20 | +5,00% | +27,78% | DEBOLE | 7,0 | 11,0 |
| -10,00% | 67,01 $ | 20/40 | +50,00% | +20,00% | 89,35 $ | 1/20 | +5,00% | +33,33% | DEBOLE | 7,0 | 11,0 |
| -15,00% | 63,29 $ | 13/40 | +32,50% | +5,00% | 78,18 $ | 2/13 | +15,38% | +23,53% | DEBOLE | 11,9 | 26,0 |
| -15,00% | 63,29 $ | 13/40 | +32,50% | +10,00% | 81,91 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 11,9 | n/d |
| -15,00% | 63,29 $ | 13/40 | +32,50% | +15,00% | 85,63 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 11,9 | n/d |
| -15,00% | 63,29 $ | 13/40 | +32,50% | +20,00% | 89,35 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 11,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 78,18 $ | 25/40 | +62,50% | prezzo iniziale | 74,46 $ | 11/25 | +44,00% | -4,76% | BASSA | 13,4 | 14,5 |
| +5,00% | 78,18 $ | 25/40 | +62,50% | -5,00% | 70,74 $ | 8/25 | +32,00% | -9,52% | DEBOLE | 13,4 | 15,8 |
| +5,00% | 78,18 $ | 25/40 | +62,50% | -8,00% | 68,50 $ | 7/25 | +28,00% | -12,38% | DEBOLE | 13,4 | 21,4 |
| +5,00% | 78,18 $ | 25/40 | +62,50% | -10,00% | 67,01 $ | 4/25 | +16,00% | -14,29% | DEBOLE | 13,4 | 19,0 |
| +5,00% | 78,18 $ | 25/40 | +62,50% | -15,00% | 63,29 $ | 1/25 | +4,00% | -19,05% | DEBOLE | 13,4 | 28,0 |
| +10,00% | 81,91 $ | 15/40 | +37,50% | prezzo iniziale | 74,46 $ | 3/15 | +20,00% | -9,09% | DEBOLE | 11,9 | 14,0 |
| +10,00% | 81,91 $ | 15/40 | +37,50% | -5,00% | 70,74 $ | 3/15 | +20,00% | -13,64% | DEBOLE | 11,9 | 15,7 |
| +10,00% | 81,91 $ | 15/40 | +37,50% | -8,00% | 68,50 $ | 3/15 | +20,00% | -16,36% | DEBOLE | 11,9 | 23,7 |
| +10,00% | 81,91 $ | 15/40 | +37,50% | -10,00% | 67,01 $ | 2/15 | +13,33% | -18,18% | DEBOLE | 11,9 | 21,0 |
| +10,00% | 81,91 $ | 15/40 | +37,50% | -15,00% | 63,29 $ | 1/15 | +6,67% | -22,73% | DEBOLE | 11,9 | 28,0 |
| +15,00% | 85,63 $ | 10/40 | +25,00% | prezzo iniziale | 74,46 $ | 1/10 | +10,00% | -13,04% | DEBOLE | 9,3 | 10,0 |
| +15,00% | 85,63 $ | 10/40 | +25,00% | -5,00% | 70,74 $ | 1/10 | +10,00% | -17,39% | DEBOLE | 9,3 | 10,0 |
| +15,00% | 85,63 $ | 10/40 | +25,00% | -8,00% | 68,50 $ | 1/10 | +10,00% | -20,00% | DEBOLE | 9,3 | 30,0 |
| +15,00% | 85,63 $ | 10/40 | +25,00% | -10,00% | 67,01 $ | 0/10 | 0,00% | -21,74% | DEBOLE | 9,3 | n/d |
| +15,00% | 85,63 $ | 10/40 | +25,00% | -15,00% | 63,29 $ | 0/10 | 0,00% | -26,09% | DEBOLE | 9,3 | n/d |
| +20,00% | 89,35 $ | 10/40 | +25,00% | prezzo iniziale | 74,46 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 10,6 | 10,0 |
| +20,00% | 89,35 $ | 10/40 | +25,00% | -5,00% | 70,74 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 10,6 | 10,0 |
| +20,00% | 89,35 $ | 10/40 | +25,00% | -8,00% | 68,50 $ | 1/10 | +10,00% | -23,33% | DEBOLE | 10,6 | 30,0 |
| +20,00% | 89,35 $ | 10/40 | +25,00% | -10,00% | 67,01 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 10,6 | n/d |
| +20,00% | 89,35 $ | 10/40 | +25,00% | -15,00% | 63,29 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 10,6 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +15,15% (5/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 5 poi sono scaricati a -5,00%. Percentuale: +33,33% (5/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06807 $ | 33/40 | +82,50% | +5,00% | 0,07523 $ | 6/33 | +18,18% | +10,53% | DEBOLE | 5,8 | 15,3 |
| -5,00% | 0,06807 $ | 33/40 | +82,50% | +10,00% | 0,07881 $ | 5/33 | +15,15% | +15,79% | DEBOLE | 5,8 | 16,8 |
| -5,00% | 0,06807 $ | 33/40 | +82,50% | +15,00% | 0,08240 $ | 3/33 | +9,09% | +21,05% | DEBOLE | 5,8 | 17,0 |
| -5,00% | 0,06807 $ | 33/40 | +82,50% | +20,00% | 0,08598 $ | 3/33 | +9,09% | +26,32% | DEBOLE | 5,8 | 18,7 |
| -8,00% | 0,06592 $ | 30/40 | +75,00% | +5,00% | 0,07523 $ | 4/30 | +13,33% | +14,13% | DEBOLE | 5,9 | 18,0 |
| -8,00% | 0,06592 $ | 30/40 | +75,00% | +10,00% | 0,07881 $ | 3/30 | +10,00% | +19,57% | DEBOLE | 5,9 | 14,7 |
| -8,00% | 0,06592 $ | 30/40 | +75,00% | +15,00% | 0,08240 $ | 1/30 | +3,33% | +25,00% | DEBOLE | 5,9 | 8,0 |
| -8,00% | 0,06592 $ | 30/40 | +75,00% | +20,00% | 0,08598 $ | 1/30 | +3,33% | +30,43% | DEBOLE | 5,9 | 11,0 |
| -10,00% | 0,06448 $ | 29/40 | +72,50% | +5,00% | 0,07523 $ | 3/29 | +10,34% | +16,67% | DEBOLE | 6,4 | 23,0 |
| -10,00% | 0,06448 $ | 29/40 | +72,50% | +10,00% | 0,07881 $ | 2/29 | +6,90% | +22,22% | DEBOLE | 6,4 | 20,5 |
| -10,00% | 0,06448 $ | 29/40 | +72,50% | +15,00% | 0,08240 $ | 0/29 | 0,00% | +27,78% | DEBOLE | 6,4 | n/d |
| -10,00% | 0,06448 $ | 29/40 | +72,50% | +20,00% | 0,08598 $ | 0/29 | 0,00% | +33,33% | DEBOLE | 6,4 | n/d |
| -15,00% | 0,06090 $ | 26/40 | +65,00% | +5,00% | 0,07523 $ | 1/26 | +3,85% | +23,53% | DEBOLE | 7,4 | 15,0 |
| -15,00% | 0,06090 $ | 26/40 | +65,00% | +10,00% | 0,07881 $ | 1/26 | +3,85% | +29,41% | DEBOLE | 7,4 | 15,0 |
| -15,00% | 0,06090 $ | 26/40 | +65,00% | +15,00% | 0,08240 $ | 0/26 | 0,00% | +35,29% | DEBOLE | 7,4 | n/d |
| -15,00% | 0,06090 $ | 26/40 | +65,00% | +20,00% | 0,08598 $ | 0/26 | 0,00% | +41,18% | DEBOLE | 7,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07523 $ | 18/40 | +45,00% | prezzo iniziale | 0,07165 $ | 14/18 | +77,78% | -4,76% | ALTA | 5,8 | 12,9 |
| +5,00% | 0,07523 $ | 18/40 | +45,00% | -5,00% | 0,06807 $ | 7/18 | +38,89% | -9,52% | BASSA | 5,8 | 21,0 |
| +5,00% | 0,07523 $ | 18/40 | +45,00% | -8,00% | 0,06592 $ | 5/18 | +27,78% | -12,38% | DEBOLE | 5,8 | 20,4 |
| +5,00% | 0,07523 $ | 18/40 | +45,00% | -10,00% | 0,06448 $ | 5/18 | +27,78% | -14,29% | DEBOLE | 5,8 | 21,0 |
| +5,00% | 0,07523 $ | 18/40 | +45,00% | -15,00% | 0,06090 $ | 3/18 | +16,67% | -19,05% | DEBOLE | 5,8 | 20,7 |
| +10,00% | 0,07881 $ | 15/40 | +37,50% | prezzo iniziale | 0,07165 $ | 10/15 | +66,67% | -9,09% | ALTA | 9,2 | 17,6 |
| +10,00% | 0,07881 $ | 15/40 | +37,50% | -5,00% | 0,06807 $ | 5/15 | +33,33% | -13,64% | DEBOLE | 9,2 | 23,2 |
| +10,00% | 0,07881 $ | 15/40 | +37,50% | -8,00% | 0,06592 $ | 3/15 | +20,00% | -16,36% | DEBOLE | 9,2 | 22,7 |
| +10,00% | 0,07881 $ | 15/40 | +37,50% | -10,00% | 0,06448 $ | 3/15 | +20,00% | -18,18% | DEBOLE | 9,2 | 22,7 |
| +10,00% | 0,07881 $ | 15/40 | +37,50% | -15,00% | 0,06090 $ | 2/15 | +13,33% | -22,73% | DEBOLE | 9,2 | 25,0 |
| +15,00% | 0,08240 $ | 13/40 | +32,50% | prezzo iniziale | 0,07165 $ | 8/13 | +61,54% | -13,04% | MEDIA | 9,2 | 21,2 |
| +15,00% | 0,08240 $ | 13/40 | +32,50% | -5,00% | 0,06807 $ | 4/13 | +30,77% | -17,39% | DEBOLE | 9,2 | 24,2 |
| +15,00% | 0,08240 $ | 13/40 | +32,50% | -8,00% | 0,06592 $ | 3/13 | +23,08% | -20,00% | DEBOLE | 9,2 | 22,7 |
| +15,00% | 0,08240 $ | 13/40 | +32,50% | -10,00% | 0,06448 $ | 3/13 | +23,08% | -21,74% | DEBOLE | 9,2 | 22,7 |
| +15,00% | 0,08240 $ | 13/40 | +32,50% | -15,00% | 0,06090 $ | 2/13 | +15,38% | -26,09% | DEBOLE | 9,2 | 25,0 |
| +20,00% | 0,08598 $ | 9/40 | +22,50% | prezzo iniziale | 0,07165 $ | 4/9 | +44,44% | -16,67% | BASSA | 11,4 | 23,2 |
| +20,00% | 0,08598 $ | 9/40 | +22,50% | -5,00% | 0,06807 $ | 2/9 | +22,22% | -20,83% | DEBOLE | 11,4 | 24,0 |
| +20,00% | 0,08598 $ | 9/40 | +22,50% | -8,00% | 0,06592 $ | 1/9 | +11,11% | -23,33% | DEBOLE | 11,4 | 19,0 |
| +20,00% | 0,08598 $ | 9/40 | +22,50% | -10,00% | 0,06448 $ | 1/9 | +11,11% | -25,00% | DEBOLE | 11,4 | 19,0 |
| +20,00% | 0,08598 $ | 9/40 | +22,50% | -15,00% | 0,06090 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 11,4 | n/d |

---
