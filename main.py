import tkinter as tk
from cli import iniciar_jogo
from gui import JogoDaVelhaGUI


def menu_principal():
    print("=== JOGO DA VELHA ===")
    print("1. Jogar no Terminal.")
    print("2. Jogar em Janela Gráfica.")

    opcao = input("Escolha uma opção (1 ou 2): ").strip()

    if opcao == "2":
        root = tk.Tk()
        root.attributes('-zoomed', True)  
        app = JogoDaVelhaGUI(root)
        root.mainloop()
    else:
        iniciar_jogo()


if __name__ == "__main__":
    menu_principal()