def obtener_datos(prompt, num_datos):
    lista_datos = []
    for _ in range(num_datos):
        dato = input(prompt)
        lista_datos.append(dato)
    return lista_datos

num_datos = 3
lista_nombres = obtener_datos("Ingrese un nombre: ", num_datos)
lista_apellidos = obtener_datos("Ingrese un apellido: ", num_datos)

lista_combinada = []
for i in range(max(len(lista_nombres), len(lista_apellidos))):
    nombre = lista_nombres[i] if i < len(lista_nombres) else ''
    apellido = lista_apellidos[i] if i < len(lista_apellidos) else ''
    lista_combinada.append(nombre + " " + apellido)

print(lista_combinada)