import sys 
from PyQt5.QtWidgets import *
from Veiculo import Veiculo

class TelaVeiculo(QMainWindow):

    def __init__(self, titulo = "Tela Veículo"):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 300, 150)
        self.layout = QVBoxLayout()

        self.definirLayout()
        #botão
        self.btnSalvar = QPushButton("Salvar", self) 
        self.btnSalvar.clicked.connect(self.salvar)
        self.layout.addWidget(self.btnSalvar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container) 
    
    def definirLayout(self):
        self.lblModelo = QLabel("Modelo: ")
        self.txtModelo = QLineEdit(self)
        self.lblAno = QLabel("Ano: ")
        self.txtAno = QLineEdit(self)

        self.layout.addWidget(self.lblModelo)
        self.layout.addWidget(self.txtModelo)
        self.layout.addWidget(self.lblAno)
        self.layout.addWidget(self.txtAno)
    

    def salvar(self):
        modelo = self.txtModelo.text()
        ano = self.txtAno.text()
        if(ano != ""):
            ano = int(ano)
        veiculo = Veiculo(modelo, ano)
        QMessageBox.information(self, "Veículo salvo", str(veiculo) )
