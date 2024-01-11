#Crea una función que reciba una lista de palabras y devuelva un diccionario donde las claves sean las palabras y los valores sean la longitud de cada palabra.

def palabras_y_longitudes(palabras):
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

palabras = ["hola", "mundo", "soy", "un", "desarrollador"]
diccionario = palabras_y_longitudes(palabras)
print(diccionario)
