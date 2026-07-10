# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-10 13:49:06 CEST**  
UTC: **2026-07-10 11:49:06 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.197 $ | 70.860 $ | 0,00% | +15,79% | rimbalzo poco frequente | 70.860 $ | 61.197 $ | +8,70% | -13,64% | spike storicamente più resistente |
| SOL | 75,35 $ | 87,25 $ | +10,71% | +15,79% | rimbalzo poco frequente | 87,25 $ | 75,35 $ | +27,78% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07051 $ | 0,08164 $ | +10,81% | +15,79% | rimbalzo poco frequente | 0,08164 $ | 0,07051 $ | +61,54% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 0 poi sono rimbalzati fino a +10,00%. Percentuale: 0,00% (0/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 2 poi sono scaricati a -5,00%. Percentuale: +8,70% (2/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.197 $ | 14/40 | +35,00% | +5,00% | 67.639 $ | 3/14 | +21,43% | +10,53% | DEBOLE | 10,5 | 29,7 |
| -5,00% | 61.197 $ | 14/40 | +35,00% | +10,00% | 70.860 $ | 0/14 | 0,00% | +15,79% | DEBOLE | 10,5 | n/d |
| -5,00% | 61.197 $ | 14/40 | +35,00% | +15,00% | 74.081 $ | 0/14 | 0,00% | +21,05% | DEBOLE | 10,5 | n/d |
| -5,00% | 61.197 $ | 14/40 | +35,00% | +20,00% | 77.302 $ | 0/14 | 0,00% | +26,32% | DEBOLE | 10,5 | n/d |
| -8,00% | 59.265 $ | 11/40 | +27,50% | +5,00% | 67.639 $ | 2/11 | +18,18% | +14,13% | DEBOLE | 13,5 | 30,0 |
| -8,00% | 59.265 $ | 11/40 | +27,50% | +10,00% | 70.860 $ | 0/11 | 0,00% | +19,57% | DEBOLE | 13,5 | n/d |
| -8,00% | 59.265 $ | 11/40 | +27,50% | +15,00% | 74.081 $ | 0/11 | 0,00% | +25,00% | DEBOLE | 13,5 | n/d |
| -8,00% | 59.265 $ | 11/40 | +27,50% | +20,00% | 77.302 $ | 0/11 | 0,00% | +30,43% | DEBOLE | 13,5 | n/d |
| -10,00% | 57.976 $ | 9/40 | +22,50% | +5,00% | 67.639 $ | 2/9 | +22,22% | +16,67% | DEBOLE | 14,6 | 30,0 |
| -10,00% | 57.976 $ | 9/40 | +22,50% | +10,00% | 70.860 $ | 0/9 | 0,00% | +22,22% | DEBOLE | 14,6 | n/d |
| -10,00% | 57.976 $ | 9/40 | +22,50% | +15,00% | 74.081 $ | 0/9 | 0,00% | +27,78% | DEBOLE | 14,6 | n/d |
| -10,00% | 57.976 $ | 9/40 | +22,50% | +20,00% | 77.302 $ | 0/9 | 0,00% | +33,33% | DEBOLE | 14,6 | n/d |
| -15,00% | 54.755 $ | 5/40 | +12,50% | +5,00% | 67.639 $ | 0/5 | 0,00% | +23,53% | DEBOLE | 11,8 | n/d |
| -15,00% | 54.755 $ | 5/40 | +12,50% | +10,00% | 70.860 $ | 0/5 | 0,00% | +29,41% | DEBOLE | 11,8 | n/d |
| -15,00% | 54.755 $ | 5/40 | +12,50% | +15,00% | 74.081 $ | 0/5 | 0,00% | +35,29% | DEBOLE | 11,8 | n/d |
| -15,00% | 54.755 $ | 5/40 | +12,50% | +20,00% | 77.302 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 11,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.639 $ | 34/40 | +85,00% | prezzo iniziale | 64.418 $ | 14/34 | +41,18% | -4,76% | BASSA | 5,3 | 13,0 |
| +5,00% | 67.639 $ | 34/40 | +85,00% | -5,00% | 61.197 $ | 6/34 | +17,65% | -9,52% | DEBOLE | 5,3 | 17,8 |
| +5,00% | 67.639 $ | 34/40 | +85,00% | -8,00% | 59.265 $ | 4/34 | +11,76% | -12,38% | DEBOLE | 5,3 | 21,0 |
| +5,00% | 67.639 $ | 34/40 | +85,00% | -10,00% | 57.976 $ | 3/34 | +8,82% | -14,29% | DEBOLE | 5,3 | 24,7 |
| +5,00% | 67.639 $ | 34/40 | +85,00% | -15,00% | 54.755 $ | 1/34 | +2,94% | -19,05% | DEBOLE | 5,3 | 24,0 |
| +10,00% | 70.860 $ | 23/40 | +57,50% | prezzo iniziale | 64.418 $ | 4/23 | +17,39% | -9,09% | DEBOLE | 5,6 | 16,8 |
| +10,00% | 70.860 $ | 23/40 | +57,50% | -5,00% | 61.197 $ | 2/23 | +8,70% | -13,64% | DEBOLE | 5,6 | 19,5 |
| +10,00% | 70.860 $ | 23/40 | +57,50% | -8,00% | 59.265 $ | 1/23 | +4,35% | -16,36% | DEBOLE | 5,6 | 23,0 |
| +10,00% | 70.860 $ | 23/40 | +57,50% | -10,00% | 57.976 $ | 1/23 | +4,35% | -18,18% | DEBOLE | 5,6 | 23,0 |
| +10,00% | 70.860 $ | 23/40 | +57,50% | -15,00% | 54.755 $ | 1/23 | +4,35% | -22,73% | DEBOLE | 5,6 | 24,0 |
| +15,00% | 74.081 $ | 20/40 | +50,00% | prezzo iniziale | 64.418 $ | 2/20 | +10,00% | -13,04% | DEBOLE | 9,8 | 17,0 |
| +15,00% | 74.081 $ | 20/40 | +50,00% | -5,00% | 61.197 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 9,8 | n/d |
| +15,00% | 74.081 $ | 20/40 | +50,00% | -8,00% | 59.265 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 9,8 | n/d |
| +15,00% | 74.081 $ | 20/40 | +50,00% | -10,00% | 57.976 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 9,8 | n/d |
| +15,00% | 74.081 $ | 20/40 | +50,00% | -15,00% | 54.755 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 9,8 | n/d |
| +20,00% | 77.302 $ | 18/40 | +45,00% | prezzo iniziale | 64.418 $ | 1/18 | +5,56% | -16,67% | DEBOLE | 11,7 | 22,0 |
| +20,00% | 77.302 $ | 18/40 | +45,00% | -5,00% | 61.197 $ | 0/18 | 0,00% | -20,83% | DEBOLE | 11,7 | n/d |
| +20,00% | 77.302 $ | 18/40 | +45,00% | -8,00% | 59.265 $ | 0/18 | 0,00% | -23,33% | DEBOLE | 11,7 | n/d |
| +20,00% | 77.302 $ | 18/40 | +45,00% | -10,00% | 57.976 $ | 0/18 | 0,00% | -25,00% | DEBOLE | 11,7 | n/d |
| +20,00% | 77.302 $ | 18/40 | +45,00% | -15,00% | 54.755 $ | 0/18 | 0,00% | -29,17% | DEBOLE | 11,7 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +10,71% (3/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 18 prima sono saliti a +10,00%. Tra quei 18, 5 poi sono scaricati a -5,00%. Percentuale: +27,78% (5/18). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 75,35 $ | 28/40 | +70,00% | +5,00% | 83,29 $ | 4/28 | +14,29% | +10,53% | DEBOLE | 6,9 | 14,5 |
| -5,00% | 75,35 $ | 28/40 | +70,00% | +10,00% | 87,25 $ | 3/28 | +10,71% | +15,79% | DEBOLE | 6,9 | 10,0 |
| -5,00% | 75,35 $ | 28/40 | +70,00% | +15,00% | 91,22 $ | 1/28 | +3,57% | +21,05% | DEBOLE | 6,9 | 8,0 |
| -5,00% | 75,35 $ | 28/40 | +70,00% | +20,00% | 95,18 $ | 1/28 | +3,57% | +26,32% | DEBOLE | 6,9 | 10,0 |
| -8,00% | 72,97 $ | 26/40 | +65,00% | +5,00% | 83,29 $ | 3/26 | +11,54% | +14,13% | DEBOLE | 9,9 | 21,0 |
| -8,00% | 72,97 $ | 26/40 | +65,00% | +10,00% | 87,25 $ | 2/26 | +7,69% | +19,57% | DEBOLE | 9,9 | 16,5 |
| -8,00% | 72,97 $ | 26/40 | +65,00% | +15,00% | 91,22 $ | 0/26 | 0,00% | +25,00% | DEBOLE | 9,9 | n/d |
| -8,00% | 72,97 $ | 26/40 | +65,00% | +20,00% | 95,18 $ | 0/26 | 0,00% | +30,43% | DEBOLE | 9,9 | n/d |
| -10,00% | 71,39 $ | 23/40 | +57,50% | +5,00% | 83,29 $ | 2/23 | +8,70% | +16,67% | DEBOLE | 10,5 | 16,5 |
| -10,00% | 71,39 $ | 23/40 | +57,50% | +10,00% | 87,25 $ | 2/23 | +8,70% | +22,22% | DEBOLE | 10,5 | 16,5 |
| -10,00% | 71,39 $ | 23/40 | +57,50% | +15,00% | 91,22 $ | 0/23 | 0,00% | +27,78% | DEBOLE | 10,5 | n/d |
| -10,00% | 71,39 $ | 23/40 | +57,50% | +20,00% | 95,18 $ | 0/23 | 0,00% | +33,33% | DEBOLE | 10,5 | n/d |
| -15,00% | 67,42 $ | 17/40 | +42,50% | +5,00% | 83,29 $ | 1/17 | +5,88% | +23,53% | DEBOLE | 12,8 | 15,0 |
| -15,00% | 67,42 $ | 17/40 | +42,50% | +10,00% | 87,25 $ | 1/17 | +5,88% | +29,41% | DEBOLE | 12,8 | 15,0 |
| -15,00% | 67,42 $ | 17/40 | +42,50% | +15,00% | 91,22 $ | 0/17 | 0,00% | +35,29% | DEBOLE | 12,8 | n/d |
| -15,00% | 67,42 $ | 17/40 | +42,50% | +20,00% | 95,18 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 12,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 83,29 $ | 23/40 | +57,50% | prezzo iniziale | 79,32 $ | 11/23 | +47,83% | -4,76% | BASSA | 3,1 | 10,2 |
| +5,00% | 83,29 $ | 23/40 | +57,50% | -5,00% | 75,35 $ | 10/23 | +43,48% | -9,52% | BASSA | 3,1 | 12,8 |
| +5,00% | 83,29 $ | 23/40 | +57,50% | -8,00% | 72,97 $ | 9/23 | +39,13% | -12,38% | BASSA | 3,1 | 14,8 |
| +5,00% | 83,29 $ | 23/40 | +57,50% | -10,00% | 71,39 $ | 7/23 | +30,43% | -14,29% | DEBOLE | 3,1 | 15,0 |
| +5,00% | 83,29 $ | 23/40 | +57,50% | -15,00% | 67,42 $ | 3/23 | +13,04% | -19,05% | DEBOLE | 3,1 | 15,3 |
| +10,00% | 87,25 $ | 18/40 | +45,00% | prezzo iniziale | 79,32 $ | 6/18 | +33,33% | -9,09% | DEBOLE | 6,5 | 12,7 |
| +10,00% | 87,25 $ | 18/40 | +45,00% | -5,00% | 75,35 $ | 5/18 | +27,78% | -13,64% | DEBOLE | 6,5 | 15,2 |
| +10,00% | 87,25 $ | 18/40 | +45,00% | -8,00% | 72,97 $ | 4/18 | +22,22% | -16,36% | DEBOLE | 6,5 | 15,2 |
| +10,00% | 87,25 $ | 18/40 | +45,00% | -10,00% | 71,39 $ | 3/18 | +16,67% | -18,18% | DEBOLE | 6,5 | 15,0 |
| +10,00% | 87,25 $ | 18/40 | +45,00% | -15,00% | 67,42 $ | 2/18 | +11,11% | -22,73% | DEBOLE | 6,5 | 16,0 |
| +15,00% | 91,22 $ | 14/40 | +35,00% | prezzo iniziale | 79,32 $ | 2/14 | +14,29% | -13,04% | DEBOLE | 10,3 | 14,0 |
| +15,00% | 91,22 $ | 14/40 | +35,00% | -5,00% | 75,35 $ | 1/14 | +7,14% | -17,39% | DEBOLE | 10,3 | 17,0 |
| +15,00% | 91,22 $ | 14/40 | +35,00% | -8,00% | 72,97 $ | 1/14 | +7,14% | -20,00% | DEBOLE | 10,3 | 17,0 |
| +15,00% | 91,22 $ | 14/40 | +35,00% | -10,00% | 71,39 $ | 0/14 | 0,00% | -21,74% | DEBOLE | 10,3 | n/d |
| +15,00% | 91,22 $ | 14/40 | +35,00% | -15,00% | 67,42 $ | 0/14 | 0,00% | -26,09% | DEBOLE | 10,3 | n/d |
| +20,00% | 95,18 $ | 12/40 | +30,00% | prezzo iniziale | 79,32 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 12,8 | n/d |
| +20,00% | 95,18 $ | 12/40 | +30,00% | -5,00% | 75,35 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 12,8 | n/d |
| +20,00% | 95,18 $ | 12/40 | +30,00% | -8,00% | 72,97 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 12,8 | n/d |
| +20,00% | 95,18 $ | 12/40 | +30,00% | -10,00% | 71,39 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 12,8 | n/d |
| +20,00% | 95,18 $ | 12/40 | +30,00% | -15,00% | 67,42 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 12,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 37 prima sono scesi a -5,00%. Tra quei 37, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +10,81% (4/37). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 13 prima sono saliti a +10,00%. Tra quei 13, 8 poi sono scaricati a -5,00%. Percentuale: +61,54% (8/13). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07051 $ | 37/40 | +92,50% | +5,00% | 0,07793 $ | 6/37 | +16,22% | +10,53% | DEBOLE | 6,6 | 13,3 |
| -5,00% | 0,07051 $ | 37/40 | +92,50% | +10,00% | 0,08164 $ | 4/37 | +10,81% | +15,79% | DEBOLE | 6,6 | 8,0 |
| -5,00% | 0,07051 $ | 37/40 | +92,50% | +15,00% | 0,08535 $ | 4/37 | +10,81% | +21,05% | DEBOLE | 6,6 | 12,0 |
| -5,00% | 0,07051 $ | 37/40 | +92,50% | +20,00% | 0,08906 $ | 4/37 | +10,81% | +26,32% | DEBOLE | 6,6 | 13,5 |
| -8,00% | 0,06828 $ | 35/40 | +87,50% | +5,00% | 0,07793 $ | 4/35 | +11,43% | +14,13% | DEBOLE | 8,4 | 16,2 |
| -8,00% | 0,06828 $ | 35/40 | +87,50% | +10,00% | 0,08164 $ | 2/35 | +5,71% | +19,57% | DEBOLE | 8,4 | 7,5 |
| -8,00% | 0,06828 $ | 35/40 | +87,50% | +15,00% | 0,08535 $ | 2/35 | +5,71% | +25,00% | DEBOLE | 8,4 | 14,5 |
| -8,00% | 0,06828 $ | 35/40 | +87,50% | +20,00% | 0,08906 $ | 2/35 | +5,71% | +30,43% | DEBOLE | 8,4 | 16,5 |
| -10,00% | 0,06680 $ | 32/40 | +80,00% | +5,00% | 0,07793 $ | 2/32 | +6,25% | +16,67% | DEBOLE | 9,2 | 25,0 |
| -10,00% | 0,06680 $ | 32/40 | +80,00% | +10,00% | 0,08164 $ | 0/32 | 0,00% | +22,22% | DEBOLE | 9,2 | n/d |
| -10,00% | 0,06680 $ | 32/40 | +80,00% | +15,00% | 0,08535 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 9,2 | n/d |
| -10,00% | 0,06680 $ | 32/40 | +80,00% | +20,00% | 0,08906 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 9,2 | n/d |
| -15,00% | 0,06309 $ | 29/40 | +72,50% | +5,00% | 0,07793 $ | 1/29 | +3,45% | +23,53% | DEBOLE | 10,8 | 25,0 |
| -15,00% | 0,06309 $ | 29/40 | +72,50% | +10,00% | 0,08164 $ | 0/29 | 0,00% | +29,41% | DEBOLE | 10,8 | n/d |
| -15,00% | 0,06309 $ | 29/40 | +72,50% | +15,00% | 0,08535 $ | 0/29 | 0,00% | +35,29% | DEBOLE | 10,8 | n/d |
| -15,00% | 0,06309 $ | 29/40 | +72,50% | +20,00% | 0,08906 $ | 0/29 | 0,00% | +41,18% | DEBOLE | 10,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07793 $ | 18/40 | +45,00% | prezzo iniziale | 0,07422 $ | 15/18 | +83,33% | -4,76% | ALTA | 6,3 | 10,4 |
| +5,00% | 0,07793 $ | 18/40 | +45,00% | -5,00% | 0,07051 $ | 13/18 | +72,22% | -9,52% | ALTA | 6,3 | 15,4 |
| +5,00% | 0,07793 $ | 18/40 | +45,00% | -8,00% | 0,06828 $ | 11/18 | +61,11% | -12,38% | MEDIA | 6,3 | 15,0 |
| +5,00% | 0,07793 $ | 18/40 | +45,00% | -10,00% | 0,06680 $ | 9/18 | +50,00% | -14,29% | MEDIA | 6,3 | 15,4 |
| +5,00% | 0,07793 $ | 18/40 | +45,00% | -15,00% | 0,06309 $ | 7/18 | +38,89% | -19,05% | BASSA | 6,3 | 12,7 |
| +10,00% | 0,08164 $ | 13/40 | +32,50% | prezzo iniziale | 0,07422 $ | 9/13 | +69,23% | -9,09% | ALTA | 6,8 | 10,3 |
| +10,00% | 0,08164 $ | 13/40 | +32,50% | -5,00% | 0,07051 $ | 8/13 | +61,54% | -13,64% | MEDIA | 6,8 | 13,9 |
| +10,00% | 0,08164 $ | 13/40 | +32,50% | -8,00% | 0,06828 $ | 7/13 | +53,85% | -16,36% | MEDIA | 6,8 | 14,3 |
| +10,00% | 0,08164 $ | 13/40 | +32,50% | -10,00% | 0,06680 $ | 6/13 | +46,15% | -18,18% | BASSA | 6,8 | 15,7 |
| +10,00% | 0,08164 $ | 13/40 | +32,50% | -15,00% | 0,06309 $ | 5/13 | +38,46% | -22,73% | BASSA | 6,8 | 14,4 |
| +15,00% | 0,08535 $ | 8/40 | +20,00% | prezzo iniziale | 0,07422 $ | 3/8 | +37,50% | -13,04% | BASSA | 9,1 | 10,7 |
| +15,00% | 0,08535 $ | 8/40 | +20,00% | -5,00% | 0,07051 $ | 3/8 | +37,50% | -17,39% | BASSA | 9,1 | 10,7 |
| +15,00% | 0,08535 $ | 8/40 | +20,00% | -8,00% | 0,06828 $ | 3/8 | +37,50% | -20,00% | BASSA | 9,1 | 11,0 |
| +15,00% | 0,08535 $ | 8/40 | +20,00% | -10,00% | 0,06680 $ | 2/8 | +25,00% | -21,74% | DEBOLE | 9,1 | 12,5 |
| +15,00% | 0,08535 $ | 8/40 | +20,00% | -15,00% | 0,06309 $ | 2/8 | +25,00% | -26,09% | DEBOLE | 9,1 | 13,0 |
| +20,00% | 0,08906 $ | 6/40 | +15,00% | prezzo iniziale | 0,07422 $ | 3/6 | +50,00% | -16,67% | MEDIA | 11,5 | 16,7 |
| +20,00% | 0,08906 $ | 6/40 | +15,00% | -5,00% | 0,07051 $ | 2/6 | +33,33% | -20,83% | DEBOLE | 11,5 | 11,5 |
| +20,00% | 0,08906 $ | 6/40 | +15,00% | -8,00% | 0,06828 $ | 2/6 | +33,33% | -23,33% | DEBOLE | 11,5 | 12,0 |
| +20,00% | 0,08906 $ | 6/40 | +15,00% | -10,00% | 0,06680 $ | 2/6 | +33,33% | -25,00% | DEBOLE | 11,5 | 12,5 |
| +20,00% | 0,08906 $ | 6/40 | +15,00% | -15,00% | 0,06309 $ | 2/6 | +33,33% | -29,17% | DEBOLE | 11,5 | 13,0 |

---
