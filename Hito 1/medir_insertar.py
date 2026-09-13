import time
import matplotlib.pyplot as plt 

from arreglo_dinamico import ArregloDinamico
from paciente import Paciente

cantidad_max = 10000
arreglo = ArregloDinamico()
tiempos = []
pacientes = []
redimensiones = []
capacidad_anterior = arreglo.capacidad

for i in range(cantidad_max):
    paciente = Paciente(
        1000000000 + i, 
        25, 
        3, 
        2.45
    )
    inicio = time.perf_counter()

    arreglo.insertar(paciente)

    fin = time.perf_counter()

    tiempo = fin - inicio 

    tiempos.append(tiempo)

    pacientes.append(i + 1)

    if arreglo.capacidad != capacidad_anterior:
        redimensiones.append(i + 1)
        capacidad_anterior = arreglo.capacidad

print("Redimensiones realizadas en: ", redimensiones)

#gráfica 
plt.figure(figsize=(12, 6))

plt.plot(pacientes, tiempos, linewidth=0.7)

#marcar los puntos donde se duplicó la capacidad
for punto in redimensiones:
    plt.axvline(
        x=punto, 
        linestyle="--",
        linewidth=0.8
    )
plt.title("Tiempo de insertar() vs. Número de pacientes")
plt.xlabel("Número de pacientes")
plt.ylabel("Tiempo de inserción (segundos)")

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("grafica_insertar.png", dpi=200)

plt.show()

print("Gráfica guardada como grafica_insertar.png")

