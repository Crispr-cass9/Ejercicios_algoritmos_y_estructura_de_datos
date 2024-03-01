def progresion(n):
    if n == 0:
        return 0
    print(2*(-3)**(n-1))
    return progresion(n-1)

print(progresion(8))

