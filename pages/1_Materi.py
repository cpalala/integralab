import streamlit as st
from modules import ui
from data.rumus import RUMUS

ui.hero("Materi Integral", "Konsep, rumus, teorema, dan sifat integral dalam satu tempat.")
t1, t2, t3 = st.tabs(["Dasar", "Rumus integral", "Integral tentu"])

with t1:
    st.markdown("Jika $f(x)$ adalah turunan dari $F(x)$, maka $f(x)$ juga turunan dari $F(x)+C$.")
    st.latex(r"\frac{d}{dx}\bigl(F(x)+C\bigr) = f(x) \;\Rightarrow\; \int f(x)\,dx = F(x) + C")
    st.markdown("**Istilah dan notasi**")
    st.markdown("- Integrasi ini disebut **integral tak tentu**, dan $C$ adalah **konstanta integrasi**\n"
                "- $f(x)\\,dx$ disebut **elemen integrasi**\n- $f(x)$ adalah **integran**\n"
                "- $dx$ adalah **diferensial** dari $x$")
    st.info("Integral adalah kebalikan dari turunan, sehingga rumus integral disusun dari rumus turunan.")

with t2:
    h = st.columns([1, 3, 3])
    h[0].markdown("**Aturan**"); h[1].markdown("**Turunan**"); h[2].markdown("**Integral**")
    for nama, tur, integ in RUMUS:
        r = st.columns([1, 3, 3])
        r[0].write(nama)
        if tur:
            r[1].latex(tur)
        r[2].latex(integ)

with t3:
    st.markdown("**Definisi (jumlah Riemann)**: jika $f$ kontinu pada $[a,b]$ dan limitnya ada,")
    st.latex(r"\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n} f(x_i)\,\Delta x_i")
    st.markdown("**Teorema A** (Teorema Dasar Kalkulus): jika $f$ kontinu pada $[a,b]$ dan $F$ antiturunan $f$,")
    st.latex(r"\int_a^b f(x)\,dx = F(b) - F(a)")
    st.markdown("**Teorema B** (sifat linear), dengan $k$ konstanta:")
    st.latex(r"\int_a^b k f(x)\,dx = k\int_a^b f(x)\,dx")
    st.latex(r"\int_a^b [f(x)\pm g(x)]\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx")
    st.markdown("**Sifat-sifat integral tentu**")
    st.latex(r"1.\ \int_a^a f(x)\,dx = 0")
    st.latex(r"2.\ \int_a^b f(x)\,dx = -\int_b^a f(x)\,dx")
    st.latex(r"3.\ \int_a^c f(x)\,dx + \int_c^b f(x)\,dx = \int_a^b f(x)\,dx,\ a<c<b")
    st.markdown("4. Jika $f(x)\\ge 0$ pada $[a,b]$, maka $\\int_a^b f(x)\\,dx \\ge 0$\n"
                "5. Jika $f(x)\\le 0$ pada $[a,b]$, maka $\\int_a^b f(x)\\,dx \\le 0$\n"
                "6. Jika $f(x) < g(x)$ pada $[a,b]$, maka $\\int_a^b f(x)\\,dx \\le \\int_a^b g(x)\\,dx$")
    st.markdown("**Metode substitusi**: jika $g$ punya turunan pada $[a,b]$ dan $f$ kontinu pada daerah hasil $g$,")
    st.latex(r"\int_a^b f(g(x))\,g'(x)\,dx = F(g(b)) - F(g(a))")
