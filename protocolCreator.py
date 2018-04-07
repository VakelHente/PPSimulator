import sys

try:
    from util_lib.utilityPrint import printRed, disableEnablePrint
    import settings as st
    from ProtocolCreatorUI import Ui_ProtocolCreator
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

class ProtocolCreator(QtWidgets.QMainWindow):

    def __init__(self, window):
        super().__init__()
        self.ui = Ui_ProtocolCreator()
        self.ui.setupUi(window)

        # Protocol's sets group
        self.ui.btn_addToInputAlphabet.clicked.connect(self.btn_addToInputAlphabet_on_click)
        self.ui.btn_removeFromInputAlphabet.clicked.connect(self.btn_removeFromInputAlphabet_on_click)
        self.ui.btn_clearInputAlphabet.clicked.connect(self.btn_clearInputAlphabet_on_click)
        self.ui.btn_addToStatesAlphabet.clicked.connect(self.btn_addToStatesAlphabet_on_click)
        self.ui.btn_removeFromStatesAlphabet.clicked.connect(self.btn_removeFromStatesAlphabet_on_click)
        self.ui.btn_clearStatesAlphabet.clicked.connect(self.btn_clearStatesAlphabet_on_click)
        self.ui.btn_addToOutputAlphabet.clicked.connect(self.btn_addToOutputAlphabet_on_click)
        self.ui.btn_removeFromOutputAlphabet.clicked.connect(self.btn_removeFromOutputAlphabet_on_click)
        self.ui.btn_clearOutputAlphabet.clicked.connect(self.btn_clearOutputAlphabet_on_click)

        # Protocol's Function group
        self.ui.btn_addInputFunction.clicked.connect(self.btn_addInputFunction_on_click)
        self.ui.btn_clearInputFunction.clicked.connect(self.btn_clearInputFunction_on_click)
        self.ui.btn_addToStatesFunction.clicked.connect(self.btn_removeFromInputAlphabet_on_click)
        self.ui.btn_addToStatesFunction.clicked.connect(self.btn_addToStatesFunction_on_click)
        self.ui.btn_removeOfStatesFunction.clicked.connect(self.btn_removeOfStatesFunction_on_click)
        self.ui.btn_clearStatesFunction.clicked.connect(self.btn_clearStatesFunction_on_click)
        self.ui.btn_addToOutputFunction.clicked.connect(self.btn_addToOutputFunction_on_click)
        self.ui.btn_removeFromOutputFunction.clicked.connect(self.btn_removeFromOutputFunction_on_click)
        self.ui.btn_clearOutputFunction.clicked.connect(self.btn_clearOutputFunction_on_click)


        self.ui.btn_BrowseProtocolDir.clicked.connect(self.btn_BrowseProtocolDir_on_click)
        self.ui.btn_clearProtocol.clicked.connect(self.btn_clearProtocol_on_click)
        self.ui.btn_SaveProtocol.clicked.connect(self.btn_SaveProtocol_on_click)

    @QtCore.pyqtSlot()
    def btn_addToInputAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_removeFromInputAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_clearInputAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_addToStatesAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_removeFromStatesAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_clearStatesAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_addToOutputAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_removeFromOutputAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_clearOutputAlphabet_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_addInputFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_removeFromInputFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_clearInputFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_addToStatesFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_removeOfStatesFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_clearStatesFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_addToOutputFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_removeFromOutputFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_clearOutputFunction_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_BrowseProtocolDir_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_clearProtocol_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btn_SaveProtocol_on_click(self):
        pass



if __name__ == "__main__":
    pass
