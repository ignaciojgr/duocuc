def menu():
    user_dict = {}
    while True:
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        option = input("Seleccione una opción: ")

        if option == '1':
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            if username in user_dict and user_dict[username] == password:
                print("Inicio de sesión exitoso!")
            else:
                print("Nombre de usuario o contraseña incorrectos.")

        elif option == '2':
            username = input("Ingrese un nombre de usuario: ")
            password = input("Ingrese una contraseña: ")
            user_dict[username] = password
            print("Usuario registrado con éxito!")

        elif option == '3':
            username = input("Ingrese el nombre de usuario que desea eliminar: ")
            password = input("Ingrese la contraseña para confirmar: ")
            if username in user_dict and user_dict[username] == password:
                del user_dict[username]
                print("Usuario eliminado con éxito!")
            else:
                print("Nombre de usuario o contraseña incorrectos. No se pudo eliminar el usuario.")

        elif option == '4':
            print("Saliendo...")
            print(user_dict)
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()

    
