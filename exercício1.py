import random

numero_secreto = round (random.randrange(0, 101))
total_de_tentativas = 0
pontos = 1000

print('Qual o nível de dificuldade?')
print(' (1) Fácil, (2) Médio, (3) Difícil')

nivel = int(input('Define o nível: '))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel ==2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

    chute_str = input('Digite um número de 1 a 100: ')
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print(f'Você acertou e fez {pontos} pontos!')
    else:
        if(maior):
            print(f'Seu número foi maior, você perdeu {pontos} pontos!')
        elif(menor):
            (print(f'Seu número foi menor, você perdeu {pontos} pontos!'))
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print('Fim do jogo!')


