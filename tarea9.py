# Parte 1 Programar el ADT pila(stack)
class Stack:
  def __init__(self):
    self._data = []

  def is_empty(self):
    return len(self._data) == 0

  def length(self):
    return len(self._data)

  def peek(self):
    if not self.is_empty():
        return self._data[-1]
    else:
        return None  
  def pop(self):
    if not self.is_empty():
      return self._data.pop()
    else:
      return None
  
  def push(self,value):
    self._data.append(value)

  def __str__(self):
      return f"estado actual de la pila: {self._data}"

    
'''
Implementar el programa que dada una entrada de texto, verifique si este contiene llaves balanceadas es decir que cada llave "{" tiene su respectiva llave de cierre "}".
De igual forma con los parentesis "(" y ")".
'''

text = "(({{}))"

def balance(text):
    stack = Stack()
    for char in text:
        if char == "(" or char == "{":
            stack.push(char)
        elif char == ")" or char == "}":
            if stack.is_empty():
                return "Desbalanceado: Existen cerraduras sin apertura"
            top = stack.pop() 

            if (char == ")" and top != "(") or (char == "}" and top != "{"):
                return "Desbalanceado: Cierres y aperturas no coinciden"

    if stack.is_empty():
        return "Las llaves y paréntesis están balanceados"
    else:
        return "Desbalanceado: Existen aperturas sin cierre"
  

if __name__ == "__main__":

  texto1 = "((((((((((((({{}}))"
  texto2 = "(({{}}))"
  texto3 = "(({{))}"
  texto4 = "(({{}"

  print(f"texto 1: {texto1}")
  print(balance(texto1))

  print(f"texto 2: {texto2}")
  print(balance(texto2))

  print(f"texto 1: {texto3}")
  print(balance(texto3))

  print(f"texto 1: {texto4}")
  print(balance(texto4))
