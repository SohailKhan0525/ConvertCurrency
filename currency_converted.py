import streamlit as st
import requests

st.title("Convert Currency into Another Currency")
amount = st.number_input("Enter your amount: ", min_value=1)

url = "https://api.exchangerate-api.com/v4/latest/INR"
response = requests.get(url)
data = response.json()
currency = list(data["rates"].keys())
target = st.selectbox("Convert to ", currency)

if st.button("Convert"):
    rate = data["rates"][target]
    convert = amount * rate
    st.success(f"{amount} INR = {convert} {target}")
