import sys 
from PyQt5.QtWidgets import *
from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro

app = QApplication(sys.argv)

TelaCarro = TelaCarro("Cadastro de Carro")
TelaCarro.show()

#TelaVeiculo = TelaVeiculo("Cadastro de Veículo")
#TelaVeiculo.show()

sys.exit(app.exec_())