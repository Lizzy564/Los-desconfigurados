import os
import sys
from collections import deque
from timeit import default_timer
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nucleo.lista_doble import ListaDoble

TAMANOS = [1000, 10000, 50000]
OPS = 200


def eliminar_doble(n):
    lista = ListaDoble()
    nodos = [lista.insertar_final(i) for i in range(n)]
    medio = nodos[n // 2:n // 2 + OPS]

    inicio = default_timer()
    for nodo in medio:
        lista.eliminar(nodo)

    return (default_timer() - inicio) / OPS * 1000000


def eliminar_list(n):
    lista = list(range(n))
    inicio = default_timer()

    for i in range(OPS):
        lista.pop(len(lista) // 2)

    return (default_timer() - inicio) / OPS * 1000000


def eliminar_deque(n):
    lista = deque(range(n))
    inicio = default_timer()

    for i in range(OPS):
        del lista[len(lista) // 2]

    return (default_timer() - inicio) / OPS * 1000000


def insertar_doble(n):
    lista = ListaDoble()
    nodos = [lista.insertar_final(i) for i in range(n)]
    medio = nodos[n // 2]
    inicio = default_timer()

    for i in range(OPS):
        lista.insertar_despues(medio, i)

    return (default_timer() - inicio) / OPS * 1000000


def insertar_list(n):
    lista = list(range(n))
    inicio = default_timer()

    for i in range(OPS):
        lista.insert(len(lista) // 2, i)

    return (default_timer() - inicio) / OPS * 1000000


def insertar_deque(n):
    lista = deque(range(n))
    inicio = default_timer()

    for i in range(OPS):
        lista.insert(len(lista) // 2, i)

    return (default_timer() - inicio) / OPS * 1000000


if __name__ == "__main__":
    figura, ejes = plt.subplots(1, 2, figsize=(10, 4))

    for eje, funciones, titulo in [
        (ejes[0], [eliminar_doble, eliminar_list, eliminar_deque], "Eliminar"),
        (ejes[1], [insertar_doble, insertar_list, insertar_deque], "Insertar")
    ]:
        for nombre, funcion in zip(["ListaDoble", "list", "deque"], funciones):
            tiempos = [funcion(n) for n in TAMANOS]
            print(titulo, nombre, [round(t, 3) for t in tiempos])
            eje.plot(TAMANOS, tiempos, marker="o", label=nombre)

        eje.set(title=titulo + " en el medio", xlabel="Tamaño", ylabel="Microsegundos",
                xscale="log", yscale="log")
        eje.legend()

    figura.tight_layout()
    figura.savefig("benchmark_listas.png")
    plt.show()
