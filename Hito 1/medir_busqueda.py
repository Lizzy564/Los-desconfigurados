import time
import matplotlib.pyplot as plt
from arreglo_dinamico import ArregloDinamico
from Ordenamientos import ordenar_por_id
from busqueda_binaria import busqueda_binaria

censo = ArregloDinamico()
censo.cargar_censo_desde_csv("censo_5000.csv")

censo = ordenar_por_id(censo)

tamanos = [10, 1000, 3000, 5000]
tiempos = []

for tamano in tamanos:
    prueba = ArregloDinamico()

    for i in range(tamano):
        prueba.insertar(censo.obtener(i))

    id_buscado = prueba.obtener(tamano // 2).id

    inicio = time.perf_counter()

    for _ in range(1000):
        busqueda_binaria(prueba, id_buscado)

    fin = time.perf_counter()

    tiempo_promedio = (fin - inicio) / 1000 * 1000
    tiempos.append(tiempo_promedio)

    print(
        f"{tamano} pacientes: "
        f"{tiempo_promedio:.8f} milisegundos"
    )

plt.plot(
    tamanos,
    tiempos,
    marker="o"
)

plt.title("Búsqueda binaria")
plt.xlabel("Cantidad de pacientes")
plt.ylabel("Tiempo promedio (milisegundos)")
plt.grid(True)

plt.savefig("grafica_busqueda.png")
plt.show()

print("Gráfica guardada como grafica_busqueda.png")
