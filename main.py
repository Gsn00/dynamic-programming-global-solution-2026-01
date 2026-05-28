import heapq
from collections import deque

"""
GS 2026 - OrbitClean: Sistema de Inteligência Orbital
Algoritmos: Busca em Largura (BFS) e Fila de Prioridade (Heapq)
Estruturas: Grafo de Adjacência e Fila FIFO (Deque)

Integrantes:
- Gabriel Silva Novais RM566370
- Kathleen Claire Spencer Lourenço RM561571
- Marcielle Janguas Pina Carvalho RM561505
- Marcos Vinicius Aquino Prado RM562775
"""

# Detritos -> detrito = (periculosidade, setor)
detritos = [
    (8, 1), (3, 2), (5, 3), (10, 4), (2, 5), (7, 6),
    (4, 7), (9, 8), (1, 9), (6, 10), (3, 11), (8, 12),
    (5, 13), (10, 14), (2, 15), (7, 16), (4, 17), (9, 18),
    (1, 19), (6, 20), (3, 21), (8, 22), (5, 23), (10, 24),
    (2, 25), (7, 26), (4, 27), (9, 28), (1, 29), (6, 30),
    (3, 31), (8, 32), (5, 33), (10, 34), (2, 35), (7, 36)
]

# Grafo do mapa orbital -> setor: [vizinho1, vizinho2...]
mapa_orbital = {
    1: [2, 7, 31], 2: [1, 3, 8], 3: [2, 4, 9], 4: [3, 5, 10], 5: [4, 6, 11], 6: [5, 12, 36],
    7: [1, 8, 13], 8: [2, 7, 9, 14], 9: [3, 8, 10, 15], 10: [4, 9, 11, 16], 11: [5, 10, 12, 17], 12: [6, 11, 18],
    13: [7, 14, 19], 14: [8, 13, 15, 20], 15: [9, 14, 16, 21], 16: [10, 15, 17, 22], 17: [11, 16, 18, 23], 18: [12, 17, 24],
    19: [13, 20, 25], 20: [14, 19, 21, 26], 21: [15, 20, 22, 27], 22: [16, 21, 23, 28], 23: [17, 22, 24, 29], 24: [18, 23, 30],
    25: [19, 26, 31], 26: [20, 25, 27, 32], 27: [21, 26, 28, 33], 28: [22, 27, 29, 34], 29: [23, 28, 30, 35], 30: [24, 29, 36],
    31: [1, 25, 32], 32: [26, 31, 33], 33: [27, 32, 34], 34: [28, 33, 35], 35: [29, 34, 36], 36: [6, 30, 35]
}

fila_prioridade = []

def preparar_fila_prioridade(lista, fila):
    ## Pega todos os detritos e adiciona em uma fila em ordem de periculosidade
    lista = sorted(lista, key=lambda x: x[0], reverse=True)

    for periculosidade, setor in lista:
        heapq.heappush(fila, (-periculosidade, setor))

def buscar_caminho(grafo, inicio, destino):
    """
    Realiza a Busca em Largura para encontrar a rota com menor número de saltos.
    """
    fila = deque([[inicio]])
    visitados = []

    while fila:
        caminho = fila.popleft()
        setor_atual = caminho[-1]

        if setor_atual == destino:
            return caminho

        if setor_atual not in visitados:
            for vizinho in grafo.get(setor_atual):
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
            visitados.append(setor_atual)

def limpar_detritos(fila, setor_inicial, grafo, combustivel):
    """
    Simula a missão de limpeza processando a Fila de Prioridade.
    Implementa lógica de consumo de recursos e telemetria de missão.
    """
    total_risco_removido = 0
    combustivel_gasto = 0

    while fila:
        detrito = heapq.heappop(fila)
        risco_detrito = -detrito[0]
        setor_detrito = detrito[1]

        rota = buscar_caminho(grafo, setor_inicial, setor_detrito)
        custo_viagem = len(rota) - 1

        if combustivel >= custo_viagem:
            combustivel -= custo_viagem
            combustivel_gasto += custo_viagem
            total_risco_removido += risco_detrito

            print(f"\n[ALVO DETECTADO] Setor {setor_detrito} | Risco: {risco_detrito}")
            print(f" > Rota: {rota} (Custo: {custo_viagem})")
            print(f" > Combustível Restante: {combustivel}")

            setor_inicial = setor_detrito
        else:
            print(f"\n[AVISO] Combustível insuficiente para coletar detrito no setor {setor_detrito}!")
            break

    print("\n" + "=" * 40)
    print("       RELATÓRIO FINAL DA MISSÃO")
    print("=" * 40)
    print(f"Risco Total Removido: {total_risco_removido}")
    print(f"Combustível Gasto: {combustivel_gasto}")
    if combustivel_gasto > 0:
        eficiencia = total_risco_removido / combustivel_gasto
        print(f"Eficiência da Operação: {eficiencia:.2f} risco/litro")
    print("=" * 40)


def iniciar_sistema():
    """
    Interface de interação com o usuário para configuração da missão
    """
    print("=" * 50)
    print("   ORBITCLEAN AI - MÓDULO DE NAVEGAÇÃO AUTÔNOMA")
    print("=" * 50)
    try:
        setor_inicial = int(input("Informe o setor inicial do satélite (1-36): "))
        if setor_inicial < 1 or setor_inicial > 36:
            print("Erro: Setor fora do alcance orbital (1-36).")
            return

        combustivel = int(input("Informe a carga de combustível inicial: "))

        preparar_fila_prioridade(detritos, fila_prioridade)
        limpar_detritos(fila_prioridade, setor_inicial, mapa_orbital, combustivel)
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros.")

iniciar_sistema()