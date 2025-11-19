

print("Para la ecuación ax^2 + bx + c = 0, ingrese los coeficientes.")

while True:
    try:
        a = float(input("Ingrese el valor de 'a': "))
        if a != 0:
            break
        else:
            print("El valor de 'a' no puede ser cero para una ecuación cuadrática.")
    except ValueError:
        print("Entrada inválida. Ingrese un número para 'a'.")

try:
    b = float(input("Ingrese el valor de 'b': "))
    c = float(input("Ingrese el valor de 'c': "))
except ValueError:
    print("Entrada inválida. Reinicie el programa e ingrese números para 'b' y 'c'.")
    exit() # Termina el programa si hay un error en b o c


discriminante = (b**2) - (4 * a * c)


print("\n--- Resultados ---")
print(f"Discriminante (b^2 - 4ac): {discriminante:.2f}")


if discriminante >= 0:
    print("La ecuación cuadrática **TIENE solución** (solución real). ✅")
else:
    print("La ecuación cuadrática **NO TIENE solución** (solución real, solo complejas). ❌")