import sys

try:
    from util_lib.utilityPrint import printRed, disableEnablePrint
    import settings as st
    from GraphCreatorUI import Ui_GraphCreator
    from PyQt5 import QtCore, QtGui, QtWidgets
    from dialogs.warnings import warnings, showDialog
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

class GraphCreator(QtWidgets.QMainWindow, Ui_GraphCreator):

    def __init__(self, listItems=None):
        super().__init__()
        self.setupUi(self)
        self.listItems = listItems
        self.cmbBxInputAlphabet.addItems(self.listItems)
        self.checkBxIfRandom.stateChanged.connect(self.randomGraph)
        self.checkBxIfRandom.setChecked(True)

#  region Method button on click
    def btnAdd_click(self):

        aa = self.cmbBxInputAlphabet.currentText()
        bb = self.txtBxNumberOfSymbol.text()
        kk = QtWidgets.QTreeWidgetItem(aa, bb)
        self.listNode.addTopLevelItems(kk)
        pass

    def btnRemove_click(self):
        self.listNode.takeItem(self.listNode.currentRow())

    def btnOk_click(self):
        if self.checkBxIfRandom.isChecked():
            if int(self.txtBxNumberOfNodes.text()) > 1:
                #TODO: create random graph
                pass
            else:
                showDialog("LowNBNodes")
                return
        else:
            #TODO: create normal graph
            pass

    def btnClear_click(self):
        self.listNode.clear()
        self.txtBxNumberOfSymbol.clear()
        self.txtBxNumberOfNodes.clear()
# endregion

    def randomGraph(self):
        if self.checkBxIfRandom.isChecked():
            self.groupBxDefineGraph.setDisabled(True)
        else:
            self.groupBxDefineGraph.setDisabled(False)

if __name__ == "__main__":
    pass
