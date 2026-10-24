from pathlib import Path
import streamlit as st


def inject_css():
    css = (Path(__file__).resolve().parent.parent / "assets" / "style.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def hero(title, subtitle="", badge=""):
    b = f'<div class="badge">{badge}</div>' if badge else ""
    st.markdown(f'<div class="hero">{b}<h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)
