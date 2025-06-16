from livro import Livro

class PilhaLivros:
    def __init__(self):
        self.livros = []

    def empilhar(self, livro: Livro):
        self.livros.append(livro)

    def desempilhar(self):
        return self.livros.pop() if self.livros else None

    def esta_vazia(self):
        return len(self.livros) == 0

    def topo(self):
        return self.livros[-1] if self.livros else None

    def mostrar_pilha(self):
        print("Pilha de Livros:")
        for livro in reversed(self.livros):
            print(livro)