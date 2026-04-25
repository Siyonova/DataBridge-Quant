import streamlit as st


def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(0, 212, 255, 0.18), transparent 35%),
            radial-gradient(circle at top right, rgba(132, 92, 255, 0.16), transparent 35%),
            #080B12;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    .hero {
        padding: 32px 36px;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(0,212,255,0.18), rgba(132,92,255,0.12));
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 20px 60px rgba(0,0,0,0.35);
        animation: fadeUp 0.8s ease-in-out;
    }

    .hero h1 {
        font-size: 54px;
        font-weight: 800;
        margin-bottom: 4px;
        background: linear-gradient(90deg, #FFFFFF, #00D4FF, #A78BFA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        color: #A1A1AA;
        font-size: 17px;
    }

    .glass-card {
        padding: 24px;
        border-radius: 22px;
        background: rgba(255,255,255,0.055);
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
        transition: all 0.3s ease;
        animation: fadeUp 0.9s ease-in-out;
    }

    .glass-card:hover {
        transform: translateY(-6px);
        border: 1px solid rgba(0,212,255,0.45);
        box-shadow: 0 20px 45px rgba(0,212,255,0.10);
    }

    .metric-label {
        color: #A1A1AA;
        font-size: 14px;
        font-weight: 600;
    }

    .metric-value {
        color: white;
        font-size: 34px;
        font-weight: 800;
        margin-top: 8px;
    }

    .metric-sub {
        color: #22C55E;
        font-size: 13px;
        margin-top: 5px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 800;
        margin-top: 34px;
        margin-bottom: 18px;
        color: white;
    }

    .badge {
        display: inline-block;
        padding: 7px 13px;
        margin-right: 8px;
        border-radius: 999px;
        background: rgba(0,212,255,0.12);
        color: #67E8F9;
        border: 1px solid rgba(103,232,249,0.25);
        font-size: 13px;
        font-weight: 600;
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(18px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_hero():
    st.markdown("""
    <div class="hero">
        <h1>📊 DataBridge Quant</h1>
        <p>Real-time Crypto Risk Analytics • Pairs Trading • Backtesting • Market Intelligence</p>
        <span class="badge">Python</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Plotly</span>
        <span class="badge">Risk Analytics</span>
    </div>
    """, unsafe_allow_html=True)


def render_section_title(title: str):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def render_metric_card(label: str, value: str, subtext: str):
    st.markdown(f"""
    <div class="glass-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-sub">{subtext}</div>
    </div>
    """, unsafe_allow_html=True)