def agregarAlumnos(alumnos):
	alumno = {}
	
	otro = "si"

	while otro == "si":
		alumno['Nombre'] = input('Ingrese el nombre: ')
		alumno['Apellido'] = input('Ingrese el Apellido: ')
		alumno['DNI'] = int(input('Ingrese el DNI: '))
		alumno['Direccion'] = input('Ingrese direccion:')
		alumno['Telefono'] = input('Ingrese telefono: ')
		alumno['Email'] = input('Ingrese direccion de email:')
		alumno['Fecha de nacimiento'] = input('Ingrese fecha de nacimiento: ')

		alumnos.append(alumno)

		otro = input("Agregar otro alumno? (si/no) : ")

	return alumnos

def listarAlumnos(alumnos):
	for alumno in alumnos:
		print(alumno)

def borrarAlumno(alumnos):
	apellido = input("Ingrese apellido de alumno a borrar: ")
	if (apellido == alumnos):

		alumnos.remove(alumno)

	otro = input("Borrar otro alumno ? (si/no) : ")
	
	return alumnos
#main
alumnos = []

opcion = -1

while opcion != 0:
	print("1 Agregar alumnos")
	print("2 Listar alumnos")
	print("3 Borrar alumno por nombre: ")
	print("0 Salir")

	opcion = int(input('Seleccione una opcion: '))

	if opcion == 1:
		alumnos = agregarAlumnos(alumnos)
	elif opcion == 2:
		listarAlumnos(alumnos)
	elif opcion == 3:
		borrarAlumno(alumnos)
