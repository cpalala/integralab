import streamlit as st
from modules import ui
import sympy as sp
from modules.solver import parse, definite, is_continuous, InputError, x
from modules.plotter import area_plot, riemann

ui.hero("Integral Tentu", "Hitung luas daerah, lihat grafiknya, dan jelajahi jumlah Riemann.")
st.caption("Batas a dan b boleh berupa bilangan, pi, atau sqrt. Contoh: 0, 2, pi/2.")

c1, c2, c3 = st.columns([3, 1, 1])
teks = c1.text_input("f(x) =", "x**2")
a_txt = c2.text_input("Batas bawah a", "0")
b_txt = c3.text_input("Batas atas b", "2")

try:
    f, a, b = parse(teks), parse(a_txt), parse(b_txt)
    if a.has(x) or b.has(x):
        raise InputError("Batas a dan b harus berupa bilangan, bukan variabel x.")
    if not is_continuous(f, a, b):
        raise InputError("f(x) tidak kontinu pada [a, b], sehingga Teorema A tidak dapat dipakai.")
    F, Fa, Fb, exact = definite(f, a, b)
except InputError as e:
    st.error(str(e)); st.stop()
except Exception:
    st.error("Terjadi kesalahan saat menghitung. Periksa kembali input Anda."); st.stop()

tab1, tab2 = st.tabs(["Hitung dan grafik", "Simulasi Riemann"])

with tab1:
    st.subheader("Hasil")
    st.latex(rf"\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} {sp.latex(f)}\,dx = {sp.latex(exact)} \approx {float(exact):.6g}")
    st.subheader("Langkah penyelesaian")
    st.markdown("**1. Cari antiturunan** $F(x)$")
    st.latex(rf"F(x) = {sp.latex(F)}")
    st.markdown("**2. Terapkan Teorema A:** $F(b) - F(a)$")
    st.latex(rf"\left[{sp.latex(F)}\right]_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} = {sp.latex(Fb)} - \left({sp.latex(Fa)}\right) = {sp.latex(exact)}")
    if a == b:
        st.info("Sifat 1: batas atas dan bawah sama, sehingga hasilnya 0.")
    elif float(a) > float(b):
        st.info("Sifat 2: karena a > b, nilai integral sama dengan negatif integral dari b ke a.")
    st.plotly_chart(area_plot(f, a, b), use_container_width=True)

with tab2:
    if float(a) >= float(b):
        st.info("Simulasi Riemann memerlukan a < b.")
    else:
        st.markdown("Semakin besar $n$, jumlah Riemann semakin mendekati nilai integral sebenarnya.")
        n = st.slider("Jumlah subinterval (n)", 1, 200, 10)
        mode = st.radio("Titik sampel", ["Kiri", "Tengah", "Kanan"], horizontal=True)
        fig, approx = riemann(f, a, b, n, mode)
        st.plotly_chart(fig, use_container_width=True)
        m = st.columns(3)
        m[0].metric("Pendekatan Riemann", f"{approx:.6g}")
        m[1].metric("Nilai eksak", f"{float(exact):.6g}")
        m[2].metric("Selisih", f"{abs(approx - float(exact)):.3g}")
