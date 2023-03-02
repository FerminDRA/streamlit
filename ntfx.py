import pandas as pd
import streamlit as st
import codecs


name_link =codecs.open('movies.csv','rU','latin1')


st.title('netflix app')

#--- LOGO ---#
st.sidebar.image("logo.jpg")
st.sidebar.markdown("##")

@st.cache
def load_data(nrows):
    name_link = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(name_link, nrows=nrows)
    return data

data_load_state = st.text('cargando')
data = load_data(500)
data_load_state.text('netflix app!! (using st.cache)')

st.dataframe(data)

sidebar=st.sidebar
agree=sidebar.checkbox("Mostrar todos los filmes")
if agree:
    load_data(500)
sidebar.markdown(name_link)

selectitle = sidebar._text_input('Select title of the film')

button_name = st.button("Buscar")
if(button_name):
    st.dataframe(selectitle)
st.markdown("__")


if(button_name):
    filterbyname = load_data(name_link)
    count_row = filterbyname.shape[0]
    st.write("total names: {count_row}")

    st.dataframe(filterbyname)
name = sidebar.text_input("Titulo del filme")
btnbuscar = sidebar.button('Buscar filme')

if(btnbuscar):
    filterbyname = load_data(name)
    count_row = filterbyname.shape[0]
    st.write("total names: {count_row}")

    st.dataframe(filterbyname)