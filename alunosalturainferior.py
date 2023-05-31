alunos = []
idades = []
alturas = []

for i in range(30):
    nome = input()
    idade = int(input())
    altura = float(input())
    alunos.append(nome)
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)

abaixo_media = []

for i in range(len(alunos)):
    if idades[i] > 13 and alturas[i] < round(media_altura,2):
        abaixo_media.append(alunos[i])

print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MĆ‰DIA")
for aluno in abaixo_media:
    print(aluno)
