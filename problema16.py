#Crea una clase llamada "Persona" con atributos "nombre" y "edad". Agrega un método para imprimir los detalles de la persona.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

persona = Persona("Juan Pérez", 30)
persona.imprimir_detalles()