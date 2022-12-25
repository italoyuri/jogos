import sys

import adivinhacao
import forca


def escolhe_jogo():


    jogo = 0
    while jogo not in [1, 2]:
        try:
            print('*' * 40)
            print('{:*^40}'.format("Escolha o seu jogo!"))
            print('*' * 40)
            print("(1) Forca (2) Adivinhação (0) Sair")
            jogo = int(input("Qual jogo? "))
            if jogo == 1:
                print("Jogando Forca")
                forca.jogar()
            elif jogo == 2:
                print("Jogando Adivinhação")
                adivinhacao.jogar()
            elif jogo == 0:
                sys.exit()
        except Exception as e:
            pass



if __name__ == "__main__":
    escolhe_jogo()
