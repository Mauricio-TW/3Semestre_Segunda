class Autor:
    def __init__(self, nome: str, nacionalidade: str):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f"{self.nome} ({self.nacionalidade})"