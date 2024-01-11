#Dada una lista de números, escribe un programa que devuelva la suma de los números positivos y la suma de los números negativos por separado.

def suma_numeros(numeros):
    suma_positivos = 0
    suma_negativos = 0
    for numero in numeros:
        if numero >= 0:
            suma_positivos += numero
        else:
            suma_negativos += numero
    return suma_positivos, suma_negativos

numeros = [1, 2, 3, -4, -5]

suma_positivos, suma_negativos = suma_numeros(numeros)

print(f"Lista de numeros: {numeros}")
print(f"La suma de los números positivos es {suma_positivos}")
print(f"La suma de los números negativos es {suma_negativos}")