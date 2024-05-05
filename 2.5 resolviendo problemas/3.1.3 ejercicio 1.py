import numpy as np
import numpy as np

# Cria um array com 12 elementos
array = np.arange(1, 13)

# Redimensiona o array para ter 4 linhas e 3 colunas
array_3x4 = array.reshape(3, 4)

# Prompt the user for input
data = input("Enter 12 comma-separated values: ")

# Split the input string into a list of values
values = data.split(",")

# Convert the values to integers
values = [int(value) for value in values]

# Create the array with the input data
array = np.array(values)

# Reshape the array to have 4 rows and 3 columns
array_3x4 = array.reshape(3, 4)

print(array_3x4)
