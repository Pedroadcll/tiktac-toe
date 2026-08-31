import tkinter as tk
from tkinter import messagebox


def verificar_vencedor(tabuleiro):
    """Verifica se ha um vencedor ou empate no tabuleiro."""
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in combinacoes:
        if tabuleiro[a] != ' ' and tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return tabuleiro[a]
    if ' ' not in tabuleiro:
        return 'Empate'
    return None


class JogoDaVelhaGUI:
    def __init__(self, root, funcao_bot=None):
        self.root = root
        self.root.title("Jogo da Velha - I.A.")
        self.root.geometry("360x460")
        self.root.resizable(False, False)
        
        self.funcao_bot = funcao_bot
        self.tabuleiro = [' '] * 9
        self.simbolo_humano = 'X'
        self.simbolo_bot = 'O'
        self.turno_humano = True
        
        self.exibir_tela_selecao()

    def exibir_tela_selecao(self):
        """Tela inicial para escolha de simbolo."""
        for widget in self.root.winfo_children():
            widget.destroy()

        label_titulo = tk.Label(self.root, text="Jogo da Velha", font=('Arial', 20, 'bold'))
        label_titulo.pack(pady=30)

        label_sub = tk.Label(self.root, text="Escolha com qual simbolo deseja jogar:", font=('Arial', 11))
        label_sub.pack(pady=10)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=20)

        btn_x = tk.Button(
            frame_botoes, text="Jogar como X\n(Voce começa)", font=('Arial', 11, 'bold'),
            width=14, height=3, bg="#4CAF50", fg="white",
            command=lambda: self.iniciar_partida('X')
        )
        btn_x.pack(side=tk.LEFT, padx=10)

        btn_o = tk.Button(
            frame_botoes, text="Jogar como O\n(Bot começa)", font=('Arial', 11, 'bold'),
            width=14, height=3, bg="#2196F3", fg="white",
            command=lambda: self.iniciar_partida('O')
        )
        btn_o.pack(side=tk.RIGHT, padx=10)

    def iniciar_partida(self, escolha_humano):
        """Monta o tabuleiro 3x3 e inicia a partida."""
        self.simbolo_humano = escolha_humano
        self.simbolo_bot = 'O' if escolha_humano == 'X' else 'X'
        self.turno_humano = (escolha_humano == 'X')
        self.tabuleiro = [' '] * 9

        for widget in self.root.winfo_children():
            widget.destroy()

        self.label_status = tk.Label(self.root, text="", font=('Arial', 12, 'bold'))
        self.label_status.pack(pady=10)

        frame_grid = tk.Frame(self.root)
        frame_grid.pack(pady=10)

        self.botoes = []
        for i in range(9):
            btn = tk.Button(
                frame_grid, text=" ", font=('Arial', 20, 'bold'), width=4, height=2,
                command=lambda pos=i: self.clique_humano(pos)
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.botoes.append(btn)

        self.atualizar_status()

        # Se o Bot for o primeiro a jogar
        if not self.turno_humano:
            self.root.after(600, self.jogada_bot)

    def atualizar_status(self):
        if self.turno_humano:
            self.label_status.config(text=f"Sua vez ({self.simbolo_humano})", fg="green")
        else:
            self.label_status.config(text=f"Vez do Bot ({self.simbolo_bot})...", fg="red")

    def clique_humano(self, posicao):
        """Processa a jogada do usuario ao clicar num botao."""
        if self.tabuleiro[posicao] == ' ' and self.turno_humano:
            self.executar_jogada(posicao, self.simbolo_humano)
            
            if not self.checar_fim_jogo():
                self.turno_humano = False
                self.atualizar_status()
                self.root.after(500, self.jogada_bot)

    def jogada_bot(self):
        """Processa a jogada da I.A."""
        if ' ' in self.tabuleiro and not self.turno_humano:
            if self.funcao_bot:
                posicao = self.funcao_bot(self.tabuleiro, self.simbolo_bot)
            else:
                posicao = self.tabuleiro.index(' ')  # Provisorio ate integrar o Minimax

            self.executar_jogada(posicao, self.simbolo_bot)

            if not self.checar_fim_jogo():
                self.turno_humano = True
                self.atualizar_status()

    def executar_jogada(self, posicao, simbolo):
        self.tabuleiro[posicao] = simbolo
        cor_texto = "#2E7D32" if simbolo == 'X' else "#1565C0"
        self.botoes[posicao].config(text=simbolo, state=tk.DISABLED, disabledforeground=cor_texto)

    def checar_fim_jogo(self):
        resultado = verificar_vencedor(self.tabuleiro)
        if resultado is not None:
            for btn in self.botoes:
                btn.config(state=tk.DISABLED)

            if resultado == self.simbolo_humano:
                msg = "Parabens! Voce venceu!"
            elif resultado == self.simbolo_bot:
                msg = "O Bot venceu!"
            else:
                msg = "Empate!"

            messagebox.showinfo("Fim de Jogo", msg)
            self.exibir_tela_selecao()
            return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDaVelhaGUI(root)
    root.mainloop()