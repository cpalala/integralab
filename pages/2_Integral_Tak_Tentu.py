import streamlit as st
from modules import ui
import sympy as sp
from modules.solver import parse, indefinite, InputError, x
from modules.steps import langkah

ui.hero("Integral Tak Tentu", "Hitung antiturunan lengkap dengan langkah penyelesaian.")
st.caption("Gunakan ** atau ^ untuk pangkat. Contoh: 2*x**2 - 5*x + 4. Fungsi: sin, cos, tan, exp, ln, sqrt.")

CONTOH = {"Contoh 1": "2*x**2 - 5*x + 4", "Contoh 2": "sqrt(x) - 2/x**3",
          "Contoh 3": "4*x*(2*x**2 - 4)**2", "Trigonometri": "3*sin(x) + cos(x)", "Eksponen dan ln": "exp(x) + 1/x"}
pilih = st.selectbox("Pilih contoh dari materi (opsional)", ["(ketik sendiri)"] + list(CONTOH))
teks = st.text_input("f(x) =", value=CONTOH.get(pilih, "x**2"), key=f"f_{pilih}")

if st.button("Hitung integral", type="primary"):
    try:
        f = parse(teks)
        F, ok = indefinite(f)
        daftar = langkah(f)
    except InputError as e:
        st.error(str(e)); st.stop()
    except Exception:
        st.error("Terjadi kesalahan saat menghitung. Periksa kembali input Anda."); st.stop()
    st.subheader("Hasil")
    st.latex(rf"\int {sp.latex(f)}\,dx = {sp.latex(F)} + C")
    st.subheader("Langkah penyelesaian")
    for i, (judul, rumus) in enumerate(daftar, 1):
        st.markdown(f"**{i}. {judul}**")
        st.latex(rumus)
    st.subheader("Pengecekan")
    st.latex(rf"\frac{{d}}{{dx}}\left({sp.latex(F)}\right) = {sp.latex(sp.simplify(sp.diff(F, x)))}")
    if ok:
        st.success("Turunan hasil sama dengan f(x).")
    else:
        st.warning("Periksa kembali hasilnya.")
