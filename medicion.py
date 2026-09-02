import random
import string
import time
from agenda import Agenda


random.seed(11)

repeticiones = 7
tamaño_nombre = 10

def generar_nombres(cantidad: int) -> list[str]:
    """Genera una cantidad exacta de nombres aleatorios de 10 letras"""

    nombres_generados: dict[str, bool] = {}

    while len(nombres_generados) < cantidad:
        nombre = "".join(random.choices(string.ascii_lowercase, k=tamaño_nombre))

    
        if nombres_generados.get(nombre) is None:
            nombres_generados[nombre] = True

    return sorted(nombres_generados.keys())

def crear_agenda(cantidad: int) -> Agenda:
    """Crea una agenda con la cantidad indicada de contactos."""
    agenda = Agenda()
    nombres = generar_nombres(cantidad)

    for nombre in nombres:
        agenda.agregar(nombre, "3000000000")

    return agenda

def busqueda_lineal(nombres: list[str], nombre_buscado: str) -> bool:
    """Busca un nombre recorriendo la lista uno por uno."""
    for nombre in nombres:
        if nombre == nombre_buscado:
            return True
    return False

def medir_busqueda_binaria(agenda: Agenda, nombre_buscado: str) -> float:
    """Mide contiene() y devuelve el mejor tiempo en microsegundos."""
    mejores_tiempos = []

    for _ in range(repeticiones):
        inicio = time.perf_counter_ns()
        agenda.contiene(nombre_buscado)
        fin = time.perf_counter_ns()

        mejores_tiempos.append((fin - inicio) / 1000)

    return min(mejores_tiempos)

def medir_busqueda_lineal(
    nombres: list[str], nombre_buscado: str
) -> float:
    """Mide la búsqueda uno por uno y devuelve el mejor tiempo en microsegundos."""
    mejores_tiempos = []

    for _ in range(repeticiones):
        inicio = time.perf_counter_ns()
        busqueda_lineal(nombres, nombre_buscado)
        fin = time.perf_counter_ns()

        mejores_tiempos.append((fin - inicio) / 1000)

    return min(mejores_tiempos)


def medir_agregar_y_eliminar(agenda: Agenda) -> float:
    """Mide agregar al principio y eliminar después. Devuelve el mejor tiempo del par agregar + eliminar,
    en microsegundos."""
    mejores_tiempos = []

    nombre_nuevo = "CCCCCCCCCC"
    telefono = "50000000000"

    for _ in range(repeticiones):
        inicio = time.perf_counter_ns()

        agenda.agregar(nombre_nuevo, telefono)
        agenda.eliminar(nombre_nuevo)

        fin = time.perf_counter_ns()

        mejores_tiempos.append((fin - inicio) / 1000)

    return min(mejores_tiempos)


def main() -> None:
    tamaños = [1000, 10000, 100000]
    resultados = []

    for cantidad in tamaños:
        print(f"Creando agenda de {cantidad:,} contactos...")
        agenda = crear_agenda(cantidad)

        nombres = agenda.nombres()

        nombre_buscado = "ABCDEFGHIJ"

        tiempo_binario = medir_busqueda_binaria(
            agenda, nombre_buscado
        )
        tiempo_lineal = medir_busqueda_lineal(
            nombres, nombre_buscado
        )
        tiempo_agregar = medir_agregar_y_eliminar(agenda)

        resultados.append(
            (
                cantidad,
                tiempo_binario,
                tiempo_lineal,
                tiempo_agregar,
            )
        )

        print(f"  Búsqueda binaria: {tiempo_binario:.2f} µs")
        print(f"  Búsqueda lineal:  {tiempo_lineal:.2f} µs")
        print(f"  Agregar + eliminar: {tiempo_agregar:.2f} µs")
        print()

    print("TABLA DE RESULTADOS")
    print()
    print("| Contactos  | Búsqueda binaria     | Búsqueda lineal     | Agregar + eliminar   |")
    print("|            | (µs)                 | (µs)                | (µs)                 |")
    print("+------------+----------------------+---------------------+----------------------+")

    for cantidad, binaria, lineal, agregar in resultados:
        cantidad_formateada = f"{cantidad:,}".replace(",", ".")
        binaria_formateada = f"{binaria:.2f}".replace(".", ",")
        lineal_formateada = f"{lineal:.2f}".replace(".", ",")
        agregar_formateada = f"{agregar:.2f}".replace(".", ",")
        
        print(
            f"| {cantidad_formateada:<10} "
            f"| {binaria_formateada:<20} "
            f"| {lineal_formateada:<19} "
            f"| {agregar_formateada:<20} |"
    )

if __name__ == "__main__":
    main()
