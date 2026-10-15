import heapq
import statistics
import sys
import time
from pathlib import Path
from collections import deque

import matplotlib.pyplot as plt

RUTA_HITO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUTA_HITO))

from nucleo.cola_dinamica import ColaDinamica
from nucleo.cola_prioridad import ColaPrioridadTriage

class PacientePrueba:
    def __init__(self, documento, nivel):
        self.documento = str(documento)
        self.nivel = nivel
        self.hora_llegada = None

def medir(funcion, repeticiones = 3):
    """Devuelve la mediana de los tiempos en milisegundos"""
    tiempos = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        tiempos.append(time.perf_counter() - inicio)

    return statistics.median(tiempos) * 1000

def probar_cola_dinamica(n):
    cola = ColaDinamica()

    for i in range(n):
        cola.encolar(i)

    for _ in range(n):
        cola.desencolar()

def probar_deque(n):
    cola = deque()

    for i in range(n):
        cola.append(i)

    for _ in range(n):
        cola.popleft()

def probar_lista(n):
    cola = []

    for i in range(n):
        cola.append(i)

    for _ in range(n):
        cola.pop(0)

def probar_triage(n):
    cola = ColaPrioridadTriage()

    pacientes = [
        PacientePrueba(i, (i % 5) + 1) for i in range(n)
    ]

    for paciente in pacientes:
        cola.encolar(paciente)

    while cola.desencolar_siguiente() is not None:
        pass

def probar_heapq(n):
    monticulo = []
    pacientes = [
        PacientePrueba(i, (i % 5) + 1) for i in range(n)
    ]

    for orden, paciente in enumerate(pacientes):
        heapq.heappush(
            monticulo,
            (int(paciente.nivel), orden, paciente)
        )
        
    while monticulo:
        heapq.heappop(monticulo)

def main():
    tamanos = [1000, 3000, 6000, 10000]
    resultados = {"ColaDinamica": [],
                    "collections.deque": [],
                    "list.pop(0)": [],
                    }
    print("\nBenchmark: Colas FIFO")
    print("=" *68)
    print("Tiempos en milisegundos; mediana de 3 ejecuciones.\n")
    print(
        f"{'Elementos':>10} "
        f"{'ColaDinamica':>16} "
        f"{'deque':>14} "
        f"{'list.pop(0)':>16}"
        )

    for n in tamanos:
        propia = medir(lambda: probar_cola_dinamica(n))
        tiempo_deque = medir(lambda: probar_deque(n))
        tiempo_lista = medir(lambda: probar_lista(n))

        resultados["ColaDinamica"].append(propia)
        resultados["collections.deque"].append(tiempo_deque)
        resultados["list.pop(0)"].append(tiempo_lista)

        print(
            f"{n:>10} "
            f"{propia:>16.3f} "
            f"{tiempo_deque:>14.3f} "
            f"{tiempo_lista:>16.3f}"
        )
        
    tamanos_triage = [100, 250, 500, 1000]
    tiempos_triage = []
    tiempos_heapq = []

    print("\nBenchmark: Cola de prioridad VS Heapq")
    print("=" *52)
    print(
        f"{'Pacientes':>10} "
        f"{'ColaPrioridad':>20} "
        f"{'heapq':>14}"
    )

    for n in tamanos_triage:
        pacientes = [
            PacientePrueba(i, (i % 5) + 1)
            for i in range(n)
        ]

        tiempo_triage = medir(lambda: probar_triage(pacientes))
        tiempo_heap = medir(lambda: probar_heapq(pacientes))
        tiempos_triage.append(tiempo_triage)
        tiempos_heapq.append(tiempo_heap)

        print(
            f"{n:>10} "
            f"{tiempo_triage:>20.3f} "
            f"{tiempo_heap:>14.3f}"
        )

    fig, ejes = plt.subplots(1, 2, figsize=(13, 5))

    for nombre, tiempos in resultados.items():
        ejes[0].plot(tamanos, tiempos, marker="o", label=nombre)

    ejes[0].set_title("Comparación de colas FIFO")
    ejes[0].set_xlabel("Cantidad de elementos")
    ejes[0].set_ylabel("Tiempo (milisegundos)")
    ejes[0].legend()
    ejes[0].grid(True, alpha=0.3)

    ejes[1].plot(tamanos_triage, tiempos_triage, marker="o", label="ColaPrioridadTriage")
    ejes[1].plot(tamanos_triage, tiempos_heapq, marker="s", label="heapq")
    
    ejes[1].set_title("Comparación de colas de prioridad")
    ejes[1].set_xlabel("Cantidad de pacientes")
    ejes[1].set_ylabel("Tiempo (milisegundos)")
    ejes[1].legend()
    ejes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    ruta = Path(__file__).resolve().parent / "resultados_bench_colas.png"
    fig.savefig(ruta, dpi=150, bbox_inches="tight")

    print(f"\nGráfico guardado en: {ruta}")
    plt.show()

if __name__ == "__main__":
    main()
