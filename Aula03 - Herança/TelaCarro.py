import sys 
from PyQt5.QtWidgets import *
from TelaVeiculo import TelaVeiculo

class TelaCarro(TelaVeiculo):
    def __init__(self, titulo = "Tela Carro"):
        super().__init__(titulo)

    def definirLayout(self):
        super().definirLayout()
        self.lblPortas = QLabel("Quantidade Portas")
        self.txtPortas = QLineEdit(self)
        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)
        