
from arreglo_dinamico import ArregloDinamico

def esta_ordenado_por_id(censo: ArregloDinamico) -> bool:
    """ Verifica si el censo está ordenado ascendentemente por ID.

    Complejidad: O(n) tiempo y O(1) espacio."""

    cantidad = censo.longitud()

    if cantidad <= 1:
        return True

    for i in range(cantidad - 1):
        id_actual = censo.obtener(i).id
        id_siguiente = censo.obtener(i + 1).id

        if id_actual > id_siguiente:
            return False

    return True


def busqueda_binaria(censo_ordenado: ArregloDinamico,
    id_buscado: int):

    """ Busca un paciente por su ID en un ArregloDinamico ordenado. La búsqueda binaria cuesta O(log n). """

    id_buscado = int(id_buscado)

    if not esta_ordenado_por_id(censo_ordenado):
        raise ValueError("El censo debe estar ordenado por ID antes de realizar la búsqueda binaria.")

    inicio = 0
    fin = censo_ordenado.longitud() - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        paciente = censo_ordenado.obtener(medio)

        if int(paciente.id) == id_buscado:
            return paciente

        elif id_buscado < int(paciente.id):
            fin = medio - 1

        else:
            inicio = medio + 1

    return None

