# Classe base (superclasse)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Classe derivada (subclasse)
class Aluno(Pessoa):  # Herda de Pessoa
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # Chama o construtor da classe Pessoa
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f"Eu sou aluno do curso de {self.curso}.")

# Criando um objeto da subclasse
aluno1 = Aluno("Mauricio", 25, "Sistemas de Informação")
aluno1.apresentar()
