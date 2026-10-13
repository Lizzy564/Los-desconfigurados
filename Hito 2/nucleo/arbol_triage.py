from nucleo.dominio import Nivel

class NodoDesicion:

    def __int__(self, pregunta=None, si=None, no=None, nivel=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no
        self.nivel = nivel

def clasificar(nodo, respuesta):
    if nodo.nivel is not None:
        return nodo.nivel

    respuesta = respuesta.pop(0)

    if respuesta:
        return clasificar(nodo.si, respuesta)

    else:
        return clasificar(nodo.no)

def contruir_arbol(spec):
    if "nivel" in spec:
        return NodoDesicion(nivel=Nivel[spec["nivel"]])

    return NodoDesicion(
        pregunta=spec["pregunta"],
        si=contruir_arbol(spec["si"]),
        no=contruir_arbol(spec["no"])
    )

def profundidad(nodo):

    if nodo.nivel is not None:
        return 0

    profundidad_si = profundidad(nodo.si)
    profundidad_no = profundidad(nodo.no)

    return 1 + max(profundidad_si, profundidad_no)

def contar_nodos(nodo):
    if nodo is None:
        return 0

    if nodo.nivel is not None:
        return 1

    return 1 + contar_nodos(nodo.si) + contar_nodos(nodo.no)