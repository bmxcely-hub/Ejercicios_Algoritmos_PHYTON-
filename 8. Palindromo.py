9. Potencia sin **
def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado
