usuarios={}	
lista_contactos={}
while True:
    menu=int(input("1. Iniciar sesión\n2. Registrarse\n3. Salir\n"))
    if menu==1:
        print("Iniciando sesión")
        usuario=input("Ingrese su usuario: ")
        contraseña=input("Ingrese su contraseña: ")
        if usuario in usuarios and usuarios[usuario]==contraseña:
            print("Sesión iniciada")
            menu_usuario=int(input("1. Cambiar contraseña\n2. Realizar llamada\n3. Lista de contactos\n4. Enviar mensaje\n5. Revisar saldo\n6. Pagar deuda\n7. Comprar\n8. Salir"))
            if menu_usuario==1:
                nueva_contraseña=input("Ingrese su nueva contraseña: ")
                usuarios[usuario]=nueva_contraseña
                print("Contraseña cambiada")
            elif menu_usuario==2:
                numero_contacto=input("Ingrese el número de contacto: ")
                if numero_contacto in lista_contactos:
                    print("Llamando a ",lista_contactos[numero_contacto])
                else:
                    print("Número no registrado")
                print("Llamada finalizada")
                sub_menu_usuario=int(input("1. Seguir en el menu\n2. Cerrar sesión"))
                if sub_menu_usuario==1:
                    continue
                elif sub_menu_usuario==2:
                    break
                else:
                    print("Opción no válida")
            elif menu_usuario==3:
                print("Lista de contactos")
                for numero, contacto in lista_contactos.items():
                    print(numero, contacto)
        else:
            print("Usuario o contraseña incorrectos")

    elif menu==2:
        print("Registrando usuario")
        usuario=input("Ingrese su usuario: ")
        contraseña=input("Ingrese su contraseña: ")
        usuarios[usuario] = contraseña
    elif menu==3:
        print("Saliendo")
        break
    else:
        print("Opción no válida")