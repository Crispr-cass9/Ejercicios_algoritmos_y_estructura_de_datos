def multiplicacion(a,b):
    if b==1 or b == -1:
        return a
    #Caso en que sea negativo, multiplico por -1 y llamo a la misma función como si fuera poitiva
    if b < 0: 
        return -1*(a + multiplicacion(a, abs(b)-1))

    return a + multiplicacion(a, b-1)

print(multiplicacion(-5, -4))
#--> 20