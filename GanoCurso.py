
suma_notas = 0.0
num_trabajos = 5
nota_minima_ganar = 3.5

print("--- Ingreso de Notas (entre 0.0 y 5.0) ---")
for i in range(1, num_trabajos + 1):
    while True:
        try:
            nota = float(input(f"Ingrese la nota del trabajo {i}: "))
           
            if 0.0 <= nota <= 5.0:
                suma_notas += nota
                break
            else:
                print("Nota fuera de rango. Ingrese una nota entre 0.0 y 5.0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")


nota_definitiva = suma_notas / num_trabajos


print("\n--- Resultados ---")
print(f"Nota Definitiva: {nota_definitiva:.2f}") # Formatear a dos decimales

if nota_definitiva > nota_minima_ganar:
    print("¡El estudiante **GANÓ** el curso! 🎉")
else:
    print("El estudiante **PERDIÓ** el curso. 😞")