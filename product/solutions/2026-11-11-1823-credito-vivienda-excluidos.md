---
opportunity: credito-vivienda-excluidos
status: chosen
chosen: puente-fsv
tests: product/tests/2026-11-11-1840-credito-vivienda-excluidos.md
---

# Soluciones para: Crédito de vivienda para quienes el banco excluye

## Lo que dice la evidencia hoy
- #2 [value] (≥ 1 de 3 excluidos) está parcialmente contradicha: el FSV presta al 4–5 % a 25 años a formales, independientes con comprobantes, informales con comprobantes y receptores de remesas (secondary, product/research/2026-11-08-1450-credito-vivienda-excluidos-mercado.md). La exclusión persiste para quien no documenta ingresos o tiene mal historial; su tamaño es desconocido.
- #6 (cuota $215–430) contradicha como benchmark: el programa del Ministerio para construir en lote propio financia $20k a ≈ $158/mes (secondary, mismo archivo).
- #3 y #7 (impago ≤ 8 % a ≤ 14 %) abiertas: no hay datos de mora para el núcleo excluido; tasa máxima legal y registro, desconocidos.
- No hay evidencia real todavía: la encuesta (product/surveys/2026-11-09-2140-credito-terreno-pago.md) sale el 2026-11-23.

## Línea base: lo que la gente hace hoy
Se queda con su familia y aporta a la casa (Karla ~$150/mes; Rosa paga la luz, $35), ahorra en cuenta programada o tanda ($80–120/mes) y, a lo sumo, consigue crédito informal pequeño y caro (Rosa: $1,500). Tras un primer rechazo bancario, deja de intentarlo (Karla). Fuente: synthetic (product/personas/, product/interviews/2026-11-09-2211-karla-mejia.md); en la práctica `assumption` hasta que la encuesta lo mida (Q2–Q5, Q9–Q11).

## Alternativas
### A1. Financiamiento directo de Torogoz (`financiamiento-directo`)
Torogoz presta, a ≤ 14 %, a quien el FSV y los bancos rechazan. Ataca la falta de prestamista. Para Rosa (secondary) y Kevin (primary). Reemplaza la espera. Idea que estaba en el brief.
### A2. Garantía familiar con el terreno (`garantia-terreno-familiar`)
El familiar dueño del terreno (José Mauricio, tertiary) respalda el crédito como codeudor o con hipoteca del terreno, ante el FSV, un banco o Torogoz. Ataca el riesgo que percibe el prestamista. Para Kevin y Diego (primary). Reemplaza el "no tengo codeudor". Idea que estaba en el brief.
### A3. Puente al FSV / programa del Ministerio (`puente-fsv`)
Torogoz no presta: acompaña al cliente a calificar al FSV o al crédito para construir en lote propio (comprobantes, carpeta, trámite) y logra que el HomeTainer sea elegible para esos créditos. Ataca la exclusión por información y por papeleo. Para Diego y Karla (primary); Rosa (secondary) solo si puede documentar su negocio; no sirve a Kevin. Reemplaza el "fui a dos bancos y lo dejé". No usa el capital de $100k.
### A4. Plan de aportes antes de la entrega (`aportes-previos`)
El cliente paga 6–12 meses de cuota antes de la entrega; si paga puntual, Torogoz financia el resto o ese historial le sirve de comprobante ante el FSV (Aporte y Crédito junta aportes de 3 a 18 meses). Ataca la falta de historial. Para Rosa y Kevin. Reemplaza la tanda sin destino.
### A5. Módulo inicial pequeño, ampliable (`modulo-incremental`)
Un primer módulo de $8–12k, pagable con ahorro más un crédito pequeño, que se amplía después. Baja el ticket en vez de financiar. Para Rosa. Reemplaza el "no me prestan $25k".

## Comparación
| Alternativa | Desirable | Feasible | Viable | Riskiest belief |
|---|---|---|---|---|
| A3 puente-fsv | mixed — pain evidenced, relief not tested (synthetic: entrevista Karla; secondary: research FSV) | strong — expediente concreto aceptado como garantía por el FSV, sin impedimento por tipo de construcción; avalúo total 117 % del precio (construcción sola 84 %) (product/tests/2026-11-11-1840-credito-vivienda-excluidos.md, T1b, (ejercicio académico, respuestas simuladas)) | mixed (assumption) — mueve ventas, libera capital; no mueve el outcome de "financiamiento propio" del brief | Un HomeTainer en terreno del cliente es financiable por el FSV o el programa del Ministerio |
| A1, A2, A4, A5 | no evaluadas (parked) | — | — | — |

## Decisión
El equipo eligió A3 para probarla (2026-11-11), sin evaluar las demás. La IA había recomendado mantener el set completo antes de evaluar; no había recomendado ninguna alternativa en particular. Advertencia registrada: si A3 gana, el outcome del brief ("viviendas vendidas con financiamiento propio", impago ≤ 8 %) tendrá que reformularse a ventas con crédito de terceros.

## A probar
- A3 — diseño de tests en product/tests/2026-11-11-1840-credito-vivienda-excluidos.md: T1 elegibilidad ante FSV/Ministerio (#8, [feasibility]); T2 concierge con entrega de documentos (#10, [value]), solo si T1 pasa. La #9 la cubren en parte la encuesta del 2026-11-23 (Q1, Q3–Q5) y el siguiente paso de T2.

## Propuesta de valor: puente-fsv (para Diego Ramírez, primary)
- Dolor que alivia: le negaron la hipoteca en dos bancos por no tener constancia de salario, aunque su ingreso califica (synthetic, persona). Hoy vive con los suegros, con tensiones de por medio.
- Ganancia: una vivienda en su propio terreno a tasa del FSV (4–5 %) o con cuota de ≈ $158–197/mes del programa del Ministerio, en vez de $55k y 10 meses de construcción tradicional.
- Reemplaza: ir de banco en banco y desistir; Torogoz arma la carpeta que el banco no le pidió bien y le presenta una vivienda que el FSV acepta.
- Deliberadamente no hace: no presta, no atiende a quien tiene mal historial crediticio (Kevin), no provee terreno, no promete aprobación.

## Creencias
- [opportunity: credito-vivienda-excluidos] [value] #2, tal como está registrada (referenciada)
- [product] [value] #1, terreno disponible (referenciada)
- [feature: puente-fsv] [feasibility] Un HomeTainer Hogareño instalado en terreno del cliente es elegible como vivienda financiable por el FSV o por el programa de construcción en lote propio del Ministerio. (#8)
- [feature: puente-fsv] [value] Al menos 1 de cada 3 personas del segmento con terreno disponible que no pidió crédito o lo dejó cumple los requisitos del FSV con acompañamiento. (#9)
- [feature: puente-fsv] [value] Al menos 1 de cada 4 de quienes califican entrega sus documentos a Torogoz para iniciar el trámite. (#10)
- [feature: puente-fsv] [viability] Torogoz puede vender un HomeTainer con crédito del FSV o del Ministerio, cobrando el desembolso como constructor, con margen positivo y sin usar su capital para prestar. (#11)

## Descartadas o en pausa
- A1 — parked: no evaluada. Vuelve si la encuesta muestra un núcleo sin comprobantes grande y la consulta legal confirma la tasa ≤ 14 %.
- A2 — parked: no evaluada. Vuelve si A3 se topa con el historial o la falta de codeudor; se puede combinar con A3.
- A4 — parked: no evaluada. Vuelve si el obstáculo resulta ser la falta de historial o de comprobantes; puede alimentar a A3 vía Aporte y Crédito.
- A5 — parked: no evaluada. Vuelve si la elegibilidad falla o la capacidad de pago (#6) resulta menor que la cuota del Ministerio.

## Resultado
- A3 `puente-fsv` — chosen, en change → T1b (elegibilidad con expediente concreto). Ver product/tests/2026-11-11-1840-credito-vivienda-excluidos.md (ejercicio académico, respuestas simuladas).
- A3 `puente-fsv` — T1b passed: continue → T2 (concierge). Ver product/tests/2026-11-11-1840-credito-vivienda-excluidos.md (ejercicio académico, respuestas simuladas).
