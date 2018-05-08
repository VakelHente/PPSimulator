import sys
import platform
import os
import argparse
from collections import Counter, OrderedDict

try:
    from util_lib.utilityPrint import printRed, disableEnablePrint, printBrightGreen
    from colorama import init
    from ppSimulatorUI import Ui_MainWindow
    from graphCreator import GraphCreator
    from protocolCreator import ProtocolCreator
    from PyQt5 import QtCore, QtGui, QtWidgets
    from dialogs.warnings import warnings, showDialog
    from util_lib.utilityYml import getYmlDict, getYmlString
    from util_lib.utilityDict import dictToObj
    from protocol import Protocol
    from validator import SwitchPpG
    import yaml
    import settings as st
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

if platform.system() == "Windows":
    init()

dir_path = os.path.dirname(os.path.realpath(__file__))
protocolAttrChecker = ["name", "protocolType", "input", "states", "output", "inputFunction", "statesFunction", "outputFunction"]
graphAttrChecker = ["name", "numberNodes", "agent"]

class PpSimulator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PpSimulator, self).__init__()
        self.setupUi(self)

        self.txtPathResult_Single.setText(st._resultDir)

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

    def btnGraphFromFile_Single_on_click(self):
        pathToProtocol = self.txtPathProtocol.text()
        if pathToProtocol.strip() == "":
            showDialog("NoProtocol")
            return
        objProtocol = dictToObj(Protocol, getYmlDict(pathToProtocol))

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', st._graphDir, '*.yml')
        grStatYml = getYmlDict(fileName)
        agents = grStatYml.pop("agent", None)
        grStatYml['agentStatistic'] =  OrderedDict(Counter(agents))
        data = getYmlString(grStatYml)
        self.txtPathGraph_Single.setText(fileName)
        self.txtInfoGraph_Single.setText(data)

    def btnProtocolCreate_on_click(self):
        self.PC = ProtocolCreator()
        self.PC.setWindowModality(QtCore.Qt.ApplicationModal)
        self.PC.show()
        self.conTxtInfoP(self.PC)
        self.conTxtPathP(self.PC)

    def btnProtocolFromFile_on_click(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', st._protocolDir, '*.yml')
        self.txtPathProtocol.setText(fileName)
        with open(fileName, 'r') as pFile:
            self.txtInfoProtocol.setText("".join(pFile.readlines()))

    def btnBrowse_Single_on_click(self):
        dialog = QtWidgets.QFileDialog(self, 'Directory', st._appDir)
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        dir = str(dialog.getExistingDirectory())
        self.txtPathResult_Single.setText(dir)

    def btnClear_Single_on_click(self):
        self.txtPathGraph_Single.clear()
        self.txtInfoGraph_Single.clear()
        self.txtFileNameResult_Singel.clear()
        self.txtPathResult_Single.clear()
        self.txtNumberRepetitions_Single.clear()

    def btnStart_Single_on_click(self):
        if not (self.validateGraph(self.txtPathGraph_Single.text()) and self.validateProtocol(self.txtPathProtocol.text())):
            print("cos poszlo nie tak")

    def btnYAMLCreate_Multi_on_click(self):
        pass

    def btnYAMLFromFile_Multi_on_click(self):
        pass

    def btnAdd_Multi_on_click(self):
        pass

    def btnRemove_Multi_on_click(self):
        pass

    def btnClear_Multi_on_click(self):
        pass

    def btnSave_Multi_on_click(self):
        pass

    def btnBrowse_Multi_on_click(self):
        pass

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


        @param protocolWindow   : Population protocol window
        @return                 : None
        """
        protocolWindow.infoPToMain.connect(self.txtInfoProtocol_setText)

    def conTxtPathP(self, protocolWindow):
        """


        @param protocolWindow   : Population protocol window
        @return                 : None
        """
        protocolWindow.pathPToMain.connect(self.txtPathProtocol_setText)

    def conTxtPathG(self, graphWindow):
        """


        @param graphWindow  : Graph creator window
        @return             : None
        """
        graphWindow.pathGToMain.connect(self.txtPathGraph_setText)

    def conTxtInfoG(self, graphWindow):
        """


        @param graphWindow  : Graph creator window
        @return             : None
        """
        graphWindow.infoGToMain.connect(self.txtInfoGraph_setText)

    def validateProtocol(self, pathFile):
        """
        Validate protocol file in terms of attributes.

        @param pathFile : Path to protocol file
        @return         : True if protocol is correct False otherwise
        """
        protocolValid = True
        try:
            ppObj = getYmlDict(pathFile)
            printBrightGreen("======Validate protocol population======")
            for attr in protocolAttrChecker:
                if SwitchPpG.switchCase(attr)(ppObj):
                    printBrightGreen("attr: (VALID)")
                else:
                    printBrightGreen("attr: (NOT VALID)")
                    protocolValid = False
        except yaml.scanner.ScannerError as error:
            printRed(error)
            return False
        return protocolValid

    def validateGraph(self, pathFile):
        """
        Validate graph file in terms of attributes.

        :param pathFile : Path to graph file
        :return         : True if graph is correct False otherwise
        """
        graphValid = True
        try:
            ppObj = getYmlDict(pathFile)
            printBrightGreen("======Validate graph======")
            for attr in graphAttrChecker:
                if SwitchPpG.switchCase(attr)(ppObj):
                    printBrightGreen("attr: (VALID)")
                else:
                    printBrightGreen("attr: (NOT VALID)")
                    graphValid = False
        except yaml.scanner.ScannerError as error:
            printRed(error)
            return False
        return graphValid

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