import ctypes
from paciente import Paciente

class ArregloDinamico:
  def __init__(self, capacidad_inicial=10):
    self.capacidad = capacidad_inicial
    self.tamano = 0
    self.datos = (ctypes.py_object * self.capacidad)()

  def insertar(self, paciente):
    if self.tamano == self.capacidad:
        self.redimensionar()
    self.datos[self.tamano] = paciente 
    self.tamano += 1

  def redimensionar(self):
    new_capacidad = self.capacidad * 2
    new_datos = (ctypes.py_object * self.capacidad)()
    
    for i in range(self.tamano):
        new_datos[i] = self.datos[i]

    self.datos = new_datos
    self.capacidad = new_capacidad

  def obtener(self, indice):
      if indice < o or indice >= self.tamano:
          raise IndexError("Índice fuera de rango")

      return self.datos[indice]
    
  def longitud(self):
      return self.tamano
 
  def eliminar(self, id):
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




