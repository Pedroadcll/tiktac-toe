def exibir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        linha = [tabuleiro[i * 3 + j] if tabuleiro[i * 3 + j] != ' ' else str(i * 3 + j + 1) for j in range(3)]
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")


def obter_jogada_humano(tabuleiro):
    while True:
        try:
            posicao = int(input("Escolha uma posicao livre (1-9): ")) - 1
            if 0 <= posicao <= 8 and tabuleiro[posicao] == ' ':
                return posicao
            print("Posicao invalida ou ja ocupada! Tente novamente.")
        except ValueError:
            print("Entrada invalida! Por favor, digite um numero de 1 a 9.")


def verificar_vencedor(tabuleiro):
    combinacoes_vitoria = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for a, b, c in combinacoes_vitoria:
        if tabuleiro[a] != ' ' and tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return tabuleiro[a]  # Retorna 'X' ou 'O'
            
    if ' ' not in tabuleiro:
        return 'Empate'
        
    return None  


def iniciar_jogo(funcao_bot=None):
    tabuleiro = [' '] * 9
    print("=== JOGO DA VELHA CONTRA I.A. ===")
    
    humano_primeiro = input("Deseja ser o primeiro a jogar? (s/n): ").strip().lower() == 's'
    simbolo_humano = 'X' if humano_primeiro else 'O'
    simbolo_bot = 'O' if humano_primeiro else 'X'
    turno_humano = humano_primeiro

    while True:
        exibir_tabuleiro(tabuleiro)
        resultado = verificar_vencedor(tabuleiro)
        if resultado is not None:
            if resultado == simbolo_humano:
                print("Parabens! Voce venceu a partida!")
            elif resultado == simbolo_bot:
                print("O Bot venceu a partida!")
            else:
                print("Empate! O tabuleiro encheu sem vencedores.")
            break

        if turno_humano:
            print(f"--- Seu turno ({simbolo_humano}) ---")
            pos = obter_jogada_humano(tabuleiro)
            tabuleiro[pos] = simbolo_humano
        else:
            print(f"--- Turno do Bot ({simbolo_bot}) ---")
            if funcao_bot:
                pos = funcao_bot(tabuleiro, simbolo_bot)
            else:
                pos = tabuleiro.index(' ')  # Jogada provisoria
            tabuleiro[pos] = simbolo_bot
            
        turno_humano = not turno_humano


if __name__ == "__main__":
    iniciar_jogo()