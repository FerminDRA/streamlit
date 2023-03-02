import streamlit as st
import pandas as pd
import codecs

st.title("Netflix App")
st.header("Fermin Del Rosario Antonio")
st.header("S19004879")

DATA_URL = ('movies2.csv')
sidebar= st.sidebar
st.sidebar.image("logoImg.jpg")
st.sidebar.markdown("##")

@st.cache
def load_data(nrows):
    f = codecs.open(DATA_URL,'r', encoding='latin')
    data=pd.read_csv(f,nrows=nrows)
    return data

def filtro_pelicula(pelicula):
    pelicula_filt = data[data['name'].str.upper().str.contains(pelicula)]
    return pelicula_filt

def filtro_director(director):
    director_filt = data[data['director'] == director]
    return director_filt

data_load_state= st.text("Loading data...")
data= load_data(1000)
data_load_state.text("Done!")

st.header("Peliculas")
agree=sidebar.checkbox("Mostrar todos los filmes")
if agree:
    st.dataframe(data)

titulofilme = st.sidebar.text_input('Titulo de la pelicula :')
botonBuscar = st.sidebar.button('Buscar pelicula')

if (botonBuscar):
   peliculas = filtro_pelicula(titulofilme.upper())
   count_row = peliculas.shape[0]  # Gives number of rows
   st.write(f"Total filmes mostrados : {count_row}")
   st.write(peliculas)

selDirector = st.sidebar.selectbox("Director", data['director'].unique())
botonFiltroDirector = st.sidebar.button('Filtro director')

if (botonFiltroDirector):
   director = filtro_director(selDirector)
   count_row = director.shape[0]  # Gives number of rows
   st.write(f"Total filmes : {count_row}")

   st.dataframe(director)