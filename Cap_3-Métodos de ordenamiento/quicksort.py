def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    
    mayores = [x for x in lista[1:] if x >= pivote]
    menores = [x for x in lista[1:] if x < pivote]
    return quicksort(mayores) + [pivote] + quicksort(menores)

print(quicksort([12, 5, 3, 2, 20, 0, 13, 17, 19, 11, 10]))