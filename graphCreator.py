import sys
import random as r
from collections import OrderedDict

try:
    from util_lib.utilityPrint import printRed, disableEnablePrint
    import settings as st
    from GraphCreatorUI import Ui_GraphCreator
    from PyQt5 import QtGui, QtWidgets, QtCore
    from PyQt5.QtCore import QRegExp, Qt
    from PyQt5.QtWidgets import QAbstractItemView
    from dialogs.warnings import warnings, showDialog
    from util_lib.utilityDict import ObjectDict
    from util_lib.utilityYml import createYmlFile, getYmlString
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

class Graph(ObjectDict):
    pass

class GraphCreator(QtWidgets.QMainWindow, Ui_GraphCreator):
    pathGToMain = QtCore.pyqtSignal(str)
    infoGToMain = QtCore.pyqtSignal(str)

    def __init__(self, listItems):
        super().__init__()
        self.setupUi(self)
        self.listItems = sorted(listItems)
        self.cmbBxInputAlphabet.addItems(self.listItems)
        self.checkBxIfRandom.stateChanged.connect(self.randomGraph)
        self.checkBxIfRandom.setChecked(True)
        self.txtBxNumberOfNodes.setReadOnly(False)
        rx = QRegExp('^[1-9]\d{3}$')
        self.txtBxNumberOfNodes.setValidator(QtGui.QRegExpValidator(rx))
        self.listWidget_node.setColumnWidth(0,70)
        self.listWidget_node.setColumnWidth(1,122)
        self.listWidget_node.verticalHeader().setDefaultSectionSize(18)

        self.btnAdd.clicked.connect(self.btnAdd_click)
        self.btnRemove.clicked.connect(self.btnRemove_click)
        self.btnOk.clicked.connect(self.btnOk_click)

#  region Method button on click
    def btnAdd_click(self):
        input = self.cmbBxInputAlphabet.currentText()
        nbSymbol = self.txtBxNumberOfSymbol.text()
        inputItem = QtWidgets.QTableWidgetItem(input)
        inputItem.setTextAlignment(Qt.AlignHCenter + Qt.AlignVCenter)
        nbSymbolItem = QtWidgets.QTableWidgetItem(nbSymbol)
        nbSymbolItem.setTextAlignment(Qt.AlignHCenter + Qt.AlignVCenter)
        rowPosition = self.listWidget_node.rowCount()

        for i in range(rowPosition):
            if self.listWidget_node.item(i, 0).text() == input:
                self.listWidget_node.setItem(i, 0, inputItem)
                self.listWidget_node.setItem(i, 1, nbSymbolItem)
                return

        self.listWidget_node.insertRow(rowPosition)
        self.listWidget_node.setItem(rowPosition, 0, inputItem)
        self.listWidget_node.setItem(rowPosition, 1, nbSymbolItem)

        self.listWidget_node.sortItems(0, Qt.AscendingOrder)


    def btnRemove_click(self):
        self.listWidget_node.removeRow(self.listWidget_node.currentRow())

    def btnOk_click(self):

        if self.checkBxIfRandom.isChecked():
            try:
                numberOfNodes = int(self.txtBxNumberOfNodes.text())
            except ValueError:
                showDialog("NoNbNodes")
                return

            if numberOfNodes > 1:
                listNodesForInput = self.generateValuesSumTo(numberOfNodes, len(self.listItems))
                agentList = []
                agentStatistic = OrderedDict()
                for index, value in enumerate(listNodesForInput):
                    agentList += [self.listItems[index] for i in range(value)]
                    agentStatistic[self.listItems[index]] = value

                self.createGraph(numberOfNodes, agentList, agentStatistic)
            else:
                showDialog("LowNBNodes")
                return
        else:
            rowCount = self.listWidget_node.rowCount()
            if rowCount == 0:
                showDialog("NoSymbol")
            else:
                columnCount = self.listWidget_node.columnCount()
                qTableItems = []
                for i in range(rowCount):
                    qTableItems.append([int(self.listWidget_node.item(i, j).text()) if j==1 else self.listWidget_node.item(i, j).text() for j in range(columnCount)])

                agentList = [qTableItem[0] for qTableItem in qTableItems for i in range(qTableItem[1])]
                numberOfNodes = sum([int(qItem[1]) for qItem in qTableItems])
                agentStatistic = OrderedDict(qTableItems)

                self.createGraph(numberOfNodes, agentList, agentStatistic)

    def btnClear_click(self):
        self.listWidget_node.clear()
        self.txtBxNumberOfSymbol.clear()
        self.txtBxNumberOfNodes.clear()
# endregion
    def createGraph(self, nodes, agentsList, agentStatistic):
        """
        Create yml graph and emit path with data to main window

        @param nodes            : Entire number of nodes in graph
        @param agentsList       : List of agents
        @param agentStatistic   : Statistic of each agent
        @return                 : None
        """
        graphName = self.createName(nodes, agentStatistic)
        nameGroup = ("name", graphName)
        nodeGroup = ("numberNodes", nodes)
        agentGroup = ("agent", agentsList)
        grYml = OrderedDict([nameGroup, nodeGroup, agentGroup])

        agentStatisticGroup = ("agentStatistic", agentStatistic)

        grStatYml = OrderedDict([nameGroup, nodeGroup, agentStatisticGroup])
        createYmlFile(graphName, grYml, st._graphDir)
        data = getYmlString(grStatYml)
        graphFilePath = "\\".join([st._graphDir, graphName + ".yml"])

        self.pathGToMain.emit(graphFilePath)
        self.infoGToMain.emit(data)
        self.close()

    def createName(self, nodes, agentsStatistic):
        """
        Create graph name based on argument.

        @param nodes                : Entire number of nodes in graph
        @param agentsStatistic      : Statistic of each agent
        @return                     : Graph name
        """
        graphName = "graph_{}nodes".format(nodes)
        for key, value in agentsStatistic.items():
            graphName += "_{}{}".format(value, key)

        return graphName

    def generateValuesSumTo(self, N, numValues):
        """
        Generate list of values of which sum is N.

        @param N        : Sum
        @param numValue : len of returned list
        @return         : list of values
        """
        listValues = []
        while numValues != 1:
            listValues.append(r.randint(0, N))
            N = N - listValues[-1]
            numValues -= 1

        return listValues + [N]

    def randomGraph(self):
        """
        Enable generating random graph if checkBxIfRandom is checked otherwise disable.

        @return : None
        """
        if self.checkBxIfRandom.isChecked():
            self.groupBxDefineGraph.setDisabled(True)
            self.txtBxNumberOfNodes.setReadOnly(False)
        else:
            self.groupBxDefineGraph.setDisabled(False)
            self.txtBxNumberOfNodes.setReadOnly(True)


if __name__ == "__main__":
    pass
    #TODO: add https://forum.qt.io/topic/9171/solved-how-can-a-lineedit-accept-only-ascii-alphanumeric-character-required-a-z-a-z-0-9/8