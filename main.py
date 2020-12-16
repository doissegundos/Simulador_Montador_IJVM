from tratamento_de_erros import Tratamento
from funções import Funcoes
from codigoIJVM import CodigoIJVM
from registradores import Registradores
from chamaRegistradores import ChamaRegistradores


import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QPushButton, QVBoxLayout, QTextEdit, QTextBrowser
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.uic import loadUiType

#Abre a janela grafica
Ui_MainWindow, QMainWindow = loadUiType('janela.ui')

#Classe da janela grafica
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" SOCORRO DEUS ")
        self.cont = 40
        self.posSP = 0
        self.i = 40
        self.linha = 0
        self.listaReg = []
        self.hh = "00000000"
        self.pilha = ["00", "00"]  # inicia a pilha, ela so pode armazenar dois valores
        self.variaveis = []
        self.codigoErro = ""
        self.chamaReg = ChamaRegistradores()
        self.registradores = Registradores()
        self.inicio()
        self.compilaButton.clicked.connect(self.compila)
        self.nextButton.clicked.connect(self.next)
        self.cont1 = 0

    def inicio(self):
        mar, mdr, pc, mbr, sp, lv, cpp, tos, opc, h = self.registradores.inicio()
        self.mar.setText(mar)
        self.mdr.setText(mdr)
        self.pc.setText(pc)
        self.mbr.setText(mbr)
        self.sp.setText(sp)
        self.lv.setText(lv)
        self.cpp.setText(cpp)
        self.tos.setText(tos)
        self.opc.setText(opc)
        self.h.setText(h)



    def compila(self):
        # Criando objetos com as classes
        function = Funcoes()
        tratamento = Tratamento()
        codigoHexadecimal = CodigoIJVM()
        registradores = Registradores()

        #ESSA PARTE VAI RECEBER O CODIGO EM .JAS E CONVERTER PARA IJVM
        codigo = self.jas.toPlainText() #Recebendo o codigo que foi escrito na interface grafica
        # Chamando os metodos para o tratamento do codigo
        codigoTratado = tratamento.converte_txt_lista(codigo)
        codigoTratado = tratamento.formatar_linha(codigoTratado)
        codigoTratado = tratamento.remove_linhas_nulas(codigoTratado)
        codigoTratado, self.codigoErro = codigoHexadecimal.converteCodigo(codigoTratado)
        self.ijvm.setText(codigoTratado)


    def next(self):
        if(self.cont1 == 0):
            self.mbr.setText(self.codigoErro[40]+self.codigoErro[41])
            self.cont1 = 1
        elif(self.cont<len(self.codigoErro)-1):
            self.cont, self.posSP, self.linha, self.hh, self.pilha, self.variaveis, self.listaReg = self.chamaReg.recebeCodigo(self.codigoErro, self.cont, self.posSP, self.linha, self.hh, self.pilha, self.variaveis)
            self.registradoresNext()

    def registradoresNext(self):
        mar, mdr, pc, mbr, sp, lv, cpp, tos, opc, h = self.listaReg
        self.mar.setText(mar)
        self.mdr.setText(mdr)
        self.pc.setText(pc)
        self.mbr.setText(mbr)
        self.sp.setText(sp)
        self.lv.setText(lv)
        self.cpp.setText(cpp)
        self.tos.setText(tos)
        self.opc.setText(opc)
        self.h.setText(h)




# '''
# Abrindo o codigo. A variavel texto vai receber todas as strings que o codigo contem.
# '''
# arq = open("t1.jas","r")
# codigo = arq.read()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

