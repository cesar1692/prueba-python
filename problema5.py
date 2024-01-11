#Escribe un programa que genere e imprima los primeros Fibonacci hasta un número límite ingresado por el usuario.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

limite = int(input("Ingrese un número límite: "))

for i in range(limite):
    print(fibonacci(i))