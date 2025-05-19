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

def verifica_caminho_ciclo_euleriano(grafo):
    """
    Um grafo direcionado tem:
    - Caminho euleriano no máximo tem um vértice com (grau_saida - grau_entrada) = 1
      e todos os outros vértices têm grau_entrada = grau_saida
    - Ciclo euleriano se todos os vértices têm grau_entrada = grau_saida
    """
    #aqui eu to setando que o grau de saida de cada vertice é o numero de arestas que ele tem
    grau_saida = {v: len(adjacentes) for v, adjacentes in grafo.items()}
    
    # Calcular graus de entrada e saída para cada vértice
    #aqui eu to setando que o grau de entrada de cada vertice é 0 pra dps contar
    grau_entrada = {v: 0 for v in grafo}

    # Contar graus de entrada
    for v in grafo:
        for adjacente in grafo[v]:
            grau_entrada[adjacente] += 1

    # Verificar condições para ciclo e caminho euleriano
    diff_positiva = 0  
    diff_negativa = 0  
    vertices_balanceados = 0  
    
    for v in grafo:
        diff = grau_saida[v] - grau_entrada[v]
        if diff == 0:
            vertices_balanceados += 1
        elif diff == 1:
            diff_positiva += 1 #tem mais arestas saindo do que entrando 
        elif diff == -1:
            diff_negativa += 1 #tem mais arestas entrando do que saindo
    
    # Verificar se tem ciclo euleriano
    tem_ciclo = (vertices_balanceados == len(grafo))
    
    # Verificar se tem caminho euleriano
    tem_caminho = (tem_ciclo or 
                  (diff_positiva == 1 and diff_negativa == 1 and 
                   vertices_balanceados == len(grafo) - 2))

    tem_caminho = "Sim" if tem_caminho else "Não"
    tem_ciclo = "Sim" if tem_ciclo else "Não"
    
    return tem_caminho, tem_ciclo


def grafo_teste():
    matriz = [
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    return matriz_para_grafo_direcionado(matriz)

matriz = [
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]


grafo = matriz_para_grafo_direcionado(matriz)

#printar o grafo
print("Grafo direcionado:", grafo)
for vertice, adjacentes in grafo.items():
    print(f"Vértice {vertice} tem arestas para: {adjacentes}")

#funçao se o grafo tem caminho euleriano
tem_caminho, tem_ciclo = verifica_caminho_ciclo_euleriano(grafo)
print(f"O grafo tem caminho euleriano? {tem_caminho}")
print(f"O grafo tem ciclo euleriano? {tem_ciclo}")


