import streamlit as st
import pandas as pd

st.title("Streamlit - Search ranges")
DATA_URL="https://firebasestorage.googleapis.com/v0/b/tourheroes-a706b.appspot.com/o/datasets%2Ffermin%2Fdataset.csv?alt=media&token=9dacdc0d-506e-439f-8e73-12a39d6a4373"


@st.cache
def load_data_byrange(startid, endid):
    data= pd.read_csv(DATA_URL)
    filtered_data_byrange= data[(data["index"]>= startid) & (data["index"]<= endid)]

    return filtered_data_byrange

startid=st.text_input("Start index : ")
endid=st.text_input("End index")
btnRange=st.button("Search by range")
if (btnRange):
    filter_byrange=load_data_byrange(int(startid), int(endid))
    count_row=filter_byrange.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filter_byrange)
