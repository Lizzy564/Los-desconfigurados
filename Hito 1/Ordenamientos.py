from arreglo_dinamico import ArregloDinamico


"""Dice que valor comparar Complejidad: O(n log n)"""
def mergesort(arreglo, clave):
    if arreglo.longitud() <= 1:
        return arreglo

    medio = arreglo.longitud() // 2

    izquierda = ArregloDinamico()
    derecha = ArregloDinamico()

    for i in range(medio):
        izquierda.insertar(arreglo.obtener(i))

    for i in range(medio, arreglo.longitud()):
        derecha.insertar(arreglo.obtener(i))

    izquierda = mergesort(izquierda, clave)
    derecha = mergesort(derecha, clave)

    return mezclar(izquierda, derecha, clave)


"""Mezcla dos arreglos ordenados Complejidad: O(n)"""
def mezclar(izquierda, derecha, clave):
    resultado = ArregloDinamico()

    i = 0
    j = 0

    while i < izquierda.longitud() and j < derecha.longitud():
        if clave(izquierda.obtener(i)) <= clave(derecha.obtener(j)):
            resultado.insertar(izquierda.obtener(i))
            i += 1
        else:
            resultado.insertar(derecha.obtener(j))
            j += 1

    while i < izquierda.longitud():
        resultado.insertar(izquierda.obtener(i))
        i += 1

    while j < derecha.longitud():
        resultado.insertar(derecha.obtener(j))
        j += 1

    return resultado


"""Ordenamiento por inserción Complejidad: O(n²)"""
def insertion_sort(arreglo, clave):
    resultado = ArregloDinamico()

    for i in range(arreglo.longitud()):
        resultado.insertar(arreglo.obtener(i))

    for i in range(1, resultado.longitud()):
        elemento_actual = resultado.obtener(i)
        j = i - 1

        while j >= 0 and clave(resultado.obtener(j)) > clave(elemento_actual):
            resultado.datos[j + 1] = resultado.obtener(j)
            j -= 1

        resultado.datos[j + 1] = elemento_actual

    return resultado


NIVELES_TRIAGE = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5
}


"""Convierte el nivel de triage a número Complejidad: O(1)"""
def nivel_a_numero(nivel):
    nivel = str(nivel).strip().upper()

    if nivel in NIVELES_TRIAGE:
        return NIVELES_TRIAGE[nivel]

    return int(nivel)


"""Convierte una hora a minutos Complejidad: O(1)"""
def hora_a_minutos(hora):
    horas, minutos = hora.strip().split(":")

    return int(horas) * 60 + int(minutos)


"""Ordena por nivel de triage y hora de llegada Complejidad: O(n log n)"""
def ordenar_por_triage_y_hora(censo):
    def clave(paciente):
        nivel = nivel_a_numero(paciente.nivel_triage)
        return (nivel, paciente.hora_llegada)

    if censo.longitud() > 30:
        return mergesort(censo, clave)

    return insertion_sort(censo, clave)


"""Ordena por tiempo de espera"""
def ordenar_por_tiempo_espera(censo, hora_actual):
    def clave(paciente):
        tiempo_espera = hora_actual - paciente.hora_llegada
        return -tiempo_espera

    if censo.longitud() > 30:
        return mergesort(censo, clave)

    return insertion_sort(censo, clave)


"""Ordena por ID"""
def ordenar_por_id(censo):
    def clave(paciente):
        return paciente.id

    if censo.longitud() > 30:
        return mergesort(censo, clave)

    return insertion_sort(censo, clave)
