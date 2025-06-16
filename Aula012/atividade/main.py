from autor import Autor
from livro import Livro
from listaAutores import ListaAutoresOrdenada
from pilhaLivros import PilhaLivros

def menu():
    lista_autores = ListaAutoresOrdenada()
    pilha_livros = PilhaLivros()

    while True:
        print("\n=== MENU ===")
        print("1. Adicionar Autor")
        print("2. Adicionar Livro")
        print("3. Remover Livro do Topo da Pilha")
        print("4. Mostrar Lista de Autores")
        print("5. Mostrar Pilha de Livros")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            autor = Autor(nome, nacionalidade)
            lista_autores.inserir(autor)
            print("Autor adicionado com sucesso!")

        elif opcao == "2":
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor (já cadastrado): ")
            autor = lista_autores.buscar_por_nome(nome_autor)
            if autor:
                try:
                    paginas = int(input("Número de páginas: "))
                    livro = Livro(titulo, autor, paginas)
                    pilha_livros.empilhar(livro)
                    print("Livro adicionado à pilha com sucesso!")
                except ValueError:
                    print("Número de páginas inválido.")
            else:
                print("Autor não encontrado. Cadastre o autor primeiro.")

        elif opcao == "3":
            removido = pilha_livros.desempilhar()
            if removido:
                print(f"Livro removido: {removido}")

        elif opcao == "4":
            lista_autores.mostrar_lista()

        elif opcao == "5":
            pilha_livros.mostrar_pilha()

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()