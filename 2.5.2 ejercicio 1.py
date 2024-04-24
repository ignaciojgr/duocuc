puntos=100000
op=0
op2=0
end=1

while end==1:
    print("Bienvenido al menú")
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    op=int(input("Seleccione una opción:\t"))
    while op<1 or op>3:
        op=int(input("Seleccione una opción válida (1, 2 o 3):\t"))
    if op==1:
        print("Los puntos que tiene son, en total: ",puntos)
        end=int(input("Presione 1 si desea continuar o 2 si desea salir:\t"))   
    elif op==2:
        print("Seleccione el producto a canjear")
        print("1. Giftcard de $10.000, valor de: 10.000 puntos")
        print("2. Secadora de pelo, valor de: 25.000 puntos")
        print("3. Disco duro portátil, valor de: 30.000 puntos")
        op2=int(input("Seleccione una opción:\t"))
        if op2==1:
            puntos=puntos-10000
            print("Canje exitoso, le quedan: $",puntos)
            end=int(input("Presione 1 si desea continuar o 2 si desea salir:\t"))
        if op2==2:
            puntos=puntos-25000
            print("Canje exitoso, le quedan: $",puntos)
            end=int(input("Presione 1 si desea continuar o 2 si desea salir:\t"))
        if op2==3:
            puntos=puntos-30000
            print("Canje exitoso, le quedan: $",puntos)
            end=int(input("Presione 1 si desea continuar o 2 si desea salir:\t"))
    else:
        end=2
    
