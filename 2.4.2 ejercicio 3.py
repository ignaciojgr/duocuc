#Manejo de errores de valor y de división por cero
try:
    numerador=float(input("Ingrese el numerador de la fracción:\n"))
except ValueError:
    numerador=float(input("Por favor, sólo ingrese números, no texto, por ejemplo: 5 o 5.0\n"))
    denominador=float(input("Ingrese el denominador de la fracción:\n"))
try:
    denominador=float(input("Ingrese el denominador de la fracción:\n"))
except ValueError:
    denominador=float(input("Por favor, sólo ingrese números, no texto, por ejemplo: 5 o 5.0\n"))
    
resultado=0
try:
    resultado=numerador/denominador
except ZeroDivisionError:
    print(resultado)