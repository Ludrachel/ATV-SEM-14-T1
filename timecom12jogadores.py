jogadores = []

for i in range(12):
    nome = input()
    altura = float(input())
    jogadores.append([nome, altura])

jogador_mais_alto = jogadores[0]
for jogador in jogadores:
    if jogador[1] > jogador_mais_alto[1]:
        jogador_mais_alto = jogador
print("JOGADOR MAIS ALTO DO TIME")
print(jogador_mais_alto[0])
print(f'{jogador_mais_alto[1]:.2f}')

soma_alturas = 0
for jogador in jogadores:
    soma_alturas += jogador[1]

media_alturas = soma_alturas / len(jogadores)
print("ALTURA MÉDIA DO TIME")
print(f'{media_alturas:.2f}')

jogadores_acima_da_media = []
for jogador in jogadores:
    if jogador[1] > media_alturas:
        jogadores_acima_da_media.append(jogador)

print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
for jogador in jogadores_acima_da_media:
    print(jogador[0])
    print(f'{jogador[1]:.2f}')
