# OrbitClean - Satélite de Remoção de Detritos

Este projeto faz parte da **Global Solution 2026** da FIAP. O objetivo é solucionar o desafio da gestão de lixo espacial utilizando algoritmos avançados de busca e priorização.


## Integrantes
- Gabriel Silva Novais RM566370
- Kathleen Claire Spencer Lourenço RM561571
- Marcielle Janguas Pina Carvalho RM561505
- Marcos Vinicius Aquino Prado RM562775

## Sobre o Projeto
O OrbitClean simula um satélite de limpeza autônomo que opera em uma malha orbital de 36 setores. O sistema decide a ordem de coleta baseando-se no risco de cada detrito e encontra a rota mais eficiente para economizar energia.

## Tecnologias e Conceitos Utilizados
- **Linguagem:** Python 3.x
- **Estruturas de Dados:**
  - **Grafos:** Representação da órbita terrestre com conexões e atalhos.
  - **Fila de Prioridade (Heapq):** Gerenciamento de detritos por nível de periculosidade.
  - **Fila FIFO (Deque):** Utilizada no algoritmo de busca para exploração por camadas.
- **Algoritmos:**
  - **BFS (Breadth-First Search):** Garantia de encontrar o caminho mais curto entre setores.
  - **Heapsort:** Organização eficiente de prioridades.

## Como Executar
1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal:
   ```bash
   python main.py
