while True:
    espacios=" "
    linea="*"
    for i in range(11):
        print(linea)
        espacios+=" "
        linea=espacios+linea
    for i in range(14):
        print(linea)
        espacios=" "
        linea=linea[i:]
    
    linea="*"
    espacio=" "
    for i in range(24):
        linea+=" * "
        espacio+="   "
    print(linea)
    espacio+="*"
    for i in range (14):
        print(espacio)
    print(linea)
    break

    
    