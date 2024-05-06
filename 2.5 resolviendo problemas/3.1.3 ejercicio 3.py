# Crie uma lista vazia chamada 'bus'
bus = []

# Use um loop for para adicionar 10 sublistas à lista 'bus'
for i in range(10):
    row = []
    for j in range(4):
        row.append(i*4 + j + 1)
    bus.append(row)

# Use outro loop for para imprimir os números dos assentos
for row in bus:
    print(*(f"{seat:2d}" for seat in row[:2]), " ", *(f"{seat:2d}" for seat in row[2:]))