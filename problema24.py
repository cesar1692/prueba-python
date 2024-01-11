#Implementa una clase llamada "Empleado" con atributos "nombre", "salario" y "aumento". 
#Agrega un método para calcular el salario actualizado después de aplicar el aumento.

class Empleado:
    def __init__(self, nombre, salario, aumento):
        self.nombre = nombre
        self.salario = salario
        self.aumento = aumento

    def calcular_salario_actualizado(self):
        return self.salario * (1 + self.aumento)


empleado = Empleado("Juan Pérez", 1000, 0.1)

salario_actualizado = empleado.calcular_salario_actualizado()

print(f"El salario actualizado de {empleado.nombre} es {salario_actualizado}")