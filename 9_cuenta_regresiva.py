# Cuenta regresiva con alerta
n = int(input("Ingrese un número entero para la cuenta regresiva: "))

for i in range(n, -1, -1):
    if i % 7 == 0 and i != 0:
        print(i, "⚠️ ¡Múltiplo de 7!")
    else:
        print(i)
