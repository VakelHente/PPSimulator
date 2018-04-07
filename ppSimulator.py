import sys
import platform
import argparse

try:
    from util_lib.utilityPrint import printRed
    from util_lib.utilityPrint import disableEnablePrint
    from colorama import init
    import settings as st
    from ppSimulatorUI import Ui_MainWindow
    from graphCreator import GraphCreator
    from protocolCreator import ProtocolCreator
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

if platform.system() == "Windows":
    init()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create object of other windows
        self.graphCreator = QtWidgets.QMainWindow()
        self.protocolCreator = QtWidgets.QMainWindow()

        # Assign method on click to push button
        self.ui.btnGraphCreate_Single.clicked.connect(self.btnGraphCreate_Single_on_click)
        self.ui.btnGraphFromFile_Single.clicked.connect(self.btnGraphFromFile_Single_on_click)
        self.ui.btnProtocolCreate.clicked.connect(self.btnProtocolCreate_on_click)
        self.ui.btnProtocolFromFile.clicked.connect(self.btnProtocolFromFile_on_click)
        self.ui.btnBrowse_Single.clicked.connect(self.btnBrowse_Single_on_click)
        self.ui.btnClear_Single.clicked.connect(self.btnClear_Single_on_click)
        self.ui.btnStart_Single.clicked.connect(self.btnStart_Single_on_click)
        self.ui.btnYAMLCreate_Multi.clicked.connect(self.btnYAMLCreate_Multi_on_click)
        self.ui.btnYAMLFromFile_Multi.clicked.connect(self.btnYAMLFromFile_Multi_on_click)
        self.ui.btnAdd_Multi.clicked.connect(self.btnAdd_Multi_on_click)
        self.ui.btnRemove_Multi.clicked.connect(self.btnRemove_Multi_on_click)
        self.ui.btnClear_Multi.clicked.connect(self.btnClear_Multi_on_click)
        self.ui.btnSave_Multi.clicked.connect(self.btnSave_Multi_on_click)
        self.ui.btnBrowse_Multi.clicked.connect(self.btnBrowse_Multi_on_click)
        self.ui.btnStart_Multi.clicked.connect(self.btnStart_Multi_on_click)

    @QtCore.pyqtSlot()
    def btnGraphCreate_Single_on_click(self):
        GraphCreator(self.graphCreator)
        self.graphCreator.setWindowModality(QtCore.Qt.ApplicationModal)
        self.graphCreator.show()

    @QtCore.pyqtSlot()
    def btnGraphFromFile_Single_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnProtocolCreate_on_click(self):
        ProtocolCreator(self.protocolCreator)
        self.protocolCreator.setWindowModality(QtCore.Qt.ApplicationModal)
        self.protocolCreator.show()

    @QtCore.pyqtSlot()
    def btnProtocolFromFile_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnBrowse_Single_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnClear_Single_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnStart_Single_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnYAMLCreate_Multi_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnYAMLFromFile_Multi_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnAdd_Multi_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnRemove_Multi_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnClear_Multi_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnSave_Multi_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnBrowse_Multi_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnStart_Multi_on_click(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    disableEnablePrint(False)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()