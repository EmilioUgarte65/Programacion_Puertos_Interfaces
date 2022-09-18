import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Factorial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.Calcular.clicked.connect(self.fac)
    # Área de los Slots
    def fac(self):

        try:
            n=int(self.Num.text())
            print("valor de n : ",n)

            resultado = 1

            for i in range(2,n+1,1):
                print("Valor de i: ", i)
                resultado = resultado * i

            print("Factorial: ", resultado)
            self.Resultado.setText(str(resultado))
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
