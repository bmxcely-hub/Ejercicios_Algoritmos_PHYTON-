
numero = int(input("Ingrese un número entero: "))


if numero < 0:
    print("Los números negativos no tienen factorial.")
else:
    factorial = 1


    for i in range(1, numero + 1):
        factorial = factorial * i


    print("El factorial de", numero, "es:", factorial)
