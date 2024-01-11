#Crea una función que tome una lista de números y devuelva la suma de todos los elementos

def suma_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

lista_numeros = [1, 2, 3, 4, 5]
suma = suma_lista(lista_numeros)
print(f"La suma de la lista {lista_numeros} es: {suma}")