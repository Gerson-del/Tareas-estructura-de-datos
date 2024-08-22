class ConjuntoADT():
    def __init__(self, conjunto):
        self.conjunto = self.convertir(conjunto)

    def convertir(self, newSet):
        lst = []
        for i in newSet:
            if i not in lst:
                lst.append(i)
        return lst

    def mostrarConjunto(self):
        print(self.conjunto)

    def longitud(self):
        return len(self.conjunto)

    def contiene(self, elemento):
        return elemento in self.conjunto

    def agregar(self, elemento):
        if not self.contiene(elemento):
            self.conjunto.append(elemento)

    def eliminar(self, elemento):
        if self.contiene(elemento):
            self.conjunto = [x for x in self.conjunto if x != elemento]

    def equals(self, otroConjunto):
        otroConjunto = self.convertir(otroConjunto.conjunto)
        if len(self.conjunto) != len(otroConjunto):
            return False
        for i in self.conjunto:
            if i not in otroConjunto:
                return False
        return True

    def esSubConjunto(self, otroConjunto):
        otroConjunto = self.convertir(otroConjunto.conjunto)
        for i in self.conjunto:
            if i not in otroConjunto:
                return False
        return True

    def union(self, otroConjunto):
        otroConjunto = self.convertir(otroConjunto.conjunto)
        nuevo_conjunto = self.conjunto[:]
        for i in otroConjunto:
            if i not in nuevo_conjunto:
                nuevo_conjunto.append(i)
        return ConjuntoADT(nuevo_conjunto)

    def interseccion(self, otroConjunto):
        otroConjunto = self.convertir(otroConjunto.conjunto)
        nuevo_conjunto = [i for i in self.conjunto if i in otroConjunto]
        return ConjuntoADT(nuevo_conjunto)

    def diferencia(self, otroConjunto):
        otroConjunto = self.convertir(otroConjunto.conjunto)
        nuevo_conjunto = [i for i in self.conjunto if i not in otroConjunto]
        return ConjuntoADT(nuevo_conjunto)

conjuntoA = ConjuntoADT([1, 2, 3, 4])
conjuntoB = ConjuntoADT([3, 4, 5, 6])


print("Conjunto A:")
conjuntoA.mostrarConjunto()

print("Conjunto B:")
conjuntoB.mostrarConjunto()


conjuntoA.agregar(7) 
print("Se ha agregado 7 al conjunto A")
conjuntoA.mostrarConjunto()

conjuntoB.eliminar(6)
print("Se ha agregado 6 al conjunto B")
conjuntoB.mostrarConjunto()


print("El conjunto A contiene a 2? ")
print(conjuntoA.contiene(2))  
print("El conjunto A contiene a 6? ")
print(conjuntoB.contiene(6))  


unionAB = conjuntoA.union(conjuntoB)
interseccionAB = conjuntoA.interseccion(conjuntoB)
diferenciaAB = conjuntoA.diferencia(conjuntoB)


print("Unión de A y B:")
unionAB.mostrarConjunto()

print("Intersección de A y B:")
interseccionAB.mostrarConjunto()

print("Diferencia de A y B:")
diferenciaAB.mostrarConjunto()