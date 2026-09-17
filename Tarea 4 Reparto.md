# Reparto de roles — Tarea 4: Una matriz sobre una sola línea

Equipo: Los-desconfigurados
Curso: IS061 — Estructura de Datos · 2026-2

## Faisury Palacios — usuario GitHub: faisurypalaciosma-cpu

**Archivo:** matriz.py (parte 1)

- `__init__`: crea la matriz vacía sobre una sola lista plana `_datos`, lanza `ValueError` si filas/columnas no son positivas
- `_posicion`: calcula `i * columnas + j` y valida el rango, O(1)
- `filas`: cantidad de filas, O(1)
- `columnas`: cantidad de columnas, O(1)

## Lorena Buitrago — usuario GitHub: LoreMedina2907

**Archivo:** matriz.py (parte 2) + integración final

- `obtener`: valor de una celda usando `_posicion`, O(1)
- `asignar`: escribe un valor en una celda usando `_posicion`, O(1)
- `suma`: recorre y suma todas las celdas, O(f · c)
- Integración de su parte con la de Faisury en un único matriz.py coherente

## Liceth Moreno — usuario GitHub: Lizzy564

**Archivo:** test_matriz.py

- 8 pruebas con pytest para la clase Matriz
- Casos borde: matriz 1×1, dimensiones no positivas (ValueError), coordenadas fuera de rango en obtener/asignar (IndexError)

## Camilo Marin — usuario GitHub: HeyItsMilo

**Archivos:** medicion.py + resultados.md

- Medición de tiempos de `suma()` con matrices de lado 250, 500 y 1.000, `random.seed(11)`, 5 corridas por matriz (mejor tiempo)
- Tabla de resultados y análisis del factor de crecimiento al doblar el lado

## Verificación cruzada

- [x] Alguien que no escribió matriz.py confirmó que no hay listas de listas ni numpy, y que `i * columnas + j` está escrito explícitamente
- [x] python -m pytest -q corre y todas las pruebas pasan
- [x] python medicion.py corre sin errores
