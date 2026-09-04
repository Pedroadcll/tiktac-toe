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
        resultado = verificar_vencedor(tabuleiro)

        if resultado is not None:
            return resultado
        
        if turno_bot:
            posicao = obter_melhor_jogada(tabuleiro, simbolo_bot)
            tabuleiro[posicao] = simbolo_bot
        else:
            disponiveis = jogadas_disponiveis(tabuleiro)

            if not disponiveis:
                return 'Empate'
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

    for i in range(50):
        resultado = simular_partida(bot_primeiro=True)

        if i < 10:
            print(f"Partida {i + 1}: {resultado}")

        if resultado == 'X':
            vitorias += 1
        elif resultado == 'O':
            derrotas += 1
        else:
            empates += 1

    for _ in range(50):
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

def test_bot_escolhe_vitoria_imediata():
    tabuleiro = [
        'X', 'X', ' ',
        'O', 'O', ' ',
        ' ', ' ', ' '
    ]

    jogada = obter_melhor_jogada(tabuleiro, 'X')

    print("Jogada escolhida:", jogada)

    assert jogada == 2

def mostrar_tabuleiro(tabuleiro):
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()


def test_partida_debug():
    tabuleiro = [' '] * 9

    simbolo_bot = 'X'
    simbolo_aleatorio = 'O'
    turno_bot = True

    while True:
        resultado = verificar_vencedor(tabuleiro)

        if resultado is not None:
            print("RESULTADO FINAL:", resultado)
            mostrar_tabuleiro(tabuleiro)
            break

        if turno_bot:
            posicao = obter_melhor_jogada(tabuleiro, simbolo_bot)
            print(f"BOT ({simbolo_bot}) jogou na posição {posicao}")
            tabuleiro[posicao] = simbolo_bot

        else:
            disponiveis = jogadas_disponiveis(tabuleiro)

            if not disponiveis:
                print("NÃO HÁ JOGADAS DISPONÍVEIS")
                print("verificar_vencedor retornou:", verificar_vencedor(tabuleiro))
                mostrar_tabuleiro(tabuleiro)
                break

            posicao = random.choice(disponiveis)
            print(f"ALEATÓRIO ({simbolo_aleatorio}) jogou na posição {posicao}")
            tabuleiro[posicao] = simbolo_aleatorio

        mostrar_tabuleiro(tabuleiro)
        turno_bot = not turno_bot