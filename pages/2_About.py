import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Sobre o portal")

with st.container():
    st.subheader("Sobre")
    st.title("Grande Reserva da Mata Atântica (GRMA)")
    st.write(
        "A Grande Reserva Mata Atlântica é uma região de rara beleza que abriga o maior contínuo bem conservado deste bioma no mundo.  Este território, localizado entre os estados de São Paulo, Paraná e Santa Catarina, ainda mantém quase toda sua diversidade de ambientes e espécies da fauna e da flora, além de sua riqueza cultural e histórica. É justamente esta riqueza que torna a Grande Reserva Mata Atlântica uma oportunidade única para o desenvolvimento a partir do conceito de Produção de Natureza.​")
    st.image(
            "https://grandereservamataatlantica.com.br/wp-content/uploads/2023/05/grande-reserva-mata-atlantica-mapa-atual-2023.jpg",
            width=400) # Manually Adjust the width of the image as per requirement)