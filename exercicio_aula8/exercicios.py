##1
def busca_binaria_iterativa(arr, x):
    baixo = 0
    alto = len(arr) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        
        if arr[meio] == x:
            return meio  
        elif arr[meio] < x:
            baixo = meio + 1  
        else:
            alto = meio - 1  
    
    return -1  

def busca_binaria_recursiva(arr, x, baixo=0, alto=None):
    if alto is None:
        alto = len(arr) - 1
    
    if baixo > alto:
        return -1  # Elemento não encontrado
    
    meio = (baixo + alto) // 2
    
    if arr[meio] == x:
        return meio  # Elemento encontrado
    elif arr[meio] < x:
        return busca_binaria_recursiva(arr, x, meio + 1, alto)  
    else:
        return busca_binaria_recursiva(arr, x, baixo, meio - 1)  


##2
import math

def pesquisa_por_salto(arr, x):
    n = len(arr)
    passo = int(math.sqrt(n))  
    baixo = 0
    alto = min(passo, n)  
    
    
    while arr[alto - 1] < x:
        baixo = alto
        alto = min(alto + passo, n)
        if baixo >= n:  
            return -1
    
    
    for i in range(baixo, alto):
        if arr[i] == x:
            return i 
    return -1  

def pesquisa_fibonacci(arr, x):
    n = len(arr)
    fib_m_minus_2 = 0  # (m-2)'th Fibonacci No.
    fib_m_minus_1 = 1  # (m-1)'th Fibonacci No.
    fib_m = fib_m_minus_1 + fib_m_minus_2  # Fibonacci m = fib(m-1) + fib(m-2)

    # Encontra o maior número Fibonacci menor ou igual ao tamanho da lista
    while fib_m < n:
        fib_m = fib_m_minus_1 + fib_m_minus_2
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m

    # Marca a posição inicial
    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m_minus_2, n-1)

        if arr[i] == x:
            return i
        elif arr[i] < x:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            offset = i
        else:
            fib_m = fib_m_minus_2
            fib_m_minus_1 -= fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1

   
    if fib_m_minus_1 and arr[offset + 1] == x:
        return offset + 1
    
    return -1

##3
import random
import time
import math


arr = sorted(random.sample(range(1, 100000), 10000))


def medir_tempo(func, arr, x):
    start_time = time.time()
    func(arr, x)
    end_time = time.time()
    return end_time - start_time


x = arr[5000]  


tempo_binaria_iterativa = medir_tempo(busca_binaria_iterativa, arr, x)
tempo_binaria_recursiva = medir_tempo(busca_binaria_recursiva, arr, x)
tempo_jump_search = medir_tempo(pesquisa_por_salto, arr, x)
tempo_fibonacci_search = medir_tempo(pesquisa_fibonacci, arr, x)

print(f"Tempo busca binária iterativa: {tempo_binaria_iterativa:.6f} segundos")
print(f"Tempo busca binária recursiva: {tempo_binaria_recursiva:.6f} segundos")
print(f"Tempo busca por salto: {tempo_jump_search:.6f} segundos")
print(f"Tempo busca Fibonacci: {tempo_fibonacci_search:.6f} segundos")






