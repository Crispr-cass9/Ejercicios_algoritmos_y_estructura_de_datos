def romano_a_decimal(string):
    lista = list(string)
    if len(lista) == 0:
        return 0
    romano = lista.pop(0)
    print(romano, lista)

    if romano == 'M':
        return 1000 + romano_a_decimal(lista)
    
    elif romano == 'D':
        if len(lista) != 0 and lista[0] in 'M':
            return -500 + romano_a_decimal(lista)
        return 500 + romano_a_decimal(lista)

    elif romano == 'C':
        if len(lista) != 0 and lista[0] in 'DM':
            return -100 + romano_a_decimal(lista)
        return 100 + romano_a_decimal(lista)

    elif romano == 'L':
        if len(lista) != 0 and lista[0] in 'CDM':
            return -50 + romano_a_decimal(lista)
        return 50 + romano_a_decimal(lista)

    elif romano == 'X':
        if len(lista) != 0 and lista[0] in 'LCDM':
            return -10 + romano_a_decimal(lista)
        return 10 + romano_a_decimal(lista)

    elif romano == 'V':
        if len(lista) != 0 and lista[0] in 'XLCDM':
            return -5 + romano_a_decimal(lista)
        return 5 + romano_a_decimal(lista)

    elif romano == 'I':
        if len(lista) != 0 and lista[0] in 'VXLCDM':
            return -1 + romano_a_decimal(lista)
        return 1 + romano_a_decimal(lista)

print(romano_a_decimal('XLV'))