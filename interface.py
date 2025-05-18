import tkinter as tk
from tkinter import Canvas
from Trabalho import grafo_teste
import math

class InterfaceGrafo(tk.Tk):
    def __init__(self, grafo=None):
        super().__init__()
        self.title("Programa de grafos")

        if grafo is None or len(grafo) == 0:
            grafoVazio = "Grafo vazio\n\n"
            grafoVazio += " Incapaz de mostrar caminhos Eulerianos ou Hamiltonianos,\npois não existem caminhos em grafo vazio. "
            self.label = tk.Label(self, text=grafoVazio, font=('Arial', 12, 'italic'), bg="lightgray", width=100)
            self.label.pack(pady=5)
            return
        
        self.grafo = grafo

        # Frame para os botões no topo
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.button_tipo = tk.Button(self.button_frame, text="Ativar fun1", command=self.funcao1)
        self.button_tipo.pack(side=tk.LEFT, padx=5)

        self.button_altura = tk.Button(self.button_frame, text="Ativar fun2", command=self.funcao2)
        self.button_altura.pack(side=tk.LEFT, padx=5)

        # Canvas para visualizar o grafo
        self.canvas = Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

        # Label inferior
        self.label = tk.Label(self, text=" ", font=('Arial', 12, 'italic'), bg="lightgray", width=100)
        self.label.pack(pady=5)

        # Desenhar o grafo
        self.positions = {}
        self.draw_grafo()

    def funcao1(self):
        texto = f"Testando função 1."
        self.label.config(text=texto)

    def funcao2(self):
        string_tipos = "Testando função 2."
        self.label.config(text=string_tipos)

    def draw_grafo(self):
        num_nodes = len(self.grafo)
        center_x = 400
        center_y = 300
        radius = 200
        angle_step = 2 * math.pi / num_nodes

        # Primeiro, posicionar os nós em círculo
        for i, node in enumerate(self.grafo):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.positions[node] = (x, y)

            # Desenhar o nó
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightblue', outline='black')
            self.canvas.create_text(x, y, text=str(node), font=('Arial', 10, 'bold'))

        # Agora, desenhar as arestas
        for origem in self.grafo:
            for destino in self.grafo[origem]:
                x1, y1 = self.positions[origem]
                x2, y2 = self.positions[destino]

                # Calcular deslocamento para a seta não sobrepor o nó
                dx, dy = x2 - x1, y2 - y1
                dist = math.sqrt(dx**2 + dy**2)
                offset_x = 20 * dx / dist
                offset_y = 20 * dy / dist

                # Desenhar linha com seta
                self.canvas.create_line(
                    x1 + offset_x, y1 + offset_y,
                    x2 - offset_x, y2 - offset_y,
                    arrow=tk.LAST
                )

    def reset_graph(self):
        self.canvas.delete("all")
        self.draw_grafo(self.grafo, 400, 50, 150, 50)


def main():
    # Árvore de teste (alterar árvore aqui)
    #root = teste1()
    #root = teste2()
    #root = teste3()
    #root = teste4()
    #root = teste5()
    #root = teste6()
    #root = teste7()
    #root = teste8()

    # Carregar / Abrir interface gráfica
    try:
        grafo = grafo_teste()
        app = InterfaceGrafo(grafo)
        app.mainloop()
    except Exception as e:
        print(f"\nAlgo deu errado: {str(e)}")


if __name__ == "__main__":
    main()