#Creen un programa que la lectura de un archivo CSV llamado 'datos.csv' que contiene
#información sobre personas, incluyendo su nombre, edad y comuna. Para cada registro
#en el archivo, se evalúa la edad y se determina si la persona es mayor o menor de edad.
#La información, que incluye el nombre, la edad, el estado de edad y la comuna, se
#imprime en la consola. Además, los registros de personas mayores o iguales a 25 años se
#recopilan en una lista llamada mayores. La lista con usuarios mayores o iguales a 25 años
#se guarda en un archivo JSON llamado 'mayores.json', se adjunta el conjunto de datos a
#incorporar en datos.csv
#La estructura del archivo 'datos.csv' es la siguiente:
#nombre,edad,comuna
#Juan,21,Puente Alto
#María,30,Concepción
#Carlos,22,Viña Del Mar
#Estela, 25,Puerto Montt

import csv
import json
