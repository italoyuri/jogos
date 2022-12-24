import random
import sys

def jogar():
    print('*'*40)
    print('{:*^40}'.format("Bem-vindo ao jogo de advinhação!"))
    print('*'*40)

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
        print()
        try:
            nivel = int(input("Defina o nível: "))
            if nivel == 0:
                sys.exit()
            if nivel not in [1, 2, 3]:
                print("Digite apenas 1, 2 ou 3")
                print("Digite 0 para sair")
                print()
        except Exception as e:
            print("Digite apenas 1, 2 ou 3 para jogar")
            print("Digite 0 para sair")
            print()

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        try:
            chute = int(
                input(f"Digite um número entre {numero_secreto_ini} e {numero_secreto_end}: ")
            )
            print()
            print(f"Você digitou {chute}")
            print()

            if chute < numero_secreto_ini or chute > numero_secreto_end:
                print(f"Você deve digitar um número entre {numero_secreto_ini} e {numero_secreto_end}!")
                continue

            acertou = chute == numero_secreto
            menor = chute < numero_secreto
            maior = chute > numero_secreto
            pontos_perdidos = abs(chute-numero_secreto)

            if not acertou:
                pontuacao -= pontos_perdidos
            if acertou:
                print(f"Você acertou e fez {pontuacao} pontos!")
                print()
                break
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto")
                print()
            elif maior:
                print("Você errou! O seu chute foi maior do que o número secreto")
                print()
        except Exception as e:
            print("Erro:", e)
    if not acertou:
        print(f"O número secreto era {numero_secreto} e você fez {pontuacao} pontos")
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()