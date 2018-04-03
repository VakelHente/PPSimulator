from subprocess import Popen
import os

listUiFiles = ["GraphCreator", "MainWindow", "ProtocolCreator"]
dir_path = os.path.dirname(os.path.realpath(__file__))
errorCounter = 0
NO_ERROR = 0

def main():
    global errorCounter
    for uiFile in listUiFiles:
        print("-I- Create {}.py file".format(uiFile))
        command = "pyuic5 {0}.ui -o {0}UI.py".format(uiFile)
        process = Popen(command, cwd=dir_path)
        stdout, stderr = process.communicate()
        if stdout or stderr:
            print("-E- {}".format(stdout))
            print("-E- {}".format(stderr))
            errorCounter += 1
        else:
            print("-I- File {}.py finished successfully")

    if(errorCounter == NO_ERROR):
        print("-I- Script finished successfully")
    else:
        print("-E- Script finished with failure")

if __name__ == "__main__":
    main()