print("bienvenido a estructuras de decision \n elija etapa a ejecuccion! \n 1. sistema edad \n 2. usuario/contraseña \n 3. notas \n 4. animales \n 5. formulario ")

try: 
    choice=int(input("Ingrese el número de opción:\n"))
except ValueError:
    choice=int(input("Por favor, ingrese un número, no texto:\n"))
    

op1=1
op2=2
op3=3
op4=4
op5=5

if choice== 1:
    print("ejecutandose 'sistema de edad'")
    edadUsuario = int(input("ingresa tu edad!:\n"))
    if edadUsuario >= 18: 
        print("usted cuenta con la mayoria de edad c: ")
    else:
        print("usted no cuenta con la mayoria de edad :c")
if choice== 2: 
    print("ejecutandose 'usuario/contraseña'")
    user1 = "Pedro"
    user2 = "Angel"
    contraseñauser1 = 1234
    contraseñauser2 = "a4s1"

    usuarioNuevo=(input("ingresa tu usuario \n"))2
    if usuarioNuevo == user1  or  usuarioNuevo == user2 :
        print("ingrese contraseña")
    else : 
        print("este usuario no existe")
 
 


if choice== 3:
    print("bienvenido a la plataforma! \n ")

#if choice== 4:


#if choice== 5: 