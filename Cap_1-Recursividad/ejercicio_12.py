'''
En este caso reutilicé el algoritmo del MCD porque la fórmula del MCM es la misma pero con una formula en un inicio, he creado otro argumento que se llama fórmula, esta sólo se aplicará sólo una vez en el código al inicio para calcular el MCM
'''

def MCM(num1, num2, formula):
    if num1%num2==0:
        return num2

    if num1>num2:
        if not formula:
            return (num1*num2)//MCM(num2, num1%num2, True)
        return(MCM(num2, num1%num2, True))
    if not formula:
        return (num1*num2)//MCM(num1, num2%num1, True)
    return MCM(num1, num2%num1, True)

print(MCM(350,450, False))