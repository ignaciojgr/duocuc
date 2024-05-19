#Objetivo del programa: Un programa funcional que, dada una lista de números
#ingresada por el usuario, identifica y muestra los números pares e impares de
#manera clara y organizada.
#Reglas de negocio:
#1. Solicitar al usuario que ingrese una lista de números enteros
#separados por espacios.
#2. Implementar una función llamada validar_lista_numeros que verifique
#que todos los elementos ingresados sean números enteros. Si se
#ingresa algún valor no válido, solicitar nuevamente la lista.
#3. la función validar_lista_numeros debe utilizar un bucle y maneja
#excepciones para asegurar que todos los elementos ingresados sean
#números enteros.
#4. Utilizar el operador de módulo % (MOD) para determinar si un
#número es par o impar en la lista de números a ingresar. Considerar
#que un número es par cuando el mod es igual a 0, en caso contrario,
#es impar
#5. Crear dos listas separadas: una para los números pares y otra para
#los impares.
#6. Mostrar al usuario las listas resultantes, indicando los números
#pares, e indicando los números impares

def validar_lista_numeros():
    while True:
        try:
            lista_numeros = input("Ingrese una lista de números enteros separados por espacios: ").split()
            lista_numeros = [int(i) for i in lista_numeros]
            return lista_numeros
        except ValueError:
            print("Debe ingresar solo números enteros")
            continue
        else:
            break
lista_numeros = validar_lista_numeros()
lista_pares = []
lista_impares = []
for i in lista_numeros:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print("Números pares: ", lista_pares)
print("Números impares: ", lista_impares)