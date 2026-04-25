import pandas as pd
import numpy as np


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


def annualized_volatility(returns: pd.Series) -> float:
    """Calculate annualized volatility from returns."""
    return returns.std() * np.sqrt(365)


def value_at_risk(returns: pd.Series, confidence: float = 0.95) -> float:
    """Calculate Value at Risk (VaR) at given confidence level."""
    return np.percentile(returns, (1 - confidence) * 100)


def calculate_drawdown(returns: pd.Series) -> pd.Series:
    """Calculate drawdown series from returns."""
    cumulative = (1 + returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    return drawdown


def max_drawdown(returns: pd.Series) -> float:
    """Calculate maximum drawdown from returns."""
    return calculate_drawdown(returns).min()


def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """Calculate Sharpe ratio from returns."""
    excess_returns = returns - risk_free_rate / 365
    return excess_returns.mean() / returns.std() * np.sqrt(365) if returns.std() > 0 else 0