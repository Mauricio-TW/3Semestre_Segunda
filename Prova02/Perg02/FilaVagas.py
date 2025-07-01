from Apartamento import Apartamento
from Torre import Torre

class FilaEsperaGaragem:
    def __init__(self):
        self.fila = []

    def adicionar_apartamento(self, apartamento):
        if apartamento.numero_vaga_garagem is None:
            self.fila.append(apartamento)
            print(f"Apartamento {apartamento.numero_apartamento} adicionado à fila de espera.")
        else:
            print(f"Apartamento {apartamento.numero_apartamento} já possui vaga.")

    def atribuir_vaga(self, numero_vaga):
        if self.fila:
            apartamento = self.fila.pop(0)
            apartamento.numero_vaga_garagem = numero_vaga
            print(f"Apartamento {apartamento.numero_apartamento} recebeu a vaga {numero_vaga}.")
            return apartamento
        else:
            print("Nenhum apartamento na fila de espera.")
            return None

    def imprimir_fila(self):
        print("Fila de espera por vaga de garagem:")
        if not self.fila:
            print("Fila vazia.")
        else:
            for i, apt in enumerate(self.fila, start=1):
                print(f"{i}. {apt}")
