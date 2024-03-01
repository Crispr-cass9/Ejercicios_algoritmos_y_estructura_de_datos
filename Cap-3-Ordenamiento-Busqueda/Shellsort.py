def shellsort(lista):
    n = len(lista)
    intervalo = 5

    while intervalo>0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j>= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j-intervalo]
                j = j - intervalo
            lista[j] = temp
        intervalo = intervalo//2
    return lista

print(shellsort([0,7,2,5,10,24,15,19,1]))