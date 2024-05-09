#Esta es una lista vacía.
bus = []

#Este es un bucle que se ejecuta 10 veces.
for i in range(20):
    #Dentro del bucle, se crea una lista vacía llamada row. 
    row = []
    for j in range(4):
        #Dentro del bucle anidado, se añade un número a la lista row.
        row.append(i*4 + j)
    bus.append(row)

#Este bucle recorre cada row en bus.
for row in bus:
    print(*(f"{seat:2d}" for seat in row[:2]), " ", *(f"{seat:2d}" for seat in row[2:]))