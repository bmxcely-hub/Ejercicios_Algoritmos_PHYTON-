

try:
    print("--- Verificación de Tres Intervalos Abiertos ---")

    x = int(input("Ingrese el número entero (x) a verificar: "))

    # Ingreso de los límites de los tres intervalos (a, b), (c, d), (e, f)
    a = int(input("Límite inferior del Intervalo 1: "))
    b = int(input("Límite superior del Intervalo 1: "))
    c = int(input("Límite inferior del Intervalo 2: "))
    d = int(input("Límite superior del Intervalo 2: "))
    e = int(input("Límite inferior del Intervalo 3: "))
    f = int(input("Límite superior del Intervalo 3: "))


    esta_en_intervalo_1 = (x > a and x < b)


    esta_en_intervalo_2 = (x > c and x < d)


    esta_en_intervalo_3 = (x > e and x < f)


    if esta_en_intervalo_1 or esta_en_intervalo_2 or esta_en_intervalo_3:
        mensaje = "El número {} se encuentra **DENTRO** de al menos uno de los tres intervalos. ✅".format(x)
    else:
        mensaje = "El número {} se encuentra **FUERA** de los tres intervalos. ❌".format(x)


    print("\n--- Resultado ---")
    print(mensaje)

except ValueError:
    print("Error: Ingrese solo números enteros válidos.")