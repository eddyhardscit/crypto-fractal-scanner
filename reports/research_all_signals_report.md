## 🔬 Research All Signals

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **RANGE**
- Famiglia: **RANGE**
- Confidenza: **80,40%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +1.0, breadth EMA50 17%, ADX 25.7.
- BTC trend score: **1,00**; ADX: **25,71**; breadth sopra EMA50: **16,67%**
- Mediana alt vs BTC: **-0,76%**; dispersione: **14,89%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **26**
- Trade research chiusi: **69**
- Eventi di mercato indipendenti chiusi: **35**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **121**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 4 | 6 | 6 | 33,33% | 0,98 | -0,02R | €-0,94 |
| SHADOW_1H_BALANCED | 6 | 22 | 22 | 27,27% | 0,69 | -0,24R | €-52,75 |
| SHADOW_1H_FAST | 4 | 24 | 24 | 25,00% | 0,46 | -0,43R | €-103,13 |
| SHADOW_4H_WIDE | 7 | 3 | 3 | 33,33% | 1,38 | 0,25R | €7,60 |
| SHADOW_EMA_TREND_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | 3 | 14 | 14 | 14,29% | 0,35 | -0,58R | €-80,57 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 4 | 6 | 6 | 33,33% | 0,98 | -0,02R | €-0,94 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,35 | 0,22R | €15,08 |
| SHADOW_1H_BALANCED | RANGE | 3 | 9 | 9 | 33,33% | 0,94 | -0,04R | €-3,45 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 3 | 6 | 6 | 0,00% | 0,00 | -1,07R | €-64,38 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,12 |
| SHADOW_1H_FAST | RANGE | 3 | 12 | 12 | 41,67% | 1,02 | 0,01R | €1,52 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 1 | 9 | 9 | 0,00% | 0,00 | -1,09R | €-98,53 |
| SHADOW_4H_WIDE | RANGE | 7 | 3 | 3 | 33,33% | 1,38 | 0,25R | €7,60 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,82 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 3 | 7 | 7 | 14,29% | 0,36 | -0,56R | €-39,42 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
