# Cria uma matriz 3D
matriz_3d = [
    [
        ["amarillo", "rojo", "naranja"],
        ["verde", "blanco", "amarillo"],
        ["rojo", "naranja", "verde"]
    ],
    [
        ["blanco", "amarillo", "rojo"],
        ["naranja", "verde", "blanco"],
        ["amarillo", "rojo", "naranja"]
    ],
    [
        ["verde", "blanco", "amarillo"],
        ["rojo", "naranja", "verde"],
        ["blanco", "amarillo", "rojo"]
    ]
]

contagem = sum(sublista.count('amarillo') for lista in matriz_3d for sublista in lista)
print(contagem)
contagem1 = 0
for lista in matriz_3d:
    for sublista in lista:
        for elemento in sublista:
            if elemento == 'amarillo':
                contagem1 += 1
print(contagem1)
contagem2=0
for lista in matriz_3d:
    for sublista in lista:
        for elemento in sublista:
            if elemento == "rojo":
                contagem2 += 1
contagem3=0
for lista in matriz_3d:
    for sublista in lista:
        for elemento in sublista:
            if elemento == "verde":
                contagem3 += 1
contagem4=0
for lista in matriz_3d:
    for sublista in lista:
        for elemento in sublista:
            if elemento == "blanco":
                contagem4 += 1
contagem5=0
for lista in matriz_3d:
    for sublista in lista:
        for elemento in sublista:
            if elemento == "naranja":
                contagem5 += 1
print("A cor amarela aparece", contagem1, "vezes")
print("A cor vermelha aparece", contagem2, "vezes")
print("A cor verde aparece", contagem3, "vezes")
print("A cor branca aparece", contagem4, "vezes")
print("A cor laranja aparece", contagem5, "vezes")