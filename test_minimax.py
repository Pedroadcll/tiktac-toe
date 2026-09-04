import random 

from minimax import obter_melhor_jogada
from cli import verificar_vencedor

def jogadas_disponiveis(tabuleiro):
    return[i for i in range(9) if tabuleiro[i] == '']

def simular_partida(bot_primeiro=True):
    tabuleiro = [' '] * 9

    if bot_primeiro:
        simbolo_bot = 'X'
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

def test_minimax_nunca_perde():
    derrotas = 0
    vitorias = 0
    empates = 0

    for _ in range(500):
        resultado = simular_partida(bot_primeiro=True)

        if resultado == 'X':
            vitorias += 1
        elif resultado == 'O':
            derrotas += 1
        else:
            empates += 1

    for _ in range(500):
        resultado = simular_partida(bot_primeiro=False)

        if resultado == 'O':
            vitorias += 1
        elif resultado == 'X':
            derrotas += 1
        else:
            empates += 1

    print()
    print("=== Resultado do teste ===")
    print(f"Vitórias do Minimax: {vitorias}")
    print(f"Empates: {empates}")
    print(f"Derrotas: {derrotas}")

    assert derrotas == 0