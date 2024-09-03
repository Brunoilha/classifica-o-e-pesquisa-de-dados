#quick
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
#shell
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
#tempo
import time
import random

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data.copy())
    end_time = time.time()
    return end_time - start_time

sizes = [100, 1000, 5000, 10000]  # Exemplo de tamanhos de lista
sort_functions = [insertion_sort, selection_sort, bubble_sort, merge_sort, quick_sort, shell_sort]
types_of_lists = ['sorted', 'reverse_sorted', 'with_duplicates', 'random']

for size in sizes:
    sorted_list = list(range(size))
    reverse_sorted_list = list(range(size, 0, -1))
    duplicates_list = [random.randint(0, size // 10) for _ in range(size)]
    random_list = [random.randint(0, size) for _ in range(size)]

    for sort_function in sort_functions:
        for list_type in types_of_lists:
            if list_type == 'sorted':
                data = sorted_list
            elif list_type == 'reverse_sorted':
                data = reverse_sorted_list
            elif list_type == 'with_duplicates':
                data = duplicates_list
            elif list_type == 'random':
                data = random_list
            
            time_taken = measure_time(sort_function, data)
            print(f"{sort_function.__name__} - {list_type} - {size} items: {time_taken:.6f} seconds")

###
# 4 Sobre o Shell Sort (a) Verdadeira
# 5 Pior Escolha para o Pivô no QuickSort (c) O menor elemento da lista não ordenada
# 6 Comparação entre Insertion Sort e Bubble Sort (a) Verdadeira
# 7 Pivô Recomendado para o Quicksort (C) O elemento central
# 8 Lista Parcialmente Ordenada após Três Passos de Bubble Sort (e) [1, 3, 7, 9, 8, 10, 12, 13, 15, 19]

