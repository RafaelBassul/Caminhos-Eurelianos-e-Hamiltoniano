from interface import InterfaceGrafo
import testes

def main():
    # grafo = testes.grafo_teste()
    grafo = testes.grafo_hamiltoniano()

    try:
        app = InterfaceGrafo(grafo)
        app.mainloop()
    except Exception as e:
        print(f"\nAlgo deu errado: {str(e)}")


if __name__ == '__main__':
    main()