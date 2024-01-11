#Crea una clase llamada "Estudiante" que herede de la clase "Persona". Agrega un atributo adicional llamado "carrera" y sobrescribe el método para imprimir los detalles del estudiante.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Carrera: {self.carrera}")


estudiante = Estudiante("Juan Pérez", 30, "Ingeniería Electrónica")
estudiante.imprimir_detalles()