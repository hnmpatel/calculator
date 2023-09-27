import calculator
import streamlit as st

tab1, tab2, tab3 = st.tabs([
    "EMI Calculator", "Tenure Calculator", "SIP Calculator"
])

with tab1:
    st.header("EMI Calculator")
    principal = st.number_input('Principal Amount: ', min_value=10000, step=1000)
    tenure = st.slider('Tenure in Years', min_value=1, max_value=30, value=5, step=1, key='tenure')
    interest_rate = st.number_input('Interest Rate: ', min_value=1.0, step=0.05, value=9.0)
    st.write('Principal - ', principal)
    st.write('Tenure - ', tenure)
    st.write('Interest Rate - ', interest_rate)
    emi = calculator.calculate_emi(principal, interest_rate, tenure)
    st.subheader('Calculated EMI - ')
    st.write(round(emi, 2))


with tab2:
    st.header("Tenure Calculator")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("SIP Calculator")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)