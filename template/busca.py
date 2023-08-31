import streamlit  as st
from streamlit_player import st_player


def busca_musicas():
    c1,c2,c3 = st.columns(3)
    with c2:
        header = st.subheader("Procure suas musicas")
        suorce = st.text_input("Musicas",placeholder="Busque a qui sua melhores musicas")
        confirma = st.button("buscar")
    if(confirma):
        st_player(f"https://soundcloud.com/{suorce}", height=600)