#Escribe un programa en Python que calcule el balance total de una empresa. 
#El programa debe solicitar al usuario el ingreso de los ingresos y los gastos de la empresa, 
#y luego mostrar el balance total (ingresos - gastos) en la consola.

def calcular_balance(ingresos, gastos):
    return ingresos - gastos


if __name__ == "__main__":
    # Solicitamos al usuario el ingreso de los ingresos y los gastos de la empresa.
    ingresos = float(input("Ingresos: "))
    gastos = float(input("Gastos: "))

    # Calculamos el balance total de la empresa.
    balance = calcular_balance(ingresos, gastos)

    # Imprimimos el balance total en la consola.
    print("Balance total:", balance)