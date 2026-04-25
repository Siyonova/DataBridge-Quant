import pandas as pd


def calculate_returns(series: pd.Series) -> pd.Series:
    return series.pct_change().dropna()


def calculate_spread(asset_1: pd.Series, asset_2: pd.Series) -> pd.Series:
    return asset_1 / asset_2


def calculate_zscore(series: pd.Series) -> pd.Series:
    return (series - series.mean()) / series.std()


def calculate_correlation(asset_1: pd.Series, asset_2: pd.Series) -> float:
    return asset_1.corr(asset_2)


def get_pair_signal(zscore_value: float) -> str:
    if zscore_value > 1:
        return "Long ETH / Short BTC"
    elif zscore_value < -1:
        return "Long BTC / Short ETH"
    return "Neutral"