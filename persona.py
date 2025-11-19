persona = {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"}
print(persona["nombre"])   
print(persona.get("correo"))

persona["correo"] = "correoinstitucional@institucional.com"
persona["edad"]= 40
persona.update ({"pais":"Suiza"})
print(persona)


for clave in persona.keys():
    print("Clave:", clave)

for valor in persona.values():
    print("Valor:", valor)

for clave, valor in persona.items():
    print(clave, "→", valor)
    