import os
import sys
import platform

try:
    import settings
    from colorama import init
    from util_lib.utilityPrint import printRed
    from util_lib.utilityPrint import printYellow
    from util_lib.utilityPrint import printBrightGreen
    from util_lib.utilityPrint import getBrightGreenString
    from util_lib.utilityReader import processCommand
except ImportError as error:
    printRed(error)
    sys.exit(settings.ErrorCode.ERROR_IMPORT)

if platform.system() == "Windows":
    init()

listUiFiles = ["GraphCreator", "ppSimulator", "ProtocolCreator"]
listFolders = ["protocol", "graph", "result"]

dir_path = os.path.dirname(os.path.realpath(__file__))
errorCounter = 0
NO_ERROR = 0

def setUp():
    """
    Create necessary window-python files and folders tree for application

    @return: None
    """
    global errorCounter
    for uiFile in listUiFiles:
        printYellow("-I- Create {}.py file".format(uiFile))
        command = "pyuic5 -x {0}.ui -o {0}UI.py".format(uiFile)
        if processCommand(command, dir_path):
            printYellow("-I- File {}UI.py was created".format(uiFile))
        else:
            errorCounter += 1

    printYellow("="*40)

    for folder in listFolders:
        printYellow("-I- Create {} folder".format(folder))
        command = "mkdir {}".format(folder)

        if processCommand(command, dir_path):
            printYellow("-I- Folder {} was created".format(folder))
        else:
            errorCounter += 1

    if (errorCounter == NO_ERROR):
        printYellow("\n-I- Script finished successfully")
    else:
        printRed("\n-E- Script finished with failure")

    input(getBrightGreenString("Press Enter to continue..."))

if __name__ == "__main__":
    if platform.system() == "Windows":
        init()

    setUp()