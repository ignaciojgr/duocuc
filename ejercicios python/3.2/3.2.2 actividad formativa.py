def caso_1():
    lista_nombres=[]
    max_longitud=0
    max_nombre=""
    for i in range(3):
        nombre_ingresado=input("Ingrese un nombre:\t")
        lista_nombres.append(nombre_ingresado)
    for nombre_ingresado in lista_nombres:
        if len(nombre_ingresado)>max_longitud:
            max_longitud=len(nombre_ingresado)
            max_nombre=nombre_ingresado
    print("El nombre más largo es: ",max_nombre)

def caso_2():
    lista_nombres = []
    lista_apellidos = []

    for i in range(3):
        nombre_ingresado = input("Ingrese un nombre:\t")
        apellido_ingresado = input("Ingrese un apellido:\t")
        lista_nombres.append(nombre_ingresado)
        lista_apellidos.append(apellido_ingresado)

    lista_nombres.sort()
    lista_apellidos.sort()

    lista_ordenada = list(zip(lista_nombres, lista_apellidos))

    print("Nombres y apellidos ordenados: ")
    for nombre, apellido in lista_ordenada:
        print(nombre, apellido)

def caso_3():
    lista_nombres=[]
    while True:
        lista_nombres.append(input("Ingrese un nombre: "))
        continuar=int(input("Desea ingresar otro nombre? (1: Sí, 0: No) "))
        if continuar==1:
            continue
        else:
            break
    mas_corto = min(lista_nombres, key=len)
    lista_nombres.remove(mas_corto)
    print(*lista_nombres)
caso_1()
caso_2()
caso_3()

    
