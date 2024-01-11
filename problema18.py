#Implementa una clase llamada "Pila" que tenga métodos para apilar, desapilar y verificar si está vacía.

class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if len(self.pila) == 0:
            return None
        return self.pila.pop()

    def esta_vacia(self):
        return len(self.pila) == 0

pila = Pila()

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())

print(pila.esta_vacia())