'''
Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
número dado
'''
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7)) 
#-->13

'''
Notas de Cristian:
Este algoritmo es extremadamente lento, de hecho no intenten probarlo con un valor como 80 o estarán una eternidad.
La razón de esta lentitud es la cantidad de veces que repetimos operaciones que ya hemos realizado, he encontrado un paper que
lo explica por lo que les dejo esta bonita imagen de aca
'''

def fibonacci2(n):
    if n == 0 or n == 1:
        return n
    a = 1
    b = 1
    for i in range(n-2): #n-2 porque los primeros 2 casos los tomamos en el if anterior
        a, b = b, a+b
    return b

print(fibonacci2(80))
#--> 23416728348467685