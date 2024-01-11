#Crea una función que reciba una cadena de texto y cuente cuántas veces aparece una letra específica.

def cuenta_letra(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

cadena = "Hola mundo, soy desarrollador Odoo!"
letra_encontrar = "a"
contador = cuenta_letra(cadena, letra_encontrar)
print(f'La letra "{letra_encontrar}" se epite {contador} veces en el texto "{cadena}"')