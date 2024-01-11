#Escribe un programa en Python para gestionar el inventario de una tienda. 
#El programa debe permitir al usuario realizar las siguientes operaciones:
#    • Agregar un nuevo producto al inventario (nombre, precio, cantidad).
#    • Actualizar la cantidad de un producto existente en el inventario.
#    • Mostrar la lista de productos y su disponibilidad en el inventario.

from collections import defaultdict

class Inventario:
    def __init__(self):
        self.inventario = defaultdict(lambda: {"nombre": "", "precio": 0, "cantidad": 0})

    def agregar_producto(self, nombre, precio, cantidad):
        self.inventario[nombre] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

    def actualizar_cantidad(self, nombre, cantidad):
        self.inventario[nombre]["cantidad"] = cantidad

    def mostrar_inventario(self):
        for nombre, producto in self.inventario.items():
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Cantidad:", producto["cantidad"])

if __name__ == "__main__":
    inventario = Inventario()

    # Agregamos un nuevo producto al inventario.
    inventario.agregar_producto("iPhone 13", 1000, 20)

    # Actualizamos la cantidad de un producto existente en el inventario.
    inventario.actualizar_cantidad("iPhone 13", 10)

    # Mostramos la lista de productos y su disponibilidad en el inventario.
    inventario.mostrar_inventario()