import math
from cli import verificar_vencedor

def minimax(tabuleiro, profundidade, is_maximizing, simbolo_bot, simbolo_humano):
    resultado = verificar_vencedor(tabuleiro)
    
    if resultado == simbolo_bot:
        return 10 - profundidade 
    elif resultado == simbolo_humano:
        return -10 + profundidade 
    elif resultado == 'Empate':
        return 0
        
    if is_maximizing:
        melhor_pontuacao = -math.inf
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = simbolo_bot 
                pontuacao = minimax(tabuleiro, profundidade + 1, False, simbolo_bot, simbolo_humano)
                tabuleiro[i] = ' ' 
                melhor_pontuacao = max(pontuacao, melhor_pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = math.inf
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = simbolo_humano
                pontuacao = minimax(tabuleiro, profundidade + 1, True, simbolo_bot, simbolo_humano)
                tabuleiro[i] = ' '
                melhor_pontuacao = min(pontuacao, melhor_pontuacao)
        return melhor_pontuacao

def obter_melhor_jogada(tabuleiro, simbolo_bot):
    simbolo_humano = 'X' if simbolo_bot == 'O' else 'O'
    melhor_pontuacao = -math.inf
    melhor_movimento = -1
    
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = simbolo_bot
            pontuacao = minimax(tabuleiro, 0, False, simbolo_bot, simbolo_humano)
            tabuleiro[i] = ' '
            
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_movimento = i
                
    return melhor_movimento