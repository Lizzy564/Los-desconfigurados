from arreglo_dinamico import ArregloDinamico
from Ordenamientos import (ordenar_por_id, ordenar_por_triage_y_hora, ordenar_por_tiempo_espera)
from busqueda_binaria import busqueda_binaria
from matriz_camas import crear_matriz

RUTA_CENSO = "censo_5000.csv"

def mostrar_pacientes(censo, cantidad=10, triage=None):
    mostrados = 0

    for i in range(censo.longitud()):
        paciente = censo.obtener(i)

        if triage is not None:
            if str(paciente.nivel_triage) != str(triage):
                continue

        print(
            f"{mostrados + 1}. "
            f"ID: {paciente.id} | "
            f"Edad: {paciente.edad} | "
            f"Triage: {paciente.nivel_triage} | "
            f"Llegada: {paciente.hora_llegada}"
        )

        mostrados += 1

        if cantidad is not None and mostrados == cantidad:
            break

    if mostrados == 0:
        print("No se encontraron pacientes")


def main():
    censo = ArregloDinamico()

    try:
        censo.cargar_censo_desde_csv(RUTA_CENSO)
    except FileNotFoundError:
        print(f"No se encontró el archivo {RUTA_CENSO}.")
        return

    censo_por_id = ordenar_por_id(censo)
    matriz = crear_matriz(3, 10)

    print(f"Censo cargado: {censo.longitud()} pacientes")

    while True:
        print(""" MENÚ
1. Buscar paciente por ID
2. Ordenar y filtrar por triage
3. Ordenar por tiempo de espera
4. Ocupar cama
5. Liberar cama
6. Consultar camas disponibles
7. Reporte de camas
8. Salir """)

        opcion = input("Opción: ")

        try:
            if opcion == "1":
                id_buscado = int(input("ID a buscar: "))
                paciente = buscar_binaria(
                    censo_por_id,
                    id_buscado
                )

                if paciente is None:
                    print("Paciente no encontrado.")
                else:
                    print(
                        f"ID: {paciente.id} | "
                        f"Edad: {paciente.edad} | "
                        f"Triage: {paciente.nivel_triage} | "
                        f"Llegada: {paciente.hora_llegada}"
                    )

            elif opcion == "2":
                ordenado = ordenar_por_triage_y_hora(censo)

                nivel = input(
                    "Elige el nivel de triage o 'todos': ").strip()
                triage = None if nivel.lower() == "todos" else int(nivel)

                cantidad = input(
                    "Cantidad (Enter=10, 0=todos): ").strip()

                cantidad = (
                    10 if cantidad == ""
                    else None if int(cantidad) == 0
                    else int(cantidad)
                )

                mostrar_pacientes(ordenado, cantidad, triage)

            elif opcion == "3":
                hora = float(input("Hora actual en minutos: "))

                ordenado = ordenar_por_tiempo_espera(censo, hora)

                mostrar_pacientes(ordenado)

            elif opcion == "4":
                cama = int(input("Cama: "))
                turno = int(input("Turno: "))

                matriz.ocupar(cama, turno)
                print("Esta cama ha sido ocupada")

            elif opcion == "5":
                cama = int(input("Cama: "))
                turno = int(input("Turno: "))

                matriz.liberar(cama, turno)
                print("Esta cama ha sido liberada")

            elif opcion == "6":
                turno = int(input("Turno: "))

                print("Camas libres:", matriz.consultar_disponibilidad(turno))

            elif opcion == "7":
                for reporte in matriz.reporte_ocupacion():
                    print(
                        f"Turno {reporte['turno']}: "
                        f"Ocupadas={reporte['ocupadas']}, "
                        f"Libres={reporte['libres']}, "
                        f"Total={reporte['total']}"
                    )

            elif opcion == "8":
                print("Saliendo...")
                break

            else:
                print("Opción no válida.")

        except (ValueError, TypeError, IndexError) as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()

