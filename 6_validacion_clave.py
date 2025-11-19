# Validación de clave con máximo 3 intentos
clave_correcta = "python123"
intentos = 0

while intentos < 3:
    clave = input("Ingrese la clave: ")
    if clave == clave_correcta:
        print("✅ Acceso permitido.")
        break
    else:
        intentos += 1
        print("❌ Clave incorrecta. Intento", intentos)

if intentos == 3:
    print("⛔ Acceso denegado. Se superó el número de intentos.")
