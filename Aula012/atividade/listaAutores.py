from autor import Autor

class NoAutor:
    def __init__(self, autor: Autor):
        self.autor = autor
        self.proximo = None

class ListaAutoresOrdenada:
    def __init__(self):
        self.inicio = None

    def inserir(self, autor: Autor):
        novo_no = NoAutor(autor)
        if self.inicio is None or autor.nome < self.inicio.autor.nome:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo and atual.proximo.autor.nome < autor.nome:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    def mostrar_lista(self):
        print("Autores na lista (ordenados):")
        atual = self.inicio
        while atual:
            print(atual.autor)
            atual = atual.proximo