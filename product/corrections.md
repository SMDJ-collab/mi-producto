# Correcciones humanas a propuestas de la IA

Registro de decisiones en las que el equipo cambió lo que la IA propuso. Cada entrada: fecha, artefacto, qué propuso la IA, qué se decidió y por qué.

## 2026-11-08 — Mezcla de personas (`/generate-personas`)

- **Artefacto:** `product/personas/`
- **Propuesta de la IA:** 4 personas: 2 `primary`, 1 `tertiary` (padre o madre dueño del terreno) y 1 `negative`, sin `secondary`.
- **Decisión:** 5 personas: 2 `primary`, 1 `secondary`, 1 `tertiary` y 1 `negative`. Se agregó Rosa Elena Flores (`secondary`).
- **Por qué:** el segmento Hogareño no es homogéneo. Hay quien quiere la vivienda solo para vivir y quien la necesita también para generar ingreso. Sin una secundaria, el set quedaba entero en asalariados o profesionales. Después del research, Rosa resultó ser la persona más cercana al núcleo que el FSV seguiría excluyendo.

## 2026-11-08 — Creencia de viabilidad de la oportunidad (`/frame-opportunity`)

- **Artefacto:** `product/opportunities/2026-11-08-1442-credito-vivienda-excluidos.md` y `product/overview.md`
- **Propuesta de la IA:** cubrir la viabilidad de la oportunidad citando la creencia `[product] [viability]` sobre financiar "al segmento" en general (hoy #7), sin formular una creencia propia de la oportunidad.
- **Decisión:** formular y registrar `[opportunity: credito-vivienda-excluidos] [viability]` como #3: financiar con $100k a quienes el FSV rechaza, a ≤ 14 % y dentro de la tasa máxima legal, con impago ≤ 8 %.
- **Por qué:** el research mostró que el FSV presta al 4–5 % a informales con comprobantes y a quienes reciben remesas, y contra eso Torogoz no compite. La viabilidad que importa es la del núcleo excluido, con el capital que existe de verdad, no la del segmento en general.

## 2026-11-08 — Capital y fecha de decisión (`/frame-opportunity`)

- **Artefacto:** `product/opportunities/2026-11-08-1442-credito-vivienda-excluidos.md` (Constraints)
- **Propuesta de la IA:** dejar el capital disponible y la fecha de decisión como "no sé", para convertirlos en hallazgos de la agenda.
- **Decisión:** capital de $100k para financiar; decisión sobre el segmento Hogareño en 6 meses (2027-05-08), cuando se puede abrir otro segmento.
- **Por qué:** son datos del negocio que solo el equipo tiene. Cambian la viabilidad: con $100k Torogoz solo puede financiar entre 3 y 5 viviendas antes de agotar el capital.

## 2026-11-11 — Decisión sobre T1 de puente-fsv (`/analyze-solution-tests`) (ejercicio académico, respuestas simuladas)

- **Artefacto:** `product/tests/2026-11-11-1840-credito-vivienda-excluidos.md`
- **Propuesta de la IA:** la regla de decisión de T1 esperaba confirmación o rechazo del producto; no contemplaba una respuesta "depende de cada expediente". Con 0 de 2 confirmaciones y ningún rechazo, la IA propuso `change` hacia T1b (elegibilidad con un expediente concreto) como interpretación, no como aplicación directa de la regla.
- **Decisión:** `change` → T1b.
- **Por qué:** ninguna institución descarta el contenedor por el material; las condiciones son las de cualquier expediente. Descartar A3 sin probar un caso concreto sería prematuro. Pendiente: corregir la regla de T1 en `/design-solution-tests` para cubrir respuestas "caso por caso".
