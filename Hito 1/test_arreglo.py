from arreglo_dinamico import ArregloDinamico
from paciente import Paciente

def crear_paciente(id):
    return Paciente(id, 25, 3, 2.45)

arreglo = ArregloDinamico(2)
paciente = Paciente(1116182650, 20, 2, 30)
paciente2 = Paciente(1202566655, 25, 3, 35)
paciente3 = Paciente(1505454555, 12, 2, 42)

arreglo.insertar(paciente)
arreglo.insertar(paciente2)
arreglo.insertar(paciente3)

print("La capacidad del arreglo es: ", arreglo.capacidad)
print("La cantidad de pacientes es: ", arreglo.longitud())
print("\n") 

print("El ID del primer paciente es: ", arreglo.obtener(0).id)
print("El ID del segundo paciente es: ", arreglo.obtener(1).id)
print("El ID del tercer paciente es: ", arreglo.obtener(2).id)

print("\n")

arreglo.eliminar(1202566655)
print("La cantidad después de eliminar es: ", arreglo.longitud())
print("El ID del primer paciente es: ", arreglo.obtener(0).id)
print("El ID del segundo paciente es: ", arreglo.obtener(1).id)

print("\n")

arreglo_poisson = ArregloDinamico()
arreglo_poisson.generar_llegadas_poisson(5)
print("Los pacientes generados con Poisson: ", arreglo_poisson.longitud())
print("\n")

arreglo_csv = ArregloDinamico()
arreglo_csv.cargar_censo_desde_csv("Hito 1/censo_prueba.csv")
print("Pacientes cargados desde CSV: ", arreglo_csv.longitud())
print("El ID del primer paciente es: ", arreglo_csv.obtener(0).id)
print("La edad del primer paciente es: ", arreglo_csv.obtener(0).edad)
print("Triage del primer paciente: ", arreglo_csv.obtener(0).nivel_triage)
print("La hora de llegada es: ", arreglo_csv.obtener(0).hora_llegada)
print("\n")

#Prueba indice fuera de rango
try:
    arreglo.obtener(10)
    assert False
except IndexError:
    print("Realizada la prueba de índice fuera de rango")

#Prueba de paciente inexistente 
try:
    arreglo.eliminar(9999999999)
    assert False
except ValueError:
    print("Realizada la prueba de paciente inexistente")

#Prueba de generacion de 5000 pacientes con Poisson
arreglo_poisson_5000 = ArregloDinamico()
arreglo_poisson_5000.generar_llegadas_poisson(5000)
assert arreglo_poisson_5000.longitud() == 5000

print("Realizada la prueba de generación de 5.000 pacientes ")

#Prueba arreglo vacío
arreglo = ArregloDinamico()
assert arreglo.longitud() == 0
print("Realizada la prueba del arreglo vacío")

print("\n")
arreglo_censo_5000 = ArregloDinamico()
arreglo_censo_5000.cargar_censo_desde_csv("Hito 1/censo_5000.csv")

print("Pacientes cargados desde censo_5000.csv", arreglo_censo_5000.obtener(0).id)
print("El ID del último paciente es: ", arreglo_censo_5000.obtener(4999).id)

#Pruebas espeficas para pytest
def test_arreglo_vacio():
    arreglo = ArregloDinamico()
    assert arreglo.longitud() == 0

def test_un_solo_elemento():
    arreglo = ArregloDinamico()
    paciente = Paciente(1000000001, 25, 3, 2.45)
    arreglo.insertar(paciente)
    assert arreglo.longitud() == 1
    assert arreglo.obtener(0).id == 1000000001

def test_insercion_dispara_redimensionamiento():
    arreglo = ArregloDinamico(2)

    paciente1 = Paciente(1000000001, 25, 3, 2.45)
    paciente2 = Paciente(1000000002, 30, 2, 3.10)
    paciente3 = Paciente(1000000003, 10, 1, 4.20)

    arreglo.insertar(paciente1)
    arreglo.insertar(paciente2)

    #la capacidad inicial es 2
    #Al insertar el tercer paciente la capacidad debe duplicase a 4
    arreglo.insertar(paciente3)

    assert arreglo.capacidad == 4
    assert arreglo.longitud() == 3
    assert arreglo.obtener(2).id == 1000000003

def test_eliminar_ultimo_elemento():
    arreglo = ArregloDinamico()

    paciente1 = Paciente(1000000001, 25, 3, 2.45)
    paciente2 = Paciente(1000000002, 30, 2, 3.10)

    arreglo.insertar(paciente1)
    arreglo.insertar(paciente2)

    arreglo.eliminar(1000000002)

    assert arreglo.longitud() == 1
    assert arreglo.obtener(0).id == 1000000001