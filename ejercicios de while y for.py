#procesamiento de bultos
try:
    cant=int(input("Ingrese la cantidad de bultos a procesar:\n"))
except ValueError:
    while ValueError:
        cant=int(input("Ingrese solamente el número de bultos, por ejemplo: 5"))

for i in cant:
    
