13. Número mayor en una lista
def mayor_lista(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor
