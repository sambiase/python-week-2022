tmp: list
lista = [23, 1, 2, 5, 7, 76, 8]

for i in range(len(lista)):
    for v in range(i+1,len(lista)):
        if lista[i] > lista[v]:
            tmp=lista[v]
            lista[v]=lista[i]
            lista[i]=tmp

print(lista)
