
#  DataBridge Quant

<div align="center">

### Real-Time Crypto Risk Analytics • Pairs Trading • Backtesting • Market Intelligence

Built with **Python, Streamlit, Plotly, Pandas, NumPy, Statsmodels, Binance API**

[Live Demo](https://your-streamlit-link.streamlit.app) • [💻 GitHub Repo](https://github.com/Siyonova/DataBridge-Quant)

</div>

---

##  Overview

**DataBridge Quant** is a production-style quantitative analytics dashboard designed for cryptocurrency market monitoring, statistical arbitrage research, and portfolio risk analysis.

The platform provides real-time market intelligence, pair-trading opportunities, strategy backtesting, and advanced risk metrics through an elegant interactive dashboard.

It was built to simulate how modern hedge funds, fintech teams, and trading desks monitor markets and evaluate systematic strategies.

---

##  Key Features

###  Live Market Dashboard
- BTC / ETH live or demo market feed
- Historical trend visualization
- Real-time pricing overview

###  Pair Trading Analytics
- BTC/ETH spread monitoring
- Z-score mean reversion signals
- Correlation analysis
- Trading opportunity detection

###  Risk Dashboard
- Annualized volatility
- 95% Daily Value at Risk (VaR)
- Maximum Drawdown
- Sharpe Ratio

###  Strategy Backtesting
- Mean reversion strategy engine
- Equity curve visualization
- Final return tracking
- Signal change count

###  Alerts Engine
- Volatility alerts
- Drawdown warnings
- Pair trading signal notifications
- Risk threshold monitoring

###  Custom Data Upload
- Upload your own CSV datasets
- Analyze custom BTC/ETH data instantly

---

##  Product Screens

### Dashboard Home

_Add screenshot here_

```txt
assets/dashboard-home.png
````

### Risk Dashboard

*Add screenshot here*

```txt
assets/risk-dashboard.png
```

### Pair Trading Signals

*Add screenshot here*

```txt
assets/pair-analysis.png
```

---

## 🛠️ Tech Stack

| Category        | Tools                     |
| --------------- | ------------------------- |
| Frontend        | Streamlit                 |
| Visualization   | Plotly                    |
| Backend Logic   | Python                    |
| Data Processing | Pandas, NumPy             |
| Quant Models    | Statsmodels, SciPy        |
| Market Data     | Binance Public API        |
| Deployment      | Streamlit Community Cloud |

---

##  Quant Models Used

### Z-Score Mean Reversion

Measures how far current spread deviates from historical mean.

```math
Z = \frac{X - \mu}{\sigma}
```

Used for pair trading signal generation.

---

### Sharpe Ratio

Measures risk-adjusted return.

```math
Sharpe = \frac{R_p - R_f}{\sigma_p}
```

---

### Maximum Drawdown

Largest decline from equity peak.

---

### Value at Risk (VaR)

Estimated worst expected loss over a confidence level.

---

##  Project Structure

```txt
DataBridge-Quant/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── data/
│   └── sample_crypto_data.csv
│── modules/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── analytics.py
│   ├── risk.py
│   ├── backtesting.py
│   ├── alerts.py
│   ├── visualization.py
│   └── ui.py
│── .streamlit/
│   └── config.toml
```

---

##  Run Locally

### 1 Clone Repo

```bash
git clone https://github.com/YOUR_USERNAME/DataBridge-Quant.git
cd DataBridge-Quant
```

### 2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 3 Start App

```bash
streamlit run app.py
```

---

##  Deployment

Hosted free on Streamlit Community Cloud.

```txt
https://your-streamlit-link.streamlit.app
```

---

##  Example Use Cases

### Recruiters / Hiring Managers

View production-ready Python dashboard skills.

### Quant / Finance Roles

Showcase understanding of:

* Volatility
* Risk
* Drawdowns
* Strategy testing
* Statistical arbitrage

### Data Analyst Roles

Demonstrates:

* Dashboarding
* Data storytelling
* KPI design
* Real-time data systems

---

##  Why This Project Matters

Most student dashboards stop at charts.

**DataBridge Quant** goes further:

✅ Live API integration
✅ Finance domain knowledge
✅ Real quant metrics
✅ Strategy simulation
✅ Clean architecture
✅ Production deployment
✅ Strong UI/UX execution

---

##  Future Enhancements

* Multi-asset portfolio optimizer
* LSTM price forecasting
* Options Greeks dashboard
* Real-time Telegram alerts
* TradingView integration
* AI-generated market commentary
* Multi-exchange data engine

---

##  Author

**Siyona B**
AI / Data / Quant Analytics Engineer

[LinkedIn](https://www.linkedin.com/in/siyona-bonam/) • [GitHub](https://github.com/Siyonova)

---

##  If You Like This Project

Please star the repository and share feedback.

---
