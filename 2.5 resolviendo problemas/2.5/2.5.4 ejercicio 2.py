end=1

while end==True:
    print("***************MENÚ***************")
    print("1.- Pagar con tarjeta de crédito\n2.- Pagar con Paypal\n3.- Pagar por transferencia")
    print("4.- Cancelar\n5.- Salir")
    while True:
        try:
            op=int(input("Ingrese la opción deseada:\t"))
        except ValueError:
            print("Hubo un error, debe ingresar sólo número, no texto.")
            continue
        else:
            break
    if op==1:
        while True:
            try:
                numero_de_tarjeta=int(input("Ingrese el número de tarjeta de crédito:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
        nombre_titular=input("Ingrese el nombre del titular de la tarjeta:\t")
        mes_vencimiento=input("Ingrese el mes de vencimiento de la tarjeta:\t") 
        año_vencimiento=input("Ingrese el año de vencimiento de la tarjeta:\t")
        print("Compra exitosa. Gracias por su compra.")
        while True:
            try:
                continuar=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
        if continuar==1:
            continue
        if continuar==2:
            end=2
    if op==2:
        correo_paypal=input("Ingrese el correo de Paypal:\t")
        contraseña_paypal=input("Ingrese la contraseña de Paypal:\t")
        print("Compra exitosa. Gracias por su compra.")
        while True:
            try:
                continuar=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
        if continuar==1:
            continue
        if continuar==2:
            end=2
    if op==3:
        while True:
            try:
                numero_de_cuenta=int(input("Ingrese el número de cuenta:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
        nombre_banco=input("Ingrese el nombre del banco:\t")
        nombre_titular=input("Ingrese el nombre del titular de la cuenta:\t")
        print("Compra exitosa. Gracias por su compra.")
        while True:
            try:
                continuar=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
        if continuar==1:
            continue
        if continuar==2:
            end=2
    if op==4:
        print("Compra cancelada.")
        while True:
            try:
                continuar=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
        if continuar==1:
            continue
        if continuar==2:
            end=2
    if op==5:
        print("Saliendo del sistema...")
        end=2
    if op<1 or op>5:
        print("Opción no válida. Intente de nuevo.")
        continue
print("Cierre de sesión exitoso.")

