

try:
    print("--- Verificación de Intervalo Cerrado ---")
    minimo_valor = int(input("Ingrese el límite mínimo del intervalo: "))
    maximo_valor = int(input("Ingrese el límite máximo del intervalo: "))
    x = int(input("Ingrese el número entero (x) a verificar: "))


    if minimo_valor > maximo_valor:
        print("Advertencia: El mínimo es mayor que el máximo. Intercambiando valores.")
        minimo_valor, maximo_valor = maximo_valor, minimo_valor


    if x >= minimo_valor and x <= maximo_valor:
        resultado = "dentro"
        mensaje = "El número {} se encuentra **DENTRO** del intervalo [{}, {}]. ✅".format(x, minimo_valor, maximo_valor)
    else:
        resultado = "fuera"
        mensaje = "El número {} se encuentra **FUERA** del intervalo [{}, {}]. ❌".format(x, minimo_valor, maximo_valor)


    print("\n--- Resultado ---")
    print(mensaje)

except ValueError:
    print("Error: Ingrese solo números enteros válidos.")