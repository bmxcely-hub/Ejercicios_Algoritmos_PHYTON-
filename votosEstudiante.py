
cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes que participarán: "))


contadorEstudiantes = 0
votosAndroid = 0
votosIOS = 0
votosInvalidos = 0


while contadorEstudiantes < cantidadEstudiantes:
    codigo = input("Ingrese el código del estudiante: ")
    voto = input("Ingrese la plataforma elegida (Android/iOS): ")

    if voto.lower() == "android":
        votosAndroid += 1
    elif voto.lower() == "ios":
        votosIOS += 1
    else:
        print("Plataforma no válida. El voto no será contado.")
        votosInvalidos += 1

    contadorEstudiantes += 1


print("\n--- RESULTADOS DE LA ENCUESTA ---")
print("Votos por Android:", votosAndroid)
print("Votos por iOS:", votosIOS)
print("Votos no válidos:", votosInvalidos)


if votosAndroid > votosIOS:
    print("La plataforma seleccionada es: Android.")
elif votosIOS > votosAndroid:
    print("La plataforma seleccionada es: iOS.")
else:
    print("Se presentó un empate. Se usará otro mecanismo de elección.")
