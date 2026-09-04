Jogo da Velha com Inteligência Artificial

Um jogo da velha desenvolvido em Python onde o jogador enfrenta um Bot munido do algoritmo Minimax, tornando a IA imbatível. O projeto conta com duas interfaces de uso: Terminal (CLI) e Interface Gráfica (GUI).

    FUNCIONALIDADES
    Duas opções de interface:
        CLI (Terminal): Jogabilidade simples via terminal.
        GUI (Tkinter): Interface gráfica amigável e interativa.
    IA Imbatível: Utilização do algoritmo Minimax para tomada de decisões.
    Escolha de Símbolo/Início: Permite ao jogador escolher se quer jogar como X (começa jogando) ou O (o Bot começa).

    TECNOLOGIAS UTILIZADAS
        Linguagem: Python 3
        Interface Gráfica: Tkinter (biblioteca nativa do Python)

    ESTRUTURA DO PROJETO
        ├── main.py       # Ponto de entrada (menu para escolher modo CLI ou GUI)
        ├── cli.py        # Lógica de interface via linha de comando (Terminal)[cite: 1]
        ├── gui.py        # Lógica de interface gráfica com Tkinter[cite: 2]
        ├── minimax.py    # Algoritmo de Inteligência Artificial
        └── README.md     # Documentação do projeto

    COMO EXECUTAR
        Por utilizar apenas bibliotecas nativas do Python (tkinter e math), não é necessário instalar dependências externas.
    
    PRÉ-REQUISITOS
        Python 3 instalado na sua máquina.

    COMO FUNCIONA O ALGORITMO MINIMAX?
        O algoritmo Minimax realiza uma busca em árvore explorando todas as jogadas possíveis até o fim da partida. Ele atribui pontuações para cada cenário:
            Vitória do Bot: +10 (descontado a profundidade do caminho)
            Vitória do Jogador: -10 (somado a profundidade do caminho)
            Empate: 0