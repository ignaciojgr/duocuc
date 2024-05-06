sw=1
matriz_alumnos=[]
while sw==1:
    nombre_alumno=input("Ingrese el nombre del alumno: ")
    direccion_alumno=input("Ingrese la direccion del alumno: ")
    telefono_alumno=input("Ingrese el telefono del alumno: ")
    op=int(input("Presione 1 si desea seguir o cualquier otra tecla para salir: "))
    if op!=1:
        sw=0
    matriz_alumnos.append([nombre_alumno,direccion_alumno,telefono_alumno])
print(matriz_alumnos)
for i in range(len(matriz_alumnos)):
    print("Nombre: ",matriz_alumnos[i][0])
    print("Direccion: ",matriz_alumnos[i][1])
    print("Telefono: ",matriz_alumnos[i][2])
    print("***************")

print("Fin del programa")
