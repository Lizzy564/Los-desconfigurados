import math as m

import pytest
from matriz_v2 import Matriz

#Casos Normales

"""Una matriz recien creada llena de ceros. """

def test_Matriz_empieza_en_cero():
  m = Matriz(5, 5)
  for i in range(5):
    for j in range(5):
      assert m.obtener(i, j) == 0

"""Lo que se asigna en una celda debe recuperarse igual"""

def test_Asignar_obtener_mismoV():
  m = Matriz(3,3)
  m.asignar(1, 1, 42)
  assert m.obtener(1, 1) == 42 #Las celdas no se deben afectar
  assert m.obtener(0, 0) == 0

"""Se debe sumar todos los valores de la matriz"""
def test_suma_resultados():
  m = Matriz(5, 4)
  valores = {}
  contador = 1
  for i in range(m.filas()):
    for j in range(m.columnas()):
      valores[(i, j)] = contador
      m.asignar(i, j, contador)
      contador += 1

  assert m.suma() == sum(valores.values())

"""Filas y columnas devuelven las dimensiones al crear la matriz """
def test_filas_columnas():
 m = Matriz(2,4)
 assert m.filas() == 2
 assert m.columnas() == 4

#Casos Borde 
"""Matriz 1x1 debe comportarse igual a la normal."""
def test_matriz_1x1():
  m = Matriz(1, 1)
  assert m.obtener(0, 0) == 0
  m.asignar(0, 0, 9)
  assert m.obtener(0, 0) == 9
  assert m.suma() == 9

"""Filas o columnas no positivas deben lanzar error"""
def test_No_positivos_error():
  with pytest.raises(ValueError):
    Matriz(0, 3)
  with pytest.raises(ValueError):
    Matriz(3, 0)
  with pytest.raises(ValueError):
    Matriz(-1, -1)

"""Coordenadas fuera de rango en obtener() debe lanzar IndexError"""
def test_Fuera_de_rangoOB_error():
  m = Matriz(2, 2)
  with pytest.raises(IndexError):
    m.obtener(2, 0)
  with pytest.raises(IndexError):
    m.obtener(0, 2)
  with pytest.raises(IndexError):
    m.obtener(-1, 0)

"""Coordenadas fuera de rango en asignar() debe lanzar IndexError"""
def test_Fuera_de_rangoAS_error():
  m = Matriz(2, 2)
  with pytest.raises(IndexError):
    m.asignar(2, 0, 5)
  with pytest.raises(IndexError):
    m.asignar(0, -1, 5)
  
