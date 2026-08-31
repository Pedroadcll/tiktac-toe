def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro 3x3 formatado no terminal."""
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