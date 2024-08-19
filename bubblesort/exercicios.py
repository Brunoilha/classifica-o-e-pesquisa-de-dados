# 1
lista = [1, 8, 5, 6, 9, 7]
n = len(lista)
for i in range(n):
    trocou = False
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
          
            lista[j], lista[j+1] = lista[j+1], lista[j]
            trocou = True
    if not trocou:
        break

print(lista)
def bubble(lista):
    lista = [1, 8, 5, 6, 9, 7]
    n = len(lista)
    for i in range(n):
        trocou = False
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
          
            lista[j], lista[j+1] = lista[j+1], lista[j]
            trocou = True
        if not trocou:
            break

arr_ordenado = [1, 2, 3, 4, 5]
print("Teste 4 - Elementos já ordenados:")
print("Original:", arr_ordenado)
bubble(arr_ordenado)
print("Ordenado:", arr_ordenado)

# Teste 2: Elementos duplicados
arr_duplicados = [3, 1, 2, 2, 3, 1]
print("Teste 2 - Elementos duplicados:")
print("Original:", arr_duplicados)
bubble(arr_duplicados)
print("Ordenado:", arr_duplicados)
print()

# Teste 3: Elementos aleatórios sem repetição
import random
arr_aleatorio = random.sample(range(1, 11), 10)
print("Teste 3 - Elementos aleatórios sem repetição:")
print("Original:", arr_aleatorio)
bubble(arr_aleatorio)
print("Ordenado:", arr_aleatorio)
print()

# Teste 4: Elementos ordenados na ordem inversa
arr_inverso = [5, 4, 3, 2, 1]
print("Teste 1 - Elementos ordenados na ordem inversa:")
print("Original:", arr_inverso)
bubble(arr_inverso)
print("Ordenado:", arr_inverso)
print()
