import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout='wide')


@st.cache(allow_output_mutation=True)
def get_data(path):
    return pd.read_csv(path)


st.markdown("<h1 style='text-align: center; color: blue;'>Dados completos BRK</h1>",
            unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: blue;'>Com intuito de promover uma análise rápida, a solução traz um compilado dos dados do Painel do Saneamento, e proporciona agilidade na comparação de indicadores, visualização de novos pontos de investimentos baseado no município de Uruguaiana, além de uma visualização rápida dos dados por ano.</h1>",
            unsafe_allow_html=True)
st.image('Img/capa1.gif', output_format='gif')


col1, col2 = st.columns(2)

# Get data
path = 'Data/all_data.csv'
path_new = 'Data/data_filtered_new_uruguaiana.csv'


data = get_data(path)
data['Investimentos_per_capita_em_saneamento'] = data['Investimentos_per_capita_em_saneamento'].fillna(
    0)
filtered = get_data(path_new)
filtered['Investimentos_per_capita_em_saneamento'] = filtered['Investimentos_per_capita_em_saneamento'].fillna(
    0)

st.sidebar.title('Filtros')

year = st.sidebar.slider('Ano', 2010, 2019, 2019)


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
municipios_new = st.sidebar.multiselect(
    'Municípios Mapeados', filtered['Município'].unique().tolist())
municipios = data[data['Município'].isin(municipio)]
municipios_filtered = data[data['Município'].isin(municipios_new)]

# Mapas
col1.markdown("<h3 style='text-align: center; color: blue;'>Municípios</h1>", unsafe_allow_html=True)
fig = px.scatter_mapbox(data, lat="lat", lon="lng", size='Investimentos_per_capita_em_saneamento', hover_name="Município",
                        color_discrete_sequence=["blue"], zoom=3, height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
    ])
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
col1.plotly_chart(fig)

col2.markdown("<h3 style='text-align: center; color: blue;'>Municípios mapeados (2019)</h1>", unsafe_allow_html=True)
fig = px.scatter_mapbox(filtered, lat="lat", lon="lng", size='Investimentos_per_capita_em_saneamento', hover_name="Município",
                        color_discrete_sequence=["blue"], zoom=3, height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
    ])
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
col2.plotly_chart(fig)


# Filtrando os anos
if year == 2019:
    col1.subheader('Indicadores dos municípios')
    col1.dataframe(data[data['Ano'] == year])
    col2.subheader('Indicadores dos municípios filtrados')
    col2.dataframe(filtered[filtered['Ano'] == year])
else:
    st.dataframe(data[data['Ano'] == year])

# Plot
indicadores = st.sidebar.multiselect('Indicadores', data.columns[2:])
st.markdown("<h3 style='text-align: center; color: blue;'>Comparação de indicadores</h1>", unsafe_allow_html=True)

plt.figure(figsize=(15, 8))
fig = px.line(municipios, x='Ano', y=indicadores, color='Município',)
st.plotly_chart(fig, use_container_width=True)


plt.figure(figsize=(15, 8))
fig = px.line(municipios_filtered, x='Ano', y=indicadores, color='Município', line_shape='spline')

st.plotly_chart(fig, use_container_width=True)
