# Jogo da Velha com Inteligência Artificial

Um jogo da velha desenvolvido em Python onde o jogador enfrenta um Bot munido do algoritmo Minimax, tornando a IA imbatível. O projeto conta com duas interfaces de uso: Terminal (CLI) e Interface Gráfica (GUI).

---

## Funcionalidades

### Duas opções de interface:

* **CLI (Terminal):** Jogabilidade simples via terminal.

* **GUI (Tkinter):** Interface gráfica amigável e interativa.

* **IA Imbatível:** Utilização do algoritmo Minimax para tomada de decisões.

* **Escolha de Símbolo/Início:** Permite ao jogador escolher se quer jogar como X (começa jogando) ou O (o Bot começa).

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica:** Tkinter (biblioteca nativa do Python)

---

## Estrutura do Projeto

```text
├── main.py       # Ponto de entrada (menu para escolher modo CLI ou GUI)
├── cli.py        # Lógica de interface via linha de comando (Terminal)[cite: 1]
├── gui.py        # Lógica de interface gráfica com Tkinter[cite: 2]
├── minimax.py    # Algoritmo de Inteligência Artificial
└── README.md     # Documentação do projeto
```

---

## Como Executar

Por utilizar apenas bibliotecas nativas do Python (tkinter e math), não é necessário instalar dependências externas.

### Pré-requisitos

* Python 3 instalado na sua máquina.

---

## Como Funciona o Algoritmo Minimax?

O algoritmo Minimax realiza uma busca em árvore explorando todas as jogadas possíveis até o fim da partida. Ele atribui pontuações para cada cenário:

* **Vitória do Bot:** +10 (descontado a profundidade do caminho)
* **Vitória do Jogador:** -10 (somado a profundidade do caminho)
* **Empate:** 0

---

## Testes Automatizados

Para validar a robustez do agente **Minimax**, foi implementado um teste automatizado utilizando o framework `pytest`.

O teste simula **100 partidas** contra um adversário que realiza jogadas aleatórias válidas. O agente é testado tanto iniciando a partida como `X` quanto jogando em segundo lugar como `O`, 50 vezes cada, somando um total de 100 partidas no final.

Durante as simulações, são contabilizadas:

* **Vitórias** do Minimax
* **Empates**
* **Derrotas**

Ao final das partidas, o teste utiliza uma asserção para garantir que o agente não sofreu nenhuma derrota:

```python
assert derrotas == 0
```

### Executando o teste

Com o `pytest` instalado, execute na pasta do projeto:

```bash
python -m pytest -s
```

### Resultado esperado

O número de vitórias e empates pode variar, pois as jogadas do adversário são aleatórias. Porém, o número de derrotas do Minimax deve ser sempre **0**.

Exemplo de execução:

```text
=== Resultado do teste ===
Vitórias do Minimax: 94
Empates: 6
Derrotas: 0

1 passed
```

Esse teste comprova que o agente é forte contra jogadas aleatórias e não perde nenhuma das partidas simuladas.

---

## Alunos
**Alisson Vitor, Pedro Felipe, Henrique Augusto e Luis Filipe**