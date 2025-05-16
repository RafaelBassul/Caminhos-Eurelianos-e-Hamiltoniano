def matriz_para_grafo_direcionado(matriz):
    """
    Converte uma matriz de adjacência em um grafo direcionado representado como dicionário
    onde as chaves são os vértices e os valores são listas dos vértices adjacentes.

    Pensei em usar uma estrutura parecida com o nosso primeiro trabalho, mas teria problemas para fazer um grafo que tem circuito, dei uma pesquisada e achei que fazer uma
    lista de de adjacencia seria mais fácil.
    """
    num_vertices = len(matriz)
    # Criar um dicionário para representar o grafo
    grafo = {}
    
    # Inicializar o dicionário com uma lista vazia
    for i in range(num_vertices):
        grafo[i] = []
    
    # Para cada aresta na matriz, adiciona a conexão direcionada
    for i in range(num_vertices):
        for j in range(num_vertices):
            if matriz[i][j] == 1:
                grafo[i].append(j)
    
    return grafo
matriz = [
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]

grafo = matriz_para_grafo_direcionado(matriz)
print("Grafo direcionado:", grafo)
for vertice in grafo:
    print(f"Vértice {vertice} tem arestas para: {grafo[vertice]}")
# saida:
# Grafo direcionado: {0: [1, 3], 1: [2], 2: [0], 3: [2]}    
