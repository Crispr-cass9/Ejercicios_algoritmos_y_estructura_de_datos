def MCD(num1, num2):
    if num1%num2==0:
        return num2

    if num1>num2:
        return MCD(num2, num1%num2)
    
    return MCD(num1, num2%num1)

print(MCD(350,450))