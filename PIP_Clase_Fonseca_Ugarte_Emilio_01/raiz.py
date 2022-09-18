import math
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Votar_Mx.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.raiz)

    def raiz(self):
        Num = float(self.ano_txt.text())
        Num=math.sqrt(Num)
        self.Resultado.setText("La raiz cuadrada es "+str(Num))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())