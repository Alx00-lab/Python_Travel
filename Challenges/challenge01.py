
personas = [
    {"nombre": "Ana",   "ciudad": "Santo Domingo"},
    {"nombre": "Luis",  "ciudad": "Santiago"},
    {"nombre": "María", "ciudad": "Santo Domingo"},
    {"nombre": "Juan",  "ciudad": "Punta Cana"},
]
# quieres:
# {
#   "Santo Domingo": ["Ana", "María"],
#   "Santiago":      ["Luis"],
#   "Punta Cana":    ["Juan"]
# }

grupo = {}

for persona in personas:
    ciudad = persona.get("ciudad")
    nombre = persona.get("nombre")
    if ciudad not in grupo:
        grupo[ciudad] = []
    grupo[ciudad].append(nombre)

# Imprimir el resultado
print(grupo)


