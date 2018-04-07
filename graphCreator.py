import sys

try:
    from util_lib.utilityPrint import printRed, disableEnablePrint
    import settings as st
    from GraphCreatorUI import Ui_GraphCreator
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

class GraphCreator(QtWidgets.QMainWindow):

    def __init__(self, window):
        super().__init__()
        self.ui = Ui_GraphCreator()
        self.ui.setupUi(window)

if __name__ == "__main__":
    pass
