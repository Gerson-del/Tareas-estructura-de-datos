class PilaADT:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def obtener_medio(pila):
  posicion_medio = pila.size() // 2

  return obtener_medio_aux(pila,posicion_medio)

def obtener_medio_aux(pila, posicion_medio, contador= 0):
  if contador == posicion_medio:
    valor_medio = pila.pop()
    pila.push(valor_medio)
    return valor_medio

  else:
    elemento = pila.pop()
    resultado = obtener_medio_aux(pila,posicion_medio,contador + 1)
    pila.push(elemento)
    return resultado




mi_pila = PilaADT()
for i in [1, 2, 3, 4, 5]:
    mi_pila.push(i)


valor_medio = obtener_medio(mi_pila)
print(f"El valor en la posición media es: {valor_medio}")


def suma_recursiva(lst):
  sum = 0

  if len(lst) == 0:
    return 0
  else:
    return  lst[0] + suma_recursiva(lst[1:])

numeros = [1, 2, 3, 4, 5]
resultado = suma_recursiva(numeros)
print(resultado)