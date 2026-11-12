---
source: synthetic
corpus: product/data/2026-11-11-1952-feedback-simulado-puente-fsv.md
metrics-analysis: none
period: 2026-12-07 to 2026-12-20
---

# Análisis de feedback: puente-fsv, Nivel 1 (oferta escrita y precalificación)

> **EJERCICIO ACADÉMICO — COMENTARIOS SIMULADOS.** El corpus lo generó Claude; este análisis es un ensayo del método, no evidencia sobre el segmento. No anota ninguna creencia en product/overview.md.

## Corpus
34 entradas, del 2026-12-07 al 2026-12-20: WhatsApp 13, CSAT 9, Facebook 5, notas de asesores 4, Google 3. Ninguna fuente pasa de la mitad. Fuera de alcance: 3 (id 14, contenedor para un cafetín, segmento Empresas; id 21, pregunta de empleo; id 32, "más info" sin contenido). Dentro del alcance: 31.

Sesgos: WhatsApp sobrerrepresenta a quien tiene interés o una duda concreta; el CSAT, solo a quien completó la precalificación y escribió; Facebook, desconfianza y preguntas públicas, a menudo de gente fuera del segmento; Google, los extremos; las notas, lo que el asesor juzgó repetido. Quien recibió la oferta y no hizo nada no aparece en ninguna fuente: solo lo muestran las métricas.

Sin análisis de métricas del Nivel 1: el análisis va solo, sin hipótesis que contrastar. Con dos semanas y pocas entradas por tema, la tendencia es `n/a`; se da el conteo por semana (sem. 1: 07–13 dic; sem. 2: 14–20 dic). Algunas personas aparecen más de una vez; cada tema dice cuántas personas distintas hay detrás.

Conteo: script product/insights/2026-11-11-1954-feedback-puente-fsv.py sobre el corpus.

## Temas

### F1. La precalificación y la cotización se entienden y sirven
- **Entradas:** 8 (26 %), 6 personas distintas · **Fuentes:** CSAT 5, WhatsApp 1, Google 1, Facebook 1 · **Resultado de precalificación:** "probablemente califica" y "probablemente no"
- **Parte de la feature:** precalificación (requisitos por tipo de ingreso), PDF de cotización, explicar lo que Torogoz no hace
- **Tipo:** `praise`
- **Severidad:** — (elogio; frecuencia alta)
- **Tendencia:** `n/a` (sem. 1: 4 · sem. 2: 4)
- > "Por fin alguien me dice clarito qué papeles necesito como independiente. En el banco nunca me explicaron" (id 5, CSAT 5)
- > "Al menos me dijeron claro que con mi historial no aplica, sin hacerme perder tiempo" (id 26, CSAT 4)

### F2. Creen que Torogoz es quien presta
- **Entradas:** 4 (13 %), 3 personas distintas + 1 nota de asesor que reporta 3 casos en una semana · **Fuentes:** WhatsApp 1, CSAT 1, Facebook 1, nota de asesor 1
- **Parte de la feature:** oferta, primer mensaje: qué hace Torogoz y qué no
- **Tipo:** `usability`
- **Severidad:** alta — frecuencia media; intensidad alta: quien no lo entiende no cumple el umbral de activation y, si llega al Nivel 2, respondería a otra oferta. Uno descubre el malentendido después de precalificar y se va (CSAT 2).
- **Tendencia:** `n/a` (sem. 1: 3 · sem. 2: 1)
- > "Pensé que ustedes daban el crédito. Si es con el FSV mejor voy yo directo" (id 12, CSAT 2)
- > "Tercera persona esta semana que pregunta si Torogoz es el que presta. Hay que revisar el primer párrafo del mensaje." (id 9, nota de asesor)

### F3. Desconfianza antes de entregar documentos
- **Entradas:** 4 (13 %), 3 personas distintas + 1 nota de asesor sobre "varias personas" · **Fuentes:** Facebook 1, WhatsApp 1, CSAT 1, nota de asesor 1
- **Parte de la feature:** paso de la precalificación a la entrega de documentos; prueba de que el HomeTainer existe
- **Tipo:** `request` (ver una casa terminada) y `complaint` (miedo a estafa, a mandar el DUI por WhatsApp)
- **Severidad:** alta — frecuencia media; intensidad alta: frena exactamente la conducta que mide la hipótesis (entregar documentos en 7 días). No hay casa muestra.
- **Tendencia:** `n/a` (sem. 1: 3 · sem. 2: 1)
- > "Está bien la precalificación pero me da miedo mandar mi DUI y la escritura por WhatsApp" (id 19, CSAT 3)
- > "Tienen alguna casa ya hecha que se pueda ir a ver? Quiero ver una antes de mandar mis documentos" (id 13, WhatsApp)

### F4. Quedan fuera por tener el lote a nombre de un familiar
- **Entradas:** 3 (10 %), 1 persona (2 mensajes) + 1 nota de asesor que reporta 2 casos · **Fuentes:** WhatsApp 2, nota de asesor 1
- **Parte de la feature:** elegibilidad (lote a nombre del solicitante)
- **Tipo:** `request`
- **Severidad:** media — frecuencia baja; intensidad alta para quien queda fuera. La exclusión es deliberada en el spec (segmento probado en T1b), pero piden lo mismo: que el familiar sea codeudor o hipoteque el terreno.
- **Tendencia:** `n/a` (sem. 1: 3 · sem. 2: 0)
- > "Entonces si el terreno no está a mi nombre no puedo? mi papá no quiere pasarlo todavía" (id 16, WhatsApp)
- > "Ambas preguntaron si el papá podía ser codeudor o hipotecar el terreno." (id 17, nota de asesor)

### F5. Dudas sobre la durabilidad del contenedor
- **Entradas:** 3 (10 %), 3 personas distintas · **Fuentes:** Facebook 1, WhatsApp 1, Google 1
- **Parte de la feature:** el producto presentado en la oferta (calor, óxido, vida útil)
- **Tipo:** `complaint` (objeción)
- **Severidad:** media — frecuencia baja; intensidad media: ninguno dice que lo frena, pero queda como duda abierta. La oferta no responde estas preguntas.
- **Tendencia:** `n/a` (sem. 1: 2 · sem. 2: 1)
- > "Y eso del óxido? por la playa los contenedores se arruinan rápido" (id 18, WhatsApp)

### F6. Fuera por historial crediticio o por no tener comprobantes
- **Entradas:** 2 (6 %), 2 personas distintas · **Fuentes:** WhatsApp 2
- **Parte de la feature:** elegibilidad (perfil de ingreso e historial)
- **Tipo:** `request`
- **Severidad:** baja — frecuencia baja; intensidad alta para ellos, pero es una exclusión deliberada del spec ("no atiende a quien tiene mal historial").
- **Tendencia:** `n/a` (sem. 1: 1 · sem. 2: 1)
- > "Ya me dijeron que como vendo en el mercado sin papeles no califico, pero ¿no hay otra forma? yo sí puedo pagar" (id 30, WhatsApp, audio transcrito)

### F7. El formulario cuesta; piden audio o visita
- **Entradas:** 2 (6 %), 2 personas distintas · **Fuentes:** WhatsApp 1, CSAT 1
- **Parte de la feature:** precalificación (formato y canal)
- **Tipo:** `usability`
- **Severidad:** media-baja — frecuencia baja; intensidad media: uno terminó en "falta información".
- **Tendencia:** `n/a` (sem. 1: 2 · sem. 2: 0)
- > "Las preguntas eran muchas y no sabía qué responder en lo de antigüedad del negocio" (id 22, CSAT 3)

## Contra las hipótesis de métricas
No hay análisis de métricas del Nivel 1. Cuando exista, F2 habla de la condición de freno "la mayoría cree que Torogoz presta" y del umbral de activation; F3, de la intención antes del Nivel 2 (retention).

## Señales débiles
- **La cuota no es exacta** (ids 8 y 27, la misma persona): pide la cuota exacta con 5 % a 25 años "para ver si me alcanza". Se excluyó de los temas porque es una sola persona.
- **"Para eso no necesito intermediario"** (id 20, Google 1): entiende la oferta y no le ve valor. Es la objeción opuesta a F2.
- **Ayuda con el impuesto municipal atrasado** para tener la escritura en orden (id 34, nota de asesor).
- **Pide el siguiente paso** tras consultarlo con su esposa (id 24): es una señal de retention, no un tema de feedback.
