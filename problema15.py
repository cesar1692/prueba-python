#Crea una función que reciba una lista de números y devuelva el número más grande y el número más pequeño.

def maximo_minimo(numeros):
    maximo = numeros[0]
    minimo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    return maximo, minimo

numeros = [1, 2, 3, 4, 5]
maximo, minimo = maximo_minimo(numeros)
print(f"Lista de números {numeros}")
print(f"El número más grande es {maximo}")
print(f"El número más pequeño es {minimo}")