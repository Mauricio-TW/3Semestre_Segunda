class Cidade:

    def __init__(self, nome = "Porto Alegre"):
        self.id = None
        self.nome = nome

    def __str__(self) -> str:
        return "Id " +str(self.id) + " - Nome da Cidade: " + self.nome