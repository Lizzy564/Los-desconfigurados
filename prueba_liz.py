from agenda import Agenda


def probar_agenda_vacia():
    a = Agenda()
    assert len(a) == 0, "Una agenda nueva debería tener tamaño 0"
    assert a.contiene("Ana") is False, "No debería contener nada todavía"


def probar_buscar_a_mano():
    # Metemos contactos directamente en la estructura interna
    # (solo para probar _buscar; en el código real esto lo hará
    # Milo desde 'agregar').
    a = Agenda()
    a._contactos = [("Ana", "111"), ("Bruno", "222"), ("Carla", "333")]

    # Buscar algo que SÍ está
    pos, encontrado = a._buscar("Bruno")
    assert encontrado is True and pos == 1, "Debería encontrar a Bruno en la posición 1"

    # Buscar algo que NO está, y ver que la posición sugerida es correcta
    pos, encontrado = a._buscar("Beto")  # va entre Ana(0) y Bruno(1)
    assert encontrado is False and pos == 1, "Beto debería insertarse en la posición 1"

    pos, encontrado = a._buscar("Zoe")  # va al final
    assert encontrado is False and pos == 3


def probar_contiene_y_telefono_de():
    a = Agenda()
    a._contactos = [("Ana", "111"), ("Bruno", "222")]

    assert a.contiene("Ana") is True
    assert a.contiene("Nadie") is False
    assert a.telefono_de("Bruno") == "222"

    try:
        a.telefono_de("Nadie")
        assert False, "Debería haber lanzado KeyError"
    except KeyError:
        pass  # esto es lo esperado


if __name__ == "__main__":
    probar_agenda_vacia()
    probar_buscar_a_mano()
    probar_contiene_y_telefono_de()
    print("Todo OK ✅ — la parte de Liz funciona como se espera.")