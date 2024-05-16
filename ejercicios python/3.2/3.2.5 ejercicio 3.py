#Este programa solicita al usuario ingresa nombre y edad. 
#Estos datos se almacenan en tuplas.
#Luego, se utiliza un conjunto para identificar las edades únicas presentes en la lista.
#Finalmente, se imprime la cantidad de edades únicas.
#Se crea una lista vacía para almacenar las tuplas.
lista_personas = []

while True:
    nombre = input("Ingrese el nombre de la persona (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    edad = int(input("Ingrese la edad de la persona: "))
    persona = (nombre, edad)  # Crea una tupla con el nombre y la edad
    lista_personas.append(persona)  # Añade la tupla a la lista

# Se crea una lista vacía para almacenar las edades.
lista_edades = [persona[1] for persona in lista_personas]

# Se recorre la lista de edades y se muestran las edades que solo aparecen una vez.
for edad in lista_edades:
    if lista_edades.count(edad) == 1:
        print(edad)
