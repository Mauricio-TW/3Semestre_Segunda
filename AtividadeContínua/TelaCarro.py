import sys 
from PyQt5.QtWidgets import *

from TelaVeiculo import TelaVeiculo
from Carro import Carro

class TelaCarro (TelaVeiculo):
    def __init__(self, titulo="Tela Carro"):
        super().__init__(titulo)
        self.setGeometry(450, 150, 300, 300)

    def definirLayout(self): 
        self.lblPortas = QLabel("Quantidade de portas: ")
        self.txtPortas = QLineEdit(self)
        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)

    def salvar(self):
        modelo = self.txtModelo.text()
        ano = self.txtAno.text()
        if(ano != ""):
            ano = int(ano)
        portas = self.txtPortas.text()
        if portas != "":
            portas = int( portas )
        carro = Carro(modelo, ano, portas)
        QMessageBox.information(self, "Carro salvo", str(carro) )
