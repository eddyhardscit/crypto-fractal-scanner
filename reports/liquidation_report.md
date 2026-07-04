# Report liquidazioni / futures BTC / SOL / DOGE

Generato: **2026-07-04 10:30:10 CEST**  
UTC: **2026-07-04 08:30:10 UTC**

Questo report legge la pressione dei futures: funding, open interest, long/short ratio, taker buy/sell e, se configurata in futuro, heatmap CoinGlass.

## Lettura velocissima

| Asset | Prezzo | Prezzo 24h | Funding | OI 24h | Account long | Taker B/S | Lettura | Forza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | n/d | n/d | n/d | n/d | n/d | n/d | NEUTRALE / MISTO | 1/5 |
| SOL | n/d | n/d | n/d | n/d | n/d | n/d | NEUTRALE / MISTO | 1/5 |
| DOGE | n/d | n/d | n/d | n/d | n/d | n/d | NEUTRALE / MISTO | 1/5 |

## Come leggere questo report

- **Funding positivo**: i long pagano gli short. Se diventa troppo positivo, il mercato può essere troppo long.
- **Funding negativo**: gli short pagano i long. Se diventa troppo negativo, il mercato può essere troppo short.
- **Open Interest in aumento**: entra più leva nel sistema.
- **Open Interest in calo**: parte della leva è già uscita.
- **Account long troppo alti**: rischio pulizia sotto.
- **Account short troppo alti**: rischio short squeeze sopra.
- **Taker buy/sell ratio sopra 1**: compratori aggressivi più forti dei venditori.
- **Taker buy/sell ratio sotto 1**: venditori aggressivi più forti dei compratori.

Nota importante: i livelli teorici di liquidazione sotto sono una semplificazione matematica. Non sono la vera heatmap del mercato. La vera heatmap richiede CoinGlass o fonte equivalente.

---


## Bitcoin — BTC

### Sintesi

**Lettura:** NEUTRALE / MISTO  
**Forza:** 1/5  
**Significato:** I dati futures non danno una direzione netta.

### Metriche principali

| Metrica | Valore |
| --- | --- |
| Prezzo mark | n/d |
| Variazione prezzo 24h | n/d |
| Funding rate ultimo | n/d |
| Prossimo funding | n/d |
| Open Interest stimato | n/d |
| Open Interest 24h | n/d |
| Open Interest 7 giorni | n/d |
| Account long | n/d |
| Account short | n/d |
| Long/Short ratio globale | n/d |
| Top trader long | n/d |
| Top trader short | n/d |
| Top trader long/short ratio | n/d |
| Taker buy/sell ratio | n/d |

### Perché lo scanner futures legge così

- Nessun segnale futures netto.


### Livelli teorici semplificati di liquidazione

Questi livelli sono calcolati come se una posizione fosse stata aperta vicino al prezzo attuale. Sono **indicativi**, non precisi, perché ogni exchange usa margine di mantenimento, fee, modalità isolated/cross e regole diverse.

| Leva | Long circa liquidato sotto | Short circa liquidato sopra |
| --- | --- | --- |
| n/d | n/d | n/d |

### Heatmap CoinGlass

Heatmap vera CoinGlass: **non attiva**.

Motivo: manca il secret `COINGLASS_API_KEY`.

Per ora il report usa dati Binance pubblici e livelli teorici semplificati.


### Errori/parziali

- premiumIndex: HTTP Error 451: 
- ticker_24hr: HTTP Error 451: 
- openInterest: HTTP Error 451: 
- openInterestHist_1h: HTTP Error 451: 
- openInterestHist_1d: HTTP Error 451: 
- globalLongShortAccountRatio_1h: HTTP Error 451: 
- topLongShortPositionRatio_1h: HTTP Error 451: 
- takerlongshortRatio_1h: HTTP Error 451: 

---


## Solana — SOL

### Sintesi

**Lettura:** NEUTRALE / MISTO  
**Forza:** 1/5  
**Significato:** I dati futures non danno una direzione netta.

### Metriche principali

| Metrica | Valore |
| --- | --- |
| Prezzo mark | n/d |
| Variazione prezzo 24h | n/d |
| Funding rate ultimo | n/d |
| Prossimo funding | n/d |
| Open Interest stimato | n/d |
| Open Interest 24h | n/d |
| Open Interest 7 giorni | n/d |
| Account long | n/d |
| Account short | n/d |
| Long/Short ratio globale | n/d |
| Top trader long | n/d |
| Top trader short | n/d |
| Top trader long/short ratio | n/d |
| Taker buy/sell ratio | n/d |

### Perché lo scanner futures legge così

- Nessun segnale futures netto.


### Livelli teorici semplificati di liquidazione

Questi livelli sono calcolati come se una posizione fosse stata aperta vicino al prezzo attuale. Sono **indicativi**, non precisi, perché ogni exchange usa margine di mantenimento, fee, modalità isolated/cross e regole diverse.

| Leva | Long circa liquidato sotto | Short circa liquidato sopra |
| --- | --- | --- |
| n/d | n/d | n/d |

### Heatmap CoinGlass

Heatmap vera CoinGlass: **non attiva**.

Motivo: manca il secret `COINGLASS_API_KEY`.

Per ora il report usa dati Binance pubblici e livelli teorici semplificati.


### Errori/parziali

- premiumIndex: HTTP Error 451: 
- ticker_24hr: HTTP Error 451: 
- openInterest: HTTP Error 451: 
- openInterestHist_1h: HTTP Error 451: 
- openInterestHist_1d: HTTP Error 451: 
- globalLongShortAccountRatio_1h: HTTP Error 451: 
- topLongShortPositionRatio_1h: HTTP Error 451: 
- takerlongshortRatio_1h: HTTP Error 451: 

---


## Dogecoin — DOGE

### Sintesi

**Lettura:** NEUTRALE / MISTO  
**Forza:** 1/5  
**Significato:** I dati futures non danno una direzione netta.

### Metriche principali

| Metrica | Valore |
| --- | --- |
| Prezzo mark | n/d |
| Variazione prezzo 24h | n/d |
| Funding rate ultimo | n/d |
| Prossimo funding | n/d |
| Open Interest stimato | n/d |
| Open Interest 24h | n/d |
| Open Interest 7 giorni | n/d |
| Account long | n/d |
| Account short | n/d |
| Long/Short ratio globale | n/d |
| Top trader long | n/d |
| Top trader short | n/d |
| Top trader long/short ratio | n/d |
| Taker buy/sell ratio | n/d |

### Perché lo scanner futures legge così

- Nessun segnale futures netto.


### Livelli teorici semplificati di liquidazione

Questi livelli sono calcolati come se una posizione fosse stata aperta vicino al prezzo attuale. Sono **indicativi**, non precisi, perché ogni exchange usa margine di mantenimento, fee, modalità isolated/cross e regole diverse.

| Leva | Long circa liquidato sotto | Short circa liquidato sopra |
| --- | --- | --- |
| n/d | n/d | n/d |

### Heatmap CoinGlass

Heatmap vera CoinGlass: **non attiva**.

Motivo: manca il secret `COINGLASS_API_KEY`.

Per ora il report usa dati Binance pubblici e livelli teorici semplificati.


### Errori/parziali

- premiumIndex: HTTP Error 451: 
- ticker_24hr: HTTP Error 451: 
- openInterest: HTTP Error 451: 
- openInterestHist_1h: HTTP Error 451: 
- openInterestHist_1d: HTTP Error 451: 
- globalLongShortAccountRatio_1h: HTTP Error 451: 
- topLongShortPositionRatio_1h: HTTP Error 451: 
- takerlongshortRatio_1h: HTTP Error 451: 

---
