def menu():
    #La variable canasta va aquí para que una vez que se completen todos los ciclos del bucle while, se almacenen los datos
    #Si la variable fuera dentro del bucle while, no acumularía todos los datos, sino sólo los del ciclo actual.

    canasta = {}
    while True:
        op = int(input("1. Agregar un item a la canasta\n2. Mostrar canasta\n3. Ver total\n4. Salir\nIngrese una opción:\t"))
        if op == 1:
            op1 = int(input(
                "1. Arroz: $1500\n"
                "2. Agua: $3000\n"
                "3. Carne: $7500\n"
                "4. Pollo: $5000\n"
                "5. Pan: 1000\n"
                "6. Salir\n"
                "Ingrese una opción:\t"
            ))
            #Se puede hacer un diccionario con los productos y sus precios para no tener que hacer tantos if.
            #La función get() de los diccionarios permite obtener el valor de una clave, si no existe, devuelve un valor por defecto.
            #En este caso, si no existe la clave, se le asigna 0.
            #Esto permite que no se tenga que hacer un if para verificar si la clave existe o no.
            #Además, se puede hacer un diccionario con los productos y sus precios para no tener que hacer tantos if.
            if op1 == 1:
                canasta["Arroz"] = canasta.get("Arroz", 0) + 1500
            elif op1 == 2:
                canasta["Agua"] = canasta.get("Agua", 0) + 3000
            elif op1 == 3:
                canasta["Carne"] = canasta.get("Carne", 0) + 7500
            elif op1 == 4:
                canasta["Pollo"] = canasta.get("Pollo", 0) + 5000
            elif op1 == 5:
                canasta["Pan"] = canasta.get("Pan", 0) + 1000
            elif op1 == 6:
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
        elif op == 2:
            for producto, precio in canasta.items():
                print(f"{producto}: ${precio}")
        elif op == 3:
            total = sum(canasta.values())
            print(f"Total: ${total}")
        elif op == 4:
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
menu()

                    
                    
                     