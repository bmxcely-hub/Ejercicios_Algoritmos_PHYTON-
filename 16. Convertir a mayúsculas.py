16. Convertir a mayúsculas sin .upper()
def a_mayusculas(cadena):
    resultado = ""
    for c in cadena:
        if 'a' <= c <= 'z':
            resultado += chr(ord(c) - 32)
        else:
            resultado += c
    return resultado
