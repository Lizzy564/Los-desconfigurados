## Tabla de tiempos

|  Lado |    Celdas | Tiempo (s) | Factor respecto de la matriz anterior |
| ----: | --------: | ---------: | ------------------------------------: |
|   250 |    62.500 |  0,0013869 |                                     - |
|   500 |   250.000 |  0,0056774 |                                  4,09 |
| 1.000 | 1.000.000 |  0,0257294 |                                  4,53 |

## Interpretación

* Al duplicar el lado de la matriz de 250 a 500, el tiempo de ejecucuon de `suma()` se multiplico en un tiempo
Aproximado a 4,09.
* Al duplicar de 500 a 1.000, se multiplico en un tiempo aproximado a 4,53.

Este comportamiento era esperado porque `suma()` recorre todas las celdas de la matriz y su comlejidad es de
O(filas x columnas). Al duplicar el lado de una matriz cuadrada, la cantiidad de las celdas se multiplica por 4,
por lo cual se ve reflejado en el tiempo de ejecución el cual aumenta aproximadamente 4 veces.

## Entorno de medicion

* **Computador:** Lenovo IdeaPad 1 14IAU7
* **Sistema operativo:** Windows
* **Vesión de Python:** 3.14.7
