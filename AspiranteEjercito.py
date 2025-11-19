
print("Género del aspirante (M/F): ")
genero = input().upper()  # Convertir a mayúsculas para simplificar la comparación

print("Estado civil del aspirante (S/C/V/D/U): ")
estadoCivil = input().upper()

print("Estatura del aspirante: ")

estatura = float(input())

print("Edad del aspirante: ")

edad = int(input())



# Si (estadoCivil == 'S' O estadoCivil == 's') Entonces
if estadoCivil == 'S':
    # Segun (genero)
    if genero == 'F':
        # Caso 'F': Si (estatura > 1.60 Y edad >= 20 Y edad < 25) Entonces
        if estatura > 1.60 and edad >= 20 and edad < 25:
            salida = "Es Apto"
        # SiNo
        # salida ya es "No es Apto" por defecto, pero se mantiene la lógica
        # else:
            # salida = "No es Apto"
        # FinSi
    elif genero == 'M':
        # Caso 'M': Si (estatura > 1.65 Y edad>=18 Y edad<24) Entonces
        if estatura > 1.65 and edad >= 18 and edad < 24:
            salida = "Es Apto"
        # SiNo
        # else:
            # salida = "No es Apto"
        # FinSi
    # EnOtroCaso: (Si el género no es 'F' ni 'M')
    # Ya que la salida se inicializó como "No es Apto", no se necesita else
    # elif genero != 'F' and genero != 'M':
    #     salida = "No es Apto" # Este caso se maneja por la inicialización
    # FinSegun

# SiNo (Si el estadoCivil no es 'S')
else:
    salida = "No es Apto"
# FinSi (principal)

print("Resultado para el aspirante: ", salida)

# FinAlgoritmo