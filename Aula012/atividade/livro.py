from autor import Autor

class Livro:
    def __init__(self, titulo: str, autor: Autor, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"'{self.titulo}' por {self.autor.nome}, {self.paginas} páginas"