import matplotlib.pyplot as plt
import networkx as nx

# Clase Nodo
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return str(self.valor)

# Clase ArbolBinario
class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def agregar_nodo(self, valor, padre_valor, direccion):
        nuevo_nodo = NodoArbol(valor)
        if self.raiz is None:
            print(f"Creando la raíz con valor {valor}.")
            self.raiz = nuevo_nodo
        else:
            padre = self.buscar_nodo(self.raiz, padre_valor)
            if padre:
                if direccion == 'izquierda':
                    if padre.izquierda is None:
                        padre.izquierda = nuevo_nodo
                        print(f"Nodo {valor} agregado a la izquierda de {padre_valor}.")
                    else:
                        print(f"El nodo {padre_valor} ya tiene un hijo izquierdo.")
                elif direccion == 'derecha':
                    if padre.derecha is None:
                        padre.derecha = nuevo_nodo
                        print(f"Nodo {valor} agregado a la derecha de {padre_valor}.")
                    else:
                        print(f"El nodo {padre_valor} ya tiene un hijo derecho.")
            else:
                print(f"No se encontró el nodo con valor {padre_valor}.")

    def buscar_nodo(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.valor == valor:
            return nodo
        izquierdo = self.buscar_nodo(nodo.izquierda, valor)
        if izquierdo:
            return izquierdo
        return self.buscar_nodo(nodo.derecha, valor)

    def imprimir_arbol(self, nodo, nivel=0, direccion="raiz"):
        if nodo is not None:
            print(" " * nivel * 4 + f"{direccion}: {nodo.valor}")
            self.imprimir_arbol(nodo.izquierda, nivel + 1, "izquierda")
            self.imprimir_arbol(nodo.derecha, nivel + 1, "derecha")

# Función para agregar nodos al grafo
def agregar_nodos_grafo(nodo, G, x=0, y=0, nivel=1):
    if nodo is None:
        return
    G.add_node(nodo.valor, pos=(x, y))
    if nodo.izquierda is not None:
        G.add_edge(nodo.valor, nodo.izquierda.valor)
        agregar_nodos_grafo(nodo.izquierda, G, x=x-1/nivel, y=y-1, nivel=nivel+1)
    if nodo.derecha is not None:
        G.add_edge(nodo.valor, nodo.derecha.valor)
        agregar_nodos_grafo(nodo.derecha, G, x=x+1/nivel, y=y-1, nivel=nivel+1)

# Función para visualizar el árbol
def visualizar_arbol(arbol):
    G = nx.DiGraph()
    agregar_nodos_grafo(arbol.raiz, G)
    pos = nx.get_node_attributes(G, 'pos')


    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='purple', node_size=3000, font_color='white', font_weight='bold', edge_color='black')
    plt.title("Árbol Binario")
    plt.show()

#primer arbol
arbol1 = ArbolBinario()


arbol1.agregar_nodo("Diego", None, None)
arbol1.agregar_nodo("Pedro", "Diego", "izquierda")
arbol1.agregar_nodo("Mario", "Diego", "derecha")
arbol1.agregar_nodo("Susan", "Pedro", "izquierda")
arbol1.agregar_nodo("Diana", "Pedro", "derecha")

#segundo arbol

arbol2 = ArbolBinario()


arbol2.agregar_nodo(10, None, None)
arbol2.agregar_nodo(5, 10, "izquierda")
arbol2.agregar_nodo(15, 10, "derecha")
arbol2.agregar_nodo(1, 5, "izquierda")

arbol2.agregar_nodo(25, 15, "derecha")



visualizar_arbol(arbol1)
visualizar_arbol(arbol2)