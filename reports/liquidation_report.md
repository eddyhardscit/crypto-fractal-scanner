# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-08 07:33:25 CEST**  
UTC: **2026-10-08 05:33:25 UTC**

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
| BTC | 82.851 $ | -1.56% | +0.0061% | $2.58B | -14.04% | 1.22 |
| SOL | 115,51 $ | -2.62% | -0.0010% | $368.96M | -16.18% | 1.94 |
| DOGE | 0.08774 $ | -2.82% | +0.0100% | $99.80M | -4.17% | 3.26 |

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
| Prezzo | $82,900 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.56% | movimento dell'ultimo giorno |
| Funding | +0.0061% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-08 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.58B | leva aperta stimata in dollari |
| Open Interest 24h | -14.04% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.22 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $66,320 | $99,480 |
| 10x | $74,610 | $91,190 |
| 20x | $78,755 | $87,045 |
| 50x | $81,242 | $84,558 |

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
| Prezzo | $115.52 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.62% | movimento dell'ultimo giorno |
| Funding | -0.0010% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-08 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $368.96M | leva aperta stimata in dollari |
| Open Interest 24h | -16.18% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.94 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $92.42 | $138.62 |
| 10x | $103.97 | $127.07 |
| 20x | $109.74 | $121.30 |
| 50x | $113.21 | $117.83 |

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
| Prezzo | $0.08769 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.82% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-08 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $99.80M | leva aperta stimata in dollari |
| Open Interest 24h | -4.17% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.26 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07015 | $0.10523 |
| 10x | $0.07892 | $0.09646 |
| 20x | $0.08331 | $0.09207 |
| 50x | $0.08594 | $0.08944 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
