def count(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

lista = []

while True:
    n = int(input())
    if n == 0:
        break
    lista.append(n)

valor_procurado = int(input())
print(lista)
print(valor_procurado)
print(count(lista, valor_procurado))
