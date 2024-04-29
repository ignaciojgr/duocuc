end=1
print("Calculadora geométrica\n")
while end==True:
    print("****************MENÚ****************")
    print("1. Calcular périmetro\n2. Calcular área\n3. Salir")
    opcion = int(input("Elija una opción: "))
    if opcion==1:
        while True:
            print("Calcular périmetro:\n1. Para círculo\n2. Para rectángulo\n3. Para cuadrado\n4. Volver al menú principal")
            opcion1=int(input("Elija una opción: "))
            if opcion1==1:
                radio=float(input("Ingrese el radio del círculo: "))
                perimetro=2*3.14*radio
                print("El perímetro del círculo es: ",perimetro)
            elif opcion1==2:
                base=float(input("Ingrese la base del rectángulo: "))
                altura=float(input("Ingrese la altura del rectángulo: "))
                perimetro=2*(base+altura)
                print("El perímetro del rectángulo es: ",perimetro)
            elif opcion1==3:
                lado=float(input("Ingrese el lado del cuadrado: "))
                perimetro=4*lado
                print("El perímetro del cuadrado es: ",perimetro)
            elif opcion1==4:
                print("Volviendo al menú principal")
                break
            else:
                print("Opción incorrecta, por favor, intente con números del 1 al 4")
    elif opcion==2:
        while True:
            print("Calcular área:\n1. Para círculo\n2. Para rectángulo\n3. Para cuadrado\n4. Volver al menú principal")
            opcion2=int(input("Elija una opción: "))
            if opcion2==1:
                radio=float(input("Ingrese el radio del círculo: "))
                area=3.14*radio**2
                print("El área del círculo es: ",area)
            elif opcion2==2:
                base=float(input("Ingrese la base del rectángulo: "))
                altura=float(input("Ingrese la altura del rectángulo: "))
                area=base*altura
                print("El área del rectángulo es: ",area)
            elif opcion2==3:
                lado=float(input("Ingrese el lado del cuadrado: "))
                area=lado**2
                print("El área del cuadrado es: ",area)
            elif opcion2==4:
                print("Volviendo al menú principal")
                break
            else:
                print("Opción incorrecta, por favor, intente con números del 1 al 4")
    elif opcion==3:
        print("Saliendo del programa...")
        end=2
print("Fin del programa")