#Implementa una clase llamada "Cola" que tenga métodos para encolar, desencolar y verificar si está vacía.

class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if len(self.cola) == 0:
            return None
        return self.cola.pop(0)

    def esta_vacia(self):
        return len(self.cola) == 0


cola = Cola()

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

print(cola.desencolar())
print(cola.desencolar())
print(cola.desencolar())

print(cola.esta_vacia())