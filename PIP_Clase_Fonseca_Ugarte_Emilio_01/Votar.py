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
        self.btn_calcular.clicked.connect(self.Vot)

    def Vot(self):
        edad = int(self.ano_txt.text())
        Respuesta=""
        if edad<18:
            Respuesta="Usted no puede votar"
        else:
            Respuesta="Usted puede votar"
        self.Resultado.setText(Respuesta)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())