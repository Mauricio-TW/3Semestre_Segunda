class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar(self, valor):
        novo_no = No(valor)
        if not self.head:  # lista vazia
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
            self.tail = novo_no

    def imprimir_frente(self):
        atual = self.head
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo
        print("None")

    def imprimir_tras(self):
        atual = self.tail
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.anterior
        print("None")

# Testando
lista = ListaDuplamenteEncadeada()
lista.adicionar(10)
lista.adicionar(20)
lista.adicionar(30)

print("Impressão da lista da frente para trás:")
lista.imprimir_frente()

print("Impressão da lista de trás para frente:")
lista.imprimir_tras()
