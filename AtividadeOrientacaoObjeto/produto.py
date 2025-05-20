from abc import ABC, abstractmethod
from categoria import Categoria

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria: Categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}, Categoria: {self.categoria.nome}"

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte

    def setPotenciaDaFonte(self, potencia):
        self._potenciaDaFonte = potencia

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Potência da Fonte: {self._potenciaDaFonte}W"

    def cadastrar(self):
        return f"Desktop cadastrado: {self.getInformacoes()}"

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getTempoDeBateria(self):
        return self.__tempoDeBateria

    def setTempoDeBateria(self, tempo):
        self.__tempoDeBateria = tempo

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Tempo de Bateria: {self.__tempoDeBateria}h"

    def cadastrar(self):
        return f"Notebook cadastrado: {self.getInformacoes()}"