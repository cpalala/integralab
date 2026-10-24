import streamlit as st
from modules import ui

st.set_page_config(page_title="IntegraLab", page_icon="∫", layout="wide")
ui.inject_css()

pg = st.navigation([
    st.Page("home.py", title="Beranda", icon="🏠", default=True),
    st.Page("pages/1_Materi.py", title="Materi", icon="📘"),
    st.Page("pages/2_Integral_Tak_Tentu.py", title="Integral Tak Tentu", icon="🧮"),
    st.Page("pages/3_Integral_Tentu.py", title="Integral Tentu", icon="📈"),
    st.Page("pages/4_Tentang.py", title="Tentang", icon="ℹ️"),
])
pg.run()
