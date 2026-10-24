import re
import sympy as sp
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                        implicit_multiplication_application, convert_xor)

x = sp.symbols("x")
_LOCAL = {"x": x, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot,
          "sec": sp.sec, "csc": sp.csc, "exp": sp.exp, "ln": sp.log, "log": sp.log,
          "sqrt": sp.sqrt, "pi": sp.pi, "e": sp.E, "abs": sp.Abs}
_TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)


class InputError(ValueError):
    pass


def parse(text):
    s = (text or "").strip()
    if not s:
        raise InputError("Input tidak boleh kosong.")
    if len(s) > 100 or not re.fullmatch(r"[0-9a-zA-Z_+\-*/^().,\s]+", s):
        raise InputError("Input mengandung karakter yang tidak diizinkan.")
    for w in re.findall(r"[A-Za-z_]+", s):
        if w not in _LOCAL:
            raise InputError(f"Simbol '{w}' tidak dikenal. Gunakan x, sin, cos, tan, exp, ln, sqrt, pi.")
    try:
        return parse_expr(s, local_dict=_LOCAL, transformations=_TRANS)
    except Exception:
        raise InputError("Sintaks tidak valid. Contoh: 2*x**2 - 5*x + 4")


def antiderivative(f):
    F = sp.integrate(f, x)
    if F.has(sp.Integral):
        raise InputError("Integral ini tidak dapat diselesaikan secara simbolik.")
    return F


def indefinite(f):
    F = antiderivative(f)
    return F, sp.simplify(sp.diff(F, x) - f) == 0


def is_continuous(f, a, b):
    lo, hi = sorted([a, b], key=float)
    if lo == hi:
        return True
    try:
        for p in sp.singularities(f, x):
            if p.is_real is not False and bool(lo <= p) and bool(p <= hi):
                return False
    except Exception:
        pass
    try:
        itv = sp.Interval(lo, hi)
        return sp.continuous_domain(f, x, itv) == itv
    except Exception:
        return True


def definite(f, a, b):
    F = antiderivative(f)
    Fa, Fb = F.subs(x, a), F.subs(x, b)
    return F, sp.simplify(Fa), sp.simplify(Fb), sp.simplify(Fb - Fa)
