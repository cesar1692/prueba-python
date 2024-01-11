#Dado un número entero, escribe un programa que determine si es par o impar.

def es_par(n):
    if (n % 2 == 0):
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

if es_par(numero):
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")