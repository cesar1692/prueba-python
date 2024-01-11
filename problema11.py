#Escribe una función recursiva para calcular el factorial de un número.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))
print(f"El factorial del número {numero} es {factorial(numero)}")