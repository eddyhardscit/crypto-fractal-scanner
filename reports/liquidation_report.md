# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-26 01:50:38 CEST**  
UTC: **2026-09-25 23:50:38 UTC**

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
| BTC | 84.065 $ | -0.44% | +0.0016% | $2.38B | -4.91% | 1.11 |
| SOL | 122,13 $ | +4.24% | +0.0039% | $379.85M | -12.84% | 1.47 |
| DOGE | 0.09899 $ | +3.32% | +0.0100% | $99.11M | -7.66% | 3.75 |

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
| Prezzo | $84,034 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.44% | movimento dell'ultimo giorno |
| Funding | +0.0016% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-26 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.38B | leva aperta stimata in dollari |
| Open Interest 24h | -4.91% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.11 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $67,227 | $100,840 |
| 10x | $75,630 | $92,437 |
| 20x | $79,832 | $88,235 |
| 50x | $82,353 | $85,714 |

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
| Prezzo | $122.01 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +4.24% | movimento dell'ultimo giorno |
| Funding | +0.0039% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-26 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $379.85M | leva aperta stimata in dollari |
| Open Interest 24h | -12.84% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.47 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $97.61 | $146.41 |
| 10x | $109.81 | $134.21 |
| 20x | $115.91 | $128.11 |
| 50x | $119.57 | $124.45 |

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
| Prezzo | $0.09901 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +3.32% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-26 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $99.11M | leva aperta stimata in dollari |
| Open Interest 24h | -7.66% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.75 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07921 | $0.11881 |
| 10x | $0.08911 | $0.10891 |
| 20x | $0.09406 | $0.10396 |
| 50x | $0.09703 | $0.10099 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
