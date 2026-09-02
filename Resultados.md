# Resultados

## Tabla de tiempos

| Contactos | Búsqueda binaria (µs) | Búsqueda lineal (µs) | Agregar y eliminar (µs) |
| --------: | --------------------: | -------------------: | ----------------------: |
|     1.000 |                  1,40 |                20,10 |                    3,30 |
|    10.000 |                  2,10 |               209,90 |                    8,60 |
|   100.000 |                  2,50 |            12423,00 |                   51,40 |

## Interpretación

* Al pasar de 10.000 a 100.000 contactos, el tiempo de la búsqueda binaria se multiplicó por 1,19, lo cual era de esperar porque su crecimiento es logarítmico y el tiempo aumenta muy poco al aumentar el tamaño de la agenda.
* Al pasar de 10.000 a 100.000 contactos, el tiempo de la búsqueda lineal se multiplicó por 59,18, lo cual era de esperar porque debe recorrer los contactos uno por uno y su tiempo aumenta con el tamaño de la agenda.
* Al pasar de 10.000 a 100.000 contactos, el tiempo de agregar y eliminar se multiplicó por 5,98, lo cual era de esperar porque estas operaciones pueden requerir recorrer o desplazar elementos de la agenda y su costo aumenta cuando hay más contactos.

## Medición

* **Computador:** ASUS VivoBook Go 15 E1504FA
* **Sistema operativo:** Windows
* **Versión de Python:** 3.14.7
