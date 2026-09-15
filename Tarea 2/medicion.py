import random
import timeit

from matriz_v2 import Matriz

random.seed(11)

def crear_matriz(lado: int)->Matriz:
    """
    Crea y llena una matriz cuadrada con digitos aleatorios

    complejidad: O(lado^2)
    """
    matriz =Matriz(lado, lado)

    for i in range(lado):
        for j in range(lado):
            matriz.asignar(i, j, random.randint(0, 9))

    return matriz

def medir_suma(matriz: Matriz)-> float:
    """
    Mide el tiempo de ejecucion de suma(), dando a su vez el mejor tempo

    Complejidad O(fila * columna)
    """
    tiempos = timeit.repeat(stmt="matriz.suma()", globals={"matriz":matriz},repeat=5,number=1)

    return min(tiempos)

def main()->None:
    """
    Ejecuta las mediciones para las tres matrices

    Complejidad: O(n^2)
    """
    for lado in (250, 500, 1000):
        matriz = crear_matriz(lado)
        tiempo = medir_suma(matriz)
        celdas = lado * lado

        print("\nLado: ", lado)
        print("Celdas: ", celdas)
        print("mejor tiempo: ", tiempo, "segundos")

if __name__ == "__main__":
    main()