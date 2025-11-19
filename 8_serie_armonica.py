# Sumar serie armónica
n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma += 1 / i

print(f"La suma armónica hasta {n} es: {suma:.4f}")
