# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-12 07:32:39 CEST**  
UTC: **2026-09-12 05:32:39 UTC**

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
| BTC | 77.219 $ | +0.18% | +0.0074% | $2.11B | -3.23% | 1.78 |
| SOL | 101,55 $ | +1.92% | +0.0073% | $281.27M | -21.05% | 2.16 |
| DOGE | 0.08434 $ | +0.52% | +0.0100% | $86.37M | -4.79% | 5.42 |

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
| Prezzo | $77,185 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.18% | movimento dell'ultimo giorno |
| Funding | +0.0074% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-12 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.11B | leva aperta stimata in dollari |
| Open Interest 24h | -3.23% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.78 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61,748 | $92,622 |
| 10x | $69,467 | $84,904 |
| 20x | $73,326 | $81,045 |
| 50x | $75,642 | $78,729 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $101.49 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.92% | movimento dell'ultimo giorno |
| Funding | +0.0073% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-12 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $281.27M | leva aperta stimata in dollari |
| Open Interest 24h | -21.05% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.16 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $81.19 | $121.79 |
| 10x | $91.34 | $111.64 |
| 20x | $96.42 | $106.56 |
| 50x | $99.46 | $103.52 |

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
| Prezzo | $0.08429 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.52% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-12 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $86.37M | leva aperta stimata in dollari |
| Open Interest 24h | -4.79% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.42 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06743 | $0.10115 |
| 10x | $0.07586 | $0.09272 |
| 20x | $0.08008 | $0.08850 |
| 50x | $0.08260 | $0.08598 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
