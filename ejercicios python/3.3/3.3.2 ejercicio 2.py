#Construir programa que permita almacenar los run ganadores del sorteo “la suerte de un
#run”. Los run ganadores son todos los run que terminan en los últimos dígitos antes del
#digito verificado sean 92, 95 y 84
#Los datos deben ser leídos desde el archivo csv llamado “listadoRun.csv” y depositados
#en el archivo llamado “ganadores.json”
listadoRun=[]
ganadores=[]
with open('listadoRun.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)
    for linea in lector_csv:
        run = linea[0]
        if run[-2:] == '92' or run[-2:] == '95' or run[-2:] == '84':
            ganadores.append(run)
        listadoRun.append(run)
with open('ganadores.json', 'w') as archivo_json:
    json.dump(ganadores, archivo_json, indent=4)