18. Contar carácter
def contar_caracter(cadena, caracter):
    total = 0
    for c in cadena:
        if c == caracter:
            total += 1
    return total
