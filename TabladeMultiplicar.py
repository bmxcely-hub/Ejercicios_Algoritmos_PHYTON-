
tabla = int(input("¿Qué tabla deseas repasar? (1 a 20): "))


if 1 <= tabla <= 20:
    print(f"\n--- Repasando la tabla del {tabla} ---")
    aciertos = 0  

    
    for i in range(1, 11):
    
        respuesta = int(input(f"{tabla} x {i} = "))

    
        if respuesta == tabla * i:
            print(" ¡Muy bien! Respuesta correcta.\n")
            aciertos += 1
        else:
            print(f" Incorrecto. La respuesta correcta era {tabla * i}.\n")

    
    print(f"Total de aciertos: {aciertos}/10")

    if aciertos <= 5:
        print("Valoración: Insuficiente ")
    elif 6 <= aciertos <= 7:
        print("Valoración: Aceptable ")
    elif 8 <= aciertos <= 9:
        print("Valoración: Sobresaliente ")
    elif aciertos == 10:
        print("Valoración: Excelente ")

else:
    print(" Debes ingresar un número entre 1 y 20.")
