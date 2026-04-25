def zscore_alert(zscore_value: float, threshold: float = 1.0) -> dict:
    if zscore_value > threshold:
        return {
            "level": "High",
            "message": "Z-score is above threshold. Possible short BTC / long ETH mean-reversion setup.",
            "type": "warning"
        }

    if zscore_value < -threshold:
        return {
            "level": "High",
            "message": "Z-score is below threshold. Possible long BTC / short ETH mean-reversion setup.",
            "type": "warning"
        }

    return {
        "level": "Normal",
        "message": "Z-score is within neutral range. No strong mean-reversion signal.",
        "type": "success"
    }


def volatility_alert(volatility: float, threshold: float = 0.40) -> dict:
    if volatility > threshold:
        return {
            "level": "Elevated",
            "message": "Annualized volatility is high. Risk exposure should be monitored.",
            "type": "warning"
        }

    return {
        "level": "Stable",
        "message": "Volatility is within acceptable range.",
        "type": "success"
    }


def drawdown_alert(max_drawdown_value: float, threshold: float = -0.15) -> dict:
    if max_drawdown_value < threshold:
        return {
            "level": "Critical",
            "message": "Drawdown exceeded risk threshold. Strategy may need review.",
            "type": "error"
        }

    return {
        "level": "Controlled",
        "message": "Drawdown is within controlled risk range.",
        "type": "success"
    }