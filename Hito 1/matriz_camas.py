class matriz_camas:
    def __init__(self, n_turnos, n_camas):
        """
        Crea una matriz con todas las camas estando libres.
        La matriz se organiza de la siguiente manera:
        - Filas: turno.
        - Columnas: camas.

        Complejidad: O(n_turnos * n_camas).
        """
        if n_turnos <= 0 or n_camas <= 0:
            raise ValueError("El numero de turnos y camas deben ser mayores que 0")
        
        self.n_turnos = n_turnos
        self.n_camas = n_camas
        self._matriz = [[0 for _ in range(n_camas)] for _ in range(n_turnos)]

    def _validar_turno(self, turno):
        """
        Verifica que el indice del turno sea valido.

        Complejidad: O(1).
        """
        if not isinstance(turno, int):
            raise TypeError("El turno debe ser un entero")

        if turno < 0 or turno >= self.n_turnos:
            raise IndexError("Turno fuera del limite")

    def _validar_cama(self, cama):
        """
        Verifica que el indice del turno sea valido.

        Complejidad: O(1).
        """
        if not isinstance(cama, int):
            raise TypeError("La Cama debe ser un entero")

        if cama< 0 or cama >= self.n_camas:
            raise IndexError("Cama fuera del limite")
        
    def ocupar(self, cama, turno)->None:
        """
        Ocupar una cama en un turno determinado.
        Usa los condicionales de la funcion _validar_indices con los paramnetros:
        - Cama: indice de la cama.
        - Turno: indice del turno.

        Complejidad: O(1).
        """
        self._validar_turno(turno)
        self._validar_cama(cama)

        if self._matriz[turno][cama] == 1:
            raise ValueError(f"La cama {cama} ya se encunentra ocupada en el turno {turno}")
        self._matriz[turno][cama] = 1

    def liberar(self, cama, turno)->None:
        """
        Libera una cama en un turno determinado.
        Usa los condicionales de la funcion _validar_indices con los paramnetros:
        - Cama: indice de la cama.
        - Turno: indice del turno.
        
        Complejidad: O(1).
        """
        self._validar_turno(turno)
        self._validar_cama(cama)

        if self._matriz[turno][cama] == 0:
            raise ValueError(f"La cama {cama} ya se encuentra libre en el turno {turno}")
        self._matriz[turno][cama] = 0

    def consultar_disponibilidad(self, turno)->list:
        """
        Devuelve una lista con los indices de la cama libres en el turno indicado.

        Complejidad: O(n_camas).
        """
        self._validar_turno(turno)

        disponibles = []

        for cama in range(self.n_camas):
            if self._matriz[turno][cama] == 0:
                disponibles.append(cama)

        return disponibles

    def reporte_ocupacion(self)-> dict:
        """
        Para construir el resumen por turnos.

        O(n_turnos * n_camas): Obligatoriamete recorre toda la matriz, debido a que tiene
        un for que reccore turnos y otro for que recorre las camas. asi que por cada turno
        revisa todas las camas.
        """
        reporte = []
        for turno in range(self.n_turnos):
            ocupadas = 0

            for cama in range(self.n_camas):
                if self._matriz[turno][cama] == 1:
                    ocupadas += 1

            libres = self.n_camas - ocupadas

            reporte.append({
                "turno": turno, "ocupadas": ocupadas, "libres": libres, "total": self.n_camas})

        return reporte

    def __repr__(self):
        return repr(self._matriz)

def crear_matriz(n_turnos, n_camas):
    return matriz_camas(n_turnos, n_camas)
