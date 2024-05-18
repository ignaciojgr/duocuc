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
