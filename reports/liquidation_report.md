# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-27 07:32:39 CEST**  
UTC: **2026-09-27 05:32:39 UTC**

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
| BTC | 84.377 $ | +0.62% | +0.0003% | $2.38B | -6.99% | 1.00 |
| SOL | 120,68 $ | +0.28% | +0.0064% | $386.97M | -0.96% | 1.16 |
| DOGE | 0.09591 $ | -1.50% | +0.0100% | $101.24M | -8.49% | 3.59 |

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
| Prezzo | $84,380 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.62% | movimento dell'ultimo giorno |
| Funding | +0.0003% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-27 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.38B | leva aperta stimata in dollari |
| Open Interest 24h | -6.99% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.00 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $67,504 | $101,256 |
| 10x | $75,942 | $92,818 |
| 20x | $80,161 | $88,599 |
| 50x | $82,693 | $86,068 |

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
- open interest abbastanza stabile
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $120.63 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.28% | movimento dell'ultimo giorno |
| Funding | +0.0064% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-27 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $386.97M | leva aperta stimata in dollari |
| Open Interest 24h | -0.96% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.16 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $96.50 | $144.76 |
| 10x | $108.57 | $132.69 |
| 20x | $114.60 | $126.66 |
| 50x | $118.22 | $123.04 |

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
| Prezzo | $0.09588 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.50% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-27 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $101.24M | leva aperta stimata in dollari |
| Open Interest 24h | -8.49% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.59 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07670 | $0.11506 |
| 10x | $0.08629 | $0.10547 |
| 20x | $0.09109 | $0.10067 |
| 50x | $0.09396 | $0.09780 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
