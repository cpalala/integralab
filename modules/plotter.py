import numpy as np
import plotly.graph_objects as go
import sympy as sp
from .solver import x


def _ys(f, xs):
    fn = sp.lambdify(x, f, "numpy")
    with np.errstate(all="ignore"):
        ys = np.broadcast_to(np.asarray(fn(xs), dtype=float), xs.shape).copy()
    ys[np.abs(ys) > 1e6] = np.nan
    return ys


def _layout(fig, title):
    fig.update_layout(template="plotly_white", title=title, height=420, margin=dict(l=10, r=10, t=50, b=10),
                      xaxis_title="x", yaxis_title="f(x)", legend=dict(orientation="h"))
    return fig


def area_plot(f, a, b):
    lo, hi = sorted([float(a), float(b)])
    m = (hi - lo) * 0.3 or 1.0
    xs = np.linspace(lo - m, hi + m, 600)
    xa = np.linspace(lo, hi, 300)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xa, y=_ys(f, xa), fill="tozeroy", mode="lines",
                             name="Luas daerah", line=dict(color="#0F6E56")))
    fig.add_trace(go.Scatter(x=xs, y=_ys(f, xs), mode="lines", name="f(x)",
                             line=dict(color="#534AB7", width=2)))
    return _layout(fig, "Grafik f(x) dan daerah antara a dan b")


def riemann(f, a, b, n, mode):
    lo, hi = sorted([float(a), float(b)])
    dx = (hi - lo) / n
    left = lo + dx * np.arange(n)
    shift = {"Kiri": 0.0, "Tengah": dx / 2, "Kanan": dx}[mode]
    h = _ys(f, left + shift)
    approx = float(np.nansum(h) * dx)
    xs = np.linspace(lo, hi, 600)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=left, y=h, width=dx, offset=0, name="Persegi panjang",
                         marker=dict(color="rgba(15,110,86,0.35)", line=dict(color="#0F6E56", width=1))))
    fig.add_trace(go.Scatter(x=xs, y=_ys(f, xs), mode="lines", name="f(x)",
                             line=dict(color="#534AB7", width=2)))
    return _layout(fig, f"Jumlah Riemann ({mode.lower()}), n = {n}"), approx
