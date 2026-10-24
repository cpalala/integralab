import streamlit as st
from modules import ui

ui.hero("Tentang", "Proyek kelompok mata kuliah Kalkulus.", badge="Kelompok · Kalkulus")

st.markdown("### IntegraLab")
st.write("IntegraLab adalah aplikasi pembelajaran integral tak tentu dan tentu. Aplikasi ini memuat materi, "
         "kalkulator dengan langkah penyelesaian, grafik luas daerah, dan simulasi jumlah Riemann.")

info = st.columns(2)
with info[0].container(border=True):
    st.markdown("#### 📚 Mata kuliah")
    st.write("Kalkulus")
with info[1].container(border=True):
    st.markdown("#### 👩‍🏫 Dosen pengampu")
    st.write("Permata, S.Si., M.Si.")

st.markdown("### Anggota kelompok")
ANGGOTA = [("Candra Palala", "26312010"), ("Muhammad Ibad Nazmi", "26312015"),
           ("Keysha Dwi Febniza", "26312042"), ("Relita Ayu Amellia", "26312001")]
for col, (nama, npm) in zip(st.columns(4), ANGGOTA):
    with col.container(border=True):
        st.markdown(f"#### {nama}")
        st.caption(f"NPM {npm}")

st.markdown("### Teknologi")
st.write("Python, Streamlit, SymPy, NumPy, dan Plotly.")
st.caption("Sumber materi: slide kuliah Integral (integral tak tentu dan tentu).")
