import tkinter as tk
from tkinter import Canvas
from Trabalho import verifica_caminho_ciclo_euleriano, GrafoHamiltoniano, GrafoHamiltonianoHeuristico, encontrar_caminho_euleriano
from testes import grafo_teste
import math
import sys


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

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.button_euler = tk.Button(self.button_frame, text="Euleriano", command=self.mostrar_euleriano)
        self.button_euler.pack(side=tk.LEFT, padx=5)

        self.button_hamil_exato = tk.Button(self.button_frame, text="Hamiltoniano Exato", command=self.mostrar_hamiltoniano_exato)
        self.button_hamil_exato.pack(side=tk.LEFT, padx=5)

        self.button_hamil_heur = tk.Button(self.button_frame, text="Hamiltoniano Heurístico", command=self.mostrar_hamiltoniano_heuristico)
        self.button_hamil_heur.pack(side=tk.LEFT, padx=5)

        self.dynamic_frame = tk.Frame(self)
        self.dynamic_frame.pack(pady=5)

        self.canvas = Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

        self.positions = {}
        self.draw_grafo()
        self.mostrar_euleriano()

    def limpar_frame_dinamico(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def mostrar_euleriano(self):
        self.limpar_frame_dinamico()

        botao = tk.Button(self.dynamic_frame, text="Fazer analise", command=self.caminhos_euler)
        botao.pack(pady=5)

        self.button_euler.config(bg='lightblue')
        self.button_hamil_exato.config(bg='#F0F0F0')
        self.button_hamil_heur.config(bg='#F0F0F0')

        self.label_euler = tk.Label(self.dynamic_frame, text="", font=('Arial', 10))
        self.label_euler.pack()

    def mostrar_hamiltoniano_exato(self):
        self.limpar_frame_dinamico()

        frame_a = tk.Frame(self.dynamic_frame)
        frame_a.pack(pady=2)

        self.var_a = tk.BooleanVar()
        chk_a = tk.Checkbutton(frame_a, text="Limite de tempo (s)", variable=self.var_a, command=self.toggle_entry_a)
        chk_a.pack(side=tk.LEFT)

        self.entry_a = tk.Entry(frame_a, state=tk.DISABLED)
        self.entry_a.pack(side=tk.LEFT, padx=5)

        frame_b = tk.Frame(self.dynamic_frame)
        frame_b.pack(pady=2)

        self.var_b = tk.BooleanVar()
        chk_b = tk.Checkbutton(frame_b, text="Limite de nº vertices", variable=self.var_b, command=self.toggle_entry_b)
        chk_b.pack(side=tk.LEFT)

        self.entry_b = tk.Entry(frame_b, state=tk.DISABLED)
        self.entry_b.pack(side=tk.LEFT, padx=5)

        botao = tk.Button(self.dynamic_frame, text="Fazer analise", command=self.caminhos_hamil_exato)
        botao.pack(pady=5)

        self.button_euler.config(bg='#F0F0F0')
        self.button_hamil_exato.config(bg='lightblue')
        self.button_hamil_heur.config(bg='#F0F0F0')

        scroll_ex = tk.Scrollbar(self.dynamic_frame)
        scroll_ex.pack(side=tk.RIGHT, fill=tk.Y)

        self.label_hamil_ex = tk.Text(self.dynamic_frame, height=10, width=100, wrap=tk.WORD, yscrollcommand=scroll_ex.set, font=('Arial', 10))
        self.label_hamil_ex.pack()
        scroll_ex.config(command=self.label_hamil_ex.yview)

    def mostrar_hamiltoniano_heuristico(self):
        self.limpar_frame_dinamico()

        frame_a = tk.Frame(self.dynamic_frame)
        frame_a.pack(pady=2)

        self.var_ha = tk.BooleanVar()
        chk_ha = tk.Checkbutton(frame_a, text="Limite de tempo (s)", variable=self.var_ha, command=self.toggle_entry_ha)
        chk_ha.pack(side=tk.LEFT)

        self.entry_ha = tk.Entry(frame_a, state=tk.DISABLED)
        self.entry_ha.pack(side=tk.LEFT, padx=5)

        frame_b = tk.Frame(self.dynamic_frame)
        frame_b.pack(pady=2)

        self.var_hb = tk.BooleanVar()
        chk_hb = tk.Checkbutton(frame_b, text="Limite de nº vertices", variable=self.var_hb, command=self.toggle_entry_hb)
        chk_hb.pack(side=tk.LEFT)

        self.entry_hb = tk.Entry(frame_b, state=tk.DISABLED)
        self.entry_hb.pack(side=tk.LEFT, padx=5)

        botao = tk.Button(self.dynamic_frame, text="Fazer analise", command=self.caminhos_hamil_heuristico)
        botao.pack(pady=5)

        self.button_euler.config(bg='#F0F0F0')
        self.button_hamil_exato.config(bg='#F0F0F0')
        self.button_hamil_heur.config(bg='lightblue')

        self.label_hamil_heur = tk.Label(self.dynamic_frame, text="", font=('Arial', 10))
        self.label_hamil_heur.pack()

    def toggle_entry_a(self):
        self.entry_a.config(state=tk.NORMAL if self.var_a.get() else tk.DISABLED)

    def toggle_entry_b(self):
        self.entry_b.config(state=tk.NORMAL if self.var_b.get() else tk.DISABLED)

    def toggle_entry_ha(self):
        self.entry_ha.config(state=tk.NORMAL if self.var_ha.get() else tk.DISABLED)

    def toggle_entry_hb(self):
        self.entry_hb.config(state=tk.NORMAL if self.var_hb.get() else tk.DISABLED)

    def caminhos_euler(self):
        try:
            self.label_euler.config(text='Executando analise...')
            tem_caminho, tem_ciclo = verifica_caminho_ciclo_euleriano(grafo=self.grafo)
        except Exception as e: 
            print(f"Analise cancelada - motivo: {e}")
            
        texto = ''
        if tem_caminho == 'Sim':
            texto += 'Existe pelo menos um caminho euleriano no grafo.\n'
        else:
            texto += 'Não existem caminhos eulerianos no grafo.\n'
        if tem_ciclo == 'Sim':
            texto += 'Existe pelo menos um ciclo euleriano no grafo.\n'
        else:
            texto += 'Não existem ciclos eulerianos no grafo.\n'

        if tem_caminho == 'Sim':
            caminho = encontrar_caminho_euleriano(self.grafo)
            texto += f'{caminho}\n'
            
        self.label_euler.config(text=texto)

    def caminhos_hamil_exato(self):       
        lim_tempo = 0
        lim_vert = 0
        
        if self.var_a.get():
            lim_tempo = int(self.entry_a.get())
        if self.var_b.get():
            lim_vert = int(self.entry_b.get())

        try:
            texto = 'Executando analise...'
            self.label_hamil_ex.config(state=tk.NORMAL) 
            self.label_hamil_ex.delete(1.0, tk.END)
            self.label_hamil_ex.insert(tk.END, texto)
            self.label_hamil_ex.config(state=tk.DISABLED)
            texto = GrafoHamiltoniano(grafo=self.grafo,
                                      tempoMaximo=lim_tempo,
                                      VerticeMaxima=lim_vert)
        except Exception as e:
            print(f"Analise cancelada - motivo: {e}")
        
        self.label_hamil_ex.config(state=tk.NORMAL) 
        self.label_hamil_ex.delete(1.0, tk.END)
        self.label_hamil_ex.insert(tk.END, texto)
        self.label_hamil_ex.config(state=tk.DISABLED)

    def caminhos_hamil_heuristico(self):
        lim_tempo = sys.maxsize
        lim_vert = sys.maxsize

        if self.var_ha.get():
            lim_tempo = float(self.entry_ha.get())
        if self.var_hb.get():
            lim_vert = float(self.entry_hb.get())
        
        try:
            self.label_hamil_heur.config(text='Executando analise...')
            texto = GrafoHamiltonianoHeuristico(grafo=self.grafo,
                                                segs=lim_tempo,
                                                limiteV=lim_vert)
        except Exception as e:
            print(f"Analise cancelada - motivo: {e}")
            
        self.label_hamil_heur.config(text=texto)

    def draw_grafo(self):
        num_nodes = len(self.grafo)
        center_x = 400
        center_y = 300
        radius = 200
        angle_step = 2 * math.pi / num_nodes

        for i, node in enumerate(self.grafo):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.positions[node] = (x, y)

            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightblue', outline='black')
            self.canvas.create_text(x, y, text=str(node), font=('Arial', 10, 'bold'))

        for origem in self.grafo:
            for destino in self.grafo[origem]:
                x1, y1 = self.positions[origem]
                x2, y2 = self.positions[destino]

                dx, dy = x2 - x1, y2 - y1
                dist = math.sqrt(dx**2 + dy**2)
                offset_x = 20 * dx / dist
                offset_y = 20 * dy / dist

                is_opposite = origem in self.grafo.get(destino, [])

                if is_opposite and origem < destino:
                    perp_dx = -dy / dist
                    perp_dy = dx / dist
                    curva = 10
                    x1 += perp_dx * curva
                    y1 += perp_dy * curva
                    x2 += perp_dx * curva
                    y2 += perp_dy * curva

                self.canvas.create_line(
                    x1 + offset_x, y1 + offset_y,
                    x2 - offset_x, y2 - offset_y,
                    arrow=tk.LAST
                )


def main():
    try:
        grafo = grafo_teste()
        app = InterfaceGrafo(grafo)
        app.mainloop()
    except Exception as e:
        print(f"\nAlgo deu errado: {str(e)}")


if __name__ == "__main__":
    main()
