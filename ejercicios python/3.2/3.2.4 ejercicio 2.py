#En este programa se genera un conjunto de números primos dentro de un rango específico. Además, se crea una función para verificar si un número es primo o no.
#Se crea una lista vacía para almacenar los números primos.
numeros_primos=[]
for numero in range(2,100):
    es_primo=True
    for i in range(2,numero):
        if numero%i==0:
            es_primo=False
            break
    if es_primo:
        numeros_primos.append(numero)
print(numeros_primos)
#Se crea una función que recibe un número y verifica si es primo o no.
def verificar_primo(numero):
    es_primo=True
    for i in range(2,numero):
        if numero%i==0:
            es_primo=False
            break
    return es_primo
#Se verifica si el número 3 es primo.
print(verificar_primo(3))