from Cliente import Cliente

class Fisico(Cliente):
    
    def __innit__(self, nome = None, cpf = None):
        super().__innit__(nome)
        self.cpf = cpf
        
    def cadastrar(self):
        self.nome = input("Digite o nome: ")
        self.limite = float(input("Digite o limite: "))
        self.cpf = input("Digite o CPF: ")
        
    def __str__(self) -> str:
        return super().__str__() + "\nCPF: " + self.cpf
    