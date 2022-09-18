import math
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "FormulaGeneral.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.Calcular.clicked.connect(self.formula)
    # Área de los Slots
    def formula(self):
        try:
            A = float(self.A.text())
            B = float(self.B.text())
            C = float(self.C.text())
            Praiz = (B*B)-4*A*C
            if Praiz<0:
                print("No hay solucion real")
            else:
                x1 = (-B+math.sqrt(Praiz))/(2*A)
                x2 = (-B-math.sqrt(Praiz))/(2*A)
                self.Resultado.setText("X1: " + str(x1))
                self.Resultado_2.setText("X2:" + str(x2))
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
