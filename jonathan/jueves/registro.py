def agregarAlumnos(alumnos):
	alumno = {}
	
	otro = "s"

	while otro == "s":
		alumno['Nombre'] = input('Ingrese el nombre: ')
		alumno['Apellido'] = input('Ingrese el Apellido: ')
		alumno['DNI'] = int(input('Ingrese el DNI: '))
		alumno['Direccion'] = input('Ingrese direccion:')
		alumno['Telefono'] = input('Ingrese telefono: ')
		alumno['Email'] = input('Ingrese direccion de email:')
		alumno['Fecha de nacimiento'] = input('Ingrese fecha de nac: ')

		alumnos.append(alumno)

		otro = input("Agregar otro alumno? (s/n)")

	return alumnos

def listarAlumnos(alumnos):
	for alumno in alumnos:
		print(alumno)
#main
alumnos = []

opcion = -1

while opcion != 0:
	print("1 Agregar alumnos")
	print("2 Listar alumnos")
	print("0 Salir")

	opcion = int(input('Seleccione una opcion: '))

	if opcion == 1:
		alumnos = agregarAlumnos(alumnos)
	elif opcion == 2:
		listarAlumnos(alumnos)
