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
        GraphCreator(self.graphCreator)
        self.graphCreator.setWindowModality(QtCore.Qt.ApplicationModal)
        self.graphCreator.show()

    @QtCore.pyqtSlot()
    def btnGraphFromFile_Single_on_click(self):
        pass

    @QtCore.pyqtSlot()
    def btnProtocolCreate_on_click(self):
        self.PC = ProtocolCreator()
        self.PC.setWindowModality(QtCore.Qt.ApplicationModal)
        self.PC.show()

    @QtCore.pyqtSlot()
    def btnProtocolFromFile_on_click(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', dir_path, '*.txt')

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
    app = QtWidgets.QApplication(sys.argv)
    window = PpSimulator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="POPULATION PROTOCOL SIMULATOR")
    parser._action_groups.pop()
    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--debug', dest='feature', action='store_true')
    feature_parser.add_argument('--no-debug', dest='feature', action='store_false')
    parser.set_defaults(feature=False)

    disableEnablePrint(parser.parse_args().feature)
    main()