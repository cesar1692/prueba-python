#Escribe un programa que reciba una lista de números y devuelva una nueva lista con los elementos en orden inverso.

def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(lista)
print(f"Lista original: {lista}")
print(f"Lista invertida: {lista_invertida}")
