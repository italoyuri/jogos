import random

import unicodedata

import generics


def jogar():
    generics.imprime_mensagem_abertura(__file__)
    palavra_secreta = carrega_palavra_secreta()

    palavra_secreta_mascara = '_' * len(palavra_secreta)

    erros = 0
    tentativas = 7
    terminar = False

    while not terminar:
        print(f"A palavra secreta é {palavra_secreta_mascara}")

        chute = input("Qual letra? ").strip().upper()

        palavra_secreta_mascara = trata_palavra_secreta(palavra_secreta, palavra_secreta_mascara, chute)

        if chute not in palavra_secreta:
            erros += 1
            desenha_forca(erros)
            print(f"Você ainda tem {tentativas - erros} tentativas")
        if erros == tentativas:
            terminar = mensagem_perdedor(palavra_secreta)
        if palavra_secreta_mascara == palavra_secreta:
            terminar = mensagem_ganhador(palavra_secreta)
    generics.mensagem_final()


def mensagem_perdedor(palavra_secreta):
    print(f"Você foi enforcado! A palavra era {palavra_secreta}!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    return True


def mensagem_ganhador(palavra_secreta):
    print(f"Você acertou a palavra {palavra_secreta}!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    return True


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def carrega_palavra_secreta():
    with open('palavras', encoding='utf-8') as palavra_arquivo:
        palavras = [linha.strip() for linha in palavra_arquivo]

    palavra_secreta = palavras[random.randint(0, len(palavras) - 1)]
    palavra_secreta = ''.join(
        ch for ch in unicodedata.normalize('NFKD', palavra_secreta) if not unicodedata.combining(ch)).upper()

    return palavra_secreta


def trata_palavra_secreta(palavra_secreta, palavra_secreta_mascara, chute):
    for i in range(len(palavra_secreta)):
        if chute == palavra_secreta[i]:
            palavra_secreta_mascara = list(palavra_secreta_mascara)
            palavra_secreta_mascara[i] = chute
            palavra_secreta_mascara = str(palavra_secreta_mascara) \
                .replace("'", "") \
                .replace(",", "") \
                .strip("[]") \
                .replace(" ", "")
    return palavra_secreta_mascara


if __name__ == "__main__":
    jogar()
