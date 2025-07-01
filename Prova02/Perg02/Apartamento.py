from Torre import Torre

class Apartamento:
    def __init__(self, id, numero_apartamento, numero_vaga_garagem, torre: Torre):
        self.id = id
        self.numero_apartamento = numero_apartamento
        self.numero_vaga_garagem = numero_vaga_garagem
        self.torre = torre

    def __str__(self):
        return (f"Apartamento {self.numero_apartamento} (ID: {self.id}), "
                f"Vaga: {self.numero_vaga_garagem}, Torre: {self.torre.nome}")