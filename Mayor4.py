		


print("Ingrese el primer número: ")
n1 = float(input())

print("Ingrese el segundo número: ")
n2 = float(input())

print("Ingrese el tercer número: ")
n3 = float(input())

print("Ingrese el cuarto número: ")
n4 = float(input())


# Si ( n1 > n2 ) Entonces
if n1 > n2:
    # Si ( n1 > n3 ) Entonces
    if n1 > n3:
        # Si ( n1 > n4 ) Entonces
        if n1 > n4:
            mayor = n1
        # SiNo (n1 no es mayor que n4)
        else:
            mayor = n4
        # FinSi (interno: n1 > n4)
    # SiNo (n1 no es mayor que n3)
    else:
        # Si ( n3 > n4 ) Entonces
        if n3 > n4:
            mayor = n3
        # SiNo (n3 no es mayor que n4)
        else:
            mayor = n4
        # FinSi (interno: n3 > n4)
    # FinSi (medio: n1 > n3)
# SiNo (n1 no es mayor que n2)
else:
    # Si ( n2 > n3 ) Entonces
    if n2 > n3:
        # Si ( n2 > n4 ) Entonces
        if n2 > n4:
            mayor = n2
        # SiNo (n2 no es mayor que n4)
        else:
            mayor = n4
        # FinSi (interno: n2 > n4)
    # SiNo (n2 no es mayor que n3)
    else:
        # Si ( n3 > n4 ) Entonces
        if n3 > n4:
            mayor = n3
        # SiNo (n3 no es mayor que n4)
        else:
            mayor = n4
        # FinSi (interno: n3 > n4)
    # FinSi (medio: n2 > n3)
# FinSi (principal: n1 > n2)


print("La número mayor es: ", mayor)

