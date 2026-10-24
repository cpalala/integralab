import sympy as sp
from .solver import x

U = sp.Symbol("u")
L = sp.latex


def _sub(f):
    cands = []
    for e in sp.preorder_traversal(f):
        if e.is_Pow and e.base.has(x) and e.base != x:
            cands.append(e.base)
        elif isinstance(e, sp.Function) and e.args[0].has(x) and e.args[0] != x:
            cands.append(e.args[0])
    for c in sorted(set(cands), key=sp.count_ops, reverse=True):
        d = sp.diff(c, x)
        if d == 0:
            continue
        raw = f / d
        for g in (raw, sp.simplify(raw), sp.factor(raw)):
            gu = g.subs(c, U)
            if not gu.has(x):
                return c, gu
    return None


def _term_steps(t):
    c, r = t.as_coeff_Mul()
    if r == 1:
        return [("Integral konstanta", rf"\int {L(t)}\,dx = {L(t * x)}")]
    n = None
    if r == x:
        n = sp.Integer(1)
    elif r.is_Pow and r.base == x and not r.exp.has(x):
        n = r.exp
    if n is not None:
        coef = "" if c == 1 else rf"{L(c)}\cdot "
        if n == -1:
            return [("Aturan 1/u (logaritma)", rf"\int {L(t)}\,dx = {coef}\ln|x|")]
        m = n + 1
        return [(f"Aturan pangkat dengan n = {n}",
                 rf"\int {L(t)}\,dx = {coef}\frac{{x^{{{L(m)}}}}}{{{L(m)}}} = {L(sp.integrate(t, x))}")]
    s = _sub(t)
    if s:
        cu, gu = s
        G = sp.integrate(gu, U)
        return [("Substitusi: misalkan u, lalu turunkan", rf"u = {L(cu)},\quad du = {L(sp.diff(cu, x))}\,dx"),
                ("Ubah integral ke bentuk u", rf"\int {L(gu)}\,du"),
                ("Integralkan terhadap u", rf"{L(G)} + C"),
                ("Kembalikan u ke x", rf"{L(G.subs(U, cu))} + C")]
    return [("Gunakan rumus tabel", rf"\int {L(t)}\,dx = {L(sp.integrate(t, x))}")]


def langkah(f):
    f = sp.sympify(f)
    out = [("Integral yang dihitung", rf"\int {L(f)}\,dx")]
    if f.is_Add:
        terms = sp.Add.make_args(f)
        parts = []
        for i, t in enumerate(terms):
            neg = t.could_extract_minus_sign()
            body = rf"\int {L(-t if neg else t)}\,dx"
            parts.append(("- " if neg else ("" if i == 0 else "+ ")) + body)
        out.append(("Aturan jumlah: integralkan suku demi suku", " ".join(parts)))
        for t in terms:
            out.append((f"Suku ${L(t)}$", rf"\int {L(t)}\,dx"))
            out.extend(_term_steps(t))
    else:
        out.extend(_term_steps(f))
    out.append(("Gabungkan hasil dan tambahkan konstanta C", rf"{L(sp.integrate(f, x))} + C"))
    return out
