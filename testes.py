from Trabalho import matriz_para_grafo_direcionado

def grafo_teste():
    matriz = [
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    return matriz_para_grafo_direcionado(matriz)

def grafo_hamiltoniano():
    matriz = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
    ]
    return matriz_para_grafo_direcionado(matriz)