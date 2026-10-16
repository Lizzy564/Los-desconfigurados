from datetime import datetime, timedelta
from types import SimpleNamespace

import pytest

from nucleo.pila_estatica import (
    PilaEstatica,
    PilaLlena,
    PilaVacia as PilaEstaticaVacia,)
from nucleo.pila_dinamica import PilaDinamica, PilaVacia as PilaDinamicaVacia

from nucleo.cola_estatica import (
    ColaCircularEstatica,
    ColaLlena,
    ColaVacia as ColaEstaticaVacia,)
from nucleo.cola_dinamica import ColaDinamica, ColaVacia as ColaDinamicaVacia
from nucleo.cola_prioridad import ColaPrioridadTriage
from nucleo.deshacer import GestorDeshacer

def paciente(documento, nivel, hora_llegada=None):
    """Crea un paciente minimo para probar las estructuras del test"""
    return SimpleNamespace(
        documento=str(documento),
        nivel=nivel,
        hora_llegada=hora_llegada,)

#---Pila Estatica---

def test_pila_estatica_respeta_lifo():
    pila = PilaEstatica(3)

    pila.push("A")
    pila.push("B")
    pila.push("C")

    assert len(pila) == 3
    assert pila.peek() == "C"
    assert pila.pop() == "C"
    assert pila.pop() == "B"
    assert pila.pop() == "A"
    assert pila.esta_vacia()

def test_pila_estatica_no_permite_superar_capacidad():
    pila = PilaEstatica(1)
    pila.push("A")

    with pytest.raises(PilaLlena):
        pila.push("B")

def test_pila_estatica_vacia_lanza_excepcion():
    pila = PilaEstatica(2)

    with pytest.raises(PilaEstaticaVacia):
        pila.pop()

    with pytest.raises(PilaEstaticaVacia):
        pila.peek()

def test_pila_estatica_valida_capacidad():
    with pytest.raises(ValueError):
        PilaEstatica(0)

    with pytest.raises(TypeError):
        PilaEstatica(True)

#---Pila Dinamica---

def test_pila_dinamica_respeta_lifo():
    pila = PilaDinamica()

    pila.push(10)
    pila.push(20)
    pila.push(30)

    assert len(pila) == 3
    assert pila.peek() == 30
    assert pila.pop() == 30
    assert pila.pop() == 20
    assert pila.pop() == 10
    assert pila.esta_vacia()

def test_pila_dinamica_vacia_lanza_exception():
    pila = PilaDinamica()

    with pytest.raises(PilaDinamicaVacia):
        pila.pop()

    with pytest.raises(PilaDinamicaVacia):
        pila.peek()

#---Cola circular estatica---

def test_cola_circular_respeta_fifo():
    cola = ColaCircularEstatica(3)

    cola.encolar("A")
    cola.encolar("B")
    cola.encolar("C")

    assert len(cola) == 3
    assert cola.frente() == "A"
    assert cola.desencolar() == "A"
    assert cola.desencolar() == "B"
    assert cola. desencolar() == "C"
    assert cola.esta_vacia()

def test_cola_circular_detecta_capacidad_completa():
    cola = ColaCircularEstatica(2)
    cola.encolar("A")
    cola.encolar("B")

    assert cola.esta_llena()

    with pytest.raises(ColaLlena):
        cola.encolar("C")

def test_cola_circular_reutiliza_posiciones():
    cola = ColaCircularEstatica(3)

    cola.encolar("A")
    cola.encolar("B")
    cola.encolar("C")

    assert cola.desencolar() == "A"
    assert cola.desencolar() == "B"

    cola.encolar("D")
    cola.encolar("E")

    assert cola.desencolar() == "C"
    assert cola.desencolar() == "D"
    assert cola.desencolar() == "E"
    assert cola.esta_vacia()

def test_cola_circular_vacia_lanza_exception():
    cola = ColaCircularEstatica(2)

    with pytest.raises(ColaEstaticaVacia):
        cola.desencolar()

    with pytest.raises(ColaEstaticaVacia):
        cola.frente()

def test_cola_circular_valida_capacidad():
    with pytest.raises(ValueError):
        ColaCircularEstatica(0)

    with pytest.raises(TypeError):
        ColaCircularEstatica(True)

#---Cola Dinamica---

def test_cola_dinamica_respeta_fifo():
    cola = ColaDinamica()

    cola.encolar("A")
    cola.encolar("B")
    cola.encolar("C")

    assert len(cola) == 3
    assert cola.frente() == "A"
    assert cola.desencolar() == "A"
    assert cola.desencolar() == "B"
    assert cola.desencolar() == "C"
    assert cola.esta_vacia()

def test_cola_dinamica_puede_reutilizarse_tras_vaciarse():
    cola = ColaDinamica()

    cola.encolar("A")
    assert cola.desencolar() == "A"
    assert cola.esta_vacia()

    cola.encolar("B")

    assert cola.frente() == "B"
    assert cola.desencolar() == "B"
    assert cola.esta_vacia()

def test_cola_dinamica_vacia_lanza_exception():
    cola = ColaDinamica()

    with pytest.raises(ColaDinamicaVacia):
        cola.desencolar()

    with pytest.raises(ColaDinamicaVacia):
        cola.frente()

#---Cola de Prioridda Triage---

def test_prioridad_atiende_nivel_mas_urgente_primero():
    cola = ColaPrioridadTriage()

    nivel3 = paciente("P3", 3)
    nivel1 = paciente("P1", 1)
    nivel2 = paciente("P2", 2)

    cola.encolar(nivel3)
    cola.encolar(nivel1)
    cola.encolar(nivel2)

    assert cola.desencolar_siguiente() is nivel1
    assert cola.desencolar_siguiente() is nivel2
    assert cola.desencolar_siguiente() is nivel3
    assert cola.desencolar_siguiente() is None

def test_prioridad_conserva_fifo_dentro_del_mismo_nivel():
    cola = ColaPrioridadTriage()

    primero = paciente("P1", 2)
    segundo = paciente("P2", 2)

    cola.encolar(primero)
    cola.encolar(segundo)

    assert cola.desencolar_siguiente() is primero
    assert cola.desencolar_siguiente() is segundo

def test_prioridad_rechaza_nivel_invalido():
    cola = ColaPrioridadTriage()

    with pytest.raises(ValueError):
        cola.encolar(paciente("P1", 0))

    with pytest.raises(ValueError):
        cola.encolar(paciente("P2", 6))

def test_prioridad_rechaza_identificador_duplicado():
    cola = ColaPrioridadTriage()

    cola.encolar(paciente("P1", 2))

    with pytest.raises(ValueError):
        cola.encolar(paciente("P1", 3))

def test_prioridad_retirar_paciente_especifico():
    cola = ColaPrioridadTriage()
    p1 = paciente("P1", 2)
    p2 = paciente("P2", 2)

    cola.encolar(p1)
    cola.encolar(p2)

    retirado = cola.retirar("P1")
    assert retirado is p1
    assert cola.desencolar_siguiente() is p2

def test_prioridad_reclasifica_paciente():
    cola = ColaPrioridadTriage()
    paciente_prueba = paciente("P1", 4)

    cola.encolar(paciente_prueba)

    assert cola.reclasificar("P1", 2) is True
    assert paciente_prueba.nivel == 2
    assert cola.desencolar_siguiente() is paciente_prueba

def test_prioridad_reclasificar_de_id_inexistente():
    cola = ColaPrioridadTriage()

    assert cola.reclasificar("No existe", 2) is False

def test_prioridad_cuenta_paciente_por_nivel():
    cola = ColaPrioridadTriage()

    cola.encolar(paciente("P1", 1))
    cola.encolar(paciente("P2", 1))
    cola.encolar(paciente("P3", 4))

    assert cola.contar_por_nivel() == {
        1: 2,
        2: 0,
        3: 0,
        4: 1,
        5: 0,
    }

def test_prioridad_envejece_con_tiempo_simulado():
    cola = ColaPrioridadTriage()
    ahora = datetime(2026, 1, 1, 12, 0, 0)

    tiempo_objetivo = __import__("nucleo.dominio", fromlist=["Nivel"]).Nivel(2).tiempo_objetivo_min

    antiguo = paciente(
        "P-antiguo",
        2,
        ahora - timedelta(minutes=tiempo_objetivo + 1),)

    cola.encolar(antiguo)
    cantidad = cola.envejecer(ahora)

    assert cantidad == 1
    assert antiguo.nivel == 1
    assert cola.desencolar_siguiente() is antiguo

#---Deshacer---

def test_deshacer_ejecuta_acciones_en_orden_inverso():
    gestor = GestorDeshacer()
    resultados = []

    gestor.registrar(lambda: resultados.append("primera"))
    gestor.registrar(lambda: resultados.append("segunda"))

    gestor.deshacer()
    assert resultados == ["segunda"]

    gestor.deshacer()
    assert resultados == ["segunda", "primera"]
    assert gestor.esta_vacio()

def test_deshacer_rechaza_objeto_no_ejecutableI():
    gestor = GestorDeshacer()

    with pytest.raises(TypeError):
        gestor.registrar("esto no es una acción")

def test_deshacer_sin_acciones_lanza_exception():
    gestor = GestorDeshacer()

    with pytest.raises(PilaDinamicaVacia):
        gestor.deshacer()

def test_deshacer_acepta_objeto_con_metodo_ejecutar():
    gestor = GestorDeshacer()

    class Accion:
        def ejecutar(self):
            return "accion ejecutada"

    gestor.registrar(Accion())

    assert gestor.deshacer() == "accion ejecutada"