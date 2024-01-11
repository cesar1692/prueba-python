#Implementa una clase llamada "PilaLimitada" que herede de la clase "Pila" y tenga un límite máximo de elementos. 
#Agrega un método para verificar si la pila está llena.

class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        return self.pila.pop()

    def esta_vacia(self):
        return len(self.pila) == 0


class PilaLimitada(Pila):
    def __init__(self, limite):
        super().__init__()
        self.limite = limite

    def apilar(self, elemento):
        if len(self.pila) < self.limite:
            super().apilar(elemento)
        else:
            raise ValueError("La pila está llena")

    def esta_llena(self):
        return len(self.pila) >= self.limite
