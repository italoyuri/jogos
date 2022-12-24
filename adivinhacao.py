import random
import sys

print('*' * 33)
print('Bem vindo ao jogo de adivinhação!')
print('*' * 33)

numero_secreto_ini = 1
numero_secreto_end = 100

numero_secreto = random.randint(
    numero_secreto_ini,
    numero_secreto_end)

total_de_tentativas = 0
nivel = 0
pontuacao = 1000

while nivel not in [1, 2, 3]:
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    print('*' * 33)
    try:
        nivel = int(input("Defina o nível: "))
        if nivel == 0:
            sys.exit()
        if nivel not in [1, 2, 3]:
            print("Digite apenas 1, 2 ou 3")
            print("Digite 0 para sair")
            print('*' * 33)
    except Exception as e:
        print("Digite apenas 1, 2 ou 3 para jogar")
        print("Digite 0 para sair")
        print('*' * 33)

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}"
          .format(rodada, total_de_tentativas))
    try:
        chute = int(
            input("Digite um número entre {} e {}: "
                  .format(numero_secreto_ini, numero_secreto_end))
        )
        print("Você digitou ", chute)

        if chute < numero_secreto_ini or chute > numero_secreto_end:
            print("Você deve digitar um número entre {} e {}!"
                  .format(numero_secreto_ini, numero_secreto_end))
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto
        pontos_perdidos = abs(chute-numero_secreto)

        if not acertou:
            pontuacao -= pontos_perdidos
        if acertou:
            print(f"Você acertou e fez {pontuacao} pontos!")
            break
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto")
        elif maior:
            print("Você errou! O seu chute foi maior do que o número secreto")
    except Exception as e:
        print("Erro:", e)

print("Fim do jogo")

