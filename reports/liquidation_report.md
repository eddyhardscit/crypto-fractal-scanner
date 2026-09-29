# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-29 07:32:43 CEST**  
UTC: **2026-09-29 05:32:43 UTC**

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
| BTC | 83.243 $ | +0.27% | +0.0043% | $2.37B | -7.69% | 1.18 |
| SOL | 117,81 $ | -0.78% | +0.0036% | $351.83M | -4.28% | 1.67 |
| DOGE | 0.09344 $ | +0.30% | +0.0100% | $97.56M | -8.22% | 3.94 |

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
| Prezzo | $83,182 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.27% | movimento dell'ultimo giorno |
| Funding | +0.0043% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-29 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.37B | leva aperta stimata in dollari |
| Open Interest 24h | -7.69% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.18 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $66,545 | $99,818 |
| 10x | $74,864 | $91,500 |
| 20x | $79,023 | $87,341 |
| 50x | $81,518 | $84,845 |

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

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $117.69 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.78% | movimento dell'ultimo giorno |
| Funding | +0.0036% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-29 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $351.83M | leva aperta stimata in dollari |
| Open Interest 24h | -4.28% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.67 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $94.15 | $141.23 |
| 10x | $105.92 | $129.46 |
| 20x | $111.81 | $123.57 |
| 50x | $115.34 | $120.04 |

### Note tecniche usate dallo score

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
| Prezzo | $0.09326 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.30% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-29 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $97.56M | leva aperta stimata in dollari |
| Open Interest 24h | -8.22% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.94 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07461 | $0.11191 |
| 10x | $0.08393 | $0.10259 |
| 20x | $0.08860 | $0.09792 |
| 50x | $0.09139 | $0.09513 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
