from collections import deque

class ColaADT:
  def __init__(self):
      self.data = deque()

  def esta_vacia(self):
    return len(self.data) == 0

  def longitud(self):
    return len(self.data)

  def frente(self):
    if not self.esta_vacia():
      return self.data[0]
    else:
      raise IndexError("La cola está vacía")

  def encolar(self,valor):
    self.data.append(valor)

  def desencolar(self):
    if not self.esta_vacia():
      return self.data.popleft()
    else:
      raise IndexError("La cola está vacía")


'''Estás diseñando un sistema para
gestionar la cola de pacientes en una clínica médica. Los pacientes llegan uno
por uno a la clínica, y necesitan ser atendidos por orden de llegada.'''

class Paciente:
  def __init__(self,nombre):
     self.nombre = nombre

  def __str__(self):
     return self.nombre

class Clinica:
    def __init__(self):
        self.colaMedica = ColaADT()

    def registrar_paciente(self, nombre_paciente):
        paciente = Paciente(nombre_paciente)
        print(f"Paciente {paciente} agregado")
        self.colaMedica.encolar(paciente)

    def atender_paciente_prioritario(self):
        print(f"Paciente {self.colaMedica.frente()} será atendido")
        self.colaMedica.desencolar()

    def mostrar_estado(self):
        print("Pacientes esperando:")
        for paciente in self.colaMedica.data:
            print(paciente)

    def verificar_vacia(self):
        if self.colaMedica.esta_vacia():
            return "La lista de pacientes está vacía"
        else:
            return "Hay pacientes esperando"

    def mostrar_siguiente(self):
        if not self.colaMedica.esta_vacia():
            print(f"El siguiente paciente es: {self.colaMedica.frente()}")
        else:
            print("No hay pacientes en la cola")

if __name__ == "__main__":
    clinica = Clinica()
    clinica.registrar_paciente("Neftaly")
    clinica.registrar_paciente("Maria")
    clinica.registrar_paciente("Isaac")
    clinica.mostrar_estado()
    clinica.mostrar_siguiente()
    clinica.atender_paciente_prioritario()
    clinica.mostrar_estado()
    clinica.registrar_paciente("Carmen")
    clinica.registrar_paciente("Cesar")
    clinica.atender_paciente_prioritario()
    clinica.mostrar_estado()