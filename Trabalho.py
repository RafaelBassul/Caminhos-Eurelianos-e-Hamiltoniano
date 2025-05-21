import time

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
            for k in range(matriz[i][j]):
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

def GrafoHamiltoniano(grafo):
    caminhos = []
    for i in grafo:
        for j in grafo[i][0]:
            grafocopia = {}
            for x in grafo:
                grafocopia[x] = [grafo[x], False]
            grafocopia[i][1] = True
            PercorrerGrafo(grafocopia,j, i, str(i) + " -> ",caminhos)

    CaminhoHamiltonianoDefinitivo = False
    HamiltinoCompletoDefinitivo = False
    CaminhosHamiltonianos = []
    for i in caminhos:
        CaminhoHamiltoniano = True
        HamiltinoCompleto = False
        for x in grafo:
            grafocopia[x] = [grafo[x], False]
        vertices = i.split(" -> ")
        if '' in vertices:
            vertices.remove("")
        if vertices[0] == vertices[-1]:
            HamiltinoCompleto = True
            HamiltinoCompletoDefinitivo = True
        for vertice in vertices:
            grafocopia[int(vertice)][1] = True
        for f in grafocopia:
            if grafocopia[f][1] == False:
                CaminhoHamiltoniano = False
                break
        if HamiltinoCompleto and CaminhoHamiltoniano:
            print("Grafo Hamiltoniano encontrado:", i)
        elif CaminhoHamiltoniano:
            CaminhoHamiltonianoDefinitivo = True
            CaminhosHamiltonianos.append(i)
    if CaminhoHamiltonianoDefinitivo and not HamiltinoCompletoDefinitivo:
        print("Grafo é Semi-Hamiltoniano Encontrado:", CaminhosHamiltonianos)
    if not CaminhoHamiltonianoDefinitivo and not HamiltinoCompletoDefinitivo:
        print("Grafo é Não é Hamiltoniano")

def PercorrerGrafo(grafo, vertice, inicio, caminho, caminhos):
    caminho += str(vertice) + " -> "
    grafo[vertice][1] = True
    for vizinho in grafo[vertice][0]:
        if vizinho == inicio and len(caminho.split("->")) > 3:
            caminhos.append(caminho + str(inicio))
        elif not grafo[vizinho][1]:
            PercorrerGrafo(grafo, vizinho, inicio, caminho, caminhos)
    grafo[vertice][1] = False  

def GrafoHamiltonianoHeuristico(grafo):
    # foi usado o teorema de dirac para a proccura heuristica
    n = len(grafo)
    res = ""
    if n < 3:
        res = "O teorema de Dirac não se aplica a grafos com menos de 3 vértices."
        return res 
    
    grau_saida = {v: len(adjacentes) for v, adjacentes in grafo.items()}
    grau_entrada = {v: 0 for v in grafo}

    # calcula o grau de entrada
    for v in grafo:
        for adjacente in grafo[v]:
            grau_entrada[adjacente] += 1

    dirac_satisfeito = True
    for v in grafo:
        grau_total = grau_saida[v] + grau_entrada[v]
        #print(f"Vértice {v}: grau entrada = {grau_entrada[v]}, grau saída = {grau_saida[v]}, grau total = {grau_total}, necessário >= {n / 2}")
        
        if grau_total < (n / 2):
            dirac_satisfeito = False
            break

    if dirac_satisfeito:
        res = "O grafo satisfaz o teorema de Dirac: É considerado um grafo Hamiltoniano."
        return res
    else:
        res = "O grafo não satisfaz o teorema de Dirac: Pode não ser um grafo Hamiltoniano."
        return res



def grafo_teste():
    matriz = [
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    return matriz_para_grafo_direcionado(matriz)

if __name__ == '__main__':
    matriz = [
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],  
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1],  
    [1, 0, 1, 0, 0, 0],  
    [0, 1, 0, 1, 0, 0],  
    ]


    grafo = matriz_para_grafo_direcionado(matriz)
    tem_caminho, tem_ciclo = verifica_caminho_ciclo_euleriano(grafo)
    print("--------------------------------")
    print("Tem caminho euleriano?:", tem_caminho)
    print("Tem ciclo euleriano?:", tem_ciclo)
    print("--------------------------------")
    GrafoHamiltoniano(grafo)
    print("--------------------------------")
    #printar o grafo
    print("Grafo direcionado:", grafo)
    print("--------------------------------")
    for vertice, adjacentes in grafo.items():
        print(f"Vértice {vertice} tem arestas para: {adjacentes}")
    print("--------------------------------")
    print("Resultado:", GrafoHamiltonianoHeuristico(grafo))


