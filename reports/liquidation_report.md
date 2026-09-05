# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-05 10:22:22 CEST**  
UTC: **2026-09-05 08:22:22 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.667 $ | -1.50% | -0.0019% | $2.18B | -9.60% | 1.17 |
| SOL | 102,31 $ | -1.48% | -0.0032% | $289.50M | -28.95% | 2.76 |
| DOGE | 0.08575 $ | -1.71% | +0.0100% | $88.74M | -10.69% | 5.08 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $79,622 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.50% | movimento dell'ultimo giorno |
| Funding | -0.0019% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.18B | leva aperta stimata in dollari |
| Open Interest 24h | -9.60% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.17 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63,698 | $95,547 |
| 10x | $71,660 | $87,584 |
| 20x | $75,641 | $83,603 |
| 50x | $78,030 | $81,215 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita

---

## Solana — SOL

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $102.23 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.48% | movimento dell'ultimo giorno |
| Funding | -0.0032% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $289.50M | leva aperta stimata in dollari |
| Open Interest 24h | -28.95% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.76 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $81.78 | $122.68 |
| 10x | $92.01 | $112.45 |
| 20x | $97.12 | $107.34 |
| 50x | $100.19 | $104.27 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.08558 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.71% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $88.74M | leva aperta stimata in dollari |
| Open Interest 24h | -10.69% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.08 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06846 | $0.10270 |
| 10x | $0.07702 | $0.09414 |
| 20x | $0.08130 | $0.08986 |
| 50x | $0.08387 | $0.08729 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
