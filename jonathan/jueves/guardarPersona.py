import json

persona = {}

persona['Nombre']= input('Nombre? ')
persona['Apellido']= input('Apellido? ')
persona['DNI']= int(input('Dni? '))

with open ('persona.json', 'w') as fileout:
	json.dump(persona , fileout)
