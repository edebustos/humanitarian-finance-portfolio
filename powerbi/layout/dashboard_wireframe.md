# Wireframe del Dashboard

Titulo del dashboard: **Humanitarian Finance & Operations Dashboard**

Direccion visual: sobria, limpia, ejecutiva y humanitaria. Usa un lienzo blanco o gris muy claro, texto en gris oscuro, separadores grises suaves y acentos rojos inspirados en Cruz Roja. Evita degradados llamativos, visuales de marketing y apariencia de startup.

Paleta sugerida:

- Rojo de acento: `#D71920`
- Texto principal: `#222222`
- Texto secundario: `#5F6368`
- Fondo claro: `#F7F7F7`
- Fondo de tarjetas: `#FFFFFF`
- Alerta ambar: `#F5A623`
- Positivo verde: `#2E7D32`

## Equivalencias De Visuales En Power BI

Estos son los nombres que probablemente veras en Power BI en español:

| Nombre en ingles | Nombre habitual en Power BI en español | Uso recomendado |
|---|---|---|
| KPI card / Card | Tarjeta | Indicadores principales como presupuesto, gasto, beneficiarios |
| Multi-row card | Tarjeta de varias filas | Resumen compacto de varios indicadores |
| Clustered bar chart | Grafico de barras agrupadas | Comparar proyectos, paises o categorias horizontalmente |
| Clustered column chart | Grafico de columnas agrupadas | Comparar valores verticalmente |
| Stacked bar chart | Grafico de barras apiladas | Comparar composicion por categoria |
| 100% stacked bar chart | Grafico de barras 100% apiladas | Mostrar porcentajes por grupo |
| Line chart | Grafico de lineas | Evolucion mensual o temporal |
| Donut chart | Grafico de anillos | Distribucion por donante o modalidad |
| Pie chart | Grafico circular | Similar al anillo, pero menos recomendable |
| Matrix | Matriz | Tabla dinamica con jerarquias, totales y formato condicional |
| Table | Tabla | Listados de transacciones o riesgos |
| Map | Mapa | Vista por pais, ciudad o coordenadas |
| Filled map | Mapa coropletico / mapa relleno | Comparacion geografica por pais o region |
| Treemap | Mapa de arbol | Distribucion por categoria de presupuesto |
| Slicer | Segmentacion de datos | Filtros de pais, ano, donante, proyecto |
| Gauge | Medidor | Avance contra objetivo, usar con moderacion |
| Heatmap | Matriz con formato condicional | Riesgo por proyecto y categoria |

Nota: Power BI puede cambiar algunos nombres segun version e idioma. Si no encuentras un visual exacto, usa el icono: barras horizontales para "barras agrupadas", columnas verticales para "columnas agrupadas", circulo con agujero para "anillos", y tabla con totales para "matriz".

## Pagina 1: Resumen Ejecutivo

Objetivo: mostrar de un vistazo el estado financiero, operativo y de cumplimiento de todo el portfolio.

Fila superior de tarjetas:

- `Total Budget`
- `Total Expenditure`
- `Burn Rate %`
- `Beneficiaries Reached`
- `Compliance Rate %`
- `Active Grants`

Visuales principales:

- **Grafico de barras agrupadas**: `Project_Name` en el eje; medidas `Revised Budget` y `Total Expenditure` como valores.
- **Grafico de barras** o **mapa**: `Country` por `Beneficiaries Reached`.
- **Grafico de anillos**: `Donor_Name` como leyenda; `Revised Budget` como valores.
- **Mapa**: latitud y longitud de `dim_locations`; tamano por `Total Expenditure`; color o leyenda por `Audit_Risk_Level`.

Segmentaciones de datos recomendadas:

- Ano
- Pais
- Proyecto
- Donante
- Sector

## Pagina 2: Presupuesto Vs Gasto Real

Objetivo: analizar presupuesto, gasto, compromisos, variaciones y ritmo de ejecucion.

Visuales:

- **Grafico de barras agrupadas**: `Budget_Category` en el eje; `Revised Budget`, `Total Expenditure` y `Total Commitments` como valores.
- **Grafico de lineas**: `Date_Table[Year-Month]` en el eje; `Burn Rate %` como valor.
- **Matriz**: proyecto, donante, categoria de presupuesto, presupuesto revisado, gasto, compromisos, presupuesto restante y variacion.
- **Mapa de arbol** o **grafico de barras**: gasto por categoria de presupuesto.

Formato condicional:

- `Burn Rate %` por encima de 90%: ambar.
- `Remaining Budget` por debajo de 0: rojo.
- `Forecast Variance` por debajo de 0: rojo.

## Pagina 3: Seguimiento De Donantes Y Grants

Objetivo: mostrar exposicion por donante, estado de grants, reporting y desviaciones de forecast.

Visuales:

- **Grafico de barras apiladas**: donante por gasto y compromisos.
- **Matriz**: grant ID, donante, proyecto, presupuesto revisado, gasto, burn rate, forecast variance y reporting status.
- **Grafico de columnas agrupadas**: forecast variance por donante.
- **Grafico de barras**: reportes a tiempo vs reportes tardios.

Segmentaciones:

- Donante
- Grant ID
- Estado de reporting
- Riesgo de deadline de donante

## Pagina 4: Operaciones CVA

Objetivo: analizar transferencias monetarias, hogares alcanzados, ciclos de pago, modalidades y PDM.

Fila superior de tarjetas:

- `CVA Transfer Total`
- `Households Reached`
- `Average Transfer Value`
- `PDM Completion %`

Visuales:

- **Grafico de columnas agrupadas**: `Payment_Cycle` en el eje; `CVA Transfer Total` como valor.
- **Grafico de anillos**: `Transfer_Modality` como leyenda; `Households Reached` como valor.
- **Matriz**: branch/base de distribucion, ciclo de pago, valor de transferencia, hogares alcanzados y estado PDM.
- **Grafico de barras**: pais y branch/base por hogares alcanzados.

Filtros:

- `Sector = CVA`
- Modalidad de transferencia
- Ciclo de pago
- Branch/base de distribucion

## Pagina 5: Alcance De Beneficiarios

Objetivo: comparar poblacion planificada vs alcanzada y mostrar desagregacion por sexo y edad.

Visuales:

- **Grafico de barras agrupadas**: proyecto en el eje; beneficiarios planificados vs alcanzados como valores.
- **Grafico de barras 100% apiladas**: mujeres, hombres, ninas y ninos por pais o proyecto.
- **Grafico de barras**: sector por `Beneficiary Achievement %`.
- **Matriz**: pais, branch/base, sector, planificados, alcanzados, porcentaje de logro y coste medio por beneficiario.

Usa rojo solo para bajo cumplimiento o riesgo. Para comparaciones normales, usa grises y tonos neutros.

## Pagina 6: Cumplimiento Y Preparacion Para Auditoria

Objetivo: mostrar documentacion, procurement, reporting, riesgo de auditoria y transacciones que requieren revision.

Fila superior de tarjetas:

- `Documentation Completeness %`
- `Procurement Completeness %`
- `On-Time Reporting %`
- `High Risk Transaction Count`
- `Audit Risk Score`

Visuales:

- **Matriz con formato condicional tipo heatmap**: proyecto por categoria de presupuesto; valor `Audit Risk Score`.
- **Grafico de barras**: estado de documentacion por numero de transacciones.
- **Grafico de barras**: estado de procurement por numero de transacciones.
- **Tabla**: listado de transacciones de alto riesgo con transaction ID, donante, proyecto, budget line, documentation status, procurement status, reporting status y comments.

Formato condicional:

- Riesgo alto: rojo.
- Riesgo medio: ambar.
- Riesgo bajo: verde.

## Pagina 7: Vista Geografica / Branch

Objetivo: comparar paises, ubicaciones, bases y branches desde una perspectiva operativa.

Visuales:

- **Mapa**: burbujas por branch/base, tamano por gasto y color por sector.
- **Grafico de barras**: branch/base por beneficiarios alcanzados.
- **Matriz**: pais, location, branch/base, proyecto, sector, gasto y compliance rate.
- **Graficos pequenos por pais** si quieres comparar gasto por sector. En Power BI puede hacerse con "small multiples" si tu version lo permite; si no, usa barras filtradas por pais.

Segmentaciones:

- Pais
- Branch/Base
- Sector
- Proyecto
- Donante

## Recomendaciones Para LinkedIn

- Exporta la Pagina 1 como imagen principal.
- Exporta la Pagina 6 como segunda imagen para mostrar compliance y audit readiness.
- Exporta la Pagina 4 como tercera imagen si quieres destacar operaciones CVA.
- Usa lienzo 16:9.
- Asegurate de que las tarjetas KPI sean legibles en tamano de feed de LinkedIn.
- Incluye una nota visible en el portfolio o en el post: "Dataset sintetico y anonimizado. No contiene datos confidenciales ni datos identificables de beneficiarios."
