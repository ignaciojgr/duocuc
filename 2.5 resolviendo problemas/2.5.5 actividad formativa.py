end=1
usuario1=0
usuario2=0
usuario3=0
contraseña1=0
contraseña2=0
contraseña3=0

while end==True:
    print("Bienvenido al menú de inicio de sesión")
    print(("1. Iniciar sesión\n2. Registrar usuario\n3. Salir"))
    opcion=int(input("Ingrese la opción que desea realizar: "))
    if opcion==1:
        print("Iniciar sesión")
        if usuario1==0 and usuario2==0 and usuario3==0:
            print("No hay usuarios registrados, por lo tanto, deberá registrar uno primero.")
            continue
        usuario=input("Ingrese su usuario: ")
        contraseña=input("Ingrese su contraseña: ")
        while True:
            if usuario==usuario1 and contraseña==contraseña1:
                print("Bienvenido",usuario)
                print("1. Realizar llamada\n2. Enviar correo electrónico\n3. Cerrar sesión")
                op_menu1=int(input("Ingrese la opción que desea realizar: "))
                if op_menu1==1:
                    telefono=int(input("Ingrese el número de teléfono al que desea llamar: "))
                    if len(str(telefono))==9 and telefono>=900000000:
                        print("Llamando al número",telefono)
                    else:
                        print("Número de teléfono no válido.")
                elif op_menu1==2:
                    correo=input("Ingrese el correo electrónico al que desea enviar el mensaje: ")
                    at_count=0
                    dot_count=0
                    for char in correo:
                        if char == "@":
                            at_count += 1
                        elif char == ".":
                            dot_count += 1
                    if at_count == 1 and dot_count == 1:
                        print("Correo electrónico válido.")
                    else:
                        print("Correo electrónico no válido.")
                        continue
                    mensaje=input("Ingrese el mensaje que desea enviar: ")
                    print("Mensaje enviado exitosamente a",correo)
                elif op_menu1==3:
                    print("Cerrando sesión...")
                    end=2
                else:
                    print("Usuario o contraseña incorrectos")
                    break
            elif usuario==usuario2 and contraseña==contraseña2:
                print("Bienvenido",usuario)
                print("1. Realizar llamada\n2. Enviar correo electrónico\n3. Cerrar sesión")
                op_menu2=int(input("Ingrese la opción que desea realizar: "))
                if op_menu2==1:
                    telefono=int(input("Ingrese el número de teléfono al que desea llamar: "))
                    if len(str(telefono))==9 and telefono>=900000000:
                        print("Llamando al número",telefono)
                    else:
                        print("Número de teléfono no válido.")
                elif op_menu2==2:
                    correo=input("Ingrese el correo electrónico al que desea enviar el mensaje: ")
                    at_count=0
                    dot_count=0
                    for char in correo:
                        if char == "@":
                            at_count += 1
                        elif char == ".":
                            dot_count += 1
                    if at_count == 1 and dot_count == 1:
                        print("Correo electrónico válido.")
                    else:
                        print("Correo electrónico no válido.")
                        continue
                    mensaje=input("Ingrese el mensaje que desea enviar: ")
                    print("Mensaje enviado exitosamente a",correo)
                elif op_menu2==3:
                    print("Cerrando sesión...")
                    end=2
                else:
                    print("Usuario o contraseña incorrectos")
                    break
            elif usuario==usuario3 and contraseña==contraseña3:
                print("Bienvenido",usuario)
                print("1. Realizar llamada\n2. Enviar correo electrónico\n3. Cerrar sesión")
                op_menu3=int(input("Ingrese la opción que desea realizar: "))
                if op_menu3==1:
                    telefono=int(input("Ingrese el número de teléfono al que desea llamar: "))
                    if len(str(telefono))==9 and telefono>=900000000:
                        print("Llamando al número",telefono)
                    else:
                        print("Número de teléfono no válido.")
                elif op_menu3==2:
                    correo=input("Ingrese el correo electrónico al que desea enviar el mensaje: ")
                    at_count=0
                    dot_count=0
                    for char in correo:
                        if char == "@":
                            at_count += 1
                        elif char == ".":
                            dot_count += 1
                    if at_count == 1 and dot_count == 1:
                        print("Correo electrónico válido.")
                    else:
                        print("Correo electrónico no válido.")
                        continue
                    mensaje=input("Ingrese el mensaje que desea enviar: ")
                    print("Mensaje enviado exitosamente a",correo)
                elif op_menu3==3:
                    print("Cerrando sesión...")
                    end=2
                else:
                    print("Usuario o contraseña incorrectos")
                    break
    elif opcion==2:
        print("Registro de usuario")
        usuario=input("Ingrese el usuario que desea registrar: ")
        contraseña=input("Ingrese la contraseña que desea registrar: ")
        if usuario1==0:
            usuario1=usuario
            contraseña1=contraseña
        elif usuario2==0:
            usuario2=usuario
            contraseña2=contraseña
        elif usuario3==0:
            usuario3=usuario
            contraseña3=contraseña
        print("Usuario registrado exitosamente.")
        print("Usuario: ",usuario)
        print("Contraseña: ",contraseña)
    elif opcion==3:
        print("Saliendo del sistema...")
        end=2
    else:
        print("Opción no válida.\nUsted será redirigido al menú de inicio de sesión...")
        
    
print("Cierre de sesión exitoso.")