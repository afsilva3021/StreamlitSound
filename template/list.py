import streamlit  as st
from streamlit_player import st_player


def list():
    st_player("https://soundcloud.com/alex-felix-997010505/sets/rock", height=600)