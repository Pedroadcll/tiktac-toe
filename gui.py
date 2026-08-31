import tkinter as tk
from tkinter import font as tkfont
import time

class JogoDaVelhaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha - I.A.")
        self.root.configure(bg="#e0e0e0")

        # Configuração de Fontes Grandes para Tela Cheia
        self.fonte_titulo = tkfont.Font(family="Arial", size=40, weight="bold")
        self.fonte_subtitulo = tkfont.Font(family="Arial", size=20)
        self.fonte_status = tkfont.Font(family="Arial", size=24, weight="bold")
        self.fonte_botoes_menu = tkfont.Font(family="Arial", size=18, weight="bold")
        self.fonte_tabuleiro = tkfont.Font(family="Arial", size=64, weight="bold")

        # Estado do jogo
        self.tabuleiro = [' '] * 9
        self.simbolo_humano = 'X'
        self.simbolo_bot = 'O'
        self.turno_humano = True
        self.game_over = False

        # Container Principal
        self.main_frame = tk.Frame(self.root, bg="#e0e0e0")
        self.main_frame.pack(expand=True, fill="both", padx=40, pady=40)

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()

        # Título principal
        lbl_titulo = tk.Label(
            self.main_frame, text="Jogo da Velha", 
            font=self.fonte_titulo, bg="#e0e0e0", fg="#222"
        )
        lbl_titulo.pack(pady=(40, 20))

        # Subtítulo
        lbl_sub = tk.Label(
            self.main_frame, text="Escolha como deseja jogar:", 
            font=self.fonte_subtitulo, bg="#e0e0e0", fg="#444"
        )
        lbl_sub.pack(pady=(0, 40))

        # Frame dos botões de escolha
        btn_frame = tk.Frame(self.main_frame, bg="#e0e0e0")
        btn_frame.pack(pady=20)

        btn_x = tk.Button(
            btn_frame, text="Jogar como X\n(Você começa)", 
            font=self.fonte_botoes_menu, bg="#4CAF50", fg="white",
            width=18, height=4, relief="flat", cursor="hand2",
            command=lambda: self.iniciar_partida('X', True)
        )
        btn_x.grid(row=0, column=0, padx=25)

        btn_o = tk.Button(
            btn_frame, text="Jogar como O\n(Bot começa)", 
            font=self.fonte_botoes_menu, bg="#2196F3", fg="white",
            width=18, height=4, relief="flat", cursor="hand2",
            command=lambda: self.iniciar_partida('O', False)
        )
        btn_o.grid(row=0, column=1, padx=25)

    def iniciar_partida(self, simbolo, humano_comeca):
        self.simbolo_humano = simbolo
        self.simbolo_bot = 'O' if simbolo == 'X' else 'X'
        self.turno_humano = humano_comeca
        self.tabuleiro = [' '] * 9
        self.game_over = False

        self.tela_jogo()

        if not self.turno_humano:
            self.root.after(600, self.jogada_bot)

    def tela_jogo(self):
        self.limpar_tela()

        # Status da Turno/Vencedor
        self.lbl_status = tk.Label(
            self.main_frame, text="", 
            font=self.fonte_status, bg="#e0e0e0", fg="#222"
        )
        self.lbl_status.pack(pady=(10, 20))
        self.atualizar_status()

        # Grade 3x3
        board_frame = tk.Frame(self.main_frame, bg="#333", bd=4)
        board_frame.pack(expand=True)

        self.botoes_tabuleiro = []
        for i in range(9):
            row = i // 3
            col = i % 3
            btn = tk.Button(
                board_frame, text="", font=self.fonte_tabuleiro,
                width=4, height=1, bg="#ffffff", relief="groove",
                cursor="hand2", command=lambda idx=i: self.jogada_humana(idx)
            )
            btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
            self.botoes_tabuleiro.append(btn)

        # Botão Reiniciar / Voltar
        btn_voltar = tk.Button(
            self.main_frame, text="Voltar ao Menu", 
            font=self.fonte_botoes_menu, bg="#757575", fg="white",
            padx=20, pady=10, relief="flat", cursor="hand2",
            command=self.tela_inicial
        )
        btn_voltar.pack(pady=(30, 10))

    def atualizar_status(self):
        if self.game_over:
            return
        if self.turno_humano:
            self.lbl_status.config(text=f"Sua vez ({self.simbolo_humano})")
        else:
            self.lbl_status.config(text=f"Vez do Bot ({self.simbolo_bot})...")

    def jogada_humana(self, index):
        if self.tabuleiro[index] == ' ' and self.turno_humano and not self.game_over:
            self.tabuleiro[index] = self.simbolo_humano
            self.botoes_tabuleiro[index].config(
                text=self.simbolo_humano, 
                fg="#4CAF50" if self.simbolo_humano == 'X' else "#2196F3"
            )
            
            if self.checar_fim():
                return
            
            self.turno_humano = False
            self.atualizar_status()
            self.root.after(500, self.jogada_bot)

    def jogada_bot(self):
        if self.game_over:
            return
        
        livres = [i for i, v in enumerate(self.tabuleiro) if v == ' ']
        if livres:
            pos = livres[0] # Substiua futuramente pela chamada da I.A. Minimax
            self.tabuleiro[pos] = self.simbolo_bot
            self.botoes_tabuleiro[pos].config(
                text=self.simbolo_bot, 
                fg="#4CAF50" if self.simbolo_bot == 'X' else "#2196F3"
            )

            if not self.checar_fim():
                self.turno_humano = True
                self.atualizar_status()

    def checar_fim(self):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in wins:
            if self.tabuleiro[a] != ' ' and self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c]:
                vencedor = self.tabuleiro[a]
                if vencedor == self.simbolo_humano:
                    msg = "🎉 Você Venceu!"
                    cor = "#2e7d32"
                else:
                    msg = "🤖 O Bot Venceu!"
                    cor = "#c62828"
                self.lbl_status.config(text=msg, fg=cor)
                self.game_over = True
                return True

        if ' ' not in self.tabuleiro:
            self.lbl_status.config(text="🤝 Empate!", fg="#ef6c00")
            self.game_over = True
            return True

        return False