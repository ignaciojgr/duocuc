#Creen un programa que emule la función de una calculadora, debe tener 4 funciones,
#sumar, restar, dividir y multiplicar, el programa debe permitir el ingreso de dos números de
#tipo enteros. Este programa debe contener una pequeña validación que indique un
#mensaje cuando se divide por 0, indicado que no se puede realizar la operación. Las
#funciones a construir deben ser con argumentos y con retorno.
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    else:
        return a / b
#Al ejercicio anterior, le debemos incorporar una función de validación, que permita validar
#que solo se puede ingresar números. Además, el ejercicio anterior no permite ingresar
#valores decimales, a lo cual, en la misma función de validación se debe incorporar una
#conversión de valor de tipo Int a valor de tipo Float
def validacion():
    while True:
        try:
             numero_ingresado=float(input("Ingrese un número: "))
             return numero_ingresado
        except ValueError:
            print("Debe ingresar un número")
            continue
        else:
            break
a=validacion()
b=validacion()

print("Suma: ", sumar(a, b))
print("Resta: ", restar(a, b))
print("Multiplicación: ", multiplicar(a, b))
print("División: ", dividir(a, b))
