def exibir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        linha = [tabuleiro[i * 3 + j] if tabuleiro[i * 3 + j] != ' ' else str(i * 3 + j + 1) for j in range(3)]
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

# --- TESTE TEMPORÁRIO ---
tabuleiro_teste = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
exibir_tabuleiro(tabuleiro_teste)

def obter_jogada_humano(tabuleiro):
    while True:
        try:
            posicao = int(input("Escolha uma posicao livre (1-9): ")) - 1
            if 0 <= posicao <= 8 and tabuleiro[posicao] == ' ':
                return posicao
            print("Posicao invalida ou ja ocupada! Tente novamente.")
        except ValueError:
            print("Entrada invalida! Por favor, digite um numero de 1 a 9.")
            
if __name__ == "__main__":
    tabuleiro_teste = [' '] * 9
    exibir_tabuleiro(tabuleiro_teste)
    
    posicao_escolhida = obter_jogada_humano(tabuleiro_teste)
    tabuleiro_teste[posicao_escolhida] = 'X'
    
    print("\nTabuleiro apos sua jogada:")
    exibir_tabuleiro(tabuleiro_teste)