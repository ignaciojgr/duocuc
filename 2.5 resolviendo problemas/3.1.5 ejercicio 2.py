import random
sw=3
numeros_participantes=[]
eleccion_del_jugador=[]
for i in range(50):
        numeros_participantes.append(i+1)
        if i==49:
            break
for i in range(7):
        eleccion_del_jugador.append(int(input("Ingrese 7 números: ")))
        if i==6:
            break
for j in range(3):
    print("Los números que usted ingresó son: ",eleccion_del_jugador)
    numeros_ganadores=random.sample(numeros_participantes, 7)
    print("Los números sorteados esta ronda son: ",numeros_ganadores)
    if eleccion_del_jugador==numeros_ganadores:
        print("¡Felicidades! Usted ha ganado el premio mayor.")
        sw=0
    else:
        print("Lo sentimos, no ha ganado esta ronda.")
    





    