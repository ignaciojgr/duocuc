piso1=0
ladrillos=int(input("Ingrese la cantidad de ladrillos: "))
altura=0
utilizados=0
por_fila=1
while utilizados<ladrillos:
    por_fila+=1
    utilizados+=por_fila
    if por_fila==ladrillos-2:
        altura+=1
print("Altura: ",altura)
