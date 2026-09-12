import csv
import random 

ruta = "Hito 1/censo_5000.csv"
tiempo_actual = 0

with open(ruta, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)

    #Encabezados
    escritor.writerow(["id", "edad", "nivel_triage", "hora_llegada"])
    
    #Generar 5.000 pacientes
    for i in range(5000):
        intervalo = random.expovariate(1)
        tiempo_actual += intervalo

        id_paciente = 1000000001 + i
        edad = random.randint(1, 100)
        nivel_triage = random.randint(1, 5)

        escritor.writerow([id_paciente,
         edad, 
         nivel_triage,
         round(tiempo_actual, 2)
        ])

print("El censo fue generado correctamente.")
print("La cantidad de pacientes es: 5000")