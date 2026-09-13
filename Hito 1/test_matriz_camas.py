import pytest

from matriz_camas import crear_matriz


def test_matriz_recien_creada():
    matriz = crear_matriz(3, 4)

    assert matriz._matriz == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]


def test_ocupar_cama():
    matriz = crear_matriz(2, 3)
    matriz.ocupar(1, 0)

    assert matriz._matriz[0][1] == 1


def test_ocupar_cama_ya_ocupada():
    matriz = crear_matriz(2, 3)
    matriz.ocupar(1, 0)

    with pytest.raises(ValueError, match="La cama 1 ya se encunentra ocupada en el turno 0"):
        matriz.ocupar(1, 0)


def test_turno_fuera_de_limite():
    matriz = crear_matriz(2, 3)

    with pytest.raises(IndexError, match="Turno fuera del limite"):
        matriz.ocupar(0, 5)


def test_cama_fuera_de_limite():
    matriz = crear_matriz(2, 3)

    with pytest.raises(IndexError, match="Cama fuera del limite"):
        matriz.ocupar(5, 0)


def test_liberar_cama_ocupada():
    matriz = crear_matriz(2, 3)
    matriz.ocupar(1, 0)
    matriz.liberar(1, 0)

    assert matriz._matriz[0][1] == 0


def test_liberar_cama_libre():
    matriz = crear_matriz(2, 3)

    with pytest.raises(ValueError, match="La cama 1 ya se encuentra libre en el turno 0"):
        matriz.liberar(1, 0)


def test_consultar_disponibilidad():
    matriz = crear_matriz(2, 4)
    matriz.ocupar(1, 0)
    matriz.ocupar(3, 0)
    disponibles = matriz.consultar_disponibilidad(0)

    assert disponibles == [0, 2]


def test_consultar_disponibilidad_todas_libres():
    matriz = crear_matriz(2, 4)
    disponibles = matriz.consultar_disponibilidad(1)

    assert disponibles == [0, 1, 2, 3]


def test_consultar_disponibilidad_sin_camas_libres():
    matriz = crear_matriz(1, 3)
    matriz.ocupar(0, 0)
    matriz.ocupar(1, 0)
    matriz.ocupar(2, 0)
    disponibles = matriz.consultar_disponibilidad(0)

    assert disponibles == []


def test_consultar_disponibilidad_turno_fuera_de_limite():
    matriz = crear_matriz(2, 4)

    with pytest.raises(IndexError, match="Turno fuera del limite"):
        matriz.consultar_disponibilidad(10)


def test_reporte_ocupacion():
    matriz = crear_matriz(2, 4)
    matriz.ocupar(0, 0)
    matriz.ocupar(2, 0)
    matriz.ocupar(1, 1)
    reporte = matriz.reporte_ocupacion()

    assert reporte == [
        {
            "turno": 0,
            "ocupadas": 2,
            "libres": 2,
            "total": 4
        },
        {
            "turno": 1,
            "ocupadas": 1,
            "libres": 3,
            "total": 4
        }
    ]


def test_reporte_matriz_sin_ocupacion():
    matriz = crear_matriz(2, 3)
    reporte = matriz.reporte_ocupacion()

    assert reporte == [
        {
            "turno": 0,
            "ocupadas": 0,
            "libres": 3,
            "total": 3
        },
        {
            "turno": 1,
            "ocupadas": 0,
            "libres": 3,
            "total": 3
        }
    ]


def test_crear_matriz_sin_turnos():
    with pytest.raises(ValueError, match="El numero de turnos y camas deben ser mayores que 0"):
        crear_matriz(0, 4)


def test_crear_matriz_sin_camas():
    with pytest.raises(ValueError, match="El numero de turnos y camas deben ser mayores que 0"):
        crear_matriz(3, 0)


def test_indices_negativos():
    matriz = crear_matriz(3, 4)

    with pytest.raises(IndexError, match="Turno fuera del limite"):
        matriz.ocupar(0, -1)


def test_representacion_matriz():
    matriz = crear_matriz(2, 3)
    matriz.ocupar(1, 0)

    assert repr(matriz) == "[[0, 1, 0], [0, 0, 0]]"