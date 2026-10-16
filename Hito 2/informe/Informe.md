**Contexto y alcance**

El sistema de urgencias hospitalarias gestiona la admisión, clasificación y atención priorizada de pacientes evaluados según cinco niveles de gravedad  \[Nivel I (criticó) a Nivel V (No urgente)\].

Estructura arquitectónica: el sistema se construyó bajo una arquitectura en capas desacoplada. la interfaz gráfica interactua exclusivamente con la fachada [Sistema.py](http://Sistema.py). Ningún componente visual importa ni manipula listas, pilas o colas de manera directa.

**Refactorización**

| \# | Retroalimentación | Cambios Realizados |
| :---- | :---- | :---- |
| 1 | La sala de espera ordenaba todo el censo mediante ordenar\_por triage\_y\_hora en cada consulta (O(n log n)) | se reemplazó por ColaPrioridadTriage con 5 cubetas FIFO fijos. la inserción de pacientes pasa a ser O(1). |
| 2 | inconsistencia de nombres e importaciones | estandarización completa a convenciones snake\_case y clases en PascalCase |
| 3 | el modelo Paciente solo contenia id, edad, nivel\_triage y hora\_llegada, sin datos clinicos ni motivo | Extension de la dataclass Paciente agregando nombre, documento (usando como ID unico) y motivo de consulta |
| 4 | la funcion busqueda binaria valida el ordenamiento en cada ejecucución llamando a esta\_ordenado\_por\_id (O(n)) | elimina la busqueda binaria sobre arreglos. Busqueda puntual O(1) usando el indice hash \_indice en registro pacientes |
| 5 | la gestión de camillas usaba matriz sobre lista nativa de python | remplazada por ColaCircularEstatica de capacidad fija con puntero circulares frente y final O(1) |
| 6 | estructura de archivos plana en una sola carpeta | reorganización en capas nucleo/, pruebas/, berchmark/ |

**Algoritmo Recursivo e iterativo**

La clasificación de un paciente en triaje sigue un cuestionario de preguntas dicotómicas (Si/No). La estructura lógica subyacente es un árbol binario donde cada nodo interno contiene una pregunta y cada hoja representa un Nivel asignado.

* Caso base: el nodo actual es una hoja (nodo.nivel is not None), se retorna el Nivel.  
* Paso Recursivo: se consume la respuesta del usuario (respuesta.pop(0)), si es True, se evalúa de forma recursiva [nodo.si](http://nodo.si); si es False, se evalúa nodo.no.

Interativa con PilaEstatica para mitigar la dependencia de la pila de llamadas nativa de python (Call stacks), se implementó clasificar\_interativo utilizando la clase PilaEstatica desarrollada en el proyecto.

Profundidad real Vs. Límite de Recursión

**Árbol clínico real:** un cuestionario de triaje médico estandarizado posee una profundidad máxima de $h\ ∊\ [5,\ 10]$ preguntas. Cada llamada recursiva consume un marco de pila. Ocupar 10 marcos sobre un límite de 1000 representa menos del 1% de la capacidad de la pila de python, lo que demuestra que la función recursiva clasificar() es completamente segura en producción.

**Caso extremo:** en la prueba se construyó un árbol degenerado de profundidad 1100 \> límite de python. La ejecución falló arrojando RecursionError. En contraste, la versión iterativa clasificar\_iterativo() procesó el árbol exitosamente gracias a que la memoria de la PilaEstatica reside en el Heap de la aplicación, evitando la saturación del intérprete.

**Tabla de reparto interno del trabajo**

| Integrantes | Requerimiento solicitado | % aprox. |
| ----- | ----- | ----- |
| Faisury | ListaSimple, ListaDoble, RegistroPacientes, bench\_listas.py. | 25% |
| Lorena | PilaEstatica, PilaDinamica, ColaCircularEstatica, ColaDinamica, ColaPrioridadTriage, GestorDeshacer, bench\_colas.py, prueba de listas. | 25% |
| Camilo | Modelos de dominio (dominio.py), árbol recursivo/iterativo (arbol\_triage.py), fachada (sistema.py), pruebas de pilas/colas (test\_pilas\_colas.py), automatización CI (pruebas.yml) y refactorización . | 25% |
| Liceth | Interfaz grafica (Figma) de 7 pantallas, pruebas del núcleo.  | 25% |

