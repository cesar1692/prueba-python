#Define una clase llamada "Rectángulo" con atributos "ancho" y "altura". Agrega métodos para calcular el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def calcular_area(self):
        return self.ancho * self.altura

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.altura)

a = 10
b = 20
rectangulo = Rectangulo(a, b)

area = rectangulo.calcular_area()
perimetro = rectangulo.calcular_perimetro()

print(f"Triangulo: Ancho: {a} Alto: {b}")
print(f"El área del rectángulo es {area}")
print(f"El perímetro del rectángulo es {perimetro}")