import pandas as pd
import streamlit as st
names_link = '/home/fermin/streamlit/dataset.csv'
names_data = pd.read_csv(names_link)

st.title("Streamlit and pandas")
st.dataframe(names_data)