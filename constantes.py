"""Contém as constantes usadas no jogo."""

NADA = " "
NIVEL_FACIL = "     0  1  2      "
LINHA_NIVEL_FACIL = "  +-----------+  "
NIVEL_MEDIO = "     0  1  2  3  4     "
LINHA_NIVEL_MEDIO = "  +-----------------+  "
NIVEL_DIFICIL = "     0  1  2  3  4  5  6  7   "
LINHA_NIVEL_DIFICIL = "  +--------------------------+  "
INSTRUCOES = """Você deve tentar permutar gemas para que elas formem cadeias
            de gemas iguais, e sejam destruídas."""

INICIO_DE_JOGO = "\033[34mVAMOS COMEÇAR O JOGO!\033[m"
FIM_DE_JOGO = "FIM DE JOGO!"
SEM_MOVIMENTOS_VALIDOS = "FIM DE JOGO: NÃO EXISTEM MAIS MOVIMENTOS VALIDOS!"
SEM_MOVIMENTOS_VALIDOS_NO_COMECO = "NÃO EXISTEM MOVIMENTOS VÁLIDOS NO MOMENTO, COMECE O JOGO NOVAMENTE!"
AJUDA = """\033[34m
            ==================AJUDA=================
             Permutação: permuta Gemas
             Dica: solicita uma dica (perde 1 ponto)
             Sair: termina o jogo
            ========================================
            \033[m """