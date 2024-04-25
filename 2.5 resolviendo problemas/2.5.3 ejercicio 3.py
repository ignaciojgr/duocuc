sw=1
saldo=0

while sw==1:
    print("1. Ver mi saldo")
    print("2. Cargar saldo")
    print("3. Salir")
    op=int(input("Seleccione una opción:\t"))
    try:
        if op>0 and op<4:
            if op==1:
                print("Tiene un saldo de: ",saldo)
                sw=int(input("Presione 1 si desea continuar o 2 si desea salir del menú:\t"))
            if op==2:
                print("Cuánto desea cargar?")
                print("1. ")
print("Cierre de sesión exitoso, adiós")