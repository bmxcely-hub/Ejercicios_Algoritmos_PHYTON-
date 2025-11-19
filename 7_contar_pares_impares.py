# Contar números pares e impares hasta ingresar 0
pares = 0
impares = 0

while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
