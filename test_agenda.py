from.agenda import Agenda 
import pytest

def test_agenda_vacia():
  agenda = Agenda()
  assert len(agenda) == 0

def test_agregar_y_contiene():
  agenda = Agenda()
  agenda.agregar("Lore", "3001234567")
  assert agenda.contiene("Lore") is true 

def test_telefono_de():
  agenda = Agenda()

  agenda.agregar("Lore", "3001234567")
  assert agenda.telefono_de("Lore") == "3001234567"

def test_nombres_ordenados():
  agenda = Agenda()
  
  agenda.agregar("María", "3115462494")
  agenda.agregar("Juan", "3124568530")
  agenda.agregar("Lore", "3203546894")
  assert agenda.nombres() == ["Juan", "Lore", "María"]

def test_telefono_de_nombre_inexistente():
  agenda = Agenda()
  agenda.agregar("Lore", "3001234567")
  
  with pytest.raises(KeyError):
    agenda.telefono_de("Carlos")

def test_eliminar_contacto():
  agenda = Agenda()
  
  agenda.agregar("Lore", "3001234567")
  agenda.eliminar("Lore")
  assert agenda.contiene("Lore") is False 

def test_eliminar_nombre_inexistente():
  agenda = Agenda()
  agenda.agregar("Lore", "3001234567")

  with pytest.raises(KeyError):
    agenda.eliminar("Carlos")

def test_agregar_nombre_vacio():
  agenda = Agenda()
  with pytest.raises(ValueError):
    agenda.agregar("", "3001234567")

def test_agregar_nombre_repetido_actualiza_telefono():
  agenda = Agenda()
  agenda.agregar("Lore", "3001234567")
  cantidad_inicial = len(agenda)
  
  agenda.agregar("Lore", "3119876543")
  assert len(agenda) == cantidad_inicial
  assert agenda.telefono_de("Lore") == "3119876543"

def test_nombres_mayusculas_y_tildes():
  agenda = Agenda()
  agenda.agregar("ana", "3001111111")
  agenda.agregar("Ana", "3002222222")
  agenda.agregar("Ána", "3003333333")
  
  assert agenda.nombres() == ["Ana", "ana", "Ána"]

def test_nombres_lista_independiente():
  agenda = Agenda()
  agenda.agregar("Lore", "3001234567")
  agenda.agregar("Carlos", "3119876543")
  
  nombres = agenda.nombres()
  nombres.append("Ana")
  
  assert agenda.nombres() == ["Carlos", "Lore"]
