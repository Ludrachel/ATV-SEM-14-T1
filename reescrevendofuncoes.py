def comprimento(lista):
    tamanho = 0
    for item in lista:
        tamanho += 1
    return tamanho

def inverter(lista):
    num_invertidos = []
    for i in range(comprimento(lista) -1,-1,-1):
        num_invertidos.append(lista[i])
    return num_invertidos

def minimo(lista):
    num_menor = lista[0]
    for item in lista:
        if item < num_menor:
            num_menor = item
    return num_menor

def maximo(lista):
    num_maior = lista[0]
    for item in lista:
        if item > num_maior:
            num_maior = item
    return num_maior

def soma(lista):
    total = 0
    for item in lista:
        total += item
    return total

lista = []
while True:
    l = int(input())
    if l == 0:
        break
    lista.append(l)

print(lista)
print(comprimento(lista))
print(inverter(lista))
print(minimo(lista))
print(maximo(lista))
print(soma(lista))
