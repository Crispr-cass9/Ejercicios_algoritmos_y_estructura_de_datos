def potencia(a,b):
    if b==1:
        return a
    #Caso exponente negativo
    if b<0:
        return 1/(a*potencia(a, abs(b)-1))
    return a * potencia(a, b-1)

print(potencia(-5, -4))
#--> 0.0016