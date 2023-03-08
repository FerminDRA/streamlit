import streamlit as st
import pandas as pd
import numpy as np

st.title('Cicle Rides in NYC')
st.header("Fermin Del Rosario Antonio")
st.header("zs19004879@estudiantes.uv.mx")

st.sidebar.image("logoImg.jpg")
st.sidebar.markdown("##")

DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading.....')
data = load_data(500)
data_load_state.text("Done!")

if st.sidebar.checkbox('Mostrar tabla'):
    st.subheader('Tabla de recorridos')
    st.write(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

hour_to_filter = st.sidebar.slider('Hora', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de recorridos alas %s:00' % hour_to_filter)
st.map(filtered_data)