import streamlit as st
from modules.alerts import zscore_alert, volatility_alert, drawdown_alert
from modules.data_loader import generate_sample_data, load_uploaded_csv, load_live_crypto_data
from modules.analytics import (
    calculate_returns,
    calculate_spread,
    calculate_zscore,
    calculate_correlation,
    get_pair_signal
)
from modules.risk import (
    annualized_volatility,
    value_at_risk,
    calculate_drawdown,
    max_drawdown,
    sharpe_ratio
)
from modules.backtesting import generate_mean_reversion_signal, run_backtest
from modules.visualization import (
    price_chart,
    zscore_chart,
    drawdown_chart,
    equity_curve_chart
)
from modules.ui import inject_custom_css, render_hero, render_section_title, render_metric_card


st.set_page_config(
    page_title="DataBridge Quant",
    page_icon="",
    layout="wide"
)

inject_custom_css()


@st.cache_data(ttl=300)
def get_data(use_live_data: bool):
    if use_live_data:
        try:
            return load_live_crypto_data()
        except Exception:
            return generate_sample_data()
    return generate_sample_data()


st.sidebar.markdown("## DataBridge Quant")
st.sidebar.caption("Professional crypto analytics suite")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Pair Analysis", "Risk Dashboard", "Backtest", "Alerts", "Data Upload", "About"]
)
use_live_data = st.sidebar.toggle("Use Live Binance Data", value=False)
st.sidebar.markdown("---")
st.sidebar.markdown("### System Status")
if use_live_data:
    st.sidebar.success("Live Binance data enabled")
else:
    st.sidebar.info("Demo data mode")
st.sidebar.info("Version 1.0.0")

df = get_data(use_live_data)

render_hero()

if page == "Overview":
    render_section_title("Market Overview")

    btc_returns = calculate_returns(df["BTC"])
    eth_returns = calculate_returns(df["ETH"])

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_metric_card("BTC Price", f"${df['BTC'].iloc[-1]:,.2f}", "Demo market feed")

    with c2:
        render_metric_card("ETH Price", f"${df['ETH'].iloc[-1]:,.2f}", "Demo market feed")

    with c3:
        render_metric_card("BTC Volatility", f"{annualized_volatility(btc_returns):.2%}", "Annualized")

    with c4:
        render_metric_card("ETH Volatility", f"{annualized_volatility(eth_returns):.2%}", "Annualized")

    render_section_title("BTC vs ETH Price Movement")
    st.plotly_chart(price_chart(df), use_container_width=True)

elif page == "Pair Analysis":
    render_section_title("Pairs Trading Signal")

    spread = calculate_spread(df["BTC"], df["ETH"])
    zscore = calculate_zscore(spread)
    latest_z = zscore.iloc[-1]

    c1, c2, c3 = st.columns(3)
    c1.metric("Latest Z-Score", f"{latest_z:.2f}")
    c2.metric("Trading Signal", get_pair_signal(latest_z))
    c3.metric("BTC-ETH Correlation", f"{calculate_correlation(df['BTC'], df['ETH']):.2f}")

    st.plotly_chart(zscore_chart(df["date"], zscore), use_container_width=True)

elif page == "Risk Dashboard":
    render_section_title("Risk Dashboard")

    returns = calculate_returns(df["BTC"])
    drawdown = calculate_drawdown(returns)

    c1, c2, c3 = st.columns(3)
    c1.metric("95% Daily VaR", f"{value_at_risk(returns):.2%}")
    c2.metric("Max Drawdown", f"{max_drawdown(returns):.2%}")
    c3.metric("Sharpe Ratio", f"{sharpe_ratio(returns):.2f}")

    st.plotly_chart(drawdown_chart(df["date"].iloc[1:], drawdown), use_container_width=True)

elif page == "Backtest":
    render_section_title("Mean-Reversion Backtest")

    spread = calculate_spread(df["BTC"], df["ETH"])
    zscore = calculate_zscore(spread)

    signal = generate_mean_reversion_signal(zscore)
    result = run_backtest(df["BTC"], signal)

    c1, c2 = st.columns(2)
    c1.metric("Final Strategy Return", f"{result['final_return']:.2%}")
    c2.metric("Total Signal Changes", result["total_signal_changes"])

    st.plotly_chart(equity_curve_chart(result["equity_curve"]), use_container_width=True)
elif page == "Alerts":
    render_section_title("Trading & Risk Alerts")

    spread = calculate_spread(df["BTC"], df["ETH"])
    zscore = calculate_zscore(spread)
    latest_z = zscore.iloc[-1]

    btc_returns = calculate_returns(df["BTC"])
    btc_vol = annualized_volatility(btc_returns)
    btc_mdd = max_drawdown(btc_returns)

    z_alert = zscore_alert(latest_z)
    v_alert = volatility_alert(btc_vol)
    d_alert = drawdown_alert(btc_mdd)

    st.markdown("### Signal Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Latest Z-Score", f"{latest_z:.2f}")
    c2.metric("BTC Volatility", f"{btc_vol:.2%}")
    c3.metric("Max Drawdown", f"{btc_mdd:.2%}")

    st.markdown("### Alert Feed")

    alerts = [
        ("Pair Trading Alert", z_alert),
        ("Volatility Alert", v_alert),
        ("Drawdown Alert", d_alert)
    ]

    for title, alert in alerts:
        if alert["type"] == "success":
            st.success(f"**{title} — {alert['level']}**  \n{alert['message']}")
        elif alert["type"] == "warning":
            st.warning(f"**{title} — {alert['level']}**  \n{alert['message']}")
        else:
            st.error(f"**{title} — {alert['level']}**  \n{alert['message']}")

    st.markdown("### Signal Explanation")

    st.markdown(f"""
    <div class="glass-card">
    <h3>How the signal is interpreted</h3>

    <p>
    The dashboard calculates the BTC/ETH spread and converts it into a z-score.
    A z-score measures how far the current spread is from its historical average.
    </p>

    <ul>
        <li><b>Z-score above +1:</b> BTC may be relatively expensive compared to ETH.</li>
        <li><b>Z-score below -1:</b> BTC may be relatively cheap compared to ETH.</li>
        <li><b>Z-score near 0:</b> Pair relationship is close to normal range.</li>
    </ul>

    <p>
    Current signal: <b>{get_pair_signal(latest_z)}</b>
    </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Data Upload":
    render_section_title("Upload Custom Crypto Dataset")

    st.markdown("""
    Your CSV must contain these columns:

    ```txt
    date,BTC,ETH
    ```
    """)

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            uploaded_df = load_uploaded_csv(uploaded_file)
            st.success("CSV uploaded successfully.")
            st.dataframe(uploaded_df.head(), use_container_width=True)
            st.plotly_chart(price_chart(uploaded_df), use_container_width=True)
        except Exception as e:
            st.error(f"Upload failed: {e}")

else:
    render_section_title("About DataBridge Quant")

    st.markdown("""
    <div class="glass-card">
    <h3>Professional Crypto Risk Analytics Platform</h3>
    <p>
    DataBridge Quant is a production-style analytics dashboard built for quantitative finance,
    crypto market monitoring, pairs trading, and financial risk analysis.
    </p>

    <p><b>Core Features:</b></p>
    <ul>
        <li>Interactive market dashboard</li>
        <li>BTC/ETH pair trading signals</li>
        <li>Z-score based mean-reversion analysis</li>
        <li>Volatility, VaR, Sharpe ratio, and drawdown metrics</li>
        <li>Backtesting engine with equity curve visualization</li>
        <li>CSV upload support for custom datasets</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)