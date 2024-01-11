#Crea una clase llamada "Libro" con atributos "título", "autor" y "año". Agrega un método para imprimir los detalles del libro.

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def imprimir_detalles(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")

libro = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro.imprimir_detalles()