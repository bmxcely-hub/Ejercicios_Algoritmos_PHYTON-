

n = int(input("Ingrese el valor de n: "))

print("x\tf(x)")
print("-------------")

for x in range(0, n + 1, 2):
    fx = (2 * x)**2 - 5
    print(x, "\t", fx)
