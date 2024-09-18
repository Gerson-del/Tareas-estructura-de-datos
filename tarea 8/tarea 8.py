from collections import deque

class ClienteBanco:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"

class ColaConPrioridadAcotada:
    def __init__(self, niveles):

        self.colas = [deque() for _ in range(0, niveles)]

    def encolar(self, prioridad, elemento):

        if 1 <= prioridad <= len(self.colas):
            self.colas[prioridad - 1].append(elemento)

    def desencolar(self):
        for cola in self.colas:
            if cola:
                return cola.popleft()
        return None

    def is_empty(self):
        return all(not cola for cola in self.colas)

    def print_estado(self):
        for i, cola in enumerate(self.colas, start=1):
            print(f"Prioridad {i}: {[str(cliente) for cliente in cola]}")

def main():
    cola = ColaConPrioridadAcotada(5)

    # 1. 
    cola.encolar(4, ClienteBanco("Jorge (cliente nuevo)", 4))
    cola.encolar(4, ClienteBanco("martha (cliente nuevo)", 4))

    # 2. 
    cola.encolar(5, ClienteBanco("ivan (cliente nuevo)", 5))
    cola.encolar(5, ClienteBanco("marcelo (cliente nuevo)", 5))
    cola.encolar(5, ClienteBanco("rufus (cliente nuevo)", 5))

    # 3. 
    cola.encolar(1, ClienteBanco("Shakira (celebridad)", 1))

    # 4.
    print("Estado de la cola:")
    cola.print_estado()

    # 5.
    cliente_atendido = cola.desencolar()
    if cliente_atendido:
        print(f"\nCliente atendido: {cliente_atendido.nombre} retira $10,000")

    # 6.
    cola.encolar(3, ClienteBanco("Joel (Cliente Frecuente)", 3))
    cola.encolar(2, ClienteBanco("Angel (Cliente Premium)", 2))

    # 7.
    cliente_atendido = cola.desencolar()
    if cliente_atendido:
        print(f"\nCliente atendido: {cliente_atendido.nombre}")

    # 8.
    print("\nEstado de la cola:")
    cola.print_estado()

    # 9. 
    print("\nAtendiendo todos los clientes restantes:")
    while not cola.is_empty():
        cliente_atendido = cola.desencolar()
        if cliente_atendido:
            print(f"Cliente atendido: {cliente_atendido.nombre}")

    # 10. 
    print("\nEstado final de la cola:")
    cola.print_estado()

if __name__ == "__main__":
    main()