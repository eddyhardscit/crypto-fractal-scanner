## 🔬 Research All Signals

Registro parallelo senza limite globale di quattro posizioni. Considera soltanto segnali validi con dati freschi; non modifica i conti paper e non genera ordini reali.

### Regime di mercato osservato

- Regime: **TRANSITION**
- Famiglia: **TRANSITION**
- Confidenza: **78,00%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Segnali contrastanti tra trend BTC, breadth e forza delle altcoin.
- BTC trend score: **3,00**; ADX: **28,64**; breadth sopra EMA50: **16,67%**
- Mediana alt vs BTC: **-0,48%**; dispersione: **8,25%**

- Aperti in questo ciclo: **18**
- Chiusi in questo ciclo: **24**
- Posizioni research aperte: **72**
- Trade research chiusi: **196**
- Eventi di mercato indipendenti chiusi: **91**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **453**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| RSI_EXTREME_SHORT_15M | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,96 |
| SHADOW_1H_BALANCED | 10 | 42 | 42 | 30,95% | 0,82 | -0,13R | €-56,32 |
| SHADOW_1H_FAST | 7 | 48 | 48 | 27,08% | 0,50 | -0,39R | €-187,47 |
| SHADOW_4H_WIDE | 7 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_BOLLINGER_MR_1H | 0 | 7 | 7 | 42,86% | 0,96 | -0,03R | €-1,87 |
| SHADOW_COMBO_ADAPTIVE | 3 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,42 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | 1 | 7 | 7 | 28,57% | 0,80 | -0,16R | €-11,00 |
| SHADOW_COMBO_TREND | 4 | 4 | 4 | 25,00% | 0,70 | -0,24R | €-9,59 |
| SHADOW_DONCHIAN_1H | 5 | 3 | 3 | 33,33% | 1,15 | 0,11R | €3,16 |
| SHADOW_EMA_TREND_1H | 8 | 8 | 8 | 25,00% | 0,69 | -0,25R | €-19,85 |
| SHADOW_GLOBAL_PURE | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_RELATIVE_STRENGTH | 8 | 28 | 28 | 21,43% | 0,57 | -0,36R | €-99,77 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 4 | 3 | 3 | 33,33% | 0,98 | -0,01R | €-0,40 |
| SHADOW_SCANNER_TOP5_BTC | 4 | 7 | 7 | 42,86% | 1,51 | 0,31R | €21,58 |
| SHADOW_SCANNER_TOP5_LONG | 5 | 10 | 10 | 40,00% | 1,22 | 0,14R | €13,81 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 0 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| MAIN | TREND_UP | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,86 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 2,27 | 0,60R | €54,20 |
| SHADOW_1H_BALANCED | RANGE | 1 | 15 | 15 | 40,00% | 1,23 | 0,15R | €21,89 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| SHADOW_1H_BALANCED | TRANSITION | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED | TREND_UP | 5 | 9 | 9 | 22,22% | 0,53 | -0,39R | €-35,16 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,38 | 0,20R | €12,11 |
| SHADOW_1H_FAST | RANGE | 1 | 19 | 19 | 42,11% | 1,01 | 0,00R | €0,76 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| SHADOW_1H_FAST | TRANSITION | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_FAST | TREND_UP | 2 | 13 | 13 | 15,38% | 0,25 | -0,70R | €-90,58 |
| SHADOW_4H_WIDE | RANGE | 2 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €2,97 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,85 | -0,10R | €-4,84 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,42 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 7 | 7 | 28,57% | 0,80 | -0,16R | €-11,00 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | TREND_UP | 3 | 4 | 4 | 25,00% | 0,70 | -0,24R | €-9,59 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_DONCHIAN_1H | TRANSITION | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,29 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_EMA_TREND_1H | TREND_UP | 6 | 7 | 7 | 28,57% | 0,82 | -0,14R | €-9,71 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 2 | 6 | 6 | 33,33% | 1,02 | 0,02R | €1,05 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 1 | 14 | 14 | 21,43% | 0,56 | -0,36R | €-49,93 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 5 | 6 | 6 | 16,67% | 0,42 | -0,51R | €-30,56 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 2,12R | €42,42 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 1 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,84 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 1,92R | €38,42 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 8 | 8 | 25,00% | 0,62 | -0,31R | €-24,61 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
