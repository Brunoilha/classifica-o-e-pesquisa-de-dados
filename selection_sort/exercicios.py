def insertion_sort(data):
    n = len(data)
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = tmp

# Exemplo de uso
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    insertion_sort(data)
    print("Sorted array:", data)



def insertion_sort_easy(data):
    n = len(data)
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = tmp

# Testando a versão easy
def test_insertion_sort_easy():
    tests = {
        "already_sorted": [1, 2, 3, 4, 5],
        "reverse_order": [5, 4, 3, 2, 1],
        "duplicates": [3, 1, 2, 1, 2],
        "random": [4, 2, 5, 1, 3]
    }
    
    for description, data in tests.items():
        sorted_data = data.copy()
        insertion_sort_easy(sorted_data)
        print(f"Test - {description}: {sorted_data}")

test_insertion_sort_easy()


# lista encadeadas
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontra o menor elemento na parte não ordenada
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Troca o elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Teste 1: Elementos ordenados na ordem inversa
arr_inverso = [5, 4, 3, 2, 1]
print("Teste 1 - Elementos ordenados na ordem inversa:")
print("Original:", arr_inverso)
sorted_inverso = selection_sort(arr_inverso)
print("Ordenado:", sorted_inverso)
print()

# Teste 2: Elementos duplicados
arr_duplicados = [3, 1, 2, 2, 3, 1]
print("Teste 2 - Elementos duplicados:")
print("Original:", arr_duplicados)
sorted_duplicados = selection_sort(arr_duplicados)
print("Ordenado:", sorted_duplicados)
print()

# Teste 3: Elementos aleatórios sem repetição
arr_aleatorio = random.sample(range(1, 11), 10)
print("Teste 3 - Elementos aleatórios sem repetição:")
print("Original:", arr_aleatorio)
sorted_aleatorio = selection_sort(arr_aleatorio)
print("Ordenado:", sorted_aleatorio)
print()

# Teste 4: Elementos já ordenados
arr_ordenado = [1, 2, 3, 4, 5]
print("Teste 4 - Elementos já ordenados:")
print("Original:", arr_ordenado)
sorted_ordenado = selection_sort(arr_ordenado)
print("Ordenado:", sorted_ordenado)
