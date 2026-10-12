import os
import sys
from collections import deque
from timeit import default_timer

import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nucleo.lista_doble import ListaDoble

TAMANOS = (1_000, 10_000, 50_000)
OPS = 200


def eliminar_doble(n):
    lista = ListaDoble()
    nodos = [lista.insertar_final(i) for i in range(n)]
    medio = nodos[n // 2: n // 2 + OPS]  # nodos ya conocidos (indice id -> nodo)

    inicio = default_timer()
    for nodo in medio:
        lista.eliminar(nodo)
    return (default_timer() - inicio) / OPS * 1e6  # microsegundos por operacion


def eliminar_list(n):
    datos = list(range(n))

    inicio = default_timer()
    for _ in range(OPS):
        datos.pop(len(datos) // 2)
    return (default_timer() - inicio) / OPS * 1e6


def eliminar_deque(n):
    datos = deque(range(n))

    inicio = default_timer()
    for _ in range(OPS):
        del datos[len(datos) // 2]
    return (default_timer() - inicio) / OPS * 1e6


def insertar_doble(n):
    lista = ListaDoble()
    nodos = [lista.insertar_final(i) for i in range(n)]
    nodo_medio = nodos[n // 2]

    inicio = default_timer()
    for i in range(OPS):
        lista.insertar_despues(nodo_medio, i)
    return (default_timer() - inicio) / OPS * 1e6


def insertar_list(n):
    datos = list(range(n))

    inicio = default_timer()
    for i in range(OPS):
        datos.insert(len(datos) // 2, i)
    return (default_timer() - inicio) / OPS * 1e6


def insertar_deque(n):
    datos = deque(range(n))

    inicio = default_timer()
    for i in range(OPS):
        datos.insert(len(datos) // 2, i)
    return (default_timer() - inicio) / OPS * 1e6


CASOS = {
    "Eliminar en el medio": {"ListaDoble": eliminar_doble, "list": eliminar_list, "deque": eliminar_deque},
    "Insertar en el medio": {"ListaDoble": insertar_doble, "list": insertar_list, "deque": insertar_deque},
}

if __name__ == "__main__":
    figura, ejes = plt.subplots(1, 2, figsize=(10, 4))
    for eje, (titulo, estructuras) in zip(ejes, CASOS.items()):
        for nombre, funcion in estructuras.items():
            tiempos = [funcion(n) for n in TAMANOS]
            print(titulo, nombre, [round(t, 3) for t in tiempos])
            eje.plot(TAMANOS, tiempos, marker="o", label=nombre)
        eje.set(title=titulo, xlabel="N", ylabel="microsegundos por operacion",
                xscale="log", yscale="log")
        eje.legend()
    figura.tight_layout()
    figura.savefig("benchmark_listas.png", dpi=150)
