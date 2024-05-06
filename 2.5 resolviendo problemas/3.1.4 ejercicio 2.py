sw=1
listaSuper=[]
valorSuper=[]
print("Presione 1 para ingresar los productos del súper")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción: "))
if (op==1):
    while sw==1:
        try:
            print("----------------")
            producto=input("Incorpore el producto. Si desea salir, presione 0: ")
            if producto=="0":
                print("Adiós!")
                sw=0
            else:
                listaSuper.append(producto)
                valor=float(input("Incorpore el valor del producto: "))
                valorSuper.append(valor)
                print("Productos ingresados: ", listaSuper)
                print("Valores ingresados: ", valorSuper)
                print("La cantidad de productos ingresados es: ",len(listaSuper))
                print("El valor total de los productos es: ",sum(valorSuper))
        except:
            print("Error. Ingrese un valor numérico")
else:
    print("Adiós!")