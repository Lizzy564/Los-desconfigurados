import time
from arreglo_dinamico import ArregloDinamico
from paciente import Paciente

def medir_insertar(cantidad):
    arreglo = ArregloDinamico()
     
    inicio = time.perf_counter()

    for i in range(cantidad):
        paciente = Paciente(
            1000000000 + i, 
            25, 
            3, 
            2.45
        )
        arreglo.insertar(paciente)
    fin = time.perf_counter()

    return fin - inicio 

cantidades = [100, 500, 1000, 2000, 5000, 10000]
print("Cantidad de pacientes  |  Tiempo de inserción")

for cantidad in cantidades:
    tiempo = medir_insertar(cantidad)
    print(cantidad, "|", tiempo)