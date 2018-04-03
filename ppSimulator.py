import sys

try:
    import settings as st
    from MainWindowUI import Ui_MainWindow
    from util_lib.util import printRed
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # btnGraphCreate_Singel
        self.ui.btnGraphCreate_Single.clicked.connect(self.on_click)

    @QtCore.pyqtSlot()
    def on_click(self):
        print("Test write")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()