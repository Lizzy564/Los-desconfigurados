import random

from arreglo_dinamico import ArregloDinamico # type: ignore
from Pacientes import Paciente

from Ordenamientos import (
    mergesort,
    insertion_sort,
    ordenar_por_id,
    ordenar_por_triage_y_hora,
    ordenar_por_tiempo_espera
)


# Casos borde generales

def test_casos_borde():

    arreglo_vacio = ArregloDinamico()

    arreglo_unico = ArregloDinamico()
    arreglo_unico.insertar(5)

    arreglo_ordenado = ArregloDinamico()
    for valor in [1, 2, 3]:
        arreglo_ordenado.insertar(valor)

    arreglo_repetidos = ArregloDinamico()
    for valor in [3, 1, 3, 2, 1]:
        arreglo_repetidos.insertar(valor)

    clave = lambda x: x

    for algoritmo in (mergesort, insertion_sort):

        resultado = algoritmo(arreglo_vacio, clave)
        assert resultado.longitud() == 0

        resultado = algoritmo(arreglo_unico, clave)
        assert resultado.obtener(0) == 5

        resultado = algoritmo(arreglo_ordenado, clave)
        assert [resultado.obtener(i) for i in range(resultado.longitud())] == [1, 2, 3]

        resultado = algoritmo(arreglo_repetidos, clave)
        assert [resultado.obtener(i) for i in range(resultado.longitud())] == [1, 1, 2, 3, 3]


# Prueba con 1000 datos

def test_coincide_con_sorted_1000_datos():

    random.seed(1)

    arreglo = ArregloDinamico()

    datos = [random.randint(0, 1500) for _ in range(1000)]

    for dato in datos:
        arreglo.insertar(dato)

    clave = lambda x: x

    resultado_mergesort = mergesort(arreglo, clave)
    resultado_insertion = insertion_sort(arreglo, clave)

    valores_mergesort = [
        resultado_mergesort.obtener(i)
        for i in range(resultado_mergesort.longitud())
    ]

    valores_insertion = [
        resultado_insertion.obtener(i)
        for i in range(resultado_insertion.longitud())
    ]

    assert valores_mergesort == sorted(datos)
    assert valores_insertion == sorted(datos)


# Censo pacientes

def censo_prueba():

    censo = ArregloDinamico()

    censo.insertar(Paciente(1, 30, 5, hora_llegada=7.0))
    censo.insertar(Paciente(2, 45, 1, hora_llegada=11.5))
    censo.insertar(Paciente(3, 22, 3, hora_llegada=8.15))
    censo.insertar(Paciente(4, 50, 2, hora_llegada=9.05))
    censo.insertar(Paciente(5, 60, 2, hora_llegada=9.50))

    return censo


def test_ordenar_por_triage_y_hora():

    resultado = ordenar_por_triage_y_hora(censo_prueba())

    ids = [
        resultado.obtener(i).id
        for i in range(resultado.longitud())
    ]

    assert ids == [2, 4, 5, 3, 1]


def test_ordenar_por_tiempo_espera_mayor():

    resultado = ordenar_por_tiempo_espera(
        censo_prueba(),
        hora_actual=20
    )

    assert resultado.obtener(0).id == 1


def test_censo_vacio():

    censo = ArregloDinamico()

    assert ordenar_por_triage_y_hora(censo).longitud() == 0

    unico = ArregloDinamico()
    paciente = Paciente(1, 30, 5, hora_llegada=5.0)
    unico.insertar(paciente)

    resultado = ordenar_por_triage_y_hora(unico)

    assert resultado.longitud() == 1
    assert resultado.obtener(0).id == 1


# Formato pacientes

def test_formato_pacientes():

    random.seed(10)

    censo = ArregloDinamico()

    for i in range(1000):
        paciente = Paciente(
            i,
            random.randint(1, 100),
            random.randint(1, 5),
            random.uniform(0, 500)
        )

        censo.insertar(paciente)

    resultado = ordenar_por_triage_y_hora(censo)

    niveles = [
        resultado.obtener(i).nivel_triage
        for i in range(resultado.longitud())
    ]

    assert niveles == sorted(niveles)


def test_ordena_por_id():

    censo = ArregloDinamico()

    censo.insertar(Paciente(30, 1, 2, 5.0))
    censo.insertar(Paciente(10, 1, 2, 5.0))
    censo.insertar(Paciente(20, 1, 2, 5.0))

    resultado = ordenar_por_id(censo)

    ids = [
        resultado.obtener(i).id
        for i in range(resultado.longitud())
    ]

    assert ids == [10, 20, 30]


