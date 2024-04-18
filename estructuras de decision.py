print("Bienvenido a estructuras de decision \n Elija etapa a ejecutarse! \n\n 1. Sistema edad \n 2. Usuario/Contraseña \n 3. Notas \n 4. Animales \n 5. Formulario ")
print("\n\n")
try: 
    choice=int(input("Ingrese el número de opción:\n"))
except ValueError:
    choice=int(input("Por favor, ingrese un número, no texto:\n"))
    

op1=1
op2=2
op3=3
op4=4
op5=5

#Esta es la estructura de decisión del sistema de edad
if choice==1:
    print("Ejecutándose 'sistema de edad'\n")
if choice==1:
    print("Ejecutandose 'sistema de edad'\n")
    edadUsuario = int(input("ingresa tu edad!:\n"))
    if edadUsuario >= 18: 
        print("Usted cuenta con la mayoria de edad c: ")
    else:
        print("Usted no cuenta con la mayoria de edad :c")

#Esta es la estructura de decisión de la validación de usuario y contraseña
if choice==2: 
    print("ejecutándose 'usuario/contraseña'")
    user1="Pedro"
    user2="Angel"
    contraseñauser1="1234"
    contraseñauser2="a4s1"

    usuarioNuevo=input("Ingrese su usuario\n")
    contraseñaNueva=input("Ingrese su contraseña\n")
    if usuarioNuevo==user1  and contraseñaNueva==contraseñauser1:
        print("Sus credenciales son válidas")
    elif usuarioNuevo==user2 and contraseñaNueva==contraseñauser2:
        print("Sus credenciales son válidas")
    else: 
            print("Por favor, vuelva a ingresar sus credenciales")
            usuarioNuevo=input("Ingrese su usuario \n")
            contraseñaNueva=input("Ingrese su contraseña \n")
            if  usuarioNuevo==user1  and contraseñaNueva==contraseñauser1:
                print("Sus credenciales son válidas")
            elif usuarioNuevo==user2 and contraseñaNueva==contraseñauser2:
                print("Sus credenciales son válidas")
            else:
                print("Ha bloqueado el número de intentos")

#Esta es la estructura de decisión del sistema de notas
if choice==3:
    print("Ejecutándose 'notas' \n ")
    cant_notas=int(input("Ingrese la cantidad de notas a ingresar"))
    tnota=0.0
    for i in range(cant_notas):
        nota=float(input("Ingrese la nota en el siguiente formato: 2.0, 3.0, etc"))
        tnota=nota+tnota
    print("El promedio entre la cantidad de notas ingresadas son",tnota/cant_notas)


#if choice== 4:


#if choice== 5: 