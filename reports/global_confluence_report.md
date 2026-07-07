# Sintesi finale di confluenza

Generato: 2026-07-07 22:45 UTC

Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.

Moduli letti:

- Scanner frattale/statistico a 30 giorni
- Market regime match
- Struttura tecnica classica
- Frattale BTC 2022 vs SOL 2026, solo per SOL
- RSI top-cycle, soprattutto per SOL
- Futures / liquidazioni
- Cambiamento giornaliero

## Sintesi operativa

| Asset   |   Punteggio | Confluenza             | Bias                           | Affidabilità   | Azione coerente                                    | Conferme                                                                                       | Invalidazioni                                |
|:--------|------------:|:-----------------------|:-------------------------------|:---------------|:---------------------------------------------------|:-----------------------------------------------------------------------------------------------|:---------------------------------------------|
| BTC     |          +6 | MODERATAMENTE POSITIVA | Costruttivo prudente           | MEDIA / ALTA   | ACCUMULA SU PULLBACK / NO SHORT                    | Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile. | Sotto 57.748 il quadro tecnico peggiora.     |
| SOL     |           0 | PARZIALE / MISTA       | Interessante ma non confermato | BASSA / MEDIA  | HOLD / SOLO ANTICIPO A TRANCHE, NO LEVA            | Conferme sopra 87,79 / 109,57 / 119,44.                                                        | Allarmi sotto 76,91 / 64,42 / 62,19.         |
| DOGE    |          -7 | NEGATIVA               | Ribassista                     | MEDIA / ALTA   | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.09169 migliora, ma resta asset debole finché scanner e struttura non girano.           | Sotto 0.06961 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset   |   Scanner |   Market regime |   Tecnico |   Frattale SOL |   RSI top-cycle |   Futures |   Daily change |   Totale |
|:--------|----------:|----------------:|----------:|---------------:|----------------:|----------:|---------------:|---------:|
| BTC     |        +2 |              +3 |         0 |              0 |               0 |         0 |             +1 |       +6 |
| SOL     |        -1 |              +1 |        -2 |             +1 |              +1 |         0 |              0 |        0 |
| DOGE    |        -2 |              -3 |        -2 |              0 |               0 |         0 |              0 |       -7 |

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+6**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **ACCUMULA SU PULLBACK / NO SHORT**

BTC è l'asset messo meglio nel breve. La struttura macro non è ancora pienamente rialzista, ma scanner, regime e segnali tecnici interni sono abbastanza coerenti per un recupero prudente.

Dettaglio moduli:

- Scanner 30g: **+2** — Casi positivi 62,50%, return centrale 30g n/a.
- Market regime: **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 14, positivi 30g 78,57%, return p50 10,58%.
- Tecnico: **0** — Score tecnico -1/12, verdetto NEUTRALE_MISTO, trend BEARISH_TREND, struttura LH_LL_DOWNSTRUCTURE, divergenza BULLISH_RSI_DIVERGENCE, Wyckoff ACCUMULATION_CANDIDATE.
- Frattale SOL/BTC: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Futures/liquidazioni: **0** — Lettura futures Misto, forza 1/5.
- Cambiamento giornaliero: **+1** — - BTC: cambiamento importante in miglioramento rispetto a ieri.

Conferme: Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **PARZIALE / MISTA**
- Bias: **Interessante ma non confermato**
- Punteggio finale: **0**
- Affidabilità: **BASSA / MEDIA**
- Azione coerente: **HOLD / SOLO ANTICIPO A TRANCHE, NO LEVA**

SOL è interessante ma non confermato. Il frattale e alcuni filtri aiutano, ma scanner e struttura tecnica non danno ancora una conferma pulita.

Dettaglio moduli:

- Scanner 30g: **-1** — Casi positivi 47,50%, return centrale 30g n/a.
- Market regime: **+1** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 24, positivi 30g 58,33%, return p50 0,80%.
- Tecnico: **-2** — Score tecnico -3/12, verdetto DEBOLE, trend MIXED_TREND, struttura LH_LL_DOWNSTRUCTURE, divergenza NONE, Wyckoff RANGE_OR_UNKNOWN.
- Frattale SOL/BTC: **+1** — Verdetto PARZIALMENTE SI, somiglianza n/a, tracking FRATTALE STABILE
-, fase FASE ANTICIPATA
-, rischio MEDIO / ALTO
-.
- RSI top-cycle: **+1** — Rischio top-cycle RSI: BASSO.
- Futures/liquidazioni: **0** — Lettura futures Misto, forza 1/5.
- Cambiamento giornaliero: **0** — - SOL: nessun cambiamento forte rispetto a ieri.

Conferme: Conferme sopra 87,79 / 109,57 / 119,44.

Invalidazioni: Allarmi sotto 76,91 / 64,42 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-7**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche se può fare rimbalzi o spike, la confluenza generale resta negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Scanner 30g: **-2** — Casi positivi 17,50%, return centrale 30g n/a.
- Market regime: **-3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 30, positivi 30g 16,67%, return p50 -25,19%.
- Tecnico: **-2** — Score tecnico -5/12, verdetto DEBOLE, trend BEARISH_TREND, struttura LH_LL_DOWNSTRUCTURE, divergenza NONE, Wyckoff ACCUMULATION_CANDIDATE.
- Frattale SOL/BTC: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Futures/liquidazioni: **0** — Lettura futures Misto, forza 1/5.
- Cambiamento giornaliero: **0** — - DOGE: nessun cambiamento forte rispetto a ieri.

Conferme: Sopra 0.09169 migliora, ma resta asset debole finché scanner e struttura non girano.

Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.

## Come leggere il punteggio

- +7 o più: confluenza positiva forte.
- Da +3 a +6: confluenza moderatamente positiva.
- Da 0 a +2: confluenza parziale o mista.
- Da -1 a -3: confluenza debole o fragile.
- -4 o meno: confluenza negativa.

Nota: questo report non sostituisce i singoli report. Serve a capire se i segnali si aiutano tra loro o se sono in conflitto.

