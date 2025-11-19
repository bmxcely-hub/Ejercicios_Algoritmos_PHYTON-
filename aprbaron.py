cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))


contadorEstudiantes = 0
aprobaron = 0
reprobaron = 0
sumaDefinitivas = 0


while contadorEstudiantes < cantidadEstudiantes:
    codigoEstudiante = input("Ingrese el código del estudiante: ")
    notaDefinitiva = float(input("Ingrese la nota definitiva: "))

    if notaDefinitiva >= 3.0:
        aprobaron += 1
    else:
        reprobaron += 1

    sumaDefinitivas += notaDefinitiva
    contadorEstudiantes += 1


promedioGrupo = sumaDefinitivas / cantidadEstudiantes

print("La cantidad que aprobaron es:", aprobaron)
print("La cantidad que reprobaron es:", reprobaron)
print("El promedio es:", promedioGrupo)
