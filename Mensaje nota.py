
print("Ingrese la nota definitiva: ")

nota = float(input())


print("Su nota es: ", end="")


if nota < 3.0:
    # Si ( nota < 3.0 ) Entonces
    print("Insuficiente")
else:
    # SiNo
    if nota <= 3.5:
        # Si ( nota <= 3.5 ) Entonces
        print("Aceptable")
    else:
        # SiNo
        if nota <= 4.0:
            # Si ( nota <= 4.0 ) Entonces
            print("Sobresaliente")
        else:
            # SiNo
            print("Excelente")