sw=1
while sw==True:
    try:
        sw=1
        print("El sistema está activo")
        print("======")
        print("Seleccione una opción:\n1. Ver mi saldo\n2. Retirar dinero\n3. Salir")
        op=int(input("Por favor, elija una opción:\t"))
        if op>0 and op<4:
            if op==1:
                print("Tiene un saldo de $500.000")
                sw=int(input("Presione 1 si desea continuar o 2 si desea salir:\t"))
            elif op==2:
                print("Transferencia realizada")
                sw=int(input("Presione 1 si desea continuar o 2 si desea salir:\t"))
            else:
                sw=2
        else:
            print("Ingreso fuera de rango")
    except ValueError:
        print("Ingreso Erróneo")
print("Ciere de sesión exitoso, adiós")
