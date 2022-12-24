import forca
import adivinhacao

def escolhe_jogo():
    print('*'*40)
    print('{:*^40}'.format("Escolha o seu jogo!"))
    print('*'*40)

    print("(1) Forca (2) Adivinhação")

    jogo = 0
    while jogo not in [1,2]:
        try:
            jogo = int(input("Qual jogo? "))
        except Exception as e:
            pass
    if jogo == 1:
        print("Jogando Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if __name__ == "__main__":
    escolhe_jogo()