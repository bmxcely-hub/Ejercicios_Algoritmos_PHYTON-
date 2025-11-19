# Determinar si un número es primo
num = int(input("Ingrese un número entero mayor que 1: "))

es_primo = True
if num <= 1:
    es_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
