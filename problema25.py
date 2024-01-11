#Crea una clase llamada "Diccionario" que represente un diccionario personalizado. 
#Agrega métodos para agregar una clave-valor, buscar un valor por clave y eliminar una clave.

class Diccionario:
    def __init__(self):
        self.diccionario = {}

    def agregar_clave_valor(self, clave, valor):
        self.diccionario[clave] = valor

    def buscar_valor_por_clave(self, clave):
        return self.diccionario.get(clave)

    def eliminar_clave(self, clave):
        del self.diccionario[clave]

diccionario = Diccionario()

diccionario.agregar_clave_valor("nombre", "Juan Pérez")
diccionario.agregar_clave_valor("edad", 30)

valor_nombre = diccionario.buscar_valor_por_clave("nombre")
valor_edad = diccionario.buscar_valor_por_clave("edad")

print(valor_nombre)
print(valor_edad)
diccionario.eliminar_clave("nombre")
valor_nombre = diccionario.buscar_valor_por_clave("nombre")
print(valor_nombre)