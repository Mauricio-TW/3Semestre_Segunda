from pilhaLivros import PilhaDeLivros

def main():
    pilha = PilhaDeLivros()

    # Adicionando 4 livros à pilha
    pilha.empilhar("O Senhor dos Anéis")
    pilha.empilhar("1984")
    pilha.empilhar("Dom Quixote")
    pilha.empilhar("A Revolução dos Bichos")

    print("\n Pilha atual:")
    pilha.exibir_pilha()

    print("\n Livro no topo da pilha:", pilha.topo())


if __name__ == "__main__":
    main()