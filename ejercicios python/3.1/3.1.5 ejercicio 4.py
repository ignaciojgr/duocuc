import random
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()
precios=[]
tiempo=[]
media_movil=[]
for t in range(51):
    precios.append(random.randint(1,20))
    tiempo.append(t)
periodos=3
for i in range(periodos-1):
    primero=media_movil[0]
    media_movil.insert(0,primero)
for conteo in range(len(precios)-periodos+1):
    promedio=0
    for i in range(periodos):
        promedio+=precios[conteo+i]
        
ax.plot(tiempo,precios)
ax.plot(tiempo,media_movil)
ax.set_title("Media móvil: precio vs tiempo")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Precio")

plt.show()
# Save the plot
plt.savefig('plot.png')