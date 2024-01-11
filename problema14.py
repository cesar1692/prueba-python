#Dado un número entero, escribe un programa que determine si es un número primo.

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Ingrese un número entero: "))
es_primo = es_primo(n)

if es_primo:
    print(f"El número {n} es primo")
else:
    print(f"El número {n} no es primo")