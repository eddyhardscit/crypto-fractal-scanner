# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-08 07:17:45 CEST**  
UTC: **2026-08-08 05:17:45 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.712 $ | 71.456 $ | +46,15% | +15,79% | rimbalzo debole | 71.456 $ | 61.712 $ | +3,45% | -13,64% | spike storicamente più resistente |
| SOL | 70,85 $ | 82,04 $ | +37,50% | +15,79% | rimbalzo debole | 82,04 $ | 70,85 $ | +6,45% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06659 $ | 0,07710 $ | +50,00% | +15,79% | rimbalzo possibile | 0,07710 $ | 0,06659 $ | +7,14% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 13 prima sono scesi a -5,00%. Tra quei 13, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +46,15% (6/13). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 1 poi sono scaricati a -5,00%. Percentuale: +3,45% (1/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.712 $ | 13/40 | +32,50% | +5,00% | 68.208 $ | 8/13 | +61,54% | +10,53% | MEDIA | 9,1 | 19,9 |
| -5,00% | 61.712 $ | 13/40 | +32,50% | +10,00% | 71.456 $ | 6/13 | +46,15% | +15,79% | BASSA | 9,1 | 19,3 |
| -5,00% | 61.712 $ | 13/40 | +32,50% | +15,00% | 74.704 $ | 4/13 | +30,77% | +21,05% | DEBOLE | 9,1 | 21,5 |
| -5,00% | 61.712 $ | 13/40 | +32,50% | +20,00% | 77.952 $ | 3/13 | +23,08% | +26,32% | DEBOLE | 9,1 | 19,7 |
| -8,00% | 59.763 $ | 9/40 | +22,50% | +5,00% | 68.208 $ | 4/9 | +44,44% | +14,13% | BASSA | 12,7 | 21,2 |
| -8,00% | 59.763 $ | 9/40 | +22,50% | +10,00% | 71.456 $ | 3/9 | +33,33% | +19,57% | DEBOLE | 12,7 | 23,0 |
| -8,00% | 59.763 $ | 9/40 | +22,50% | +15,00% | 74.704 $ | 2/9 | +22,22% | +25,00% | DEBOLE | 12,7 | 26,0 |
| -8,00% | 59.763 $ | 9/40 | +22,50% | +20,00% | 77.952 $ | 1/9 | +11,11% | +30,43% | DEBOLE | 12,7 | 25,0 |
| -10,00% | 58.464 $ | 8/40 | +20,00% | +5,00% | 68.208 $ | 3/8 | +37,50% | +16,67% | BASSA | 14,4 | 23,3 |
| -10,00% | 58.464 $ | 8/40 | +20,00% | +10,00% | 71.456 $ | 2/8 | +25,00% | +22,22% | DEBOLE | 14,4 | 25,5 |
| -10,00% | 58.464 $ | 8/40 | +20,00% | +15,00% | 74.704 $ | 1/8 | +12,50% | +27,78% | DEBOLE | 14,4 | 29,0 |
| -10,00% | 58.464 $ | 8/40 | +20,00% | +20,00% | 77.952 $ | 0/8 | 0,00% | +33,33% | DEBOLE | 14,4 | n/d |
| -15,00% | 55.216 $ | 4/40 | +10,00% | +5,00% | 68.208 $ | 1/4 | +25,00% | +23,53% | DEBOLE | 16,2 | 23,0 |
| -15,00% | 55.216 $ | 4/40 | +10,00% | +10,00% | 71.456 $ | 0/4 | 0,00% | +29,41% | DEBOLE | 16,2 | n/d |
| -15,00% | 55.216 $ | 4/40 | +10,00% | +15,00% | 74.704 $ | 0/4 | 0,00% | +35,29% | DEBOLE | 16,2 | n/d |
| -15,00% | 55.216 $ | 4/40 | +10,00% | +20,00% | 77.952 $ | 0/4 | 0,00% | +41,18% | DEBOLE | 16,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 68.208 $ | 36/40 | +90,00% | prezzo iniziale | 64.960 $ | 3/36 | +8,33% | -4,76% | DEBOLE | 8,7 | 16,3 |
| +5,00% | 68.208 $ | 36/40 | +90,00% | -5,00% | 61.712 $ | 3/36 | +8,33% | -9,52% | DEBOLE | 8,7 | 20,3 |
| +5,00% | 68.208 $ | 36/40 | +90,00% | -8,00% | 59.763 $ | 3/36 | +8,33% | -12,38% | DEBOLE | 8,7 | 21,0 |
| +5,00% | 68.208 $ | 36/40 | +90,00% | -10,00% | 58.464 $ | 3/36 | +8,33% | -14,29% | DEBOLE | 8,7 | 22,0 |
| +5,00% | 68.208 $ | 36/40 | +90,00% | -15,00% | 55.216 $ | 0/36 | 0,00% | -19,05% | DEBOLE | 8,7 | n/d |
| +10,00% | 71.456 $ | 29/40 | +72,50% | prezzo iniziale | 64.960 $ | 1/29 | +3,45% | -9,09% | DEBOLE | 13,5 | 12,0 |
| +10,00% | 71.456 $ | 29/40 | +72,50% | -5,00% | 61.712 $ | 1/29 | +3,45% | -13,64% | DEBOLE | 13,5 | 19,0 |
| +10,00% | 71.456 $ | 29/40 | +72,50% | -8,00% | 59.763 $ | 1/29 | +3,45% | -16,36% | DEBOLE | 13,5 | 21,0 |
| +10,00% | 71.456 $ | 29/40 | +72,50% | -10,00% | 58.464 $ | 1/29 | +3,45% | -18,18% | DEBOLE | 13,5 | 22,0 |
| +10,00% | 71.456 $ | 29/40 | +72,50% | -15,00% | 55.216 $ | 0/29 | 0,00% | -22,73% | DEBOLE | 13,5 | n/d |
| +15,00% | 74.704 $ | 23/40 | +57,50% | prezzo iniziale | 64.960 $ | 0/23 | 0,00% | -13,04% | DEBOLE | 15,7 | n/d |
| +15,00% | 74.704 $ | 23/40 | +57,50% | -5,00% | 61.712 $ | 0/23 | 0,00% | -17,39% | DEBOLE | 15,7 | n/d |
| +15,00% | 74.704 $ | 23/40 | +57,50% | -8,00% | 59.763 $ | 0/23 | 0,00% | -20,00% | DEBOLE | 15,7 | n/d |
| +15,00% | 74.704 $ | 23/40 | +57,50% | -10,00% | 58.464 $ | 0/23 | 0,00% | -21,74% | DEBOLE | 15,7 | n/d |
| +15,00% | 74.704 $ | 23/40 | +57,50% | -15,00% | 55.216 $ | 0/23 | 0,00% | -26,09% | DEBOLE | 15,7 | n/d |
| +20,00% | 77.952 $ | 19/40 | +47,50% | prezzo iniziale | 64.960 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 15,9 | n/d |
| +20,00% | 77.952 $ | 19/40 | +47,50% | -5,00% | 61.712 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 15,9 | n/d |
| +20,00% | 77.952 $ | 19/40 | +47,50% | -8,00% | 59.763 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 15,9 | n/d |
| +20,00% | 77.952 $ | 19/40 | +47,50% | -10,00% | 58.464 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 15,9 | n/d |
| +20,00% | 77.952 $ | 19/40 | +47,50% | -15,00% | 55.216 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 15,9 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +37,50% (6/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 2 poi sono scaricati a -5,00%. Percentuale: +6,45% (2/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 70,85 $ | 16/40 | +40,00% | +5,00% | 78,31 $ | 8/16 | +50,00% | +10,53% | MEDIA | 8,7 | 24,0 |
| -5,00% | 70,85 $ | 16/40 | +40,00% | +10,00% | 82,04 $ | 6/16 | +37,50% | +15,79% | BASSA | 8,7 | 24,3 |
| -5,00% | 70,85 $ | 16/40 | +40,00% | +15,00% | 85,77 $ | 5/16 | +31,25% | +21,05% | DEBOLE | 8,7 | 24,4 |
| -5,00% | 70,85 $ | 16/40 | +40,00% | +20,00% | 89,50 $ | 3/16 | +18,75% | +26,32% | DEBOLE | 8,7 | 23,7 |
| -8,00% | 68,61 $ | 15/40 | +37,50% | +5,00% | 78,31 $ | 7/15 | +46,67% | +14,13% | BASSA | 10,9 | 23,6 |
| -8,00% | 68,61 $ | 15/40 | +37,50% | +10,00% | 82,04 $ | 5/15 | +33,33% | +19,57% | DEBOLE | 10,9 | 23,4 |
| -8,00% | 68,61 $ | 15/40 | +37,50% | +15,00% | 85,77 $ | 4/15 | +26,67% | +25,00% | DEBOLE | 10,9 | 23,2 |
| -8,00% | 68,61 $ | 15/40 | +37,50% | +20,00% | 89,50 $ | 3/15 | +20,00% | +30,43% | DEBOLE | 10,9 | 23,7 |
| -10,00% | 67,12 $ | 14/40 | +35,00% | +5,00% | 78,31 $ | 7/14 | +50,00% | +16,67% | MEDIA | 10,6 | 23,6 |
| -10,00% | 67,12 $ | 14/40 | +35,00% | +10,00% | 82,04 $ | 5/14 | +35,71% | +22,22% | BASSA | 10,6 | 23,4 |
| -10,00% | 67,12 $ | 14/40 | +35,00% | +15,00% | 85,77 $ | 4/14 | +28,57% | +27,78% | DEBOLE | 10,6 | 23,2 |
| -10,00% | 67,12 $ | 14/40 | +35,00% | +20,00% | 89,50 $ | 3/14 | +21,43% | +33,33% | DEBOLE | 10,6 | 23,7 |
| -15,00% | 63,39 $ | 6/40 | +15,00% | +5,00% | 78,31 $ | 3/6 | +50,00% | +23,53% | MEDIA | 13,0 | 25,3 |
| -15,00% | 63,39 $ | 6/40 | +15,00% | +10,00% | 82,04 $ | 2/6 | +33,33% | +29,41% | DEBOLE | 13,0 | 27,5 |
| -15,00% | 63,39 $ | 6/40 | +15,00% | +15,00% | 85,77 $ | 2/6 | +33,33% | +35,29% | DEBOLE | 13,0 | 27,5 |
| -15,00% | 63,39 $ | 6/40 | +15,00% | +20,00% | 89,50 $ | 1/6 | +16,67% | +41,18% | DEBOLE | 13,0 | 30,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 78,31 $ | 35/40 | +87,50% | prezzo iniziale | 74,58 $ | 7/35 | +20,00% | -4,76% | DEBOLE | 9,9 | 13,6 |
| +5,00% | 78,31 $ | 35/40 | +87,50% | -5,00% | 70,85 $ | 3/35 | +8,57% | -9,52% | DEBOLE | 9,9 | 12,7 |
| +5,00% | 78,31 $ | 35/40 | +87,50% | -8,00% | 68,61 $ | 3/35 | +8,57% | -12,38% | DEBOLE | 9,9 | 13,0 |
| +5,00% | 78,31 $ | 35/40 | +87,50% | -10,00% | 67,12 $ | 3/35 | +8,57% | -14,29% | DEBOLE | 9,9 | 15,3 |
| +5,00% | 78,31 $ | 35/40 | +87,50% | -15,00% | 63,39 $ | 1/35 | +2,86% | -19,05% | DEBOLE | 9,9 | 11,0 |
| +10,00% | 82,04 $ | 31/40 | +77,50% | prezzo iniziale | 74,58 $ | 4/31 | +12,90% | -9,09% | DEBOLE | 14,1 | 15,0 |
| +10,00% | 82,04 $ | 31/40 | +77,50% | -5,00% | 70,85 $ | 2/31 | +6,45% | -13,64% | DEBOLE | 14,1 | 11,5 |
| +10,00% | 82,04 $ | 31/40 | +77,50% | -8,00% | 68,61 $ | 2/31 | +6,45% | -16,36% | DEBOLE | 14,1 | 12,0 |
| +10,00% | 82,04 $ | 31/40 | +77,50% | -10,00% | 67,12 $ | 2/31 | +6,45% | -18,18% | DEBOLE | 14,1 | 14,5 |
| +10,00% | 82,04 $ | 31/40 | +77,50% | -15,00% | 63,39 $ | 1/31 | +3,23% | -22,73% | DEBOLE | 14,1 | 11,0 |
| +15,00% | 85,77 $ | 23/40 | +57,50% | prezzo iniziale | 74,58 $ | 2/23 | +8,70% | -13,04% | DEBOLE | 15,5 | 20,5 |
| +15,00% | 85,77 $ | 23/40 | +57,50% | -5,00% | 70,85 $ | 0/23 | 0,00% | -17,39% | DEBOLE | 15,5 | n/d |
| +15,00% | 85,77 $ | 23/40 | +57,50% | -8,00% | 68,61 $ | 0/23 | 0,00% | -20,00% | DEBOLE | 15,5 | n/d |
| +15,00% | 85,77 $ | 23/40 | +57,50% | -10,00% | 67,12 $ | 0/23 | 0,00% | -21,74% | DEBOLE | 15,5 | n/d |
| +15,00% | 85,77 $ | 23/40 | +57,50% | -15,00% | 63,39 $ | 0/23 | 0,00% | -26,09% | DEBOLE | 15,5 | n/d |
| +20,00% | 89,50 $ | 19/40 | +47,50% | prezzo iniziale | 74,58 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 16,2 | n/d |
| +20,00% | 89,50 $ | 19/40 | +47,50% | -5,00% | 70,85 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 16,2 | n/d |
| +20,00% | 89,50 $ | 19/40 | +47,50% | -8,00% | 68,61 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 16,2 | n/d |
| +20,00% | 89,50 $ | 19/40 | +47,50% | -10,00% | 67,12 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 16,2 | n/d |
| +20,00% | 89,50 $ | 19/40 | +47,50% | -15,00% | 63,39 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 16,2 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (14/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 2 poi sono scaricati a -5,00%. Percentuale: +7,14% (2/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +5,00% | 0,07359 $ | 14/28 | +50,00% | +10,53% | MEDIA | 5,3 | 15,9 |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +10,00% | 0,07710 $ | 14/28 | +50,00% | +15,79% | MEDIA | 5,3 | 18,2 |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +15,00% | 0,08060 $ | 13/28 | +46,43% | +21,05% | BASSA | 5,3 | 21,0 |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +20,00% | 0,08411 $ | 9/28 | +32,14% | +26,32% | DEBOLE | 5,3 | 22,8 |
| -8,00% | 0,06448 $ | 24/40 | +60,00% | +5,00% | 0,07359 $ | 10/24 | +41,67% | +14,13% | BASSA | 7,3 | 17,6 |
| -8,00% | 0,06448 $ | 24/40 | +60,00% | +10,00% | 0,07710 $ | 10/24 | +41,67% | +19,57% | BASSA | 7,3 | 19,5 |
| -8,00% | 0,06448 $ | 24/40 | +60,00% | +15,00% | 0,08060 $ | 9/24 | +37,50% | +25,00% | BASSA | 7,3 | 22,3 |
| -8,00% | 0,06448 $ | 24/40 | +60,00% | +20,00% | 0,08411 $ | 6/24 | +25,00% | +30,43% | DEBOLE | 7,3 | 24,0 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +5,00% | 0,07359 $ | 8/22 | +36,36% | +16,67% | BASSA | 7,0 | 17,6 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +10,00% | 0,07710 $ | 8/22 | +36,36% | +22,22% | BASSA | 7,0 | 19,9 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +15,00% | 0,08060 $ | 7/22 | +31,82% | +27,78% | DEBOLE | 7,0 | 23,3 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +20,00% | 0,08411 $ | 5/22 | +22,73% | +33,33% | DEBOLE | 7,0 | 25,2 |
| -15,00% | 0,05958 $ | 16/40 | +40,00% | +5,00% | 0,07359 $ | 3/16 | +18,75% | +23,53% | DEBOLE | 6,1 | 18,0 |
| -15,00% | 0,05958 $ | 16/40 | +40,00% | +10,00% | 0,07710 $ | 3/16 | +18,75% | +29,41% | DEBOLE | 6,1 | 19,0 |
| -15,00% | 0,05958 $ | 16/40 | +40,00% | +15,00% | 0,08060 $ | 3/16 | +18,75% | +35,29% | DEBOLE | 6,1 | 21,3 |
| -15,00% | 0,05958 $ | 16/40 | +40,00% | +20,00% | 0,08411 $ | 2/16 | +12,50% | +41,18% | DEBOLE | 6,1 | 26,5 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07359 $ | 30/40 | +75,00% | prezzo iniziale | 0,07009 $ | 19/30 | +63,33% | -4,76% | MEDIA | 9,2 | 14,5 |
| +5,00% | 0,07359 $ | 30/40 | +75,00% | -5,00% | 0,06659 $ | 8/30 | +26,67% | -9,52% | DEBOLE | 9,2 | 11,2 |
| +5,00% | 0,07359 $ | 30/40 | +75,00% | -8,00% | 0,06448 $ | 7/30 | +23,33% | -12,38% | DEBOLE | 9,2 | 11,4 |
| +5,00% | 0,07359 $ | 30/40 | +75,00% | -10,00% | 0,06308 $ | 7/30 | +23,33% | -14,29% | DEBOLE | 9,2 | 11,9 |
| +5,00% | 0,07359 $ | 30/40 | +75,00% | -15,00% | 0,05958 $ | 3/30 | +10,00% | -19,05% | DEBOLE | 9,2 | 8,7 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | prezzo iniziale | 0,07009 $ | 13/28 | +46,43% | -9,09% | BASSA | 14,1 | 19,7 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -5,00% | 0,06659 $ | 2/28 | +7,14% | -13,64% | DEBOLE | 14,1 | 17,5 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -8,00% | 0,06448 $ | 2/28 | +7,14% | -16,36% | DEBOLE | 14,1 | 17,5 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -10,00% | 0,06308 $ | 2/28 | +7,14% | -18,18% | DEBOLE | 14,1 | 18,5 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -15,00% | 0,05958 $ | 1/28 | +3,57% | -22,73% | DEBOLE | 14,1 | 9,0 |
| +15,00% | 0,08060 $ | 24/40 | +60,00% | prezzo iniziale | 0,07009 $ | 5/24 | +20,83% | -13,04% | DEBOLE | 18,7 | 19,8 |
| +15,00% | 0,08060 $ | 24/40 | +60,00% | -5,00% | 0,06659 $ | 0/24 | 0,00% | -17,39% | DEBOLE | 18,7 | n/d |
| +15,00% | 0,08060 $ | 24/40 | +60,00% | -8,00% | 0,06448 $ | 0/24 | 0,00% | -20,00% | DEBOLE | 18,7 | n/d |
| +15,00% | 0,08060 $ | 24/40 | +60,00% | -10,00% | 0,06308 $ | 0/24 | 0,00% | -21,74% | DEBOLE | 18,7 | n/d |
| +15,00% | 0,08060 $ | 24/40 | +60,00% | -15,00% | 0,05958 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 18,7 | n/d |
| +20,00% | 0,08411 $ | 20/40 | +50,00% | prezzo iniziale | 0,07009 $ | 3/20 | +15,00% | -16,67% | DEBOLE | 21,5 | 23,7 |
| +20,00% | 0,08411 $ | 20/40 | +50,00% | -5,00% | 0,06659 $ | 0/20 | 0,00% | -20,83% | DEBOLE | 21,5 | n/d |
| +20,00% | 0,08411 $ | 20/40 | +50,00% | -8,00% | 0,06448 $ | 0/20 | 0,00% | -23,33% | DEBOLE | 21,5 | n/d |
| +20,00% | 0,08411 $ | 20/40 | +50,00% | -10,00% | 0,06308 $ | 0/20 | 0,00% | -25,00% | DEBOLE | 21,5 | n/d |
| +20,00% | 0,08411 $ | 20/40 | +50,00% | -15,00% | 0,05958 $ | 0/20 | 0,00% | -29,17% | DEBOLE | 21,5 | n/d |

---
