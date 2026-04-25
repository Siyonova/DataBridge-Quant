import pandas as pd
import numpy as np
import requests


def generate_sample_data(periods: int = 300) -> pd.DataFrame:
    np.random.seed(42)

    dates = pd.date_range(start="2024-01-01", periods=periods, freq="D")
    btc = 42000 + np.cumsum(np.random.normal(0, 600, periods))
    eth = 2200 + np.cumsum(np.random.normal(0, 45, periods))

    return pd.DataFrame({
        "date": dates,
        "BTC": btc,
        "ETH": eth
    })


def fetch_binance_klines(symbol: str, interval: str = "1d", limit: int = 300) -> pd.DataFrame:
    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
    ])

    df["date"] = pd.to_datetime(df["open_time"], unit="ms")
    df["close"] = df["close"].astype(float)

    return df[["date", "close"]]


def load_live_crypto_data(limit: int = 300) -> pd.DataFrame:
    btc_df = fetch_binance_klines("BTCUSDT", limit=limit)
    eth_df = fetch_binance_klines("ETHUSDT", limit=limit)

    df = pd.DataFrame({
        "date": btc_df["date"],
        "BTC": btc_df["close"],
        "ETH": eth_df["close"]
    })

    return df


def load_uploaded_csv(uploaded_file) -> pd.DataFrame:
    df = pd.read_csv(uploaded_file)

    required_columns = {"date", "BTC", "ETH"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["date"] = pd.to_datetime(df["date"])
    return df