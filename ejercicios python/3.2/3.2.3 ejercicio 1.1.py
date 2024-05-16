diccionario_palabras={}
texto_ingresado=input("Ingrese un texto: ")
for palabra in texto_ingresado.split():
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1

print(diccionario_palabras)