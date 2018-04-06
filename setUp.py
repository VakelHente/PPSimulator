import os
import sys
from subprocess import check_call, PIPE, call, Popen

try:
    import settings
    from util_lib.utilityPrint import printRed
    from util_lib.utilityReader import processCommand
except ImportError as error:
    printRed(error)
    sys.exit(settings.ErrorCode.ERROR_IMPORT)

listUiFiles = ["GraphCreator", "ppSimulator", "ProtocolCreator"]
dir_path = os.path.dirname(os.path.realpath(__file__))
errorCounter = 0
NO_ERROR = 0

def main():
    global errorCounter
    for uiFile in listUiFiles:
        print("-I- Create {}.py file".format(uiFile))
        command = "pyuic5 {0}.ui -o {0}UI.py".format(uiFile)
        if processCommand(command, dir_path):
            print("-I- File {}UI.py was created".format(uiFile))
        else:
            errorCounter += 1

    if(errorCounter == NO_ERROR):
        print("\n-I- Script finished successfully")
    else:
        print("\n-E- Script finished with failure")

if __name__ == "__main__":
    main()