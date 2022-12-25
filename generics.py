import os


def imprime_mensagem_abertura(nome):
    print('{}\n{:*^40}\n{}'.format('*' * 40, f"Bem-vindo ao jogo da {os.path.basename(nome.strip('.py'))}!",
                                   '*' * 40))


def mensagem_final():
    print("Fim de jogo")
