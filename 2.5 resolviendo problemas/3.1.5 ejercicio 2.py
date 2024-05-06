numeros_participantes=[]
for i in range(50):
    numeros_participantes.append(i+1)
    if i==49:
        break
eleccion_del_jugador=[]
for i in range(7):
    eleccion_del_jugador.append(int(input("Ingrese 7 números: ")))
    if i==6:
        break
print("Los números que usted ingresó son: ",eleccion_del_jugador)
print("Los números sorteados esta ronda son: ",numeros_participantes)
for j in range(len(numeros_participantes)):
    print(numeros_participantes[j])




    