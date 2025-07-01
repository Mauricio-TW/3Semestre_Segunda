from Torre import Torre
from Apartamento import Apartamento
from FilaVagas import FilaEsperaGaragem

def menu():

    torre1 = Torre(1, "Torre A", "Av. Central, 100")
    fila = FilaEsperaGaragem()

    while True:
        print("\n--- MENU ---")
        print("1. Adicionar apartamento à fila de espera")
        print("2. Atribuir vaga a um apartamento")
        print("3. Imprimir fila de espera")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            id_apartamento = input("Digite o ID do apartamento: ")
            numero_apartamento = input("Digite o número do apartamento: ")
            
            apt = Apartamento(id=int(id_apartamento), numero_apartamento=numero_apartamento, 
                              numero_vaga_garagem=None, torre=torre1)
            fila.adicionar_apartamento(apt)
        
        elif opcao == '2':
            numero_vaga = input("Digite o número da vaga a ser atribuída: ")
            fila.atribuir_vaga(numero_vaga)
        
        elif opcao == '3':
            fila.imprimir_fila()
        
        elif opcao == '4':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
