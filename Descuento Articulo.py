
porcentaje = 0.0


print("Ingrese el valor del artículo: ")

valor = float(input())

print("Ingrese el tipo de artículo (1, 2, o 3): ")

tipo = input()





if tipo == '1':
    # Caso '1': porcentaje = 0.125 // 12.5%
    porcentaje = 0.125
    # FinCaso
elif tipo == '2':
    # Caso '2': porcentaje = 0.083 // 8.3%
    porcentaje = 0.083
    # FinCaso
elif tipo == '3':
    # Caso '3': porcentaje = 0.032 // 3.2%
    porcentaje = 0.032
    # FinCaso
else:
    # EnOtroCaso: porcentaje = 0.0
    porcentaje = 0.0
# FinSegun



print("El valor del descuento es: ", descuento)

# FinAlgoritmo