import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from folium import plugins
# from streamlit_folium import folium_static

st.set_page_config(page_title="Manguezais da GRMA")

# with open('assets/style.css') as f:
# css = f.read()
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with st.container():
    st.subheader("O maior contínuo de manguezais do planeta")
    st.title("Manguezais da Grande Reserva da Mata Atlântica")
    st.write(
        "Explore uma série de dados e informações sobre os manguezais da GRMA")


with st.container():
    # Criar um mapa Folium básico
    
    mapaGRMA = folium.Map(
        location=[-25.357190402362466, -46.939575287205884], zoom_start=7.5)

    folium.WmsTileLayer(url='https://ide.lageamb.ufpr.br/geoserver/geonode/wms?',
                        name='Manguezais da GRMA',
                        fmt='image/png',
                        layers='BIO_manguezaisGRMA',
                        transparent=True,
                        overlay=True,
                        control=True,).add_to(mapaGRMA)

    # Adicionar controle de camadas (LayerControl) para permitir que o usuário ative/desative camadas
    folium.LayerControl().add_to(mapaGRMA)

    # Exibir o mapa no Streamlit usando st.write
    st.write("### Localização dos manguezais na GRMA")
    st_folium(mapaGRMA, width=700, height=450)

st.write(
        "A Elevação do nível do mar e aquecimento da atmosfera ameaçam a conservação desses ecossistemas costeiros, que são berçários da vida marinha e podem conter duas vezes mais carbono por hectare do que florestas tropicais. Especialmente por sua capacidade de estoque em sua biomassa abaixo do solo, que é altamente orgânico. Apesar dos manguezais da Grande Reserva não apresentarem dosséis altos quando comparados a região norte do país, são muito importantes devido a sua série de serviços ecossistêmicos . Apesar disso, encontram-se altamente ameaçados")
col1, col2 = st.columns(2)

with col1:
    # Criar um mapa Folium básico
    mapaBiomass = folium.Map(
        location=[-25.357190402362466, -46.939575287205884], zoom_start=7.5, tiles="cartodb positron")

    folium.WmsTileLayer(url='http://webmap.ornl.gov/ogcbroker/wms?',
                        name='Biomass aboveground',
                        fmt='image/png&amp',
                        layers='1665_13',
                        transparent=True,
                        overlay=True,
                        control=True).add_to(mapaBiomass)

    # Adicionar controle de camadas (LayerControl) para permitir que o usuário ative/desative camadas
    folium.LayerControl().add_to(mapaBiomass)

    # Exibir o mapa no Streamlit usando st.write
    st.write("### Biomassa abaixo do solo")
    st_folium(mapaBiomass, width=700, height=450)


with col2:
    # Criar um mapa Folium básico
    mapaCanopy = folium.Map(
        location=[-25.357190402362466, -46.939575287205884], zoom_start=7.5, tiles="cartodb positron")

    folium.WmsTileLayer(url='http://webmap.ornl.gov/ogcbroker/wms?',
                        name='Canopy heigh',
                        fmt='image/png&amp',
                        layers='1665_245',
                        transparent=True,
                        overlay=True,
                        control=True).add_to(mapaCanopy)

    # Adicionar controle de camadas (LayerControl) para permitir que o usuário ative/desative camadas
    folium.LayerControl().add_to(mapaCanopy)

    # Exibir o mapa no Streamlit usando st.write
    st.write("### Altura Máxima das árvores")
    st_folium(mapaCanopy, width=700, height=450)

with st.container():
    st.subheader("Pressão antrópica x Manguezais")
    st.write(
        "No litoral do Paraná, os fatores geradores de significativos efeitos negativos sobre os manguezais englobam o desmatamento para fins de expansão urbana, de atividades industrial, portuária, entre outros; a exploração de madeira; especulação imobiliária; potenciais riscos da aquicultura; contaminação por petróleo e seus derivados, fertilizantes, defensivos agrícolas ou metais pesados; dragagens; aterros para construção de vias de acesso; entre outros(LANA, 2004). ")
    st.write(
        "Esse cenário é bastante comum á região da GRMA, o que levou ao decrescimo da presença de florestas de mangue no bioma")

import pandas as pd
import altair as alt

# Carrega os dados do arquivo Excel
@st.cache
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Função para agrupar e contabilizar os registros por ano
def agrupar_por_ano(df):
    df_agrupado = df.groupby('year')['area_km'].sum().reset_index()
    return df_agrupado

# Função para filtrar os dados pelo intervalo de anos selecionado pelo usuário
def filtrar_por_intervalo(df, ano_inicio, ano_fim):
    df_filtrado = df[(df['year'] >= ano_inicio) & (df['year'] <= ano_fim)]
    return df_filtrado

# Título do dashboard
st.title('Dashboard de Desmatamento')

# Carrega os dados
file_path = 'desmatamentoGRMA.xlsx'
df = load_data(file_path)

# Sidebar para selecionar o intervalo de anos
ano_inicio = st.sidebar.slider('Ano de início', min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].min()))
ano_fim = st.sidebar.slider('Ano de fim', min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].max()))

# Filtra os dados pelo intervalo selecionado
df_filtrado = filtrar_por_intervalo(df, ano_inicio, ano_fim)

# Agrupa os dados filtrados por ano
df_agrupado = agrupar_por_ano(df_filtrado)

# Cria o gráfico de linhas usando Altair
chart = alt.Chart(df_agrupado).mark_line().encode(
    x='year:O',
    y='area_km:Q',
    tooltip=['year:O', 'area_km:Q']
).properties(
    width=800,
    height=400
).interactive()

# Mostra o gráfico
st.altair_chart(chart, use_container_width=True)
