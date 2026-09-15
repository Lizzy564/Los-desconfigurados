#Algoritmo Mergesort


"""Dice que valor comparar
Complejidad: O(n log n)"""
def mergesort(lista, clave):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio], clave)
    derecha = mergesort(lista[medio:], clave)

    return mezclar(izquierda, derecha, clave) 

"""Une dos listas en una sola ordenada"""

def mezclar(izquierda, derecha, clave):
    resultado =[]
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if clave(izquierda[i]) <= clave(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar lo que sobro
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

#Algoritmo InsertionSort

"""Ordenar por inserción
Complejidad: O(n) si ya está ordenado, O(n^2) si está desordenado"""

def insertion_sort(lista, clave):
    lista = lista.copy()  # Crear una copia de la lista para no modificar la original

    for i in range(1, len(lista)):
        elemento_actual = lista[i]
        j = i - 1

        while j >= 0 and clave(lista[j]) > clave(elemento_actual):
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = elemento_actual
    return lista

#funciones para convertir triage y hora en valores comparables

NIVELES_TRIAGE = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}

"""Convierte el nivel de triage a un valor numérico """

def nivel_a_numero(nivel):
    nivel = str(nivel).strip().upper()

    if nivel in NIVELES_TRIAGE:
        return NIVELES_TRIAGE[nivel]
    return int(nivel)  # Si no es un nivel válido, intenta convertirlo a entero

"""Convierte una hora en formato 'HH:MM' a minutos desde la medianoche."""
def hora_a_minutos(hora):
    horas, minutos = hora.strip().split(":")
    return int(horas) * 60 + int(minutos)

#Funciones de la guia
"""Ordena la lista de pacientes primero por nivel de triage y luego por hora de llegada."""
def ordenar_por_triage_y_hora(censo):
    def clave(paciente):
        nivel = nivel_a_numero(paciente.nivel_triage)
        return (nivel, paciente.hora_llegada)  
    

    if len(censo) > 30:
        return mergesort(censo, clave)
    else:
        return insertion_sort(censo, clave)
    
"""Ordena el censo de mayor a menor tiempo de espera."""
def ordenar_por_tiempo_espera(censo, hora_actual):
        def clave(paciente):
            tiempo_espera = hora_actual - paciente.hora_llegada
            return -tiempo_espera  # Se pone negativo para ordenar de mayor a menor

        if len(censo) > 30:
            return mergesort(censo, clave)
        else:
            return insertion_sort(censo, clave)

"""Ordena el censo por ID"""
def ordenar_por_id(censo):
    def clave(paciente):
        return paciente.id

    if len(censo) > 30:
        return mergesort(censo, clave)
    else:
        return insertion_sort(censo, clave)
