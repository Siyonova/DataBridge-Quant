import plotly.graph_objects as go
import pandas as pd


def price_chart(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["BTC"],
        name="BTC",
        mode="lines",
        line=dict(width=3)
    ))

    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["ETH"],
        name="ETH",
        mode="lines",
        line=dict(width=3)
    ))

    fig.update_layout(
        template="plotly_dark",
        height=520,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.02)",
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", y=1.1, x=0.75)
    )

    return fig


def zscore_chart(dates: pd.Series, zscore: pd.Series) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates,
        y=zscore,
        name="Z-Score",
        line=dict(width=3)
    ))

    fig.add_hline(y=1, line_dash="dash", annotation_text="Short BTC / Long ETH")
    fig.add_hline(y=-1, line_dash="dash", annotation_text="Long BTC / Short ETH")
    fig.add_hline(y=0, line_dash="dot")

    fig.update_layout(
        title="Z-Score Mean Reversion Signal",
        template="plotly_dark",
        height=520,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.02)"
    )

    return fig


def drawdown_chart(dates: pd.Series, drawdown: pd.Series) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates,
        y=drawdown,
        name="Drawdown",
        line=dict(width=3)
    ))

    fig.update_layout(
        title="BTC Drawdown Curve",
        template="plotly_dark",
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.02)"
    )

    return fig


def equity_curve_chart(equity_curve: pd.Series) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=equity_curve,
        name="Strategy Equity Curve",
        line=dict(width=3)
    ))

    fig.update_layout(
        title="Strategy Equity Curve",
        template="plotly_dark",
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.02)"
    )

    return fig