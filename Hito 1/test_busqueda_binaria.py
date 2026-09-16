import pytest

from arreglo_dinamico import ArregloDinamico
from Ordenamientos import ordenar_por_id
from busqueda_binaria import (busqueda_binaria, esta_ordenado_por_id)

RUTA_CENSO = "censo_5000.csv"

@pytest.fixture
def censo_real_ordenado():
    """Carga el censo real desde el CSV y lo ordena por ID"""
    censo = ArregloDinamico()
    censo.cargar_censo_desde_csv(RUTA_CENSO)

    return ordenar_por_id(censo)

def test_documento_existente(censo_real_ordenado):
    """Verifica un ID que sí existe en el censo real"""

    paciente_objetivo = censo_real_ordenado.obtener(0)
    id_buscado = paciente_objetivo.id

    paciente_encontrado = busqueda_binaria(censo_real_ordenado, id_buscado)

    assert paciente_encontrado is not None
    assert paciente_encontrado.id == id_buscado

def test_documento_inexistente(censo_real_ordenado):
    """Verifica un ID que no existe en el censo"""

    id_inexistente = -999999

    paciente_encontrado = busqueda_binaria(
        censo_real_ordenado,
        id_inexistente
    )

    assert paciente_encontrado is None


def test_arreglo_desordenado_falla_controladamente():
    """Verifica que la búsqueda falle si el arreglo no está ordenado por ID"""

    censo_original = ArregloDinamico()
    censo_original.cargar_censo_desde_csv(RUTA_CENSO)
    censo_desordenado = ArregloDinamico()

    # Insertamos dos pacientes en orden contrario.
    primero = censo_original.obtener(0)
    segundo = censo_original.obtener(1)

    censo_desordenado.insertar(segundo)
    censo_desordenado.insertar(primero)

    assert esta_ordenado_por_id(censo_desordenado) is False

    with pytest.raises(ValueError):
        busqueda_binaria(censo_desordenado, primero.id)
