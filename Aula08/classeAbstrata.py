from abc import ABC, abstractmethod

# Classe abstrata
class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        pass  # Método abstrato, sem implementação

# Subclasse que implementa o método abstrato
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

# Subclasse que implementa o método abstrato
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

# Testando
cachorro = Cachorro()
gato = Gato()

cachorro.fazer_som()  # Saída: Au au!
gato.fazer_som()      # Saída: Miau!
