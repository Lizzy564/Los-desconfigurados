1. Justificación de las estructuras de pilas y colas 

Las pilas siguen el principio LIFO (último en entrar, primero en salir), por lo que nos sirven para implementar la función deshacer acciones.

Las colas FIFO procesan los elementos en orden de llegada. Para ello, el proyecto utiliza ColaDinamica. Además, ColaPrioridadTriage organiza a los pacientes según su nivel de prioridad, respetando el orden de llegada entre pacientes del mismo nivel.

 2. Complejidad

- Pilas: Insertar y extraer elementos puedecostar O(1) según la implementación

- Cola FIFO: Encolar y desencolar cuesta O(1) si se utilizan referencias al inicio y al final 

- ColaPrioridadTriage: Insertar puede costar O(n) porque busca identificadores duplicados

- heapq: Insertar y extraer elementos cuesto O(\log n)

 3. Funcionamiento de la cola de prioridad

La cola distribuye los pacientes en cinco niveles de triage. Al solicitar el siguiente paciente, revisa primero el nivel de mayor prioridad y conserva el orden FIFO dentro de cada nivel. También permite retirar pacientes y reclasificarlos

Además, se comparó esta implementación con heapq, que organiza los elementos mediante un monticulo de prioridad 

 4. Resultados de los benchmarks 


