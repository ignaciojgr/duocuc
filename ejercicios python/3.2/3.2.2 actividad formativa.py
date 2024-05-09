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
    
