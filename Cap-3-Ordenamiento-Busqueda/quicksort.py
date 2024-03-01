import time
import random

lista = [random.randint(0, 1000000) for x in range(10000000)]
maximo = max(lista)

inicio = time.time()

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    
    mayores = [x for x in lista[1:] if x >= pivote]
    menores = [x for x in lista[1:] if x < pivote]
    return quicksort(mayores) + [pivote] + quicksort(menores)

print(quicksort(lista))

final = time.time()

print(final-inicio)