"""Contém todas as funções que são chamadas no módulo "interface",
                   e fazem o jogo funcionar."""

from constantes import *
import random


def constroi_tabuleiro(l, c):
    """Constrói o tabuleiro de acordo com o tamanho que é dado pelo usuário."""
    tabuleiro = []
    for i in range(l):
        tabuleiro.append([])
        for j in range(c):
             tabuleiro[i].append(NADA)
    return tabuleiro


def imprime_tabuleiro(tabuleiro, tam_tabuleiro):
    """Imprime o tabulero para o jogador"""
    if tam_tabuleiro == 3:
        print("{}".format(NIVEL_FACIL))
        print("{}".format(LINHA_NIVEL_FACIL))
    elif tam_tabuleiro == 5:
        print("{}".format(NIVEL_MEDIO))
        print("{}".format(LINHA_NIVEL_MEDIO))
    elif tam_tabuleiro == 8:
        print("{}".format(NIVEL_DIFICIL))
        print("{}".format(LINHA_NIVEL_DIFICIL))

    for i in range(tam_tabuleiro):
        print("{} |".format(i), end=" ")
        for j in range(tam_tabuleiro):
            print(" {} ".format(tabuleiro[i][j]), end="")
            if j == tam_tabuleiro - 1:
                print(" |")

    if tam_tabuleiro == 3:
        print("{}".format(LINHA_NIVEL_FACIL))
    elif tam_tabuleiro == 5:
        print("{}".format(LINHA_NIVEL_MEDIO))
    elif tam_tabuleiro == 8:
        print("{}".format(LINHA_NIVEL_DIFICIL))


def preenche_tabuleiro(tabuleiro, num_cores):
    """Preenche o tabuleiro com as gemas."""
    cores = {"azul": "\033[34m","vermelho": "\033[31m","roxo": "\033[35m","verde": "\033[32m","amarelo": "\033[33m","cinza": "\033[37m","limpa": "\033[m"}
    gemas = ["{}@{}".format(cores["azul"], cores["limpa"]),"{}@{}".format(cores["amarelo"], cores["limpa"]),"{}@{}".format(cores["vermelho"], cores["limpa"]),"{}@{}".format(cores["roxo"], cores["limpa"]),"{}@{}".format(cores["verde"], cores["limpa"]),"{}@{}".format(cores["cinza"], cores["limpa"]),"@"]
    linhas = len(tabuleiro)
    coluna = len(tabuleiro)
    for i in range(linhas):
        for j in range(coluna):
            if tabuleiro[i][j] == " ":
                gema = random.randrange(num_cores)
                tabuleiro[i][j] = gemas[gema]


def permutacao_valida(l1, c1, l2, c2, tabuleiro):
    """Verifica se a permutação feita pelo jogador é válida."""
    # verifica os tabuleiros de tamanhos 5x5 e 8x8
    if len(tabuleiro) >= 5:
        # Verifica permutações válidas na mesma linha
        for i in range(min(l1, l2), len(tabuleiro)):
            for j in range(min(c1, c2), len(tabuleiro)):
                if i == l1 and j == c1 or i == l2 and j == c2:
                    if j < len(tabuleiro) - 1:
                        # Verifica elementos iguais pra direita
                        if tabuleiro[i][j] == tabuleiro[i][j + 1]:
                            if tabuleiro[i][j + 1] == tabuleiro[i][j + 2]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                return True
                    if j > 1:
                        # Verifica elementos iguais pra esquerda
                        if tabuleiro[i][j] == tabuleiro[i][j - 1]:
                            if tabuleiro[i][j - 1] == tabuleiro[i][j - 2]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                return True

        # Verifica permutações válidas na mesma coluna
        for j in range(min(l1, l2), len(tabuleiro)):
            for i in range(min(c1, c2), len(tabuleiro)):
                if j == l1 and i == c1 or j == l2 and i == c2:
                    if j < len(tabuleiro) - 1:
                        # Verifica elementos iguais pra baixo
                        if tabuleiro[j][i] == tabuleiro[j + 1][i]:
                            if tabuleiro[j + 1][i] == tabuleiro[j + 2][i]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                return True
                    if j >= 1:
                        # Verifica elementos iguais pra cima
                        if tabuleiro[j][i] == tabuleiro[j - 1][i]:
                            if tabuleiro[j - 1][i] == tabuleiro[j - 2][i]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                # Permutação válida
                                return True
        return False
    # verifica o tabuleiro de tamanho 3x3
    else:
        for i in range(min(l1, l2), len(tabuleiro)):
            for j in range(min(c1, c2), len(tabuleiro)):
                if i == l1 and j == c1 or i == l2 and j == c2:
                    if j < 2:
                        # Verifica elementos iguais pra direita
                        if tabuleiro[i][0] == tabuleiro[i][1]:
                            if tabuleiro[i][1] == tabuleiro[i][2]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                return True
                    if j == 2:
                        # Verifica elementos iguais pra esquerda
                        if tabuleiro[i][j] == tabuleiro[i][1]:
                            if tabuleiro[i][1] == tabuleiro[i][0]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                return True

        for j in range(min(l1, l2), len(tabuleiro)):
            for i in range(min(c1, c2), len(tabuleiro)):
                if j == l1 and i == c1 or j == l2 and i == c2:
                    if j < 2:
                        # Verifica elementos iguais pra baixo
                        if tabuleiro[j][i] == tabuleiro[1][i]:
                            if tabuleiro[1][i] == tabuleiro[2][i]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                return True
                    if j == 2:
                        # Verifica elementos iguais pra cima
                        if tabuleiro[j][i] == tabuleiro[1][i]:
                            if tabuleiro[1][i] == tabuleiro[0][i]:  # 3 elementos seguidos?
                                # Então é uma permutação válida
                                # Permutação válida
                                return True
        return False


def trocar(l1, c1, l2, c2, tabuleiro):
    """ Troca a gema da linha 1, coluna 1 pela gema da coluna 2, coluna 2, que é dada pelo jogador. """
    anterior = tabuleiro[l1][c1]
    tabuleiro[l1][c1] = tabuleiro[l2][c2]
    tabuleiro[l2][c2] = anterior

    valida = permutacao_valida(l1, c1, l2, c2, tabuleiro)
    if valida:
        return True, tabuleiro

    anterior = tabuleiro[l1][c1]
    tabuleiro[l1][c1] = anterior
    tabuleiro[l2][c2] = tabuleiro[l2][c2]
    return False, tabuleiro


def cadeias_horizontais(tabuleiro):
    """Dá as coordenadas da cadeia horizontal, sendo: [[linha, coluna_inicial, linha, coluna_final]]"""
    for i in range(len(tabuleiro)):
        cadeia_horizontal = []
        comeco = ""
        fim = ""
        cont = 1
        cordenadas = []
        for j in range(len(tabuleiro)):
            if j < len(tabuleiro) - 1:
                if tabuleiro[i][j] == tabuleiro[i][j + 1]:
                    cont += 1
                    if cont >= 3:
                        comeco = ((j + 2) - cont)
                        fim = (j + 1)
                        cordenadas.append(i)
                        cordenadas.append(comeco)
                        cordenadas.append(i)
                        cordenadas.append(fim)
                        cont = 1
                        cadeia_horizontal.append(cordenadas)
                elif cont == 2:
                    cont = 1
        if len(cadeia_horizontal) > 0:
            elimina_cadeia(tabuleiro, cadeia_horizontal)


def cadeias_verticais(tabuleiro):
    """Dá as coordenadas da cadeia vertical, sendo: [[linha_inicial, coluna, linha_final, coluna]]"""
    for j in range(len(tabuleiro)):
        cadeia_vertical = []
        comeco = ""
        fim = ""
        cont = 1
        cordenadas = []
        for i in range(len(tabuleiro)):
            if i < len(tabuleiro) - 1:
                if tabuleiro[i][j] == tabuleiro[i + 1][j]:
                    cont += 1
                    if cont >= 3:
                        comeco = ((i + 2) - cont)
                        fim = (i + 1)
                        cordenadas.append(comeco)
                        cordenadas.append(j)
                        cordenadas.append(fim)
                        cordenadas.append(j)
                        cont = 1
                        cadeia_vertical.append(cordenadas)
                elif cont == 2:
                    cont = 1
        if len(cadeia_vertical) > 0:
            elimina_cadeia(tabuleiro, cadeia_vertical)


def elimina_cadeia(tabuleiro, cadeia):
    """ Substitui por uma string vazia (" ") as gemas compreendidas numa cadeia."""
    linha_inicial = 0
    linha_final = 0
    coluna_inicial = 0
    coluna_final = 0

    for i in range(len(cadeia)):
        for j in range(len(cadeia[i])):
            linha_inicial = cadeia[i][0]
            linha_final = cadeia[i][2]
            coluna_inicial = cadeia[i][1]
            coluna_final = cadeia[i][3]

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if i >= linha_inicial and j >= coluna_inicial and i <= linha_final and j <= coluna_final:
                tabuleiro[i][j] = " "


def eliminar(tabuleiro):
    """ Elimina as cadeias substituindo gemas por " " e retorna o número de gemas destruídas. """
    cadeias_horizontais(tabuleiro)
    cadeias_verticais(tabuleiro)
    num_gemas = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == " ":
                num_gemas += 1
    return num_gemas


def deslocar_coluna(tabuleiro, i):
    """ Desloca coluna por coluna, os elementos que estão acima de espaços vazios (" ") para esses espaços vazios,
               e onde esses elemntos deslocados estavam, ficam vazios (" ")."""
    for coluna in range(len(tabuleiro)+1):
        if coluna == i:
            cont = 0
            for linha in range(len(tabuleiro)):
                if linha > 0 and tabuleiro[linha][coluna] == " " and tabuleiro[linha-1][coluna] != " ":
                    cont += 1

            while cont > 0:
                for linha in range(len(tabuleiro)):
                    if linha > 0 and tabuleiro[linha][coluna] == " " and tabuleiro[linha-1][coluna] != " ":
                        tabuleiro[linha][coluna] = tabuleiro[linha-1][coluna]
                        tabuleiro[linha - 1][coluna] = " "
                cont -= 1
    return


def deslocar(tabuleiro):
    """Desloca de uma vez só todas as colunas e linhas que estão acima de espaços vazios."""
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            if tabuleiro[linha][coluna] == " ":
                deslocar_coluna(tabuleiro, coluna)


def obter_dica(tabuleiro):
    """Verfica as possibilidades de permutação, seja na horizontal, seja na vertical."""
    linha = -1
    coluna = -1

    # Verifica os tabuleiros de tamanho 5x5 e 8x8
    if len(tabuleiro) >= 5:
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                if j < len(tabuleiro) - 3:  # Verifica pra direita
                    if tabuleiro[i][j] == tabuleiro[i][j + 1]:
                        if tabuleiro[i][j + 1] == tabuleiro[i][j + 3]:
                            linha = i
                            coluna = j + 2

                if j > 3:  # Verifica pra esquerda
                    if tabuleiro[i][j] == tabuleiro[i][j - 1]:
                        if tabuleiro[i][j - 1] == tabuleiro[i][j - 3]:
                            linha = i
                            coluna = j - 2


        for j in range(len(tabuleiro)):
            for i in range(len(tabuleiro)):
                if i < len(tabuleiro) - 3:  # Verifica pra baixo
                    if tabuleiro[i][j] == tabuleiro[i + 1][j]:
                        if tabuleiro[i + 1][j] == tabuleiro[i + 3][j]:
                            linha = j
                            coluna = i + 2

                if i > 3:  # Verifica pra cima
                    if tabuleiro[i][j] == tabuleiro[i - 1][j]:
                        if tabuleiro[i - 1][j] == tabuleiro[i - 3][j]:
                            linha = j
                            coluna = i - 2
        return linha, coluna

    # Verifica o tabuleiro de tamanho 3x3
    else:
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)): # verifica pra baixo
                if i < 2:
                    if tabuleiro[i][0] == tabuleiro[i][1] or tabuleiro[i][1] == tabuleiro[i][2]:
                        if tabuleiro[i+1][2] == tabuleiro[i][0] or tabuleiro[i+1][0] == tabuleiro[i][1]:
                            linha = i
                            coluna = 2

                if i == 2: # verefica pra cima
                    if tabuleiro[i][0] == tabuleiro[i][1] or tabuleiro[i][1] == tabuleiro[i][2]:
                        if tabuleiro[i - 1][2] == tabuleiro[i][0] or tabuleiro[i - 1][0] == tabuleiro[i][1]:
                            linha = i
                            coluna = 2

        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)): # verifica pra direita
                if j < 2:
                    if tabuleiro[0][j] == tabuleiro[1][j] or tabuleiro[1][j] == tabuleiro[2][j]:
                        if tabuleiro[2][j+1] == tabuleiro[0][j] or tabuleiro[0][j+1] == tabuleiro[1][j]:
                            linha = j
                            coluna = 1

                if j == 2: # verefica pra esquerda
                    if tabuleiro[0][j] == tabuleiro[1][j] or tabuleiro[1][j] == tabuleiro[2][j]:
                        if tabuleiro[2][j - 1] == tabuleiro[0][j] or tabuleiro[0][j - 1] == tabuleiro[1][j]:
                            linha = j
                            coluna = 1


        # verifica possibilidades de gemas do meio
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)): # verifica pra baixo
                if i < 2:
                    if tabuleiro[i][0] == tabuleiro[i][2]:
                        if tabuleiro[i+1][1] == tabuleiro[i][0]:
                            linha = i
                            coluna = 1

                if i == 2: # verefica pra cima
                    if tabuleiro[i][0] == tabuleiro[i][2]:
                        if tabuleiro[i-1][1] == tabuleiro[i][0]:
                            linha = i
                            coluna = 1

        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)): # verifica pra direita
                if j < 2:
                    if tabuleiro[0][j] == tabuleiro[2][j]:
                        if tabuleiro[1][j+1] == tabuleiro[0][j]:
                            linha = 1
                            coluna = j

                if j == 2: # verefica pra esquerda
                    if tabuleiro[0][j] == tabuleiro[2][j]:
                        if tabuleiro[1][j-1] == tabuleiro[0][j]:
                            linha = 1
                            coluna = j

        return linha, coluna


def exitem_movimentos_validos(tabuleiro):
    """Verifica se existem movimentos válidos há sejem feitos."""
    existe = True
    permutacao = obter_dica(tabuleiro)
    if permutacao[0] == -1 and permutacao[1] == -1:
        existe = False

    return existe
