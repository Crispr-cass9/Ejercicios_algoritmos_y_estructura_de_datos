def revertir(string):
    print(string)
    if len(string) == 1:
        return string
    return revertir(string[1:]) + string[0] #Hacemos una rebanada que elimina el primer elemento para no repetirlo

print(revertir('mecanografía')) 