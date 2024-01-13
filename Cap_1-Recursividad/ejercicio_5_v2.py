def romano_a_decimal(string):
    if not string:
        return 0
    
    valores = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    valor_decimal = valores[string[0]]
    
    if len(string) > 1 and valores[string[1]] > valor_decimal:
        return -valor_decimal + romano_a_decimal(string[1:])
    return valor_decimal + romano_a_decimal(string[1:])

print(romano_a_decimal('XLV'))