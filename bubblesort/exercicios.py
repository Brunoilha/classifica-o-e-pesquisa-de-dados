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

