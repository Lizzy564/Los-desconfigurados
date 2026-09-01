# Reparto de roles — Tarea 3: Agenda

Equipo: Los-desconfigurados
Curso: IS061 — Estructura de Datos · 2026-2

## Liceth Moreno — usuario GitHub: Lizzy564

**Archivo:** agenda.py (parte 1)

- `__init__`: crea la agenda vacía
- `__len__`: cantidad de contactos, O(1)
- `_buscar`: búsqueda binaria propia, O(log n)
- `contiene`: verifica si un nombre existe, O(log n)
- `telefono_de`: devuelve el teléfono de un contacto, O(log n)

## Camilo Marin — usuario GitHub: HeyItsMilo

**Archivos:** agenda.py (parte 2) + README.md

- `nombres`: lista de nombres en orden alfabético, O(n)
- `agregar`: agrega o actualiza un contacto, O(n)
- `eliminar`: elimina un contacto, O(n)
- README.md: descripción del proyecto y cómo correrlo

## Lorena Buitrago — usuario GitHub: lorenamed209-alt

**Archivo:** test_agenda.py

- Pruebas con pytest para los 7 métodos de Agenda
- Casos borde: agenda vacía, nombre repetido, nombre inexistente

## Faisury Palacios — usuario GitHub: faisurypalaciosma-cpu

**Archivos:** medicion.py + resultados.md

- Medición de tiempos con 1.000, 10.000 y 100.000 contactos
- Tabla de resultados y análisis de las tres mediciones

## Verificación cruzada

- [x] Alguien que no escribió agenda.py confirmó que no hay bisect, in, .index(), sorted() ni .sort()
- [x] python -m pytest -q corre y todas las pruebas pasan
- [x] python medicion.py corre sin errores