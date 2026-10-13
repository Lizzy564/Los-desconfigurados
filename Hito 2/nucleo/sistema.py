from nucleo.dominio import Paciente, Nivel, SignosVitales

class SistemaUrgencias:

    def __init__(self):
        """Inicializa el sistema de urgencias"""
        pass

    def registrar_paciente(
        self,
        nombre,
        documento,
        edad,
        motivo,
        nivel=None,
        respuesta=None) -> Paciente:
        """
        Registra un paciente en el sistema
        
        Si no se proporciona nivel, puede
        utilizar las respuestas del cuestionario de triage

        Retorna: Paciente registrado
        """

    def iniciar_cuestionario(self):
        """
        Inicia el cuestionario de triage

        Retorna: Pregunta inicial
        """
        raise NotImplementedError

    def responder(self, sesion, si: bool):
        """
        Responde una pregunta del cuestionario

        Retorna: Siguiente pregunta o nivel de triage
        """
        raise NotImplementedError

    def llamar_siguiente(self):
        """
        Obtiene el siguiente paciente según la prioridad de triage

        Retorna: Paciente o None
        """
        raise NotImplementedError

    def dar_alta(self, id, motivo):
        """
        Da de alta, traslada o registra el abandono de un paciente
        """
        raise NotImplementedError

    def reclasificar(self, id, nuevo_nivel, justificacion):
        """
        Cambia el nivel de triage de un paciente
        """
        raise NotImplementedError

    def registrar_signos(self, id, signos):
        """
        Registra una medición de signos vitales
        """
        raise NotImplementedError

    def historial(self, id) -> list[SignosVitales]:
        """
        Retorna el historial de signos vitales del paciente
        """
        raise NotImplementedError

    def en_espera(self, nivel=None) -> list[Paciente]:
        """
        Retorna los pacientes que están en espera

        Si se proporciona nivel, filtra por dicho nivel
        """
        raise NotImplementedError

    def buscar(self, texto) -> list[Paciente]:
        """
        Busca pacientes utilizando un texto
        """
        raise NotImplementedError

    def deshacer(self):
        """
        Deshace la última acción reversible

        Retorna: Descripción de la acción deshecha o None
        """
        raise NotImplementedError

    def ingresar_ambulancia(self, datos) -> bool:
        """
        Registra una ambulancia en la cola circular

        Retorna: False si la cola está llena
        """
        raise NotImplementedError

    def camillas(self):
        """
        Retorna la cantidad de camillas ocupadas y el total

        Retorna: Tupla (ocupadas, total)
        """
        raise NotImplementedError

    def metricas(self):
        """
        Retorna métricas generales del sistema

        Retorna: Diccionario con conteo por nivel, espera media y pacientes vencidos
        """
        raise NotImplementedError

    def snapshot_estructuras(self):
        """
        Retorna un resumen de las estructuras utilizadas
        por el sistema
        """
        raise NotImplementedError