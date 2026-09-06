# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-06 07:32:55 CEST**  
UTC: **2026-09-06 05:32:55 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.859 $ | +0.36% | +0.0048% | $2.18B | -8.44% | 1.31 |
| SOL | 106,09 $ | +4.05% | +0.0100% | $320.50M | -32.97% | 2.91 |
| DOGE | 0.09084 $ | +7.33% | +0.0036% | $102.77M | -16.26% | 5.43 |

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
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $79,843 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.36% | movimento dell'ultimo giorno |
| Funding | +0.0048% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.18B | leva aperta stimata in dollari |
| Open Interest 24h | -8.44% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.31 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63,874 | $95,811 |
| 10x | $71,858 | $87,827 |
| 20x | $75,850 | $83,835 |
| 50x | $78,246 | $81,439 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $105.88 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +4.05% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $320.50M | leva aperta stimata in dollari |
| Open Interest 24h | -32.97% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.91 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $84.70 | $127.06 |
| 10x | $95.29 | $116.47 |
| 20x | $100.59 | $111.17 |
| 50x | $103.76 | $108.00 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.09083 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +7.33% | movimento dell'ultimo giorno |
| Funding | +0.0036% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $102.77M | leva aperta stimata in dollari |
| Open Interest 24h | -16.26% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.43 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07266 | $0.10900 |
| 10x | $0.08175 | $0.09991 |
| 20x | $0.08629 | $0.09537 |
| 50x | $0.08901 | $0.09265 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
