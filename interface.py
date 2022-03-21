from funcoes import *
import random
random.seed()

def main():
    print()
    print("***********************************")
    print("    Bem vindo(a) ao jogo Gemas!    ")
    print("***********************************")
    print()

    pontos = 0
    while True:
        nivel_jogo = input("Digite o nível que deseja jogar: ").upper()
        if nivel_jogo == "FÁCIL":
            tamanho_tabuleiro = 3
            break
        elif nivel_jogo == "MÉDIO":
            tamanho_tabuleiro = 5
            break
        elif nivel_jogo == "DIFÍCIL":
            tamanho_tabuleiro = 8
            break
        else:
            print("Nível inválido!!")

    num_cores = int(input("Digite o número de cores (no máximo 7): "))
    tabuleiro = constroi_tabuleiro(tamanho_tabuleiro, tamanho_tabuleiro)
    preenche_tabuleiro(tabuleiro, num_cores)
    imprime_tabuleiro(tabuleiro, tamanho_tabuleiro)
    num_gemas = eliminar(tabuleiro)
    while num_gemas > 0:
        deslocar(tabuleiro)
        preenche_tabuleiro(tabuleiro, num_cores)
        num_gemas = eliminar(tabuleiro)

    imprime_tabuleiro(tabuleiro, tamanho_tabuleiro)



main()