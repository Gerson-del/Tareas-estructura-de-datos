class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def transversal(self):
        current = self
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("none")

class ListaLigada:
    def __init__(self):
        self.head = None  # Iniciamos el primer nodo como vacío

    def get_size(self):
        counter = 0
        current = self.head
        while current is not None:
            current = current.next
            counter += 1
        return counter

    def esta_vacia(self):
        return self.head is None

    def agregar_al_final(self, data):
        new_node = Node(data)
        if not self.head:  # Lista vacía
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

    def agregar_al_inicio(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def agregar_despues_de(self, referencia, valor):
        current = self.head
        while current is not None:
            if current.data == referencia:
                new_node = Node(valor)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Referencia no se encontró en la lista")
        return -1

    def eliminar(self, posicion):
        if self.head is None:
            print("La lista está vacía")
            return -1

        if posicion == 0:
            self.head = self.head.next
            return

        counter = 0
        current = self.head
        previo = None

        while current is not None:
            if counter == posicion:
                if previo is not None:
                    previo.next = current.next
                return
            previo = current
            current = current.next
            counter += 1

        print("No se encontró la posición")
        return -1

    def eliminar_el_primero(self):
        if self.head is None:
            print("La lista está vacía")
            return -1
        self.head = self.head.next

    def eliminar_el_final(self):
        if self.head is None:  # Lista vacía
            print("La lista está vacía")
            return -1

        if self.head.next is None:  # Solo un nodo
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def buscar(self, valor):
        if self.head is None:
            print("La lista está vacía")
            return -1

        current = self.head
        contador = 0

        while current is not None:
            if current.data == valor:
                return contador
            current = current.next
            contador += 1

        return -1

    def actualizar(self, a_buscar, valor):
        if self.head is None:
            print("La lista está vacía")
            return -1

        current = self.head

        while current is not None:
            if current.data == a_buscar:
                current.data = valor
                return True
            current = current.next

        print("No se encontró el elemento a buscar")
        return -1


class SmartPhone:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"{self.marca} {self.modelo} (${self.precio})"


def main():

    lista_smartphones = ListaLigada()


    lista_smartphones.agregar_al_final(SmartPhone("Huawei", "Mate 40 Pro", 1099))
    lista_smartphones.agregar_al_final(SmartPhone("Xiaomi", "Redmi Note 10", 199))
    lista_smartphones.agregar_al_final(SmartPhone("Google", "Pixel 6", 599))
    lista_smartphones.agregar_al_final(SmartPhone("Apple", "iPhone 13 Pro", 999))
    lista_smartphones.agregar_al_final(SmartPhone("Samsung", "Galaxy Z Fold 3", 1799))

    print("Lista de smartphones:")
    lista_smartphones.head.transversal()


    lista_smartphones.eliminar(2)

    print("\nLista después de eliminar el tercer smartphone:")
    lista_smartphones.head.transversal()


    lista_smartphones.actualizar(SmartPhone("Xiaomi", "Redmi Note 10", 199), SmartPhone("OnePlus", "9 Pro", 969))


    lista_smartphones.agregar_al_inicio(SmartPhone("Sony", "Xperia 1 III", 1199))
    lista_smartphones.agregar_al_final(SmartPhone("Motorola", "Edge 20 Pro", 699))

    print("\nLista después de agregar un smartphone al inicio y otro al final:")
    lista_smartphones.head.transversal()


    lista_smartphones.eliminar_el_primero()

    print("\nLista después de eliminar el primer smartphone:")
    lista_smartphones.head.transversal()

if __name__ == "__main__":
    main()
