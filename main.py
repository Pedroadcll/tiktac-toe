import tkinter as tk
from cli import iniciar_jogo
from gui import JogoDaVelhaGUI
from minimax import obter_melhor_jogada

def menu_principal():
    print("=== JOGO DA VELHA ===")
    print("1. Jogar no Terminal (CLI)")
    print("2. Jogar em Janela Grafica (GUI)")
    
    opcao = input("Escolha uma opcao (1 ou 2): ").strip()
    
    if opcao == "2":
        root = tk.Tk()
        app = JogoDaVelhaGUI(root, funcao_bot=obter_melhor_jogada)
        root.mainloop()
    else:
        iniciar_jogo(funcao_bot=obter_melhor_jogada)


if __name__ == "__main__":
    menu_principal()