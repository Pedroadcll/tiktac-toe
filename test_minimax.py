import random 

from minimax import obter_melhor_jogada
from cli import verificar_vencedor

def jogadas_disponiveis(tabuleiro):
    return[i for i in range(9) if tabuleiro[i] == '']

def simular_partida(bot_primeiro=true):
    tabuleiro = [' '] * 9

    if bot_primeiro:
        simbolo_x = 'X'
        simbolo_aleatorio = 'O'
        turno_bot = True
    else:
        simbolo_bot = 'O'
        simbolo_aleatorio = 'X'
        turno_bot = False

    while True:
        if turno_bot:
            posicao = obter_melhor_jogada(tabuleiro, simbolo_bot)
            tabuleiro[posicao] = simbolo_bot
        else:
            posicao = random.choice(jogadas_disponiveis(tabuleiro))
            tabuleiro[posicao] = simbolo_aleatorio

        resultado = verificar_vencedor(tabuleiro)

        if resultado is not None:
            return resultado
        
        turno_bot = not turno_bot

