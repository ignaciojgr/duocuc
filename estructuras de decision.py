print("Bienvenido a estructuras de decision \n Elija etapa a ejecuccion! \n 1. Sistema edad \n 2. Usuario/Contraseña \n 3. Notas \n 4. Animales \n 5. Formulario ")
print("\n\n\n")
try: 
    choice=int(input("Ingrese el número de opción:\n"))
except ValueError:
    choice=int(input("Por favor, ingrese un número, no texto:\n"))
    

op1=1
op2=2
op3=3
op4=4
op5=5

if choice==1:
    print("ejecutandose 'sistema de edad'\n")
    edadUsuario = int(input("ingresa tu edad!:\n"))
    if edadUsuario >= 18: 
        print("usted cuenta con la mayoria de edad c: ")
    else:
        print("usted no cuenta con la mayoria de edad :c")
if choice==2: 
    print("ejecutándose 'usuario/contraseña'")
    user1="Pedro"
    user2="Angel"
    contraseñauser1=1234
    contraseñauser2="a4s1"

    usuarioNuevo=input("ingresa tu usuario\n")
    contraseñaNueva=input("ingresa tu contraseña\n")
    if usuarioNuevo==user1  and contraseñaNueva==contraseñauser1 or usuarioNuevo==user2 and contraseñaNueva=="a4s1":
        print("sus credenciales son válidas")
    else : 
        while usuarioNuevo!=user1  and contraseñaNueva!=contraseñauser1 or usuarioNuevo!=user2 and contraseñaNueva!="a4s1":
            print("Por favor, vuelva a ingresar sus credenciales")
            usuarioNuevo=input("ingresa tu usuario \n")
            contraseñaNueva=input("ingresa tu contraseña \n")
 
 


if choice== 3:
    print("bienvenido a la plataforma! \n ")

#if choice== 4:


#if choice== 5: 