

print("Ingrese el costo del artículo: ")
costo = float(input())

descuento = 0.0  # Inicializamos el descuento en cero


if costo > 150000:
    descuento = costo * 0.05
    print("¡Felicidades! Se aplica un descuento del 5%.")
else:
    descuento = 0.0
    print("El costo no supera los $150.000. No se aplica descuento.")


print("Costo original: $", costo)
print("Valor del descuento: $", descuento)
print("Costo final: $", costo - descuento)