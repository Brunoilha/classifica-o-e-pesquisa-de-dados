import random

def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        menor = data[i]
        menor_id = i
        for j in range(i + 1, n):
            if data[j] < menor:
                menor = data[j]
                menor_id = j
        # Troca o menor elemento encontrado com o elemento na posição i
        data[i], data[menor_id] = data[menor_id], data[i]

# Teste 1: Elementos ordenados
arr_ordenado = [1, 2, 3, 4, 5]
print("Teste 4 - Elementos já ordenados:")
print("Original:", arr_ordenado)
selection_sort(arr_ordenado)
print("Ordenado:", arr_ordenado)


# Teste 2: Elementos duplicados
arr_duplicados = [3, 1, 2, 2, 3, 1]
print("Teste 2 - Elementos duplicados:")
print("Original:", arr_duplicados)
selection_sort(arr_duplicados)
print("Ordenado:", arr_duplicados)
print()

# Teste 3: Elementos aleatórios sem repetição
arr_aleatorio = random.sample(range(1, 11), 10)
print("Teste 3 - Elementos aleatórios sem repetição:")
print("Original:", arr_aleatorio)
selection_sort(arr_aleatorio)
print("Ordenado:", arr_aleatorio)
print()

# Teste 4: Elementos ordenados na ordem inversa
arr_inverso = [5, 4, 3, 2, 1]
print("Teste 1 - Elementos ordenados na ordem inversa:")
print("Original:", arr_inverso)
selection_sort(arr_inverso)
print("Ordenado:", arr_inverso)
print()
