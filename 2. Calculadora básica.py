# Calculadora básica
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    op = input("Operación (+, -, *, /): ")

    if op == "+":
        print(sumar(a, b))
    elif op == "-":
        print(restar(a, b))
    elif op == "*":
        print(multiplicar(a, b))
    elif op == "/":
        print(dividir(a, b))
    else:
        print("Operación inválida")
