def agregarPersonas(personas):
	persona = {}

	otro = "si"

	while otro == "si":
		persona['Nombre'] = input('Ingrese nombre: ')
		persona['Apellido'] = input('Ingrese apellido: ')
		
		comidas = []
		
		otraComida = "si"

		while otraComida == "si":
			comidas.append(input('Ingrese comida favorita: '))
			otraComida = input('Agregar otra comida? (si/no) : ')

		persona['Comidas'] = comidas
		personas.append(persona)	

		otro = input("Agregar otra persona? (si/no): ")

	return personas

def mostrarPersonas(personas):
	for persona in personas:
		print(persona)
#main

personas = []
opcion = -1

while opcion != 0:
	print("1) Agregar personas")
	print("2) Mostrar personas")
	print("0) Salir")

	opcion = int(input('Seleccione una opcion: '))

	if opcion == 1:
		personas = agregarPersonas(personas)
	elif opcion == 2:
		mostrarPersonas(personas)

