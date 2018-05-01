import sys

try:
    from util_lib.utilityPrint import printRed
    import settings as st
    from dialogs.warningDialogUI import Ui_warningDialog
    from PyQt5 import QtWidgets
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

warnings = {
    "emptyPName"            : "No protocol name.",
    "noExt"                 : "Provide protocol name without extension.",
    "LW_input"              : "No input alphabet.",
    "LW_states"             : "No states.",
    "LW_output"             : "No output alphabet.",
    "LW_inputFunction"      : "No input function.",
    "LW_statesFunction"     : "No states function.",
    "LW_outputFunction"     : "No output function.",
    "LowNBNodes"            : "Number of nodes must be at least 2.",
    "NoProtocol"            : "No protocol selected.",
    "NoSymbol"              : "No symbol added.",
    "NoNbNodes"             : "No number of nodes."
}

def showDialog(key):
    """
    Show dialog with provided key to warnings dict.

    @param key  : key to warnings dict
    @return     : None
    """
    warningDialog = QtWidgets.QDialog()
    warningDialog.ui = Ui_warningDialog()
    warningDialog.ui.setupUi(warningDialog)
    warningDialog.ui.label_warningMessage.setText(warnings[key])
    warningDialog.exec_()