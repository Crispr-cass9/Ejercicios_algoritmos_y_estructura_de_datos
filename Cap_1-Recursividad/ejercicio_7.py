def serie(n):
    if n == 0:
        return 'No puedes dividir por 0'
    elif n == 1:
        return n
    
    return 1/n + serie(n-1)
print(serie(4))
#-->2.08333333