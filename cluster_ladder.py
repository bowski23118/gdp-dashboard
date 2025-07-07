import streamlit as st

st.title("📊 Cluster Ladder Builder")

underlying = st.text_input("Underlying Symbol", "SPY")
current_price = st.number_input("Current Price", min_value=0.0, value=500.0, step=1.0)
forecast_pct = st.slider("Cluster Forecast Expected Move (%)", 1.0, 10.0, 3.5, step=0.1)
days = st.slider("Days to Expected Spike", 1, 10, 4, step=1)
budget = st.number_input("Total Risk Budget ($)", min_value=100.0, value=1300.0, step=50.0)

if st.button("Build Cluster Ladder"):
    move = current_price * (forecast_pct / 100)

    call1 = round(current_price + move * 0.6, 2)
    call2 = round(current_price + move, 2)
    call3 = round(current_price + move * 1.4, 2)

    put1 = round(current_price - move * 0.6, 2)
    put2 = round(current_price - move, 2)
    put3 = round(current_price - move * 1.4, 2)

    atm_alloc = budget * 0.45
    otm_alloc = budget * 0.3
    spread_alloc = budget * 0.25

    st.subheader("Cluster Ladder Structure")

    st.markdown(f"""
    **▶ ATM CALL:** Buy at **{current_price}**, ~${atm_alloc/2:.0f}<br>
    **▶ OTM CALL:** Buy at **{call2}**, ~${otm_alloc/2:.0f}<br>
    **▶ CALL SPREAD:** Buy **{call3}** / Sell **{call3+5}**, ~${spread_alloc/2:.0f}<br>
    **▶ ATM PUT:** Buy at **{current_price}**, ~${atm_alloc/2:.0f}<br>
    **▶ OTM PUT:** Buy at **{put2}**, ~${otm_alloc/2:.0f}<br>
    **▶ PUT SPREAD:** Buy **{put3}** / Sell **{put3-5}**, ~${spread_alloc/2:.0f}
    """, unsafe_allow_html=True)

    st.success("✅ Cluster Ladder ready. Enter these legs into your broker.")

