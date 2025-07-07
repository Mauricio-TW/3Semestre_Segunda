class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late: Au au!")

class Gato(Animal):
    def falar(self):
        print("O gato mia: Miau!")

# Lista de animais
animais = [Cachorro(), Gato(), Animal()]

# Usando polimorfismo
for animal in animais:
    animal.falar()
