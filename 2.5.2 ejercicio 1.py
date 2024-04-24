puntos=100000
op=0
op2=0

while op!=3:
    print("Bienvenido al menú")
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    op=int(input("Seleccione una opción:\t"))
    if op==1:
        print("Los puntos que tiene son, en total: ",puntos)
    elif op==2:
        print("Seleccione el producto a canjear")
        print("1. Giftcard de $10.000, valor de: 10.000 puntos")
        print("2. Secadora de pelo, valor de: 25.000 puntos")
        print("3. Disco duro portátil, valor de: 30.000 puntos")
        op2=int(input("Seleccione una opción:\t"))
        if op2==1
            puntos=puntos-10000
            print("Canje exitoso, le quedan: $")
