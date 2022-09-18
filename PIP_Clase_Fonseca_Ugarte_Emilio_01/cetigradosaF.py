import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "CtoF.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_CtoF.clicked.connect(self.CtoF)

        #self.btn_FtoC.clicked.connect(self.FtoC)

    def CtoF(self):
        Dato = float(self.Dato_txt.text())
        Dato = (Dato/5)*9
        Dato= Dato+32
        self.Resultado.setText(str(Dato)+"° Fahrenheit")

    def FtoC(self):
        Dato = float(self.Dato_txt.text())
        Dato = (Dato-32)/1.8
        self.Resultado.setText(str(Dato) + "° Celsius")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
