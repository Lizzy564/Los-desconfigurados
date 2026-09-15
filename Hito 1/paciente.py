class Paciente:
    def __init__(self, id, edad, nivel_triage, hora_llegada, tiempo_espera = 0):
        self.id = id
        self.edad = edad
        self.nivel_triage = nivel_triage
        self.hora_llegada = hora_llegada 
        self.tiempo_espera = tiempo_espera
