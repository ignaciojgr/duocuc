#Construir programa que permita identificar las empresas que han tenido ventas inferiores a $100.000.000, entre $100.000.001 y $200.000.000 y más de $200.000.000, a lo cual usted deberá crear un archivo llamado “segmentacionEmpresas.json” que permita hacer esta distinción, a los datos listados más abajo deberá incorporar una columna adicional llamada clasificacionEmpresa donde se indique “Pequeño Contribuyente”, “Mediano Contribuyente” y “Gran Contribuyente

import csv
import json
with open('listadoRutEmpresa.csv', 'r') as file:
    reader = csv.DictReader(file)
    empresas = list(reader)
    for empresa in empresas:
        ventas = float(empresa['ventas'])
        if ventas < 100000000:
            empresa['clasificacionEmpresa'] = 'Pequeño Contribuyente'
        elif ventas >= 100000001 and ventas <= 200000000:
            empresa['clasificacionEmpresa'] = 'Mediano Contribuyente'
        else:
            empresa['clasificacionEmpresa'] = 'Gran Contribuyente'
    with open('segmentacionEmpresas.json', 'w') as file:
        json.dump(empresas, file, indent=4)
    print('Archivo segmentacionEmpresas.json creado con éxito')

