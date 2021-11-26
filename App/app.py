import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout='wide')


@st.cache(allow_output_mutation=True)
def get_data(path):
    return pd.read_csv(path)


st.markdown("<h1 style='text-align: center; color: blue;'>Dados completos BRK</h1>",
            unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: blue;'>Dados completos BRK</h1>",
            unsafe_allow_html=True)
col1, col2 = st.columns(2)

# Get data
path = '/home/maksonvinicio/Documents/GitHub/Datathon-BRK/Data/all_data.csv'
path_new = '/home/maksonvinicio/Documents/GitHub/Datathon-BRK/Data/data_filtered_new_uruguaiana.csv'

data = get_data(path)
data['Investimentos_per_capita_em_saneamento'] = data['Investimentos_per_capita_em_saneamento'].fillna(
    0)
filtered = get_data(path_new)
filtered['Investimentos_per_capita_em_saneamento'] = filtered['Investimentos_per_capita_em_saneamento'].fillna(
    0)

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
municipios_new = st.sidebar.multiselect('Municípios Mapeados', filtered['Município'].unique().tolist())
municipios = data[data['Município'].isin(municipio)]
municipios_filtered = data[data['Município'].isin(municipios_new)]

# Mapas
col1.subheader('Municípios')
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

col2.subheader('Novas Uruguaianas em 2019')
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

# Plot
indicadores = st.sidebar.multiselect('Indicadores', data.columns[2:])
plt.figure(figsize=(15, 8))
fig = px.line(municipios, x='Ano', y=indicadores, color='Município',)
st.plotly_chart(fig, use_container_width=True)


plt.figure(figsize=(15, 8))
fig = px.line(municipios_filtered, x='Ano', y=indicadores, color='Município',)
st.plotly_chart(fig, use_container_width=True)



# Filtrando os anos

col1.dataframe(data[data['Ano'] == year])
col2.dataframe(filtered[filtered['Ano'] == year])