import time
import random

lista = [random.randint(0, 1000000) for x in range(1000000)]

inicio = time.time()

def bucket_sort(arr):
    # Crear una lista de cubetas
    buckets = [[] for _ in range(len(arr))]
    
    # Distribuir elementos en las cubetas
    for num in arr:
        index = int(num * len(buckets) / (max(arr) + 1))
        buckets[index].append(num)
    
    # Ordenar individualmente cada cubeta (puede utilizarse otro algoritmo de ordenación)
    for bucket in buckets:
        bucket.sort()
    
    # Concatenar las cubetas ordenadas para obtener el arreglo final
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Ejemplo de uso
sorted_arr = bucket_sort(lista)
print("Arreglo ordenado:", sorted_arr)

final = time.time()

print(final-inicio)
