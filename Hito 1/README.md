## Análisis de complejidad del arreglo dinámico 
La complejidad de las operaciones principales establecidas son:

- **Insertar un paciente:** O(1) amortizada, normalmente el paciente se agrega directamente al final del arreglo. Aunque cuando el arreglo se llena es necesario redimensionarlo

- **Redimensionar:** O(n) se crea un arreglo con doble capacidad y se copian los elementos existentes.

- **Obtener un paciente:** O(1) se accede directamente al paciente a trevés de su índice 

- **Eliminar paciente:** O(n) es necesario buscar el paciente por su ID y mover los elementos siguientes para ocupar el espacio disponible

## Medición del tiempo de inserción 
| Cantidad de pacientes | Tiempo de inserción (s) |
|---:|---:|
| 100 | 0.000248 |
| 500 | 0.000483 |
| 1.000 | 0.000839 |
| 2.000 | 0.001671 |
| 5.000 | 0.006505 |
| 10.000 | 0.009101 |

Estos resultados permiten observar cómo cambia el tiempo de inserción a medida que aumenta la cantidad de pacientes. Las variaciones se relacionan con las operaciones normales de inserción y con las redimensiones del arreglo cuando se alcanza su capacidad.
