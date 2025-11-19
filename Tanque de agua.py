

print("Ingrese el nivel actual del tanque (en litros): ")
nivel = float(input())


if nivel < 250:
    # Si el nivel es muy bajo
    accion = "Abrir la llave"
    mensaje = "El nivel está por debajo de 250 litros. ¡Abra la llave para llenado!"
elif nivel > 450:
    # Si el nivel es muy alto
    accion = "Cerrar la llave"
    mensaje = "El nivel está por encima de 450 litros. ¡Cierre la llave para evitar desbordes!"
else:
    # Si el nivel está entre 250 y 450 (incluidos)
    accion = "Cerrar la llave"
    mensaje = "El nivel es óptimo (entre 250 y 450 litros). Mantenga la llave cerrada."


print("-" * 30)
print("Nivel actual: {} litros".format(nivel))
print("Acción recomendada: **{}**".format(accion))
print(mensaje)