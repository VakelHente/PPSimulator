import os
import sys
import platform
import errno
from collections import OrderedDict

try:
    import settings
    from colorama import init
    from util_lib.utilityPrint import printRed
    from util_lib.utilityPrint import printYellow
    from util_lib.utilityPrint import printBrightGreen
    from util_lib.utilityPrint import getBrightGreenString
    from util_lib.utilityReader import processCommand
    from util_lib.utilityYml import createYmlFile
except ImportError as error:
    printRed(error)
    sys.exit(settings.ErrorCode.ERROR_IMPORT)

if platform.system() == "Windows":
    init()

listUiFiles = ["GraphCreator", "ppSimulator", "ProtocolCreator", "warningDialog"]
UiDialog    = "warningDialog"
listFolders = ["protocol", "graph", "result"]
configFile  = "settings"

currentFilePath = os.path.dirname(os.path.realpath(__file__))
errorCounter = 0
NO_ERROR = 0

def setUp():
    """
    Create necessary window-python files and folders tree for application

    @return: None
    """
    global errorCounter
    printYellow("=" * 40)
    for uiFile in listUiFiles:
        printYellow("-I- Create {}UI.py file".format(uiFile))

        if uiFile == listUiFiles[-1]:
            command = "pyuic5 -x dialogs/{0}.ui -o dialogs/{0}UI.py".format(uiFile)
        else:
            command = "pyuic5 -x {0}.ui -o {0}UI.py".format(uiFile)

        if processCommand(command, currentFilePath):
            printYellow("-I- File {}UI.py was created\n".format(uiFile))
        else:
            printRed("-E- File {}UI.py was not created\n".format(uiFile))
            errorCounter += 1

    printYellow("="*40)

    for folder in listFolders:
        printYellow("-I- Create {} folder".format(folder))

        if os.path.isdir("\\".join([currentFilePath,folder])):
            printYellow("-I- Folder {} already exists\n".format(folder))
            continue

        command = "mkdir {}".format(folder)

        if processCommand(command, currentFilePath):
            printYellow("-I- Folder {} was created\n".format(folder))
        else:
            printRed("-E- Folder {} was not created\n".format(folder))
            errorCounter += 1

    if (errorCounter == NO_ERROR):
        printYellow("\n-I- Script finished successfully")
    else:
        printRed("\n-E- Script finished with failure")

    createSettings(configFile)
    input(getBrightGreenString("Press Enter to continue..."))

def silentRemoveFile(file, ext="yml"):
    """
    Remove provided file without any message. If There is different exception than "no such file or directory" raise it.

    @return : None
    """
    try:
        os.remove("{}.{}".format(file,ext))
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise e

def createSettings(name):
    """
    Create configuration file which contain directory to graph, protocol and result. Also contain setup later features.

    @name   : name of configuration file
    @return : None
    """
    silentRemoveFile(name)
    orderedConfig = OrderedDict([("name", "settings"), ("directories", OrderedDict([(elem, "\\".join([currentFilePath,elem])) for elem in listFolders]))])
    createYmlFile(name, orderedConfig, currentFilePath)

if __name__ == "__main__":
    setUp()