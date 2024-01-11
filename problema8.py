#Escribe un programa que determine si una cadena de texto es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
#Ejemplo de palabras palindromo: radar, aerea, dañad, arenera

def es_palindromo(cadena):
    for i in range(len(cadena) // 2):
        if cadena[i] != cadena[-i - 1]:
            return False
    return True

cadena = input("Ingrese una cadena de texto: ")

es_palindromo = es_palindromo(cadena)

if es_palindromo:
    print(f"La cadena {cadena} es un palíndromo")
else:
    print(f"La cadena {cadena} no es un palíndromo")