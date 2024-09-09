#maximo
def heapify(arr, n, i):
    largest = i  # Inicializa o maior como raiz
    l = 2 * i + 1  # Filho esquerdo
    r = 2 * i + 2  # Filho direito

    # Verifica se o filho esquerdo é maior que a raiz
    if l < n and arr[i] < arr[l]:
        largest = l

    # Verifica se o filho direito é maior que a raiz
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Se o maior não for a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca

        # Recursivamente transforma o subárvore afetado em heap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai os elementos um por um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move o atual root para o final
        heapify(arr, i, 0)  # Chama heapify no heap reduzido

#minimo
def heapify_min(arr, n, i):
    smallest = i  # Inicializa o menor como raiz
    l = 2 * i + 1  # Filho esquerdo
    r = 2 * i + 2  # Filho direito

    # Verifica se o filho esquerdo é menor que a raiz
    if l < n and arr[i] > arr[l]:
        smallest = l

    # Verifica se o filho direito é menor que a raiz
    if r < n and arr[smallest] > arr[r]:
        smallest = r

    # Se o menor não for a raiz
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Troca

        # Recursivamente transforma o subárvore afetado em heap
        heapify_min(arr, n, smallest)
      def heapSort_min(arr):
    n = len(arr)

    # Constrói um heap mínimo
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)

    # Extrai os elementos um por um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move o atual root para o final
        heapify_min(arr, i, 0)  # Chama heapify no heap reduzido
      
#CountingSort
def countingSort(arr):
    if len(arr) == 0:
        return arr

    # Encontra o valor máximo e mínimo na lista
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Cria o array de contagem
    count = [0] * range_of_elements

    # Preenche o array de contagem
    for num in arr:
        count[num - min_val] += 1

    # Preenche o array ordenado
    index = 0
    for i in range(range_of_elements):
        while count[i] > 0:
            arr[index] = i + min_val
            index += 1
            count[i] -= 1


