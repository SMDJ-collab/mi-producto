# Conteo de temas del feedback simulado de puente-fsv, Nivel 1.
# Corpus: product/data/2026-11-11-1952-feedback-simulado-puente-fsv.md (source: synthetic)
import re, sys, collections
path = sys.argv[1]
rows = {}
for line in open(path, encoding="utf-8"):
    m = re.match(r"^\| (\d+) \| (\S+) \| (\S+) \|", line)
    if m:
        rows[int(m.group(1))] = (m.group(2), m.group(3))
OUT = {14, 21, 32}
THEMES = {
    "F1 Claridad de precalificación y cotización": [4, 5, 11, 15, 23, 26, 29, 33],
    "F2 Creen que Torogoz presta": [1, 9, 12, 28],
    "F3 Desconfianza antes de entregar documentos": [3, 13, 19, 25],
    "F4 Fuera por lote a nombre de un familiar": [2, 16, 17],
    "F5 Dudas sobre la durabilidad del contenedor": [6, 18, 31],
    "F6 Fuera por historial o falta de comprobantes": [10, 30],
    "F7 Formulario difícil; piden audio o visita": [7, 22],
    "Señales débiles": [8, 27, 20, 24, 34],
}
tagged = [i for ids in THEMES.values() for i in ids]
assert len(tagged) == len(set(tagged)), "entrada en dos temas"
inscope = set(rows) - OUT
assert set(tagged) == inscope, (set(tagged) ^ inscope)
n = len(inscope)
print(f"total={len(rows)} fuera={len(OUT)} dentro={n}")
src = collections.Counter(rows[i][1] for i in rows)
print("por fuente:", dict(src))
for t, ids in THEMES.items():
    s = collections.Counter(rows[i][1] for i in ids)
    w1 = sum(1 for i in ids if rows[i][0] <= "2026-12-13")
    w2 = len(ids) - w1
    print(f"{t}: n={len(ids)} ({100*len(ids)/n:.0f}%) fuentes={dict(s)} sem1={w1} sem2={w2}")
