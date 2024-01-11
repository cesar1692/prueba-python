#Crea un programa en Python que simule el proceso de ventas de una tienda. 
#El programa debe permitir al usuario ingresar el nombre y el precio de los productos vendidos, así como la cantidad vendida. 
#Luego, calcula el total de ventas y muestra el resultado en la consola.

def calcular_total_ventas(ventas):
    total = 0
    print(f"Ventas:  {ventas}")
    for producto, atributos in ventas.items():
    	total += atributos['precio'] * atributos['cantidad']
    return total

if __name__ == "__main__":
    # Inicializamos el diccionario de ventas.
    ventas = {}

    # Solicitamos al usuario el ingreso de los datos de las ventas.
    while True:
        # Solicitamos el nombre del producto.
        nombre_producto = input("Nombre del producto: ")

        # Si el nombre del producto es vacío, terminamos el ciclo.
        if nombre_producto == "":
            break

        # Solicitamos el precio del producto.
        precio_producto = float(input("Precio del producto: "))

        # Solicitamos la cantidad vendida.
        cantidad_vendida = int(input("Cantidad vendida: "))

        # Agregamos los datos del producto al diccionario de ventas.
        ventas[nombre_producto] = {"precio": precio_producto, "cantidad": cantidad_vendida}

    # Calculamos el total de ventas.
    total_ventas = calcular_total_ventas(ventas)

    # Imprimimos el total de ventas en la consola.
    print("Total de ventas:", total_ventas)