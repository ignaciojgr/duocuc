end=1
deuda=100000
saldo=0
nuevo_saldo=0
while end==1:
    print("Bienvenido al menú del Banco de DuocUC")
    print("\n=============\nSeleccione una opción:\n1. Pagar monto\n2. Simular una compra")
    op=int(input("Seleccione una opción:\t"))
    if op==1:
        print("Usted tiene una deuda de: $",deuda)
        pago=int(input("Monto a pagar:\t$"))
        saldo=pago-deuda
        print("Nuevo saldo de la tarjeta:\t",saldo)
    if op==2:
        cantidad_simulada=int(input("Por favor, ingrese la cantidad de compras que quiere simular:\t"))
        for i in range(cantidad_simulada):
            numero_de_compra=i+1
            print("Compra número 1:\n================")
            monto_de_compra=int(input("Ingrese el monto de la compra:\t"))
            nuevo_saldo=saldo-monto_de_compra
            saldo=nuevo_saldo
            print("Su nuevo saldo es:\t",nuevo_saldo)
            
            