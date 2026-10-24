# Tabel rumus: (nama, turunan, integral). Edit di sini untuk menambah rumus.
RUMUS = [
    ("Konstanta", "", r"\int c\,du = cu + C"),
    ("Jumlah", "", r"\int (du + dv) = u + v + C"),
    ("Pangkat", "", r"\int u^n\,du = \frac{u^{n+1}}{n+1} + C,\; n \neq -1"),
    ("sin u", r"d(\sin u) = \cos u\,du", r"\int \cos u\,du = \sin u + C"),
    ("cos u", r"d(\cos u) = -\sin u\,du", r"\int \sin u\,du = -\cos u + C"),
    ("e^u", r"d(e^u) = e^u\,du", r"\int e^u\,du = e^u + C"),
    ("ln u", r"d(\ln u) = \frac{1}{u}\,du", r"\int \frac{1}{u}\,du = \ln|u| + C"),
    ("tan u", r"d(\tan u) = \sec^2 u\,du", r"\int \sec^2 u\,du = \tan u + C"),
    ("cot u", r"d(\cot u) = -\csc^2 u\,du", r"\int \csc^2 u\,du = -\cot u + C"),
    ("sec u", r"d(\sec u) = \sec u \tan u\,du", r"\int \sec u \tan u\,du = \sec u + C"),
    ("csc u", r"d(\csc u) = -\csc u \cot u\,du", r"\int \csc u \cot u\,du = -\csc u + C"),
]
