#Crea un programa en Python que calcule el impuesto a pagar según los ingresos anuales de una persona. El programa debe solicitar al usuario 
#ingresar los ingresos anuales y luego calcular el impuesto aplicando la siguiente tabla:
#    • Para ingresos menores o iguales a $10,000, no se paga impuesto.
#    • Para ingresos mayores a $10,000 y menores o iguales a $50,000, el impuesto es del 10%.
#    • Para ingresos mayores a $50,000, el impuesto es del 20%.
#    • Muestra el impuesto a pagar en la consola.

def calcular_impuesto(ingresos):
    if ingresos <= 10000:
        return 0
    elif ingresos <= 50000:
        return ingresos * 0.1
    else:
        return ingresos * 0.2

def main():
    # Solicitamos al usuario los ingresos anuales.
    ingresos = float(input("Ingresos anuales: "))

    # Calculamos el impuesto a pagar.
    impuesto = calcular_impuesto(ingresos)

    # Imprimimos el impuesto a pagar en la consola.
    print("Impuesto a pagar:", impuesto)

if __name__ == "__main__":
    main()