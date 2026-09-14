class Matriz:
  
    """Matriz de números en una lista plana"""

    def __init__(self, filas: int, columnas: int) -> None:
        """Crea una matriz de filas x columnas llena de ceros, ademas lanza ValueError si no son positivas.
        Complejidad: O(f · c)"""
        
        if filas <= 0 or columnas <= 0:
            raise ValueError("Las filas y columnas deben ser números positivos")

        self._filas = filas
        self._columnas = columnas
        self._datos = [0] * (filas * columnas)

    def _posicion(self, i: int, j: int) -> int:
        """Calcula la posición de una celda. 
        Complejidad: O(1)"""
        
        if i < 0 or i >= self._filas or j < 0 or j >= self._columnas:
            raise IndexError("Celda fuera del rango de la matriz")

        return i * self._columnas + j

    def filas(self) -> int:
        """Devuelve la cantidad de filas de la matriz.
        Complejidad: O(1)"""
        return self._filas

    def columnas(self) -> int:
        """Devuelve la cantidad de columnas de la matriz.
        Complejidad: O(1)"""
        return self._columnas
    
    def obtener(self, i: int, j: int):
        """Devuelve el valor de una celda de la matriz.
        Complejidad: O(1)"""

       posicion = self._posicion(i, j)
       return self._datos[posicion]

    def asignar(self, i: int, j: int, valor):
        """Asigna un valor a una celda de la matriz.
        Complejidad: O(1)"""

        posicion = self._posicion(i, j)
        self._datos[posicion] = valor

    def suma(self):
        """Suma todos los valores de la matriz.
        Complejidad: O(f · c)"""

        total = 0

        for valor in self._datos:
            total += valor
        return total

