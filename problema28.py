#Crea una clase llamada "CuentaBancaria" con atributos "titular" y "saldo". 
#Agrega métodos para depositar dinero, retirar dinero y verificar el saldo.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError("No hay suficiente saldo")

    def consultar_saldo(self):
        return self.saldo


cuenta_bancaria = CuentaBancaria("Juan Pérez", 1000)
cuenta_bancaria.depositar(100)
cuenta_bancaria.retirar(500)
print(f"El saldo del titular {cuenta_bancaria.titular} es de: {cuenta_bancaria.consultar_saldo()}")