import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Potencia.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.Calcular.clicked.connect(self.Pot)
    # Área de los Slots
    def Pot(self):
        try:
            num = int(self.Num.text())
            pot = int(self.Potencia.text())
            x= num
            for z in range(1,pot):
                num =num*x


            self.Resultado.setText(str(num))
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())