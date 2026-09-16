import time
import matplotlib.pyplot as plt
from arreglo_dinamico import ArregloDinamico
from Ordenamientos import ordenar_por_id
from busqueda_binaria import busqueda_binaria
from matriz_camas import crear_matriz

RUTA_CENSO = "censo_5000.csv"

TAMANOS = [10, 1000, 3000, 5000]
ITERACIONES = 100

tiempos_insercion = []
tiempos_matriz = []
tiempos_ordenamiento = []
tiempos_busqueda = []

# Cargar el censo base
censo_base = ArregloDinamico()
censo_base.cargar_censo_desde_csv(RUTA_CENSO)

#ARREGLO DINÁMICO

for tamano in TAMANOS:

    inicio = time.perf_counter()

    for _ in range(ITERACIONES):
        subcenso = ArregloDinamico()

        for i in range(tamano):
            subcenso.insertar(censo_base.obtener(i))
    fin = time.perf_counter()
    tiempo_promedio = ((fin - inicio) / ITERACIONES) * 1000

    tiempos_insercion.append(tiempo_promedio)

    censo_prueba = ArregloDinamico()

    for i in range(tamano):
        censo_prueba.insertar(censo_base.obtener(i))

    #MATRIZ DE CAMAS
    
    matriz = crear_matriz(n_turnos=3, n_camas=tamano)

    for cama in range(tamano // 2):
        matriz.ocupar(cama, 0)

    inicio = time.perf_counter()

    for _ in range(ITERACIONES):
        matriz.reporte_ocupacion()

    fin = time.perf_counter()

    tiempo_promedio = ((fin - inicio) / ITERACIONES) * 1000

    tiempos_matriz.append(tiempo_promedio)

    # ORDENAMIENTO
    
    inicio = time.perf_counter()

    for _ in range(ITERACIONES):
        censo_ordenado = ordenar_por_id(censo_prueba)
    fin = time.perf_counter()

    tiempo_promedio = ((fin - inicio) / ITERACIONES) * 1000

    tiempos_ordenamiento.append(tiempo_promedio)
    
    #BÚSQUEDA BINARIA
    
    id_buscado = censo_ordenado.obtener(tamano // 2).id

    inicio = time.perf_counter()

    for _ in range(ITERACIONES):
        busqueda_binaria(censo_ordenado, id_buscado)

    fin = time.perf_counter()

    tiempo_promedio = ((fin - inicio) / ITERACIONES) * 1000

    tiempos_busqueda.append(tiempo_promedio)


    print(f"\nTamaño {tamano} procesado")

    print(f"\nInserción: {tiempos_insercion[-1]:.6f} ms")

    print(f"Matriz: {tiempos_matriz[-1]:.6f} ms")

    print(f"Ordenamiento: {tiempos_ordenamiento[-1]:.6f} ms")

    print(f"Búsqueda: {tiempos_busqueda[-1]:.6f} ms")

# GRÁFICA

plt.figure(figsize=(10, 6))

plt.plot(TAMANOS, tiempos_insercion, marker="o", label="Arreglo dinámico")

plt.plot(TAMANOS, tiempos_matriz, marker="s", label="Matriz de camas")

plt.plot(TAMANOS, tiempos_ordenamiento, marker="^", label="Ordenamiento")

plt.plot(TAMANOS, tiempos_busqueda, marker="d", label="Búsqueda binaria")

plt.title("Benchmark de los cuatro módulos")

plt.xlabel("Cantidad de pacientes o camas")

plt.ylabel("Tiempo promedio (milisegundos)")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafica_benchmarks_modulos.png",dpi=300)
plt.show()
print("\nBenchmark completado")
print("Gráfica guardada como 'grafica_benchmarks_modulos.png'")

