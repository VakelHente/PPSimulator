import sys
import os

try:
    from util_lib.utilityPrint import printRed
    from util_lib.utilityPrint import disableEnablePrint
    import settings as st
    from ProtocolCreatorUI import Ui_ProtocolCreator
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

dir_path = os.path.dirname(os.path.realpath(__file__))

class ProtocolCreator(QtWidgets.QMainWindow, Ui_ProtocolCreator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Protocol's sets group
        self.btn_addToInputAlphabet.clicked.connect(self.btn_addToInputAlphabet_on_click)
        self.btn_removeFromInputAlphabet.clicked.connect(self.btn_removeFromInputAlphabet_on_click)
        self.btn_clearInputAlphabet.clicked.connect(self.btn_clearInputAlphabet_on_click)
        self.btn_addToStatesAlphabet.clicked.connect(self.btn_addToStatesAlphabet_on_click)
        self.btn_removeFromStatesAlphabet.clicked.connect(self.btn_removeFromStatesAlphabet_on_click)
        self.btn_clearStatesAlphabet.clicked.connect(self.btn_clearStatesAlphabet_on_click)
        self.btn_addToOutputAlphabet.clicked.connect(self.btn_addToOutputAlphabet_on_click)
        self.btn_removeFromOutputAlphabet.clicked.connect(self.btn_removeFromOutputAlphabet_on_click)
        self.btn_clearOutputAlphabet.clicked.connect(self.btn_clearOutputAlphabet_on_click)

        # Protocol's Function group
        self.btn_addInputFunction.clicked.connect(self.btn_addInputFunction_on_click)
        self.btn_clearInputFunction.clicked.connect(self.btn_clearInputFunction_on_click)
        self.btn_addToStatesFunction.clicked.connect(self.btn_removeFromInputAlphabet_on_click)
        self.btn_addToStatesFunction.clicked.connect(self.btn_addToStatesFunction_on_click)
        self.btn_removeOfStatesFunction.clicked.connect(self.btn_removeOfStatesFunction_on_click)
        self.btn_clearStatesFunction.clicked.connect(self.btn_clearStatesFunction_on_click)
        self.btn_addToOutputFunction.clicked.connect(self.btn_addToOutputFunction_on_click)
        self.btn_removeFromOutputFunction.clicked.connect(self.btn_removeFromOutputFunction_on_click)
        self.btn_clearOutputFunction.clicked.connect(self.btn_clearOutputFunction_on_click)


        self.btn_browseProtocolDir.clicked.connect(self.btn_browseProtocolDir_on_click)
        self.btn_clearProtocol.clicked.connect(self.btn_clearProtocol_on_click)
        self.btn_saveProtocol.clicked.connect(self.btn_saveProtocol_on_click)


    @QtCore.pyqtSlot()
    def btn_addToInputAlphabet_on_click(self):
        item = QtWidgets.QListWidgetItem(self.textBox_inputAlphabet.text())
        self.listWidget_inputAlphabet.addItem(item)
        self.comboBox_firstElemOfInputFunc.addItem(self.textBox_inputAlphabet.text())
        self.comboBox_secondElemOfInputFunc.addItem(self.textBox_inputAlphabet.text())

    @QtCore.pyqtSlot()
    def btn_removeFromInputAlphabet_on_click(self):
        self.listWidget_inputAlphabet.takeItem(self.listWidget_inputAlphabet.currentRow())

    @QtCore.pyqtSlot()
    def btn_clearInputAlphabet_on_click(self):
        self.textBox_inputAlphabet.clear()
        self.listWidget_inputAlphabet.clear()

    @QtCore.pyqtSlot()
    def btn_addToStatesAlphabet_on_click(self):
        item = QtWidgets.QListWidgetItem(self.textBox_stateAlphabet.text())
        self.listWidget_stateAlphabet.addItem(item)
        self.comboBox_firstElemOfStatesFunc.addItem(self.textBox_stateAlphabet.text())
        self.comboBox_secondElemOfStatesFunc.addItem(self.textBox_stateAlphabet.text())

    @QtCore.pyqtSlot()
    def btn_removeFromStatesAlphabet_on_click(self):
        self.listWidget_stateAlphabet.takeItem(self.listWidget_stateAlphabet.currentRow())

    @QtCore.pyqtSlot()
    def btn_clearStatesAlphabet_on_click(self):
        self.textBox_stateAlphabet.clear()
        self.listWidget_stateAlphabet.clear()

    @QtCore.pyqtSlot()
    def btn_addToOutputAlphabet_on_click(self):
        item = QtWidgets.QListWidgetItem(self.textBox_outputAlphabet.text())
        self.listWidget_outputAlphabet.addItem(item)
        self.comboBox_firstElemOfOutpuFunc.addItem(self.textBox_outputAlphabet.text())
        self.comboBox_secondElemOfOutpuFunc.addItem(self.textBox_outputAlphabet.text())

    @QtCore.pyqtSlot()
    def btn_removeFromOutputAlphabet_on_click(self):
        self.listWidget_outputAlphabet.takeItem(self.listWidget_outputAlphabet.currentRow())

    @QtCore.pyqtSlot()
    def btn_clearOutputAlphabet_on_click(self):
        self.textBox_outputAlphabet.clear()
        self.listWidget_outputAlphabet.clear()

    @QtCore.pyqtSlot()
    def btn_addInputFunction_on_click(self):
        firstElem = self.comboBox_firstElemOfInputFunc.currentText()
        secondElem = self.comboBox_secondElemOfInputFunc.currentText()
        item = QtWidgets.QListWidgetItem("({})->({})".format(firstElem, secondElem))
        self.listWidget_inputFunction.addItem(item)

    @QtCore.pyqtSlot()
    def btn_removeFromInputFunction_on_click(self):
        self.listWidget_inputFunction.takeItem(self.listWidget_inputFunction.currentRow())

    @QtCore.pyqtSlot()
    def btn_clearInputFunction_on_click(self):
        self.comboBox_firstElemOfInputFunc.clear()
        self.comboBox_secondElemOfInputFunc.clear()
        self.listWidget_inputFunction.clear()

    @QtCore.pyqtSlot()
    def btn_addToStatesFunction_on_click(self):
        firstElem = self.comboBox_firstElemOfStatesFunc.currentText()
        secondElem = self.comboBox_secondElemOfStatesFunc.currentText()
        item = QtWidgets.QListWidgetItem("({})->({})".format(firstElem, secondElem))
        self.listWidget_statesFunction.addItem(item)

    @QtCore.pyqtSlot()
    def btn_removeOfStatesFunction_on_click(self):
        self.listWidget_statesFunction.takeItem(self.listWidget_statesFunction.currentRow())

    @QtCore.pyqtSlot()
    def btn_clearStatesFunction_on_click(self):
        self.comboBox_firstElemOfStatesFunc.clear()
        self.comboBox_secondElemOfStatesFunc.clear()
        self.listWidget_statesFunction.clear()

    @QtCore.pyqtSlot()
    def btn_addToOutputFunction_on_click(self):
        firstElem = self.comboBox_firstElemOfOutpuFunc.currentText()
        secondElem = self.comboBox_secondElemOfOutpuFunc.currentText()
        item = QtWidgets.QListWidgetItem("({})->({})".format(firstElem, secondElem))
        self.listWidget_outputFunction.addItem(item)

    @QtCore.pyqtSlot()
    def btn_removeFromOutputFunction_on_click(self):
        self.listWidget_outputFunction.takeItem(self.listWidget_outputFunction.currentRow())

    @QtCore.pyqtSlot()
    def btn_clearOutputFunction_on_click(self):
        self.comboBox_firstElemOfOutpuFunc.clear()
        self.comboBox_secondElemOfOutpuFunc.clear()
        self.listWidget_outputFunction.clear()

    @QtCore.pyqtSlot()
    def btn_browseProtocolDir_on_click(self):
        directory= QtWidgets.QFileDialog.getExistingDirectory(self, 'Open', dir_path, QtWidgets.QFileDialog.ShowDirsOnly)
        print(directory)

    @QtCore.pyqtSlot()
    def btn_clearProtocol_on_click(self):
        self.btn_clearInputAlphabet_on_click()
        self.btn_clearStatesAlphabet_on_click()
        self.btn_clearOutputAlphabet_on_click()
        self.btn_clearInputFunction_on_click()
        self.btn_clearStatesFunction_on_click()
        self.btn_clearOutputFunction_on_click()
        self.lineEdit_protocolName.clear()
        self.lineEdit_pathProtocol.clear()

    @QtCore.pyqtSlot()
    def btn_saveProtocol_on_click(self):
        if self.lineEdit_protocolName.text().strip() == "":
            pass

        if self.lineEdit_pathProtocol.text().strip == "":
            pass



if __name__ == "__main__":
    pass
