import sys
import platform
import os
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
    from dialogs.warnings import warnings, showDialog
    from util_lib.utilityYml import getYmlDict
    from util_lib.utilityDict import dictToObj
    from protocol import Protocol
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

if platform.system() == "Windows":
    init()

dir_path = os.path.dirname(os.path.realpath(__file__))

class PpSimulator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PpSimulator, self).__init__()
        self.setupUi(self)

        # Create object of other windows
        self.graphCreator = QtWidgets.QMainWindow()
        self.protocolCreator = QtWidgets.QMainWindow()

        # Assign method on click to push button
        self.btnGraphCreate_Single.clicked.connect(self.btnGraphCreate_Single_on_click)
        self.btnGraphFromFile_Single.clicked.connect(self.btnGraphFromFile_Single_on_click)
        self.btnProtocolCreate.clicked.connect(self.btnProtocolCreate_on_click)
        self.btnProtocolFromFile.clicked.connect(self.btnProtocolFromFile_on_click)
        self.btnBrowse_Single.clicked.connect(self.btnBrowse_Single_on_click)
        self.btnClear_Single.clicked.connect(self.btnClear_Single_on_click)
        self.btnStart_Single.clicked.connect(self.btnStart_Single_on_click)
        self.btnYAMLCreate_Multi.clicked.connect(self.btnYAMLCreate_Multi_on_click)
        self.btnYAMLFromFile_Multi.clicked.connect(self.btnYAMLFromFile_Multi_on_click)
        self.btnAdd_Multi.clicked.connect(self.btnAdd_Multi_on_click)
        self.btnRemove_Multi.clicked.connect(self.btnRemove_Multi_on_click)
        self.btnClear_Multi.clicked.connect(self.btnClear_Multi_on_click)
        self.btnSave_Multi.clicked.connect(self.btnSave_Multi_on_click)
        self.btnBrowse_Multi.clicked.connect(self.btnBrowse_Multi_on_click)
        self.btnStart_Multi.clicked.connect(self.btnStart_Multi_on_click)

#  region Method button on click
    @QtCore.pyqtSlot()
    def btnGraphCreate_Single_on_click(self):
        pathToProtocol = self.txtPathProtocol.text()
        if pathToProtocol.strip() == "":
            showDialog("NoProtocol")
            return
        objProtocol = dictToObj(Protocol, getYmlDict(pathToProtocol))
        self.GC = GraphCreator(objProtocol.input)
        self.GC.setWindowModality(QtCore.Qt.ApplicationModal)
        self.GC.show()
        self.conTxtPathG(self.GC)
        self.conTxtInfoG(self.GC)

    @QtCore.pyqtSlot()
    def btnGraphFromFile_Single_on_click(self):
        pathToProtocol = self.txtPathProtocol.text()
        if pathToProtocol.strip() == "":
            showDialog("NoProtocol")
            return
        objProtocol = dictToObj(Protocol, getYmlDict(pathToProtocol))

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', st._graphDir, '*.yml')

    @QtCore.pyqtSlot()
    def btnProtocolCreate_on_click(self):
        self.PC = ProtocolCreator()
        self.PC.setWindowModality(QtCore.Qt.ApplicationModal)
        self.PC.show()
        self.conTxtInfoP(self.PC)
        self.conTxtPathP(self.PC)

    @QtCore.pyqtSlot()
    def btnProtocolFromFile_on_click(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', st._protocolDir, '*.yml')
        self.txtPathProtocol.setText(fileName)
        with open(fileName, 'r') as pFile:
            self.txtInfoProtocol.setText("".join(pFile.readlines()))

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
# endregion

    @QtCore.pyqtSlot(str)
    def txtPathProtocol_setText(self, string):
        self.txtPathProtocol.setText(string)

    @QtCore.pyqtSlot(str)
    def txtInfoProtocol_setText(self, string):
        self.txtInfoProtocol.setText(string)

    @QtCore.pyqtSlot(str)
    def txtPathGraph_setText(self, string):
        self.txtPathGraph_Single.setText(string)

    @QtCore.pyqtSlot(str)
    def txtInfoGraph_setText(self, string):
        self.txtInfoGraph_Single.setText(string)

    def conTxtInfoP(self, protocolWindow):
        """


        @param lineEditObj  :
        @return             : None
        """
        protocolWindow.infoPToMain.connect(self.txtInfoProtocol_setText)

    def conTxtPathP(self, protocolWindow):
        """


        @param lineEditObj  :
        @return             : None
        """
        protocolWindow.pathPToMain.connect(self.txtPathProtocol_setText)

    def conTxtPathG(self, graphWindow):
        """


        @param graphWindow  :
        @return             : None
        """
        graphWindow.pathGToMain.connect(self.txtPathGraph_setText)

    def conTxtInfoG(self, graphWindow):
        """


        @param graphWindow  :
        @return             : None
        """
        graphWindow.infoGToMain.connect(self.txtInfoGraph_setText)

    def validateProtocol(self, pathFile):
        """
        Validate protocol file in terms of attributes.

        @param pathFile : Path to protocol file
        @return         : True if protocol is correct False otherwise
        """
        pass

    def validateGraph(self, pathFile):
        """
        Validate graph file in terms of attributes.

        :param pathFile : Path to graph file
        :return         : True if graph is correct False otherwise
        """
        pass

def main():
    st.init()
    app = QtWidgets.QApplication(sys.argv)
    window = PpSimulator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="POPULATION PROTOCOL SIMULATOR")
    parser._action_groups.pop()
    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--debug', dest='feature', action='store_true')
    parser.set_defaults(feature=False)

    disableEnablePrint(parser.parse_args().feature)
    main()