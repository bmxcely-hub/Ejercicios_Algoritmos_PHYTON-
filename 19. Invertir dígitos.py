
def invertir_numero(n):
    signo = -1 if n < 0 else 1
    n = abs(n)
    invertido = int(str(n)[::-1])
    return signo * invertido
