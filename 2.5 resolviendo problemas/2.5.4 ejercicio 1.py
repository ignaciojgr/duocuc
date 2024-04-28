patio=0
sala=0
jardin=0
pasillo=0
end=1

print("Bienvenido al menú de luces\n====================")
while end==1:
    print("Seleccione una opción:\n1. Encender/Apagar luces Patio (alternado)")
    print("2. Encender/Apagar luces Sala (alternado)\n3. Encender/Apagar luces Pasillo (alternado)")
    print("4. Encender/Apagar luces Jardín (alternado)\n5. Encender todo (alternado)\n6. Apagar todo (alternado)")
    print("7. Salir del sistema")
    while True:
        try:
            op=int(input("Ingrese la opción deseada:\t"))
        except ValueError:
            print("Hubo un error, debe ingresar sólo número, no texto.")
            continue
        else:
            break
    if op==1:
        patio+=1
        if patio%2==0:
            luz_patio="Luces del patio apagadas..."
            print(luz_patio)
        if patio%2!=0:
            luz_patio="Luces del patio encendidas..."
            print(luz_patio)
        while True:
            try:
                op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
    if op==2:
        sala+=1
        if sala%2==0:
            luz_sala="Luces de la sala apagadas..."
            print(luz_sala)
        if sala%2!=0:
            luz_sala="Luces de la sala encendidas..."
            print(luz_sala)
        while True:
            try:
                op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
    if op==3:
        pasillo+=1
        if pasillo%2==0:
            luz_pasillo="Luces del pasillo apagadas..."
            print(luz_pasillo)
        if pasillo%2!=0:
            luz_pasillo="Luces del pasillo encendidas..."
            print(luz_pasillo)
        while True:
            try:
                op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
    if op==4:
        jardin+=1
        if jardin%2==0:
            luz_jardin="Luces del jardín apagadas..."
            print(luz_jardin)
        if jardin%2!=0:
            luz_jardin="Luces del jardín encendidas..."
            print(luz_jardin)
        while True:
            try:
                op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
    if op==5:
        if patio%2==0:
            patio+=1
        if patio%2!=0:
            print("Luces del patio encendidas")
        if sala%2==0:
            sala+=1
        if sala%2!=0:
            print("Luces de la sala encendidas")
        if pasillo%2==0:
            pasillo+=1
        if pasillo%2!=0:
            print("Luces del pasillo encendidas")
        if jardin%2==0:
            jardin+=1
        if jardin%2!=0:
            print("Luces del jardín encendidas")
        while True:
            try:
                op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
    if op==6:
        if patio%2!=0:
            patio+=1
        if patio%2==0:
            print("Luces del patio apagadas")
        if sala%2!=0:
            sala+=1
        if sala%2==0:
            print("Luces de la sala apagadas")
        if pasillo%2!=0:
            pasillo+=1
        if pasillo%2==0:
            print("Luces del pasillo apagadas")
        if jardin%2!=0:
            jardin+=1
        if jardin%2==0:
            print("Luces del jardín apagadas")
        while True:
            try:
                op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
            except ValueError:
                print("Hubo un error, debe ingresar sólo número, no texto.")
                continue
            else:
                break
    if op==7:
        end=2
        print("Saliendo del sistema...")
        break
    

