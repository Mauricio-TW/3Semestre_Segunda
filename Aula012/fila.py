class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)  # adiciona no fim da fila

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)  # remove do início da fila
        else:
            return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

# Testando a fila
fila = Fila()
fila.enfileirar('A')
fila.enfileirar('B')
fila.enfileirar('C')

print(fila.desenfileirar())  # Saída: A
print(fila.desenfileirar())  # Saída: B
print(fila.esta_vazia())     # Saída: False
print(fila.desenfileirar())  # Saída: C
print(fila.esta_vazia())     # Saída: True
