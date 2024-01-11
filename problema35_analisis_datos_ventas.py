#Escribe un programa en Python que analice los datos de ventas de una tienda. El programa debe leer un archivo CSV que contiene información #sobre las ventas realizadas (fecha, producto, cantidad, precio) y realizar lo siguiente:
#    • Calcular el total de ventas.
#    • Determinar el producto más vendido.
#    • Calcular el promedio de ventas diarias.
#NOTA: Se incluye archivo csv de ejemplo

import csv


def calcular_total_ventas(ventas):
    """
    Calcula el total de ventas.

    Args:
        ventas: Un diccionario que contiene los datos de las ventas.

    Returns:
        El total de ventas.
    """

    total = 0
    for fecha, productos in ventas.items():
        for producto, cantidad, precio in productos:
            total += precio * cantidad
    return total


def determinar_producto_mas_vendido(ventas):
    """
    Determina el producto más vendido.

    Args:
        ventas: Un diccionario que contiene los datos de las ventas.

    Returns:
        El producto más vendido.
    """

    producto_mas_vendido = None
    cantidad_mas_vendida = 0
    for fecha, productos in ventas.items():
        for producto, cantidad, precio in productos:
            if cantidad > cantidad_mas_vendida:
                producto_mas_vendido = producto
                cantidad_mas_vendida = cantidad
    return producto_mas_vendido


def calcular_promedio_ventas_diarias(ventas):
    """
    Calcula el promedio de ventas diarias.

    Args:
        ventas: Un diccionario que contiene los datos de las ventas.

    Returns:
        El promedio de ventas diarias.
    """

    if len(ventas) == 0:
        return 0

    fechas = set()
    for fecha, _ in ventas.items():
        fechas.add(fecha)

    return calcular_total_ventas(ventas) / len(fechas)


def main():
    # Abrimos el archivo CSV.
    with open("ventas.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")

        # Inicializamos el diccionario de ventas.
        ventas = {}

        # Leemos los datos del archivo CSV.
        count = 0
        for row in reader:
            count +=1
            # Obtenemos la fecha, el producto, la cantidad y el precio de la venta.
            if count > 1:
                print(f"{row}")
                fecha = row[0]
                producto = row[1]
                cantidad = int(row[2])
                precio = float(row[3])

                # Agregamos los datos de la venta al diccionario de ventas.
                if fecha not in ventas:
                    ventas[fecha] = []
                ventas[fecha].append((producto, cantidad, precio))

        # Calculamos el total de ventas.
        total_ventas = calcular_total_ventas(ventas)

        # Determinamos el producto más vendido.
        producto_mas_vendido = determinar_producto_mas_vendido(ventas)

        # Calculamos el promedio de ventas diarias.
        promedio_ventas_diarias = calcular_promedio_ventas_diarias(ventas)

        # Imprimimos los resultados.
        print("Total de ventas:", total_ventas)
        print("Producto más vendido:", producto_mas_vendido)
        print("Promedio de ventas diarias:", round(promedio_ventas_diarias,2))


if __name__ == "__main__":
    main()