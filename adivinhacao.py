import random

print('*' * 33)
print('Bem vindo ao jogo de adivinhação!')
print('*' * 33)

numero_secreto_ini = 1
numero_secreto_end = 50
numero_secreto = random.randint(
    numero_secreto_ini,
    numero_secreto_end)

total_de_tentativas = 3

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
        menor   = chute < numero_secreto
        maior   = chute > numero_secreto

        if acertou:
            print("Você acertou!")
            break
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto")
        elif maior:
            print("Você errou! O seu chute foi maior do que o número secreto")
    except Exception as e:
        print("Erro:", e)

print("Fim do jogo")
print("O número secreto é", numero_secreto)
