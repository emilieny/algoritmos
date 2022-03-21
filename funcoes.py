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


def cadeias_horizontais(tabuleiro):
    """Dá as coordenada da cadeia horizontal, sendo: [[linha, coluna_inicial, linha, coluna_final]]"""
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
    cadeias_horizontais(tabuleiro)
    cadeias_verticais(tabuleiro)
    num_gemas = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == " ":
                num_gemas += 1
    return num_gemas


def deslocar_coluna(tabuleiro, i):
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
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            if tabuleiro[linha][coluna] == " ":
                deslocar_coluna(tabuleiro, coluna)