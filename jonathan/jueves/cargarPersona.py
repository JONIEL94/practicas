import json

persona = {}

with open('persona.json' , 'r') as filein:
		persona=json.load(filein)

print(persona['Nombre'])
print(persona['Apellido'])
print(persona['DNI'])
