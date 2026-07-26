# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-26 07:13:48 CEST**  
UTC: **2026-07-26 05:13:48 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.237 $ | 70.906 $ | +46,67% | +15,79% | rimbalzo debole | 70.906 $ | 61.237 $ | +8,70% | -13,64% | spike storicamente più resistente |
| SOL | 71,33 $ | 82,59 $ | +26,92% | +15,79% | rimbalzo poco frequente | 82,59 $ | 71,33 $ | +9,52% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06982 $ | 0,08084 $ | +39,29% | +15,79% | rimbalzo debole | 0,08084 $ | 0,06982 $ | +46,67% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +46,67% (14/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 2 poi sono scaricati a -5,00%. Percentuale: +8,70% (2/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.237 $ | 30/40 | +75,00% | +5,00% | 67.683 $ | 15/30 | +50,00% | +10,53% | MEDIA | 5,9 | 15,3 |
| -5,00% | 61.237 $ | 30/40 | +75,00% | +10,00% | 70.906 $ | 14/30 | +46,67% | +15,79% | BASSA | 5,9 | 19,7 |
| -5,00% | 61.237 $ | 30/40 | +75,00% | +15,00% | 74.129 $ | 12/30 | +40,00% | +21,05% | BASSA | 5,9 | 22,2 |
| -5,00% | 61.237 $ | 30/40 | +75,00% | +20,00% | 77.351 $ | 10/30 | +33,33% | +26,32% | DEBOLE | 5,9 | 24,6 |
| -8,00% | 59.303 $ | 20/40 | +50,00% | +5,00% | 67.683 $ | 5/20 | +25,00% | +14,13% | DEBOLE | 9,6 | 16,8 |
| -8,00% | 59.303 $ | 20/40 | +50,00% | +10,00% | 70.906 $ | 5/20 | +25,00% | +19,57% | DEBOLE | 9,6 | 23,0 |
| -8,00% | 59.303 $ | 20/40 | +50,00% | +15,00% | 74.129 $ | 4/20 | +20,00% | +25,00% | DEBOLE | 9,6 | 23,2 |
| -8,00% | 59.303 $ | 20/40 | +50,00% | +20,00% | 77.351 $ | 4/20 | +20,00% | +30,43% | DEBOLE | 9,6 | 27,2 |
| -10,00% | 58.014 $ | 17/40 | +42,50% | +5,00% | 67.683 $ | 2/17 | +11,76% | +16,67% | DEBOLE | 12,6 | 20,0 |
| -10,00% | 58.014 $ | 17/40 | +42,50% | +10,00% | 70.906 $ | 2/17 | +11,76% | +22,22% | DEBOLE | 12,6 | 26,5 |
| -10,00% | 58.014 $ | 17/40 | +42,50% | +15,00% | 74.129 $ | 2/17 | +11,76% | +27,78% | DEBOLE | 12,6 | 26,5 |
| -10,00% | 58.014 $ | 17/40 | +42,50% | +20,00% | 77.351 $ | 2/17 | +11,76% | +33,33% | DEBOLE | 12,6 | 29,5 |
| -15,00% | 54.791 $ | 13/40 | +32,50% | +5,00% | 67.683 $ | 0/13 | 0,00% | +23,53% | DEBOLE | 14,4 | n/d |
| -15,00% | 54.791 $ | 13/40 | +32,50% | +10,00% | 70.906 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 14,4 | n/d |
| -15,00% | 54.791 $ | 13/40 | +32,50% | +15,00% | 74.129 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 14,4 | n/d |
| -15,00% | 54.791 $ | 13/40 | +32,50% | +20,00% | 77.351 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 14,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.683 $ | 29/40 | +72,50% | prezzo iniziale | 64.460 $ | 8/29 | +27,59% | -4,76% | DEBOLE | 12,4 | 14,4 |
| +5,00% | 67.683 $ | 29/40 | +72,50% | -5,00% | 61.237 $ | 6/29 | +20,69% | -9,52% | DEBOLE | 12,4 | 14,3 |
| +5,00% | 67.683 $ | 29/40 | +72,50% | -8,00% | 59.303 $ | 5/29 | +17,24% | -12,38% | DEBOLE | 12,4 | 15,6 |
| +5,00% | 67.683 $ | 29/40 | +72,50% | -10,00% | 58.014 $ | 5/29 | +17,24% | -14,29% | DEBOLE | 12,4 | 16,8 |
| +5,00% | 67.683 $ | 29/40 | +72,50% | -15,00% | 54.791 $ | 5/29 | +17,24% | -19,05% | DEBOLE | 12,4 | 18,0 |
| +10,00% | 70.906 $ | 23/40 | +57,50% | prezzo iniziale | 64.460 $ | 2/23 | +8,70% | -9,09% | DEBOLE | 17,7 | 18,5 |
| +10,00% | 70.906 $ | 23/40 | +57,50% | -5,00% | 61.237 $ | 2/23 | +8,70% | -13,64% | DEBOLE | 17,7 | 19,0 |
| +10,00% | 70.906 $ | 23/40 | +57,50% | -8,00% | 59.303 $ | 2/23 | +8,70% | -16,36% | DEBOLE | 17,7 | 19,0 |
| +10,00% | 70.906 $ | 23/40 | +57,50% | -10,00% | 58.014 $ | 2/23 | +8,70% | -18,18% | DEBOLE | 17,7 | 19,0 |
| +10,00% | 70.906 $ | 23/40 | +57,50% | -15,00% | 54.791 $ | 2/23 | +8,70% | -22,73% | DEBOLE | 17,7 | 19,5 |
| +15,00% | 74.129 $ | 20/40 | +50,00% | prezzo iniziale | 64.460 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 74.129 $ | 20/40 | +50,00% | -5,00% | 61.237 $ | 1/20 | +5,00% | -17,39% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 74.129 $ | 20/40 | +50,00% | -8,00% | 59.303 $ | 1/20 | +5,00% | -20,00% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 74.129 $ | 20/40 | +50,00% | -10,00% | 58.014 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 20,4 | 17,0 |
| +15,00% | 74.129 $ | 20/40 | +50,00% | -15,00% | 54.791 $ | 1/20 | +5,00% | -26,09% | DEBOLE | 20,4 | 18,0 |
| +20,00% | 77.351 $ | 17/40 | +42,50% | prezzo iniziale | 64.460 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 22,1 | 17,0 |
| +20,00% | 77.351 $ | 17/40 | +42,50% | -5,00% | 61.237 $ | 1/17 | +5,88% | -20,83% | DEBOLE | 22,1 | 17,0 |
| +20,00% | 77.351 $ | 17/40 | +42,50% | -8,00% | 59.303 $ | 1/17 | +5,88% | -23,33% | DEBOLE | 22,1 | 17,0 |
| +20,00% | 77.351 $ | 17/40 | +42,50% | -10,00% | 58.014 $ | 1/17 | +5,88% | -25,00% | DEBOLE | 22,1 | 17,0 |
| +20,00% | 77.351 $ | 17/40 | +42,50% | -15,00% | 54.791 $ | 1/17 | +5,88% | -29,17% | DEBOLE | 22,1 | 18,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +26,92% (7/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 2 poi sono scaricati a -5,00%. Percentuale: +9,52% (2/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,33 $ | 26/40 | +65,00% | +5,00% | 78,83 $ | 12/26 | +46,15% | +10,53% | BASSA | 8,5 | 17,6 |
| -5,00% | 71,33 $ | 26/40 | +65,00% | +10,00% | 82,59 $ | 7/26 | +26,92% | +15,79% | DEBOLE | 8,5 | 19,6 |
| -5,00% | 71,33 $ | 26/40 | +65,00% | +15,00% | 86,34 $ | 5/26 | +19,23% | +21,05% | DEBOLE | 8,5 | 20,0 |
| -5,00% | 71,33 $ | 26/40 | +65,00% | +20,00% | 90,10 $ | 5/26 | +19,23% | +26,32% | DEBOLE | 8,5 | 21,0 |
| -8,00% | 69,07 $ | 21/40 | +52,50% | +5,00% | 78,83 $ | 6/21 | +28,57% | +14,13% | DEBOLE | 11,2 | 20,8 |
| -8,00% | 69,07 $ | 21/40 | +52,50% | +10,00% | 82,59 $ | 5/21 | +23,81% | +19,57% | DEBOLE | 11,2 | 21,8 |
| -8,00% | 69,07 $ | 21/40 | +52,50% | +15,00% | 86,34 $ | 4/21 | +19,05% | +25,00% | DEBOLE | 11,2 | 23,8 |
| -8,00% | 69,07 $ | 21/40 | +52,50% | +20,00% | 90,10 $ | 4/21 | +19,05% | +30,43% | DEBOLE | 11,2 | 25,0 |
| -10,00% | 67,57 $ | 15/40 | +37,50% | +5,00% | 78,83 $ | 1/15 | +6,67% | +16,67% | DEBOLE | 14,1 | 20,0 |
| -10,00% | 67,57 $ | 15/40 | +37,50% | +10,00% | 82,59 $ | 1/15 | +6,67% | +22,22% | DEBOLE | 14,1 | 27,0 |
| -10,00% | 67,57 $ | 15/40 | +37,50% | +15,00% | 86,34 $ | 1/15 | +6,67% | +27,78% | DEBOLE | 14,1 | 28,0 |
| -10,00% | 67,57 $ | 15/40 | +37,50% | +20,00% | 90,10 $ | 1/15 | +6,67% | +33,33% | DEBOLE | 14,1 | 28,0 |
| -15,00% | 63,82 $ | 7/40 | +17,50% | +5,00% | 78,83 $ | 0/7 | 0,00% | +23,53% | DEBOLE | 19,1 | n/d |
| -15,00% | 63,82 $ | 7/40 | +17,50% | +10,00% | 82,59 $ | 0/7 | 0,00% | +29,41% | DEBOLE | 19,1 | n/d |
| -15,00% | 63,82 $ | 7/40 | +17,50% | +15,00% | 86,34 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 19,1 | n/d |
| -15,00% | 63,82 $ | 7/40 | +17,50% | +20,00% | 90,10 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 19,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 78,83 $ | 30/40 | +75,00% | prezzo iniziale | 75,08 $ | 11/30 | +36,67% | -4,76% | BASSA | 9,6 | 12,6 |
| +5,00% | 78,83 $ | 30/40 | +75,00% | -5,00% | 71,33 $ | 9/30 | +30,00% | -9,52% | DEBOLE | 9,6 | 14,2 |
| +5,00% | 78,83 $ | 30/40 | +75,00% | -8,00% | 69,07 $ | 7/30 | +23,33% | -12,38% | DEBOLE | 9,6 | 16,0 |
| +5,00% | 78,83 $ | 30/40 | +75,00% | -10,00% | 67,57 $ | 4/30 | +13,33% | -14,29% | DEBOLE | 9,6 | 20,8 |
| +5,00% | 78,83 $ | 30/40 | +75,00% | -15,00% | 63,82 $ | 3/30 | +10,00% | -19,05% | DEBOLE | 9,6 | 21,3 |
| +10,00% | 82,59 $ | 21/40 | +52,50% | prezzo iniziale | 75,08 $ | 3/21 | +14,29% | -9,09% | DEBOLE | 12,4 | 13,3 |
| +10,00% | 82,59 $ | 21/40 | +52,50% | -5,00% | 71,33 $ | 2/21 | +9,52% | -13,64% | DEBOLE | 12,4 | 17,0 |
| +10,00% | 82,59 $ | 21/40 | +52,50% | -8,00% | 69,07 $ | 1/21 | +4,76% | -16,36% | DEBOLE | 12,4 | 24,0 |
| +10,00% | 82,59 $ | 21/40 | +52,50% | -10,00% | 67,57 $ | 1/21 | +4,76% | -18,18% | DEBOLE | 12,4 | 24,0 |
| +10,00% | 82,59 $ | 21/40 | +52,50% | -15,00% | 63,82 $ | 0/21 | 0,00% | -22,73% | DEBOLE | 12,4 | n/d |
| +15,00% | 86,34 $ | 17/40 | +42,50% | prezzo iniziale | 75,08 $ | 1/17 | +5,88% | -13,04% | DEBOLE | 14,9 | 19,0 |
| +15,00% | 86,34 $ | 17/40 | +42,50% | -5,00% | 71,33 $ | 1/17 | +5,88% | -17,39% | DEBOLE | 14,9 | 23,0 |
| +15,00% | 86,34 $ | 17/40 | +42,50% | -8,00% | 69,07 $ | 1/17 | +5,88% | -20,00% | DEBOLE | 14,9 | 24,0 |
| +15,00% | 86,34 $ | 17/40 | +42,50% | -10,00% | 67,57 $ | 1/17 | +5,88% | -21,74% | DEBOLE | 14,9 | 24,0 |
| +15,00% | 86,34 $ | 17/40 | +42,50% | -15,00% | 63,82 $ | 0/17 | 0,00% | -26,09% | DEBOLE | 14,9 | n/d |
| +20,00% | 90,10 $ | 13/40 | +32,50% | prezzo iniziale | 75,08 $ | 1/13 | +7,69% | -16,67% | DEBOLE | 16,5 | 19,0 |
| +20,00% | 90,10 $ | 13/40 | +32,50% | -5,00% | 71,33 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 16,5 | 23,0 |
| +20,00% | 90,10 $ | 13/40 | +32,50% | -8,00% | 69,07 $ | 1/13 | +7,69% | -23,33% | DEBOLE | 16,5 | 24,0 |
| +20,00% | 90,10 $ | 13/40 | +32,50% | -10,00% | 67,57 $ | 1/13 | +7,69% | -25,00% | DEBOLE | 16,5 | 24,0 |
| +20,00% | 90,10 $ | 13/40 | +32,50% | -15,00% | 63,82 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 16,5 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +39,29% (11/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 14 poi sono scaricati a -5,00%. Percentuale: +46,67% (14/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06982 $ | 28/40 | +70,00% | +5,00% | 0,07716 $ | 18/28 | +64,29% | +10,53% | MEDIA | 8,2 | 14,2 |
| -5,00% | 0,06982 $ | 28/40 | +70,00% | +10,00% | 0,08084 $ | 11/28 | +39,29% | +15,79% | BASSA | 8,2 | 14,7 |
| -5,00% | 0,06982 $ | 28/40 | +70,00% | +15,00% | 0,08451 $ | 5/28 | +17,86% | +21,05% | DEBOLE | 8,2 | 10,8 |
| -5,00% | 0,06982 $ | 28/40 | +70,00% | +20,00% | 0,08819 $ | 5/28 | +17,86% | +26,32% | DEBOLE | 8,2 | 16,4 |
| -8,00% | 0,06761 $ | 20/40 | +50,00% | +5,00% | 0,07716 $ | 8/20 | +40,00% | +14,13% | BASSA | 12,6 | 15,2 |
| -8,00% | 0,06761 $ | 20/40 | +50,00% | +10,00% | 0,08084 $ | 4/20 | +20,00% | +19,57% | DEBOLE | 12,6 | 16,5 |
| -8,00% | 0,06761 $ | 20/40 | +50,00% | +15,00% | 0,08451 $ | 2/20 | +10,00% | +25,00% | DEBOLE | 12,6 | 8,5 |
| -8,00% | 0,06761 $ | 20/40 | +50,00% | +20,00% | 0,08819 $ | 2/20 | +10,00% | +30,43% | DEBOLE | 12,6 | 15,5 |
| -10,00% | 0,06614 $ | 18/40 | +45,00% | +5,00% | 0,07716 $ | 8/18 | +44,44% | +16,67% | BASSA | 12,6 | 17,1 |
| -10,00% | 0,06614 $ | 18/40 | +45,00% | +10,00% | 0,08084 $ | 4/18 | +22,22% | +22,22% | DEBOLE | 12,6 | 16,5 |
| -10,00% | 0,06614 $ | 18/40 | +45,00% | +15,00% | 0,08451 $ | 2/18 | +11,11% | +27,78% | DEBOLE | 12,6 | 8,5 |
| -10,00% | 0,06614 $ | 18/40 | +45,00% | +20,00% | 0,08819 $ | 2/18 | +11,11% | +33,33% | DEBOLE | 12,6 | 15,5 |
| -15,00% | 0,06247 $ | 11/40 | +27,50% | +5,00% | 0,07716 $ | 3/11 | +27,27% | +23,53% | DEBOLE | 14,8 | 19,0 |
| -15,00% | 0,06247 $ | 11/40 | +27,50% | +10,00% | 0,08084 $ | 3/11 | +27,27% | +29,41% | DEBOLE | 14,8 | 19,7 |
| -15,00% | 0,06247 $ | 11/40 | +27,50% | +15,00% | 0,08451 $ | 1/11 | +9,09% | +35,29% | DEBOLE | 14,8 | 10,0 |
| -15,00% | 0,06247 $ | 11/40 | +27,50% | +20,00% | 0,08819 $ | 1/11 | +9,09% | +41,18% | DEBOLE | 14,8 | 24,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07716 $ | 36/40 | +90,00% | prezzo iniziale | 0,07349 $ | 26/36 | +72,22% | -4,76% | ALTA | 5,6 | 10,6 |
| +5,00% | 0,07716 $ | 36/40 | +90,00% | -5,00% | 0,06982 $ | 21/36 | +58,33% | -9,52% | MEDIA | 5,6 | 14,1 |
| +5,00% | 0,07716 $ | 36/40 | +90,00% | -8,00% | 0,06761 $ | 15/36 | +41,67% | -12,38% | BASSA | 5,6 | 16,8 |
| +5,00% | 0,07716 $ | 36/40 | +90,00% | -10,00% | 0,06614 $ | 13/36 | +36,11% | -14,29% | BASSA | 5,6 | 16,3 |
| +5,00% | 0,07716 $ | 36/40 | +90,00% | -15,00% | 0,06247 $ | 5/36 | +13,89% | -19,05% | DEBOLE | 5,6 | 16,6 |
| +10,00% | 0,08084 $ | 30/40 | +75,00% | prezzo iniziale | 0,07349 $ | 19/30 | +63,33% | -9,09% | MEDIA | 7,9 | 14,5 |
| +10,00% | 0,08084 $ | 30/40 | +75,00% | -5,00% | 0,06982 $ | 14/30 | +46,67% | -13,64% | BASSA | 7,9 | 19,0 |
| +10,00% | 0,08084 $ | 30/40 | +75,00% | -8,00% | 0,06761 $ | 8/30 | +26,67% | -16,36% | DEBOLE | 7,9 | 19,5 |
| +10,00% | 0,08084 $ | 30/40 | +75,00% | -10,00% | 0,06614 $ | 6/30 | +20,00% | -18,18% | DEBOLE | 7,9 | 18,8 |
| +10,00% | 0,08084 $ | 30/40 | +75,00% | -15,00% | 0,06247 $ | 3/30 | +10,00% | -22,73% | DEBOLE | 7,9 | 14,3 |
| +15,00% | 0,08451 $ | 21/40 | +52,50% | prezzo iniziale | 0,07349 $ | 12/21 | +57,14% | -13,04% | MEDIA | 7,6 | 14,9 |
| +15,00% | 0,08451 $ | 21/40 | +52,50% | -5,00% | 0,06982 $ | 8/21 | +38,10% | -17,39% | BASSA | 7,6 | 19,9 |
| +15,00% | 0,08451 $ | 21/40 | +52,50% | -8,00% | 0,06761 $ | 4/21 | +19,05% | -20,00% | DEBOLE | 7,6 | 17,8 |
| +15,00% | 0,08451 $ | 21/40 | +52,50% | -10,00% | 0,06614 $ | 3/21 | +14,29% | -21,74% | DEBOLE | 7,6 | 18,0 |
| +15,00% | 0,08451 $ | 21/40 | +52,50% | -15,00% | 0,06247 $ | 1/21 | +4,76% | -26,09% | DEBOLE | 7,6 | 11,0 |
| +20,00% | 0,08819 $ | 16/40 | +40,00% | prezzo iniziale | 0,07349 $ | 6/16 | +37,50% | -16,67% | BASSA | 12,1 | 18,7 |
| +20,00% | 0,08819 $ | 16/40 | +40,00% | -5,00% | 0,06982 $ | 3/16 | +18,75% | -20,83% | DEBOLE | 12,1 | 21,0 |
| +20,00% | 0,08819 $ | 16/40 | +40,00% | -8,00% | 0,06761 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 12,1 | n/d |
| +20,00% | 0,08819 $ | 16/40 | +40,00% | -10,00% | 0,06614 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 12,1 | n/d |
| +20,00% | 0,08819 $ | 16/40 | +40,00% | -15,00% | 0,06247 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 12,1 | n/d |

---
