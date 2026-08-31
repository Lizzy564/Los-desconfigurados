from typing import List

class Agenda:
    """Agenda de contactos, ordenada por nombre alfabéticamente"""

    #Se crea la agenda vacia
    def __init__(self) -> None:
        """Crear una agenda vacía
        
        Complejidad: O(1)
        """

        #Se mantiene siempre lista de tuplas (nombre, telefono) ordenada.
        #Ordenada por nombre; de eso depende la busqueda binaria.
        self._contactos: List[tuple[str, str]] = []

        #Saber cuantos contactos hay en la agenda
    def __len__(self) -> int:
            """Devuelve la cantidad de contactos en la agenda
            
            Complejidad: O(1)
            """
            return len(self._contactos)
        
        #Busqueda binaria.
    def _buscar(self, nombre: str) -> tuple[int, bool]:
            """Busca un contacto por nombre en la agenda
            
            Devuelve una tupla (posicion, encontrado) donde:
                - posicion: es el índice donde se encuentra el contacto o donde debería insertarse.
                - encontrado: es True si el contacto fue encontrado, False en caso contrario.
            
            Complejidad: O(log n)
            """
            izquierda = 0
            derecha = len(self._contactos) - 1

            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                nombre_medio = self._contactos[medio][0]

                if nombre_medio == nombre:
                    return (medio, True)
                elif nombre_medio < nombre:
                    #Nombre buscado va mas a la derecha.
                    izquierda = medio + 1
                else:
                    #Nombre buscado va mas a la izquierda.
                    derecha = medio - 1
        #No se encontró: 'Izquierda' es la posición donde debería insertarse.
            return (izquierda, False)

        #Métodos públicos que usan _buscar para realizar operaciones en la agenda.  

    def contiene(self, nombre: str) -> bool:
            """Verifica si un contacto con el nombre dado existe en la agenda
            
            Complejidad: O(log n)
            """
            _, encontrado = self._buscar(nombre)
            return encontrado

    def telefono_de(self, nombre: str) -> str:
            """Devuelve el teléfono del contacto con el nombre dado
            
            Complejidad: O(log n)
            """
            posicion, encontrado = self._buscar(nombre)
            if not encontrado:
                raise KeyError(f"Contacto con nombre '{nombre}' no encontrado.")
            return self._contactos[posicion][1]

    def nombres(self) -> List[str]:
            """
            Devuelve una lista con todos los nombres de los contactos en orden alfabético
            
            Complejidad: O(n)
            """
            return [contacto[0] for contacto in self._contactos]

    def agregar(self, nombre: str, telefono: str) -> None:
        """
        Agrega un contacto a la agenda y en caso de que este exista lo actualiza
        
        complejidad: O(n)
        """
        if nombre == "":
            raise ValueError("El nombre del contacto no puede estar vacío.")
            #si el nombre esta vacio, se muestra el mensaje de ValueError

        posicion, encontrado = self._buscar(nombre)
        telefono = str(telefono)  
        #Asegurarse de que el teléfono sea una string

        if encontrado:
            #Si el contacto ya existe, actualizamos su teléfono
            self._contactos[posicion] = (nombre, telefono)
        else:
            #Si el contacto no existe, lo insertamos en la posición correcta
            self._contactos.insert(posicion, (nombre, telefono))

    def eliminar(self, nombre: str) -> None:
        """
        Elimina un contacto de la agenda por su nombre
        
        Complejidad: O(n)
        """
        posicion, encontrado = self._buscar(nombre)

        if not encontrado:
            raise KeyError(f"Contacto con nombre '{nombre}' no encontrado.")
            #Si el contacto no se encuentra, se muestra el mensaje de KeyError

        self._contactos.pop(posicion)
        #Si el contacto existe, se elimina de la agenda usando pop() para mantener el orden.
