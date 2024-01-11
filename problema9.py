#Crea una función que tome una lista de números y devuelva una nueva lista con los números pares.

def numeros_pares(numeros):
    numeros_pares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

numeros = [1, 2, 3, 4, 5]
numeros_pares = numeros_pares(numeros)
print(f"Los numeros pares de la siguiente lista {numeros} son los siguientes {numeros_pares}")