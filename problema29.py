#Define una clase llamada "Matriz" que represente una matriz de números. 
#Agrega métodos para sumar dos matrices y multiplicar una matriz por un escalar.

class Matriz:
    def __init__(self, filas, columnas, datos):
        self.filas = filas
        self.columnas = columnas
        self.datos = datos

    def sumar_matrices(self, matriz):
        if self.filas != matriz.filas or self.columnas != matriz.columnas:
            raise ValueError("Las matrices deben tener el mismo tamaño")

        matriz_resultado = Matriz(self.filas, self.columnas, [[0] * self.columnas for _ in range(self.filas)])

        for i in range(self.filas):
            for j in range(self.columnas):
                matriz_resultado.datos[i][j] = self.datos[i][j] + matriz.datos[i][j]

        return matriz_resultado

    def multiplicar_por_escalar(self, escalar):
        matriz_resultado = Matriz(self.filas, self.columnas)

        for i in range(self.filas):
            for j in range(self.columnas):
                matriz_resultado.datos[i][j] = self.datos[i][j] * escalar

        return matriz_resultado

matriz_1 = Matriz(2, 3, [[1, 2, 3], [4, 5, 6]])
matriz_2 = Matriz(2, 3, [[7, 8, 9], [10, 11, 12]])

matriz_resultado = matriz_1.sumar_matrices(matriz_2)

print(matriz_resultado.datos)