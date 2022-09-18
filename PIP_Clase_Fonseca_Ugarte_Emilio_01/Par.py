import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Num_Par.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.Num_Par)

    def Num_Par(self):
        anio = int(self.ano_txt.text())
        res = anio/2
        res1 = int(res)
        bis = ""
        if res == res1:
            bis = ("Su numero "+str(anio)+" es Par")
        else:
            bis = ("Su numero " + str(anio) + " No es par")
        self.Resultado.setText(bis)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())