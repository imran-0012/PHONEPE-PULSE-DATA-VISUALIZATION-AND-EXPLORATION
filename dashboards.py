# =========================================================
# PhonePe Pulse Analytics Dashboard 
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PhonePe Pulse Dashboard",
    layout="wide"
)

st.title("📊 PhonePe Pulse Analytics Dashboard")
st.markdown("Analyze Transactions, Insurance and Users Data")

# =========================================================
# LOAD DATA
# =========================================================

transaction_df = pd.read_csv("Agg_transaction.csv")
users_df = pd.read_csv("Agg_user.csv")
insurance_df = pd.read_csv("Agg_insurence.csv")

transaction_df.columns = transaction_df.columns.str.strip()
users_df.columns = users_df.columns.str.strip()
insurance_df.columns = insurance_df.columns.str.strip()

# Rename for consistency
users_df.rename(columns={"state_user": "State"}, inplace=True)

# =========================================================
# STATE CLEANER + MAPPING
# =========================================================

def clean_state(series):
    return (
        series.astype(str)
        .str.strip()
        .str.lower()
        .str.replace("&", "&", regex=False)
        .str.replace("-", " ", regex=False)
    )

STATE_MAP = {
    'andaman & nicobar islands': 'Andaman and Nicobar',
    'andaman and nicobar islands': 'Andaman and Nicobar',
    'andhra pradesh': 'Andhra Pradesh',
    'arunachal pradesh': 'Arunachal Pradesh',
    'assam': 'Assam',
    'bihar': 'Bihar',
    'chandigarh': 'Chandigarh',
    'chhattisgarh': 'Chhattisgarh',
    'dadra & nagar haveli & daman & diu': 'Dadra and Nagar Haveli and Daman and Diu',
    'dadra and nagar haveli and daman and diu': 'Dadra and Nagar Haveli and Daman and Diu',
    'delhi': 'Delhi',
    'goa': 'Goa',
    'gujarat': 'Gujarat',
    'haryana': 'Haryana',
    'himachal pradesh': 'Himachal Pradesh',
    'jammu & kashmir': 'Jammu and Kashmir',
    'jammu and kashmir': 'Jammu and Kashmir',
    'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka',
    'kerala': 'Kerala',
    'ladakh': 'Ladakh',
    'lakshadweep': 'Lakshadweep',
    'madhya pradesh': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'odisha': 'Orissa',
    'puducherry': 'Puducherry',
    'punjab': 'Punjab',
    'rajasthan': 'Rajasthan',
    'sikkim': 'Sikkim',
    'tamil nadu': 'Tamil Nadu',
    'telangana': 'Telangana',
    'tripura': 'Tripura',
    'uttar pradesh': 'Uttar Pradesh',
    'uttarakhand': 'Uttarakhand',
    'uttaranchal': 'Uttarakhand',
    'west bengal': 'West Bengal'
}

# Apply cleaning
transaction_df["State"] = clean_state(transaction_df["State"]).replace(STATE_MAP)
users_df["State"] = clean_state(users_df["State"]).replace(STATE_MAP)
insurance_df["State"] = clean_state(insurance_df["State"]).replace(STATE_MAP)

# =========================================================
# LOAD GEOJSON
# =========================================================

@st.cache_data
def load_geojson():
    url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson"
    return requests.get(url).json()

india_states = load_geojson()

# =========================================================
# MAP FUNCTION 
# =========================================================

def create_india_map(df, state_col, value_col, title):

    map_df = df.copy()

    map_df[state_col] = map_df[state_col].astype(str).str.strip()

    map_df = map_df.groupby(state_col, as_index=False)[value_col].sum()

    fig = px.choropleth(
        map_df,
        geojson=india_states,
        featureidkey="properties.NAME_1",
        locations=state_col,
        color=value_col,
        hover_name=state_col,
        color_continuous_scale="Viridis",
        title=title
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=700)

    return fig

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🔍 Filters")

selected_state = st.sidebar.multiselect(
    "Select State",
    transaction_df["State"].unique(),
    default=transaction_df["State"].unique()
)

selected_year = st.sidebar.multiselect(
    "Select Year",
    transaction_df["Year"].unique(),
    default=transaction_df["Year"].unique()
)

# =========================================================
# FILTER DATA
# =========================================================

filtered_transaction = transaction_df[
    (transaction_df["State"].isin(selected_state)) &
    (transaction_df["Year"].isin(selected_year))
]

# =========================================================
# KPI
# =========================================================

total_transactions = filtered_transaction["Transaction_count"].sum()
total_amount = filtered_transaction["Transaction_amount"].sum()

col1, col2 = st.columns(2)

col1.metric("💳 Total Transactions", f"{int(total_transactions):,}")
col2.metric("💰 Total Amount", f"₹ {total_amount:,.0f}")

st.divider()

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs(["💳 Transactions", "🛡 Insurance", "👥 Users"])

# =========================================================
# TAB 1 - TRANSACTIONS
# =========================================================

with tab1:

    st.subheader("State-wise Transactions")

    state_txn = filtered_transaction.groupby("State")["Transaction_amount"].sum().reset_index()

    st.plotly_chart(
        px.bar(state_txn, x="State", y="Transaction_amount", text_auto=True),
        use_container_width=True
    )

    st.subheader("Transaction Type")

    type_txn = filtered_transaction.groupby("Transaction_type")["Transaction_amount"].sum().reset_index()

    st.plotly_chart(
        px.pie(type_txn, names="Transaction_type", values="Transaction_amount"),
        use_container_width=True
    )

    st.subheader("🗺 Map")

    st.plotly_chart(
        create_india_map(state_txn, "State", "Transaction_amount",
                         "Transaction Map"),
        use_container_width=True
    )

# =========================================================
# TAB 2 - INSURANCE
# =========================================================

with tab2:

    st.subheader("Insurance Overview")

    col1, col2 = st.columns(2)

    col1.metric("Insurance Count", f"{int(insurance_df['insurance_count'].sum()):,}")
    col2.metric("Insurance Amount", f"₹ {insurance_df['insurance_amount'].sum():,.0f}")

    ins_state = insurance_df.groupby("State")["insurance_amount"].sum().reset_index()

    st.plotly_chart(
        px.bar(ins_state, x="State", y="insurance_amount"),
        use_container_width=True
    )

    st.plotly_chart(
        px.pie(
            insurance_df.groupby("insurance_type")["insurance_amount"].sum().reset_index(),
            names="insurance_type",
            values="insurance_amount"
        ),
        use_container_width=True
    )

    st.subheader("🗺 Insurance Map")

    st.plotly_chart(
        create_india_map(ins_state, "State", "insurance_amount",
                         "Insurance Map"),
        use_container_width=True
    )

# =========================================================
# TAB 3 - USERS
# =========================================================

with tab3:

    st.subheader("Users Overview")

    col1, col2 = st.columns(2)

    col1.metric("Registered Users", f"{int(users_df['reg_user'].sum()):,}")
    col2.metric("App Opens", f"{int(users_df['app_open'].sum()):,}")

    user_state = users_df.groupby("State")["reg_user"].sum().reset_index()

    st.plotly_chart(
        px.bar(user_state, x="State", y="reg_user"),
        use_container_width=True
    )

    st.plotly_chart(
        px.pie(user_state, names="State", values="reg_user", hole=0.4),
        use_container_width=True
    )

    st.subheader("🗺 Users Map")

    st.plotly_chart(
        create_india_map(user_state, "State", "reg_user",
                         "Users Map"),
        use_container_width=True
    )

# =========================================================
# END
# =========================================================
