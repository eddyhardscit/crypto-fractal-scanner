# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-25 07:33:39 CET**  
UTC: **2026-10-25 06:33:39 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.521 $ | -0.18% | +0.0086% | $2.40B | -4.35% | 1.25 |
| SOL | 101,76 $ | -0.24% | -0.0049% | $307.54M | +9.79% | 1.61 |
| DOGE | 0.07697 $ | -1.62% | -0.0064% | $93.31M | -0.02% | 3.32 |

## Spiegazione rapida dei termini

- **Funding positivo**: i long pagano gli short. Se è troppo positivo, tanti stanno scommettendo al rialzo.
- **Funding negativo**: gli short pagano i long. Se è troppo negativo, tanti stanno scommettendo al ribasso.
- **Open Interest / OI**: quanta leva è aperta sul mercato. Se sale, entra più leva. Se scende, la leva sta uscendo.
- **Long/Short sopra 1**: più mercato orientato long.
- **Long/Short sotto 1**: più mercato orientato short.
- **Flush sotto**: discesa rapida per pulire i long.
- **Short squeeze sopra**: salita rapida per liquidare gli short.

---

## Bitcoin — BTC

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $80,596 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.18% | movimento dell'ultimo giorno |
| Funding | +0.0086% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-25 09:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.40B | leva aperta stimata in dollari |
| Open Interest 24h | -4.35% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.25 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64,477 | $96,715 |
| 10x | $72,537 | $88,656 |
| 20x | $76,566 | $84,626 |
| 50x | $78,984 | $82,208 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

SOL: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding negativo: gli short pagano i long
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $101.89 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.24% | movimento dell'ultimo giorno |
| Funding | -0.0049% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-25 09:00 | prossimo aggiornamento funding |
| Open Interest stimato | $307.54M | leva aperta stimata in dollari |
| Open Interest 24h | +9.79% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.61 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $81.51 | $122.27 |
| 10x | $91.70 | $112.08 |
| 20x | $96.80 | $106.98 |
| 50x | $99.85 | $103.93 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo giù + leva su + funding negativo: rischio short squeeze sopra
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding negativo: gli short pagano i long
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07704 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.62% | movimento dell'ultimo giorno |
| Funding | -0.0064% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-25 09:00 | prossimo aggiornamento funding |
| Open Interest stimato | $93.31M | leva aperta stimata in dollari |
| Open Interest 24h | -0.02% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.32 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06163 | $0.09245 |
| 10x | $0.06934 | $0.08474 |
| 20x | $0.07319 | $0.08089 |
| 50x | $0.07550 | $0.07858 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
