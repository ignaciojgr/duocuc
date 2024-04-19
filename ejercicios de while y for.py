#procesamiento de bultos
p_total=0
peso=0
try:
    cant=int(input("Ingrese la cantidad de bultos a procesar:\n"))
except ValueError:
    while ValueError:
        cant=int(input("Ingrese solamente el número de bultos, por ejemplo: 5"))

for i in cant:
    peso=float(input("Ingrese el peso del bulto"))
    p_total=peso+p_total

