import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout='wide')


@st.cache(allow_output_mutation=True)
def get_data(path):
    return pd.read_csv(path)


st.title('Dados completos BRK')

# Get data
path = '/home/maksonvinicio/Documents/GitHub/Datathon-BRK/Data/all_data.csv'

data = get_data(path)

year = st.sidebar.slider('Ano', 2010, 2019, 2015)

# Filtrando os anos
df = data[data['Ano'] == year]

# Filtrando os municipios da BRK
municipio_brk = ['Rio de janeiro (Município)',
                 'Uruguaiana (Município)',
                 'Cachoeiro de Itapemirim (Município)',
                 'São José de Ribamar (Município)',
                 'Salvador (Município)',
                 'Blumenau (Município)',
                 'Rio Verde (Município)',
                 'Palmas (Município)',
                 'Olinda (Município)',
                 ]

municipio = st.sidebar.multiselect('Municípios BRK', municipio_brk)

municipios = data[data['Município'].isin(municipio)]
st.write(municipios)

# Plot
indicadores = st.sidebar.multiselect('Indicadores', data.columns[2:])
plt.figure(figsize=(15, 8))
fig = px.line(municipios, x='Ano', y=indicadores, color='Município',)

st.plotly_chart(fig, use_container_width=True)
