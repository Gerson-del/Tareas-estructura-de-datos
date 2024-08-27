class Node:
    def __init__(self, givenData):
        self.data = givenData
        self.next = None 

    def printNodes(self):
        current = self
        while current is not None:
          print(current.data)
          current = current.next

nodeA = Node(100) 
nodeB = Node(200) 
nodeC = Node(300) 
nodeD = Node(400) 
nodeE = Node(600) 

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print(" Imprimir todo usando un while.")

nodeA.printNodes()


print("cambiar el valor del 3er nodo de 300 a 333.")

nodeC.data = 333

#imprimir todo nuevamente.
nodeA.printNodes()

print("Insertar un nodo 700 después del nodo 600 (Al final)")

nodeF = Node(700)
nodeE.next = nodeF

#imprimir todo nuevamente.
nodeA.printNodes()

print("Insertar un nodo con valor 50 al principio (antes del nodo 100)")

nodeU = Node(50)
nodeU.next = nodeA
nodeA = nodeU


nodeA.printNodes()