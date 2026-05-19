import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Smart Ambulance AI System",
    page_icon="🚑",
    layout="wide"
)

# =====================================================
# PREMIUM UI DESIGN
# =====================================================
st.markdown("""
<style>

/* ================================
MAIN BACKGROUND
================================ */
.stApp {
    background:
    radial-gradient(circle at top left, #1e3a8a 0%, transparent 30%),
    radial-gradient(circle at bottom right, #0ea5e9 0%, transparent 30%),
    linear-gradient(135deg, #020617, #0f172a, #111827);
    
    background-attachment: fixed;
}

/* ================================
MAIN CONTAINER
================================ */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    backdrop-filter: blur(18px);

    box-shadow:
    0 8px 32px rgba(0,0,0,0.4);
}

/* ================================
TITLE
================================ */
h1 {
    text-align: center;
    font-size: 4.5rem !important;
    font-weight: 900 !important;

    background: linear-gradient(
        90deg,
        #38bdf8,
        #60a5fa,
        #ffffff
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 10px;

    letter-spacing: 1px;

    text-shadow:
    0 0 20px rgba(56,189,248,0.3);
}

/* ================================
HEADINGS
================================ */
h2, h3, h4, h5, h6 {
    color: #f8fafc !important;
    font-weight: 700 !important;
}

/* ================================
TEXT
================================ */
p, label, span {
    color: #e2e8f0 !important;
}

/* ================================
SIDEBAR
================================ */
section[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.85) !important;

    border-right:
    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(14px);
}

/* ================================
BUTTONS
================================ */
.stButton>button {

    width: 100%;

    background:
    linear-gradient(
        90deg,
        #0ea5e9,
        #2563eb
    );

    color: white;

    border: none;

    border-radius: 16px;

    padding: 14px 22px;

    font-size: 16px;

    font-weight: 700;

    transition: 0.3s ease;

    box-shadow:
    0 0 18px rgba(14,165,233,0.35);
}

.stButton>button:hover {

    transform:
    translateY(-3px)
    scale(1.02);

    box-shadow:
    0 0 28px rgba(14,165,233,0.6);
}

/* ================================
INPUT BOXES
================================ */
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {

    background:
    rgba(255,255,255,0.08) !important;

    color: white !important;

    border-radius: 14px !important;

    border:
    1px solid rgba(255,255,255,0.08);

    padding: 10px;
}

/* ================================
SLIDERS
================================ */
.stSlider > div > div {

    color: #38bdf8 !important;
}

/* ================================
METRICS
================================ */
div[data-testid="metric-container"] {

    background:
    rgba(255,255,255,0.06);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 18px;

    box-shadow:
    0 6px 22px rgba(0,0,0,0.25);

    backdrop-filter: blur(14px);
}

/* ================================
TABS
================================ */
button[data-baseweb="tab"] {

    font-size: 16px;

    font-weight: 700;

    color: #cbd5e1 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {

    color: white !important;

    border-bottom:
    4px solid #38bdf8;
}

/* ================================
DATAFRAME
================================ */
[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;
}

/* ================================
SCROLLBAR
================================ */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #38bdf8;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATASET
# =====================================================
df = pd.read_csv(
    "notebook/ambulance_updated_dataset (3).csv"
)

df.columns = df.columns.str.strip()

# =====================================================
# TITLE
# =====================================================
st.title("🚑 Smart Ambulance AI System")

st.markdown("""
<div style='text-align:center;
font-size:20px;
color:#cbd5e1;
margin-bottom:30px;'>

AI Powered Emergency Response & Resource Allocation Dashboard

</div>
""", unsafe_allow_html=True)

# =====================================================
# TABS
# =====================================================
tab1, tab2, tab3 = st.tabs([
    "📊 Demand Prediction",
    "🚨 Allocation",
    "📍 Emergency Insights"
])

# =====================================================
# TAB 1
# =====================================================
with tab1:

    st.header("📊 Ambulance Demand Prediction")

    col1, col2 = st.columns(2)

    with col1:

        latitude = st.number_input(
            "📍 Latitude",
            value=19.07,
            format="%.2f"
        )

        longitude = st.number_input(
            "📍 Longitude",
            value=72.87,
            format="%.2f"
        )

        hour = st.slider(
            "🕒 Hour",
            0, 23, 12
        )

        traffic = st.selectbox(
            "🚦 Traffic Level",
            ["Low", "Medium", "High"]
        )

    with col2:

        temp = st.slider(
            "🌡️ Temperature",
            10, 50, 30
        )

        rain = st.selectbox(
            "🌧️ Rain Status",
            ["No", "Yes"]
        )

        emergency = st.selectbox(
            "🚨 Emergency Type",
            ["Accident", "Heart Attack", "Fire", "Other"]
        )

        day_name = st.selectbox(
            "📅 Day",
            [
                "Monday", "Tuesday",
                "Wednesday", "Thursday",
                "Friday", "Saturday",
                "Sunday"
            ]
        )

    # =====================================================
    # LOGIC
    # =====================================================
    traffic_map = {
        "Low": 5,
        "Medium": 10,
        "High": 20
    }

    rain_map = {
        "No": 0,
        "Yes": 15
    }

    emergency_map = {
        "Accident": 15,
        "Heart Attack": 25,
        "Fire": 30,
        "Other": 5
    }

    day_map = {
        "Monday": 5,
        "Tuesday": 5,
        "Wednesday": 5,
        "Thursday": 5,
        "Friday": 10,
        "Saturday": 15,
        "Sunday": 15
    }

    # =====================================================
    # PREDICT BUTTON
    # =====================================================
    if st.button("🔍 Predict Ambulance Demand"):

        score = (
            hour +
            traffic_map[traffic] +
            temp +
            rain_map[rain] +
            emergency_map[emergency] +
            day_map[day_name]
        )

        st.subheader("🚑 Prediction Result")

        st.info(
            f"📍 Location: {latitude}, {longitude}"
        )

        if score > 120:

            st.error(
                "🔴 HIGH Ambulance Demand Expected"
            )

        elif score > 80:

            st.warning(
                "🟡 MEDIUM Ambulance Demand Expected"
            )

        else:

            st.success(
                "🟢 LOW Ambulance Demand Expected"
            )

        st.metric(
            "📊 Demand Score",
            score
        )

# =====================================================
# TAB 2
# =====================================================
with tab2:

    st.header("🚨 Smart Allocation System")

    col1, col2 = st.columns(2)

    with col1:

        priority = st.selectbox(
            "⚡ Priority Level",
            ["Low", "Medium", "High"]
        )

    with col2:

        traffic2 = st.selectbox(
            "🚦 Traffic Condition",
            ["Low", "Medium", "High"]
        )

    if st.button("🚑 Allocate Ambulance"):

        base_ambulance = {
            "Low": 1,
            "Medium": 2,
            "High": 4
        }

        traffic_delay = {
            "Low": 5,
            "Medium": 10,
            "High": 20
        }

        st.subheader("🚨 Allocation Result")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🚑 Ambulances",
            base_ambulance[priority]
        )

        c2.metric(
            "⏱️ Response Time",
            f"{10 + traffic_delay[traffic2]} mins"
        )

        c3.metric(
            "🚦 Traffic",
            traffic2
        )

        c4.metric(
            "⚡ Priority",
            priority
        )

# =====================================================
# TAB 3
# =====================================================
with tab3:

    st.header("📍 Emergency Insights Dashboard")

    emergency_selected = st.selectbox(
        "🚨 Select Emergency Type",
        df['emergency_type'].unique()
    )

    if st.button("📈 Analyze Emergency Data"):

        data = df[
            df['emergency_type']
            == emergency_selected
        ]

        total_cases = len(data)

        avg_temp = data[
            'temperature'
        ].mean()

        col1, col2 = st.columns(2)

        col1.metric(
            "📌 Total Cases",
            total_cases
        )

        col2.metric(
            "🌡️ Avg Temperature",
            round(avg_temp, 2)
        )

        if avg_temp > 30:

            st.warning(
                "⚠️ High Risk Zone Detected"
            )

        else:

            st.success(
                "✅ Normal Risk Zone"
            )

        st.subheader(
            "📋 Sample Emergency Records"
        )

        st.dataframe(
            data.head(10),
            use_container_width=True
        )

# =====================================================
# FOOTER
# =====================================================
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
text-align:center;
padding:20px;
border-radius:20px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
">

<h3 style="
color:white;
margin-bottom:8px;
">

🚑 Smart Ambulance Emergency Management System

</h3>

<p style="
color:#cbd5e1;
font-size:15px;
">

AI Based Emergency Prediction & Resource Allocation

</p>

</div>
""", unsafe_allow_html=True)