

print("Ingrese un número entero entre 0 y 20: ")
num = int(input())


primos_conocidos = [2, 3, 5, 7, 11, 13, 17, 19]


if num < 0 or num > 20:
    resultado = "El número está fuera del rango (0 a 20)."
else:

    if num in primos_conocidos:
        resultado = "Es un **número primo**."
    elif num == 0 or num == 1:
        resultado = "No es un número primo (0 y 1 no se consideran primos)."
    else:
        resultado = "No es un número primo."

print("-" * 30)
print("El número ingresado es:", num)
print("Diagnóstico:", resultado)