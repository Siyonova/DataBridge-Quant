import numpy as np
import pandas as pd


def generate_mean_reversion_signal(zscore: pd.Series, threshold: float = 1.0) -> np.ndarray:
    return np.where(zscore > threshold, -1, np.where(zscore < -threshold, 1, 0))


def run_backtest(price_series: pd.Series, signal: np.ndarray) -> dict:
    returns = price_series.pct_change().fillna(0)

    strategy_returns = signal[:-1] * returns.iloc[1:].values
    equity_curve = (1 + pd.Series(strategy_returns)).cumprod()

    final_return = equity_curve.iloc[-1] - 1
    total_signal_changes = int(np.sum(np.abs(np.diff(signal)) > 0))

    return {
        "strategy_returns": pd.Series(strategy_returns),
        "equity_curve": equity_curve,
        "final_return": final_return,
        "total_signal_changes": total_signal_changes
    }