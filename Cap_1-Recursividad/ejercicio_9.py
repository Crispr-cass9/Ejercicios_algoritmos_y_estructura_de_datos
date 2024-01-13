def contar_digitos(n):
    #Antes de comprobar el caso base compruebo si es negativo ya que mi caso base interrumpirá la ejecución esperada en caso de que lo sea. 
    if n < 0:
        return 1 + contar_digitos(abs(n)/10) #Paso n a positivo
    
    if n/10<1:
        return 1
    return 1 + contar_digitos(n/10)

print(contar_digitos(-1234886234))
#--> 10