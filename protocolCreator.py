import sys
import os
from collections import OrderedDict

try:
    from util_lib.utilityPrint import printRed
    import settings as st
    from ProtocolCreatorUI import Ui_ProtocolCreator
    from PyQt5 import QtCore, QtGui, QtWidgets
    from util_lib.utilityYml import createYmlFile
    from dialogs.warnings import warnings, showDialog
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

class ProtocolCreator(QtWidgets.QMainWindow, Ui_ProtocolCreator):
    pathPToMain = QtCore.pyqtSignal(str)
    infoPToMain = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_pathProtocol.setText(st._protocolDir)

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

#  region Method button on click
    def btn_addToInputAlphabet_on_click(self):
        item = QtWidgets.QListWidgetItem(self.textBox_inputAlphabet.text())
        self.listWidget_inputAlphabet.addItem(item)
        self.comboBox_firstElemOfInputFunc.addItem(self.textBox_inputAlphabet.text())

    def btn_removeFromInputAlphabet_on_click(self):
        self.listWidget_inputAlphabet.takeItem(self.listWidget_inputAlphabet.currentRow())

    def btn_clearInputAlphabet_on_click(self):
        self.textBox_inputAlphabet.clear()
        self.listWidget_inputAlphabet.clear()

    def btn_addToStatesAlphabet_on_click(self):
        state = self.textBox_stateAlphabet.text()
        item = QtWidgets.QListWidgetItem(state)
        self.listWidget_stateAlphabet.addItem(item)
        self.comboBox_secondElemOfInputFunc.addItem(state)
        self.comboBox_firstElemOfStatesFunc.addItem(state)
        self.comboBox_secondElemOfStatesFunc.addItem(state)
        self.comboBox_thirdElemOfStatesFunc.addItem(state)
        self.comboBox_fourthElemOfStatesFunc.addItem(state)
        self.comboBox_firstElemOfOutpuFunc.addItem(state)

    def btn_removeFromStatesAlphabet_on_click(self):
        self.listWidget_stateAlphabet.takeItem(self.listWidget_stateAlphabet.currentRow())

    def btn_clearStatesAlphabet_on_click(self):
        self.textBox_stateAlphabet.clear()
        self.listWidget_stateAlphabet.clear()

    def btn_addToOutputAlphabet_on_click(self):
        output = self.textBox_outputAlphabet.text()
        item = QtWidgets.QListWidgetItem(output)
        self.listWidget_outputAlphabet.addItem(item)
        self.comboBox_secondElemOfOutpuFunc.addItem(output)

    def btn_removeFromOutputAlphabet_on_click(self):
        self.listWidget_outputAlphabet.takeItem(self.listWidget_outputAlphabet.currentRow())

    def btn_clearOutputAlphabet_on_click(self):
        self.textBox_outputAlphabet.clear()
        self.listWidget_outputAlphabet.clear()

    def btn_addInputFunction_on_click(self):
        firstElem = self.comboBox_firstElemOfInputFunc.currentText()
        secondElem = self.comboBox_secondElemOfInputFunc.currentText()
        item = QtWidgets.QListWidgetItem("({})->({})".format(firstElem, secondElem))
        self.listWidget_inputFunction.addItem(item)

    def btn_removeFromInputFunction_on_click(self):
        self.listWidget_inputFunction.takeItem(self.listWidget_inputFunction.currentRow())

    def btn_clearInputFunction_on_click(self):
        self.comboBox_firstElemOfInputFunc.clear()
        self.comboBox_secondElemOfInputFunc.clear()
        self.listWidget_inputFunction.clear()

    def btn_addToStatesFunction_on_click(self):
        firstElem = self.comboBox_firstElemOfStatesFunc.currentText()
        secondElem = self.comboBox_secondElemOfStatesFunc.currentText()
        item = QtWidgets.QListWidgetItem("({})->({})".format(firstElem, secondElem))
        self.listWidget_statesFunction.addItem(item)

    def btn_removeOfStatesFunction_on_click(self):
        self.listWidget_statesFunction.takeItem(self.listWidget_statesFunction.currentRow())

    def btn_clearStatesFunction_on_click(self):
        self.comboBox_firstElemOfStatesFunc.clear()
        self.comboBox_secondElemOfStatesFunc.clear()
        self.listWidget_statesFunction.clear()

    def btn_addToOutputFunction_on_click(self):
        firstElem = self.comboBox_firstElemOfOutpuFunc.currentText()
        secondElem = self.comboBox_secondElemOfOutpuFunc.currentText()
        item = QtWidgets.QListWidgetItem("({})->({})".format(firstElem, secondElem))
        self.listWidget_outputFunction.addItem(item)

    def btn_removeFromOutputFunction_on_click(self):
        self.listWidget_outputFunction.takeItem(self.listWidget_outputFunction.currentRow())

    def btn_clearOutputFunction_on_click(self):
        self.comboBox_firstElemOfOutpuFunc.clear()
        self.comboBox_secondElemOfOutpuFunc.clear()
        self.listWidget_outputFunction.clear()

    def btn_browseProtocolDir_on_click(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open', st._appDir, QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit_pathProtocol.setText(directory)

    def btn_clearProtocol_on_click(self):
        self.btn_clearInputAlphabet_on_click()
        self.btn_clearStatesAlphabet_on_click()
        self.btn_clearOutputAlphabet_on_click()
        self.btn_clearInputFunction_on_click()
        self.btn_clearStatesFunction_on_click()
        self.btn_clearOutputFunction_on_click()
        self.lineEdit_protocolName.clear()
        self.lineEdit_pathProtocol.clear()

    def btn_saveProtocol_on_click(self):
        protocolName = self.lineEdit_protocolName.text()
        protocolPath = self.lineEdit_pathProtocol.text()

        if protocolName.strip() == "":
            showDialog("emptyPName")
            return
        elif '.' in protocolName:
            showDialog("noExt")
            return

        nameGroup = ("name", protocolName)
        if self.radioButton_liderElection.isChecked():
            typeGroup = self.createTuple("protocolType", "Leader Election")
        else:
            typeGroup = self.createTuple("protocolType", "Majority")

        inputGroup = self.createTuple("input", self.listWidget_inputAlphabet)
        statesGroup = self.createTuple("states", self.listWidget_stateAlphabet)
        outputGroup = self.createTuple("output", self.listWidget_outputAlphabet)
        inputFunction = self.createTuple("inputFunction", self.listWidget_inputFunction)
        statesFunction = self.createTuple("statesFunction", self.listWidget_statesFunction)
        outputFunction = self.createTuple("outputFunction", self.listWidget_outputFunction)
        unOrderedTuple = [nameGroup, typeGroup, inputGroup, statesGroup, outputGroup, inputFunction, statesFunction, outputFunction]

        for tup in unOrderedTuple:
            if [] in tup:
                self.showDialog("LW_{}".format(tup[0]))
                return

        ppYml = OrderedDict(unOrderedTuple)

        createYmlFile(protocolName, ppYml, protocolPath)
        protocolFile = "\\".join([protocolPath, protocolName+".yml"])
        self.pathPToMain.emit(protocolFile)
        with open(protocolFile, 'r') as pFile:
            self.infoPToMain.emit("".join(pFile.readlines()))
        self.close()
# endregion

    def createTuple(self, key, value):
        """
        Create Tuple later necessary for create ordered dict.

        @param key   : Key
        @param value : Value
        @return      : Tuple
        """
        if isinstance(value, QtWidgets.QListWidget):
            return (key, self.getAllListWidgetItems(value))
        else:
            return (key, value)

    def getAllListWidgetItems(self, listWidget):
        """
        Get all items from ListWidget.

        @return : List of items
        """
        return [listWidget.item(i).text() for i in range(listWidget.count())]

if __name__ == "__main__":
    pass
