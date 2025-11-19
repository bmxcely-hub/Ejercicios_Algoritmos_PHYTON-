14. Contar vocales
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    total = 0
    for c in cadena:
        if c in vocales:
            total += 1
    return total
