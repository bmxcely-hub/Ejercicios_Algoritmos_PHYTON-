

numero = int(input("Ingrese un número entero: "))

if numero > 0:

    cifras = 0
    temporal = numero
    suma_cifras = 0


    while temporal > 0:
        digito = temporal % 10          
        suma_cifras = suma_cifras + digito
        cifras = cifras + 1
        temporal = temporal // 10       
    print("El número tiene", cifras, "cifras.")
    print("La suma de las cifras es:", suma_cifras)
else:
    print("El número no es positivo.")
