end=1
deuda=100000
cupomax=100000
nuevo_saldo=0
saldo1=0
while end==1:
    print("Bienvenido al menú del Banco de DuocUC")
    print("=============\nSeleccione una opción:\n1. Pagar monto\n2. Simular una compra\n3. Salir")
    while True:
        try:
            op=int(input("Seleccione una opción:\t"))
        except ValueError:
            print("Hubo un error, debe ingresar sólo número, no texto.")
            continue
        else:
            break
    if op==1:
        print("==============\nUsted tiene una deuda de: $ ",deuda)
        if deuda==0:
            print("Usted no tiene que pagar más")
            print("Su cupo disponible es \t$ ",cupomax)
            while True:
                try:
                    end=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
                except ValueError:
                    print("Hubo un error, debe ingresar sólo número, no texto.")
                    continue
                else:
                    break
        if deuda>0:
            while True:
                try:
                    pago=int(input("Monto a pagar:\t$ "))
                except ValueError:
                    print("Hubo un error, debe ingresar sólo número, no texto.")
                    continue
                else:
                    if pago>0:
                        saldo1=deuda-pago
                        deuda=saldo1
                        print("===============\nNuevo saldo de la tarjeta:\t",cupomax-saldo1,"\n===========")
                    break
                
        if saldo1>cupomax:
            print("El cupo máximo de su tarjeta de crédito es:\t",cupomax,"\nPor lo tanto, no puede excederlo")
            saldo1=cupomax
    if op==2:
        print("==============\nUsted tiene una deuda de: $ ",deuda)
        while True:
            try:
                cantidad_simulada=int(input("Por favor, ingrese la cantidad de compras que quiere simular:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
        nuevo_saldo=cupomax-deuda
        for i in range(cantidad_simulada):
            numero_de_compra=i+1
            print("=============\nCompra número ",numero_de_compra," :\n================")
            monto_de_compra=int(input("Ingrese el monto de la compra:\t"))
            nuevo_saldo=nuevo_saldo-monto_de_compra
            print("Su nuevo saldo es:\t",nuevo_saldo)
            if nuevo_saldo<0:
                print("Usted ha excedido el cupo de su tarjeta de crédito")
                print("Su nueva deuda es de:\t",abs(nuevo_saldo-100000))
    if op==3:
        end=2
print("=============\nCierre de sesión exitoso, vuelva pronto!") 