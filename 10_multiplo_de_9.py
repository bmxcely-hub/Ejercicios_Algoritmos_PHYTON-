# Primer múltiplo de 9 entre N y M
n = int(input("Ingrese el valor de N: "))
m = int(input("Ingrese el valor de M: "))

encontrado = False

for i in range(n, m + 1):
    if i % 9 == 0:
        print("El primer múltiplo de 9 en el rango es:", i)
        encontrado = True
        break

if not encontrado:
    print("No hay múltiplos de 9 en el rango dado.")
