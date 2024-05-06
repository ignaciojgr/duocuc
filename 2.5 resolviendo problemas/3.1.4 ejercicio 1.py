#promedio Notas
sw=1
listaNotas=[]
print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción:"))

if (op==1):
    while sw==1:
        try:
            print("----------------")
            nota=int(input("Incorpore su nota. Si desea salir, presione 0: "))
            if nota!=0:
                listaNotas.append(nota)
                notas_str = ", ".join(map(str, listaNotas))
                print("Notas ingresadas: ", notas_str)
                print("La cantidad de notas ingresadas es: ",len(listaNotas))
                print("El promedio de notas es: ",sum(listaNotas)/len(listaNotas))
            else: 
                print("Adiós!")
                sw=0
        except:
            print("Ingreso erróneo")
