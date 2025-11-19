# Suma continua hasta ingresar 0
suma = 0

while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    if num < 0:
        continue
    suma += num

print("La suma total de los números positivos es:", suma)
