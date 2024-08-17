def insertion_sort(data):
    n = len(data)
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = tmp

# Testes

# Teste 1: Elementos já ordenados
arr_ordenado = [1, 2, 3, 4, 5]
print("Teste 4 - Elementos já ordenados:")
print("Original:", arr_ordenado)
insertion_sort(arr_ordenado)
print("Ordenado:", arr_ordenado)

# Teste 2: Elementos duplicados
arr_duplicados = [3, 1, 2, 2, 3, 1]
print("Teste 2 - Elementos duplicados:")
print("Original:", arr_duplicados)
insertion_sort(arr_duplicados)
print("Ordenado:", arr_duplicados)
print()

# Teste 3: Elementos aleatórios sem repetição
import random
arr_aleatorio = random.sample(range(1, 11), 10)
print("Teste 3 - Elementos aleatórios sem repetição:")
print("Original:", arr_aleatorio)
insertion_sort(arr_aleatorio)
print("Ordenado:", arr_aleatorio)
print()

# Teste 4: Elementos ordenados na ordem inversa
arr_inverso = [5, 4, 3, 2, 1]
print("Teste 1 - Elementos ordenados na ordem inversa:")
print("Original:", arr_inverso)
insertion_sort(arr_inverso)
print("Ordenado:", arr_inverso)
print()
