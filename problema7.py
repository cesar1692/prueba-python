#Dada una lista de palabras, escribe un programa que devuelva una nueva lista con las palabras que tengan más de 5 caracteres.

def palabras_largas(palabras):
    palabras_largas = []
    for palabra in palabras:
        if len(palabra) >= 5:
            palabras_largas.append(palabra)
    return palabras_largas

palabras = ["Hola", "soy", "un", "desarrollador", "de", "código"]
palabras_largas = palabras_largas(palabras)
print(f"La lista {palabras} contiene las siguientes palabras con mas de 5 letras: {palabras_largas}")