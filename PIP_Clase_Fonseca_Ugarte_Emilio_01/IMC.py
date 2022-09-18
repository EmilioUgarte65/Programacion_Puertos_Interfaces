import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "IndiceMC.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.IndiceMCs)

    def IndiceMCs(self):
        peso = float(self.peso_txt.text())
        altura = float(self.Altura_txt.text())
        altura = altura ** 2
        imc = peso / altura
        self.Resultado.setText("Su indice de masa corporal es: " + str(imc))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
