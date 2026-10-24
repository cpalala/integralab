import streamlit as st
import sympy as sp
from modules import ui
from modules.solver import x

ui.hero("Belajar Integral Jadi Lebih Mudah",
        "Materi ringkas, kalkulator dengan langkah penyelesaian, grafik luas daerah, dan simulasi Riemann interaktif.",
        badge="Kalkulus · Integral tak tentu dan tentu")

st.markdown("### Mulai belajar")
FITUR = [("📘", "Materi", "Konsep, rumus, teorema, dan sifat integral.", "pages/1_Materi.py", "Buka materi →"),
         ("🧮", "Integral Tak Tentu", "Hitung antiturunan dengan langkah lengkap.", "pages/2_Integral_Tak_Tentu.py", "Buka kalkulator →"),
         ("📈", "Integral Tentu", "Hitung luas daerah, grafik, dan simulasi Riemann.", "pages/3_Integral_Tentu.py", "Buka kalkulator →")]
for col, (ico, judul, ket, path, label) in zip(st.columns(3), FITUR):
    with col.container(border=True):
        st.markdown(f"#### {ico} {judul}")
        st.caption(ket)
        st.page_link(path, label=label)

st.markdown("### Tujuan belajar")
t = st.columns(3)
t[0].info("**Memahami** integral tak tentu dan tentu")
t[1].info("**Mengetahui** aturan integral tak tentu dan tentu")
t[2].info("**Menyelesaikan** integral tak tentu dan tentu")

st.markdown("### Coba contoh langsung")
CONTOH = {"Contoh 1": 2 * x**2 - 5 * x + 4, "Contoh 2": sp.sqrt(x) - 2 / x**3, "Contoh 3": 4 * x * (2 * x**2 - 4) ** 2}
pilih = st.radio("Pilih contoh dari materi", list(CONTOH), horizontal=True)
f = CONTOH[pilih]
st.latex(rf"\int {sp.latex(f)}\,dx = {sp.latex(sp.integrate(f, x))} + C")

st.divider()
st.caption("Proyek kelompok mata kuliah Kalkulus · Dosen: Permata, S.Si., M.Si.")
