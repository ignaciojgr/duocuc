#procesamiento de bultos
p_liviano=1000
p_pesado=2000
p_total=0
peso=0
bulto=0
b_liviano=0
b_pesado=0
b_livianoT=0
b_pesadoT=0
try:
    cant=int(input("Ingrese la cantidad de bultos a procesar:\n"))
except ValueError:
        cant=int(input("Ingrese solamente el número de bultos, por ejemplo: 5\n"))

for i in range(cant):
    bulto=i+1
    try:
        peso=float(input("Ingrese el peso del bulto:\n"))
        if peso>=1.0 and peso<=5.9:
            b_liviano=1
            print("\n",bulto," Liviano  $",p_liviano)
        if peso>=6.0 and peso<=10.9:
            b_pesado=1
            print("\n",bulto," Normal  $",p_pesado)
        if peso>=11.0:
            11.0/0
    except ValueError:
         peso=float(input("Ingrese sólo el número, por ejemplo: 5.5"))
         if peso>=1.0 and peso<=5.9:
            b_liviano=1
            print("\n",bulto," Liviano  $",p_liviano)
         if peso>=6.0 and peso<=10.9:
            b_pesado=1
            print("\n",bulto," Normal  $",p_pesado)

    except ZeroDivisionError:
            while peso>=11.0:
                peso=float(input("El peso no puede procesarse, por favor, intente con un peso entre 1.0 y 10.9:\n"))
                if peso>=1.0 and peso<=5.9:
                    b_liviano=1
                    print("\n",bulto," Liviano  $",p_liviano)
                if peso>=6.0 and peso<=10.9:
                    b_pesado=1
                    print("\n",bulto," Normal  $",p_pesado)
    b_livianoT=b_livianoT+b_liviano
    b_pesadoT=b_pesadoT+b_pesado
    p_total=peso+p_total
print("Cantidad de bultos livianos: ",b_livianoT)
print("Cantidad de bultos pesados: ",b_pesadoT)
print("Valor total a pagar: $",(b_livianoT*1000)+(b_pesadoT*2000))


    





