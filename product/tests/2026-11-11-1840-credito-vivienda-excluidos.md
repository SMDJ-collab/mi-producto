---
opportunity: credito-vivienda-excluidos
solutions: product/solutions/2026-11-11-1823-credito-vivienda-excluidos.md
status: designed
---

# Tests de solución para: Crédito de vivienda para quienes el banco excluye

## Por qué probar
Solo A3 (`puente-fsv`) está en prueba. Sobre el problema hay señales `synthetic` y `secondary`, ninguna `real` todavía (la encuesta sale el 2026-11-23). Sobre la solución no hay nada. Nadie ha confirmado que el FSV o el Ministerio financien una vivienda en contenedor, y nadie del segmento ha reaccionado a una oferta de acompañamiento. Primero va la elegibilidad (#8): si falla, A3 no existe. Después va el valor (#10).

## T1. puente-fsv: consulta de elegibilidad al FSV y al Ministerio
- **Test status:** ready
- **Belief under test:** "Un HomeTainer Hogareño instalado en terreno del cliente es elegible como vivienda financiable por el FSV o por el programa de construcción en lote propio del Ministerio." (#8)
- **Risk:** [feasibility]
- **Test type:** eligibility-consultation
- **What we do:** 1) Pedir por escrito (correo o carta, con una visita de seguimiento) una consulta formal a dos instancias: la línea de vivienda/construcción del FSV y la oficina del programa de construcción en lote propio del Ministerio de Vivienda. 2) Adjuntar la ficha técnica del HomeTainer Hogareño. 3) Hacer las mismas preguntas a las dos: ¿es elegible como garantía una vivienda en contenedor sobre lote del cliente? ¿Con qué condiciones? (normativa estructural y sísmica, cimentación, área mínima, permisos municipales u OPAMSS, avalúo, registro del constructor). ¿El lote tiene que estar a nombre del solicitante o puede ser familiar? ¿El desembolso va al constructor? ¿Qué institución, tasa y criterios de ingreso tiene el programa del Ministerio? 4) Si no responden en 10 días hábiles, consultar como respaldo a un perito valuador registrado ante el FSV.
- **With whom:** FSV y Ministerio de Vivienda (2 instancias), y como respaldo 1 perito valuador. Responsable: tech (quien lleve la construcción en Torogoz).
- **Material needed:** una ficha técnica de 1 página (dimensiones, estructura, aislamiento, cimentación, instalaciones, vida útil estimada, precio de referencia, 2 fotos reales), la lista de preguntas de arriba y una hoja de captura por instancia: respuesta sí/no/depende, cada condición con su juicio de tech "cumplible en ≤ 3 meses: sí/no", y si la respuesta fue por escrito o verbal. Se deja fuera a propósito: renders de marketing, propuestas de convenio y la mención del financiamiento propio de Torogoz.
- **Material:** product/tests/materials/t1-puente-fsv/ (ficha-tecnica.md, consulta.md, hoja-captura.md)
- **Duration:** 3 semanas, hasta el 2026-12-04.
- **Signal and threshold:** respuesta documentada (por escrito o con la norma publicada) de al menos 1 de las 2 instancias que confirme la elegibilidad, con condiciones que tech juzgue cumplibles en ≤ 3 meses. Una respuesta verbal o un "depende" sin condiciones concretas no cuenta. Si después de 3 semanas no hay respuesta documentada de ninguna instancia, el resultado es `inconclusive`.
- **Decision rule:** continue si al menos una instancia confirma la elegibilidad con condiciones cumplibles en ≤ 3 meses · change si solo es elegible con condiciones que tardan más de 3 meses pero alcanzan antes del 2027-05-08, o que cambian el producto (A3 sigue redefinida a esa línea o versión, y la nueva versión necesita su propio test) · discard si ambas dicen que no, o si las condiciones no se pueden cumplir antes del 2027-05-08 (se revisan A5, A1 y A2 según sus reglas de pausa).
- **Expected provenance:** real
- **Next step if it passes:** T2.

## T2. puente-fsv: concierge, oferta de acompañamiento con entrega de documentos
- **Test status:** designed
- **Belief under test:** "Al menos 1 de cada 4 de quienes califican entrega sus documentos a Torogoz para iniciar el trámite." (#10)
- **Risk:** [value]
- **Test type:** concierge
- **What we do:** Solo se corre si T1 pasa. 1) Reclutar entre quienes dejaron opt-in en la encuesta y probablemente califican al FSV: ingreso formal o independiente con comprobantes (Q1), acceso a terreno (Q6, opciones 1–2) y escrituras en orden (Q8). Si T1 dice que el lote tiene que estar a nombre del solicitante, aplicar ese filtro. 2) Conversación de 20–30 minutos (llamada o en persona) con la oferta concreta: Torogoz arma tu carpeta para el FSV o el Ministerio y te acompaña en el trámite; el HomeTainer es elegible según lo que respondió la institución en T1; no se promete aprobación. 3) Pedir un compromiso concreto: enviar por WhatsApp o en persona, en los 7 días siguientes, los documentos de la lista (DUI, comprobantes de ingreso, escritura del terreno) para hacer la precalificación. 4) Registrar quién entrega, qué entrega y qué objeción da quien no entrega.
- **With whom:** 12 personas reales del segmento (20–40 años, San Salvador o La Libertad, $800–1,700/mes, viven con su familia), reclutadas de los opt-in de la encuesta. Si hay suficientes, la mitad con terreno propio y la mitad con terreno familiar.
- **Material needed:** una oferta de 1 página apta para WhatsApp (qué hace Torogoz, qué no hace, qué dijo la institución en T1, fotos reales del HomeTainer, sin precios inventados ni promesa de aprobación), un guion de conversación con la petición de compromiso textual, una checklist de documentos con un aviso de uso y resguardo de datos, y una hoja de captura por participante (perfil Q1/Q6/Q8, fecha de la conversación, compromiso pedido sí/no, documentos entregados completos/parciales/ninguno, fecha de entrega, objeción literal). Se deja fuera a propósito: simulador de cuotas, página web, app, cualquier cobro y la venta del HomeTainer en sí.
- **Material:** —
- **Duration:** 2 semanas desde la primera conversación, una vez cerrada la encuesta y pasado T1.
- **Signal and threshold:** al menos 3 de 12 (≥ 25 %) entregan los documentos completos en 7 días. Decir "me interesa" o "lo voy a pensar" no cuenta. Con menos de 8 conversaciones completadas, el resultado es `inconclusive`.
- **Decision rule:** continue si ≥ 3 de 12 entregan los documentos completos · change si ≤ 2 entregan pero al menos 3 de quienes no entregan dan la misma objeción y es corregible (desconfianza, falta de un documento, el dueño del terreno es otro familiar); se prueba la versión ajustada · discard si ≤ 2 entregan y no se repite ninguna objeción corregible.
- **Expected provenance:** real
- **Next step if it passes:** presentar las carpetas recibidas a precalificación del FSV o del Ministerio. Eso prueba la #9 con casos reales. Si pasa, A3 queda lista para spec.

## Results
### T1 — ensayo (synthetic), 2026-11-11
- **Observado:** corrida simulada por el equipo; ninguna institución fue consultada. FSV simulado: "depende", con 4 condiciones (memoria de cálculo firmada, permisos y factibilidad de servicios, avalúo aceptado, titularidad del lote). Ministerio simulado: sin respuesta. Perito simulado: respuesta verbal, sin determinar elegibilidad.
- **Con quién y cuántos:** 0 instancias reales; 2 instancias y 1 perito simulados.
- **Provenance:** synthetic
- **Resultado del ensayo:** inconclusive (0 de 2 respuestas documentadas). No es el resultado de T1: la corrida real sigue pendiente.
- **Decisión:** ninguna sobre A3. Para la corrida real: conseguir la memoria de cálculo firmada antes de enviar, que la hoja exija sí/no a tech y hacer la visita al Ministerio a los 5–7 días hábiles.

### T2 — not run

## Decision
