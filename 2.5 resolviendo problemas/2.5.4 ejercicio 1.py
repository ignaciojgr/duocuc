patio=0
sala=0
jardin=0
pasillo=0
end=1
print("Bienvenido al menú de luces\n====================")
print("Seleccione una opción:\n1. Encender/Apagar luces Patio (alternado)")
print("2. Encender/Apagar luces Sala (alternado)\n3. Encender/Apagar luces Pasillo (alternado)")
print("4. Encender/Apagar luces Jardín (alternado)\n5. Encender todo (alternado)\n6. Apagar todo (alternado)")
print("7. Salir del sistema")
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
        patio=patio+1
        if patio%2==0:
            print("Luces del patio apagadas...")
        if patio%2!=0:
            print("Luces del patio encendidas...")
        op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
    if op==2:
        sala+=1
        if sala%2==0:
            print("Luces de la sala apagadas...")
        if sala%2!=0:
            print("Luces de la sala encendidas...")
        op=int(input("Presione 1 para seguir en el menú o 2 para salir:\t"))
    if op==7:
        end=2
        print("Saliendo del sistema...")
        break
    
