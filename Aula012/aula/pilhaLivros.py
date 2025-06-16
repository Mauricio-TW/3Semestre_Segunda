class PilhaDeLivros:
    def __init__(self):
        self.pilha = []

    def empilhar(self, livro):
        """Adiciona um livro ao topo da pilha."""
        self.pilha.append(livro)
        print(f"Livro '{livro}' adicionado à pilha.")

    def desempilhar(self):
        """Remove o livro do topo da pilha."""
        if self.esta_vazia():
            print("A pilha está vazia. Nenhum livro para remover.")
            return None
        livro = self.pilha.pop()
        print(f"Livro '{livro}' removido da pilha.")
        return livro

    def topo(self):
        """Mostra o livro no topo da pilha sem remover."""
        if self.esta_vazia():
            print("A pilha está vazia.")
            return None
        return self.pilha[-1]

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.pilha) == 0

    def exibir_pilha(self):
        """Exibe todos os livros da pilha."""
        if self.esta_vazia():
            print("A pilha está vazia.")
        else:
            print("Livros na pilha (do topo para a base):")
            for livro in reversed(self.pilha):
                print(f"{livro}")