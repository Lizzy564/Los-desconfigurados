import ctypes
import random
import csv
from paciente import Paciente 

class ArregloDinamico:
    def __init__(self, capacidad_inicial: int = 10) -> None:
        """Inicializa el arreglo dinamico con una capacidad inicial.
        complejidad: O(1) tiempo, O(1) espacio
        """

        self.capacidad = capacidad_inicial
        self.tamano = 0
        self.datos = (ctypes.py_object * self.capacidad)()

    def insertar(self, paciente: Paciente) -> None:
        """Inserta un paciente al arreglo dinamico.
        complejidad: O(1) tiempo amortizado, O(1) espacio.
        """

        if self.tamano == self.capacidad:
            self.redimensionar()
        
        self.datos[self.tamano] = paciente 
        self.tamano += 1

    def redimensionar(self) -> None:
        """Duplica la capacidad del arreglo y conserva sus elementos.
        complejidad: O(n) tiempo, O(n) espacio.
        """

        new_capacidad = self.capacidad * 2
        new_datos = (ctypes.py_object * new_capacidad)()
        
        for i in range(self.tamano):
            new_datos[i] = self.datos[i]

        self.datos = new_datos
        self.capacidad = new_capacidad

    def obtener(self, indice: int) -> Paciente:
        """Obtiene el paciente almacenado en el índice indicado.
        Complejidad: O(1) tiempo, O(1) espacio.
        """

        if indice < 0 or indice >= self.tamano:
            raise IndexError("Índice fuera de rango")

        return self.datos[indice]
        
    def longitud(self) -> int:
        """Retorna la cantidad de pacientes almacenados.
        Complejidad: O(1) tiempo, O(1) espacio.
        """

        return self.tamano
    
    def eliminar(self, id: int) -> None:
        """Elimina el paciente que tiene el ID indicado.
        Complejidad: O(n) tiempo, O(1) espacio.
        """

        posicion = -1

        for i in range(self.tamano): 
            if self.datos[i].id == id:
                posicion = i
                break 

        if posicion == -1:
            raise ValueError("Paciente no encontrado")

        for i in range(posicion, self.tamano -1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.tamano -1] = None 
        self.tamano -= 1 

    def generar_llegadas_poisson(self, n: int = 5000) -> None:
        """Genera n pacientes con tiempos de llegada según distribución de Poisson.
        Complejidad: O(n) tiempo, O(n) espacio.
        """

        tiempo_actual = 0

        for i in range(n):
            intervalo = random.expovariate(1)
            tiempo_actual += intervalo

            paciente = Paciente(
                1000000000 + i, 
                random.randint(1, 100), 
                random.randint(1, 5), 
                tiempo_actual
            )
            self.insertar(paciente)
            
    def cargar_censo_desde_csv(self, ruta: str) -> None:
        """Carga pacientes desde un archivo CSV y los inserta en el arreglo.
        Complejidad: o(n) tiempo, O(n) espacio.
        """
        
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                paciente = Paciente(
                    int(fila["id"]), 
                    int(fila["edad"]),
                    int(fila["nivel_triage"]),
                    float(fila["hora_llegada"])
                )
                self.insertar(paciente)


