#Implementa una clase llamada "ÁrbolBinario" que represente un árbol binario.
#Agrega métodos para insertar un nodo, recorrer el árbol en orden y buscar un valor en el árbol.

class ArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def insertar(self, valor):
        if valor < self.valor:
            if self.izquierdo is None:
                self.izquierdo = ArbolBinario(valor)
            else:
                self.izquierdo.insertar(valor)
        else:
            if self.derecho is None:
                self.derecho = ArbolBinario(valor)
            else:
                self.derecho.insertar(valor)

    def recorrer_en_orden(self):
        if self.izquierdo is not None:
            self.izquierdo.recorrer_en_orden()
        print(self.valor)
        if self.derecho is not None:
            self.derecho.recorrer_en_orden()

    def buscar(self, valor):
        if self.valor == valor:
            return True
        elif valor < self.valor and self.izquierdo is not None:
            return self.izquierdo.buscar(valor)
        elif valor > self.valor and self.derecho is not None:
            return self.derecho.buscar(valor)
        else:
            return False


arbol_binario = ArbolBinario(10)

arbol_binario.insertar(5)
arbol_binario.insertar(15)
arbol_binario.insertar(2)
arbol_binario.insertar(7)
arbol_binario.insertar(12)

arbol_binario.recorrer_en_orden()

print(arbol_binario.buscar(10))
print(arbol_binario.buscar(5))
print(arbol_binario.buscar(15))
print(arbol_binario.buscar(2))
print(arbol_binario.buscar(7))
print(arbol_binario.buscar(12))