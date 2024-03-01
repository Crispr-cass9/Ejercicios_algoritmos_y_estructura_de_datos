import time
import random

lista = [random.randint(0, 1000000) for x in range(10000000)]
maximo = max(lista)

inicio = time.time()



def countsort(lista, maximo):
    lista_intermedia = [0] * (maximo + 1)
    lista_ordenada = [None] * len(lista)

    for elemento in lista:
        lista_intermedia[elemento] += 1
    

    total = 0

    for i in range(len(lista_intermedia)):
        lista_intermedia[i], total = total, total + lista_intermedia[i]

    for indice in lista:
        lista_ordenada[lista_intermedia[indice]] = indice
        lista_intermedia[indice] += 1
    return lista_ordenada


print(countsort(lista, maximo))

final = time.time()

print(final-inicio)