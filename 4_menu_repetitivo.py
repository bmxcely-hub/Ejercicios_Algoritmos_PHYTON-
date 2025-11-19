# Menú repetitivo: sumar, restar o salir
while True:
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", a + b)
    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", a - b)
    elif opcion == "3":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
