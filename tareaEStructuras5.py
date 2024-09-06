class NodoDoble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def transversal(self):
        current = self
        print("none <->", end = "")
        while current is not None:
            print(current.data, end="<->")
            current = current.next
        print("none")

class DoubleLinkedList:
    def __init__(self):
        self.head = None  # Iniciamos el primer nodo como vacío

    def get_tamanio(self):
        counter = 0
        current = self.head
        while current is not None:
            current = current.next
            counter += 1
        return counter

    def esta_vacia(self):
        return self.head is None


    def agregar_al_final(self, valor):
        new_node = NodoDoble(valor)
        if not self.head:  # Lista vacía
            self.head = new_node
            return
        else:
          current = self.head
          while current.next is not None:
            current = current.next
          current.next = new_node
          new_node.prev = current


    def agregar_al_inicio(self, data):
        new_node = NodoDoble(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def agregar_despues_de(self, referencia, valor):
      current = self.head
      # supongamos que tenemos 2 <-> 3 <-> 5 y queremos agregar 4 despues del 3
      while current is not None:
        if current.data == referencia:
          new_node = NodoDoble(valor)
          new_node.next = current.next # 4.next = 5 conectamos 4 con 5 
          if current.next is not None:
            current.next.prev = new_node #5.prev = 4
          current.next = new_node
          new_node.prev = current
          return
        current = current.next
      print("No se encontro su elemento en la lista")
      return -1

    def obtener(self,posicion):
      counter = 0
      current = self.head
      while current is not None:
        if counter == posicion:
          return current.data
        counter += 1
      return None
  
    def eliminar(self, posicion):
        if self.head is None:
            print("La lista está vacía")
            return -1

        # Eliminar el primer nodo
        if posicion == 0:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return

        counter = 0
        current = self.head

        while current is not None:
            if counter == posicion:
                if current.next is not None:
                    current.next.prev = current.prev
                if current.prev is not None:
                    current.prev.next = current.next
                return
            current = current.next
            counter += 1

        print("No se encontró la posición")
        return -1


    def eliminar_el_primero(self):
      if self.head is None:
        print("La lista esta vacia")
        return -1
      if self.head.next is None:
        self.head = None
      else:
        self.head = self.head.next
        self.head.prev = None

    def eliminar_el_final(self):
      if self.head is None:
        print("La lista esta vacia")
        return -1

      if self.head.next is None:
        self.head = None
        return

      current = self.head

      while current.next.next is not None:
        current = current.next
  
      current.next = None



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

    def transversal(self, direccion="izq_a_der"):
        if self.head is None:
            print("La lista está vacía")
            return
        
        if direccion == "izq_a_der":
            current = self.head
            print("none <->", end="")
            while current is not None:
                print(current.data, end="<->")
                current = current.next
            print("none")
        elif direccion == "der_a_izq":
            # Primero buscamos el último nodo
            current = self.head
            while current.next is not None:
                current = current.next
            # Ahora recorremos hacia atrás
            print("none <->", end="")
            while current is not None:
                print(current.data, end="<->")
                current = current.prev
            print("none")



# Ejemplo práctico
def main():
      lista = DoubleLinkedList()

      #Agregamos los elementos"

      lista.agregar_al_inicio(50) 
      lista.agregar_al_final(60)
      lista.agregar_al_final(65)
      lista.agregar_al_final(70)
      lista.agregar_al_final(80)
      lista.agregar_al_final(90)

      print("Imprimir el contenido: ")

      lista.transversal()

      lista.eliminar(2) # Eliminamos el de la posicion 2

      print("volver a imprimir el contenido. (se elimino la posicion 2)")

      lista.transversal()

      #Actualizar el cuarto elemento a 88.

      lista.actualizar(70,88)
      print("\nLista después de actualizar el cuarto elemento a 88:")
      lista.transversal()

      print("Buscar el valor 80, e imprimir en que posición se encuentra.")
      lista.buscar(80)

if __name__ == "__main__":
    main()