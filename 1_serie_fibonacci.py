# Serie Fibonacci hasta N
n = int(input("Ingrese el valor máximo N: "))

a, b = 0, 1
print("Serie de Fibonacci:")

while a <= n:
    print(a, end=" ")
    a, b = b, a + b
