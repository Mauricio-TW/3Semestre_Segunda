class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)  # adiciona no topo da pilha

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()  # remove do topo da pilha
        else:
            return None

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

# Testando a pilha
pilha = Pilha()
pilha.empilhar('A')
pilha.empilhar('B')
pilha.empilhar('C')

print(pilha.desempilhar())  # Saída: C
print(pilha.topo())         # Saída: B
print(pilha.esta_vazia())   # Saída: False
print(pilha.desempilhar())  # Saída: B
print(pilha.desempilhar())  # Saída: A
print(pilha.esta_vazia())   # Saída: True
