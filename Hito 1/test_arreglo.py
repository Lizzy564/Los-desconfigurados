from arreglo_dinamico import ArregloDinamico
from paciente import Paciente

arreglo = ArregloDinamico()
paciente = Paciente(1, 20, 2, "08:30")
arreglo.insertar(paciente)

print("La cantidad inicial es: ", arreglo.longitud())
print("El ID del paciente es: ", arreglo.obtener(0).id)
