from cidade import cidade

class Pessoa:
    def __init__(self, nome = None, cpf = None, cid = cidade("Itati") ):
        self.id = None
        self.nome = nome
        self.cpf = cpf
        self.cidade = cidade
        self.salario = 1518.00

    def setSalario(self, valor):
        if valor > self.salario:
            self.salario = valor
    def __str__(self):
        txt = "Nome: " + self.nome
        txt += "\nCPF: " + self.cpf
        txt += "\nSalario: " + str(self.salario)
        txt += "\nCidade: " + str (self.cidade)
        return txt