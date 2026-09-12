from arreglo_dinamico import ArregloDinamico
from paciente import Paciente

arreglo = ArregloDinamico(2)
paciente = Paciente(1116182650, 20, 2, "08:30")
paciente2 = Paciente(1202566655, 25, 3, "04:50")
paciente3 = Paciente(1505454555, 12, 2, "01:12")

arreglo.insertar(paciente)
arreglo.insertar(paciente2)
arreglo.insertar(paciente3)

print("La capacidad del arreglo es: ", arreglo.capacidad)
print("La cantidad de pacientes es: ", arreglo.longitud())
print("El ID del primer paciente es: ", arreglo.obtener(0).id)
print("El ID del segundo paciente es: ", arreglo.obtener(1).id)
print("El ID del tercer paciente es: ", arreglo.obtener(2).id)

arreglo.eliminar(1202566655)
print("La cantidad después de eliminar es: ", arreglo.longitud())
print("El ID del primer paciente es: ", arreglo.obtener(0).id)
print("El ID del segundo paciente es: ", arreglo.obtener(1).id)
