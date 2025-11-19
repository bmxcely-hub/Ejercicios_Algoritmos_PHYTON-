
n = int(input("Ingrese el número de términos que desea generar: "))

print("Serie de números impares:")

for i in range(1, n * 2, 2):
    print(i, end=", ")
