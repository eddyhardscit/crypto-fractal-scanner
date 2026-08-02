# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-02 07:15:07 CEST**  
UTC: **2026-08-02 05:15:07 UTC**

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
| BTC | 63.406 $ | +0.59% | +0.0037% | $1.98B | +0.62% | 1.65 |
| SOL | 73,42 $ | +0.48% | -0.0008% | $211.64M | +25.85% | 1.50 |
| DOGE | 0.07014 $ | +0.23% | +0.0006% | $89.46M | -18.96% | 3.44 |

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
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $63,452 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.59% | movimento dell'ultimo giorno |
| Funding | +0.0037% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-02 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.98B | leva aperta stimata in dollari |
| Open Interest 24h | +0.62% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.65 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,761 | $76,142 |
| 10x | $57,106 | $69,797 |
| 20x | $60,279 | $66,624 |
| 50x | $62,183 | $64,721 |

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
| Prezzo | $73.48 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.48% | movimento dell'ultimo giorno |
| Funding | -0.0008% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-02 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $211.64M | leva aperta stimata in dollari |
| Open Interest 24h | +25.85% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.50 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $58.78 | $88.18 |
| 10x | $66.13 | $80.83 |
| 20x | $69.81 | $77.15 |
| 50x | $72.01 | $74.95 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
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
| Prezzo | $0.07024 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.23% | movimento dell'ultimo giorno |
| Funding | +0.0006% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-02 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $89.46M | leva aperta stimata in dollari |
| Open Interest 24h | -18.96% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.44 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05619 | $0.08429 |
| 10x | $0.06322 | $0.07726 |
| 20x | $0.06673 | $0.07375 |
| 50x | $0.06884 | $0.07164 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
