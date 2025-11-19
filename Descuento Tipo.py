

print("Ingrese el valor del artículo: ")

try:
    valor = float(input())
except ValueError:
    print("Error: Ingrese un valor numérico válido.")
    exit()

print("\nTipos disponibles: Textil, Electrodoméstico, Elementos de cocina, Video juego")
print("Ingrese el tipo de artículo: ")

tipo = input().strip().lower()

porcentaje_descuento = 0.0


if tipo == "textil":
    porcentaje_descuento = 0.00  # 0%
elif tipo == "electrodomestico":
    porcentaje_descuento = 0.037  # 3.7%
elif tipo == "elementos de cocina":
    porcentaje_descuento = 0.042  # 4.2%
elif tipo == "video juego":
    porcentaje_descuento = 0.078  # 7.8%
else:
    print(f"\nAdvertencia: Tipo de artículo '{tipo}' no reconocido. No se aplicará descuento.")
    porcentaje_descuento = 0.0


valor_descuento = valor * porcentaje_descuento
valor_final = valor - valor_descuento


print("\n--- Resumen de Compra ---")
print(f"Tipo de artículo: {tipo.capitalize()}") # Mostrar el tipo capitalizado para mejor lectura
print(f"Porcentaje aplicado: {porcentaje_descuento * 100:.1f}%") # Mostrar como porcentaje con 1 decimal
print(f"Valor original: ${valor:.2f}")
print(f"Valor del descuento: ${valor_descuento:.2f}")
print(f"Valor total a pagar: ${valor_final:.2f}")

# FinAlgoritmo