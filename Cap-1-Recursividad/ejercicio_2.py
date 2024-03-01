'''
Suma el primer numero y vuelve a llamarse pero restando 1, cuando n sea igual a 1 se finaliza la recursividad
'''

def sumatoria(n):
    if n == 0:
        return 0

    if n<0: #Para el caso en que n sea negativo
        print(n)
        return n + sumatoria(n+1)

    return n + sumatoria(n-1) 

print(sumatoria(-10))