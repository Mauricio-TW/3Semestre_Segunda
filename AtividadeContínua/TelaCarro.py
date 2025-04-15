import sys 
from PyQt5.QtWidgets import *

from TelaVeiculo import TelaVeiculo
from Carro import Carro

class TelaCarro(TelaVeiculo):
    def __init__(self, titulo = "Tela Carro", categorias = [], telaCarro = None ):
        self.listaCategorias = categorias
        self.telaCategorias = telaCat
        super().__init__(titulo)
        self.setGeometry(450, 150, 300, 300)

    def definirLayout(self):
        super().definirLayout()
        self.lblPortas = QLabel("Quantidade Portas")
        self.txtPortas = QLineEdit(self)
        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)
        
        self.lblCategoria = QLabel("Categoria")
        self.layout.addWidget(self.lblCategoria)

        self.cmbCategoria = QComboBox(self)
        self.carregarCategorias()
        self.Layout.addWidget(self.cmbCategoria)
        
    def carregarCategorias(self):
        self.cmbCategoria.addItem("Selecione...", None)
        for cat in self.lblCategorias:
            self.cmbCategoria.addItem(cat.nome, cat)
        

    def __salvar(self):
        nome = self.txtNome.text()
        if(nome != ""):
            cat = Categoria (nome)
            self.listaCategorias.append(cat)     
            self.telaCarro.carregarCategorias()     
        QMessageBox.information(self, "Categoria Salva", str(cat))