import requests
import streamlit as st
from streamlit_option_menu import option_menu
from template.home import home
from template.busca import busca_musicas
from template.list import list
from template.top50 import top50

st.set_page_config(layout="wide")

with st.sidebar:
    selected = option_menu("Player", ["Home", 'Busca','Top 50','Play liste'], 
        icons=['boombox-fill', 'music-player', 'vinyl-fill', 'music-note-list'], menu_icon="soundwave", default_index=0,
    )

if(selected == "Home"):
    home()
elif(selected == "Busca"):
    busca_musicas()
elif(selected == "Play liste"):
    list()
elif(selected == "Top 50"):
    top50()