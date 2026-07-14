# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-14 11:33:38 CEST**  
UTC: **2026-07-14 09:33:38 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.453 $ | 68.841 $ | +31,58% | +15,79% | rimbalzo poco frequente | 68.841 $ | 59.453 $ | +16,67% | -13,64% | spike storicamente più resistente |
| SOL | 71,31 $ | 82,57 $ | +13,79% | +15,79% | rimbalzo poco frequente | 82,57 $ | 71,31 $ | +29,41% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06849 $ | 0,07930 $ | +11,76% | +15,79% | rimbalzo poco frequente | 0,07930 $ | 0,06849 $ | +42,86% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +31,58% (6/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 4 poi sono scaricati a -5,00%. Percentuale: +16,67% (4/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.453 $ | 19/40 | +47,50% | +5,00% | 65.712 $ | 8/19 | +42,11% | +10,53% | BASSA | 9,1 | 22,2 |
| -5,00% | 59.453 $ | 19/40 | +47,50% | +10,00% | 68.841 $ | 6/19 | +31,58% | +15,79% | DEBOLE | 9,1 | 25,2 |
| -5,00% | 59.453 $ | 19/40 | +47,50% | +15,00% | 71.970 $ | 4/19 | +21,05% | +21,05% | DEBOLE | 9,1 | 24,2 |
| -5,00% | 59.453 $ | 19/40 | +47,50% | +20,00% | 75.099 $ | 4/19 | +21,05% | +26,32% | DEBOLE | 9,1 | 25,0 |
| -8,00% | 57.576 $ | 15/40 | +37,50% | +5,00% | 65.712 $ | 4/15 | +26,67% | +14,13% | DEBOLE | 10,8 | 22,5 |
| -8,00% | 57.576 $ | 15/40 | +37,50% | +10,00% | 68.841 $ | 2/15 | +13,33% | +19,57% | DEBOLE | 10,8 | 20,5 |
| -8,00% | 57.576 $ | 15/40 | +37,50% | +15,00% | 71.970 $ | 2/15 | +13,33% | +25,00% | DEBOLE | 10,8 | 20,5 |
| -8,00% | 57.576 $ | 15/40 | +37,50% | +20,00% | 75.099 $ | 2/15 | +13,33% | +30,43% | DEBOLE | 10,8 | 21,0 |
| -10,00% | 56.324 $ | 12/40 | +30,00% | +5,00% | 65.712 $ | 2/12 | +16,67% | +16,67% | DEBOLE | 10,3 | 24,5 |
| -10,00% | 56.324 $ | 12/40 | +30,00% | +10,00% | 68.841 $ | 1/12 | +8,33% | +22,22% | DEBOLE | 10,3 | 26,0 |
| -10,00% | 56.324 $ | 12/40 | +30,00% | +15,00% | 71.970 $ | 1/12 | +8,33% | +27,78% | DEBOLE | 10,3 | 26,0 |
| -10,00% | 56.324 $ | 12/40 | +30,00% | +20,00% | 75.099 $ | 1/12 | +8,33% | +33,33% | DEBOLE | 10,3 | 26,0 |
| -15,00% | 53.195 $ | 9/40 | +22,50% | +5,00% | 65.712 $ | 0/9 | 0,00% | +23,53% | DEBOLE | 14,8 | n/d |
| -15,00% | 53.195 $ | 9/40 | +22,50% | +10,00% | 68.841 $ | 0/9 | 0,00% | +29,41% | DEBOLE | 14,8 | n/d |
| -15,00% | 53.195 $ | 9/40 | +22,50% | +15,00% | 71.970 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 14,8 | n/d |
| -15,00% | 53.195 $ | 9/40 | +22,50% | +20,00% | 75.099 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 14,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.712 $ | 33/40 | +82,50% | prezzo iniziale | 62.583 $ | 22/33 | +66,67% | -4,76% | ALTA | 4,7 | 12,9 |
| +5,00% | 65.712 $ | 33/40 | +82,50% | -5,00% | 59.453 $ | 11/33 | +33,33% | -9,52% | DEBOLE | 4,7 | 13,3 |
| +5,00% | 65.712 $ | 33/40 | +82,50% | -8,00% | 57.576 $ | 7/33 | +21,21% | -12,38% | DEBOLE | 4,7 | 13,0 |
| +5,00% | 65.712 $ | 33/40 | +82,50% | -10,00% | 56.324 $ | 5/33 | +15,15% | -14,29% | DEBOLE | 4,7 | 12,6 |
| +5,00% | 65.712 $ | 33/40 | +82,50% | -15,00% | 53.195 $ | 4/33 | +12,12% | -19,05% | DEBOLE | 4,7 | 18,8 |
| +10,00% | 68.841 $ | 24/40 | +60,00% | prezzo iniziale | 62.583 $ | 8/24 | +33,33% | -9,09% | DEBOLE | 10,1 | 10,6 |
| +10,00% | 68.841 $ | 24/40 | +60,00% | -5,00% | 59.453 $ | 4/24 | +16,67% | -13,64% | DEBOLE | 10,1 | 9,5 |
| +10,00% | 68.841 $ | 24/40 | +60,00% | -8,00% | 57.576 $ | 3/24 | +12,50% | -16,36% | DEBOLE | 10,1 | 13,3 |
| +10,00% | 68.841 $ | 24/40 | +60,00% | -10,00% | 56.324 $ | 2/24 | +8,33% | -18,18% | DEBOLE | 10,1 | 14,0 |
| +10,00% | 68.841 $ | 24/40 | +60,00% | -15,00% | 53.195 $ | 1/24 | +4,17% | -22,73% | DEBOLE | 10,1 | 12,0 |
| +15,00% | 71.970 $ | 19/40 | +47,50% | prezzo iniziale | 62.583 $ | 3/19 | +15,79% | -13,04% | DEBOLE | 12,6 | 13,7 |
| +15,00% | 71.970 $ | 19/40 | +47,50% | -5,00% | 59.453 $ | 0/19 | 0,00% | -17,39% | DEBOLE | 12,6 | n/d |
| +15,00% | 71.970 $ | 19/40 | +47,50% | -8,00% | 57.576 $ | 0/19 | 0,00% | -20,00% | DEBOLE | 12,6 | n/d |
| +15,00% | 71.970 $ | 19/40 | +47,50% | -10,00% | 56.324 $ | 0/19 | 0,00% | -21,74% | DEBOLE | 12,6 | n/d |
| +15,00% | 71.970 $ | 19/40 | +47,50% | -15,00% | 53.195 $ | 0/19 | 0,00% | -26,09% | DEBOLE | 12,6 | n/d |
| +20,00% | 75.099 $ | 17/40 | +42,50% | prezzo iniziale | 62.583 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 14,4 | 7,0 |
| +20,00% | 75.099 $ | 17/40 | +42,50% | -5,00% | 59.453 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 14,4 | n/d |
| +20,00% | 75.099 $ | 17/40 | +42,50% | -8,00% | 57.576 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 14,4 | n/d |
| +20,00% | 75.099 $ | 17/40 | +42,50% | -10,00% | 56.324 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 14,4 | n/d |
| +20,00% | 75.099 $ | 17/40 | +42,50% | -15,00% | 53.195 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 14,4 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +13,79% (4/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 5 poi sono scaricati a -5,00%. Percentuale: +29,41% (5/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,31 $ | 29/40 | +72,50% | +5,00% | 78,81 $ | 8/29 | +27,59% | +10,53% | DEBOLE | 7,2 | 23,5 |
| -5,00% | 71,31 $ | 29/40 | +72,50% | +10,00% | 82,57 $ | 4/29 | +13,79% | +15,79% | DEBOLE | 7,2 | 21,2 |
| -5,00% | 71,31 $ | 29/40 | +72,50% | +15,00% | 86,32 $ | 4/29 | +13,79% | +21,05% | DEBOLE | 7,2 | 21,5 |
| -5,00% | 71,31 $ | 29/40 | +72,50% | +20,00% | 90,07 $ | 2/29 | +6,90% | +26,32% | DEBOLE | 7,2 | 23,0 |
| -8,00% | 69,06 $ | 25/40 | +62,50% | +5,00% | 78,81 $ | 3/25 | +12,00% | +14,13% | DEBOLE | 9,7 | 23,3 |
| -8,00% | 69,06 $ | 25/40 | +62,50% | +10,00% | 82,57 $ | 2/25 | +8,00% | +19,57% | DEBOLE | 9,7 | 22,0 |
| -8,00% | 69,06 $ | 25/40 | +62,50% | +15,00% | 86,32 $ | 2/25 | +8,00% | +25,00% | DEBOLE | 9,7 | 22,0 |
| -8,00% | 69,06 $ | 25/40 | +62,50% | +20,00% | 90,07 $ | 2/25 | +8,00% | +30,43% | DEBOLE | 9,7 | 23,0 |
| -10,00% | 67,55 $ | 20/40 | +50,00% | +5,00% | 78,81 $ | 1/20 | +5,00% | +16,67% | DEBOLE | 9,7 | 29,0 |
| -10,00% | 67,55 $ | 20/40 | +50,00% | +10,00% | 82,57 $ | 0/20 | 0,00% | +22,22% | DEBOLE | 9,7 | n/d |
| -10,00% | 67,55 $ | 20/40 | +50,00% | +15,00% | 86,32 $ | 0/20 | 0,00% | +27,78% | DEBOLE | 9,7 | n/d |
| -10,00% | 67,55 $ | 20/40 | +50,00% | +20,00% | 90,07 $ | 0/20 | 0,00% | +33,33% | DEBOLE | 9,7 | n/d |
| -15,00% | 63,80 $ | 14/40 | +35,00% | +5,00% | 78,81 $ | 0/14 | 0,00% | +23,53% | DEBOLE | 11,1 | n/d |
| -15,00% | 63,80 $ | 14/40 | +35,00% | +10,00% | 82,57 $ | 0/14 | 0,00% | +29,41% | DEBOLE | 11,1 | n/d |
| -15,00% | 63,80 $ | 14/40 | +35,00% | +15,00% | 86,32 $ | 0/14 | 0,00% | +35,29% | DEBOLE | 11,1 | n/d |
| -15,00% | 63,80 $ | 14/40 | +35,00% | +20,00% | 90,07 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 11,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 78,81 $ | 24/40 | +60,00% | prezzo iniziale | 75,06 $ | 13/24 | +54,17% | -4,76% | MEDIA | 5,9 | 10,2 |
| +5,00% | 78,81 $ | 24/40 | +60,00% | -5,00% | 71,31 $ | 11/24 | +45,83% | -9,52% | BASSA | 5,9 | 11,3 |
| +5,00% | 78,81 $ | 24/40 | +60,00% | -8,00% | 69,06 $ | 9/24 | +37,50% | -12,38% | BASSA | 5,9 | 15,8 |
| +5,00% | 78,81 $ | 24/40 | +60,00% | -10,00% | 67,55 $ | 6/24 | +25,00% | -14,29% | DEBOLE | 5,9 | 15,7 |
| +5,00% | 78,81 $ | 24/40 | +60,00% | -15,00% | 63,80 $ | 4/24 | +16,67% | -19,05% | DEBOLE | 5,9 | 22,2 |
| +10,00% | 82,57 $ | 17/40 | +42,50% | prezzo iniziale | 75,06 $ | 5/17 | +29,41% | -9,09% | DEBOLE | 8,7 | 7,8 |
| +10,00% | 82,57 $ | 17/40 | +42,50% | -5,00% | 71,31 $ | 5/17 | +29,41% | -13,64% | DEBOLE | 8,7 | 8,8 |
| +10,00% | 82,57 $ | 17/40 | +42,50% | -8,00% | 69,06 $ | 5/17 | +29,41% | -16,36% | DEBOLE | 8,7 | 14,6 |
| +10,00% | 82,57 $ | 17/40 | +42,50% | -10,00% | 67,55 $ | 3/17 | +17,65% | -18,18% | DEBOLE | 8,7 | 11,0 |
| +10,00% | 82,57 $ | 17/40 | +42,50% | -15,00% | 63,80 $ | 2/17 | +11,76% | -22,73% | DEBOLE | 8,7 | 20,0 |
| +15,00% | 86,32 $ | 13/40 | +32,50% | prezzo iniziale | 75,06 $ | 1/13 | +7,69% | -13,04% | DEBOLE | 10,4 | 10,0 |
| +15,00% | 86,32 $ | 13/40 | +32,50% | -5,00% | 71,31 $ | 1/13 | +7,69% | -17,39% | DEBOLE | 10,4 | 10,0 |
| +15,00% | 86,32 $ | 13/40 | +32,50% | -8,00% | 69,06 $ | 1/13 | +7,69% | -20,00% | DEBOLE | 10,4 | 30,0 |
| +15,00% | 86,32 $ | 13/40 | +32,50% | -10,00% | 67,55 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 10,4 | n/d |
| +15,00% | 86,32 $ | 13/40 | +32,50% | -15,00% | 63,80 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 10,4 | n/d |
| +20,00% | 90,07 $ | 10/40 | +25,00% | prezzo iniziale | 75,06 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 9,9 | 10,0 |
| +20,00% | 90,07 $ | 10/40 | +25,00% | -5,00% | 71,31 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 9,9 | 10,0 |
| +20,00% | 90,07 $ | 10/40 | +25,00% | -8,00% | 69,06 $ | 1/10 | +10,00% | -23,33% | DEBOLE | 9,9 | 30,0 |
| +20,00% | 90,07 $ | 10/40 | +25,00% | -10,00% | 67,55 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 9,9 | n/d |
| +20,00% | 90,07 $ | 10/40 | +25,00% | -15,00% | 63,80 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 9,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +11,76% (4/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 14 prima sono saliti a +10,00%. Tra quei 14, 6 poi sono scaricati a -5,00%. Percentuale: +42,86% (6/14). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06849 $ | 34/40 | +85,00% | +5,00% | 0,07569 $ | 5/34 | +14,71% | +10,53% | DEBOLE | 5,3 | 14,8 |
| -5,00% | 0,06849 $ | 34/40 | +85,00% | +10,00% | 0,07930 $ | 4/34 | +11,76% | +15,79% | DEBOLE | 5,3 | 12,5 |
| -5,00% | 0,06849 $ | 34/40 | +85,00% | +15,00% | 0,08290 $ | 2/34 | +5,88% | +21,05% | DEBOLE | 5,3 | 9,0 |
| -5,00% | 0,06849 $ | 34/40 | +85,00% | +20,00% | 0,08651 $ | 2/34 | +5,88% | +26,32% | DEBOLE | 5,3 | 11,0 |
| -8,00% | 0,06632 $ | 34/40 | +85,00% | +5,00% | 0,07569 $ | 5/34 | +14,71% | +14,13% | DEBOLE | 6,2 | 14,8 |
| -8,00% | 0,06632 $ | 34/40 | +85,00% | +10,00% | 0,07930 $ | 4/34 | +11,76% | +19,57% | DEBOLE | 6,2 | 12,5 |
| -8,00% | 0,06632 $ | 34/40 | +85,00% | +15,00% | 0,08290 $ | 2/34 | +5,88% | +25,00% | DEBOLE | 6,2 | 9,0 |
| -8,00% | 0,06632 $ | 34/40 | +85,00% | +20,00% | 0,08651 $ | 2/34 | +5,88% | +30,43% | DEBOLE | 6,2 | 11,0 |
| -10,00% | 0,06488 $ | 31/40 | +77,50% | +5,00% | 0,07569 $ | 2/31 | +6,45% | +16,67% | DEBOLE | 6,8 | 18,0 |
| -10,00% | 0,06488 $ | 31/40 | +77,50% | +10,00% | 0,07930 $ | 2/31 | +6,45% | +22,22% | DEBOLE | 6,8 | 18,5 |
| -10,00% | 0,06488 $ | 31/40 | +77,50% | +15,00% | 0,08290 $ | 0/31 | 0,00% | +27,78% | DEBOLE | 6,8 | n/d |
| -10,00% | 0,06488 $ | 31/40 | +77,50% | +20,00% | 0,08651 $ | 0/31 | 0,00% | +33,33% | DEBOLE | 6,8 | n/d |
| -15,00% | 0,06128 $ | 30/40 | +75,00% | +5,00% | 0,07569 $ | 2/30 | +6,67% | +23,53% | DEBOLE | 8,1 | 18,0 |
| -15,00% | 0,06128 $ | 30/40 | +75,00% | +10,00% | 0,07930 $ | 2/30 | +6,67% | +29,41% | DEBOLE | 8,1 | 18,5 |
| -15,00% | 0,06128 $ | 30/40 | +75,00% | +15,00% | 0,08290 $ | 0/30 | 0,00% | +35,29% | DEBOLE | 8,1 | n/d |
| -15,00% | 0,06128 $ | 30/40 | +75,00% | +20,00% | 0,08651 $ | 0/30 | 0,00% | +41,18% | DEBOLE | 8,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07569 $ | 18/40 | +45,00% | prezzo iniziale | 0,07209 $ | 15/18 | +83,33% | -4,76% | ALTA | 3,0 | 9,7 |
| +5,00% | 0,07569 $ | 18/40 | +45,00% | -5,00% | 0,06849 $ | 11/18 | +61,11% | -9,52% | MEDIA | 3,0 | 9,1 |
| +5,00% | 0,07569 $ | 18/40 | +45,00% | -8,00% | 0,06632 $ | 11/18 | +61,11% | -12,38% | MEDIA | 3,0 | 10,1 |
| +5,00% | 0,07569 $ | 18/40 | +45,00% | -10,00% | 0,06488 $ | 9/18 | +50,00% | -14,29% | MEDIA | 3,0 | 11,4 |
| +5,00% | 0,07569 $ | 18/40 | +45,00% | -15,00% | 0,06128 $ | 8/18 | +44,44% | -19,05% | BASSA | 3,0 | 10,4 |
| +10,00% | 0,07930 $ | 14/40 | +35,00% | prezzo iniziale | 0,07209 $ | 10/14 | +71,43% | -9,09% | ALTA | 9,1 | 14,0 |
| +10,00% | 0,07930 $ | 14/40 | +35,00% | -5,00% | 0,06849 $ | 6/14 | +42,86% | -13,64% | BASSA | 9,1 | 11,8 |
| +10,00% | 0,07930 $ | 14/40 | +35,00% | -8,00% | 0,06632 $ | 6/14 | +42,86% | -16,36% | BASSA | 9,1 | 12,7 |
| +10,00% | 0,07930 $ | 14/40 | +35,00% | -10,00% | 0,06488 $ | 5/14 | +35,71% | -18,18% | BASSA | 9,1 | 14,4 |
| +10,00% | 0,07930 $ | 14/40 | +35,00% | -15,00% | 0,06128 $ | 4/14 | +28,57% | -22,73% | DEBOLE | 9,1 | 13,2 |
| +15,00% | 0,08290 $ | 10/40 | +25,00% | prezzo iniziale | 0,07209 $ | 5/10 | +50,00% | -13,04% | MEDIA | 12,8 | 18,4 |
| +15,00% | 0,08290 $ | 10/40 | +25,00% | -5,00% | 0,06849 $ | 3/10 | +30,00% | -17,39% | DEBOLE | 12,8 | 20,3 |
| +15,00% | 0,08290 $ | 10/40 | +25,00% | -8,00% | 0,06632 $ | 2/10 | +20,00% | -20,00% | DEBOLE | 12,8 | 17,0 |
| +15,00% | 0,08290 $ | 10/40 | +25,00% | -10,00% | 0,06488 $ | 2/10 | +20,00% | -21,74% | DEBOLE | 12,8 | 17,0 |
| +15,00% | 0,08290 $ | 10/40 | +25,00% | -15,00% | 0,06128 $ | 2/10 | +20,00% | -26,09% | DEBOLE | 12,8 | 17,5 |
| +20,00% | 0,08651 $ | 6/40 | +15,00% | prezzo iniziale | 0,07209 $ | 2/6 | +33,33% | -16,67% | DEBOLE | 11,8 | 11,5 |
| +20,00% | 0,08651 $ | 6/40 | +15,00% | -5,00% | 0,06849 $ | 2/6 | +33,33% | -20,83% | DEBOLE | 11,8 | 17,5 |
| +20,00% | 0,08651 $ | 6/40 | +15,00% | -8,00% | 0,06632 $ | 1/6 | +16,67% | -23,33% | DEBOLE | 11,8 | 8,0 |
| +20,00% | 0,08651 $ | 6/40 | +15,00% | -10,00% | 0,06488 $ | 1/6 | +16,67% | -25,00% | DEBOLE | 11,8 | 8,0 |
| +20,00% | 0,08651 $ | 6/40 | +15,00% | -15,00% | 0,06128 $ | 1/6 | +16,67% | -29,17% | DEBOLE | 11,8 | 9,0 |

---
