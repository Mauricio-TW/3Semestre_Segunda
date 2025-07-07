class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        return self.__saldo

# Testando
conta = ContaBancaria("Mauricio", 1000)
conta.depositar(500)
conta.sacar(300)
print("Saldo atual:", conta.ver_saldo())

# Tentando acessar o saldo diretamente (não recomendado)
# print(conta.__saldo)  # Isso gera erro: AttributeError
