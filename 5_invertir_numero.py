# Invertir un número entero sin convertir a cadena
n = int(input("Ingrese un número entero: "))
invertido = 0

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10

print("Número invertido:", invertido)
