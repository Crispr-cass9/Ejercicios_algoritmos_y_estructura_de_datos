def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribuir elementos en los cubos
    for i in range(n):
        print(int(arr[i] * n), arr[i] * n)
        index = int(arr[i] * n)
        buckets[index].append(arr[i])

    # Ordenar individualmente cada cubo (puede utilizarse otro algoritmo de ordenación)
    for bucket in buckets:
        bucket.sort()

    # Concatenar los cubos ordenados para obtener el arreglo final
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

# Ejemplo de uso
arr = [0.8, 0.2, 0.6, 0.4, 0.9, 0.1, 0.7, 0.5, 0.3]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
