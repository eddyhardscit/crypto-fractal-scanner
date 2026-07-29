# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-29 07:14:01 CEST**  
UTC: **2026-07-29 05:14:01 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.726 $ | 70.314 $ | +36,84% | +15,79% | rimbalzo debole | 70.314 $ | 60.726 $ | +3,85% | -13,64% | spike storicamente più resistente |
| SOL | 69,80 $ | 80,82 $ | +31,58% | +15,79% | rimbalzo poco frequente | 80,82 $ | 69,80 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06708 $ | 0,07767 $ | +36,67% | +15,79% | rimbalzo debole | 0,07767 $ | 0,06708 $ | +55,17% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +36,84% (7/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 1 poi sono scaricati a -5,00%. Percentuale: +3,85% (1/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.726 $ | 19/40 | +47,50% | +5,00% | 67.118 $ | 8/19 | +42,11% | +10,53% | BASSA | 4,2 | 17,0 |
| -5,00% | 60.726 $ | 19/40 | +47,50% | +10,00% | 70.314 $ | 7/19 | +36,84% | +15,79% | BASSA | 4,2 | 17,3 |
| -5,00% | 60.726 $ | 19/40 | +47,50% | +15,00% | 73.510 $ | 7/19 | +36,84% | +21,05% | BASSA | 4,2 | 18,9 |
| -5,00% | 60.726 $ | 19/40 | +47,50% | +20,00% | 76.706 $ | 7/19 | +36,84% | +26,32% | BASSA | 4,2 | 22,0 |
| -8,00% | 58.808 $ | 16/40 | +40,00% | +5,00% | 67.118 $ | 5/16 | +31,25% | +14,13% | DEBOLE | 6,9 | 20,6 |
| -8,00% | 58.808 $ | 16/40 | +40,00% | +10,00% | 70.314 $ | 4/16 | +25,00% | +19,57% | DEBOLE | 6,9 | 21,5 |
| -8,00% | 58.808 $ | 16/40 | +40,00% | +15,00% | 73.510 $ | 4/16 | +25,00% | +25,00% | DEBOLE | 6,9 | 23,8 |
| -8,00% | 58.808 $ | 16/40 | +40,00% | +20,00% | 76.706 $ | 4/16 | +25,00% | +30,43% | DEBOLE | 6,9 | 26,8 |
| -10,00% | 57.529 $ | 13/40 | +32,50% | +5,00% | 67.118 $ | 2/13 | +15,38% | +16,67% | DEBOLE | 7,8 | 29,5 |
| -10,00% | 57.529 $ | 13/40 | +32,50% | +10,00% | 70.314 $ | 1/13 | +7,69% | +22,22% | DEBOLE | 7,8 | 30,0 |
| -10,00% | 57.529 $ | 13/40 | +32,50% | +15,00% | 73.510 $ | 1/13 | +7,69% | +27,78% | DEBOLE | 7,8 | 30,0 |
| -10,00% | 57.529 $ | 13/40 | +32,50% | +20,00% | 76.706 $ | 1/13 | +7,69% | +33,33% | DEBOLE | 7,8 | 30,0 |
| -15,00% | 54.333 $ | 12/40 | +30,00% | +5,00% | 67.118 $ | 1/12 | +8,33% | +23,53% | DEBOLE | 9,7 | 29,0 |
| -15,00% | 54.333 $ | 12/40 | +30,00% | +10,00% | 70.314 $ | 1/12 | +8,33% | +29,41% | DEBOLE | 9,7 | 30,0 |
| -15,00% | 54.333 $ | 12/40 | +30,00% | +15,00% | 73.510 $ | 1/12 | +8,33% | +35,29% | DEBOLE | 9,7 | 30,0 |
| -15,00% | 54.333 $ | 12/40 | +30,00% | +20,00% | 76.706 $ | 1/12 | +8,33% | +41,18% | DEBOLE | 9,7 | 30,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.118 $ | 29/40 | +72,50% | prezzo iniziale | 63.922 $ | 3/29 | +10,34% | -4,76% | DEBOLE | 10,6 | 6,3 |
| +5,00% | 67.118 $ | 29/40 | +72,50% | -5,00% | 60.726 $ | 2/29 | +6,90% | -9,52% | DEBOLE | 10,6 | 7,5 |
| +5,00% | 67.118 $ | 29/40 | +72,50% | -8,00% | 58.808 $ | 2/29 | +6,90% | -12,38% | DEBOLE | 10,6 | 9,0 |
| +5,00% | 67.118 $ | 29/40 | +72,50% | -10,00% | 57.529 $ | 1/29 | +3,45% | -14,29% | DEBOLE | 10,6 | 12,0 |
| +5,00% | 67.118 $ | 29/40 | +72,50% | -15,00% | 54.333 $ | 1/29 | +3,45% | -19,05% | DEBOLE | 10,6 | 12,0 |
| +10,00% | 70.314 $ | 26/40 | +65,00% | prezzo iniziale | 63.922 $ | 1/26 | +3,85% | -9,09% | DEBOLE | 13,9 | 9,0 |
| +10,00% | 70.314 $ | 26/40 | +65,00% | -5,00% | 60.726 $ | 1/26 | +3,85% | -13,64% | DEBOLE | 13,9 | 10,0 |
| +10,00% | 70.314 $ | 26/40 | +65,00% | -8,00% | 58.808 $ | 1/26 | +3,85% | -16,36% | DEBOLE | 13,9 | 12,0 |
| +10,00% | 70.314 $ | 26/40 | +65,00% | -10,00% | 57.529 $ | 1/26 | +3,85% | -18,18% | DEBOLE | 13,9 | 12,0 |
| +10,00% | 70.314 $ | 26/40 | +65,00% | -15,00% | 54.333 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 13,9 | 12,0 |
| +15,00% | 73.510 $ | 23/40 | +57,50% | prezzo iniziale | 63.922 $ | 1/23 | +4,35% | -13,04% | DEBOLE | 15,7 | 9,0 |
| +15,00% | 73.510 $ | 23/40 | +57,50% | -5,00% | 60.726 $ | 1/23 | +4,35% | -17,39% | DEBOLE | 15,7 | 10,0 |
| +15,00% | 73.510 $ | 23/40 | +57,50% | -8,00% | 58.808 $ | 1/23 | +4,35% | -20,00% | DEBOLE | 15,7 | 12,0 |
| +15,00% | 73.510 $ | 23/40 | +57,50% | -10,00% | 57.529 $ | 1/23 | +4,35% | -21,74% | DEBOLE | 15,7 | 12,0 |
| +15,00% | 73.510 $ | 23/40 | +57,50% | -15,00% | 54.333 $ | 1/23 | +4,35% | -26,09% | DEBOLE | 15,7 | 12,0 |
| +20,00% | 76.706 $ | 19/40 | +47,50% | prezzo iniziale | 63.922 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.706 $ | 19/40 | +47,50% | -5,00% | 60.726 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.706 $ | 19/40 | +47,50% | -8,00% | 58.808 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.706 $ | 19/40 | +47,50% | -10,00% | 57.529 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.706 $ | 19/40 | +47,50% | -15,00% | 54.333 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 17,9 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +31,58% (6/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 69,80 $ | 19/40 | +47,50% | +5,00% | 77,14 $ | 9/19 | +47,37% | +10,53% | BASSA | 8,1 | 19,7 |
| -5,00% | 69,80 $ | 19/40 | +47,50% | +10,00% | 80,82 $ | 6/19 | +31,58% | +15,79% | DEBOLE | 8,1 | 20,7 |
| -5,00% | 69,80 $ | 19/40 | +47,50% | +15,00% | 84,49 $ | 4/19 | +21,05% | +21,05% | DEBOLE | 8,1 | 19,2 |
| -5,00% | 69,80 $ | 19/40 | +47,50% | +20,00% | 88,16 $ | 3/19 | +15,79% | +26,32% | DEBOLE | 8,1 | 22,0 |
| -8,00% | 67,59 $ | 15/40 | +37,50% | +5,00% | 77,14 $ | 5/15 | +33,33% | +14,13% | DEBOLE | 10,4 | 23,4 |
| -8,00% | 67,59 $ | 15/40 | +37,50% | +10,00% | 80,82 $ | 3/15 | +20,00% | +19,57% | DEBOLE | 10,4 | 25,0 |
| -8,00% | 67,59 $ | 15/40 | +37,50% | +15,00% | 84,49 $ | 2/15 | +13,33% | +25,00% | DEBOLE | 10,4 | 24,5 |
| -8,00% | 67,59 $ | 15/40 | +37,50% | +20,00% | 88,16 $ | 2/15 | +13,33% | +30,43% | DEBOLE | 10,4 | 24,5 |
| -10,00% | 66,12 $ | 14/40 | +35,00% | +5,00% | 77,14 $ | 4/14 | +28,57% | +16,67% | DEBOLE | 11,7 | 23,5 |
| -10,00% | 66,12 $ | 14/40 | +35,00% | +10,00% | 80,82 $ | 2/14 | +14,29% | +22,22% | DEBOLE | 11,7 | 26,0 |
| -10,00% | 66,12 $ | 14/40 | +35,00% | +15,00% | 84,49 $ | 1/14 | +7,14% | +27,78% | DEBOLE | 11,7 | 23,0 |
| -10,00% | 66,12 $ | 14/40 | +35,00% | +20,00% | 88,16 $ | 1/14 | +7,14% | +33,33% | DEBOLE | 11,7 | 23,0 |
| -15,00% | 62,45 $ | 7/40 | +17,50% | +5,00% | 77,14 $ | 0/7 | 0,00% | +23,53% | DEBOLE | 17,0 | n/d |
| -15,00% | 62,45 $ | 7/40 | +17,50% | +10,00% | 80,82 $ | 0/7 | 0,00% | +29,41% | DEBOLE | 17,0 | n/d |
| -15,00% | 62,45 $ | 7/40 | +17,50% | +15,00% | 84,49 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 17,0 | n/d |
| -15,00% | 62,45 $ | 7/40 | +17,50% | +20,00% | 88,16 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 17,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,14 $ | 31/40 | +77,50% | prezzo iniziale | 73,47 $ | 6/31 | +19,35% | -4,76% | DEBOLE | 10,4 | 12,5 |
| +5,00% | 77,14 $ | 31/40 | +77,50% | -5,00% | 69,80 $ | 3/31 | +9,68% | -9,52% | DEBOLE | 10,4 | 12,7 |
| +5,00% | 77,14 $ | 31/40 | +77,50% | -8,00% | 67,59 $ | 2/31 | +6,45% | -12,38% | DEBOLE | 10,4 | 13,0 |
| +5,00% | 77,14 $ | 31/40 | +77,50% | -10,00% | 66,12 $ | 1/31 | +3,23% | -14,29% | DEBOLE | 10,4 | 20,0 |
| +5,00% | 77,14 $ | 31/40 | +77,50% | -15,00% | 62,45 $ | 0/31 | 0,00% | -19,05% | DEBOLE | 10,4 | n/d |
| +10,00% | 80,82 $ | 25/40 | +62,50% | prezzo iniziale | 73,47 $ | 2/25 | +8,00% | -9,09% | DEBOLE | 13,6 | 17,5 |
| +10,00% | 80,82 $ | 25/40 | +62,50% | -5,00% | 69,80 $ | 0/25 | 0,00% | -13,64% | DEBOLE | 13,6 | n/d |
| +10,00% | 80,82 $ | 25/40 | +62,50% | -8,00% | 67,59 $ | 0/25 | 0,00% | -16,36% | DEBOLE | 13,6 | n/d |
| +10,00% | 80,82 $ | 25/40 | +62,50% | -10,00% | 66,12 $ | 0/25 | 0,00% | -18,18% | DEBOLE | 13,6 | n/d |
| +10,00% | 80,82 $ | 25/40 | +62,50% | -15,00% | 62,45 $ | 0/25 | 0,00% | -22,73% | DEBOLE | 13,6 | n/d |
| +15,00% | 84,49 $ | 20/40 | +50,00% | prezzo iniziale | 73,47 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 15,0 | 22,0 |
| +15,00% | 84,49 $ | 20/40 | +50,00% | -5,00% | 69,80 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 15,0 | n/d |
| +15,00% | 84,49 $ | 20/40 | +50,00% | -8,00% | 67,59 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 15,0 | n/d |
| +15,00% | 84,49 $ | 20/40 | +50,00% | -10,00% | 66,12 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 15,0 | n/d |
| +15,00% | 84,49 $ | 20/40 | +50,00% | -15,00% | 62,45 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 15,0 | n/d |
| +20,00% | 88,16 $ | 14/40 | +35,00% | prezzo iniziale | 73,47 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 16,4 | n/d |
| +20,00% | 88,16 $ | 14/40 | +35,00% | -5,00% | 69,80 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 16,4 | n/d |
| +20,00% | 88,16 $ | 14/40 | +35,00% | -8,00% | 67,59 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 16,4 | n/d |
| +20,00% | 88,16 $ | 14/40 | +35,00% | -10,00% | 66,12 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 16,4 | n/d |
| +20,00% | 88,16 $ | 14/40 | +35,00% | -15,00% | 62,45 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 16,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +36,67% (11/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 16 poi sono scaricati a -5,00%. Percentuale: +55,17% (16/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06708 $ | 30/40 | +75,00% | +5,00% | 0,07414 $ | 15/30 | +50,00% | +10,53% | MEDIA | 9,8 | 20,9 |
| -5,00% | 0,06708 $ | 30/40 | +75,00% | +10,00% | 0,07767 $ | 11/30 | +36,67% | +15,79% | BASSA | 9,8 | 20,9 |
| -5,00% | 0,06708 $ | 30/40 | +75,00% | +15,00% | 0,08120 $ | 7/30 | +23,33% | +21,05% | DEBOLE | 9,8 | 17,1 |
| -5,00% | 0,06708 $ | 30/40 | +75,00% | +20,00% | 0,08473 $ | 4/30 | +13,33% | +26,32% | DEBOLE | 9,8 | 14,0 |
| -8,00% | 0,06496 $ | 26/40 | +65,00% | +5,00% | 0,07414 $ | 12/26 | +46,15% | +14,13% | BASSA | 11,2 | 23,0 |
| -8,00% | 0,06496 $ | 26/40 | +65,00% | +10,00% | 0,07767 $ | 8/26 | +30,77% | +19,57% | DEBOLE | 11,2 | 22,2 |
| -8,00% | 0,06496 $ | 26/40 | +65,00% | +15,00% | 0,08120 $ | 4/26 | +15,38% | +25,00% | DEBOLE | 11,2 | 17,0 |
| -8,00% | 0,06496 $ | 26/40 | +65,00% | +20,00% | 0,08473 $ | 2/26 | +7,69% | +30,43% | DEBOLE | 11,2 | 15,5 |
| -10,00% | 0,06355 $ | 23/40 | +57,50% | +5,00% | 0,07414 $ | 9/23 | +39,13% | +16,67% | BASSA | 11,2 | 21,2 |
| -10,00% | 0,06355 $ | 23/40 | +57,50% | +10,00% | 0,07767 $ | 5/23 | +21,74% | +22,22% | DEBOLE | 11,2 | 18,2 |
| -10,00% | 0,06355 $ | 23/40 | +57,50% | +15,00% | 0,08120 $ | 4/23 | +17,39% | +27,78% | DEBOLE | 11,2 | 17,0 |
| -10,00% | 0,06355 $ | 23/40 | +57,50% | +20,00% | 0,08473 $ | 2/23 | +8,70% | +33,33% | DEBOLE | 11,2 | 15,5 |
| -15,00% | 0,06002 $ | 15/40 | +37,50% | +5,00% | 0,07414 $ | 2/15 | +13,33% | +23,53% | DEBOLE | 14,5 | 19,0 |
| -15,00% | 0,06002 $ | 15/40 | +37,50% | +10,00% | 0,07767 $ | 1/15 | +6,67% | +29,41% | DEBOLE | 14,5 | 9,0 |
| -15,00% | 0,06002 $ | 15/40 | +37,50% | +15,00% | 0,08120 $ | 1/15 | +6,67% | +35,29% | DEBOLE | 14,5 | 10,0 |
| -15,00% | 0,06002 $ | 15/40 | +37,50% | +20,00% | 0,08473 $ | 1/15 | +6,67% | +41,18% | DEBOLE | 14,5 | 24,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07414 $ | 35/40 | +87,50% | prezzo iniziale | 0,07061 $ | 27/35 | +77,14% | -4,76% | ALTA | 5,6 | 10,4 |
| +5,00% | 0,07414 $ | 35/40 | +87,50% | -5,00% | 0,06708 $ | 23/35 | +65,71% | -9,52% | ALTA | 5,6 | 13,0 |
| +5,00% | 0,07414 $ | 35/40 | +87,50% | -8,00% | 0,06496 $ | 18/35 | +51,43% | -12,38% | MEDIA | 5,6 | 13,1 |
| +5,00% | 0,07414 $ | 35/40 | +87,50% | -10,00% | 0,06355 $ | 15/35 | +42,86% | -14,29% | BASSA | 5,6 | 13,0 |
| +5,00% | 0,07414 $ | 35/40 | +87,50% | -15,00% | 0,06002 $ | 9/35 | +25,71% | -19,05% | DEBOLE | 5,6 | 16,4 |
| +10,00% | 0,07767 $ | 29/40 | +72,50% | prezzo iniziale | 0,07061 $ | 19/29 | +65,52% | -9,09% | ALTA | 9,5 | 13,6 |
| +10,00% | 0,07767 $ | 29/40 | +72,50% | -5,00% | 0,06708 $ | 16/29 | +55,17% | -13,64% | MEDIA | 9,5 | 15,5 |
| +10,00% | 0,07767 $ | 29/40 | +72,50% | -8,00% | 0,06496 $ | 11/29 | +37,93% | -16,36% | BASSA | 9,5 | 15,8 |
| +10,00% | 0,07767 $ | 29/40 | +72,50% | -10,00% | 0,06355 $ | 8/29 | +27,59% | -18,18% | DEBOLE | 9,5 | 13,6 |
| +10,00% | 0,07767 $ | 29/40 | +72,50% | -15,00% | 0,06002 $ | 7/29 | +24,14% | -22,73% | DEBOLE | 9,5 | 15,1 |
| +15,00% | 0,08120 $ | 19/40 | +47,50% | prezzo iniziale | 0,07061 $ | 8/19 | +42,11% | -13,04% | BASSA | 12,5 | 17,4 |
| +15,00% | 0,08120 $ | 19/40 | +47,50% | -5,00% | 0,06708 $ | 7/19 | +36,84% | -17,39% | BASSA | 12,5 | 17,4 |
| +15,00% | 0,08120 $ | 19/40 | +47,50% | -8,00% | 0,06496 $ | 4/19 | +21,05% | -20,00% | DEBOLE | 12,5 | 17,0 |
| +15,00% | 0,08120 $ | 19/40 | +47,50% | -10,00% | 0,06355 $ | 3/19 | +15,79% | -21,74% | DEBOLE | 12,5 | 15,3 |
| +15,00% | 0,08120 $ | 19/40 | +47,50% | -15,00% | 0,06002 $ | 2/19 | +10,53% | -26,09% | DEBOLE | 12,5 | 16,0 |
| +20,00% | 0,08473 $ | 13/40 | +32,50% | prezzo iniziale | 0,07061 $ | 4/13 | +30,77% | -16,67% | DEBOLE | 12,5 | 21,0 |
| +20,00% | 0,08473 $ | 13/40 | +32,50% | -5,00% | 0,06708 $ | 2/13 | +15,38% | -20,83% | DEBOLE | 12,5 | 18,5 |
| +20,00% | 0,08473 $ | 13/40 | +32,50% | -8,00% | 0,06496 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 12,5 | n/d |
| +20,00% | 0,08473 $ | 13/40 | +32,50% | -10,00% | 0,06355 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 12,5 | n/d |
| +20,00% | 0,08473 $ | 13/40 | +32,50% | -15,00% | 0,06002 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 12,5 | n/d |

---
