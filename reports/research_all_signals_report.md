## 🔬 Research All Signals

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **RANGE**
- Famiglia: **RANGE**
- Confidenza: **80,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +1.0, breadth EMA50 17%, ADX 25.5.
- BTC trend score: **1,00**; ADX: **25,52**; breadth sopra EMA50: **16,67%**
- Mediana alt vs BTC: **-0,48%**; dispersione: **8,66%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **28**
- Trade research chiusi: **60**
- Eventi di mercato indipendenti chiusi: **32**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **121**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 4 | 4 | 50,00% | 1,95 | 0,48R | €19,32 |
| SHADOW_1H_BALANCED | 6 | 20 | 20 | 30,00% | 0,78 | -0,16R | €-32,47 |
| SHADOW_1H_FAST | 3 | 23 | 23 | 26,09% | 0,49 | -0,40R | €-93,00 |
| SHADOW_4H_WIDE | 9 | 1 | 1 | 100,00% | ∞ | 2,79R | €27,87 |
| SHADOW_RELATIVE_STRENGTH | 4 | 12 | 12 | 16,67% | 0,42 | -0,50R | €-60,29 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 6 | 4 | 4 | 50,00% | 1,95 | 0,48R | €19,32 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,35 | 0,22R | €15,08 |
| SHADOW_1H_BALANCED | RANGE | 3 | 7 | 7 | 42,86% | 1,41 | 0,24R | €16,83 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 3 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,38 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,12 |
| SHADOW_1H_FAST | RANGE | 2 | 11 | 11 | 45,45% | 1,19 | 0,11R | €11,65 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 1 | 9 | 9 | 0,00% | 0,00 | -1,09R | €-98,53 |
| SHADOW_4H_WIDE | RANGE | 9 | 1 | 1 | 100,00% | ∞ | 2,79R | €27,87 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,82 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 4 | 5 | 5 | 20,00% | 0,53 | -0,38R | €-19,14 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
