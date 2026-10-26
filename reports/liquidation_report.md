# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-26 07:33:42 CET**  
UTC: **2026-10-26 06:33:42 UTC**

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
| BTC | 79.856 $ | -0.71% | +0.0086% | $2.49B | -8.42% | 1.29 |
| SOL | 100,60 $ | -1.01% | +0.0100% | $312.16M | +14.36% | 1.45 |
| DOGE | 0.07658 $ | -0.32% | -0.0014% | $95.16M | +1.51% | 2.95 |

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
| Prezzo | $80,014 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.71% | movimento dell'ultimo giorno |
| Funding | +0.0086% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-26 09:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.49B | leva aperta stimata in dollari |
| Open Interest 24h | -8.42% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.29 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64,011 | $96,017 |
| 10x | $72,013 | $88,016 |
| 20x | $76,014 | $84,015 |
| 50x | $78,414 | $81,615 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

SOL: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $100.81 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.01% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-26 09:00 | prossimo aggiornamento funding |
| Open Interest stimato | $312.16M | leva aperta stimata in dollari |
| Open Interest 24h | +14.36% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.45 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $80.65 | $120.97 |
| 10x | $90.73 | $110.89 |
| 20x | $95.77 | $105.85 |
| 50x | $98.79 | $102.83 |

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

- funding negativo: gli short pagano i long
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07678 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.32% | movimento dell'ultimo giorno |
| Funding | -0.0014% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-26 09:00 | prossimo aggiornamento funding |
| Open Interest stimato | $95.16M | leva aperta stimata in dollari |
| Open Interest 24h | +1.51% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.95 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06142 | $0.09214 |
| 10x | $0.06910 | $0.08446 |
| 20x | $0.07294 | $0.08062 |
| 50x | $0.07524 | $0.07832 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
