# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-21 07:33:43 CEST**  
UTC: **2026-10-21 05:33:43 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.812 $ | +1.12% | +0.0040% | $2.46B | -3.15% | 1.04 |
| SOL | 105,97 $ | +1.20% | +0.0061% | $304.32M | +8.02% | 1.74 |
| DOGE | 0.08169 $ | +2.88% | +0.0100% | $102.76M | -10.88% | 3.42 |

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
| Prezzo | $82,853 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.12% | movimento dell'ultimo giorno |
| Funding | +0.0040% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-21 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.46B | leva aperta stimata in dollari |
| Open Interest 24h | -3.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.04 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $66,283 | $99,424 |
| 10x | $74,568 | $91,139 |
| 20x | $78,711 | $86,996 |
| 50x | $81,196 | $84,510 |

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 5/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $106.00 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.20% | movimento dell'ultimo giorno |
| Funding | +0.0061% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-21 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $304.32M | leva aperta stimata in dollari |
| Open Interest 24h | +8.02% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.74 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $84.80 | $127.20 |
| 10x | $95.40 | $116.60 |
| 20x | $100.70 | $111.30 |
| 50x | $103.88 | $108.12 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
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
| Prezzo | $0.08172 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.88% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-21 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $102.76M | leva aperta stimata in dollari |
| Open Interest 24h | -10.88% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.42 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06538 | $0.09806 |
| 10x | $0.07355 | $0.08989 |
| 20x | $0.07763 | $0.08581 |
| 50x | $0.08009 | $0.08335 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
