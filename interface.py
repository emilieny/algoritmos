"""
Módulo que faz interface com o jogador, recebe as jogadas e
             contém a função principal do jogo.
"""

from funcoes import *
import random
random.seed()

def main():
    """
    Contém os comandos que obtém os parametros necessários para criação
    do jogo.
    """
    print()
    print("\033[31m************************************************************\033[m")
    print("                BEM VINDO(A) AO JOGO GEMAS!                 ")
    print("\033[31m************************************************************\033[m")
    print()

    print(INSTRUCOES)
    print()
    print()

    pontos = 0
    while True:
        nivel_jogo = input("Digite o nível que deseja jogar(Fácil, Médio ou Difícil): ").upper()
        if nivel_jogo == "FÁCIL" or nivel_jogo == "FACIL":
            tamanho_tabuleiro = 3
            break
        elif nivel_jogo == "MÉDIO" or nivel_jogo == "MEDIO":
            tamanho_tabuleiro = 5
            break
        elif nivel_jogo == "DIFÍCIL" or nivel_jogo == "DIFICIL":
            tamanho_tabuleiro = 8
            break
        else:
            print("Nível inválido!!")

    while True:
        try:
            num_cores = int(input("Digite o número de cores (entre 3 e 7): "))
            if num_cores > 2 and num_cores <= 7:
                break
            else:
                print("\033[31mDigite um número de cores válido!\033[m")
        except ValueError:
            print("\033[31mDigite um número de cores válido!\033[m")

    # cria o tabuleiro com as configurações iniciais
    tabuleiro = constroi_tabuleiro(tamanho_tabuleiro, tamanho_tabuleiro)
    preenche_tabuleiro(tabuleiro, num_cores)
    num_gemas = eliminar(tabuleiro)
    while num_gemas > 0:
        deslocar(tabuleiro)
        preenche_tabuleiro(tabuleiro, num_cores)
        num_gemas = eliminar(tabuleiro)
    print()
    print(INICIO_DE_JOGO)
    print()

    # Laço principal
    while exitem_movimentos_validos(tabuleiro): # O jogo só funciona se existirem movimentos válidos
        imprime_tabuleiro(tabuleiro, tamanho_tabuleiro)
        comando = input("Digite um comando ( P-(Permutação), D-(Dica), S-(Sair), A-(Ajuda) ): ").upper()
        if comando == "P":
            while True:
                try:
                    linha1 = int(input("Digite a linha da primeira gema: "))
                    coluna1 = int(input("Digite a coluna da primeira gema: "))
                    linha2 = int(input("Digite a linha da segunda gema: "))
                    coluna2 = int(input("Digite a coluna da segunda gema: "))
                    print()
                    valido = trocar(linha1, coluna1, linha2, coluna2, tabuleiro)
                    break

                except ValueError:
                    print("\033[31mDIGITE UM NÚMERO INTEIRO!\033[m")
            if valido[0] == True:
                num_gemas = eliminar(tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    deslocar(tabuleiro)
                    preenche_tabuleiro(tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: {} gemas foram destruidas!".format(num_gemas))
                    print()
                    imprime_tabuleiro(tabuleiro, tamanho_tabuleiro)
                    print()
                    num_gemas = eliminar(tabuleiro)
                pontos += total_gemas
                print()
                print("Você destruiu {} gemas! ".format(total_gemas))
                print()
            else:
                print()
                print("Movimento inválido! ")
                print()

        elif comando == "D":
            pontos -= 1
            dica = obter_dica(tabuleiro)
            print()
            print("Dica: Tente permutar a gema com as seguintes coordenadas: {}, {}".format(dica[0], dica[1]))
            print()

        elif comando == "S":
            print(FIM_DE_JOGO)
            print("Você destruiu um total de {} gemas".format(pontos))
            return

        elif comando == "A":
            print(AJUDA)
            print()

        else:
            print()
            print("\033[31mComando inválido! Tente ajuda para receber uma lista de comandos válidos.\033[m")
            print()

    if pontos == 0:
        print(SEM_MOVIMENTOS_VALIDOS_NO_COMECO) # Quando o tabuleiro construído não possui permutações válida

    else:
        print(SEM_MOVIMENTOS_VALIDOS)
        print("Você destruiu um total de {} gemas ".format(pontos))

main()