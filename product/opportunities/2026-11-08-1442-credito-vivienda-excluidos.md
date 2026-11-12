---
status: framed
segment: Personas de 20–40 años en San Salvador y La Libertad, con ingresos de $800–1,700/mes que el sistema bancario no acepta (formales bajos, independientes variables o informales en efectivo), que quieren independizarse de su familia de origen
personas: rosa-elena-flores, kevin-alvarado, karla-mejia, diego-ramirez, jose-mauricio-hernandez, andrea-castillo
---

# Opportunity: Crédito de vivienda para quienes el banco excluye

Personas de 20–40 años con ingresos de $800–1,700 que podrían pagar una cuota mensual siguen viviendo con su familia porque ninguna institución les presta para una vivienda; el costo es postergar la vida en pareja y los hijos, tensiones de convivencia y aportar a un hogar sin construir patrimonio. Por qué ahora: HomeTainer Torogoz arranca su descubrimiento por el segmento Hogareño y tiene 6 meses antes de abrir el siguiente.

## Segment and personas
- Karla Beatriz Mejía (primary) — suffers it: salario formal de ~$950, le piden codeudor o el doble de ingreso
- Diego Alejandro Ramírez (primary) — suffers it: ingreso de independiente sin constancia de salario
- Rosa Elena Flores (secondary) — suffers it: ingreso informal en efectivo, sin comprobantes
- José Mauricio Hernández (tertiary) — does not suffer it; puede aparecer como codeudor o como garantía vía terreno
- Andrea Sofía Castillo (negative) — does not suffer it; su barrera es precio, ubicación y falta de terreno, no la exclusión crediticia
- Missing: persona cuyo ingreso depende en parte de remesas (frecuente en El Salvador; los bancos suelen no computarlo) → `/generate-personas`

## Signals
| Signal | Provenance | Source |
|---|---|---|
| Los bancos exigen ingresos altos para prestar al segmento | unverified | product/overview.md |
| Casa desde $120k, apartamento desde $140k | unverified | product/overview.md (sin fuente) |
| Enfermera con salario formal de ~$950: le piden codeudor o el doble de ingreso | synthetic | product/personas/karla-mejia.md |
| Independiente con $1,300–1,700: hipoteca negada por falta de constancia de salario | synthetic | product/personas/diego-ramirez.md |
| Comerciante informal: ninguna institución le presta más de $1,500 | synthetic | product/personas/rosa-elena-flores.md |

## Business outcome
Commercial. Ingresos por venta de HomeTainers Hogareños financiados por Torogoz, con cartera sana. Se miden juntos:
- Número de viviendas vendidas con financiamiento propio al segmento excluido por la banca.
- Impago anual ≤ 8 % con tasa al cliente ≤ 14 % anual.

## Constraints
- Geografía: San Salvador y La Libertad.
- Capital disponible para financiar: $100k → entre 3 y 5 viviendas de $20–30k antes de agotarlo.
- Fecha: decisión sobre el segmento Hogareño en 6 meses (2027-05-08), cuando se puede abrir un nuevo segmento.
- Regulación: la Ley contra la Usura fija tasas máximas, y la regulación aplicable depende de quién otorga el crédito — pendiente de verificar contra la tasa ≤ 14 %.

## Beliefs
Registradas en product/overview.md:
- [opportunity: credito-vivienda-excluidos] [value] De las personas del segmento que quieren independizarse, al menos 1 de cada 3 ha sido rechazada por un banco o una cooperativa para un crédito de vivienda, o no lo solicitó porque daba por hecho que no calificaría. (#2)
- [opportunity: credito-vivienda-excluidos] [viability] Torogoz puede financiar, con su capital de $100k, a personas del segmento que el FSV rechaza, a una tasa igual o menor al 14 % anual que además esté dentro de la tasa máxima legal, con un impago anual igual o menor al 8 %, de modo que la cartera recupere el capital para volver a prestar. (#3)
- [product] [viability] El segmento puede y está dispuesto a pagar una cuota mensual de unos $215–430 durante 10–15 años para financiar una vivienda de $20k–30k. (#6)
- [product] [viability] Torogoz puede financiar al segmento con un impago anual igual o menor al 8 %, y aun así cubrir su costo de capital con una tasa al cliente igual o menor al 14 % anual. (#7)

## Research agenda
| Belief | Instrument | Decision it unlocks | By when |
|---|---|---|---|
| #2 [value] Exclusión crediticia ≥ 1 de 3 | `/research-market`: requisitos de bancos, cooperativas y FSV; datos de acceso a crédito de vivienda por ingreso | Si la b sigue siendo el problema a atacar o se reformula hacia precio (a) o terreno (c) | 2026-11-30 |
| #2 [value] Exclusión crediticia ≥ 1 de 3 | `/design-survey` al segmento, con bloque de opt-in para entrevistas | Confirmar o descartar la oportunidad con datos propios | 2027-01-15 |
| #6 Capacidad y disposición de pago | Misma encuesta (ingreso, gastos, cuota máxima aceptable) + `/design-interview` con opt-ins | Rango de precio y plazo viable del financiamiento | 2027-02-15 |
| #7 Impago ≤ 8 % con tasa ≤ 14 % | `/research-market`: tasas de impago en microcrédito y crédito de vivienda de bajo ingreso en El Salvador; tasas máximas vigentes | Si Torogoz financia directamente o necesita un aliado | 2026-12-15 |
| #3 [viability] + restricción regulatoria | Consulta legal o secundaria: quién puede otorgar crédito y con qué tasa máxima | Si el financiamiento propio es legalmente viable tal como está planteado | 2026-12-15 |

## Candidate ideas (not evaluated)
- HomeTainer Hogareño de $20–30k financiado directamente por Torogoz (del overview) → `parked` (A1, `financiamiento-directo`) — product/solutions/2026-11-11-1823-credito-vivienda-excluidos.md
- Usar al familiar dueño del terreno como codeudor, o el terreno como garantía (surgió al revisar a José Mauricio) → `parked` (A2, `garantia-terreno-familiar`) — product/solutions/2026-11-11-1823-credito-vivienda-excluidos.md
