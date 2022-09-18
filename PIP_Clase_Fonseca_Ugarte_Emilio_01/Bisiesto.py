import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Bisiesto.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.Bisiesto)

    def Bisiesto(self):
        anio = int(self.ano_txt.text())
        res = anio/4
        res1 = int(res)
        bis = ""
        if res == res1:
            bis = ("El año "+str(anio)+" es bisiesto")
        else:
            bis = ("El año " + str(anio) + " No bisiesto")
        self.Resultado.setText(bis)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
