import random
from Pacientes import Paciente # type: ignore
from Ordenamientos import mergesort, insertion_sort, ordenar_por_triage_y_hora, ordenar_por_tiempo_espera


#Casos borde generales
def test_casos_borde():
    clave = lambda x: x  # Función de clave que devuelve el mismo valor
    for algoritmo in (mergesort, insertion_sort):
        assert algoritmo([], clave) == []
        assert algoritmo([5], clave) == [5]
        assert algoritmo([1, 2, 3], clave) == [1, 2, 3]
        assert algoritmo([3, 1, 3, 2, 1], clave) == [1, 1, 2, 3, 3]


#Prueba con 1000 datos 

def test_coincide_con_sorted_1000_datos():
    random.seed(1)
    datos = [random.randint(0, 1500) for _ in range(1000)]
    clave = lambda x: x  # Función de clave que devuelve el mismo valor
    assert mergesort(datos, clave) == sorted(datos)
    assert insertion_sort(datos, clave) == sorted(datos)


#Censo pacientes
def censo_prueba():
    return [
        Paciente(1, 30, 5, hora_llegada=7.0),
        Paciente(2, 45, 1, hora_llegada=11.5),
        Paciente(3, 22, 3, hora_llegada=8.15),
        Paciente(4, 50, 2, hora_llegada=9.05),
        Paciente(5, 60, 2, hora_llegada=9.50), ]

def test_ordenar_por_triage_y_hora():
    resultado = ordenar_por_triage_y_hora(censo_prueba())
    ids = [paciente.id for paciente in resultado]
    assert ids == [2, 4, 5, 3, 1]


def test_ordenar_por_tiempo_espera_mayor():
    resultado = ordenar_por_tiempo_espera(censo_prueba(), hora_actual=20)
    assert resultado[0].id == 1  # Paciente con mayor tiempo de espera


def test_censo_vacio():
    assert ordenar_por_triage_y_hora([]) == []
    unico = [Paciente(1, 30, 5, hora_llegada=5.0)]
    assert ordenar_por_triage_y_hora(unico) == unico

#Formato pacientes

def test_formato_pacientes():
    random.seed(10)
    censo = [
        Paciente(i, random.randint(1, 100), random.randint(1, 5), random.uniform(0, 500))
        for i in range(1000)
    ]
    resultado = ordenar_por_triage_y_hora(censo)
    niveles = [paciente.nivel_triage for paciente in resultado]
    assert niveles == sorted(niveles)

def test_ordena_por_id():
    censo = [Paciente(30, 1, 2, 5.0), Paciente(10, 1, 2, 5.0), Paciente(20, 1, 2, 5.0)]
    resultado = ordenar_por_id(censo)
    assert [paciente.id for paciente in resultado] == [10, 20, 30]
