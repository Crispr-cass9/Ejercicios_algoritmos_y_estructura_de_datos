# Algoritmos de ordenamiento

### *Quick sort*

| Ámbito | Comportamiento |
| :----: | :------------- |
| **Peor caso** | n^2         |
| **Mejor caso** | n * log n  |
| **Análisis**   | Es un algoritmo recursivo sin embargo controla muy bien el uso de la pila por lo que es muy dificil alcanzar el desbordamiento de la pila de llamadas. |

**Complejidad de la Partición:**

La eficiencia del Quicksort está vinculada a la eficiencia del proceso de particionamiento, donde se selecciona un pivote y se reorganizan los elementos de manera que los elementos menores que el pivote estén a su izquierda y los mayores estén a su derecha. La complejidad de esta operación es O(n), donde n es la longitud del arreglo.

**Recursión:**

Después de la partición, el algoritmo se aplica recursivamente a los subarreglos resultantes. Cada llamada recursiva divide el arreglo en subarreglos más pequeños, y cada nivel de la recursión contribuye con un factor logarítmico a la complejidad total. El número total de niveles de recursión es 
log2(n), donde n es la longitud del arreglo.

**Combinación:**

La combinación de los resultados de los subarreglos no contribuye significativamente a la complejidad total. La combinación se realiza en el nivel superior de la recursión y solo implica la concatenación de los subarreglos.
 

