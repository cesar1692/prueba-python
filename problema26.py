#Define una clase llamada "Circulo" con atributos "radio" y "color". Agrega un método para calcular el área del círculo.

class Circulo:
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    def calcular_area(self):
        pi = 3.1416
        return pi * self.radio ** 2

circulo = Circulo(5, "azul")
area = circulo.calcular_area()
print(f"El área del circulo {circulo.color} con radio {circulo.radio} es {area}")