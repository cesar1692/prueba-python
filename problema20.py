#Define una clase llamada "Calculadora" con métodos estáticos para sumar, restar, multiplicar y dividir dos números.

class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        return a / b

numero1 = float(input("Ingrese un primer número: "))
numero2 = float(input("Ingrese un segundo número: "))
print(f"Suma: {Calculadora.sumar(numero1, numero2)} ")
print(f"Resta: {Calculadora.restar(numero1, numero2)} ")
print(f"Multiplicación: {Calculadora.multiplicar(numero1, numero2)} ")
print(f"División: {Calculadora.dividir(numero1, numero2)} ")