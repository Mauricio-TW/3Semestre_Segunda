from categoria import Categoria
from produto import Desktop, Notebook

def menu():
    categorias = [
        Categoria(1, "Gamer"),
        Categoria(2, "Trabalho"),
        Categoria(3, "Estudo")
    ]

    while True:
        print("\n=== CADASTRO DE PRODUTO ===")
        print("1 - Cadastrar Desktop")
        print("2 - Cadastrar Notebook")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando...")
            break

        modelo = input("Modelo: ")
        cor = input("Cor: ")
        try:
            preco = float(input("Preço: "))
        except ValueError:
            print("Preço inválido.")
            continue

        print("\nCategorias:")
        for c in categorias:
            print(f"{c.id} - {c.nome}")
        cat_id = int(input("ID da categoria: "))
        categoria = next((c for c in categorias if c.id == cat_id), None)
        if not categoria:
            print("Categoria inválida.")
            continue

        if opcao == "1":
            potencia = int(input("Potência da Fonte (W): "))
            produto = Desktop(modelo, cor, preco, categoria, potencia)
        elif opcao == "2":
            tempo = float(input("Tempo de Bateria (h): "))
            produto = Notebook(modelo, cor, preco, categoria, tempo)
        else:
            print("Opção inválida.")
            continue

        print("\n" + produto.cadastrar())

if __name__ == "__main__":
    menu()