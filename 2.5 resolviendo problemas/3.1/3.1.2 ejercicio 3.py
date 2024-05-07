lista = []
end="sí"
while end.lower()=="sí" or end.upper()=="SI":
    dato=input("Ingrese un nombre: ")
    lista.append(dato)
    
    end=input("¿Desea continuar?, responda con sí o no")
if lista:  # Verifica si la lista no está vacía
    menor = min(lista, key=len)
    lista.remove(menor)
print(lista)        
    