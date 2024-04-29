end=1

while end==True:
    print("Bienvenido al menú de inicio de sesión")
    print(("1. Iniciar sesión\n2. Registrar usuario\n3. Salir"))
    usuario1=0
    usuario2=0
    usuario3=0
    contraseña1=0
    contraseña2=0
    contraseña3=0
    opcion=int(input("Ingrese la opción que desea realizar: "))
    if opcion==1:
        print("Iniciar sesión")
        usuario=input("Ingrese su usuario: ")
        contraseña=input("Ingrese su contraseña: ")
        if usuario==usuario1 and contraseña==contraseña1:
            print("Bienvenido",usuario)
        elif usuario==usuario2 and contraseña==contraseña2:
            print("Bienvenido",usuario)
        elif usuario==usuario3 and contraseña==contraseña3:
            print("Bienvenido",usuario)
        else:
            print("Usuario o contraseña incorrectos")
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