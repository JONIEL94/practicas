alumnos= []
continuar = 'si'

while continuar == 'si':
	alumno = {}
	alumno['DNI'] = input('Ingrese DNI:')
	alumno['NOMBRE'] = input('Ingrese nombre: ')

	alumnos.append(alumno)

	continuar=input('continuar?: ')

print(alumnos)
