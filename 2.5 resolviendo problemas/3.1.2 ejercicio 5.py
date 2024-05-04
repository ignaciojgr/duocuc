def menu():
    #La variable canasta va aquí para que una vez que se completen todos los ciclos del bucle while, se almacenen los datos
    canasta = {}
    while True:
        print("1. Adicionar item à canasta\n2. Exibir canasta\n3. Sair")
        op = int(input("Escolha uma opção: "))
        if op == 1:
            print(
                "1. Arroz: $1500\n"
                "2. Agua: $3000\n"
                "3. Carne: $7500\n"
                "4. Pollo: $5000\n"
                "5. Pan: 1000\n"
                "6. Sair\n"
            )
            op1 = int(input("Ingrese la opción del producto:\n"))
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
                print("Opción inválida. Por favor, tente novamente.")
        elif op == 2:
            for producto, precio in canasta.items():
                print(f"{producto}: ${precio}")
        elif op == 3:
            break
        else:
            print("Opción inválida. Por favor, tente novamente.")
menu()

                    
                    
                     