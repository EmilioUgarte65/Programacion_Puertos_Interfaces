import math
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Punto_A_B.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.Calcular.clicked.connect(self.Distancia)
    # Área de los Slots
    def Distancia(self):
        A_X=float(self.A_x.text())
        A_Y=float(self.A_y.text())
        B_X=float(self.B_x.text())
        B_Y=float(self.B_y.text())
        parte1=(A_X-B_X)**2
        parte2=(A_Y-B_Y)**2
        parte3=parte1+parte2
        distancia=math.sqrt(parte3)
        self.Resultado.setText("La distancia entre los puntos es:"+str(distancia))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())